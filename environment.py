# -*- coding: utf-8 -*-
"""
ARES-SPACE TRANSPORT V4.0 — Cryogenic Environment & Thermal Shielding Module
Author: Ranyellson Quintão
"""

class MethaneStorageZBO:
    def __init__(self, initial_mass_tons=1130.0):
        self.max_capacity_tons = 1130.0
        self.current_mass_tons = initial_mass_tons
        self.tank_surface_area_m2 = 565.0       
        self.latent_heat_methane_j_kg = 510000   
        self.cryocooler_efficiency_cop = 0.05   # Operational COP at 110K
        self.cryocoolers_on = True
        
    def simulate_thermal_leak(self, days, distance_au):
        """Calculates structural thermal equilibrium and active pulse tube requirements."""
        external_thermal_flux = 400.0 / (distance_au ** 2)  
        mli_transmittance = 0.001                            # High-efficiency MLI baseline
        heat_leak_watts = self.tank_surface_area_m2 * external_thermal_flux * mli_transmittance
        
        if self.cryocoolers_on:
            evaporated_tons = 0.0
            electrical_power_watts = heat_leak_watts / self.cryocooler_efficiency_cop
            power_kw = electrical_power_watts / 1000.0
            energy_consumed_kwh = power_kw * 24.0 * days
            status = f"ZBO NORMAL: Fuel boiling completely locked at {power_kw:.2f} kWe draw."
        else:
            total_joules = heat_leak_watts * (days * 86400.0)
            evaporated_kg = total_joules / self.latent_heat_methane_j_kg
            evaporated_tons = evaporated_kg / 1000.0
            self.current_mass_tons -= evaporated_tons
            if self.current_mass_tons < 0: 
                self.current_mass_tons = 0.0
            energy_consumed_kwh = 0.0
            status = f"CRITICAL LEAK: Venting at {(evaporated_tons / days) * 1000:.2f} kg/day."
            
        return {
            "remaining_fuel_tons": round(self.current_mass_tons, 2),
            "lost_fuel_tons": round(evaporated_tons, 3),
            "cryo_power_used_kwh": round(energy_consumed_kwh, 2),
            "system_status": status
        }
