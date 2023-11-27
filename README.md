# Setup

1. Activate python virtual environment
2. `pip install eth-ape`
3. `ape plugins install vyper`
4. `ape plugins install hardhat`
5. `ape plugins install foundry`
6. `npm i hardhat`
7. [Install foundry](https://book.getfoundry.sh/getting-started/installation) if not already installed

# Strange results
1. `if_greater1()` has the same logic as `if_greater2()` but the gas report results are different
2. The gas report for `uninitialize()` shows 4084 gas with a `default_provider` of foundry but only 304 gas with a `default_provider` of hardhat