from django.db import models
from django.urls import reverse


class JobOpening(models.Model):
    """
    Career opportunities and engineering vacancies at Krupa Elevator works and branch offices.
    """
    DEPARTMENT_CHOICES = [
        ('Installation & Erection', 'Installation & Field Erection'),
        ('Maintenance & AMC', 'Service, AMC & Maintenance'),
        ('Engineering & Design', 'Engineering, Hoistway CAD & Design'),
        ('Quality & Safety Inspection', 'Quality Assurance & Safety Inspection'),
        ('Technical Sales & Estimation', 'Technical Sales & Estimation'),
        ('Manufacturing & Factory Operations', 'Manufacturing & Factory Operations'),
        ('Administration & Accounts', 'Corporate HR, Administration & Accounts'),
    ]

    EMPLOYMENT_CHOICES = [
        ('Full-Time Permanent', 'Full-Time Permanent'),
        ('Contractual', 'Contractual Project Basis'),
        ('Apprenticeship / Trainee', 'Apprenticeship / Graduate Trainee'),
    ]

    title = models.CharField(max_length=180, help_text="Job role title, e.g. 'Senior Elevator Installation Engineer'")
    slug = models.SlugField(max_length=200, unique=True, help_text="SEO URL slug")
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, db_index=True)
    location = models.CharField(max_length=120, help_text="Work location, e.g. 'Ahmedabad (GIDC Works)', 'Mumbai', 'Pune', 'Surat'")
    employment_type = models.CharField(max_length=60, choices=EMPLOYMENT_CHOICES, default='Full-Time Permanent')
    experience_required = models.CharField(max_length=80, help_text="e.g. '3 - 5 Years in Lift / Elevator Industry'")
    education = models.CharField(max_length=120, blank=True, help_text="e.g. 'ITI / Diploma / B.E. Mechanical or Electrical'")
    number_of_vacancies = models.PositiveIntegerField(default=1, help_text="Total open positions")
    description = models.TextField(help_text="Role summary, department context, and reporting hierarchy")
    responsibilities = models.TextField(help_text="Key responsibilities and daily tasks (one bullet per line)")
    requirements = models.TextField(help_text="Skills, lift technical knowledge, certifications required (one per line)")
    benefits = models.TextField(blank=True, help_text="Compensation perks, PF/ESIC, performance incentives (one per line)")
    is_urgent = models.BooleanField(default=False, help_text="Highlight with 'Urgent Hiring' badge")
    active = models.BooleanField(default=True, help_text="Visible for applications on careers page")
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Job Opening"
        verbose_name_plural = "Job Openings"

    def __str__(self):
        return f"{self.title} ({self.location})"

    def get_absolute_url(self):
        return reverse('careers:detail', kwargs={'slug': self.slug})

    def get_responsibilities_list(self):
        if not self.responsibilities:
            return []
        return [r.strip() for r in self.responsibilities.splitlines() if r.strip()]

    def get_requirements_list(self):
        if not self.requirements:
            return []
        return [r.strip() for r in self.requirements.splitlines() if r.strip()]

    def get_benefits_list(self):
        if not self.benefits:
            return []
        return [b.strip() for b in self.benefits.splitlines() if b.strip()]


class JobApplication(models.Model):
    """
    Candidate job applications, uploaded resumes, and HR recruitment tracking.
    """
    STATUS_CHOICES = [
        ('New', 'New Application'),
        ('Under Review', 'Under Technical Review'),
        ('Shortlisted', 'Shortlisted for Interview'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Offered', 'Job Offer Made'),
        ('Rejected', 'Not Selected / Archive'),
    ]

    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE, related_name='applications')
    applicant_name = models.CharField(max_length=120, help_text="Full Name of candidate")
    email = models.EmailField(help_text="Email Address")
    phone = models.CharField(max_length=25, help_text="Mobile Number")
    current_city = models.CharField(max_length=100, help_text="Current residential city")
    years_of_experience = models.CharField(max_length=50, help_text="e.g. '4.5 Years', 'Fresher'")
    current_company = models.CharField(max_length=150, blank=True, help_text="Current / Most Recent Employer")
    resume = models.FileField(
        upload_to='resumes/%Y/%m/',
        help_text="Upload CV/Resume in PDF, DOC, or DOCX format (Max 5MB)"
    )
    cover_note = models.TextField(blank=True, help_text="Brief candidate intro or elevator industry projects handled")
    status = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        default='New',
        db_index=True
    )
    admin_notes = models.TextField(blank=True, help_text="Internal HR feedback, interview dates, salary expectations")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"

    def __str__(self):
        return f"{self.applicant_name} - {self.job.title} [{self.status}]"
