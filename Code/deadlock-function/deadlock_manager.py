import psutil
import networkx as nx
import threading
import time

class DeadlockManager:
    def __init__(self):
        self.lock = threading.Lock()
        self.resource_allocation = {}  # {pid: [resources]}
        self.waiting_processes = {}  # {pid: [resources]}
        self.graph = nx.DiGraph()

    def allocate_resource(self, pid, resource):
        with self.lock:
            if resource not in self.resource_allocation:
                self.resource_allocation[resource] = pid
                return True
            else:
                if pid not in self.waiting_processes:
                    self.waiting_processes[pid] = []
                self.waiting_processes[pid].append(resource)
                self.graph.add_edge(pid, self.resource_allocation[resource])
                return False

    def release_resource(self, pid, resource):
        with self.lock:
            if resource in self.resource_allocation and self.resource_allocation[resource] == pid:
                del self.resource_allocation[resource]
                for waiting_pid, resources in list(self.waiting_processes.items()):
                    if resource in resources:
                        resources.remove(resource)
                        if not resources:
                            del self.waiting_processes[waiting_pid]
                        self.allocate_resource(waiting_pid, resource)
                self.graph.remove_node(pid)

    def detect_deadlock(self):
        with self.lock:
            try:
                cycle = nx.find_cycle(self.graph, orientation='original')
                return [edge[0] for edge in cycle]
            except nx.NetworkXNoCycle:
                return None

    def recover_deadlock(self):
        deadlocked_processes = self.detect_deadlock()
        if deadlocked_processes:
            print(f"Recovering from deadlock. Terminating processes: {deadlocked_processes}")
            for pid in deadlocked_processes:
                try:
                    psutil.Process(pid).terminate()
                    print(f"Process {pid} terminated to resolve deadlock.")
                except psutil.NoSuchProcess:
                    print(f"Process {pid} no longer exists.")

    def monitor_deadlocks(self):
        while True:
            deadlocked = self.detect_deadlock()
            if deadlocked:
                print(f"Deadlock detected among processes: {deadlocked}")
                self.recover_deadlock()
            time.sleep(5)

# Initialize deadlock manager
deadlock_manager = DeadlockManager()
monitor_thread = threading.Thread(target=deadlock_manager.monitor_deadlocks, daemon=True)
monitor_thread.start()
