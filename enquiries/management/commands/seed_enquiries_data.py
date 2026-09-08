from django.core.management.base import BaseCommand
from enquiries.models import ContactEnquiry, QuoteRequest


class Command(BaseCommand):
    help = "Seed sample contact enquiries and detailed quote requests across various statuses"

    def handle(self, *args, **options):
        self.stdout.write("Seeding Enquiries & Quote Requests...")

        # 1. Sample Contact Enquiries
        enquiries_data = [
            {
                'name': 'Rajesh Sharma',
                'phone': '+91 98250 11223',
                'email': 'rajesh.sharma@sharmabuilders.com',
                'company': 'Sharma Construction Co.',
                'city': 'Ahmedabad',
                'subject': 'Passenger Elevator for 7-Floor Commercial Scheme',
                'message': 'We have an ongoing commercial project near Prahladnagar, Ahmedabad. Looking for 2 passenger lifts with SS titanium finish and ARD.',
                'status': 'New',
                'admin_notes': 'Received via website inquiry form. Need to assign engineer for site laser survey.'
            },
            {
                'name': 'Dr. Meena Deshmukh',
                'phone': '+91 97654 33445',
                'email': 'dr.meena@lifelinehospital.org',
                'company': 'LifeLine Multispeciality Hospital',
                'city': 'Pune',
                'subject': 'Hospital Stretcher Elevator Requirement',
                'message': 'Require urgent quotation for 1 bed/stretcher elevator with priority code, antibacterial handrails, and smooth acceleration.',
                'status': 'Contacted',
                'admin_notes': 'Called Dr. Meena. Discussed 1000 kg capacity stretcher dimensions. Waiting for shaft drawings.'
            },
            {
                'name': 'Vikram Mehta',
                'phone': '+91 98201 55667',
                'email': 'v.mehta@seasidevillas.in',
                'company': 'Private Residence',
                'city': 'Mumbai',
                'subject': 'Glass Home Lift for Duplex Penthouse',
                'message': 'Looking for a compact pitless glass elevator for an existing duplex penthouse in Worli. Single phase power operable if possible.',
                'status': 'Follow Up',
                'admin_notes': 'Shared brochure for Krupa Home Panoramic series. Client scheduled follow up call for next Tuesday.'
            },
            {
                'name': 'Anand Patel',
                'phone': '+91 99099 77889',
                'email': 'anand@pateltextiles.com',
                'company': 'Patel Textile Mills Ltd.',
                'city': 'Surat',
                'subject': '3-Ton Industrial Goods Lift for Warehouse',
                'message': 'Need heavy duty freight lift with bi-parting steel collapsible gates for textile rolls handling.',
                'status': 'Converted',
                'admin_notes': 'Converted to contract #KT-2026-088. Advance 30% payment received. Manufacturing underway.'
            },
            {
                'name': 'Sanjay Kulkarni',
                'phone': '+91 98450 99001',
                'email': 'sanjay.k@kulkarniinfra.com',
                'company': 'Kulkarni Infra',
                'city': 'Vadodara',
                'subject': 'Annual Maintenance Contract Renewal',
                'message': 'Existing elevator AMC contract expiring next month. Need comprehensive proposal for 4 elevators.',
                'status': 'Closed',
                'admin_notes': 'Client renewed contract for 3 years comprehensive maintenance.'
            },
        ]

        for item in enquiries_data:
            enquiry, created = ContactEnquiry.objects.get_or_create(
                email=item['email'],
                subject=item['subject'],
                defaults=item
            )
            if created:
                self.stdout.write(f"  + Created Contact Enquiry: {enquiry.name} [{enquiry.status}]")
            else:
                self.stdout.write(f"  * Exists Contact Enquiry: {enquiry.name}")

        # 2. Sample Quote Requests across full pipeline
        quotes_data = [
            {
                'customer_name': 'Deepak Singhania',
                'company_name': 'Singhania Real Estate Developers',
                'phone': '+91 98111 22334',
                'email': 'deepak@singhaniagroup.com',
                'city': 'Ahmedabad',
                'project_location': 'Near Vaishnodevi Circle, SG Highway',
                'building_type': 'Residential Apartment',
                'elevator_type': 'Passenger Elevator',
                'number_of_floors': 'G+14 Floors (15 Stops)',
                'capacity_required': '13 Passengers / 884 kg',
                'number_of_elevators': 3,
                'project_stage': 'Civil Construction Ongoing',
                'message': 'Dual car passenger bank with duplex collective microprocessor controller. Speed 1.75 m/s. Stainless steel gold etched cabin.',
                'status': 'New',
                'admin_notes': 'High priority lead. Developer building 240 luxury flats.'
            },
            {
                'customer_name': 'Ar. Priya Sen',
                'company_name': 'Studio Sen Architecture & Interiors',
                'phone': '+91 98222 44556',
                'email': 'priya@studiosen.com',
                'city': 'Mumbai',
                'project_location': 'Bandra West',
                'building_type': 'Private Villa / Bungalow',
                'elevator_type': 'Home / Villa Elevator',
                'number_of_floors': 'G+2 (3 Stops)',
                'capacity_required': '4 Passengers / 300 kg',
                'number_of_elevators': 1,
                'project_stage': 'Architectural Planning',
                'message': 'Panoramic structural curved glass lift shaft in the central spiral staircase. Minimal pit required.',
                'status': 'Contacted',
                'admin_notes': 'Sent architectural shaft clearance drawings and CAD blocks.'
            },
            {
                'customer_name': 'Harish Verma',
                'company_name': 'Carewell Hospitals Group',
                'phone': '+91 98333 66778',
                'email': 'h.verma@carewellhospitals.com',
                'city': 'Pune',
                'project_location': 'Kothrud, Pune',
                'building_type': 'Hospital / Healthcare',
                'elevator_type': 'Hospital Stretcher Elevator',
                'number_of_floors': 'B+G+8 Floors (10 Stops)',
                'capacity_required': '26 Passengers / 1768 kg (Stretcher Bed)',
                'number_of_elevators': 2,
                'project_stage': 'Civil Hoistway Ready',
                'message': 'Strict jerk-free travel required for ICU patients. Medical priority key switch on both ground and emergency floors.',
                'status': 'Survey Scheduled',
                'admin_notes': 'Site survey scheduled for Friday with Chief Project Engineer Mr. Patel.'
            },
            {
                'customer_name': 'Ramesh Bhai Choksi',
                'company_name': 'Choksi Diamond Arcade',
                'phone': '+91 98444 88990',
                'email': 'rbc@choksidiamonds.com',
                'city': 'Surat',
                'project_location': 'Varachha Road, Surat',
                'building_type': 'Commercial / Corporate Office',
                'elevator_type': 'MRL Elevator',
                'number_of_floors': 'G+11 Floors (12 Stops)',
                'capacity_required': '10 Passengers / 680 kg',
                'number_of_elevators': 4,
                'project_stage': 'Civil Construction Ongoing',
                'message': 'High traffic commercial complex. Energy saving PMSM gearless technology with destination control integration.',
                'status': 'Quotation Sent',
                'admin_notes': 'Quotation Ref #KQ-SUR-2026-44 emailed on March 2nd for INR 48.5 Lakhs.'
            },
            {
                'customer_name': 'Nitin Gadkari Enterprises',
                'company_name': 'Western Logistics Hub',
                'phone': '+91 98555 11223',
                'email': 'logistics@westerngroup.in',
                'city': 'Vadodara',
                'project_location': 'Makarpura GIDC',
                'building_type': 'Industrial / Factory / Warehouse',
                'elevator_type': 'Freight / Goods Elevator',
                'number_of_floors': 'G+3 Floors (4 Stops)',
                'capacity_required': '3000 kg Heavy Freight',
                'number_of_elevators': 2,
                'project_stage': 'Civil Hoistway Ready',
                'message': 'Forklift operable landing sill plates, IP65 water/dust resistant push buttons.',
                'status': 'Negotiation',
                'admin_notes': 'Meeting held on technical clarifications. Revision 2 quote under negotiation for payment milestone terms.'
            },
            {
                'customer_name': 'Kavita Sundaram',
                'company_name': 'The Oberoi Gateway Luxury Resort',
                'phone': '+91 98666 33445',
                'email': 'ksundaram@gatewayresorts.com',
                'city': 'Mumbai',
                'project_location': 'Juhu Beachfront',
                'building_type': 'Hotel / Hospitality',
                'elevator_type': 'Panoramic Glass Elevator',
                'number_of_floors': 'G+6 Floors (7 Stops)',
                'capacity_required': '16 Passengers / 1088 kg',
                'number_of_elevators': 2,
                'project_stage': 'Modernization / Replacement',
                'message': 'Replacement of 20-year old hydraulic lifts with modern glass capsules facing Arabian Sea.',
                'status': 'Won',
                'admin_notes': 'Contract signed and LOI issued! Contract Value: INR 62 Lakhs. Commissioning target: Q4 2026.'
            },
            {
                'customer_name': 'Bipin Shah',
                'company_name': 'Shah Plaza Commercial',
                'phone': '+91 98777 55667',
                'email': 'bipin@shahplaza.in',
                'city': 'Ahmedabad',
                'project_location': 'Ashram Road',
                'building_type': 'Commercial / Corporate Office',
                'elevator_type': 'Passenger Elevator',
                'number_of_floors': 'G+5 Floors',
                'capacity_required': '6 Passengers / 408 kg',
                'number_of_elevators': 1,
                'project_stage': 'Civil Hoistway Ready',
                'message': 'Standard passenger elevator with manual collapsible gate.',
                'status': 'Lost',
                'admin_notes': 'Lost to low-cost unorganized assembler on price difference. Client opted for manual gate system.'
            },
        ]

        for q in quotes_data:
            quote, created = QuoteRequest.objects.get_or_create(
                email=q['email'],
                elevator_type=q['elevator_type'],
                number_of_floors=q['number_of_floors'],
                defaults=q
            )
            if created:
                self.stdout.write(f"  + Created Quote Request: {quote.customer_name} ({quote.elevator_type}) [{quote.status}]")
            else:
                self.stdout.write(f"  * Exists Quote Request: {quote.customer_name}")

        self.stdout.write(self.style.SUCCESS("Successfully seeded Phase 5 enquiries and quote requests!"))

