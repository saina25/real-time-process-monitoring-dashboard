import os

def simulate_deadlock():
    pid1 = os.getpid()  # Get the current process ID (simulating Process 1)
    pid2 = pid1 + 1  # Fake another process ID (simulating Process 2)
    
    resource1 = "Resource_A"
    resource2 = "Resource_B"

    # Process 1 requests Resource A
    allocated1 = deadlock_manager.allocate_resource(pid1, resource1)
    print(f"Process {pid1} allocated {resource1}: {allocated1}")

    # Process 2 requests Resource B
    allocated2 = deadlock_manager.allocate_resource(pid2, resource2)
    print(f"Process {pid2} allocated {resource2}: {allocated2}")

    # Now, both processes request each other's resources, causing a circular wait
    deadlock_manager.allocate_resource(pid1, resource2)  # Process 1 waits for Resource B
    deadlock_manager.allocate_resource(pid2, resource1)  # Process 2 waits for Resource A

    print("Deadlock simulated! Checking for deadlocks...")

# Run the simulation after the GUI starts
root.after(5000, simulate_deadlock)
