import pytest
from prime_checker import is_prime

def test_is_prime():
    assert not is_prime(-1)   # Negative
    assert not is_prime(0)    # Zero
    assert not is_prime(1)    # 1 is not prime
    assert is_prime(2)        # Smallest prime
    assert is_prime(3)        # Small odd prime
    assert not is_prime(4)    
    assert is_prime(17)       # Larger prime
    assert not is_prime(25)   # Square of prime
    assert is_prime(7919)     