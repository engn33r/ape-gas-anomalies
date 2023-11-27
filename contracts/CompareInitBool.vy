# @version 0.3.10
# pragma evm-version shanghai

initialized: public(bool)

@external
def __init__():
    self.initialized = True

@external
def uninitialize():
    self.initialized = False

@external
def reinitialize():
    self.initialized = True

@external
def is_initialized() -> bool:
    return self.initialized

