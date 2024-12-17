import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value, seed):
    random.seed(seed)
    array = [random.randint(1, max_value) for _ in range(n)]
    assert all(1 <= x <= max_value for x in array), "Generated value exceeds max_value"
    return array

def is_unique(array):
    return len(array) == len(set(array))

def measure_time(n, max_value, seed):
    array = generate_array(n, max_value, seed)

    start_time = time.perf_counter()
    _ = is_unique(array)
    end_time = time.perf_counter()

    return end_time - start_time

# Parameters
stambuk_last_3 = 50  
max_value = 250 - stambuk_last_3
n_values = [100, 150, 200, 250, 300, 350, 400, 500] 
seeds = [42, 43, 44, 45, 46]

worst_case_times = []
average_case_times = []

for n in n_values:
    # Measure times
    avg_times = []
    for seed in seeds:
        avg_times.append(measure_time(n, max_value, seed))

    # Calculate average and worst-case time
    average_case_times.append(sum(avg_times) / len(avg_times))
    worst_case_times.append(max(avg_times))

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(n_values, average_case_times, label="Average Case", marker="o")
plt.plot(n_values, worst_case_times, label="Worst Case", marker="x")
plt.title("Performance Analysis of Unique Element Check")
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.show()
