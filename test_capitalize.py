#sample basic pytests from semaphoreci.com pytest tutorials

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('ciao') == 'Ciao'