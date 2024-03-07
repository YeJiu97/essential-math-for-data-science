# Description: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
summation = sum([i for i in range(1, 101)])

print(summation)


x = [1, 2, 3, 4]
n = len(x)
summation = sum(10 * x[i] for i in range(0, n))
print(summation)