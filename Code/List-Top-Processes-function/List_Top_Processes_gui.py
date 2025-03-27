# Process List Frame
process_frame = ttk.LabelFrame(root, text="Top Processes", padding=5)
process_frame.pack(fill="both", expand=True, padx=5, pady=5)

columns = ("PID", "Name", "CPU %")
process_tree = ttk.Treeview(process_frame,
                            columns=columns,
                            show="headings",
                            height=8)
for col in columns:
    process_tree.heading(col, text=col)
    process_tree.column(col,
                        width=150 if col == "Name" else 70,
                        anchor="center")
process_tree.pack(fill="both", expand=True)
