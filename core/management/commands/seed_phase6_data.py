from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Testimonial
from blog.models import BlogCategory, BlogPost
from careers.models import JobOpening


class Command(BaseCommand):
    help = "Seeds Testimonials, Blog Categories, Blog Posts, and Job Openings for Krupa Elevator"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding Phase 6 data (Testimonials, Blog, Careers)..."))

        # 1. Seed Testimonials
        testimonials_data = [
            {
                "client_name": "Hareshbhai Patel",
                "client_title": "Chairman & Developer",
                "company": "Skyline Heights Cooperative Housing",
                "city": "Ahmedabad",
                "elevator_type_installed": "Dual High-Speed Gearless MRL Passenger Lifts",
                "rating": 5,
                "quote": (
                    "Krupa Elevator installed two 13-passenger MRL elevators in our 18-storey residential tower. "
                    "The ride quality is whisper-quiet, door leveling is pinpoint accurate, and their proactive AMC "
                    "team has kept our building uptime at 99.8% over the past three years. Highly recommended!"
                ),
                "display_order": 1,
                "featured": True,
            },
            {
                "client_name": "Dr. Sunita Deshmukh",
                "client_title": "Medical Director",
                "company": "Apex Multi-Speciality Hospital",
                "city": "Pune",
                "elevator_type_installed": "Bed & Stretcher Lifts with Anti-Bacterial Cabins",
                "rating": 5,
                "quote": (
                    "In emergency healthcare, elevator jerk or delay can endanger patients. Krupa's stretcher elevators "
                    "feature exceptionally gentle V3F acceleration and spacious cabins that fit critical care equipment. "
                    "Their 24/7 technical team is always responsive."
                ),
                "display_order": 2,
                "featured": True,
            },
            {
                "client_name": "Vikram Singhania",
                "client_title": "Vice President - Infrastructure",
                "company": "Matrix Logistics & Warehousing Park",
                "city": "Navi Mumbai",
                "elevator_type_installed": "5-Ton Heavy Duty Industrial Goods Elevator",
                "rating": 5,
                "quote": (
                    "We move heavy pallet jacks and industrial machinery 18 hours a day. The 5,000 kg freight elevator "
                    "engineered by Krupa is indestructible. The reinforced checkered steel flooring and heavy-duty sill "
                    "construction withstand brutal forklift loadings effortlessly."
                ),
                "display_order": 3,
                "featured": True,
            },
            {
                "client_name": "Rajiv Mehra",
                "client_title": "Villa Owner & Architect",
                "company": "Gulmohar Greens Bungalow",
                "city": "Vadodara",
                "elevator_type_installed": "Panoramic Glass Hydraulic Home Lift",
                "rating": 5,
                "quote": (
                    "We wanted a scenic glass lift for our triplex bungalow without digging a deep pit. Krupa's "
                    "engineering team designed a stunning hydraulic glass capsule lift that seamlessly blends into "
                    "our living room architecture. It runs smoothly on standard single-phase power."
                ),
                "display_order": 4,
                "featured": True,
            },
            {
                "client_name": "Anil Agarwal",
                "client_title": "Chief Facility Officer",
                "company": "Prestige Cyber One IT Park",
                "city": "Surat",
                "elevator_type_installed": "Group Supervisory 2.0 m/s Commercial Lifts",
                "rating": 5,
                "quote": (
                    "Handling peak-hour morning traffic of 1,200 software professionals requires smart dispatching. "
                    "Krupa's microprocessor controller with duplex collective selective control eliminated lobby "
                    "wait times completely. Outstanding execution and aesthetic cabin finishes."
                ),
                "display_order": 5,
                "featured": True,
            },
        ]

        created_testimonials = 0
        for data in testimonials_data:
            testimonial, created = Testimonial.objects.update_or_create(
                client_name=data["client_name"],
                company=data["company"],
                defaults=data
            )
            if created:
                created_testimonials += 1
        self.stdout.write(self.style.SUCCESS(f"✓ Seeded {len(testimonials_data)} Testimonials ({created_testimonials} new)"))

        # 2. Seed Blog Categories
        categories_data = [
            {
                "name": "Safety & Statutory Compliance",
                "slug": "safety-compliance",
                "description": "Guides on IS 14665 standards, National Building Code (NBC), elevator licensing, and passenger safety protocols.",
                "display_order": 1,
            },
            {
                "name": "Technology & Innovation",
                "slug": "technology-innovation",
                "description": "Deep-dives into Gearless PMSM drives, IoT predictive maintenance, regenerative energy, and ARD backup systems.",
                "display_order": 2,
            },
            {
                "name": "Maintenance & AMC Best Practices",
                "slug": "maintenance-amc",
                "description": "Essential preventative maintenance routines, wire rope care, and lubrication schedules for facility managers.",
                "display_order": 3,
            },
            {
                "name": "Architecture & Cabin Design",
                "slug": "architecture-design",
                "description": "Shaft clearance calculations, pit-less villa lift planning, luxury titanium SS interiors, and glass aesthetics.",
                "display_order": 4,
            },
        ]

        category_objs = {}
        for cdata in categories_data:
            cat, _ = BlogCategory.objects.update_or_create(
                slug=cdata["slug"],
                defaults=cdata
            )
            category_objs[cat.slug] = cat
        self.stdout.write(self.style.SUCCESS(f"✓ Seeded {len(categories_data)} Blog Categories"))

        # 3. Seed Blog Posts
        posts_data = [
            {
                "category": category_objs["technology-innovation"],
                "title": "Gearless PMSM vs Geared Traction Elevators: Energy, Speed & Space Comparison",
                "slug": "gearless-pmsm-vs-geared-traction-elevators-comparison",
                "author": "Er. Pankaj Sharma (Head of R&D)",
                "reading_time": 5,
                "summary": "Understand why modern commercial and residential projects are rapidly switching to Permanent Magnet Synchronous Motors (PMSM) for up to 40% power savings and Machine Room-Less efficiency.",
                "content": (
                    "### The Evolution of Modern Elevator Traction Systems\n\n"
                    "For decades, the standard vertical transport system relied on geared induction motors coupled to a worm gear gearbox. "
                    "While reliable, traditional geared motors consume substantial electricity, generate friction heat, require regular oil changes, "
                    "and necessitate a bulky concrete machine room directly atop the elevator hoistway.\n\n"
                    "With the advent of Permanent Magnet Synchronous Motor (PMSM) technology, vertical mobility underwent a revolution. "
                    "Here is how modern gearless elevators compare against legacy geared systems:\n\n"
                    "#### 1. Energy Efficiency & Power Consumption\n"
                    "PMSM motors operate without mechanical gearboxes, eliminating mechanical transmission friction losses. "
                    "When paired with Variable Voltage Variable Frequency (V3F) regenerative drives, PMSM systems consume up to **35% - 40% less electrical energy**. "
                    "During descending trips with full load or ascending trips with light load, regenerative braking can even pump clean power back into the building grid.\n\n"
                    "#### 2. Machine Room-Less (MRL) Architecture\n"
                    "Because PMSM machines are ultra-compact and lightweight, they can be mounted directly onto the guide rails inside the top of the elevator hoistway. "
                    "This eliminates the costly and architecturally restrictive rooftop machine room, saving valuable terrace space and reducing building structural load.\n\n"
                    "#### 3. Ride Quality, Noise & Vibration\n"
                    "Geared systems produce audible hums and low-frequency vibrations due to tooth engagement in the gearbox. "
                    "Gearless PMSM direct-drive machines operate at whisper-quiet sound levels below 48 dB, ensuring a serene ambiance inside high-end residences and luxury hotel lobbies.\n\n"
                    "#### Conclusion\n"
                    "For any new construction or complete elevator overhaul, gearless PMSM technology delivers a rapid return on investment through power savings, zero oil maintenance, and superior passenger comfort."
                ),
                "featured": True,
                "meta_title": "Gearless PMSM vs Geared Traction Elevators | Krupa Elevator",
                "meta_description": "Comprehensive comparison between PMSM gearless and traditional geared elevator machines, covering energy efficiency, MRL layout, and ride acoustics.",
                "meta_keywords": "PMSM elevator, gearless lift, MRL elevator, elevator energy saving, V3F drive",
            },
            {
                "category": category_objs["safety-compliance"],
                "title": "Understanding IS 14665 & EN-81: Crucial Elevator Safety Directives Explained",
                "slug": "understanding-is-14665-en-81-elevator-safety-directives",
                "author": "Krupa Engineering Safety Committee",
                "reading_time": 6,
                "summary": "An in-depth breakdown of Indian Standard IS 14665 and European EN-81 standards for passenger elevators, encompassing overspeed governors, door interlocks, and car safety gears.",
                "content": (
                    "### Passenger Safety: The Non-Negotiable Core of Vertical Mobility\n\n"
                    "Elevators are statistically the safest mode of passenger transit in the world. This exceptional safety record is the result of "
                    "stringent engineering codes: primarily **Bureau of Indian Standards (IS 14665)** and international **EN-81** standards.\n\n"
                    "Every Krupa Elevator installation adheres to these critical safeguards:\n\n"
                    "#### 1. Progressive Safety Gear & Overspeed Governor (OSG)\n"
                    "The overspeed governor is a mechanical flywheel continuously monitoring car velocity. If cable breakage or traction slippage causes "
                    "the car to exceed 115% of rated speed, the OSG mechanically trips and wedges hardened steel wedges against the guide rails, stopping the car smoothly within inches.\n\n"
                    "#### 2. Infrared Multi-Beam Light Curtains\n"
                    "Gone are the days of rigid mechanical safety edges hitting passengers. Krupa installs dense 128-beam infrared invisible curtains "
                    "that span floor to ceiling. Any obstruction breaks the optical matrix, triggering an instantaneous door reopen before contact is made.\n\n"
                    "#### 3. Dual Electro-Mechanical Interlocks\n"
                    "Landing doors cannot be opened unless the elevator car is leveled precisely within ±5 mm of that floor sill. Dual mechanical locks "
                    "prevent accidental falls into the hoistway shaft.\n\n"
                    "#### 4. Automatic Rescue Device (ARD)\n"
                    "When city mains supply fails, the battery-backed microprocessor ARD takes over within seconds, slowly leveling the cabin to the nearest floor and opening the doors to safely discharge passengers.\n\n"
                    "Ensure your building management inspects statutory certificates annually and mandates regular brake inspection logs."
                ),
                "featured": True,
                "meta_title": "IS 14665 & EN-81 Elevator Safety Directives Explained",
                "meta_description": "Learn about the vital safety mechanisms mandated by IS 14665 and EN-81 standards: overspeed governors, safety gears, and infrared door curtains.",
                "meta_keywords": "IS 14665, EN-81 elevator, elevator safety, overspeed governor, ARD safety",
            },
            {
                "category": category_objs["maintenance-amc"],
                "title": "5 Preventative Maintenance Practices That Double Elevator Lifespan",
                "slug": "5-preventative-maintenance-practices-double-elevator-lifespan",
                "author": "Nilesh Jadav (Service Operations Manager)",
                "reading_time": 4,
                "summary": "Discover how proactive 52-point monthly inspections, traction rope tensioning, and electronic leveling calibration prevent costly breakdowns in residential and commercial buildings.",
                "content": (
                    "### Shifting from Reactive Repairs to Proactive Care\n\n"
                    "Many housing society committees make the mistake of calling technicians only after an elevator breaks down. "
                    "Reactive repairs result in prolonged passenger inconvenience, costly emergency parts replacements, and shortened equipment lifespan.\n\n"
                    "Here are five preventative maintenance protocols that double elevator durability:\n\n"
                    "#### 1. Hoist Cable Tension Equalization\n"
                    "Unequal tension across multi-strand steel wire ropes leads to accelerated sheave groove wear and cabin shudder. "
                    "Tension meters must be used every quarter to equalize rope loads across all cables.\n\n"
                    "#### 2. Brake Clearance & Lining Thickness Verification\n"
                    "The electro-mechanical holding brake is the primary safety stopper. Caliper air gaps must be calibrated within 0.2 to 0.3 mm, "
                    "and brake shoes inspected for glazed or oil-contaminated linings.\n\n"
                    "#### 3. Guide Rail Lubrication & Roller Guide Wear\n"
                    "Misaligned or dry guide rails create metallic groaning noises and jerk. Automatic wick oilers must be topped with approved "
                    "high-viscosity gear lubricants, or replaced with modern polyurethane roller guides that run lubrication-free.\n\n"
                    "#### 4. Landing Door Header & Roller Maintenance\n"
                    "Over 70% of elevator service calls originate from landing door contact dirt, worn hanger rollers, or misaligned sill grooves. "
                    "Keeping sill tracks free of construction debris and dusting microswitch contacts prevents door jams.\n\n"
                    "#### 5. Battery Health Checks for ARD & Emergency Lights\n"
                    "Lead-acid and SMF batteries inside Automatic Rescue Devices degrade after 24 to 36 months. Routine quarterly load testing "
                    "guarantees backup rescue functions flawlessly when a real blackout occurs."
                ),
                "featured": False,
                "meta_title": "5 Elevator Preventative Maintenance Practices | Krupa Elevator",
                "meta_description": "Essential preventative maintenance routines for building managers: rope tensioning, brake calibration, and door contact servicing.",
                "meta_keywords": "elevator maintenance, lift AMC, hoist rope tension, elevator brake inspection",
            },
            {
                "category": category_objs["architecture-design"],
                "title": "Planning a Private Home Elevator: Shaft Clearances, Pit Depth & Single-Phase Power",
                "slug": "planning-private-home-elevator-shaft-pit-single-phase",
                "author": "Krupa Architectural Advisory Desk",
                "reading_time": 5,
                "summary": "A comprehensive guide for architects and homeowners looking to incorporate stylish, pit-less, machine-room-less lifts in duplex homes and private bungalows.",
                "content": (
                    "### Integrating Vertical Luxury into Private Villas\n\n"
                    "A home elevator is no longer an extravagant luxury—it has become a necessity for elderly mobility, accessibility, and enhancing property valuation. "
                    "However, residential bungalows present unique structural constraints that standard commercial lifts cannot accommodate.\n\n"
                    "#### 1. Shallow Pit or Pit-Less Solutions\n"
                    "Standard commercial elevators require pit depths of 1,200 mm to 1,500 mm. In existing bungalows or rocky terrains, deep excavations are impossible. "
                    "Krupa's residential hydraulic and gearless home lifts require a nominal pit of just **200 mm**, or can be installed completely pit-less with a subtle 50 mm approach ramp.\n\n"
                    "#### 2. Minimal Overhead Headroom\n"
                    "Traditional elevators need 4,200 mm overhead height above the top landing. Krupa home elevator models function comfortably with standard ceiling heights as low as **2,800 mm**.\n\n"
                    "#### 3. Single-Phase 230V Domestic Power Operation\n"
                    "Most homes lack industrial 415V three-phase electrical power. Our energy-optimized home lifts utilize high-torque V3F drives that run "
                    "on standard domestic single-phase 230V electricity, drawing no more power than a standard household microwave or 1.5-ton AC unit.\n\n"
                    "#### 4. Bespoke Cabin Esthetics\n"
                    "From panoramic curved structural glass shafts to warm teakwood paneling and champagne titanium stainless steel, Krupa customizes "
                    "every cabin to reflect the interior theme of your dream residence."
                ),
                "featured": False,
                "meta_title": "Planning a Private Home Elevator | Shaft & Pit Requirements",
                "meta_description": "Architectural guidelines for bungalow home lifts: pit depth, overhead headroom, single-phase power, and panoramic glass designs.",
                "meta_keywords": "home elevator, villa lift, pitless elevator, residential lift Gujarat, hydraulic home lift",
            },
            {
                "category": category_objs["safety-compliance"],
                "title": "Hospital Elevator Design Standards: Stretcher Sizing, Jerk-Free Control & Hygiene",
                "slug": "hospital-elevator-design-standards-stretcher-sizing-hygiene",
                "author": "Er. Pankaj Sharma (Head of R&D)",
                "reading_time": 6,
                "summary": "Key technical requirements for medical elevators, including stretcher and ICU bed dimensions, anti-bacterial cabin finishes, and priority medical override controls.",
                "content": (
                    "### Vertical Transit in Critical Care Healthcare Facilities\n\n"
                    "Elevators in multi-speciality hospitals are critical life-support transit channels. When transporting post-operative patients, "
                    "ICU beds, or emergency trauma cases, ride smoothness, cabin dimensions, and leveling accuracy are paramount.\n\n"
                    "#### 1. Cabin Dimensions for Stretcher & Bed Access\n"
                    "Standard passenger lifts cannot accommodate modern intensive care beds with intravenous poles and life-support attachments. "
                    "Indian Standard IS 14665 specifies a minimum car depth of **2,400 mm** and width of **1,000 mm to 1,600 mm**, with clear telescopic door openings of at least 1,200 mm to 1,500 mm.\n\n"
                    "#### 2. Jerk-Free V3F S-Curve Acceleration\n"
                    "Patient comfort demands imperceptible acceleration and deceleration. Krupa medical lifts incorporate 32-bit closed-loop digital encoders "
                    "producing an ultra-smooth 'S-Curve' motion profile, eliminating any vestibular shock to recovering patients.\n\n"
                    "#### 3. Emergency Medical Service (EMS) Priority Override\n"
                    "During 'Code Blue' cardiac emergencies, authorized doctors and nurses can insert an emergency key into the landing station or cabin COP. "
                    "The lift immediately cancels all intermediate landing calls and rushes directly to the emergency department.\n\n"
                    "#### 4. Anti-Microbial Stainless Steel & Touchless Controls\n"
                    "Cabins are fabricated from high-grade SS 304 with copper-ion antimicrobial coatings, UV-C germicidal air sterilizers inside ceiling ducts, "
                    "and gesture-based touchless call buttons to combat hospital-acquired infections (HAIs)."
                ),
                "featured": False,
                "meta_title": "Hospital Stretcher Elevator Design Standards | Krupa Elevator",
                "meta_description": "Medical elevator engineering specifications: stretcher dimensions, jerk-free V3F control, code blue priority, and anti-bacterial hygiene.",
                "meta_keywords": "hospital elevator, stretcher lift, medical lift, code blue elevator, anti-microbial elevator cabin",
            },
            {
                "category": category_objs["technology-innovation"],
                "title": "How Internet of Things (IoT) is Revolutionizing Elevator Remote Monitoring",
                "slug": "how-iot-revolutionizes-elevator-remote-monitoring",
                "author": "Krupa Engineering Digital Team",
                "reading_time": 4,
                "summary": "Explore Krupa's smart cloud telemetry system that transmits real-time vibrations, door cycling metrics, and predictive error codes before breakdowns happen.",
                "content": (
                    "### The Era of Smart Connected Elevators\n\n"
                    "Elevator servicing has historically been episodic: an elevator stops, passengers report the problem, a technician travels to the site, "
                    "diagnoses the faulty sensor, orders parts, and completes the repair hours or days later.\n\n"
                    "Krupa Elevator is modernizing this workflow through embedded IoT edge controllers:\n\n"
                    "#### 1. 24/7 Cloud Telemetry Stream\n"
                    "Every microswitch state, V3F inverter current, door open/close cycle duration, and car acceleration waveform is captured by on-board sensors "
                    "and transmitted securely via 4G/5G gateways to Krupa's centralized operations command center.\n\n"
                    "#### 2. Predictive Failure Algorithms\n"
                    "If an optical door sensor experiences a 20 millisecond delay in closure due to dust accumulation, the system flags a predictive alert. "
                    "A field service engineer is dispatched during non-peak hours to clean the sensor before a passenger lockout occurs.\n\n"
                    "#### 3. Transparent Client Dashboard\n"
                    "Facility managers access a mobile portal providing live uptime percentages, total trip counts, power consumption statistics, "
                    "and scheduled maintenance visit reports with digital technician signatures.\n\n"
                    "Smart telemetry transforms building management from stressful firefighting to guaranteed vertical mobility."
                ),
                "featured": False,
                "meta_title": "IoT Remote Monitoring in Modern Elevators | Krupa Elevator",
                "meta_description": "Discover how IoT edge computing and predictive maintenance prevent elevator breakdowns and ensure transparent building management.",
                "meta_keywords": "IoT elevator, remote elevator monitoring, predictive lift maintenance, smart building",
            },
        ]

        created_posts = 0
        for pdata in posts_data:
            post, created = BlogPost.objects.update_or_create(
                slug=pdata["slug"],
                defaults=pdata
            )
            if created:
                created_posts += 1
        self.stdout.write(self.style.SUCCESS(f"✓ Seeded {len(posts_data)} Blog Posts ({created_posts} new)"))

        # 4. Seed Job Openings
        jobs_data = [
            {
                "title": "Senior Elevator Erection & Installation Engineer",
                "slug": "senior-elevator-erection-installation-engineer",
                "department": "Installation & Erection",
                "location": "Ahmedabad & Surat",
                "employment_type": "Full-Time Permanent",
                "experience_required": "4 - 7 Years in Elevator Mechanical/Electrical Erection",
                "education": "Diploma / B.E. in Mechanical or Electrical Engineering",
                "number_of_vacancies": 3,
                "description": (
                    "We are seeking an experienced Senior Elevator Erection Engineer to supervise turnkey installation projects across "
                    "residential and commercial developments in Gujarat. You will lead field technicians, oversee plumb-line laser hoistway alignment, "
                    "and execute rigorous pre-commissioning safety checks according to IS 14665."
                ),
                "responsibilities": (
                    "Manage on-site elevator mechanical erection, guide rail positioning, and counterweight assembly\n"
                    "Coordinate with client civil contractors and architects for shaft handover and power supply readiness\n"
                    "Execute wiring of controller panels, car operating panels (COP), and landing push buttons\n"
                    "Conduct no-load and full-load test runs, safety gear overspeed drop tests, and ARD commissioning\n"
                    "Ensure statutory government lift inspector requirements and safety compliance standards are met"
                ),
                "requirements": (
                    "Diploma / B.E. in Mechanical / Electrical Engineering or certified ITI Wireman\n"
                    "Minimum 4 years of proven field erection experience with traction and hydraulic elevator systems\n"
                    "In-depth working knowledge of V3F inverter programming, encoder calibration, and safety circuits\n"
                    "Strong leadership capabilities to direct teams of junior mechanics and assistant fitters\n"
                    "Valid driving license and willingness to travel across regional project sites"
                ),
                "benefits": (
                    "Competitive industry salary with project milestone bonuses\n"
                    "PF, ESIC, and comprehensive Group Personal Accident Insurance coverage\n"
                    "Travel, lodging, and daily field allowances\n"
                    "Technical skill advancement workshops and OEM certified training"
                ),
                "is_urgent": True,
                "display_order": 1,
            },
            {
                "title": "Preventative Maintenance & AMC Technician",
                "slug": "preventative-maintenance-amc-technician",
                "department": "Maintenance & AMC",
                "location": "Ahmedabad, Vadodara, Rajkot",
                "employment_type": "Full-Time Permanent",
                "experience_required": "2 - 5 Years in Lift AMC & Breakdown Troubleshooting",
                "education": "ITI Electrician / Wireman or Diploma in Electrical Engineering",
                "number_of_vacancies": 5,
                "description": (
                    "Join our elite service team responsible for maintaining high elevator reliability and passenger safety. "
                    "You will conduct monthly scheduled 52-point preventative inspections, diagnose electrical fault codes, "
                    "and respond swiftly to emergency breakdown calls within your assigned geographical route."
                ),
                "responsibilities": (
                    "Perform monthly preventative servicing: oiling, lubrication, brake adjustments, and door header cleaning\n"
                    "Inspect wire rope tension, traveling cables, safety switches, and landing door locks\n"
                    "Troubleshoot microprocessor controller fault codes, relay failures, and door inverter errors\n"
                    "Conduct battery health checks for emergency alarms, ARD units, and cabin car lights\n"
                    "Record digital service log reports and obtain sign-offs from residential society managers"
                ),
                "requirements": (
                    "ITI Wireman / Electrician or Diploma in Electrical Engineering\n"
                    "2+ years experience servicing passenger, goods, and hospital elevators\n"
                    "Familiarity with multi-meter testing, circuit diagrams, and controller error logs\n"
                    "Two-wheeler vehicle with valid driving license for mobile route visits\n"
                    "Customer-oriented attitude and calm demeanor during emergency troubleshooting"
                ),
                "benefits": (
                    "Fixed monthly salary + route completion incentives + overtime allowances\n"
                    "Company smartphone with digital service app\n"
                    "Annual safety gear and PPE kit provided\n"
                    "Full medical coverage and annual health checkups"
                ),
                "is_urgent": True,
                "display_order": 2,
            },
            {
                "title": "Lift Hoistway & Structural CAD Design Engineer",
                "slug": "lift-hoistway-structural-cad-design-engineer",
                "department": "Engineering & Design",
                "location": "Ahmedabad (Corporate Office)",
                "employment_type": "Full-Time Permanent",
                "experience_required": "3 - 6 Years in Elevator GA / Layout Drawing Preparation",
                "education": "B.E. / B.Tech in Mechanical Engineering or Diploma in CAD/Drafting",
                "number_of_vacancies": 2,
                "description": (
                    "We are looking for a meticulous CAD Design Engineer to create General Arrangement (GA) drawings, "
                    "hoistway layouts, machine room-less (MRL) structural configurations, and custom luxury cabin 3D models "
                    "for upcoming builder projects."
                ),
                "responsibilities": (
                    "Prepare detailed General Arrangement (GA) drawings, shaft cross-sections, and pit/overhead calculations\n"
                    "Coordinate with architects and structural consultants to resolve hoistway civil clearance discrepancies\n"
                    "Draft sheet-metal fabrication blueprints for custom SS 304 / titanium gold luxury cabin designs\n"
                    "Calculate guide rail bracket loads, car frame stresses, buffer reactions, and counterweight balance ratios\n"
                    "Maintain standard product catalog libraries and BOM (Bill of Materials) documentation"
                ),
                "requirements": (
                    "B.E. Mechanical Engineering or Diploma in Mechanical Drafting\n"
                    "Proficiency in AutoCAD 2D, SolidWorks / Inventor 3D, and sheet metal modeling\n"
                    "Thorough understanding of IS 14665 elevator dimensions and clearance regulations\n"
                    "Ability to interpret civil architectural blueprints and structural beam drawings\n"
                    "Strong analytical problem-solving and communication skills"
                ),
                "benefits": (
                    "Attractive corporate salary package based on CAD proficiency\n"
                    "Modern air-conditioned engineering office environment with high-end workstations\n"
                    "Performance bonuses and annual increments\n"
                    "Collaborative work culture with senior industry veterans"
                ),
                "is_urgent": False,
                "display_order": 3,
            },
            {
                "title": "Technical Sales & Elevator Estimation Executive",
                "slug": "technical-sales-elevator-estimation-executive",
                "department": "Technical Sales & Estimation",
                "location": "Ahmedabad & Mumbai",
                "employment_type": "Full-Time Permanent",
                "experience_required": "2 - 5 Years in Elevator, HVAC, or Building Material Sales",
                "education": "Any Graduate / B.E. / MBA in Marketing",
                "number_of_vacancies": 2,
                "description": (
                    "Drive sales growth for Krupa Elevator by building lasting relationships with property developers, "
                    "architecture firms, hospital infrastructure committees, and turnkey MEP contractors. Prepare customized "
                    "techno-commercial proposals and negotiate high-value elevator supply contracts."
                ),
                "responsibilities": (
                    "Identify new residential high-rise and commercial projects in designated sales territories\n"
                    "Meet architects, builders, and structural consultants to present Krupa product advantages\n"
                    "Analyze architectural drawings, determine elevator traffic capacity, and formulate accurate quotations\n"
                    "Conduct commercial negotiations, follow up on tenders, and secure project advance contracts\n"
                    "Collaborate with engineering and installation teams to ensure seamless project handover"
                ),
                "requirements": (
                    "Bachelor's degree in Engineering, Architecture, or Commerce / Business Administration\n"
                    "Proven track record in B2B technical equipment sales (preferably lifts, generators, HVAC, or facade systems)\n"
                    "Outstanding presentation, interpersonal negotiation, and proposal drafting skills\n"
                    "Self-motivated with strong closing ability and target orientation\n"
                    "Fluent in English, Hindi, and Gujarati"
                ),
                "benefits": (
                    "Lucrative fixed remuneration + uncapped quarterly sales commission\n"
                    "Mobile phone allowance and client entertainment expenses\n"
                    "Fast-track career path to Regional Sales Manager\n"
                    "Corporate travel allowances"
                ),
                "is_urgent": False,
                "display_order": 4,
            },
            {
                "title": "Quality Assurance & Safety Inspector (Elevators)",
                "slug": "quality-assurance-safety-inspector-elevators",
                "department": "Quality & Safety Inspection",
                "location": "Ahmedabad Works & Field Sites",
                "employment_type": "Full-Time Permanent",
                "experience_required": "5+ Years in Elevator Safety Audit & Factory QA",
                "education": "B.E. Mechanical / Electrical Engineering or Certified Safety Auditor",
                "number_of_vacancies": 1,
                "description": (
                    "Lead our quality assurance and safety auditing division. You will inspect incoming raw materials, "
                    "sheet metal fabrication tolerances, traction motor testing at factory works, and conduct pre-handover "
                    "field audits to guarantee zero defects."
                ),
                "responsibilities": (
                    "Inspect fabricated car frames, slings, guide shoes, and door headers against engineering tolerances\n"
                    "Witness high-voltage insulation tests, safety gear drop tests, and brake torque checks\n"
                    "Conduct surprise field safety audits on active installation sites for PPE and scaffolding compliance\n"
                    "Maintain ISO 9001 quality audit documentation and root-cause analysis for warranty claims\n"
                    "Certify final commissioning checklist before handing over elevators to clients"
                ),
                "requirements": (
                    "Degree/Diploma in Mechanical/Electrical with certified Quality/Safety credential\n"
                    "5+ years in elevator manufacturing QA or third-party safety inspection (e.g. TÜV, SGS)\n"
                    "Meticulous attention to detail and zero tolerance for safety shortcuts\n"
                    "Deep knowledge of IS 14665, EN-81, and National Building Code guidelines"
                ),
                "benefits": (
                    "Competitive senior compensation\n"
                    "Executive medical health coverage\n"
                    "Company vehicle / fuel allowance for site visits\n"
                    "Opportunity to shape company-wide safety culture"
                ),
                "is_urgent": False,
                "display_order": 5,
            },
        ]

        created_jobs = 0
        for jdata in jobs_data:
            job, created = JobOpening.objects.update_or_create(
                slug=jdata["slug"],
                defaults=jdata
            )
            if created:
                created_jobs += 1
        self.stdout.write(self.style.SUCCESS(f"✓ Seeded {len(jobs_data)} Job Openings ({created_jobs} new)"))

        self.stdout.write(self.style.SUCCESS("\n🎉 Successfully completed Phase 6 data seeding for Krupa Elevator!"))

