import multiprocessing
import importlib
import cube

LEN = 50
NUM_PROCESSES = 4

number_sequence = range(LEN)
result = multiprocessing.Array('i', LEN)
num_per_processes = LEN // NUM_PROCESSES
remaining = LEN % NUM_PROCESSES 
processes = []
start = 0

for i in range(NUM_PROCESSES):
    end = start + num_per_processes + (1 if i < remaining else 0)
    p = multiprocessing.Process(target=cube.func, args=(number_sequence, start, end, result))
    processes.append(p)
    p.start()
    start = end

for p in processes:
    p.join()

print(f"No. of Processes: {NUM_PROCESSES}")
print(f"Result: {list(result)}")