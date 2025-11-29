Week 17: CPU Scheduling (Round Robin Case Study)

📂 Project Overview

This project demonstrates the Round Robin (RR) CPU scheduling algorithm. It contains two Python scripts: one for calculating the mathematical metrics (Waiting Time, Turnaround Time) and one for generating a visual Gantt Chart.

This software was created to satisfy the Week 17 requirement: "Present case study and created software for CPU Scheduling algorithm."

🚀 How to Use the Software

1. The Logic Script (cpu_scheduler.py)

This script simulates the CPU logic in text format. It shows exactly when processes start, stop, and finish.

How to Run:
Open your terminal or command prompt and type:

python cpu_scheduler.py


What it Output:

A step-by-step log of the CPU's actions (e.g., Time 2: Process P1 runs...).

A final summary table showing Turnaround Time and Waiting Time for each process.

2. The Visualizer Script (cpu_scheduling_vizualizer.py)

This script creates a graphical Gantt Chart to help the audience visualize the "time slices."

Prerequisites:
You must install the matplotlib library first:

pip install matplotlib


How to Run:

python cpu_scheduling_vizualizer.py


What it Outputs:

A window displaying a colored timeline. Each color represents a different process, showing how they share the CPU over time.

🧠 How the Code Works (Technical Explanation)

The software implements the Round Robin algorithm, which is a Preemptive algorithm. Here is the logic flow inside the code:

The Queue: We use a simple list to represent the "Ready Queue."

Sorting: Before starting, the code sorts all processes by arrival_time. Crucial Note: The code does not just run them in the order they were typed; it respects who arrived first.

The Time Quantum: We set a limit (e.g., quantum = 2).

The Loop:

The CPU picks the first process in the queue.

It calculates execute_time = min(time_quantum, remaining_time). This ensures we don't over-run if a process only needs 1ms but the quantum is 2ms.

It subtracts this time from the process's remaining_time.

Context Switch: If the process is not finished, it is appended to the end of the queue. If it is finished, we calculate its metrics.

New Arrivals: While a process is running, the code constantly checks if a new process has "Arrived" (reached the current time) and adds them to the queue immediately.

📚 Week 17 Lesson: CPU Scheduling

1. The Concept

Imagine a single waiter (the CPU) trying to serve 4 tables (Processes) at once. If the waiter spends 1 hour with Table 1 while everyone else waits, customers get angry.
CPU Scheduling is the set of rules the waiter follows to switch between tables fast enough so that everyone feels like they are being served simultaneously.

2. Key Terms Defined

Arrival Time (AT): The specific time on the clock when a process requests the CPU.

Note: This is NOT the index/position in the list. A process can be 1st in your list but arrive late (e.g., at Time 10).

Burst Time (BT): The total time a process needs to complete its job.

Time Quantum (TQ): The strict time limit (in milliseconds) a process is allowed to hold the CPU before being paused.

Waiting Time (WT): Turnaround Time - Burst Time. This measures how long a process sat idle in the queue doing nothing.

3. Case Study Walkthrough (The "Story")

We used the following data for our presentation:

P1: Needs 5ms (Arrives at 0)

P2: Needs 4ms (Arrives at 1)

P3: Needs 2ms (Arrives at 2)

P4: Needs 1ms (Arrives at 4)

Quantum: 2ms

The Timeline:

Time 0: P1 starts. Runs for 2ms. (Paused).

Time 2: P2 runs for 2ms. (Paused).

Time 4: P3 runs for 2ms. (Finished!)

Time 6: P1 runs again for 2ms. (Paused).

Time 8: P2 runs again for 2ms. (Finished!)

Time 10: P4 runs for 1ms. (Finished!)

Time 11: P1 runs its final 1ms. (Finished!)

4. Why Round Robin?

We chose Round Robin for this week's requirement because it is Fair.

In a "First-Come-First-Serve" system, P1 would have blocked everyone for 5 full milliseconds.

In Round Robin, P3 (a short task) was able to finish at Time 6, even though P1 (a long task) didn't finish until Time 12. This makes the system feel responsive and fast.