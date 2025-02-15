# mode.py
from collections import Counter

def mode(numbers):
    if len(numbers) == 0:
        return 0
    count = Counter(numbers)
    most_common = count.most_common(1)
    return most_common[0][0] if most_common else 0