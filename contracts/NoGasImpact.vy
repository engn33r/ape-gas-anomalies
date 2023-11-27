# pragma evm-version shanghai

diff: public(uint256)

@external
def __init__():
    self.diff = 1

@external
def if_greater1(a: uint256) -> uint256:
    b: uint256 = 0
    if a < 5:
        b = 1
    else:
        b = 2
    self.diff = b
    return b

@external
def if_greater2(a: uint256) -> uint256:
    b: uint256 = 0
    if a < 5:
        b = 1
    else:
        b = 2
    self.diff = b
    return b