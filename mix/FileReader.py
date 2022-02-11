class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)
    def __enter__(self):
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
with CustomOpen('test.txt') as f:
    contents = f.read()
    print(contents)

from contextlib import contextmanager

@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

with custom_open('test.txt') as f:
    contents = f.read()
    print(contents)