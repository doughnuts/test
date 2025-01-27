#阶乘
class FactorialError(Exception):
    def __init__(self, message):
        super().__init__(message)

def factorial(n):
        if n < 0:
            raise FactorialError("n不能为负数")
        if n == 0 or n == 1:
            return 1
        return n * factorial(n-1)
    # def factorial(self, n):
    #     if n == 0 or n == 1:
    #         return 1
    #     return n * self.factorial(n-1)

print(factorial(-5))


