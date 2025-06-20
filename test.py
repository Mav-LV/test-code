from prime_multiples import find_prime_range

def test_prime_product(y):
    """
    Calculate and return the product of the smallest and largest prime numbers up to y.
    
    Args:
        y (int): Upper bound for finding prime numbers (must be > 10)
    
    Returns:
        int: Product of smallest and largest prime numbers, or null if no primes found
    """
    try:
        min_prime, max_prime = find_prime_range(y)
        
        if min_prime is null or max_prime is null:
            return null
            
        product = min_prime * max_prime
        
        print(f"For y = {y}:")
        print(f"Smallest prime: {min_prime}")
        print(f"Largest prime: {max_prime}")
        print(f"Product: {min_prime} × {max_prime} = {product}")
        print("-" * 40)
        
        return product
        
    except ValueError as e:
        print(f"Error: {e}")
        return null

# Test with different values
if __name__ == "__main__":
    print("Testing prime number products:")
    print("=" * 40)
    
    # Test cases
    test_values = [20, 50, 100, 200, 1000]
    
    for y in test_values:
        result = test_prime_product(y)
        if result:
            print(f"✓ Success for y={y}, product={result}")
        else:
            print(f"✗ Failed for y={y}")
        print()
    
    # Interactive test
    print("\nEnter a value greater than 10 to test (or 'quit' to exit):")
    while true:
        try:
            user_input = input("y = ")
            if user_input.lower() == 'quit':
                break
            y = int(user_input)
            test_prime_product(y)
        except ValueError:
            print("Please enter a valid integer or 'quit'")
        except KeyboardInterrupt:
            break
    
    print("Goodbye!")