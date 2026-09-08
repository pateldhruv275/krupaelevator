from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from careers.models import JobOpening, JobApplication
from careers.forms import JobApplicationForm


class CareersAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.job1 = JobOpening.objects.create(
            title="Senior Elevator Erection Engineer",
            slug="senior-elevator-erection-engineer",
            department="Installation & Erection",
            location="Ahmedabad & Surat",
            employment_type="Full-Time Permanent",
            experience_required="4 - 7 Years",
            education="B.E. Mechanical",
            number_of_vacancies=3,
            description="Supervise field erection of traction and hydraulic lifts.",
            responsibilities="Oversee guide rail laser alignment\nSupervise installation crew\nConduct test drop runs",
            requirements="B.E. Mechanical / Electrical\n4+ years experience in lifts\nValid driving license",
            benefits="Competitive salary\nMilestone bonus\nHealth insurance",
            is_urgent=True,
            active=True
        )

        self.job2 = JobOpening.objects.create(
            title="AMC Service Technician",
            slug="amc-service-technician",
            department="Maintenance & AMC",
            location="Pune",
            employment_type="Full-Time Permanent",
            experience_required="2 - 4 Years",
            education="ITI Electrician",
            number_of_vacancies=2,
            description="Preventative maintenance and emergency breakdown calls.",
            responsibilities="Monthly 52-point inspection\nDoor header lubrication",
            requirements="ITI Wireman/Electrician\nTwo-wheeler license",
            benefits="Bonus and overtime\nPF/ESIC",
            is_urgent=False,
            active=True
        )

        self.inactive_job = JobOpening.objects.create(
            title="Archived Draft Role",
            slug="archived-draft-role",
            department="Administration & Accounts",
            location="Ahmedabad",
            description="Draft role not open to public.",
            responsibilities="None",
            requirements="None",
            active=False
        )

    def test_models_representation_and_helpers(self):
        self.assertIn("Senior Elevator Erection Engineer", str(self.job1))
        self.assertEqual(self.job1.get_absolute_url(), reverse('careers:detail', kwargs={'slug': 'senior-elevator-erection-engineer'}))
        self.assertEqual(len(self.job1.get_responsibilities_list()), 3)
        self.assertEqual(len(self.job1.get_requirements_list()), 3)
        self.assertEqual(len(self.job1.get_benefits_list()), 3)

    def test_careers_list_view(self):
        response = self.client.get(reverse('careers:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'careers/career_list.html')
        self.assertContains(response, "Senior Elevator Erection Engineer")
        self.assertContains(response, "AMC Service Technician")
        self.assertNotContains(response, "Archived Draft Role")
        self.assertIn('jobs', response.context)
        self.assertIn('available_departments', response.context)

    def test_careers_list_filter_by_department(self):
        response = self.client.get(reverse('careers:list'), {'department': 'Installation & Erection'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Senior Elevator Erection Engineer")
        self.assertNotContains(response, "AMC Service Technician")

    def test_career_detail_view_get(self):
        response = self.client.get(reverse('careers:detail', kwargs={'slug': self.job1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'careers/career_detail.html')
        self.assertContains(response, "Senior Elevator Erection Engineer")
        self.assertContains(response, "Supervise field erection")
        self.assertIn('form', response.context)

    def test_career_detail_404_on_invalid_or_inactive(self):
        response_404 = self.client.get(reverse('careers:detail', kwargs={'slug': 'non-existent-career'}))
        self.assertEqual(response_404.status_code, 404)

        response_inactive = self.client.get(reverse('careers:detail', kwargs={'slug': self.inactive_job.slug}))
        self.assertEqual(response_inactive.status_code, 404)

    def test_job_application_form_valid(self):
        resume_file = SimpleUploadedFile("resume.pdf", b"Dummy PDF file content", content_type="application/pdf")
        form_data = {
            'applicant_name': 'Ramesh Parmar',
            'email': 'ramesh@example.com',
            'phone': '+91 98765 11223',
            'current_city': 'Ahmedabad',
            'years_of_experience': '5 Years',
            'current_company': 'Gujarat Lift Works',
            'cover_note': 'Extensive experience in traction lifts.',
        }
        form_files = {'resume': resume_file}
        form = JobApplicationForm(data=form_data, files=form_files)
        self.assertTrue(form.is_valid(), form.errors)

    def test_job_application_form_invalid_extension(self):
        bad_file = SimpleUploadedFile("script.sh", b"echo 'hacked'", content_type="application/x-sh")
        form_data = {
            'applicant_name': 'Test Applicant',
            'email': 'test@example.com',
            'phone': '+91 98765 00000',
            'current_city': 'Mumbai',
            'years_of_experience': '2 Years',
        }
        form_files = {'resume': bad_file}
        form = JobApplicationForm(data=form_data, files=form_files)
        self.assertFalse(form.is_valid())
        self.assertIn('resume', form.errors)

    def test_career_detail_post_submission_success(self):
        resume_file = SimpleUploadedFile("my_cv.pdf", b"%PDF-1.4 dummy pdf resume content", content_type="application/pdf")
        post_data = {
            'applicant_name': 'Ketan Mehta',
            'email': 'ketan.mehta@example.com',
            'phone': '+91 98250 12345',
            'current_city': 'Ahmedabad',
            'years_of_experience': '6 Years',
            'current_company': 'Ketan Engineering Works',
            'cover_note': 'Interested in leading the erection team.',
            'resume': resume_file,
        }
        response = self.client.post(
            reverse('careers:detail', kwargs={'slug': self.job1.slug}),
            data=post_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)

        # Verify application created in DB
        application = JobApplication.objects.filter(applicant_name='Ketan Mehta', job=self.job1).first()
        self.assertIsNotNone(application)
        self.assertEqual(application.email, 'ketan.mehta@example.com')
        self.assertEqual(application.status, 'New')
        self.assertIn('Ketan Mehta', str(application))
