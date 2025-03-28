import tkinter as tk
from tkinter import ttk, messagebox

# Initialize Deadlock Manager
deadlock_manager = DeadlockManager()

def check_deadlocks():
    deadlocked_processes = deadlock_manager.detect_deadlock()
    if deadlocked_processes:
        messagebox.showwarning("Deadlock Detected", f"Deadlock found in processes: {deadlocked_processes}")
    else:
        messagebox.showinfo("No Deadlock", "No deadlocks detected.")

# Create GUI
check_deadlock_button = ttk.Button(root, text="Check Deadlocks", command=check_deadlocks)
check_deadlock_button.pack(pady=5)

root.mainloop()
