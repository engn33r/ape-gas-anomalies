import pytest

@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]

@pytest.fixture(scope="session")
def payer(accounts):
    return accounts[1]

@pytest.fixture(scope="session")
def new_nogasimpact(project, owner):
    return owner.deploy(project.NoGasImpact)

@pytest.fixture(scope="session")
def new_compare_init_bool(project, owner):
    return owner.deploy(project.CompareInitBool)

@pytest.fixture(scope="session")
def new_compare_init_int(project, owner):
    return owner.deploy(project.CompareInitInt)
