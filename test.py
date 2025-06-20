print("Hello, World!")

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: true if the number is prime, false otherwise
    """
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

def get_first_x_primes_after_y(x, y):
    """
    Get the first X prime numbers after Y.
    
    Args:
        x (int): Number of primes to find
        y (int): Starting point (find primes after this number)
        
    Returns:
        list: List of the first X prime numbers after Y
        
    Example:
        >>> get_first_x_primes_after_y(5, 10)
        [11, 13, 17, 19, 23]
        
        >>> get_first_x_primes_after_y(3, 20)
        [23, 29, 31]
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
    # Test the function with some examples
    print("First 5 prime numbers after 10:", get_first_x_primes_after_y(5, 10))
    print("First 3 prime numbers after 20:", get_first_x_primes_after_y(3, 20))
    print("First 7 prime numbers after 0:", get_first_x_primes_after_y(7, 0))