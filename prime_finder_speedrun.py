import time

def sieve_of_eratosthenes(limit):
    if limit <= 2:
        return []

    sieve = [True] * limit
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    sieve[2] = True
    # for start in range(2, 3):
    #     if sieve[start]:
    #         for multiple in range(start*start, limit, start):
    #             sieve[multiple] = False
    for i in range(4, limit, 2):
        sieve[i] = False
                
    for start in range(3, int(limit**0.5) + 1, 2):
        if sieve[start]:
            for multiple in range(start*start, limit, start):
                sieve[multiple] = False
    

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    # print(len(primes))
    return primes

def main():
    try:
        number = int(input("Enter an integer: "))
        
        start_time = time.time()  # Start timing
        primes = sieve_of_eratosthenes(number)
        end_time = time.time()  # End timing
        
        if not primes:
            print("There are no prime numbers smaller than", number)
        else:
            print("Prime numbers smaller than", number, "are:", len(primes))
        
        print(f"Time taken: {end_time - start_time:.6f} seconds")  # Print the elapsed time

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()