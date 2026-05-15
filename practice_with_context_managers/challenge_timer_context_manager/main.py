import time

class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        self.elapsed = self.end_time - self.start_time         
        print(f"Elapsed time: {self.elapsed:.6f} seconds")

with Timer():
    total = 0
    for i in range(1000000):
        total += i