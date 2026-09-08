import re
from django import forms
from .models import ContactEnquiry, QuoteRequest


PHONE_REGEX = re.compile(r'^(\+?\d{1,4}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?[\d\s\-]{7,12}$')


class ContactEnquiryForm(forms.ModelForm):
    """
    Form for general inquiries, service queries, and customer reach-outs.
    """
    class Meta:
        model = ContactEnquiry
        fields = ['name', 'phone', 'email', 'company', 'city', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name *',
                'required': True,
                'autocomplete': 'name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone / Mobile Number *',
                'required': True,
                'autocomplete': 'tel',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address *',
                'required': True,
                'autocomplete': 'email',
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company / Firm Name (Optional)',
                'autocomplete': 'organization',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City / Location *',
                'required': True,
                'autocomplete': 'address-level2',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject / Elevator Model of Interest',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about your requirements, building type, stops or questions...',
                'required': True,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError("Please provide a valid full name (minimum 2 characters).")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits_only = re.sub(r'\D', '', phone)
        if len(digits_only) < 10:
            raise forms.ValidationError("Please enter a valid phone number with at least 10 digits.")
        if len(digits_only) > 15:
            raise forms.ValidationError("Phone number cannot exceed 15 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise forms.ValidationError("Please provide a valid email address.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 5:
            raise forms.ValidationError("Please provide a brief message describing your elevator requirement (minimum 5 characters).")
        return message


class QuoteRequestForm(forms.ModelForm):
    """
    Detailed engineering quotation request form.
    """
    class Meta:
        model = QuoteRequest
        fields = [
            'customer_name', 'company_name', 'phone', 'email',
            'city', 'project_location', 'building_type', 'elevator_type',
            'number_of_floors', 'capacity_required', 'number_of_elevators',
            'project_stage', 'message'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contact Person Full Name *',
                'required': True,
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Developer / Architecture Firm / Entity',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+91 98765 43210 *',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@company.com (For Official Quotation PDF) *',
                'required': True,
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Ahmedabad, Mumbai, Surat, Pune *',
                'required': True,
            }),
            'project_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Site Locality or Project Address (e.g. Bodakdev, SG Highway)',
            }),
            'building_type': forms.Select(attrs={
                'class': 'form-select',
                'required': True,
            }),
            'elevator_type': forms.Select(attrs={
                'class': 'form-select',
                'required': True,
            }),
            'number_of_floors': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. G+4 Floors, 12 Stops, Ground + 2 *',
                'required': True,
            }),
            'capacity_required': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 8 Passengers / 544 kg, 1000 kg Stretcher, 2 Ton Goods',
            }),
            'number_of_elevators': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'value': 1,
                'required': True,
            }),
            'project_stage': forms.Select(attrs={
                'class': 'form-select',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Specify any shaft dimensions, cabin finishes (Titanium Gold, SS Hairline, Panoramic Glass), door speed, or custom requirements...',
            }),
        }

    def clean_customer_name(self):
        name = self.cleaned_data.get('customer_name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError("Please enter a valid customer contact name.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        digits_only = re.sub(r'\D', '', phone)
        if len(digits_only) < 10:
            raise forms.ValidationError("Please enter a valid telephone / mobile number (minimum 10 digits).")
        if len(digits_only) > 15:
            raise forms.ValidationError("Phone number cannot exceed 15 digits.")
        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise forms.ValidationError("Please provide a valid email address for receiving quotes.")
        return email

    def clean_number_of_elevators(self):
        units = self.cleaned_data.get('number_of_elevators')
        if units is None or units < 1:
            raise forms.ValidationError("Number of elevators must be at least 1.")
        return units

    def clean_number_of_floors(self):
        floors = self.cleaned_data.get('number_of_floors', '').strip()
        if not floors:
            raise forms.ValidationError("Please specify the number of floors or stops (e.g. G+4 Floors).")
        return floors

