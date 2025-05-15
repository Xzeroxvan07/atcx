import pyautogui
import keyboard
import time
import threading
import json
import os
import argparse
from pynput import mouse
from datetime import datetime

class AdvancedAutoClicker:
    def __init__(self):
        self.clicking = False
        self.click_speed = 0.01  # Default: 0.01 seconds between clicks (100 CPS)
        self.position = None
        self.running = True
        self.click_thread = None
        self.click_count = 0
        self.start_time = None
        self.click_type = "single"  # single, double, triple
        self.click_button = "left"  # left, right, middle
        self.profiles = {}
        self.current_profile = "default"
        self.stats_thread = None
        
        # Create profiles directory if it doesn't exist
        if not os.path.exists("profiles"):
            os.makedirs("profiles")
            
        # Load default profile if it exists
        self.load_profile("default")
    
    def toggle_clicking(self):
        self.clicking = not self.clicking
        if self.clicking:
            self.start_time = datetime.now()
            self.click_count = 0
            print(f"Auto Clicking: ON - {self.click_speed}s delay ({1/self.click_speed:.1f} CPS)")
            
            if self.click_thread is None:
                self.click_thread = threading.Thread(target=self.auto_click)
                self.click_thread.daemon = True
                self.click_thread.start()
                
            if self.stats_thread is None:
                self.stats_thread = threading.Thread(target=self.show_stats)
                self.stats_thread.daemon = True
                self.stats_thread.start()
        else:
            print(f"Auto Clicking: OFF - Clicked {self.click_count} times")
    
    def set_click_speed(self, speed):
        self.click_speed = max(0.001, speed)  # Minimum 0.001s (1000 CPS)
        print(f"Click speed: {self.click_speed:.4f}s ({1/self.click_speed:.1f} CPS)")
    
    def increase_speed(self):
        self.set_click_speed(max(0.001, self.click_speed / 1.5))
        
    def decrease_speed(self):
        self.set_click_speed(self.click_speed * 1.5)
    
    def cycle_click_type(self):
        types = ["single", "double", "triple"]
        current_index = types.index(self.click_type)
        self.click_type = types[(current_index + 1) % len(types)]
        print(f"Click type: {self.click_type}")
    
    def cycle_click_button(self):
        buttons = ["left", "right", "middle"]
        current_index = buttons.index(self.click_button)
        self.click_button = buttons[(current_index + 1) % len(buttons)]
        print(f"Click button: {self.click_button}")
    
    def on_click(self, x, y, button, pressed):
        if pressed and button == mouse.Button.middle:
            # Middle mouse button sets the position
            self.position = (x, y)
            print(f"Position set to: {self.position}")
            return True
    
    def auto_click(self):
        while self.running:
            if self.clicking:
                try:
                    if self.position:
                        # Click at specified position
                        if self.click_type == "single":
                            pyautogui.click(self.position[0], self.position[1], button=self.click_button)
                        elif self.click_type == "double":
                            pyautogui.doubleClick(self.position[0], self.position[1], button=self.click_button)
                        elif self.click_type == "triple":
                            pyautogui.tripleClick(self.position[0], self.position[1], button=self.click_button)
                    else:
                        # Click at current position
                        if self.click_type == "single":
                            pyautogui.click(button=self.click_button)
                        elif self.click_type == "double":
                            pyautogui.doubleClick(button=self.click_button)
                        elif self.click_type == "triple":
                            pyautogui.tripleClick(button=self.click_button)
                    
                    self.click_count += 1
                    time.sleep(self.click_speed)
                except Exception as e:
                    print(f"Error clicking: {e}")
            else:
                time.sleep(0.1)  # Short sleep when not clicking
    
    def show_stats(self):
        while self.running:
            if self.clicking and self.start_time:
                elapsed = (datetime.now() - self.start_time).total_seconds()
                if elapsed > 0:
                    actual_cps = self.click_count / elapsed
                    print(f"Stats: {self.click_count} clicks in {elapsed:.1f}s | Actual CPS: {actual_cps:.1f}", end="\r")
            time.sleep(1)
            
    def save_profile(self, name):
        profile = {
            "click_speed": self.click_speed,
            "click_type": self.click_type,
            "click_button": self.click_button,
            "position": self.position
        }
        
        self.profiles[name] = profile
        
        # Save to file
        try:
            with open(f"profiles/{name}.json", 'w') as f:
                json.dump(profile, f, indent=4)
            print(f"Profile '{name}' saved successfully!")
            self.current_profile = name
        except Exception as e:
            print(f"Error saving profile: {e}")
    
    def load_profile(self, name):
        # Try to load from file
        try:
            if os.path.exists(f"profiles/{name}.json"):
                with open(f"profiles/{name}.json", 'r') as f:
                    profile = json.load(f)
                    
                self.click_speed = profile.get("click_speed", 0.01)
                self.click_type = profile.get("click_type", "single")
                self.click_button = profile.get("click_button", "left")
                self.position = profile.get("position", None)
                
                self.profiles[name] = profile
                self.current_profile = name
                print(f"Profile '{name}' loaded successfully!")
                return True
        except Exception as e:
            print(f"Error loading profile: {e}")
        
        return False
        
    def list_profiles(self):
        profiles = []
        
        # Get profiles from directory
        if os.path.exists("profiles"):
            profiles = [f[:-5] for f in os.listdir("profiles") if f.endswith(".json")]
        
        if profiles:
            print("\nAvailable profiles:")
            for p in profiles:
                if p == self.current_profile:
                    print(f" * {p} (active)")
                else:
                    print(f" - {p}")
        else:
            print("No saved profiles found.")
    
    def run(self):
        # Setup keyboard hotkeys
        keyboard.add_hotkey('f6', self.toggle_clicking)  # F6 to start/stop clicking
        keyboard.add_hotkey('f7', self.increase_speed)  # F7 to increase speed
        keyboard.add_hotkey('f8', self.decrease_speed)  # F8 to decrease speed
        keyboard.add_hotkey('f9', self.exit_program)  # F9 to exit
        keyboard.add_hotkey('f10', self.cycle_click_type)  # F10 to cycle click type
        keyboard.add_hotkey('f11', self.cycle_click_button)  # F11 to cycle click button
        keyboard.add_hotkey('f2', lambda: self.save_profile(self.current_profile or "default"))  # F2 to quick save
        keyboard.add_hotkey('f3', lambda: self.list_profiles())  # F3 to list profiles
        
        # Setup mouse listener for position setting
        listener = mouse.Listener(on_click=self.on_click)
        listener.start()
        
        print("\n========== Advanced Auto Clicker ==========")
        print("Controls:")
        print("F6: Start/Stop clicking")
        print("F7: Increase clicking speed")
        print("F8: Decrease clicking speed")
        print("F9: Exit program")
        print("F10: Cycle click type (single/double/triple)")
        print("F11: Cycle click button (left/right/middle)")
        print("F2: Quick save current profile")
        print("F3: List saved profiles")
        print("Middle mouse button: Set clicking position")
        print("=========================================")
        print(f"Current click speed: {self.click_speed:.4f}s ({1/self.click_speed:.1f} CPS)")
        print(f"Click type: {self.click_type}")
        print(f"Click button: {self.click_button}")
        if self.position:
            print(f"Position: {self.position}")
        print("=========================================\n")
        
        try:
            # Keep the program running
            while self.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.exit_program()
    
    def exit_program(self):
        print("\nExiting Auto Clicker...")
        self.clicking = False
        self.running = False
        keyboard.unhook_all()


def main():
    parser = argparse.ArgumentParser(description='Advanced Auto Clicker')
    parser.add_argument('--speed', type=float, default=0.01,
                        help='Initial clicking speed in seconds (default: 0.01)')
    parser.add_argument('--profile', type=str, default="default",
                        help='Load a saved profile')
    args = parser.parse_args()
    
    clicker = AdvancedAutoClicker()
    
    # Try to load profile, otherwise set speed
    if not clicker.load_profile(args.profile):
        clicker.set_click_speed(args.speed)
    
    clicker.run()

if __name__ == "__main__":
    main()
