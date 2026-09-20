"""
Dual-Side Laser Hazard Marker (BX) System
Core Simulation and Controller Script
"""

class BXHazardMarkerSystem:
    def __init__(self, hazard_id="BX-001", power_mode="eco"):
        self.hazard_id = hazard_id
        self.power_mode = power_mode
        self.is_active = False
        self.left_laser_status = "OFF"
        self.right_laser_status = "OFF"

    def detect_hazard(self):
        print(f"[{self.hazard_id}] Road hazard/pothole detected. Initiating safety protocol...")
        self.is_active = True

    def activate_lasers(self):
        if self.is_active:
            self.left_laser_status = "ACTIVE (Cross-Beam Projecting)"
            self.right_laser_status = "ACTIVE (Cross-Beam Projecting)"
            print(f"[{self.hazard_id}] Dual-side high-visibility cross-lasers engaged.")
        else:
            print(f"[{self.hazard_id}] System inactive. Lasers offline.")

    def get_status(self):
        return {
            "hazard_id": self.hazard_id,
            "is_active": self.is_active,
            "left_laser": self.left_laser_status,
            "right_laser": self.right_laser_status,
            "power_mode": self.power_mode
        }

if __name__ == "__main__":
    print("Initializing Dual-Side Laser Hazard Marker (BX) System...")
    bx_marker = BXHazardMarkerSystem(hazard_id="BX-INDIA-01")
    bx_marker.detect_hazard()
    bx_marker.activate_lasers()
    print("System Status Report:", bx_marker.get_status())
  
