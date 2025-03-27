# **Real-Time Process Monitoring Dashboard**  

Welcome to the Real-Time Process Monitoring Dashboard! This project provides an intuitive desktop application to monitor system performance by tracking CPU and memory usage, listing top processes, and enabling process termination using Python and Tkinter.

Table of Contents
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Dashboard Preview](#dashboard-preview)
- [How It Works](#how-it-works)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)
----
## Introduction

Real-time monitoring of system resources is essential for ensuring optimal system performance and managing processes efficiently. This project leverages Python, Tkinter and psutil to create a GUI-based application that displays CPU and memory usage, lists top processes, and provides the ability to terminate processes.

---
## Features
 
- **Real-time CPU & Memory Usage Monitoring**  
- **Displays Top 10 CPU-consuming Processes**  
- **Kill Selected Processes with One Click**  
- **Simple & User-Friendly Interface**
---
## Technologies Used

- Python
- Tkinter (for GUI)
- Psutil (for system information)
- Replit (Execution)
---
## Setup Instructions
1. Clone the repository: `git clone https://github.com/your-username/process-monitor.git
`
2. Navigate to the project folder:
`cd process-monitor
`
3. Install required dependencies: `pip install -r requirements.txt
`
4. Run the application: `python main.py
`
---
## Usage
- Ensure you have **Python 3.x** installed along with the required dependencies: `pip install psutil`
- Launch the application using python main.py.
- Monitor CPU and memory usage dynamically.
- View the top processes by CPU usage.
- Select a process from the list and click "Kill Process" to terminate it.

---
## Dashboard Preview
The application interface includes:
- CPU and memory usage progress bars.
- A list displaying the top processes by CPU usage.
- A button to terminate selected processes.

![Screenshot of the Real-time Dashboard](/images/system_performance.png")


---
## How It Works  
- Install dependencies(pip install psutil).
- Implement CPU & memory tracking.
- Display top processes dynamically.
- Add a kill process feature with exception handling.
- Test and refine UI for smooth operation.
- The application updates CPU and memory usage every **2 seconds**.  
- The **top 10 processes** consuming the most CPU are displayed.  
- To **terminate a process**, select it from the list and click **"Kill Process"**.
---  
## Future Enhancements
- Add sorting and filtering options for the process list.  
- Improve error handling for permission-restricted processes.  
- Implement a confirmation prompt before killing processes.  

---
## Acknowledgments
- Thanks to the Psutil library for providing seamless system monitoring.
- Special appreciation to the Tkinter community for extensive GUI resources.
---
## Contact
<a href="https://www.linkedin.com/in/anushikagupta/" target="_blank">Anushika Gupta</a><br>
<a href="https://www.linkedin.com/in/tanya-suratkal/" target="_blank">Tanya Suratkal</a><br>
<a href="http://www.linkedin.com/in/saina25" target="_blank">Saina Roy</a><br>

---

