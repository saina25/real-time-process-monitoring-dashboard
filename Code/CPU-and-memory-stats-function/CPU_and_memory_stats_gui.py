# CPU and Memory Frame
stats_frame = ttk.LabelFrame(root, text="System Stats", padding=5)
stats_frame.pack(fill="x", padx=5, pady=5)

cpu_label = ttk.Label(stats_frame, text="CPU: 0%")
cpu_label.pack(anchor="w", padx=5, pady=2)
cpu_bar = ttk.Progressbar(stats_frame, mode='determinate')
cpu_bar.pack(fill="x", padx=5, pady=2)

memory_label = ttk.Label(stats_frame, text="Memory: 0%")
memory_label.pack(anchor="w", padx=5, pady=2)
memory_bar = ttk.Progressbar(stats_frame, mode='determinate')
memory_bar.pack(fill="x", padx=5, pady=2)
