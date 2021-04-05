#pytest test practice -example from semaphoreci.com

import pytest
from wallet import Wallet, InsufficientAmount

def test_default_intial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(30)
    wallet.spend_cash(20)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)



