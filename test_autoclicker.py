import unittest
import os
import json
from unittest.mock import patch, MagicMock
from autoclicker import AdvancedAutoClicker

class TestAdvancedAutoClicker(unittest.TestCase):
    
    def setUp(self):
        # Create test directory for profiles
        if not os.path.exists("test_profiles"):
            os.makedirs("test_profiles")
        
        # Patch the profiles directory
        self.patcher = patch('autoclicker.os.path.exists')
        self.mock_exists = self.patcher.start()
        self.mock_exists.return_value = True
        
        # Create clicker instance
        self.clicker = AdvancedAutoClicker()
        self.clicker.profiles = {}
        
    def tearDown(self):
        self.patcher.stop()
        # Clean up test directory
        if os.path.exists("test_profiles"):
            for f in os.listdir("test_profiles"):
                os.remove(os.path.join("test_profiles", f))
            os.rmdir("test_profiles")
    
    def test_set_click_speed(self):
        self.clicker.set_click_speed(0.05)
        self.assertEqual(self.clicker.click_speed, 0.05)
        
        # Test minimum speed limit
        self.clicker.set_click_speed(0.0005)
        self.assertEqual(self.clicker.click_speed, 0.001)
    
    def test_increase_decrease_speed(self):
        self.clicker.click_speed = 0.01
        
        self.clicker.increase_speed()
        self.assertAlmostEqual(self.clicker.click_speed, 0.01/1.5, places=4)
        
        self.clicker.decrease_speed()
        self.assertAlmostEqual(self.clicker.click_speed, 0.01, places=4)
    
    def test_cycle_click_type(self):
        self.clicker.click_type = "single"
        
        self.clicker.cycle_click_type()
        self.assertEqual(self.clicker.click_type, "double")
        
        self.clicker.cycle_click_type()
        self.assertEqual(self.clicker.click_type, "triple")
        
        self.clicker.cycle_click_type()
        self.assertEqual(self.clicker.click_type, "single")
    
    def test_cycle_click_button(self):
        self.clicker.click_button = "left"
        
        self.clicker.cycle_click_button()
        self.assertEqual(self.clicker.click_button, "right")
        
        self.clicker.cycle_click_button()
        self.assertEqual(self.clicker.click_button, "middle")
        
        self.clicker.cycle_click_button()
        self.assertEqual(self.clicker.click_button, "left")
    
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('json.dump')
    def test_save_profile(self, mock_json_dump, mock_open):
        self.clicker.click_speed = 0.05
        self.clicker.click_type = "double"
        self.clicker.click_button = "right"
        self.clicker.position = (100, 200)
        
        self.clicker.save_profile("test_profile")
        
        expected_profile = {
            "click_speed": 0.05,
            "click_type": "double",
            "click_button": "right",
            "position": (100, 200)
        }
        
        # Check if the profile was saved in memory
        self.assertIn("test_profile", self.clicker.profiles)
        self.assertEqual(self.clicker.profiles["test_profile"], expected_profile)
        
        # Check if file operations were called correctly
        mock_open.assert_called_once_with("profiles/test_profile.json", 'w')
        mock_json_dump.assert_called_once()
        args, kwargs = mock_json_dump.call_args
        self.assertEqual(args[0], expected_profile)
    
    @patch('builtins.open', new_callable=unittest.mock.mock_open, 
           read_data='{"click_speed": 0.03, "click_type": "triple", "click_button": "middle", "position": [150, 250]}')
    @patch('json.load')
    def test_load_profile(self, mock_json_load, mock_open):
        mock_json_load.return_value = {
            "click_speed": 0.03,
            "click_type": "triple",
            "click_button": "middle",
            "position": [150, 250]
        }
        
        with patch('os.path.exists', return_value=True):
            result = self.clicker.load_profile("test_profile")
        
        self.assertTrue(result)
        self.assertEqual(self.clicker.click_speed, 0.03)
        self.assertEqual(self.clicker.click_type, "triple")
        self.assertEqual(self.clicker.click_button, "middle")
        self.assertEqual(self.clicker.position, [150, 250])
        
        # Check if file operations were called correctly
        mock_open.assert_called_once_with("profiles/test_profile.json", 'r')
        mock_json_load.assert_called_once()

if __name__ == '__main__':
    unittest.main()
