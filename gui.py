import tkinter as tk
from tkinter import ttk
import threading
import subprocess

class ScenarioRunnerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scenario Runner GUI")
        
        # Set window size
        self.root.geometry("400x200")  # Set width to 400 pixels and height to 200 pixels
        
        # Create scenario label
        self.scenario_label = ttk.Label(root, text="Scenario:")
        self.scenario_label.place(relx=0.3, rely=0.4, anchor=tk.E)
        
        # Create scenario options
        self.scenario_options = ["FollowLeadingVehicle_1", "IntersectionCrossingScenario"]  # Add more scenarios as needed
        
        # Create scenario combobox
        self.scenario_combobox = ttk.Combobox(root, values=self.scenario_options, width=30)
        self.scenario_combobox.place(relx=0.6, rely=0.4, anchor=tk.CENTER)
        self.scenario_combobox.set(self.scenario_options[0])  # Set default value
        
        # Create run scenario button
        self.run_scenario_button = ttk.Button(root, text="Run Scenario", command=self.run_scenario)
        self.run_scenario_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Create run manual control button
        self.run_manual_control_button = ttk.Button(root, text="Run Manual Control", command=self.run_manual_control)
        self.run_manual_control_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        
    def run_scenario(self):
        scenario = self.scenario_combobox.get()
        command = ["python", "scenario_runner.py", "--reloadWorld"]
        
        if scenario:
            command.extend(["--scenario", scenario])
        
        # Run the subprocess in a separate thread
        threading.Thread(target=self.run_subprocess, args=(command,)).start()

    def run_manual_control(self):
        # Run the manual control subprocess in a separate thread
        threading.Thread(target=self.run_subprocess, args=(["python", "manual_control.py"],)).start()

    def run_subprocess(self, command):
        try:
            subprocess.run(command, check=True)
            print("Process completed successfully!")
        except subprocess.CalledProcessError as e:
            print("Error:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScenarioRunnerGUI(root)
    # Center the window on the screen
    root.eval('tk::PlaceWindow . center')
    root.mainloop()