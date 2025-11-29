import matplotlib.pyplot as plt
import random


class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time


def simulate_round_robin(processes, time_quantum):
    """Simulates RR and returns a list of execution slices for plotting."""
    current_time = 0
    queue = []
    execution_log = []  # Store (pid, start_time, end_time)
    n = len(processes)

    # Sort by arrival time
    processes.sort(key=lambda x: x.arrival_time)

    # Push initial processes to queue
    i = 0
    while i < n and processes[i].arrival_time <= current_time:
        queue.append(processes[i])
        i += 1

    completed = 0
    while completed < n:
        if not queue:
            if i < n:
                current_time = processes[i].arrival_time
                queue.append(processes[i])
                i += 1
            else:
                break  # Should not happen if logic is correct
            continue

        current_process = queue.pop(0)

        start_time = current_time
        execute_time = min(time_quantum, current_process.remaining_time)

        current_process.remaining_time -= execute_time
        current_time += execute_time
        end_time = current_time

        # Log the execution slice
        execution_log.append((current_process.pid, start_time, end_time))

        # Check for new arrivals
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1

        if current_process.remaining_time > 0:
            queue.append(current_process)
        else:
            completed += 1

    return execution_log


def plot_gantt_chart(execution_log, processes, time_quantum):
    """Plots a Gantt chart from the execution log."""
    fig, gnt = plt.subplots(figsize=(10, 5))

    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time Units')
    gnt.set_ylabel('Process ID')

    # Setting ticks on y-axis
    pids = sorted([p.pid for p in processes], reverse=True)
    gnt.set_yticks([i + 0.5 for i in range(len(pids))])
    gnt.set_yticklabels(pids)

    # Setting graph limits
    max_time = execution_log[-1][2] + 2
    gnt.set_xlim(0, max_time)
    gnt.set_ylim(0, len(pids) + 1)

    # Setting graph title
    gnt.set_title(f'Round Robin Scheduling Gantt Chart (Quantum = {time_quantum})')

    # Assign a unique color to each process
    colors = {}
    cmap = plt.get_cmap('tab10')  # Use a nice colormap
    for idx, pid in enumerate(pids):
        colors[pid] = cmap(idx)

    # Plotting the bars
    for pid, start, end in execution_log:
        duration = end - start
        # The bar is plotted at (start, y-index) with width=duration and height=0.8
        y_idx = pids.index(pid)
        gnt.broken_barh([(start, duration)], (y_idx + 0.1, 0.8), facecolors=colors[pid], edgecolor='black')
        # Add time labels on the bars for clarity
        gnt.text(start + duration / 2, y_idx + 0.5, str(end), ha='center', va='center', color='white',
                 fontweight='bold')

    # Adding a legend
    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[pid]) for pid in pids]
    gnt.legend(handles, pids, title="Processes")

    gnt.grid(True, axis='x', linestyle='--', alpha=0.6)

    # Ensure x-axis has a tick for every time unit for readability
    gnt.set_xticks(range(0, max_time + 1))

    plt.tight_layout()
    print("Displaying Gantt Chart...")
    plt.show()


# --- Main Execution ---
if __name__ == "__main__":
    # Case Study Data
    process_data = [
        Process("P1", 0, 5),
        Process("P2", 1, 4),
        Process("P3", 2, 2),
        Process("P4", 4, 1)
    ]
    quantum = 2

    print("--- Starting Simulation ---")
    # 1. Run the simulation to get the data
    # We need to pass copies so the original objects aren't modified for plotting setup
    import copy

    log = simulate_round_robin(copy.deepcopy(process_data), quantum)

    # 2. Plot the data on a Gantt chart
    plot_gantt_chart(log, process_data, quantum)