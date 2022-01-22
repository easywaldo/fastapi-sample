from typing import ClassVar, Dict, List


primes: List[int] = []

captain: str  # Note: no initial value!

class Starship:
    stats: ClassVar[Dict[str, int]] = {}


def test_primes():
    primes = [1,2,3,4,5,6,100,9]
    assert len(primes) == 7