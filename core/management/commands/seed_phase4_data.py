from datetime import date
from django.core.management.base import BaseCommand
from core.models import Service, Client
from projects.models import Project
from gallery.models import GalleryCategory, GalleryImage


class Command(BaseCommand):
    help = "Seeds comprehensive Services, Clients, Projects, and Gallery data for Krupa Elevator"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding Phase 4 data (Services, Clients, Projects, Gallery)..."))

        # 1. Seed Services
        services_data = [
            {
                "title": "Elevator Installation",
                "slug": "elevator-installation",
                "short_description": "Turnkey erection, mechanical assembly, and electrical commissioning adhering to IS 14665 & EN-81 directives.",
                "description": (
                    "Krupa Elevator offers end-to-end turnkey elevator installation services for residential societies, commercial complexes, "
                    "hospitals, and heavy industrial facilities. Our certified mechanical erection specialists utilize precision laser-guided "
                    "alignment tools to ensure guide rails and car frames operate with zero vibration and millimeter accuracy."
                ),
                "icon": "bi-hammer",
                "features": (
                    "Precision laser hoistway and plumb-line alignment\n"
                    "Rigorous structural load and overspeed governor testing\n"
                    "Complete statutory elevator licensing approvals support\n"
                    "Millimeter-accurate leveling sensor calibration\n"
                    "Comprehensive technician and building operator handover training"
                ),
                "display_order": 1,
            },
            {
                "title": "Annual Maintenance Contract (AMC)",
                "slug": "elevator-maintenance-amc",
                "short_description": "Proactive preventative maintenance keeping elevator downtime near zero with 24/7 rapid breakdown support.",
                "description": (
                    "Our preventative Annual Maintenance Contracts (AMC) protect your investment, maintain passenger safety, and extend "
                    "equipment lifespan. Choose from Comprehensive (parts + labor) or Semi-Comprehensive service plans, backed by scheduled "
                    "monthly safety audits and prioritized emergency response."
                ),
                "icon": "bi-shield-check",
                "features": (
                    "Scheduled monthly 52-point mechanical and electrical safety inspection\n"
                    "24/7 dedicated breakdown hotline with 30-minute urban response time\n"
                    "Lubrication, brake adjustment, and door operator calibration\n"
                    "Digital service log and automated preventative maintenance alerts\n"
                    "Genuine OEM spare parts replacement coverage"
                ),
                "display_order": 2,
            },
            {
                "title": "Elevator Modernization & Upgrades",
                "slug": "elevator-modernization",
                "short_description": "Transform aging elevators with modern regenerative V3F drives, digital displays, and luxury cabin interiors.",
                "description": (
                    "Is your building elevator slow, noisy, or constantly breaking down? Krupa Modernization packages replace aging geared traction "
                    "machines with energy-efficient gearless PMSM motors, install modern microprocessor controllers with ARD, and refresh "
                    "dated cabin interiors with luxurious stainless steel and ambient lighting."
                ),
                "icon": "bi-arrow-repeat",
                "features": (
                    "Up to 40% reduction in electrical power consumption\n"
                    "Whisper-quiet, jerk-free riding comfort and accurate floor leveling\n"
                    "Integration of full-height infrared door curtains and Automatic Rescue Devices (ARD)\n"
                    "Designer SS 304 / Titanium Gold cabin wall panel replacement\n"
                    "High-resolution 7-inch TFT floor indicator and multimedia screens"
                ),
                "display_order": 3,
            },
            {
                "title": "Elevator Repair & Diagnostics",
                "slug": "elevator-repair",
                "short_description": "Fast-track troubleshooting and certified component repair for all elevator brands and drive configurations.",
                "description": (
                    "When equipment malfunctions, our diagnostic engineers arrive equipped with specialized testing instruments to identify "
                    "and rectify mechanical, electrical, and control board faults swiftly, minimizing tenant inconvenience."
                ),
                "icon": "bi-tools",
                "features": (
                    "Rapid fault code analysis and PCB repair\n"
                    "Drive motor rewinding, brake re-lining, and sheave regrooving\n"
                    "Wire rope replacement and counterweight balancing\n"
                    "Door operator belt, clutch, and roller replacement\n"
                    "Emergency safety gear drop-test re-certification"
                ),
                "display_order": 4,
            },
            {
                "title": "Elevator Replacement & Retrofitting",
                "slug": "elevator-replacement",
                "short_description": "Complete hoistway strip-down and installation of modern high-speed elevators in existing structural shafts.",
                "description": (
                    "For elevators past their statutory economic life, we provide seamless elevator replacement services. We safely dismantle "
                    "obsolete equipment and erect brand-new high-capacity systems inside existing concrete or steel shafts with minimal building disruption."
                ),
                "icon": "bi-building-up",
                "features": (
                    "Safe hoistway decommissioning and scrap removal\n"
                    "Custom car sizing to maximize existing hoistway dimensions\n"
                    "Compliance with latest national building codes and fire safety norms\n"
                    "Turnkey project management from structural audit to government licensing"
                ),
                "display_order": 5,
            },
            {
                "title": "Site Inspection & Safety Audits",
                "slug": "site-inspection-safety-audit",
                "short_description": "Comprehensive hoistway laser audits, load calculations, and statutory compliance certification.",
                "description": (
                    "Ensure absolute legal compliance and peace of mind. Our chartered safety engineers conduct thorough third-party "
                    "safety audits of elevator hoistways, pit drainage, machine rooms, safety gears, and emergency communication systems."
                ),
                "icon": "bi-clipboard-check",
                "features": (
                    "Detailed 75-point statutory safety audit report\n"
                    "Laser measurement of hoistway plumb, pit depth, and overhead clearances\n"
                    "Overspeed governor trip speed testing and safety gear drop checks\n"
                    "Electrical earth resistance and insulation resistance testing"
                ),
                "display_order": 6,
            },
            {
                "title": "Lift Consultation & Architectural Planning",
                "slug": "lift-consultation-design",
                "short_description": "Early-stage traffic analysis, structural shaft modeling, and architectural specification consulting.",
                "description": (
                    "We collaborate with architects, structural engineers, and real estate developers from initial concept stages. "
                    "We provide vertical transportation traffic simulations, dispatch analysis, electrical load calculations, and tailored CAD drawings."
                ),
                "icon": "bi-compass",
                "features": (
                    "Peak-hour passenger traffic simulations and waiting interval modeling\n"
                    "Custom 2D/3D CAD hoistway layout drawings and structural reaction loads\n"
                    "Energy consumption calculations and green building credit advisory\n"
                    "Preparation of technical tender documentation and component specifications"
                ),
                "display_order": 7,
            },
            {
                "title": "24/7 Breakdown & Emergency Rescue Support",
                "slug": "emergency-breakdown-rescue",
                "short_description": "Dedicated round-the-clock rapid response mobile squads for elevator entrapment and emergency assistance.",
                "description": (
                    "Passenger safety is our highest priority. Our 24/7 central emergency control desk coordinates immediate dispatch of "
                    "equipped field teams to resolve passenger entrapments and critical breakdown emergencies within minutes."
                ),
                "icon": "bi-headset",
                "features": (
                    "24-Hour dedicated emergency helpline and direct WhatsApp control desk\n"
                    "Trained passenger rescue technicians deployed on dedicated rapid-response two-wheelers\n"
                    "Coordination with local fire and building security personnel\n"
                    "Immediate root-cause failure analysis and equipment recommissioning"
                ),
                "display_order": 8,
            },
        ]

        for s_data in services_data:
            s_slug = s_data.pop("slug")
            s_obj, created = Service.objects.update_or_create(slug=s_slug, defaults=s_data)
            status = "Created" if created else "Updated"
            self.stdout.write(f"  [{status}] Service: {s_obj.title}")

        # 2. Seed Clients
        clients_data = [
            {"name": "Shivalik Real Estate Developers", "industry": "Premium Residential & Commercial", "description": "Over 120+ elevators installed across luxury residential high-rises and corporate headquarters."},
            {"name": "Zydus Healthcare & Hospitals", "industry": "Multi-Speciality Healthcare", "description": "High-precision bed and stretcher lifts deployed across critical surgical care centers."},
            {"name": "Adani Township Infrastructure", "industry": "Mega Infrastructure", "description": "Heavy-duty passenger and maintenance vertical systems across multi-acre residential townships."},
            {"name": "Iscon Platinum Corporate Towers", "industry": "Commercial Real Estate", "description": "High-speed group supervisory passenger elevator banks handling 10,000+ daily occupants."},
            {"name": "Hyatt Regency Hospitality", "industry": "Luxury 5-Star Hotel", "description": "Custom titanium gold panoramic scenic glass elevators delivering scenic atrium vistas."},
            {"name": "Tata Electronics Industrial Complex", "industry": "Heavy Manufacturing", "description": "10-ton industrial hydraulic freight and automotive logistics elevators."},
        ]

        for c_data in clients_data:
            c_obj, created = Client.objects.update_or_create(name=c_data["name"], defaults=c_data)
            status = "Created" if created else "Updated"
            self.stdout.write(f"  [{status}] Client: {c_obj.name}")

        # 3. Seed Projects
        projects_data = [
            {
                "title": "Skyline Grand Twin Towers",
                "slug": "skyline-grand-twin-towers",
                "client_name": "Shivalik Group",
                "location": "SG Highway, Bodakdev",
                "city": "Ahmedabad",
                "project_type": "Residential",
                "elevator_type": "Passenger Elevator",
                "number_of_elevators": 6,
                "description": (
                    "Supplied and commissioned 6 units of Gearless High-Speed Passenger Elevators (2.0 m/s) with duplex group supervisory "
                    "control for 32-story twin residential towers. Features titanium gold etched cabins and regenerative V3F drives."
                ),
                "completion_date": date(2024, 6, 15),
                "featured": True,
                "display_order": 1,
            },
            {
                "title": "Apollo Super-Speciality Hospital",
                "slug": "apollo-super-speciality-hospital",
                "client_name": "Apollo Healthcare",
                "location": "Ring Road, Athwa",
                "city": "Surat",
                "project_type": "Healthcare",
                "elevator_type": "Hospital Stretcher Elevator",
                "number_of_elevators": 4,
                "description": (
                    "Turnkey design and installation of 4 spacious stretcher elevators (26 passenger capacity) with medical priority control, "
                    "anti-bacterial cabin panels, and millimeter-level floor landing accuracy for sensitive ICU patient transit."
                ),
                "completion_date": date(2024, 3, 20),
                "featured": True,
                "display_order": 2,
            },
            {
                "title": "Corporate One IT Business Park",
                "slug": "corporate-one-it-business-park",
                "client_name": "Iscon Developers",
                "location": "Alkapuri Business District",
                "city": "Vadodara",
                "project_type": "Commercial",
                "elevator_type": "MRL Elevator",
                "number_of_elevators": 8,
                "description": (
                    "Integrated 8 high-efficiency Machine Room-Less (MRL) gearless elevators serving 18 commercial office floors. "
                    "Equipped with smart card access control, energy-saving standby mode, and 1.75 m/s travel velocity."
                ),
                "completion_date": date(2023, 11, 10),
                "featured": True,
                "display_order": 3,
            },
            {
                "title": "Royal Heritage Luxury Villas",
                "slug": "royal-heritage-luxury-villas",
                "client_name": "Private Elite Estates",
                "location": "Kalawad Road",
                "city": "Rajkot",
                "project_type": "Residential",
                "elevator_type": "Home / Villa Elevator",
                "number_of_elevators": 12,
                "description": (
                    "Customized pitless home elevators installed inside 12 bespoke bungalow residences. Engineered with quiet single-phase "
                    "operation, panoramic glass doors, and luxury Italian marble floor inserts."
                ),
                "completion_date": date(2024, 7, 5),
                "featured": False,
                "display_order": 4,
            },
            {
                "title": "Grand Sapphire 5-Star Hotel",
                "slug": "grand-sapphire-5-star-hotel",
                "client_name": "Hyatt Hospitality",
                "location": "Bandra Kurla Complex",
                "city": "Mumbai",
                "project_type": "Hospitality",
                "elevator_type": "Panoramic Glass Elevator",
                "number_of_elevators": 3,
                "description": (
                    "3 units of breathtaking circular curved glass panoramic elevators traversing a 20-story soaring atrium. "
                    "Features under-car ambient illumination and silent synchronous traction machinery."
                ),
                "completion_date": date(2023, 9, 30),
                "featured": True,
                "display_order": 5,
            },
            {
                "title": "Gujarat Logistics Hub & Warehouses",
                "slug": "gujarat-logistics-hub-warehouses",
                "client_name": "Tata Supply Chain",
                "location": "Sanand Industrial Estate",
                "city": "Ahmedabad",
                "project_type": "Industrial",
                "elevator_type": "Freight / Goods Elevator",
                "number_of_elevators": 5,
                "description": (
                    "Heavy-duty 5,000 kg payload goods elevators designed for continuous forklift cargo transfer across 4 warehouse tiers. "
                    "Built with reinforced chequered steel floors and industrial bi-parting safety gates."
                ),
                "completion_date": date(2024, 2, 18),
                "featured": True,
                "display_order": 6,
            },
            {
                "title": "Metro City Central Mall",
                "slug": "metro-city-central-mall",
                "client_name": "Central Retail Consortium",
                "location": "Dumas Road",
                "city": "Surat",
                "project_type": "Commercial",
                "elevator_type": "Escalator",
                "number_of_elevators": 6,
                "description": (
                    "High-volume heavy-traffic commercial moving stairways and scenic observation elevators moving 8,000+ shoppers per hour "
                    "with VVVF radar energy-saving controllers."
                ),
                "completion_date": date(2023, 8, 12),
                "featured": False,
                "display_order": 7,
            },
            {
                "title": "Platinum Corporate Heights",
                "slug": "platinum-corporate-heights",
                "client_name": "Platinum Realty",
                "location": "Prahladnagar",
                "city": "Ahmedabad",
                "project_type": "Commercial",
                "elevator_type": "Passenger Elevator",
                "number_of_elevators": 6,
                "description": (
                    "6 units of high-speed passenger elevators equipped with destination dispatch systems and touchless call buttons "
                    "for a marquee 22-floor corporate financial tower."
                ),
                "completion_date": date(2024, 5, 25),
                "featured": False,
                "display_order": 8,
            }
        ]

        for p_data in projects_data:
            p_slug = p_data.pop("slug")
            p_obj, created = Project.objects.update_or_create(slug=p_slug, defaults=p_data)
            status = "Created" if created else "Updated"
            self.stdout.write(f"  [{status}] Project: {p_obj.title} ({p_obj.city})")

        # 4. Seed Gallery Categories & Images
        gallery_cats = [
            {"name": "Cabin Interiors & Luxury Finishes", "slug": "cabin-interiors", "display_order": 1},
            {"name": "Panoramic & Glass Elevators", "slug": "panoramic-glass", "display_order": 2},
            {"name": "Commercial & High-Rise Towers", "slug": "commercial-towers", "display_order": 3},
            {"name": "Heavy Freight & Industrial Lifts", "slug": "industrial-freight", "display_order": 4},
        ]

        for g_cat in gallery_cats:
            gc_slug = g_cat.pop("slug")
            gc_obj, _ = GalleryCategory.objects.update_or_create(slug=gc_slug, defaults=g_cat)
            self.stdout.write(f"  [Category] Gallery: {gc_obj.name}")

        self.stdout.write(self.style.SUCCESS("Phase 4 data successfully seeded for Krupa Elevator!"))
