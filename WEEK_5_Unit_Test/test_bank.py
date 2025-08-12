



from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("Hello, Mr Hlungwane") == 0

def test_h():
    assert value("hey") == 20
    assert value("HEY") == 20
    assert value("Hey") == 20
    assert value("Hey, Mr Hlungwane") == 20
    assert value("How are you") == 20
    assert value("How is everything going?") == 20

def test_others():
    assert value("Welcome, Mr Hlungwane") == 100
    assert value("Mr Hlungwane, hello to you") == 100
    assert value("What can we help you with today?") == 100


def test_random():
    assert value("123") == 100
    assert value("@#$%") == 100
    assert value("coin") == 100


def test_nothing():
    assert value("") == 100
