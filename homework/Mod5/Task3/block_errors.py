class BlockErrors:
    def __init__(self, err_types):
        self.err_types = err_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            for err_type in self.err_types:
                if issubclass(exc_type, err_type):
                    return True
        return False 