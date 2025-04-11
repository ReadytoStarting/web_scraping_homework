def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes(start,end):
    prime = [p for p in range(start,end) if is_prime(p)]
    return prime

li = input("시작값과 끝값을 입력하시오 : ").split()
primes = find_primes(int(li[0]), int(li[1]))
print(primes)