from django.test import TestCase, Client as HttpClient
from django.urls import reverse
from core.models import SiteSettings, HeroSlider, Statistic, Feature, ProcessStep, Industry, Service, Client, Testimonial


class CoreModelsAndViewsTestCase(TestCase):
    def setUp(self):
        self.client = HttpClient()
        self.settings = SiteSettings.objects.create(
            company_name="KRUPA ELEVATOR",
            phone="+91 98765 43210",
            email="test@krupaelevator.com"
        )
        self.slide = HeroSlider.objects.create(
            title="Premium Elevators",
            subtitle="German Tech",
            display_order=1,
            active=True
        )
        self.stat = Statistic.objects.create(
            title="Years Experience",
            number="25",
            suffix="+",
            icon="bi-award",
            active=True
        )
        self.feature = Feature.objects.create(
            title="High Safety Standards",
            description="ISO certified",
            icon="bi-shield-check",
            active=True
        )
        self.step = ProcessStep.objects.create(
            step_number=1,
            title="Site Consultation",
            short_description="Initial analysis",
            active=True
        )
        self.industry = Industry.objects.create(
            name="Healthcare & Hospitals",
            description="Specialized bed elevators",
            active=True
        )
        self.service = Service.objects.create(
            title="Elevator Installation",
            slug="elevator-installation",
            short_description="Turnkey installation services",
            description="Detailed installation workflow...",
            icon="bi-gear-wide-connected",
            active=True
        )
        self.client_corp = Client.objects.create(
            name="Apex Towers",
            industry="Residential Complex",
            active=True
        )
        self.testimonial = Testimonial.objects.create(
            client_name="Hareshbhai Patel",
            client_title="Chairman",
            company="Skyline Heights",
            city="Ahmedabad",
            elevator_type_installed="Dual High-Speed MRL",
            rating=5,
            quote="Krupa Elevator installed two 13-passenger MRL elevators. Exceptional quality!",
            featured=True,
            active=True
        )

    def test_singleton_site_settings(self):
        second = SiteSettings.objects.create(company_name="Second Company")
        self.assertEqual(SiteSettings.objects.count(), 1)
        self.assertEqual(SiteSettings.get_settings().company_name, "Second Company")

    def test_models_str(self):
        self.assertEqual(str(self.slide), "Premium Elevators")
        self.assertIn("25+", str(self.stat))
        self.assertEqual(str(self.feature), "High Safety Standards")
        self.assertIn("Step 1", str(self.step))
        self.assertEqual(str(self.industry), "Healthcare & Hospitals")
        self.assertEqual(str(self.service), "Elevator Installation")
        self.assertEqual(str(self.client_corp), "Apex Towers")
        self.assertIn("Hareshbhai Patel", str(self.testimonial))
        self.assertEqual(len(self.testimonial.rating_range), 5)
        self.assertEqual(len(self.testimonial.empty_rating_range), 0)

    def test_homepage_view(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, "KRUPA ELEVATOR")
        self.assertContains(response, "Premium Elevators")
        self.assertContains(response, "High Safety Standards")
        self.assertContains(response, "Healthcare &amp; Hospitals")
        self.assertContains(response, "Elevator Installation")
        self.assertContains(response, "Hareshbhai Patel")
        self.assertContains(response, "Skyline Heights")
        self.assertIn('site_settings', response.context)
        self.assertIn('hero_slides', response.context)
        self.assertIn('statistics', response.context)
        self.assertIn('features', response.context)
        self.assertIn('process_steps', response.context)
        self.assertIn('industries', response.context)
        self.assertIn('services', response.context)
        self.assertIn('clients', response.context)
        self.assertIn('testimonials', response.context)

    def test_service_list_view(self):
        response = self.client.get(reverse('core:services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/service_list.html')
        self.assertContains(response, "Elevator Installation")
        self.assertContains(response, "Turnkey installation services")

    def test_service_detail_view(self):
        response = self.client.get(reverse('core:service_detail', kwargs={'slug': self.service.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/service_detail.html')
        self.assertContains(response, "Elevator Installation")
        self.assertContains(response, "Detailed installation workflow...")

    def test_service_detail_404(self):
        response = self.client.get(reverse('core:service_detail', kwargs={'slug': 'non-existent-service'}))
        self.assertEqual(response.status_code, 404)

    def test_client_list_view(self):
        response = self.client.get(reverse('core:clients'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/client_list.html')
        self.assertContains(response, "Apex Towers")
        self.assertContains(response, "Residential Complex")
