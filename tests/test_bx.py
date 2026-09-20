"""
Unit Tests for Dual-Side Laser Hazard Marker (BX) System
"""

import unittest
import sys
import os

# Add root directory to path to import bx_system
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bx_system import BXHazardMarkerSystem

class TestBXHazardMarkerSystem(unittest.TestCase):
    
    def setUp(self):
        self.bx = BXHazardMarkerSystem(hazard_id="TEST-BX-01", power_mode="eco")

    def test_initial_state(self):
        self.assertEqual(self.bx.hazard_id, "TEST-BX-01")
        self.assertFalse(self.bx.is_active)
        self.assertEqual(self.bx.left_laser_status, "OFF")
        self.assertEqual(self.bx.right_laser_status, "OFF")

    def test_hazard_detection(self):
        self.bx.detect_hazard()
        self.assertTrue(self.bx.is_active)

    def test_laser_activation(self):
        self.bx.detect_hazard()
        self.bx.activate_lasers()
        self.assertIn("ACTIVE", self.bx.left_laser_status)
        self.assertIn("ACTIVE", self.bx.right_laser_status)

    def test_status_report(self):
        status = self.bx.get_status()
        self.assertIsInstance(status, dict)
        self.assertEqual(status["power_mode"], "eco")

if __name__ == "__main__":
    unittest.main()
  
