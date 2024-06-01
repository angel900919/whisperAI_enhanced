import time
from memory_profiler import memory_usage


def monitor_resources(func, *args, **kwargs):
    """
    Monitors and reports the resource usage of a function including execution time and memory.

    Args:
        func: The function to monitor.
        args: Positional arguments to pass to the function.
        kwargs: Keyword arguments to pass to the function.

    Returns:
        The result of the function execution.
    """
    start_time = time.time()  # Start time
    mem_usage_before = memory_usage()  # Memory usage before function execution

    result = func(*args, **kwargs)  # Execute the function

    mem_usage_after = memory_usage()  # Memory usage after function execution
    end_time = time.time()  # End time

    print(f"Execution Time: {end_time - start_time} seconds")
    print(f"Memory Usage: {max(mem_usage_after) - min(mem_usage_before)} MB")

    return result
