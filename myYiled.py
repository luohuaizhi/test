def get_primes(number):
    while True:
        if number % 2:
            yield number
        number += 1

def get_prime():
    number = 11
    for next_p in get_primes(number):
        if next_p < 100:
            print next_p
        else:
            return


def main():
    for next_p in get_primes(11):
        if next_p < 100:
            print next_p
        else:
            return


if __name__ == '__main__':
    # main()
    prime = get_prime()
    print  next(prime)
    print  next(prime)
    print  next(prime)
