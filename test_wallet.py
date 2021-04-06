#pytest test practice -example from https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
#best practices/pointers for fixtures: use docstrings/ each test has its own new initialized class instance: Wallet() not one used in another test
# $pytest --fixtures allows you to view all available fixtures

import pytest


from wallet import Wallet, InsufficientAmount

#refactoring of tests to use the pytest fixture helper code 
# fixture functions are created by the decorator : @pytest.fixture
# reduces boilerplate code of instance 'wallet = Wallet(10) etc.'

#empty_wallet and wallet fixtures below initialize the Wallet() class in tests,
#where it is needed with different values

#parametrized test functions: test various combinations of these methods vs individual methods
#the pytest.mark.parametrize will run for each set of parameters earned/spent/expected 

@pytest.mark.parametrize('earned, spent, expected', [
    (30, 10, 20), 
    (20, 2, 18),
    ])

def test_transactions(earned, spent, expected): 
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet class instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet class instance with a balance of 20'''
    return Wallet(20)

#initial Tests written before app -- commented out == test before refactoring 
def test_default_intial_amount(empty_wallet):
    # wallet = Wallet()
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    # wallet = Wallet(100)
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    # wallet = Wallet(10)
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    # wallet = Wallet(30)
    wallet.spend_cash(10)
    assert wallet.balance == 10



def test_wallet_spend_cash_raises_exception_insufficient_amount(empty_wallet):
    # wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)



#combining test fixtues and parametrized test functions
#to refactor even more we can replace the wallet initialization with a test fixture

@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance '''
    return Wallet()

@pytest.mark.parametrize('earned, spent, expected', [
    (30, 10, 20), 
    (20, 2, 18),
    ])

def test_transactions(my_wallet, earned, spent, expected): 
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
