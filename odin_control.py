# -*- coding: utf-8 -*-
"""
ARES-SPACE TRANSPORT V4.0 — ODIN Autonomous Mission Control Subsystem
Author: Ranyellson Quintão
Description: Automated state machine for switching between Solar Thermal Cruise 
             and High-Thrust Chemical Landings/Lift-offs.
"""

class OdinFlightComputer:
    def __init__(self):
        self.flight_phase = "LEO_PARKED"
        self.mirrors_deployed = False
        self.active_propulsion = "NONE"
        self.cryo_zbo_status = "STEADY"
        self.electrical_margin_kw = 15.0 # Baseline solar array margin
        
    def transition_to_solar_cruise(self):
        """Prepares and engages the two Solar Thermal Propulsion (STP) units for deep space transit."""
        print("[ODIN STATUS] Transitioning to SOLAR_CRUISE mode...")
        self.flight_phase = "DEEP_SPACE_CRUISE"
        
        # Deploy mirrors in vacuum (Altitude must be above 400km to avoid aerodynamic drag)
        self.mirrors_deployed = True
        self.active_propulsion = "SOLAR_THERMAL_STP"
        self.cryo_zbo_status = "OPTIMIZED"
        
        print(" -> Inflatable parabolic mirrors: DEPLOYED (1250m² x2)")
        print(" -> Primary propulsion aligned: 2x STP Aerospike Cluster active")
        print(" -> Cryogenic cooling loop: ZBO active under mirror parasol shadow\n")
        
        return {
            "phase": self.flight_phase,
            "propulsion": self.active_propulsion,
            "mirrors": self.mirrors_deployed
        }
        
    def prepare_atmospheric_entry(self):
        """Critical safety gate: Deflates and secures mirror arrays before atmospheric interface or propulsive landing."""
        print("[ODIN CRITICAL ALERT] Atmospheric interface or terminal landing approach detected.")
        print(" -> Initiating emergency mirror retraction sequence...")
        
        # Mirrors must be completely hidden to avoid catastrophic aerodynamic tearing (RUD)
        self.mirrors_deployed = False
        self.active_propulsion = "NONE"
        self.flight_phase = "ATMOSPHERIC_ENTRY"
        
        print(" -> Inflatable mirrors: SECURED AND RECOILED INSIDE HULL")
        print(" -> Aerodynamic stress status: SAFE FOR RE-ENTRY\n")
        
        return self.mirrors_deployed
        
    def engage_chemical_landing(self, target_body="MARS"):
        """Activates the high-thrust secondary Methox ring engines for vertical propulsive landing."""
        if self.mirrors_deployed:
            raise RuntimeError("CRITICAL ERROR: Cannot fire chemical engines with solar mirrors deployed! Structural failure imminent.")
            
        print(f"[ODIN STATUS] Engaging CHEMICAL_LANDING on destination: {target_body}")
        self.flight_phase = f"{target_body}_TERMINAL_DESCENT"
        self.active_propulsion = "METHOX_CHEMICAL_RING"
        self.cryo_zbo_status = "STANDBY" # ZBO power repurposed for high-flow turbopumps
        
        print(f" -> Secondary propulsion online: High-thrust Liquid Methane/LOX ring engaged")
        print(f" -> Landing mode: Active guidance vertical propulsive descent engaged")
        print(f" -> Onboard computer verdict: Ready for touchdown on {target_body}\n")
        
        return {
            "phase": self.flight_phase,
            "propulsion": self.active_propulsion,
            "engine_status": "THROTTLING_NOMINAL"
        }

# Internal unit testing driver block
if __name__ == "__main__":
    odin = OdinFlightComputer()
    
    print("--- SIMULATING DEEP SPACE DEPARTURE FROM ALCANTARA ---")
    odin.transition_to_solar_cruise()
    
    print("--- SIMULATING APPROACH TO DESTINATION ---")
    odin.prepare_atmospheric_entry()
    
    try:
        odin.engage_chemical_landing(target_body="MARS")
    except RuntimeError as error:
        print(f"Abort system triggered: {error}")
