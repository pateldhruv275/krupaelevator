from django.test import TestCase, Client
from django.urls import reverse
from projects.models import Project, ProjectImage


class ProjectsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Project 1: Residential in Mumbai, Passenger Lift
        self.project1 = Project.objects.create(
            title="Skyline Regency Luxury Tower",
            slug="skyline-regency-luxury-tower",
            client_name="Skyline Developers",
            city="Mumbai",
            location="Worli, Mumbai",
            project_type="Residential",
            elevator_type="Passenger Elevator",
            number_of_elevators=4,
            description="Complete engineering and installation of 4 duplex gearless elevators.",
            featured=True,
            active=True
        )

        # Project 2: Commercial in Pune, Glass / Panoramic
        self.project2 = Project.objects.create(
            title="TechPark Central Tower",
            slug="techpark-central-tower",
            client_name="InfraTech Corp",
            city="Pune",
            location="Hinjewadi, Pune",
            project_type="Commercial",
            elevator_type="Panoramic Glass Elevator",
            number_of_elevators=6,
            description="Curved panoramic glass elevators facing the central atrium.",
            featured=True,
            active=True
        )

        # Project 3: Healthcare in Ahmedabad, Hospital Bed Lift
        self.project3 = Project.objects.create(
            title="Sterling Multispeciality Hospital",
            slug="sterling-multispeciality-hospital",
            client_name="Sterling Healthcare",
            city="Ahmedabad",
            location="Bopal, Ahmedabad",
            project_type="Healthcare",
            elevator_type="Hospital Stretcher Elevator",
            number_of_elevators=3,
            description="Equipped with automatic rescue device, antibacterial walls and priority call logic.",
            featured=False,
            active=True
        )

        # Inactive Project
        self.project_inactive = Project.objects.create(
            title="Private Villa Lift",
            slug="private-villa-lift",
            city="Goa",
            location="Panjim, Goa",
            project_type="Residential",
            elevator_type="Home / Villa Elevator",
            number_of_elevators=1,
            description="Draft project",
            active=False
        )

        # Project Image
        self.p1_img = ProjectImage.objects.create(
            project=self.project1,
            caption="Skyline Lobby Entrance",
            display_order=1
        )

    def test_project_model_str_and_properties(self):
        self.assertEqual(str(self.project1), "Skyline Regency Luxury Tower - Mumbai")
        self.assertIn("Skyline Regency Luxury Tower", str(self.p1_img))
        self.assertEqual(self.project1.get_absolute_url(), reverse('projects:detail', kwargs={'slug': self.project1.slug}))

    def test_project_list_view(self):
        response = self.client.get(reverse('projects:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_list.html')
        self.assertEqual(len(response.context['projects']), 3)
        self.assertIn("Mumbai", response.context['available_cities'])
        self.assertIn("Pune", response.context['available_cities'])
        self.assertIn("Ahmedabad", response.context['available_cities'])
        self.assertContains(response, "Skyline Regency")
        self.assertContains(response, "TechPark Central Tower")
        self.assertContains(response, "Sterling Multispeciality Hospital")
        self.assertNotContains(response, "Private Villa Lift")

    def test_filter_by_city(self):
        response = self.client.get(reverse('projects:list'), {'city': 'Mumbai'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['projects']), 1)
        self.assertEqual(response.context['projects'][0], self.project1)
        self.assertContains(response, "Skyline Regency")
        self.assertNotContains(response, "TechPark Central")

    def test_filter_by_project_type(self):
        response = self.client.get(reverse('projects:list'), {'project_type': 'Commercial'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['projects']), 1)
        self.assertEqual(response.context['projects'][0], self.project2)
        self.assertContains(response, "TechPark Central Tower")
        self.assertNotContains(response, "Skyline Regency")

    def test_filter_by_elevator_type(self):
        response = self.client.get(reverse('projects:list'), {'elevator_type': 'Hospital Stretcher Elevator'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['projects']), 1)
        self.assertEqual(response.context['projects'][0], self.project3)
        self.assertContains(response, "Sterling Multispeciality Hospital")
        self.assertNotContains(response, "Skyline Regency")

    def test_filter_by_search_query(self):
        response = self.client.get(reverse('projects:list'), {'q': 'InfraTech'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['projects']), 1)
        self.assertEqual(response.context['projects'][0], self.project2)

    def test_combined_filters(self):
        response = self.client.get(reverse('projects:list'), {
            'city': 'Mumbai',
            'project_type': 'Residential',
            'elevator_type': 'Passenger Elevator'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['projects']), 1)
        self.assertEqual(response.context['projects'][0], self.project1)

    def test_project_detail_view(self):
        response = self.client.get(reverse('projects:detail', kwargs={'slug': self.project1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'projects/project_detail.html')
        self.assertEqual(response.context['project'], self.project1)
        self.assertContains(response, "Skyline Regency Luxury Tower")
        self.assertContains(response, "Worli, Mumbai")
        self.assertContains(response, "4 Units Commissioned")

    def test_project_detail_404_on_inactive(self):
        response = self.client.get(reverse('projects:detail', kwargs={'slug': self.project_inactive.slug}))
        self.assertEqual(response.status_code, 404)

