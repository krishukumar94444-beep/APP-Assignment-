
import gc
import time
import tracemalloc

# Enable memory tracking
tracemalloc.start()

# Display garbage collection status
print("Garbage Collection Enabled:", gc.isenabled())
print("Initial Garbage Collector Count:", gc.get_count())

# Function to create objects and circular references
def create_objects():
    objects = []

    for i in range(10000):
        a = []
        b = []
        a.append(b)
        b.append(a)

        objects.append(a)
        objects.append(b)

    return objects


# Create objects
print("\nCreating objects...")
objects = create_objects()

print("Objects created successfully.")
print("Garbage Collector Count:", gc.get_count())

# Remove references
print("\nDeleting object references...")
del objects

# Check memory before garbage collection
current_memory, peak_memory = tracemalloc.get_traced_memory()

print("\nMemory Before Manual Garbage Collection:")
print("Current Memory:", current_memory / 1024, "KB")
print("Peak Memory:", peak_memory / 1024, "KB")

# Perform manual garbage collection
start_time = time.time()

collected_objects = gc.collect()

end_time = time.time()

# Check memory after garbage collection
current_memory_after, peak_memory_after = tracemalloc.get_traced_memory()

print("\nManual Garbage Collection Performed")
print("Collected Objects:", collected_objects)

print("\nMemory After Garbage Collection:")
print("Current Memory:", current_memory_after / 1024, "KB")
print("Peak Memory:", peak_memory_after / 1024, "KB")

print("\nGarbage Collection Time:",
      (end_time - start_time) * 1000, "milliseconds")

# Stop memory tracking
tracemalloc.stop()

print("\nProgram completed successfully.")

Comment :-
Garbage Collection Enabled: True
Initial Garbage Collector Count: (....)

Creating objects...
Objects created successfully.
Garbage Collector Count: (....)

Deleting object references...

Memory Before Manual Garbage Collection:
Current Memory:  .... KB
Peak Memory:     .... KB

Manual Garbage Collection Performed
Collected Objects: 20000

Memory After Garbage Collection:
Current Memory:  .... KB
Peak Memory:     .... KB

Garbage Collection Time: .... milliseconds

Program completed successfully.
