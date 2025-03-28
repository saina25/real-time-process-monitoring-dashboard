import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

# Create Matplotlib figure and axes for performance graphs
fig, ax = plt.subplots(2, 1, figsize=(5, 4))
cpu_usage_data = []
memory_usage_data = []
time_data = []

# Function to update performance graphs dynamically
def update_graph(frame):
    global cpu_usage_data, memory_usage_data, time_data
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    # Limit the data length to 20 points
    if len(cpu_usage_data) > 20:
        cpu_usage_data.pop(0)
        memory_usage_data.pop(0)
        time_data.pop(0)

    cpu_usage_data.append(cpu_usage)
    memory_usage_data.append(memory_usage)
    time_data.append(len(time_data))

    # Update CPU Usage Graph
    ax[0].cla()
    ax[0].plot(time_data, cpu_usage_data, label='CPU Usage', color='red')
    ax[0].set_title("CPU Usage")
    ax[0].set_ylim(0, 100)
    ax[0].legend()

    # Update Memory Usage Graph
    ax[1].cla()
    ax[1].plot(time_data, memory_usage_data, label='Memory Usage', color='blue')
    ax[1].set_title("Memory Usage")
    ax[1].set_ylim(0, 100)
    ax[1].legend()

# Embed the Matplotlib canvas into Tkinter GUI
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Update the graph every 2 seconds using FuncAnimation
ani = animation.FuncAnimation(fig, update_graph, interval=2000)
