# median.py
def median(numbers):
    if len(numbers) == 0:
        return 0
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2

def main(numbers):
    print("Median:", median(numbers))
