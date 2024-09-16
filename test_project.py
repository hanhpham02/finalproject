from project import income, expenses, savings

def test_income():
    assert income("2024-07-01", "2024-07-05") == "Your income from 2024-07-01 00:00:00 to 2024-07-05 00:00:00 is: 440"

def test_expenses():
    assert expenses("2024-07-01", "2024-07-05") == "Your expense from 2024-07-01 00:00:00 to 2024-07-05 00:00:00 is: 120"

def test_savings():
    assert savings("2024-07-01", "2024-07-05") == "Your savings from 2024-07-01 00:00:00 to 2024-07-05 00:00:00 is: 320"