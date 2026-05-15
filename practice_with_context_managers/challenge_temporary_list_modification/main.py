from contextlib import contextmanager

@contextmanager
def temp_append(lst, item):
    lst.append(item)
    try:
        yield
    finally:
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] == item:
                del lst[i]
                break

# Example usage:
numbers = [1, 2, 3]
with temp_append(numbers, 99):
    print("Inside context:", numbers)
print("Outside context:", numbers)