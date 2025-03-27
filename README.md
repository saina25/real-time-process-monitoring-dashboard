# **Real-Time Process Monitoring Dashboard**  

A simple **Tkinter-based** desktop application for monitoring system resource usage and managing running processes. This tool displays CPU and memory usage and lists the top processes by CPU consumption. Users can also **terminate** selected processes directly from the UI.  

## **Features**  
✅ **Real-time CPU & Memory Usage Monitoring**  
✅ **Displays Top 10 CPU-consuming Processes**  
✅ **Kill Selected Processes with One Click**  
✅ **Simple & User-Friendly Interface**  

## **Installation**  

### **Prerequisites**  
Ensure you have **Python 3.x** installed along with the required dependencies:  

```bash
pip install psutil
```

## **Usage**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Run the script:  
   ```bash
   python main.py
   ```

## **How It Works**  

- The application updates CPU and memory usage every **2 seconds**.  
- The **top 10 processes** consuming the most CPU are displayed.  
- To **terminate a process**, select it from the list and click **"Kill Process"**.  


## **Future Enhancements**  
🔹 Add sorting and filtering options for the process list.  
🔹 Improve error handling for permission-restricted processes.  
🔹 Implement a confirmation prompt before killing processes.  
