class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

class RoundRobinScheduler:
    def __init__(self, processes, quantum):
        self.processes = processes
        self.quantum = quantum
        self.n = len(processes)

    def find_waiting_time(self):
        t = 0  # Current time

        # Loop until all processes are done
        while True:
            done = True

            # Traverse through all processes one by one
            for process in self.processes:
                # If the remaining time of the process is greater than 0, it needs to be processed
                if process.remaining_time > 0:
                    done = False  # There is a pending process

                    if process.remaining_time > self.quantum:
                        # Increase the current time by quantum
                        t += self.quantum

                        # Decrease remaining time of the current process by quantum
                        process.remaining_time -= self.quantum
                    else:
                        # Increase the time by remaining time
                        t += process.remaining_time

                        # Waiting time is current time minus burst time
                        process.waiting_time = t - process.burst_time

                        # Process is fully executed
                        process.remaining_time = 0

            # If all processes are done, exit the loop
            if done:
                break

    def find_turnaround_time(self):
        # Turnaround time = burst time + waiting time
        for process in self.processes:
            process.turnaround_time = process.burst_time + process.waiting_time

    def find_avg_time(self):
        self.find_waiting_time()
        self.find_turnaround_time()

        total_wt = 0
        total_tat = 0

        # Display process information
        print("Processes    Burst Time    Waiting Time    Turn-Around Time")
        for process in self.processes:
            total_wt += process.waiting_time
            total_tat += process.turnaround_time
            print(f"    {process.pid}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

        # Calculate and display average times
        print(f"\nAverage waiting time = {total_wt / self.n:.5f}")
        print(f"Average turn around time = {total_tat / self.n:.5f}")

# Driver code
if __name__ == "__main__":
    # List of processes (pid, burst_time)
    processes = [
        Process(1, 10),
        Process(2, 5),
        Process(3, 8)
    ]

    # Time quantum
    quantum = 2

    scheduler = RoundRobinScheduler(processes, quantum)
    scheduler.find_avg_time()
