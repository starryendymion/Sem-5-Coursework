class Process:
    def __init__(self, pid, burst_time, arrival_time):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

class SRTF:
    def __init__(self, processes):
        self.processes = processes
        self.n = len(processes)

    def find_waiting_time(self):
        t = 0  # Current time
        completed = 0  # Number of processes completed
        minm = float('inf')
        short = None
        check = False

        while completed != self.n:
            # Find the process with the minimum remaining time at time t
            for i in range(self.n):
                if (self.processes[i].arrival_time <= t and
                    self.processes[i].remaining_time < minm and
                    self.processes[i].remaining_time > 0):
                    minm = self.processes[i].remaining_time
                    short = i
                    check = True

            if not check:
                t += 1
                continue

            # Reduce the remaining time of the current shortest process
            self.processes[short].remaining_time -= 1

            # Update the minimum remaining time
            minm = self.processes[short].remaining_time
            if minm == 0:
                minm = float('inf')

            # If the process is completed
            if self.processes[short].remaining_time == 0:
                completed += 1
                check = False

                # Calculate finish time
                finish_time = t + 1

                # Calculate waiting time
                self.processes[short].waiting_time = finish_time - self.processes[short].burst_time - self.processes[short].arrival_time

                if self.processes[short].waiting_time < 0:
                    self.processes[short].waiting_time = 0

            t += 1

    def find_turnaround_time(self):
        for process in self.processes:
            process.turnaround_time = process.burst_time + process.waiting_time

    def find_avg_time(self):
        self.find_waiting_time()
        self.find_turnaround_time()

        total_wt = 0
        total_tat = 0

        # Display results
        print("Processes    Burst Time    Waiting Time    Turn-Around Time")
        for process in self.processes:
            total_wt += process.waiting_time
            total_tat += process.turnaround_time
            print(f"    {process.pid}\t\t{process.burst_time}\t\t{process.waiting_time}\t\t{process.turnaround_time}")

        # Calculate and display averages
        print(f"\nAverage waiting time = {total_wt / self.n:.5f}")
        print(f"Average turn around time = {total_tat / self.n:.5f}")

# Driver code
if __name__ == "__main__":
    # List of processes (pid, burst_time, arrival_time)
    processes = [
        Process(1, 6, 1),
        Process(2, 8, 1),
        Process(3, 7, 2),
        Process(4, 3, 3)
    ]

    srtf_scheduler = SRTF(processes)
    srtf_scheduler.find_avg_time()
