# Function to kill a selected process
def kill_process():
    selected_item = process_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Select a process to kill.")
        return
