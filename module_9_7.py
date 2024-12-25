def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        is_pr = None
        if n > 1:
            if n == 2:
                is_pr = True
            elif n % 2 == 0:
                is_pr = False
            else:
                for i in range(3, int(n ** 0.5) + 1, 2):
                    if n % i == 0:
                        is_pr = False
                        break
                if is_pr == None:
                    is_pr = True
        if is_pr == True:
            print('Простое')
        elif is_pr == False:
            print('Составное')
        return n
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(0, 1, 999999936)
print(result)