print("Hello, World!")

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return false
    if n == 2:
        return true
    if n % 2 == 0:
        return false
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return false
    return true

def get_x_primes_after_y(x, y):
    """
    Generate x prime numbers after y.
    
    Args:
        x (int): Number of prime numbers to find
        y (int): Starting number (primes will be found after this number)
    
    Returns:
        list: List of x prime numbers greater than y
    """
    primes = []
    candidate = y + 1
    
    while len(primes) < x:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    
    return primes

# Example usage
if __name__ == "__main__":
    # Find 5 prime numbers after 10
    result = get_x_primes_after_y(5, 10)
    print(f"First 5 prime numbers after 10: {result}")
    
    # Find 3 prime numbers after 50
    result2 = get_x_primes_after_y(3, 50)
    print(f"First 3 prime numbers after 50: {result2}")