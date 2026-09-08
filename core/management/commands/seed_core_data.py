from django.core.management.base import BaseCommand
from core.models import SiteSettings, HeroSlider, Statistic, Feature, ProcessStep, Industry


class Command(BaseCommand):
    help = "Seeds initial corporate content and configuration for Krupa Elevator"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding Krupa Elevator core data..."))

        # 1. Site Settings
        settings, created = SiteSettings.objects.get_or_create(id=1)
        settings.company_name = "KRUPA ELEVATOR"
        settings.tagline = "Precision Engineering. Supreme Safety. Elevated Living."
        settings.phone = "+91 98765 43210"
        settings.alternate_phone = "+91 98765 43211"
        settings.email = "contact@krupaelevator.com"
        settings.whatsapp = "+919876543210"
        settings.address = "Plot No. 42, Engineering Zone, GIDC Phase II, Ahmedabad, Gujarat 382445, India"
        settings.working_hours = "Monday – Saturday: 9:00 AM – 7:00 PM | 24x7 Emergency Service"
        settings.emergency_helpline = "+91 98765 43210"
        settings.facebook = "https://facebook.com"
        settings.instagram = "https://instagram.com"
        settings.linkedin = "https://linkedin.com"
        settings.youtube = "https://youtube.com"
        settings.twitter = "https://twitter.com"
        settings.footer_description = (
            "Krupa Elevator is an industry-leading vertical mobility engineering company dedicated to designing, "
            "manufacturing, installing, and servicing superior passenger, freight, and custom architectural elevators across India."
        )
        settings.save()
        self.stdout.write(self.style.SUCCESS("[✔] SiteSettings verified."))

        # 2. Hero Slides
        slides_data = [
            {
                "title": "Next-Generation Vertical Mobility Solutions",
                "subtitle": "ENGINEERED FOR SUPREME SAFETY & COMFORT",
                "description": "Empowering modern architecture with energy-efficient passenger, panoramic, and high-speed elevators crafted with European precision.",
                "button_text": "Explore Elevators",
                "button_url": "#products",
                "secondary_button_text": "Get a Quote",
                "secondary_button_url": "#enquiry",
                "display_order": 1,
            },
            {
                "title": "Heavy-Duty Freight & Industrial Elevators",
                "subtitle": "UNCOMPROMISING POWER & DURABILITY",
                "description": "Robust material handling systems engineered for manufacturing plants, logistics hubs, and automobile complexes with capacities up to 10,000 kg.",
                "button_text": "Industrial Range",
                "button_url": "#products",
                "secondary_button_text": "Request Inspection",
                "secondary_button_url": "#contact",
                "display_order": 2,
            },
            {
                "title": "Smart Hospital & Stretcher Elevators",
                "subtitle": "PRECISION LEVELING FOR HEALTHCARE TRANSIT",
                "description": "Whisper-quiet, jerk-free elevators built specifically for sensitive patients, ICU stretchers, and critical hospital emergency logistics.",
                "button_text": "Healthcare Range",
                "button_url": "#products",
                "secondary_button_text": "Consult an Expert",
                "secondary_button_url": "#enquiry",
                "display_order": 3,
            }
        ]

        HeroSlider.objects.all().delete()
        for data in slides_data:
            HeroSlider.objects.create(**data, active=True)
        self.stdout.write(self.style.SUCCESS(f"[✔] Seeded {len(slides_data)} Hero Sliders."))

        # 3. Statistics
        stats_data = [
            {"title": "Years of Excellence", "number": "25", "suffix": "+", "icon": "bi-award", "display_order": 1},
            {"title": "Elevators Installed", "number": "1,850", "suffix": "+", "icon": "bi-building-up", "display_order": 2},
            {"title": "Satisfied Clients", "number": "980", "suffix": "+", "icon": "bi-people", "display_order": 3},
            {"title": "Cities Served", "number": "35", "suffix": "+", "icon": "bi-geo-alt", "display_order": 4},
        ]
        Statistic.objects.all().delete()
        for s in stats_data:
            Statistic.objects.create(**s, active=True)
        self.stdout.write(self.style.SUCCESS(f"[✔] Seeded {len(stats_data)} Statistics."))

        # 4. Features ("Why Choose Krupa Elevator")
        features_data = [
            {
                "title": "Advanced Microprocessor Control",
                "badge_text": "Smart Tech",
                "icon": "bi-cpu",
                "description": "Smart dispatch algorithms and regenerative V3F drives reducing electricity consumption by up to 40% while ensuring whisper-quiet movement.",
                "display_order": 1,
            },
            {
                "title": "Multi-Tier Safety Architecture",
                "badge_text": "Zero Compromise",
                "icon": "bi-shield-check",
                "description": "Fitted with progressive safety gears, overspeed governors, full-height multi-beam infrared curtains, and automatic rescue devices (ARD).",
                "display_order": 2,
            },
            {
                "title": "Whisper-Quiet Smooth Ride",
                "badge_text": "Acoustic Shield",
                "icon": "bi-soundwave",
                "description": "Precision roller guide assemblies and isolated car suspensions eliminate high-speed vibration and cabin air-rush noise.",
                "display_order": 3,
            },
            {
                "title": "Bespoke Luxury Cabins",
                "badge_text": "Custom Aesthetics",
                "icon": "bi-gem",
                "description": "Customizable SS 304/316 hair-line, titanium gold etched panels, panoramic structural glass, marble floorings, and ambient LED lighting.",
                "display_order": 4,
            },
            {
                "title": "MRL Space-Saving Systems",
                "badge_text": "Eco-Smart",
                "icon": "bi-lightning-charge",
                "description": "Machine Room-Less (MRL) gearless permanent magnet synchronous motors (PMSM) eliminating roof machine rooms and saving build costs.",
                "display_order": 5,
            },
            {
                "title": "24/7 Rapid Response & AMC",
                "badge_text": "Round the Clock",
                "icon": "bi-headset",
                "description": "Dedicated mobile field-service squads and proactive IoT-ready predictive monitoring keeping equipment uptime at 99.8%.",
                "display_order": 6,
            },
            {
                "title": "Certified Quality Standards",
                "badge_text": "IS / EN 81",
                "icon": "bi-patch-check",
                "description": "Full compliance with Bureau of Indian Standards (IS 14665) and European EN-81 safety directives for absolute peace of mind.",
                "display_order": 7,
            },
            {
                "title": "Turnkey Engineering & Execution",
                "badge_text": "Full Lifecycle",
                "icon": "bi-tools",
                "description": "From shaft survey, structural calculations, and CAD fabrication to statutory licensing approvals and user commissioning.",
                "display_order": 8,
            },
        ]
        Feature.objects.all().delete()
        for f in features_data:
            Feature.objects.create(**f, active=True)
        self.stdout.write(self.style.SUCCESS(f"[✔] Seeded {len(features_data)} Features."))

        # 5. Process Steps
        steps_data = [
            {
                "step_number": 1,
                "title": "Consultation & Traffic Study",
                "icon": "bi-chat-left-dots",
                "short_description": "We analyze architectural plans, floor heights, anticipated passenger traffic, and interior design expectations.",
                "display_order": 1,
            },
            {
                "step_number": 2,
                "title": "Precision Laser Site Survey",
                "icon": "bi-compass",
                "short_description": "Our senior project engineers capture exact laser dimensions of the hoistway, pit depth, and overhead clearances.",
                "display_order": 2,
            },
            {
                "step_number": 3,
                "title": "Custom CAD Engineering",
                "icon": "bi-pencil-square",
                "short_description": "Tailored structural drawings and 3D cabin renders are prepared for structural approval and spatial optimization.",
                "display_order": 3,
            },
            {
                "step_number": 4,
                "title": "High-Precision Manufacturing",
                "icon": "bi-gear-wide-connected",
                "short_description": "Fabrication of guide rails, car frames, control controllers, and drive systems adhering to rigorous quality standards.",
                "display_order": 4,
            },
            {
                "step_number": 5,
                "title": "Erection & Mechanical Assembly",
                "icon": "bi-hammer",
                "short_description": "Certified mechanical specialists install guide rails, counterweights, suspension cables, and car bodies with millimeter precision.",
                "display_order": 5,
            },
            {
                "step_number": 6,
                "title": "Multi-Point Safety & Load Testing",
                "icon": "bi-clipboard-check",
                "short_description": "Rigorous full-capacity drop tests, overspeed governor checks, and emergency ARD backup validation before certification.",
                "display_order": 6,
            },
            {
                "step_number": 7,
                "title": "Statutory Handover & 24/7 AMC",
                "icon": "bi-key",
                "short_description": "Final inspection certificate handover, operator training, and enrollment into our proactive preventative AMC care.",
                "display_order": 7,
            },
        ]
        ProcessStep.objects.all().delete()
        for step in steps_data:
            ProcessStep.objects.create(**step, active=True)
        self.stdout.write(self.style.SUCCESS(f"[✔] Seeded {len(steps_data)} Process Steps."))

        # 6. Industries We Serve
        industries_data = [
            {
                "name": "Residential High-Rises & Villas",
                "icon": "bi-houses",
                "description": "Smooth, whisper-quiet passenger lifts and custom luxury bungalow elevators designed for comfort and energy efficiency.",
                "display_order": 1,
            },
            {
                "name": "Commercial Towers & IT Hubs",
                "icon": "bi-buildings",
                "description": "High-speed elevators with group supervisory dispatch algorithms handling dense morning and evening peak traffic.",
                "display_order": 2,
            },
            {
                "name": "Hospitals & Medical Centers",
                "icon": "bi-hospital",
                "description": "Spacious stretcher and bed elevators engineered with shock-free acceleration and antibacterial cabin finishes.",
                "display_order": 3,
            },
            {
                "name": "Luxury Hotels & Resorts",
                "icon": "bi-building-fill-check",
                "description": "Architectural panoramic glass elevators and bespoke finishes delivering an upscale hospitality experience.",
                "display_order": 4,
            },
            {
                "name": "Manufacturing & Warehouses",
                "icon": "bi-factory",
                "description": "Heavy-capacity freight elevators, goods lifts, and dumbwaiters built to withstand relentless industrial loads.",
                "display_order": 5,
            },
            {
                "name": "Shopping Malls & Retail Hubs",
                "icon": "bi-shop",
                "description": "High-throughput scenic lifts and moving walkways maximizing visitor visual engagement and accessibility.",
                "display_order": 6,
            },
            {
                "name": "Colleges & Public Institutions",
                "icon": "bi-mortarboard",
                "description": "Heavy-duty, vandal-resistant, low-maintenance vertical mobility compliant with all accessible design codes.",
                "display_order": 7,
            },
            {
                "name": "Government & Infrastructure",
                "icon": "bi-bank",
                "description": "Secure, durable installations engineered for railway hubs, airports, civil headquarters, and civic monuments.",
                "display_order": 8,
            },
        ]
        Industry.objects.all().delete()
        for ind in industries_data:
            Industry.objects.create(**ind, active=True)
        self.stdout.write(self.style.SUCCESS(f"[✔] Seeded {len(industries_data)} Industries."))

        self.stdout.write(self.style.SUCCESS("All core database models successfully populated for Krupa Elevator!"))
