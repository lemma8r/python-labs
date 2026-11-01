import time
from contextlib import contextmanager

# Способ 1: На основе класса
class cm_timer_1:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"time: {self.end - self.start:.1f}")

# Способ 2: С использованием contextlib
@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    end = time.time()
    print(f"time: {end - start:.1f}")

if __name__ == '__main__':
    from time import sleep

    with cm_timer_1():
        sleep(1.5)

    with cm_timer_2():
        sleep(1.5)
