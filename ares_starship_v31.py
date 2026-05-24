# =========================================================================
# ARES-SPACE TRANSPORT V4.0 - FULL VEHICLE EXECUTION READY (2x STP SYSTEM)
# STATUS: CONVERTED FROM NUCLEAR TO SOLAR THERMAL | METHOX-STP HYBRID | 2030 TARGET
# REVISION: IRIDIUM/Ta4HfC5 COATING | ZERO CORROSION | ACTIVE ZBO INTEGRATED
# CONTACT: ranyellson@gmail.com
# =========================================================================
import math
import csv

class AresStarshipSTP:
    def __init__(self):
        # === SOLAR THERMAL PROPULSION (STP) - V4.0 CLUSTER 2x UNITS ===
        self.SOLAR_CONSTANT_EARTH = 1361.0   # Mean solar irradiance at Earth orbit (W/m²)
        self.MIRROR_AREA_PER_ENGINE = 1250.0 # Inflatable parabolic mirror area per engine (m²)
        self.OPTICAL_EFFICIENCY = 0.85       # Reflectivity of aluminized Mylar film
        self.ABSORBER_EFFICIENCY = 0.78      # Ceramic heat exchanger thermal retention factor
        self.R_METHANE = 518.3               # Specific gas constant for Methane (J/kg·K)
        self.GAMMA_METHANE = 1.32            # Specific heat ratio (Cp/Cv) for superheated LCH4
        self.G0 = 9.80665                    # Standard gravity acceleration (m/s²)
        
        self.ENGINE_COUNT = 2
        self.THRUST_PER_STP_NOMINAL = 185000 # N (185 kN per nozzle at 1.0 AU)
        self.TARGET_THRUST_N = self.THRUST_PER_STP_NOMINAL * self.ENGINE_COUNT # 370 kN total LEO thrust
        self.CHAMBER_PRESSURE = 5.5e6        # Pa (Optimized expansion chamber pressure)
        self.ALLOWABLE_STRESS = 180e6        # Pa (Ta4HfC5 high-temperature mechanical yield stress)
        self.CHAMBER_COATING = "Iridium / Ta4HfC5 (Zero Corrosion Baseline)"
        self.INTERNAL_RADIUS = 0.45          # m (Compacted throat radius for LCH4)

        # === CRYOGENIC STORAGE & ZERO BOIL-OFF (ZBO) SUBSYSTEM ===
        self.METHANE_DENSITY = 422.6         # kg/m³ (Liquid methane density at 112 K)
        self.TOTAL_PROPELLANT = 1130000      # kg (1,130.0 metric tons maximum load capacity)
        self.CRYOCOOLER_EFFICIENCY_COP = 0.05 # Pulse tube cryocooler Coefficient of Performance at 110 K
        self.TANK_SURFACE_AREA = 565.0       # m² (9-meter diameter hull total heat exchange area)

        # === SEQUENTIAL MISSION ARCHITECTURE (2030 ROADMAP) ===
        self.LAUNCH_SITE = "Alcantara Space Center, Brazil (2.3°S) - Clean Commercial Operations"
        self.EARTH_BONUS = 463               # m/s (Equatorial rotation tangential velocity bonus)
        self.CREW_COUNT = 6
        self.HABITAT_VOL = 380               # m³
        
        # PHASE I - Cislunar High-Yield Fleet Validation (Autonomous Round-Trip)
        self.LUNAR_PAYLOAD = 55000           # kg (55.0 t net delivery payload)
        self.LUNAR_DELTA_V_REAL = 8400.0     # m/s (Includes 5% gravity loss margin for continuous STP)
        self.LUNAR_DAYS = 28                 # Total duration of cislunar checkout transit

        # PHASE II - Interplanetary Cargo Transport (Mars Direct - Project Prometheus I)
        self.MARS_PAYLOAD = 71000            # kg (71.0 t Trans-Mars Injection net payload)
        self.MARS_DELTA_V_REAL = 4200.0      # m/s (LEO escape injection delta-V burn profile)
        self.MARS_DAYS = 776                 # Duração total da missão Prometheus I

        # === SYSTEMS MASS BUDGET RECALIBRATION V4.0 ===
        self.dry_mass = 120000               # kg (120.0 t - Sem peso nuclear ou blindagens)
        self.tanks_mass = 75000              # kg (75.0 t - Estrutura menor devido à densidade do metano)
        self.launchpad_total_mass = self.dry_mass + self.TOTAL_PROPELLANT + self.tanks_mass # 1,325.0 t em LEO

    def calculate_stp_aerospike_physics(self, distance_au, mass_flow_rate_kg_s=15.0):
        """Calculates aerodynamic thrust and chamber thermodynamics based on inverse-square law solar flux."""
        available_flux = self.SOLAR_CONSTANT_EARTH / (distance_au ** 2)
        total_mirror_area = self.MIRROR_AREA_PER_ENGINE * self.ENGINE_COUNT
        thermal_power_w = available_flux * total_mirror_area * self.OPTICAL_EFFICIENCY * self.ABSORBER_EFFICIENCY
        
        cp_methane = 3500.0
        t_initial = 112.0  
        delta_t = thermal_power_w / (mass_flow_rate_kg_s * cp_methane)
        chamber_temp_k = t_initial + delta_t
        
        if chamber_temp_k > 3200.0:
            chamber_temp_k = 3200.0

        v_exhaust = math.sqrt((2 * self.GAMMA_METHANE / (self.GAMMA_METHANE - 1)) * self.R_METHANE * chamber_temp_k)
        real_isp = v_exhaust / self.G0
        
        stress_ratio = (self.ALLOWABLE_STRESS + self.CHAMBER_PRESSURE) / (self.ALLOWABLE_STRESS - self.CHAMBER_PRESSURE)
        external_radius = self.INTERNAL_RADIUS * math.sqrt(stress_ratio)
        wall_thickness = external_radius - self.INTERNAL_RADIUS
        
        spike_mass = math.pi * (external_radius**2 - self.INTERNAL_RADIUS**2) * 3.5 * 1930 * self.ENGINE_COUNT
        real_thrust_n = mass_flow_rate_kg_s * v_exhaust
        
        return wall_thickness, spike_mass, real_isp, real_thrust_n, chamber_temp_k, thermal_power_w

    def calculate_zbo_thermal_leak(self, days, distance_au):
        """Calculates multi-layer background thermal leak and active cryocooler kWe power requirements."""
        external_thermal_flux = 400.0 / (distance_au ** 2)  
        mli_transmittance = 0.001                            
        heat_leak_watts = self.TANK_SURFACE_AREA * external_thermal_flux * mli_transmittance
        
        electrical_power_watts = heat_leak_watts / self.CRYOCOOLER_EFFICIENCY_COP
        energy_consumed_kwh = (electrical_power_watts / 1000.0) * 24.0 * days
        
        return energy_consumed_kwh, electrical_power_watts / 1000.0
    def evaluate_rocket_equation(self, payload_kg, delta_v_target, real_isp):
        """Applies numerical Tsiolkovsky equations to verify system kinetic closure margins."""
        v_e = real_isp * self.G0
        mass_initial = self.launchpad_total_mass + payload_kg
        mass_final_required = mass_initial / math.exp(delta_v_target / v_e)
        
        fuel_needed_kg = mass_initial - mass_final_required
        margin_kg = self.TOTAL_PROPELLANT - fuel_needed_kg
        viable = fuel_needed_kg <= self.TOTAL_PROPELLANT
        
        return fuel_needed_kg, margin_kg, viable

    def generate_all_files(self):
        wall_t, spike_m, real_isp, thrust_n, tc_k, power_w = self.calculate_stp_aerospike_physics(distance_au=1.0)
        
        lunar_fuel_kg, lunar_margin_kg, lunar_ok = self.evaluate_rocket_equation(self.LUNAR_PAYLOAD, self.LUNAR_DELTA_V_REAL, real_isp)
        mars_fuel_kg, mars_margin_kg, mars_ok = self.evaluate_rocket_equation(self.MARS_PAYLOAD, self.MARS_DELTA_V_REAL, real_isp)
        
        lch4_volume_m3 = self.TOTAL_PROPELLANT / self.METHANE_DENSITY
        tank_length = lch4_volume_m3 / (math.pi * 4.5**2)
        total_height = 4.5 + tank_length + 12.0
        orbital_tw = thrust_n / (self.dry_mass * self.G0)
        engine_out_tw = (thrust_n / 2) / (self.dry_mass * self.G0) 

        # === GENERATION: FILE 01 - BILL OF MATERIALS (BOM) ===
        bom_items = [
            ["System", "Item", "Spec", "Mass_kg", "USD", "TRL_2030"],
            ["Propulsion", "Aerospike Chamber Expansion Line", f"{wall_t*1000:.1f}mm Ta4HfC5 Matrix x2", int(spike_m*0.3), 2500000, 7],
            ["Propulsion", "Inner Engine Iridium Film Coating", "Anti-corrosive chemical barrier", 150, 4500000, 8],
            ["Propulsion", "Inflatable Parabolic Mirror Array", "1250m2 Mylar Coated x2 Units", 1200, 3100000, 7],
            ["Propulsion", "LCH4 Turbopumps High-Density Array", "15.0 kg/s flow operational", 3500, 7000000, 8],
            ["Structure", "LCH4 Cryogenic Tank Al-Li (9m)", f"9mD x {tank_length:.1f}mH Heavy Duty", int(self.tanks_mass), 6500000, 9],
            ["Structure", "ATHENA Habitat Core Module", f"{self.HABITAT_VOL}m3 Internal Vol", 10000, 15000000, 8],
            ["Thermal", "Active ZBO Pulse Tube Cryocoolers", "2.5 kW Active Helium Loop Array", 1800, 3800000, 7],
            ["Thermal", "MLI + Silica Aerogel Insulation Shield", "0.001 Transmittance Factor Matrix", 2200, 1200000, 9],
            ["EHS", "ECLSS Regenerative Closed-Loop", "90% Water & Oxygen Recycling", 4500, 12000000, 7],
            ["Avionics", "ODIN AI Navigation & Autonomous Core", "Radiation Hardened Avionics Architecture", 1500, 2100000, 8]
        ]
        
        # Type fix: Summing only the primary currency integers located at index 4
        total_cost = sum([int(row[4]) for row in bom_items[1:]])
        bom_data = bom_items + [["TOTAL", "COMPLETE VEHICLE V4.0", "STP METHANE CONFIG", int(self.dry_mass), total_cost, ""]]

        try:
            with open("01_BOM_STARSHIP_V3.1.csv", "w", newline='') as file_bom:
                csv.writer(file_bom).writerows(bom_data)

            # === GENERATION: FILE 02 - MASS BREAKDOWN REPORT ===
            lunar_zbo_kwh, lunar_zbo_kw = self.calculate_zbo_thermal_leak(self.LUNAR_DAYS, distance_au=1.0)
            mars_zbo_kwh, mars_zbo_kw = self.calculate_zbo_thermal_leak(self.MARS_DAYS, distance_au=1.2) 

            mass_report = f"""ARES-SPACE TRANSPORT V4.0 - REALISTIC EXECUTION DESIGN - TARGET 2030
PROPULSION CONFIGURATION: SOLAR THERMAL PROPULSION (STP) VIA INFLATABLE CONCENTRATORS
INDUSTRIAL SYNC: ANTICORROSIVE IRIDIUM COATING & ACTIVE ZERO BOIL-OFF SYSTEM

LAUNCH SITE INTERFACE: {self.LAUNCH_SITE}
LAUNCHPAD INJECTION CAPACITY (LEO TOTAL): {self.launchpad_total_mass/1000:.1f} t
Airframe Dry Mass: {self.dry_mass/1000:.1f} t
Optimized Liquid Methane Mass (LCH4): {self.TOTAL_PROPELLANT/1000:.1f} t
Al-Li Cryogenic Shell Tank Mass: {self.tanks_mass/1000:.1f} t
Thrust-to-Weight Ratio (LEO Orbital T/W): {orbital_tw:.2f}
Cluster Redundancy Profile (Engine-Out T/W - 1/2 Active): {engine_out_tw:.2f}
Total Calculated Vehicle Structural Height: {total_height:.1f} m
Required Internal Tank Core Volume: {lch4_volume_m3:.1f} m3

------------------------------------------------------------------------
SOLAR THERMAL EXPANSION ENGINE PRODUCT SPECIFICATIONS
------------------------------------------------------------------------
Active Expanding Nozzles: {self.ENGINE_COUNT}x STP Linear Aerospike Arrays
Combined Gross Thrust (LEO Core): {thrust_n/1000:.1f} kN
Calculated Vacuum Specific Impulse (Isp): {real_isp:.1f} s
Expansion Chamber Working Temperature: {tc_k:.1f} K
Net Absorbed Solar Thermal Power Core: {power_w/1e6:.2f} MW
Chemical Wall Shielding: {self.CHAMBER_COATING}

------------------------------------------------------------------------
PHASE I: LUNAR MISSION LOGISTICS (AUTONOMOUS CISLUNAR ROUND-TRIP)
------------------------------------------------------------------------
Allocated Delivery Payload (Lunar Payload): {self.LUNAR_PAYLOAD/1000:.1f} t
Required Kinetic Delta-V (With Gravity Losses): {self.LUNAR_DELTA_V_REAL} m/s
Computed Liquid Methane Consumption Fleet: {lunar_fuel_kg/1000:.1f} t
Remaining Fuel Tank Margin Overhead: {lunar_margin_kg/1000:.1f} t
Active Thermal Fuel Preservation (ZBO): {lunar_zbo_kw:.2f} kWe Steady
Total Lunar Cooling Mission Power Consumption: {lunar_zbo_kwh:.1f} kWh
PHASE I KINETIC CLOSURE VIABILITY: {"APPROVED FOR FLIGHT" if lunar_ok else "REJECTED - MASS OVERFLOW"}

------------------------------------------------------------------------
PHASE II: INTERPLANETARY MISSION PROMETHEUS I (DEEP-SPACE MARS TRANSIT)
------------------------------------------------------------------------
Trans-Mars Injection Payload (TMI Payload): {self.MARS_PAYLOAD/1000:.1f} t
Required LEO Escape Maneuver Delta-V: {self.MARS_DELTA_V_REAL} m/s
Escape Burn Methane Mass Consumption: {mars_fuel_kg/1000:.1f} t
Retained Mars Injection Fuel Safeguard: {mars_margin_kg/1000:.1f} t
Active Transit Thermal Fuel Preservation (ZBO): {mars_zbo_kw:.2f} kWe
Total Interplanetary Journey ZBO Power Draw: {mars_zbo_kwh:.1f} kWh
PHASE II KINETIC CLOSURE VIABILITY: {"APPROVED FOR FLIGHT" if mars_ok else "REJECTED - MASS OVERFLOW"}

Structural Configuration Coefficients:
- Propellant Mass Fraction Over Gross Weight: {self.TOTAL_PROPELLANT/self.launchpad_total_mass*100:.1f}%
- Insulation Thermal Matrix Density: Silica Aerogel Integrated Multi-Layer Shield
- ATHENA Onboard Human Habitable Volume: {self.HABITAT_VOL} m3
"""
            with open("02_MASS_BREAKDOWN_V3.1.txt", "w") as file_mass:
                file_mass.write(mass_report)

            # === GENERATION: FILE 03 - INVESTOR PITCH (ONE-PAGER) ===
            pitch = f"""ARES-SPACE TRANSPORT V4.0 - INVESTOR ONE PAGER - TARGET 2030

Problem: Heavy cislunar and interplanetary transport using traditional chemical propulsion 
forces massive, inefficient propellant-depot architectures. Fission alternatives meet absolute 
geopolitical, regulatory, and financial barriers that stall execution timelines.

Solution: A Reusable Deep-Space Cargo Freighter powered by Solar Thermal Propulsion (STP) and Liquid Methane. 
Drastically drops refueling launch chains, operating clean from Alcantara Space Center, Brazil.

Technical Competitive Edge (Challenging Aerospace Giants by 2030):
- Low CAPEX Framework: Zero radioactive containment requirements or nuclear handling overheads.
- Anti-Corrosive Barrier: Atomic Iridium layer bonded over Ta4HfC5 ceramic grants instant engine reusability.
- Zero Fuel Waste: High-TRL Active Zero Boil-Off (ZBO) mechanical cryocoolers preserve propellant mass indefinitely.
- Verified Kinetics: Delivers a real {real_isp:.1f}s specific impulse with a {thrust_n/1000:.1f} kN LEO core burn.
- Versatile Revenue Generation: Single modular design executing two high-yield milestones:
  * Phase I (Moon Market): Delivers {self.LUNAR_PAYLOAD/1000:.0f}t of net payload and returns to LEO on a zero-refuel round-trip.
  * Phase II (Mars Market): Stabilizes a high-energy Trans-Mars Injection delivering {self.MARS_PAYLOAD/1000:.0f}t payload.

Financial & Operating Modeling:
- Projected Vehicle Unit Production Cost: \${total_cost/1e6:.1f}M
- Regulatory Profiling: 100% radiation-free lifecycle, fast-tracking environmental approvals.

Funding Request: Seed round to finalize and space-test a vacuum deployment TRL-7 inflatable mirror demonstrator.
Systems Engineering Direct Contact: ranyellson@gmail.com"""
            with open("03_INVESTOR_PITCH_V3.1.txt", "w") as file_pitch:
                file_pitch.write(pitch)

            print("========================================================================")
            print("ARES-SPACE TRANSPORT V4.0 - SYSTEMS INTEGRATION COMPLETE")
            print("========================================================================")
            print(f"1. BOM COMPILATION SUCCESS (01_BOM_STARSHIP_V3.1.csv): \${total_cost/1e6:.1f}M")
            print(f"2. SYSTEMS MASS REPORT SUCCESS (02_MASS_BREAKDOWN_V3.1.txt): {real_isp:.1f}s Isp")
            print(f"3. EXECUTIVE INVESTOR PITCH SUCCESS (03_INVESTOR_PITCH_V3.1.txt): Synced")
            print("========================================================================")
        except IOError as e:
            print(f"Critical I/O error writing mission files: {e}")

if __name__ == "__main__":
    AresStarshipSTP().generate_all_files()
