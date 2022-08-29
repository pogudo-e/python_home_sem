# Составить список простых множителей натурального числа N


n = int(input('Введите число: '))

def EasyNum(n):
    ans = []
    x = 2
    while x * x <= n:
        if n % x == 0:
            ans.append(x)
            n //= x
        else:
            x += 1
    if n > 1:
        ans.append(n)
    return ans

print(f'{n} => {EasyNum(n)}')