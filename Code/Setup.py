# Create main window
root = tk.Tk()
root.title("Real-Time Process Monitoring DashBoard")
root.geometry("500x350")

# Start updating stats
update_stats()
root.mainloop()
