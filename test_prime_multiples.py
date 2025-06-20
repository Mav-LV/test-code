import time
from prime_multiples import (
    find_multiples_of_10_between_primes,
    optimized_find_multiples_of_10_between_primes,
    find_prime_range,
    is_prime
)

def test_basic_functionality():
    """Test basic functionality with known values"""
    print("Testing basic functionality...")
    
    # Test case 1: y = 30
    # Primes up to 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    # Min prime: 2, Max prime: 29
    # Multiples of 10 between 2 and 29: 10, 20
    result = find_multiples_of_10_between_primes(30)
    expected = (10, 20)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ y=30: {result}")
    
    # Test case 2: y = 50  
    # Max prime: 47
    # Multiples of 10 between 2 and 47: 10, 20, 30, 40
    result = find_multiples_of_10_between_primes(50)
    expected = (10, 40)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ y=50: {result}")
    
    # Test case 3: y = 15
    # Primes up to 15: 2, 3, 5, 7, 11, 13
    # Multiples of 10 between 2 and 13: 10
    result = find_multiples_of_10_between_primes(15)
    expected = (10, 10)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ y=15: {result}")


def test_edge_cases():
    """Test edge cases"""
    print("\nTesting edge cases...")
    
    # Test case: y = 11 (smallest valid input > 10)
    result = find_multiples_of_10_between_primes(11)
    # Primes up to 11: 2, 3, 5, 7, 11
    # No multiples of 10 between 2 and 11
    expected = (null, null)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"✓ y=11: {result}")
    
    # Test invalid input
    try:
        find_multiples_of_10_between_primes(5)
        assert false, "Should have raised ValueError"
    except ValueError:
        print("✓ Correctly raised ValueError for y <= 10")


def test_performance_comparison():
    """Compare performance of both implementations"""
    print("\nPerformance comparison...")
    
    test_values = [100, 500, 1000]
    
    for y in test_values:
        print(f"\nTesting y = {y}:")
        
        # Test basic implementation
        start_time = time.time()
        result1 = find_multiples_of_10_between_primes(y)
        time1 = time.time() - start_time
        
        # Test optimized implementation  
        start_time = time.time()
        result2 = optimized_find_multiples_of_10_between_primes(y)
        time2 = time.time() - start_time
        
        # Verify results match
        assert result1 == result2, f"Results don't match: {result1} vs {result2}"
        
        print(f"  Basic implementation: {result1} (Time: {time1:.6f}s)")
        print(f"  Optimized implementation: {result2} (Time: {time2:.6f}s)")
        print(f"  Speedup: {time1/time2:.2f}x" if time2 > 0 else "  Speedup: N/A")


def demonstrate_algorithm():
    """Demonstrate the algorithm with detailed output"""
    print("\n" + "="*60)
    print("ALGORITHM DEMONSTRATION")
    print("="*60)
    
    y = 100
    print(f"Finding multiples of 10 between min and max primes up to {y}")
    
    # Step 1: Find prime range
    min_prime, max_prime = find_prime_range(y)
    print(f"\nStep 1: Find prime range")
    print(f"  Minimum prime: {min_prime}")
    print(f"  Maximum prime: {max_prime}")
    
    # Step 2: Calculate multiples of 10
    print(f"\nStep 2: Find multiples of 10 in range [{min_prime}, {max_prime}]")
    
    # Smallest multiple >= min_prime
    smallest = ((min_prime - 1) // 10 + 1) * 10
    print(f"  Smallest multiple of 10 >= {min_prime}: {smallest}")
    
    # Largest multiple <= max_prime  
    largest = (max_prime // 10) * 10
    print(f"  Largest multiple of 10 <= {max_prime}: {largest}")
    
    # All multiples in range
    multiples = list(range(smallest, largest + 1, 10))
    print(f"  All multiples of 10 in range: {multiples}")
    
    result = find_multiples_of_10_between_primes(y)
    print(f"\nFinal result: {result}")
    
    # Verify with prime checking
    print(f"\nVerification:")
    print(f"  {min_prime} is prime: {is_prime(min_prime)}")
    print(f"  {max_prime} is prime: {is_prime(max_prime)}")
    print(f"  {result[0]} is multiple of 10: {result[0] % 10 == 0}")
    print(f"  {result[1]} is multiple of 10: {result[1] % 10 == 0}")


def analyze_complexity():
    """Analyze and explain the time complexity"""
    print("\n" + "="*60)
    print("TIME COMPLEXITY ANALYSIS")
    print("="*60)
    
    print("Basic Implementation:")
    print("  - Prime checking: O(√n) per number")
    print("  - Checking y numbers: O(y * √y)")
    print("  - Finding multiples: O(1)")
    print("  - Total: O(y * √y)")
    print("  - Space: O(1)")
    
    print("\nOptimized Implementation (Sieve of Eratosthenes):")
    print("  - Sieve generation: O(y log log y)")
    print("  - Finding min/max primes: O(y)")
    print("  - Finding multiples: O(1)")
    print("  - Total: O(y log log y)")
    print("  - Space: O(y)")
    
    print("\nRecommendations:")
    print("  - For y < 10,000: Use basic implementation (lower memory)")
    print("  - For y >= 10,000: Use optimized implementation (faster)")
    print("  - For repeated queries: Use optimized with caching")


if __name__ == "__main__":
    print("PRIME MULTIPLES SOLVER - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    # Run all tests
    test_basic_functionality()
    test_edge_cases()
    test_performance_comparison()
    demonstrate_algorithm()
    analyze_complexity()
    
    print("\n" + "="*60)
    print("ALL TESTS PASSED! ✅")
    print("The solution efficiently finds the smallest and largest")
    print("multiples of 10 between min and max prime numbers.")
    print("="*60)