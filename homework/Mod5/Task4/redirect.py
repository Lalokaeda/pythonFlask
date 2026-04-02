import sys
from contextlib import contextmanager


@contextmanager
def redirect(stdout=None, stderr=None):
    original_stdout = sys.stdout
    original_stderr = sys.stderr

    if stdout is not None:
        sys.stdout = stdout
    if stderr is not None:
        sys.stderr = stderr

    try:
        yield
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr