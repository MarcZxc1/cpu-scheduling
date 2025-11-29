import time


class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0


def round_robin_scheduler(processes, time_quantum):
    current_time = 0
    queue = []
    completed = 0
    n = len(processes)

    # Sort by arrival time first
    processes.sort(key=lambda x: x.arrival_time)

    # Push initial processes to queue
    i = 0
    while i < n and processes[i].arrival_time <= current_time:
        queue.append(processes[i])
        i += 1

    print(f"\n--- Starting Simulation (Time Quantum: {time_quantum}) ---")

    while completed < n:
        if not queue:
            # If queue is empty but processes remain, jump time
            if i < n:
                current_time = processes[i].arrival_time
                queue.append(processes[i])
                i += 1
            continue

        current_process = queue.pop(0)

        # Execute process
        execute_time = min(time_quantum, current_process.remaining_time)
        print(f"Time {current_time}: Process {current_process.pid} runs for {execute_time} units")

        current_process.remaining_time -= execute_time
        current_time += execute_time

        # Check for new arrivals while this process was running
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1

        # If process is not finished, put it back in queue
        if current_process.remaining_time > 0:
            queue.append(current_process)
        else:
            # Process Finished
            print(f"Time {current_time}: Process {current_process.pid} COMPLETED!")
            current_process.completion_time = current_time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed += 1

    print("--- Simulation Finished ---\n")


def print_table(processes):
    print(f"{'PID':<5} {'Arrival':<10} {'Burst':<10} {'Completion':<12} {'Turnaround':<12} {'Waiting':<10}")
    print("-" * 65)
    total_wt = 0
    total_tat = 0
    for p in processes:
        print(
            f"{p.pid:<5} {p.arrival_time:<10} {p.burst_time:<10} {p.completion_time:<12} {p.turnaround_time:<12} {p.waiting_time:<10}")
        total_wt += p.waiting_time
        total_tat += p.turnaround_time

    print("-" * 65)
    print(f"Average Waiting Time: {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time: {total_tat / len(processes):.2f}")


# --- CASE STUDY DATA ---
if __name__ == "__main__":
    # Case Study: 4 Processes arriving at different times
    # P1 arrives at 0, needs 5 units
    # P2 arrives at 1, needs 4 units
    # P3 arrives at 2, needs 2 units
    # P4 arrives at 4, needs 1 unit

    data = [
        Process("P1", 0, 5),
        Process("P2", 1, 4),
        Process("P3", 2, 2),
        Process("P4", 4, 1)
    ]

    quantum = 2
    round_robin_scheduler(data, quantum)
    print_table(data)