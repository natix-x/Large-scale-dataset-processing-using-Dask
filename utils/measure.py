import time
import psutil
from utils.csv_saver import CSVSaver

def measure_time_and_memory(operation_name, cluster_type, input_size, csv_saver):
    def decorator(func):
        def wrapper(*args, **kwargs):
            mem_before = psutil.Process().memory_info().rss / 1e6
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed_time = time.perf_counter() - start_time
            mem_after = psutil.Process().memory_info().rss / 1e6
            used_memory = mem_after - mem_before

            print(f"[{operation_name}] Time: {elapsed_time:.4f}s | RAM usage: {used_memory:.2f}")
            csv_saver.save(operation_name, cluster_type, input_size, elapsed_time, used_memory)
            return result
        return wrapper
    return decorator
