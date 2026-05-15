from contextlib import contextmanager

some_value = 10

@contextmanager
def temporary_value(new_value):
    global some_value
    original = some_value
    some_value = new_value
    try:
        yield
    finally:
        some_value = original

print(f"Before: {some_value}")
with temporary_value(99):
    print(f"Inside: {some_value}")
print(f"After: {some_value}")