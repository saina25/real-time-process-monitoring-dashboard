# Function to update CPU and memory stats
def update_stats():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    cpu_label.config(text=f"CPU: {cpu_usage:.2f}%")
    cpu_bar['value'] = cpu_usage

    memory_label.config(text=f"Memory: {memory_usage:.2f}%")
    memory_bar['value'] = memory_usage

    list_processes()
    root.after(2000, update_stats)  # Update every 2 seconds
