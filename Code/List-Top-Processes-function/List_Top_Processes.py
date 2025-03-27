# Function to list top processes by CPU usage
def list_processes():
    process_tree.delete(*process_tree.get_children())
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            info = proc.info
            processes.append((info['pid'], info['name'], info['cpu_percent']))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes = sorted(processes, key=lambda x: x[2], reverse=True)[:10]
    for proc in processes:
        process_tree.insert("",
                            "end",
                            values=(proc[0], proc[1], f"{proc[2]:.1f}%"))
