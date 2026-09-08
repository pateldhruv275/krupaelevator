from django.db import models


class ContactEnquiry(models.Model):
    """
    General inquiries, maintenance requests, and contact messages from prospective clients.
    """
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Follow Up', 'Follow Up'),
        ('Converted', 'Converted'),
        ('Closed', 'Closed'),
    ]

    name = models.CharField(max_length=120, help_text="Full Name of the inquirer")
    phone = models.CharField(max_length=25, help_text="Primary Contact / Mobile Number")
    email = models.EmailField(help_text="Email Address")
    company = models.CharField(max_length=150, blank=True, help_text="Company / Firm Name (Optional)")
    city = models.CharField(max_length=100, help_text="City / Location")
    subject = models.CharField(max_length=200, blank=True, help_text="Subject / Purpose of inquiry")
    message = models.TextField(help_text="Message / Requirements")
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='New',
        db_index=True,
        help_text="Current lead processing status"
    )
    admin_notes = models.TextField(
        blank=True,
        help_text="Internal sales/executive notes on follow-up calls or client remarks"
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Enquiry"
        verbose_name_plural = "Contact Enquiries"

    def __str__(self):
        return f"{self.name} - {self.city} [{self.status}]"


class QuoteRequest(models.Model):
    """
    Detailed technical quotation requests for new elevators, modernizations, or turnkey builds.
    """
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Survey Scheduled', 'Survey Scheduled'),
        ('Quotation Sent', 'Quotation Sent'),
        ('Negotiation', 'Negotiation'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    ]

    BUILDING_TYPE_CHOICES = [
        ('Residential Apartment', 'Residential Apartment / Society'),
        ('Private Villa / Bungalow', 'Private Villa / Bungalow'),
        ('Commercial / Corporate Office', 'Commercial / Corporate Office'),
        ('Hospital / Healthcare', 'Hospital / Healthcare Facility'),
        ('Hotel / Hospitality', 'Hotel / Hospitality Resort'),
        ('Industrial / Factory / Warehouse', 'Industrial / Factory / Warehouse'),
        ('Mall / Retail Showroom', 'Mall / Retail Showroom'),
        ('Educational / Institution', 'Educational / Institution'),
        ('Other', 'Other Structure'),
    ]

    ELEVATOR_TYPE_CHOICES = [
        ('Passenger Elevator', 'Passenger Elevator (Gearless / Geared)'),
        ('Home / Villa Elevator', 'Home / Villa Elevator (Compact / Pitless)'),
        ('Hospital Stretcher Elevator', 'Hospital Stretcher Elevator (Bed Lift)'),
        ('Freight / Goods Elevator', 'Freight / Goods Elevator (Heavy Duty)'),
        ('Panoramic Glass Elevator', 'Panoramic Glass Elevator (Capsule / Scenic)'),
        ('Hydraulic Elevator', 'Hydraulic Elevator'),
        ('MRL Elevator', 'Machine Room-Less (MRL) Elevator'),
        ('Dumbwaiter', 'Dumbwaiter / Food Lift'),
        ('Escalator / Moving Walkway', 'Commercial Escalator / Moving Walkway'),
        ('Modernization / AMC', 'Elevator Modernization / AMC'),
        ('Other', 'Other Elevator System'),
    ]

    PROJECT_STAGE_CHOICES = [
        ('Architectural Planning', 'Architectural Planning / Blueprints Stage'),
        ('Civil Construction Ongoing', 'Civil Construction Ongoing (Shaft Under Build)'),
        ('Civil Hoistway Ready', 'Civil Hoistway Ready for Elevator Installation'),
        ('Modernization / Replacement', 'Modernization / Replacement of Existing Lift'),
        ('Urgent Requirement', 'Immediate / Urgent Requirement'),
    ]

    customer_name = models.CharField(max_length=120, help_text="Full Name of the contact person")
    company_name = models.CharField(max_length=150, blank=True, help_text="Builder, Architect, or Company Name")
    phone = models.CharField(max_length=25, help_text="Contact Phone Number")
    email = models.EmailField(help_text="Email Address for sending quotation PDF")
    city = models.CharField(max_length=100, db_index=True, help_text="City where project is located")
    project_location = models.CharField(max_length=255, blank=True, help_text="Locality, site address or landmark")
    building_type = models.CharField(max_length=60, choices=BUILDING_TYPE_CHOICES, db_index=True)
    elevator_type = models.CharField(max_length=60, choices=ELEVATOR_TYPE_CHOICES, db_index=True)
    number_of_floors = models.CharField(
        max_length=50,
        help_text="e.g. G+4 Floors, 10 Stops, Basement + Ground + 3"
    )
    capacity_required = models.CharField(
        max_length=100,
        blank=True,
        default="8 Passengers / 544 kg",
        help_text="e.g. 6 Passengers / 408 kg, 8 Passengers / 544 kg, 13 Passengers / 884 kg, 1000 kg Stretcher, 2 Ton Goods"
    )
    number_of_elevators = models.PositiveIntegerField(
        default=1,
        help_text="Number of elevator units needed"
    )
    project_stage = models.CharField(
        max_length=60,
        choices=PROJECT_STAGE_CHOICES,
        default='Civil Construction Ongoing',
        blank=True
    )
    message = models.TextField(
        blank=True,
        help_text="Specific requirements: cabin finishes, door types, speed, shaft dimensions, or special remarks"
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='New',
        db_index=True,
        help_text="Current pipeline stage"
    )
    admin_notes = models.TextField(
        blank=True,
        help_text="Internal sales estimation notes, survey findings, proposal price and date"
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Quote Request"
        verbose_name_plural = "Quote Requests"

    def __str__(self):
        return f"Quote #{self.id}: {self.customer_name} - {self.elevator_type} ({self.city}) [{self.status}]"
