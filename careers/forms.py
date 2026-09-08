import os
import re
from django import forms
from .models import JobApplication


class JobApplicationForm(forms.ModelForm):
    """
    Candidate job application form with secure resume file upload validation.
    """
    class Meta:
        model = JobApplication
        fields = [
            'applicant_name', 'email', 'phone', 'current_city',
            'years_of_experience', 'current_company', 'resume', 'cover_note'
        ]
        widgets = {
            'applicant_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name *',
                'required': True,
                'autocomplete': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address *',
                'required': True,
                'autocomplete': 'email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+91 98765 43210 *',
                'required': True,
                'autocomplete': 'tel',
            }),
            'current_city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Current City (e.g. Ahmedabad, Mumbai, Pune) *',
                'required': True,
            }),
            'years_of_experience': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 3.5 Years, Fresher *',
                'required': True,
            }),
            'current_company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Current Employer / Company (Optional)',
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx',
                'required': True,
            }),
            'cover_note': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Summarize your elevator industry experience, certifications, or key achievements...',
            }),
        }

    def clean_applicant_name(self):
        name = self.cleaned_data.get('applicant_name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError("Please provide your full name (minimum 2 characters).")
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

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if not resume:
            raise forms.ValidationError("Please upload your resume file.")

        # Check file extension
        ext = os.path.splitext(resume.name)[1].lower()
        allowed_extensions = ['.pdf', '.doc', '.docx']
        if ext not in allowed_extensions:
            raise forms.ValidationError("Invalid file type. Please upload a PDF or Microsoft Word (.doc, .docx) document.")

        # Check file size (5MB max)
        max_size = 5 * 1024 * 1024  # 5 MB
        if resume.size > max_size:
            raise forms.ValidationError(f"File size exceeds 5MB limit. Your file is {resume.size / (1024*1024):.1f}MB.")

        return resume

