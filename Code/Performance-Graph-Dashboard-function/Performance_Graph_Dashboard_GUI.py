# performance_dashboard_gui.py
import tkinter as tk
from tkinter import ttk
from performance_dashboard import fig, update_graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

# Create GUI Window
root = tk.Tk()
root.title("Real-Time Performance Dashboard")
root.geometry("600x500")

# Graph Frame
graph_frame = ttk.LabelFrame(root, text="Performance Graphs", padding=5)
graph_frame.pack(fill="both", expand=True, padx=5, pady=5)

# Embed Matplotlib Figure
canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Start Animation
ani = animation.FuncAnimation(fig, update_graph, interval=2000)

root.mainloop()
