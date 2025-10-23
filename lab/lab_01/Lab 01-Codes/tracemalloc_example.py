import tracemalloc

tracemalloc.start() # Start tracing memory allocations

# Your code 

snapshot = tracemalloc.take_snapshot() # Take a snapshot of the current memory allocations
stats = snapshot.statistics('lineno') # Get statistics for memory usage, sorted according to lineno

tracemalloc.stop() # Stop tracing memory allocations

print("Top 10 memory-consuming lines:")
for stat in stats[:10]:
    print(stat)
    
# We also find the total memory allocated by summing the memory allocations
total_allocated = sum(stat.size for stat in stats) / 1024 # e.g., in KiB
print("Total memory allocated: ", total_allocated)

