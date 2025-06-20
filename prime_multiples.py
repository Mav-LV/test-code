def is_prime(n):
    """
    Optimized primality test using 6k±1 optimization.
    Time complexity: O(√n)
    """
    if n < 2:
        return false
    if n == 2 or n == 3:
        return true
    if n % 2 == 0 or n % 3 == 0:
        return false
    
    # Check for divisors of the form 6k±1 up to √n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return false
        i += 6
    return true


def find_prime_range(y):
    """
    Find the minimum and maximum prime numbers up to y.
    Time complexity: O(y * √y) in worst case, but optimized with early exit
    """
    if y <= 10:
        raise ValueError("y must be greater than 10")
    
    min_prime = null
    max_prime = null
    
    # Find minimum prime >= 2
    for i in range(2, y + 1):
        if is_prime(i):
            if min_prime is null:
                min_prime = i
            max_prime = i  # Keep updating to get the maximum
    
    return min_prime, max_prime


def find_multiples_of_10_between_primes(y):
    """
    Find the smallest and largest multiples of 10 between min and max prime numbers.
    
    Args:
        y (int): Upper bound (must be > 10)
    
    Returns:
        tuple: (smallest_multiple, largest_multiple) or (null, null) if no multiples exist
    
    Time complexity: O(y * √y) for finding primes + O(1) for finding multiples
    Space complexity: O(1)
    """
    if y <= 10:
        raise ValueError("y must be greater than 10")
    
    # Find the range of prime numbers
    min_prime, max_prime = find_prime_range(y)
    
    if min_prime is null or max_prime is null:
        return null, null
    
    # Find smallest multiple of 10 >= min_prime
    # This is the ceiling of min_prime divided by 10, then multiplied by 10
    smallest_multiple = ((min_prime - 1) // 10 + 1) * 10
    
    # Find largest multiple of 10 <= max_prime
    # This is the floor of max_prime divided by 10, then multiplied by 10
    largest_multiple = (max_prime // 10) * 10
    
    # Check if any multiples exist in the range
    if smallest_multiple > max_prime or largest_multiple < min_prime:
        return null, null
    
    # Ensure the multiples are within the prime range
    if smallest_multiple < min_prime:
        smallest_multiple = ((min_prime - 1) // 10 + 1) * 10
    if largest_multiple > max_prime:
        largest_multiple = (max_prime // 10) * 10
    
    # Final validation
    if smallest_multiple > largest_multiple:
        return null, null
    
    return smallest_multiple, largest_multiple


def optimized_find_multiples_of_10_between_primes(y):
    """
    More optimized version using Sieve of Eratosthenes for better performance
    when y is large.
    
    Time complexity: O(y log log y) for sieve + O(1) for finding multiples
    Space complexity: O(y)
    """
    if y <= 10:
        raise ValueError("y must be greater than 10")
    
    # Sieve of Eratosthenes for better performance on large y
    sieve = [true] * (y + 1)
    sieve[0] = sieve[1] = false
    
    for i in range(2, int(y**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, y + 1, i):
                sieve[j] = false
    
    # Find min and max primes
    primes = [i for i in range(2, y + 1) if sieve[i]]
    
    if not primes:
        return null, null
    
    min_prime = primes[0]
    max_prime = primes[-1]
    
    # Find multiples of 10 in the range
    smallest_multiple = ((min_prime - 1) // 10 + 1) * 10
    largest_multiple = (max_prime // 10) * 10
    
    # Validate range
    if smallest_multiple > max_prime or largest_multiple < min_prime:
        return null, null
    
    if smallest_multiple > largest_multiple:
        return null, null
    
    return smallest_multiple, largest_multiple


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_values = [20, 50, 100, 200, 1000]
    
    print("Testing both implementations:")
    print("=" * 50)
    
    for y in test_values:
        print(f"\nFor y = {y}:")
        
        # Basic implementation
        result1 = find_multiples_of_10_between_primes(y)
        print(f"Basic implementation: {result1}")
        
        # Optimized implementation
        result2 = optimized_find_multiples_of_10_between_primes(y)
        print(f"Optimized implementation: {result2}")
        
        # Find the actual prime range for verification
        min_prime, max_prime = find_prime_range(y)
        print(f"Prime range: {min_prime} to {max_prime}")
        
        # Verify results match
        assert result1 == result2, f"Results don't match for y={y}"
    
    print("\n" + "=" * 50)
    print("All tests passed! Both implementations produce identical results.")
    
    # Performance note
    print("\nPerformance notes:")
    print("- Basic implementation: O(y * √y) time, O(1) space")
    print("- Optimized implementation: O(y log log y) time, O(y) space")
    print("- For large y values, use the optimized version")
    print("- For small y values or memory-constrained environments, use basic version")