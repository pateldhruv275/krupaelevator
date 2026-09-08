from django.core.management.base import BaseCommand
from products.models import ProductCategory, Product


class Command(BaseCommand):
    help = "Seeds initial elevator product categories and models for Krupa Elevator"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding Krupa Elevator product categories and products..."))

        categories_data = [
            {
                "name": "Passenger Elevator",
                "slug": "passenger-elevator",
                "short_description": "Smooth, high-speed vertical mobility engineered for high-rise residential societies and commercial towers.",
                "description": (
                    "Krupa Passenger Elevators are crafted to move occupants swiftly, quietly, and comfortably. "
                    "Utilizing next-generation PMSM gearless technology and advanced microprocessor group supervisory controls, "
                    "our passenger lifts minimize wait times and ensure millimeter-accurate floor leveling."
                ),
                "icon": "bi-person-walking",
                "display_order": 1,
                "meta_title": "Passenger Elevators | High Speed Lifts | Krupa Elevator",
                "meta_description": "Engineered passenger lifts for residential and commercial complexes with energy saving V3F drives.",
                "meta_keywords": "passenger elevator, commercial lift, high speed elevator, passenger lift manufacturer",
                "products": [
                    {
                        "name": "Gearless High-Speed Passenger Elevator",
                        "slug": "gearless-high-speed-passenger-elevator",
                        "short_description": "High-efficiency traction passenger elevator for modern multi-story residential towers and IT parks.",
                        "description": (
                            "Engineered for heavy passenger traffic, the Gearless High-Speed Passenger Elevator features synchronous "
                            "permanent magnet motor technology. It delivers whisper-silent acceleration, regenerative braking, "
                            "and smart destination dispatch for buildings up to 40 floors."
                        ),
                        "capacity": "8 to 26 Persons (544 kg - 1768 kg)",
                        "speed": "1.0 m/s to 2.5 m/s",
                        "number_of_stops": "Up to 40 Stops (G+39)",
                        "drive_type": "Regenerative Closed-Loop V3F Microprocessor",
                        "machine_type": "Permanent Magnet Synchronous Motor (PMSM Gearless)",
                        "door_type": "Center Opening Automatic Stainless Steel Doors",
                        "application": "High-Rise Apartments, Commercial Corporate Towers, 5-Star Hotels",
                        "pit_depth": "1500 mm - 1800 mm",
                        "overhead": "4200 mm - 4800 mm",
                        "power_supply": "415V AC, 3-Phase, 50 Hz",
                        "features": (
                            "Full-height multi-beam infrared safety light curtains (128 beams)\n"
                            "Automatic Rescue Device (ARD) with maintenance-free battery pack\n"
                            "Overload warning indicator with audio-visual chime and door lock\n"
                            "Fireman emergency control switch and emergency intercom phone\n"
                            "Earthquake seismic sensor & automatic leveling stop\n"
                            "Regenerative drive converting gravitational potential into grid energy\n"
                            "Dynamic LED ceiling lighting with automatic eco-sleep standby mode"
                        ),
                        "technical_specifications": (
                            "Drive Control: VVVF Vector Closed-Loop Controller\n"
                            "Car Operating Panel (COP): 7-inch TFT Multi-media Display with Braille Buttons\n"
                            "Guide Rails: Machined T-Profile Heavy Steel Guides (T89/T127)\n"
                            "Braking System: Dual Independent Disc Caliper Brakes\n"
                            "Leveling Accuracy: +/- 3 mm with Optical Sensor Retargeting\n"
                            "Suspension: High-Tensile Steel Wire Ropes / Coated Polyurethane Belts\n"
                            "Safety Gear: Instantaneous / Progressive Bi-Directional Safety Clamp"
                        ),
                        "finishes": (
                            "Hairline Finished Stainless Steel (SS 304)\n"
                            "Titanium Gold Mirror Etched Floral Cabin Panels\n"
                            "Rose Gold Vibration Stainless Steel Finish\n"
                            "Granite / Italian Composite Marble Floor Tiles\n"
                            "Panoramic Half-Moon Rear Glass Wall"
                        ),
                        "featured": True,
                        "display_order": 1,
                    },
                    {
                        "name": "Eco-Smart Residential Passenger Lift",
                        "slug": "eco-smart-residential-passenger-lift",
                        "short_description": "Compact, energy-efficient passenger lift engineered for modern housing societies.",
                        "description": (
                            "An economical and space-optimized vertical transport solution for low and medium-rise residential buildings. "
                            "Combines low power draw with long component lifespan and low maintenance overhead."
                        ),
                        "capacity": "4 to 8 Persons (320 kg - 544 kg)",
                        "speed": "0.65 m/s to 1.0 m/s",
                        "number_of_stops": "Up to 12 Stops (G+11)",
                        "drive_type": "Microprocessor Integrated V3F Drive",
                        "machine_type": "Compact Gearless PMSM / Precision Geared",
                        "door_type": "Two-Panel Side Opening Telescopic Automatic",
                        "application": "Residential Societies, Low-Rise Apartments, Gated Communities",
                        "pit_depth": "1400 mm",
                        "overhead": "4000 mm",
                        "power_supply": "415V AC, 3-Phase or 230V Single-Phase",
                        "features": (
                            "Infrared door sensor protection\n"
                            "Emergency battery lowering (ARD)\n"
                            "Anti-vibration car frame suspension\n"
                            "LED illuminated push buttons with acoustic feedback"
                        ),
                        "technical_specifications": (
                            "Control Architecture: Microprocessor Serial Communication\n"
                            "Door Operator: VVVF Frequency Controlled Synchronous Belt Drive\n"
                            "Cab Flooring: Heavy Duty Anti-Skid PVC Matting\n"
                            "Emergency Lighting: Integrated Inverter Backup (4 Hours)"
                        ),
                        "finishes": (
                            "Brushed Satin Stainless Steel\n"
                            "Powder Coated RAL Designer Shades\n"
                            "Mirror Finish Rear Panel Accent"
                        ),
                        "featured": False,
                        "display_order": 2,
                    }
                ]
            },
            {
                "name": "Home Elevator",
                "slug": "home-elevator",
                "short_description": "Compact, luxurious, and pitless elevators engineered specifically for private villas, duplexes, and bungalows.",
                "description": (
                    "Krupa Home Elevators bring timeless elegance, accessibility, and effortless mobility to private residences. "
                    "Requiring minimal architectural modifications, no deep pit, and operating quietly on household single-phase electricity."
                ),
                "icon": "bi-house-heart",
                "display_order": 2,
                "meta_title": "Luxury Home Elevators | Villa Lifts | Krupa Elevator",
                "meta_description": "Premium villa and bungalow home elevators with pitless design and custom Italian finishes.",
                "meta_keywords": "home elevator, villa lift, bungalow lift, pitless home elevator, residential lift",
                "products": [
                    {
                        "name": "Luxury Bungalow & Villa Elevator",
                        "slug": "luxury-bungalow-villa-elevator",
                        "short_description": "Aesthetic, pitless residential lift designed to elevate private villas and luxury penthouses.",
                        "description": (
                            "Crafted with exquisite Italian-style finishes and ultra-quiet drive technology, "
                            "this home elevator connects multiple stories seamlessly. Can be installed inside existing stairwells "
                            "or self-supporting glass structures with minimal pit requirements."
                        ),
                        "capacity": "2 to 6 Persons (200 kg - 450 kg)",
                        "speed": "0.3 m/s to 0.5 m/s",
                        "number_of_stops": "Up to 6 Floors (G+5)",
                        "drive_type": "Hydraulic or PMSM Belt Traction",
                        "machine_type": "Ultra-Silent Gearless / Hydraulic Power Pack",
                        "door_type": "Automatic Glass Frameless Doors or Swing Glass Doors",
                        "application": "Private Villas, Duplex Penthouses, Heritage Bungalows",
                        "pit_depth": "Min. 150 mm - 250 mm (Pitless Ramp Option Available)",
                        "overhead": "Min. 2600 mm - 3000 mm",
                        "power_supply": "230V, Single-Phase Domestic Supply",
                        "features": (
                            "Runs on standard single-phase 230V domestic power socket\n"
                            "Ultra-quiet hydraulic or belt traction (under 45 dB)\n"
                            "Automatic ground floor return during home power cuts\n"
                            "Child safety locks and touch-screen car operating panel\n"
                            "Customizable self-supporting aluminum or glass shaft"
                        ),
                        "technical_specifications": (
                            "Safety Standards: EN 81-41 Machinery Directive Compliant\n"
                            "Drive Power: 2.2 kW High-Efficiency Motor\n"
                            "Shaft Footprint: Compact starting from 1000 mm x 1000 mm\n"
                            "Communication: Integrated Hands-free GSM Dialer to Mobile"
                        ),
                        "finishes": (
                            "Full 360-degree Laminated Clear Glass Enclosure\n"
                            "Champagne Gold Brushed Aluminum Frame\n"
                            "Warm Oak Wood Veneer Interior Walls\n"
                            "Custom Italian Onyx Backlit Marble Floor"
                        ),
                        "featured": True,
                        "display_order": 1,
                    }
                ]
            },
            {
                "name": "Hospital Elevator",
                "slug": "hospital-elevator",
                "short_description": "Spacious, jerk-free stretcher and bed elevators designed with precision leveling for critical medical transit.",
                "description": (
                    "Krupa Hospital Elevators are specifically designed to meet the rigorous demands of healthcare facilities. "
                    "Engineered with extra-deep cabins to accommodate patient stretchers, life-support ICU equipment, and medical personnel, "
                    "all backed by antibacterial surfaces and emergency priority override."
                ),
                "icon": "bi-hospital",
                "display_order": 3,
                "meta_title": "Hospital Elevators | Medical Stretcher Lifts | Krupa Elevator",
                "meta_description": "Jerk-free hospital stretcher elevators with priority dispatch and antibacterial cabins.",
                "meta_keywords": "hospital elevator, stretcher lift, medical bed elevator, patient elevator",
                "products": [
                    {
                        "name": "Critical Care Stretcher & Bed Elevator",
                        "slug": "critical-care-stretcher-bed-elevator",
                        "short_description": "Shock-free, high-precision leveling elevator for ICU beds, stretchers, and surgical teams.",
                        "description": (
                            "Features advanced S-curve acceleration curves that eliminate any sensation of jerk or vibration, "
                            "protecting post-operative patients and sensitive medical instruments during transit."
                        ),
                        "capacity": "15 to 26 Persons (1020 kg - 2000 kg)",
                        "speed": "0.75 m/s to 1.75 m/s",
                        "number_of_stops": "Up to 30 Stops (G+29)",
                        "drive_type": "Closed-Loop V3F Microprocessor with Priority Emergency Override",
                        "machine_type": "Heavy Duty PMSM Gearless Traction",
                        "door_type": "Two-Panel Center Opening or Telescopic Side Opening (1100 mm - 1300 mm clear opening)",
                        "application": "Multi-Speciality Hospitals, Surgical Trauma Centers, Nursing Homes",
                        "pit_depth": "1600 mm",
                        "overhead": "4400 mm",
                        "power_supply": "415V AC, 3-Phase, 50 Hz",
                        "features": (
                            "Medical Priority Control (Code Blue emergency key switch)\n"
                            "Infrared full-height multi-beam door safety protection\n"
                            "Antibacterial UV-C air purifier and copper ion cabin touchpoints\n"
                            "Extra-deep cabin dimensions accommodating standard hospital beds (1500 mm x 2400 mm)\n"
                            "Protective stainless steel bumper rails on all three interior walls\n"
                            "ARD with priority bed evacuation"
                        ),
                        "technical_specifications": (
                            "Leveling Precision: +/- 2 mm exact floor alignment for rolling wheels\n"
                            "Cab Wall Material: Heavy Gauge Medical Grade SS 304 Hairline\n"
                            "Cabin Ventilation: High-Volume Whisper Quiet Cross-Flow Blower Fan\n"
                            "Door Clearance: 1200 mm Wide x 2100 mm High"
                        ),
                        "finishes": (
                            "Medical Grade SS 304 Stainless Steel\n"
                            "Heavy Gauge Dual Wall Protection Bumpers\n"
                            "Anti-Bacterial Heavy Duty Vinyl Seamless Flooring"
                        ),
                        "featured": True,
                        "display_order": 1,
                    }
                ]
            },
            {
                "name": "Goods Elevator",
                "slug": "goods-elevator",
                "short_description": "Heavy-duty freight and cargo elevators engineered for warehouses, automotive plants, and heavy industrial cargo.",
                "description": (
                    "When moving tons of cargo, machinery, and pallets, Krupa Freight Elevators deliver unyielding strength and durability. "
                    "Built with reinforced steel car frames, heavy gauge diamond-plate steel flooring, and rugged mechanical interlocks."
                ),
                "icon": "bi-box-seam",
                "display_order": 4,
                "meta_title": "Heavy Goods Elevators | Freight Lifts | Krupa Elevator",
                "meta_description": "Industrial freight elevators and goods lifts engineered for heavy industrial material handling.",
                "meta_keywords": "goods elevator, freight lift, industrial elevator, cargo lift",
                "products": [
                    {
                        "name": "Heavy Industrial Freight & Cargo Elevator",
                        "slug": "heavy-industrial-freight-cargo-elevator",
                        "short_description": "Rugged material-handling elevator engineered for capacities from 1 ton up to 10 tons.",
                        "description": (
                            "Designed to withstand forklift loading and rugged factory usage. "
                            "Constructed with structural channel car slings, reinforced sub-frames, and heavy vertical bi-parting or collapsible gates."
                        ),
                        "capacity": "1,000 kg to 10,000 kg (1 Ton - 10 Tons)",
                        "speed": "0.25 m/s to 0.75 m/s",
                        "number_of_stops": "Up to 15 Floors (G+14)",
                        "drive_type": "Heavy Duty Geared Traction or Hydraulic Cylinder System",
                        "machine_type": "Traction Geared / Heavy Duty Hydraulic Twin Jack",
                        "door_type": "Manual Collapsible / Imperforate Gate / Power Bi-Parting Steel Doors",
                        "application": "Manufacturing Plants, Logistics Warehouses, Textile Mills, Automobile Factories",
                        "pit_depth": "1600 mm - 2200 mm",
                        "overhead": "4500 mm - 5200 mm",
                        "power_supply": "415V AC, 3-Phase, 50 Hz Heavy Duty Input",
                        "features": (
                            "Reinforced steel platform designed for forklift roll-on impact\n"
                            "Heavy-duty mechanical safety gear and slack rope safety switches\n"
                            "Robust chequered steel or aluminum anti-skid floor plates\n"
                            "Bright industrial IP65 protected illumination\n"
                            "Full interlocking landing and car door safety switches"
                        ),
                        "technical_specifications": (
                            "Car Sling: Channel Steel Welded Truss Structure\n"
                            "Guide Rails: Heavy Solid T-Steel Rails (T127 / T140)\n"
                            "Overload Device: Strain Gauge Load Cell with Audio Buzzer\n"
                            "Motor Protection: Thermal Overload and Phase Reversal Relay"
                        ),
                        "finishes": (
                            "Heavy Duty MS Fabricated Body with Industrial Epoxy Coating\n"
                            "Galvanized Steel Wall Protection\n"
                            "5 mm Thick Chequered Steel Plate Flooring"
                        ),
                        "featured": True,
                        "display_order": 1,
                    }
                ]
            },
            {
                "name": "Car Elevator",
                "slug": "car-elevator",
                "short_description": "Automotive vertical transfer systems engineered for multi-story car parking, showrooms, and luxury residences.",
                "description": (
                    "Krupa Automobile Elevators eliminate the need for space-wasting circular concrete ramps in modern parking garages. "
                    "Engineered with wide car platforms, precise guidance indicators, and dual front-and-rear through-door configurations."
                ),
                "icon": "bi-car-front",
                "display_order": 5,
                "meta_title": "Automobile & Car Elevators | Parking Lifts | Krupa Elevator",
                "meta_description": "Space-saving automobile elevators for luxury multi-story parking and automobile dealerships.",
                "meta_keywords": "car elevator, automobile lift, vehicle elevator, parking lift",
                "products": [
                    {
                        "name": "Automated Vehicle & Parking Elevator",
                        "slug": "automated-vehicle-parking-elevator",
                        "short_description": "Spacious car elevator for multi-tier parking complexes, luxury garages, and vehicle showrooms.",
                        "description": (
                            "Allows vehicles to be transported vertically between basement parking and rooftop decks safely. "
                            "Features optical tire position sensors and dual remote-control operation from inside the vehicle."
                        ),
                        "capacity": "3,000 kg to 5,000 kg (Full Size SUVs & Sedans)",
                        "speed": "0.25 m/s to 0.5 m/s",
                        "number_of_stops": "Up to 10 Stops (G+9)",
                        "drive_type": "Hydraulic Synchronous Cylinders or 4:1 Traction Geared",
                        "machine_type": "Heavy Duty PMSM Traction / Dual Hydraulic Ram",
                        "door_type": "4-Panel Center Opening Automatic Steel Doors (2600 mm wide)",
                        "application": "Commercial Parking Structures, Luxury Penthouse Garages, Automobile Dealerships",
                        "pit_depth": "1600 mm - 1900 mm",
                        "overhead": "4500 mm",
                        "power_supply": "415V AC, 3-Phase, 50 Hz",
                        "features": (
                            "Vehicle entry and exit guidance laser beams\n"
                            "Dual car operating panels accessible from driver side window\n"
                            "Through-type front and rear opening doors (drive-in, drive-out)\n"
                            "Heavy duty bumper guards along car perimeter\n"
                            "High payload capacity designed for heavy electric SUVs and luxury sedans"
                        ),
                        "technical_specifications": (
                            "Platform Dimensions: 3000 mm Width x 6000 mm Length x 2400 mm Height\n"
                            "Door Opening Size: 2600 mm Width x 2200 mm Height\n"
                            "Floor Plate: 6 mm Heavy Tear-Pattern Anti-Slip Steel Plate\n"
                            "Emergency Lowering: Hydraulic Manual Solenoid Valve Release"
                        ),
                        "finishes": (
                            "Industrial Grade Epoxy Paint with High Visibility Hazard Stripes\n"
                            "Galvanized Perforated Steel Wall Panels\n"
                            "High Impact Rubber Wheel Stops"
                        ),
                        "featured": False,
                        "display_order": 1,
                    }
                ]
            },
            {
                "name": "Scenic Elevator",
                "slug": "scenic-elevator",
                "short_description": "Architectural panoramic glass elevators providing captivating 360-degree vistas for malls, atriums, and hotels.",
                "description": (
                    "Turn the vertical journey into a breathtaking visual experience. "
                    "Krupa Scenic Elevators integrate seamlessly into building facades and soaring indoor atriums, "
                    "delivering architectural brilliance alongside whisper-quiet travel."
                ),
                "icon": "bi-eye",
                "display_order": 6,
                "meta_title": "Scenic & Panoramic Glass Elevators | Krupa Elevator",
                "meta_description": "Custom curved glass panoramic elevators engineered for shopping malls, luxury atriums, and hotels.",
                "meta_keywords": "scenic elevator, panoramic elevator, glass lift, observation elevator",
                "products": [
                    {
                        "name": "Architectural Panoramic Glass Elevator",
                        "slug": "architectural-panoramic-glass-elevator",
                        "short_description": "Curved and polygonal architectural glass elevators for shopping atriums and luxury hotels.",
                        "description": (
                            "Constructed with multi-layered laminated safety glass and minimalist stainless steel structural frames. "
                            "Features concealed mechanicals and under-car LED ambient lighting that accentuates the building architecture."
                        ),
                        "capacity": "8 to 20 Persons (544 kg - 1360 kg)",
                        "speed": "1.0 m/s to 2.0 m/s",
                        "number_of_stops": "Up to 30 Stops (G+29)",
                        "drive_type": "Regenerative V3F Gearless Traction",
                        "machine_type": "Permanent Magnet Synchronous Machine (PMSM)",
                        "door_type": "Full Frameless Laminated Glass Automatic Doors",
                        "application": "Luxury Malls, Corporate Headquarters Atriums, 5-Star Resorts",
                        "pit_depth": "1500 mm",
                        "overhead": "4400 mm",
                        "power_supply": "415V AC, 3-Phase, 50 Hz",
                        "features": (
                            "Curved circular or polygonal high-strength laminated safety glass (10+10 mm PVB)\n"
                            "Minimalist stainless steel structural glass fittings\n"
                            "Concealed car top and bottom mechanical shroud covers with LED mood lighting\n"
                            "Air-conditioned cabin climate control integration\n"
                            "Emergency battery rescue with glass door release"
                        ),
                        "technical_specifications": (
                            "Glass Spec: Double Laminated Heat-Strengthened Float Glass\n"
                            "Car Sling: Custom Cantilever / Centralized Observation Frame\n"
                            "Door System: Synchronous Glass Door Operator with Hidden Mechanisms\n"
                            "Lighting: Dynamic Color Temperature Changing LED Ceiling & Skirting"
                        ),
                        "finishes": (
                            "Mirror Titanium Gold Stainless Steel Skeleton\n"
                            "Satin Hairline SS 304 Architectural Trims\n"
                            "Polished White Thassos Marble Flooring"
                        ),
                        "featured": True,
                        "display_order": 1,
                    }
                ]
            },
            {
                "name": "Hydraulic Elevator",
                "slug": "hydraulic-elevator",
                "short_description": "Reliable low-rise vertical transit utilizing smooth fluid power with no overhead machine room requirements.",
                "description": (
                    "Krupa Hydraulic Elevators provide robust lifting capacity with exceptionally low overhead requirements. "
                    "Ideal for low-rise buildings, factories, luxury homes, and situations where overhead hoistway headroom is restricted."
                ),
                "icon": "bi-droplet",
                "display_order": 7,
                "meta_title": "Hydraulic Elevators | Low Headroom Lifts | Krupa Elevator",
                "meta_description": "High-load hydraulic elevators with compact power packs and minimal pit depth.",
                "meta_keywords": "hydraulic elevator, hydraulic lift, low rise elevator, pitless lift",
                "products": [
                    {
                        "name": "Precision Hydraulic Passenger & Freight Lift",
                        "slug": "precision-hydraulic-passenger-freight-lift",
                        "short_description": "Smooth hydraulic elevator system engineered for low-rise buildings with low headroom.",
                        "description": (
                            "Driven by precision hydraulic power units with proportional control valves, "
                            "delivering shock-free starts and smooth stops without needing a rooftop penthouse machine room."
                        ),
                        "capacity": "4 to 20 Persons (300 kg - 1500 kg)",
                        "speed": "0.3 m/s to 0.63 m/s",
                        "number_of_stops": "Up to 6 Floors (G+5)",
                        "drive_type": "Submerged Motor Hydraulic Power Pack with Proportional Electronic Valve",
                        "machine_type": "Direct Acting or Indirect 2:1 Hydraulic Piston",
                        "door_type": "Automatic Stainless Steel or Manual Swing Doors",
                        "application": "Low-Rise Commercial Buildings, Factories, Private Residences, Showrooms",
                        "pit_depth": "1200 mm",
                        "overhead": "3400 mm (Low Headroom)",
                        "power_supply": "415V AC, 3-Phase or 230V Single-Phase",
                        "features": (
                            "No overhead machine room required (power unit can be placed up to 10m away)\n"
                            "Exceptionally smooth acceleration with electronic servo valve modulation\n"
                            "Emergency gravity lowering valve guarantees descent during total power outages\n"
                            "Low ongoing maintenance and fewer moving mechanical wear parts\n"
                            "Quiet submerged power unit acoustic enclosure"
                        ),
                        "technical_specifications": (
                            "Power Pack: GMV / Bucher Precision Proportional Valve Unit\n"
                            "Cylinder: Ground and Polished Heavy Wall Seamless Steel Ram\n"
                            "Rupture Valve: Instantaneous Velocity Check Valve on Cylinder Inlet\n"
                            "Oil Cooling: Air-Oil Heat Exchanger System"
                        ),
                        "finishes": (
                            "Brushed Satin Stainless Steel\n"
                            "Scratch-Resistant Textured PVC Laminate\n"
                            "Durable Granite Composite Flooring"
                        ),
                        "featured": False,
                        "display_order": 1,
                    }
                ]
            },
            {
                "name": "MRL Elevator",
                "slug": "mrl-elevator",
                "short_description": "Machine Room-Less elevators optimizing architectural space, structural cost, and building aesthetics.",
                "description": (
                    "Machine Room-Less (MRL) technology represents the modern benchmark for vertical mobility. "
                    "By mounting a compact gearless PMSM motor directly inside the top of the elevator hoistway, "
                    "MRL eliminates the bulky rooftop penthouse, reducing building construction costs and energy usage."
                ),
                "icon": "bi-gear",
                "display_order": 8,
                "meta_title": "Machine Room-Less (MRL) Elevators | Krupa Elevator",
                "meta_description": "Advanced MRL gearless elevators eliminating rooftop machine rooms with up to 40% energy savings.",
                "meta_keywords": "MRL elevator, machine room less elevator, gearless MRL lift, space saving lift",
                "products": [
                    {
                        "name": "Next-Gen MRL Gearless Traction Elevator",
                        "slug": "next-gen-mrl-gearless-traction-elevator",
                        "short_description": "Space-saving Machine Room-Less elevator engineered with synchronous permanent magnet technology.",
                        "description": (
                            "Designed for contemporary architects who desire a clean rooftop horizon without bulky machine rooms. "
                            "Delivers 40% electricity savings and exceptionally smooth riding comfort."
                        ),
                        "capacity": "6 to 16 Persons (408 kg - 1088 kg)",
                        "speed": "1.0 m/s to 1.75 m/s",
                        "number_of_stops": "Up to 24 Stops (G+23)",
                        "drive_type": "Microprocessor Integrated Regenerative V3F Controller",
                        "machine_type": "PMSM Ultra-Compact Gearless Traction Motor inside Hoistway",
                        "door_type": "Center Opening Automatic Stainless Steel Doors",
                        "application": "Modern Residential Towers, Boutique Hotels, Corporate Offices",
                        "pit_depth": "1400 mm",
                        "overhead": "3800 mm - 4000 mm",
                        "power_supply": "415V AC, 3-Phase, 50 Hz",
                        "features": (
                            "No rooftop machine room required – saves concrete structural costs\n"
                            "Permanent magnet synchronous gearless motor operates at 85%+ efficiency\n"
                            "Lubrication-free eco-friendly design with no gear oil changes needed\n"
                            "Thin controller cabinet installed flush beside the top landing door\n"
                            "Full automatic rescue device (ARD) with maintenance-free batteries"
                        ),
                        "technical_specifications": (
                            "Motor Dimensions: Compact Disk PMSM with High Torque Density\n"
                            "Machine Location: Mounted on Guide Rails at Shaft Head\n"
                            "Controller Location: Integrated into Top Landing Door Jamb\n"
                            "Energy Classification: VDI 4707 Energy Efficiency Class A"
                        ),
                        "finishes": (
                            "Hairline SS 304 Stainless Steel Panels\n"
                            "Titanium Black Mirror Finish Accent Lines\n"
                            "High-Lux LED Downlight Ceiling Panel"
                        ),
                        "featured": True,
                        "display_order": 1,
                    }
                ]
            },
            {
                "name": "Dumbwaiter",
                "slug": "dumbwaiter",
                "short_description": "Compact vertical service lifts engineered for hotels, restaurants, libraries, and hospitals to move food, books, and supplies.",
                "description": (
                    "Krupa Service Dumbwaiters provide efficient, sanitary vertical transport for small payloads. "
                    "Widely used in multi-level restaurants, banquet kitchens, luxury residences, hospitals, and libraries "
                    "to transfer dishes, medicines, documents, and linen effortlessly."
                ),
                "icon": "bi-archive",
                "display_order": 9,
                "meta_title": "Commercial & Kitchen Dumbwaiters | Food Lifts | Krupa Elevator",
                "meta_description": "Stainless steel kitchen dumbwaiters and small service lifts for restaurants, hotels, and residences.",
                "meta_keywords": "dumbwaiter, food lift, kitchen elevator, small service lift, restaurant lift",
                "products": [
                    {
                        "name": "Commercial Kitchen & Service Dumbwaiter",
                        "slug": "commercial-kitchen-service-dumbwaiter",
                        "short_description": "Food-grade stainless steel service dumbwaiter for restaurants, hotels, and luxury residences.",
                        "description": (
                            "Engineered with food-grade SS 304 sanitary car interiors, removable shelving, and bi-parting vertical doors. "
                            "Transfers dishes, wine bottles, laundry, and pharmaceutical supplies between floors swiftly."
                        ),
                        "capacity": "50 kg to 250 kg Payload",
                        "speed": "0.35 m/s to 0.5 m/s",
                        "number_of_stops": "Up to 8 Floors (G+7)",
                        "drive_type": "Worm Geared Traction Motor with Inverter Speed Control",
                        "machine_type": "Compact Machine Room Top/Bottom Drive",
                        "door_type": "Vertical Bi-Parting Stainless Steel Counterbalanced Doors",
                        "application": "Restaurants, Hotel Room Service Kitchens, Hospitals, High-End Homes, Libraries",
                        "pit_depth": "Counter Level Loading (Floor Pit Not Required) or 300 mm",
                        "overhead": "2800 mm",
                        "power_supply": "415V 3-Phase or 230V Single-Phase Domestic",
                        "features": (
                            "Food-grade SS 304 stainless steel cabin with removable perforated shelves\n"
                            "Counter-height floor loading for ergonomic dish tray handling\n"
                            "Intercom phone and arrival chime indicator at every station\n"
                            "Safe vertical bi-parting doors with electromechanical interlocks\n"
                            "Smooth jerk-free start and stop to prevent liquids from spilling"
                        ),
                        "technical_specifications": (
                            "Car Interior Dimensions: 600 mm x 600 mm x 800 mm (Customizable)\n"
                            "Car Door: Vertical Bi-Parting Stainless Steel Wire-Assisted\n"
                            "Call & Send Station: Push buttons with Arrival Buzzer and In-Use Indicator\n"
                            "Safety Device: Slack Rope Safety Gear with Limit Switches"
                        ),
                        "finishes": (
                            "Food-Grade Sanitary SS 304 Stainless Steel\n"
                            "Brushed Satin Exterior Landing Frames\n"
                            "Adjustable Intermediate Shelving Trays"
                        ),
                        "featured": False,
                        "display_order": 1,
                    }
                ]
            },
            {
                "name": "Escalator",
                "slug": "escalator",
                "short_description": "Continuous high-capacity moving stairways and walkways engineered for commercial malls, transit terminals, and airports.",
                "description": (
                    "Krupa Heavy-Duty Escalators and Moving Walkways ensure continuous, high-volume pedestrian circulation. "
                    "Engineered with precision trusses, energy-saving radar sensors, and multi-tier safety brakes."
                ),
                "icon": "bi-stairs",
                "display_order": 10,
                "meta_title": "Commercial Escalators & Moving Walkways | Krupa Elevator",
                "meta_description": "High throughput commercial escalators and moving walkways for shopping malls and airports.",
                "meta_keywords": "escalator, moving walkway, travelator, commercial escalator manufacturer",
                "products": [
                    {
                        "name": "Heavy-Traffic Commercial Escalator",
                        "slug": "heavy-traffic-commercial-escalator",
                        "short_description": "Reliable, high-volume moving stairway engineered for shopping malls, airports, and metro stations.",
                        "description": (
                            "Engineered for relentless operation with smooth step guidance, anti-slip aluminum step treads, "
                            "and smart VVVF auto-walk radar sensors that slow the unit when no passengers are approaching to conserve power."
                        ),
                        "capacity": "4,500 to 9,000 Passengers Per Hour",
                        "speed": "0.5 m/s",
                        "number_of_stops": "Floor-to-Floor Inclination: 30° / 35°",
                        "drive_type": "VVVF Intelligent Eco-Drive with Sleep Mode Radar",
                        "machine_type": "High-Efficiency Helical Gear Drive",
                        "door_type": "Tempered Safety Glass Balustrade (10 mm) with Rubber Handrails",
                        "application": "Retail Malls, Railway Stations, Airports, Exhibition Centers",
                        "pit_depth": "Standard Escalator Pit Dimensions",
                        "overhead": "Structural Ceiling Clearance as per Inclination Angle",
                        "power_supply": "415V AC, 3-Phase, 50 Hz",
                        "features": (
                            "Smart VVVF radar sensor switches escalator to eco-idle when vacant\n"
                            "Comb-plate safety switches stopping operation if foreign objects enter\n"
                            "Step sag detection and broken drive chain safety interlocks\n"
                            "Emergency stop buttons located at top, bottom, and central skirtings\n"
                            "Under-step yellow demarcation lighting and handrail inlet safety guards"
                        ),
                        "technical_specifications": (
                            "Step Width: 800 mm / 1000 mm Die-Cast Aluminum Steps\n"
                            "Balustrade: High Strength Transparent Laminated Glass Panels\n"
                            "Truss Structure: Rectangular Steel Pipe Structural Welded Truss\n"
                            "Handrail: Multi-Layer Synthetic Rubber Handrail with Steel Core"
                        ),
                        "finishes": (
                            "Transparent Crystal Balustrade Glass with Colored LED Lighting\n"
                            "Stainless Steel Hairline Cladding\n"
                            "Black / Colored Ergonomic Handrails"
                        ),
                        "featured": True,
                        "display_order": 1,
                    }
                ]
            },
        ]

        # Seed Categories and Products
        for cat_data in categories_data:
            prods = cat_data.pop("products")
            category, created = ProductCategory.objects.update_or_create(
                slug=cat_data["slug"],
                defaults=cat_data
            )
            status_text = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"[{status_text}] Category: {category.name}"))

            for prod_data in prods:
                prod_slug = prod_data.pop("slug")
                product, p_created = Product.objects.update_or_create(
                    slug=prod_slug,
                    category=category,
                    defaults=prod_data
                )
                p_status = "Created" if p_created else "Updated"
                self.stdout.write(f"    - [{p_status}] Product: {product.name}")

        self.stdout.write(self.style.SUCCESS("All 10 elevator product categories and products successfully seeded!"))
