from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from enquiries.models import ContactEnquiry, QuoteRequest
from enquiries.forms import ContactEnquiryForm, QuoteRequestForm


class EnquiriesTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='testadmin',
            email='admin@test.com',
            password='Password123!'
        )

    # -------------------------------------------------------------
    # 1. Model Tests
    # -------------------------------------------------------------
    def test_contact_enquiry_model(self):
        enquiry = ContactEnquiry.objects.create(
            name="Rohan Joshi",
            phone="+91 98980 12345",
            email="rohan@example.com",
            city="Ahmedabad",
            subject="Elevator AMC Query",
            message="Need AMC quote for 2 residential lifts."
        )
        self.assertEqual(enquiry.status, 'New')
        self.assertIn("Rohan Joshi", str(enquiry))
        self.assertIn("Ahmedabad", str(enquiry))
        self.assertIn("[New]", str(enquiry))

    def test_quote_request_model(self):
        quote = QuoteRequest.objects.create(
            customer_name="Sunil Agarwal",
            company_name="Agarwal Builders",
            phone="+91 98251 98765",
            email="sunil@agarwalbuilders.com",
            city="Surat",
            building_type="Commercial / Corporate Office",
            elevator_type="Passenger Elevator",
            number_of_floors="G+8 Floors",
            capacity_required="10 Passengers / 680 kg",
            number_of_elevators=2
        )
        self.assertEqual(quote.status, 'New')
        self.assertIn("Sunil Agarwal", str(quote))
        self.assertIn("Passenger Elevator", str(quote))
        self.assertIn("Surat", str(quote))

    # -------------------------------------------------------------
    # 2. Form Validation Tests
    # -------------------------------------------------------------
    def test_contact_enquiry_form_valid(self):
        form_data = {
            'name': 'Pooja Verma',
            'phone': '+91 99887 76655',
            'email': 'pooja@verma.com',
            'company': 'Verma Hospital',
            'city': 'Pune',
            'subject': 'Bed Lift Inquiry',
            'message': 'Please share brochure and quote for hospital stretcher elevator.'
        }
        form = ContactEnquiryForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_contact_enquiry_form_invalid_phone(self):
        form_data = {
            'name': 'Pooja Verma',
            'phone': '123',  # Too short
            'email': 'pooja@verma.com',
            'city': 'Pune',
            'message': 'Test inquiry message.'
        }
        form = ContactEnquiryForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone', form.errors)

    def test_contact_enquiry_form_invalid_email(self):
        form_data = {
            'name': 'Pooja Verma',
            'phone': '+91 99887 76655',
            'email': 'not-an-email',
            'city': 'Pune',
            'message': 'Valid message here.'
        }
        form = ContactEnquiryForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_quote_request_form_valid(self):
        form_data = {
            'customer_name': 'Karan Malhotra',
            'company_name': 'Malhotra Corp',
            'phone': '+91 98765 43210',
            'email': 'karan@malhotra.com',
            'city': 'Mumbai',
            'project_location': 'Worli',
            'building_type': 'Residential Apartment',
            'elevator_type': 'Passenger Elevator',
            'number_of_floors': 'G+12 Floors',
            'capacity_required': '8 Passengers / 544 kg',
            'number_of_elevators': 2,
            'project_stage': 'Civil Construction Ongoing',
            'message': 'Need high-speed gearless PMSM elevators.'
        }
        form = QuoteRequestForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_quote_request_form_invalid_units(self):
        form_data = {
            'customer_name': 'Karan Malhotra',
            'phone': '+91 98765 43210',
            'email': 'karan@malhotra.com',
            'city': 'Mumbai',
            'building_type': 'Residential Apartment',
            'elevator_type': 'Passenger Elevator',
            'number_of_floors': 'G+12',
            'number_of_elevators': 0,  # Invalid: cannot be 0
        }
        form = QuoteRequestForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('number_of_elevators', form.errors)

    # -------------------------------------------------------------
    # 3. View Tests: Quote Request
    # -------------------------------------------------------------
    def test_quote_request_get_view(self):
        response = self.client.get(reverse('enquiries:quote_request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'enquiries/quote_request.html')
        self.assertContains(response, "Request An Elevator Quotation")

    def test_quote_request_get_with_prefilled_type(self):
        response = self.client.get(reverse('enquiries:quote_request'), {'elevator_type': 'Panoramic Glass Elevator'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].initial.get('elevator_type'), 'Panoramic Glass Elevator')

    def test_quote_request_post_valid(self):
        post_data = {
            'customer_name': 'Nilesh Patel',
            'company_name': 'Patel Heights',
            'phone': '+91 98981 23456',
            'email': 'nilesh@patelheights.com',
            'city': 'Ahmedabad',
            'project_location': 'Bopal',
            'building_type': 'Residential Apartment',
            'elevator_type': 'Passenger Elevator',
            'number_of_floors': 'G+7 Floors',
            'capacity_required': '6 Passengers / 408 kg',
            'number_of_elevators': 2,
            'project_stage': 'Civil Hoistway Ready',
            'message': 'Looking for immediate quotation.'
        }
        response = self.client.post(reverse('enquiries:quote_request'), post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(QuoteRequest.objects.count(), 1)
        created_quote = QuoteRequest.objects.first()
        self.assertEqual(created_quote.customer_name, 'Nilesh Patel')
        self.assertEqual(created_quote.status, 'New')
        self.assertContains(response, "Your quotation request for 2 Passenger Elevator unit(s) has been successfully registered")

    def test_quote_request_post_invalid(self):
        post_data = {
            'customer_name': 'Nilesh Patel',
            # missing phone, email, city, building_type, etc.
        }
        response = self.client.post(reverse('enquiries:quote_request'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(QuoteRequest.objects.count(), 0)
        self.assertContains(response, "There was an error in your submission")

    # -------------------------------------------------------------
    # 4. View Tests: Contact Us
    # -------------------------------------------------------------
    def test_contact_get_view(self):
        response = self.client.get(reverse('enquiries:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'enquiries/contact.html')
        self.assertContains(response, "Get In Touch With Krupa Elevator")
        self.assertContains(response, "Corporate Office &amp; Factory")

    def test_contact_post_valid(self):
        post_data = {
            'name': 'Hitesh Dave',
            'phone': '+91 98240 55443',
            'email': 'hitesh@dave.com',
            'company': 'Dave Enterprises',
            'city': 'Surat',
            'subject': 'Modernization',
            'message': 'We want to replace old hydraulic lift with MRL elevator.'
        }
        response = self.client.post(reverse('enquiries:contact'), post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactEnquiry.objects.count(), 1)
        enquiry = ContactEnquiry.objects.first()
        self.assertEqual(enquiry.name, 'Hitesh Dave')
        self.assertEqual(enquiry.status, 'New')
        self.assertContains(response, "Your enquiry has been received")

    def test_contact_post_redirect_next(self):
        post_data = {
            'name': 'Gaurav Shah',
            'phone': '+91 98790 11223',
            'email': 'gaurav@shah.com',
            'city': 'Vadodara',
            'subject': 'General Query',
            'message': 'Inquiring about warranty period and AMC terms.',
            'next': '/'
        }
        response = self.client.post(reverse('enquiries:contact'), post_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    # -------------------------------------------------------------
    # 5. Admin Integration Tests
    # -------------------------------------------------------------
    def test_admin_changelist_accessible(self):
        self.client.force_login(self.admin_user)
        res_enquiry = self.client.get('/admin/enquiries/contactenquiry/')
        self.assertEqual(res_enquiry.status_code, 200)
        res_quote = self.client.get('/admin/enquiries/quoterequest/')
        self.assertEqual(res_quote.status_code, 200)
