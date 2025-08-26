
from jar import Jar
import pytest


def test_init():
      jar = Jar()
      assert jar.capacity == 12
      assert jar.cookies == 0
      jar.deposit(5)
      assert jar.cookies == 5
      jar.deposit(5)
      assert jar.cookies == 10
      jar.capacity = 20
      assert jar.capacity == 20
      jar.capacity = 50
      assert jar.capacity == 50



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"




def test_deposit():
      jar = Jar()
      assert jar.cookies == 0
      jar.deposit(5)
      assert jar.cookies == 5
      jar.deposit(4)
      assert jar.cookies == 9




def test_withdraw():
      jar = Jar()
      assert jar.cookies == 0
      jar.deposit(10)
      jar.withdraw(5)
      assert jar.cookies == 5
      jar.deposit(2)
      jar.withdraw(1)
      assert jar.cookies == 6

