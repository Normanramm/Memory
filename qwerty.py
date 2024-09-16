import os
import psutil


def clear_memory():
    # Get current process
    current_process = psutil.Process(os.getpid())

    # Memory info before clearing
    memory_before = current_process.memory_info().rss / 1024 / 1024  # in MB
    print(f"Использование памяти перед очисткой: {memory_before} MB")

    # Perform garbage collection
    import gc
    gc.collect()

    # Memory info after clearing
    memory_after = current_process.memory_info().rss / 1024 / 1024  # in MB
    print(f"Использование памяти после очистки: {memory_after} MB")


clear_memory()