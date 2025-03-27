# Function to kill a selected process
def kill_process():
    selected_item = process_tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Select a process to kill.")
        return
        
    try:
        pid = int(process_tree.item(selected_item[0])['values'][0])
        psutil.Process(pid).kill()
        messagebox.showinfo("Success", f"Process {pid} terminated.")
        list_processes()
    except Exception as e:
        messagebox.showerror("Error", f"Unable to kill process: {e}")
