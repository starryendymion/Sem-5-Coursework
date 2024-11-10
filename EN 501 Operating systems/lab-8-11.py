import numpy as np

def is_safe_state(processes, available, max_need, allocation):
    n_processes = len(processes)
    n_resources = len(available)
    
    need = max_need - allocation
    finish = [False] * n_processes
    safe_sequence = []
    
    work = available.copy()
    
    while len(safe_sequence) < n_processes:
        found_process = False
        for i in range(n_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(n_resources)):
                work += allocation[i]
                finish[i] = True
                safe_sequence.append(processes[i])
                found_process = True
                break
        
        if not found_process:
            return False, []
    
    return True, safe_sequence

def request_resources(processes, available, max_need, allocation, process_id, request):
    n_resources = len(available)
    
    if any(request[j] > max_need[process_id][j] for j in range(n_resources)):
        raise ValueError("Error: Process has exceeded its maximum claim.")
    
    if all(request[j] <= available[j] for j in range(n_resources)):
        available_temp = available - request
        allocation_temp = allocation.copy()
        allocation_temp[process_id] += request
        max_need_temp = max_need.copy()
        max_need_temp[process_id] -= request
        
        safe, _ = is_safe_state(processes, available_temp, max_need_temp, allocation_temp)
        
        if safe:
            available -= request
            allocation[process_id] += request
            max_need[process_id] -= request
            return True
        else:
            print("Request cannot be granted as it leads to an unsafe state.")
            return False
    else:
        print("Resources are not available for this request.")
        return False

# Example usage
processes = [0, 1, 2, 3, 4]
available = np.array([3, 3, 2])

max_need = np.array([[7, 5, 3],
                     [3, 2, 2],
                     [9, 0, 2],
                     [2, 2, 2],
                     [4, 3, 3]])

allocation = np.array([[0, 1, 0],
                       [2, 0, 0],
                       [3, 0, 2],
                       [2, 1, 1],
                       [0, 0, 2]])

# Check if the current state is safe
safe, sequence = is_safe_state(processes, available, max_need, allocation)
if safe:
    print("The system is in a safe state.")
    print("Safe sequence:", sequence)
else:
    print("The system is not in a safe state.")

# Request resources for a process
process_id = 1  # Process making the request
request = np.array([1, 0, 2])

if request_resources(processes, available, max_need, allocation, process_id, request):
    print(f"Request granted for process {process_id}.")
    print("Updated available resources:", available)
    print("Updated allocation matrix:\n", allocation)
    print("Updated max need matrix:\n", max_need)
else:
    print(f"Request denied for process {process_id}.")
