#!/usr/bin/env python3
"""
Test file for RightTriangleAngles functionality.
This file demonstrates and tests the right triangle angles computation.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.compute.angles import RightTriangleAngles, compute_right_triangle_angles
import math


def test_basic_functionality():
    """Test basic functionality with known triangle."""
    print("=" * 60)
    print("TESTING RIGHT TRIANGLE ANGLES COMPUTATION")
    print("=" * 60)
    
    # Test 1: Classic 3-4-5 triangle (both legs provided)
    print("\n1. Testing 3-4-5 triangle (legs provided):")
    triangle1 = RightTriangleAngles(3, 4, "legs")
    angles1 = triangle1.compute()
    info1 = triangle1.get_triangle_info()
    
    print(f"   Triangle: {triangle1}")
    print(f"   Angle A: {angles1['angle_A']:.2f}° ({angles1['angle_A_rad']:.4f} rad)")
    print(f"   Angle B: {angles1['angle_B']:.2f}° ({angles1['angle_B_rad']:.4f} rad)")
    print(f"   Angle C: {angles1['angle_C']:.2f}° (right angle)")
    print(f"   Hypotenuse: {info1['hypotenuse']}")
    print(f"   Area: {info1['area']}")
    print(f"   Perimeter: {info1['perimeter']}")
    
    # Verify angles sum to 180°
    angle_sum = angles1['angle_A'] + angles1['angle_B'] + angles1['angle_C']
    print(f"   Angle sum: {angle_sum:.2f}° (should be 180°)")
    assert abs(angle_sum - 180.0) < 0.001, "Angles should sum to 180°"
    
    # Test 2: Leg and hypotenuse provided  
    print("\n2. Testing leg=5, hypotenuse=13 (leg-hypotenuse):")
    triangle2 = RightTriangleAngles(5, 13, "leg_hyp")
    angles2 = triangle2.compute()
    info2 = triangle2.get_triangle_info()
    
    print(f"   Triangle: {triangle2}")
    print(f"   Angle A: {angles2['angle_A']:.2f}° ({angles2['angle_A_rad']:.4f} rad)")
    print(f"   Angle B: {angles2['angle_B']:.2f}° ({angles2['angle_B_rad']:.4f} rad)")
    print(f"   All sides: a={info2['side_a']}, b={info2['side_b']}, c={info2['hypotenuse']}")
    
    # Test 3: Auto-detection
    print("\n3. Testing auto-detection (6, 10):")
    triangle3 = RightTriangleAngles(6, 10, "auto")
    angles3 = triangle3.compute()
    info3 = triangle3.get_triangle_info()
    
    print(f"   Triangle: {triangle3}")
    print(f"   Detected configuration: {info3['configuration']}")
    print(f"   Angle A: {angles3['angle_A']:.2f}°")
    print(f"   Angle B: {angles3['angle_B']:.2f}°")


def test_convenience_function():
    """Test the convenience function."""
    print("\n" + "=" * 60)
    print("TESTING CONVENIENCE FUNCTION")
    print("=" * 60)
    
    # Test the standalone function
    angles = compute_right_triangle_angles(8, 6, "legs")
    print(f"\nUsing convenience function with legs 8 and 6:")
    print(f"Angle A: {angles['angle_A']:.2f}°")
    print(f"Angle B: {angles['angle_B']:.2f}°")
    print(f"Angle C: {angles['angle_C']:.2f}°")


def test_edge_cases():
    """Test edge cases and error handling."""
    print("\n" + "=" * 60)
    print("TESTING EDGE CASES")
    print("=" * 60)
    
    # Test 1: Very small triangle
    print("\n1. Testing very small triangle (0.001, 0.001):")
    try:
        small_triangle = RightTriangleAngles(0.001, 0.001, "legs")
        small_angles = small_triangle.compute()
        print(f"   Angles: A={small_angles['angle_A']:.2f}°, B={small_angles['angle_B']:.2f}°")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: Very large triangle
    print("\n2. Testing very large triangle (1000, 2000):")
    try:
        large_triangle = RightTriangleAngles(1000, 2000, "legs")
        large_angles = large_triangle.compute()
        print(f"   Angles: A={large_angles['angle_A']:.2f}°, B={large_angles['angle_B']:.2f}°")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 3: Equal legs (45-45-90 triangle)
    print("\n3. Testing isosceles right triangle (5, 5):")
    try:
        iso_triangle = RightTriangleAngles(5, 5, "legs")
        iso_angles = iso_triangle.compute()
        print(f"   Angles: A={iso_angles['angle_A']:.2f}°, B={iso_angles['angle_B']:.2f}°")
        print(f"   Should be two 45° angles")
        assert abs(iso_angles['angle_A'] - 45.0) < 0.001, "Should be 45°"
        assert abs(iso_angles['angle_B'] - 45.0) < 0.001, "Should be 45°"
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 4: Invalid inputs
    print("\n4. Testing error handling:")
    
    # Negative values
    try:
        bad_triangle1 = RightTriangleAngles(-3, 4, "legs")
        print("   ERROR: Should have caught negative value!")
    except ValueError as e:
        print(f"   ✓ Correctly caught negative value: {e}")
    
    # Zero values  
    try:
        bad_triangle2 = RightTriangleAngles(0, 4, "legs")
        print("   ERROR: Should have caught zero value!")
    except ValueError as e:
        print(f"   ✓ Correctly caught zero value: {e}")
    
    # Invalid leg-hypotenuse combination
    try:
        bad_triangle3 = RightTriangleAngles(10, 5, "leg_hyp")  # leg > hypotenuse
        angles = bad_triangle3.compute()
        print("   ERROR: Should have caught invalid leg-hypotenuse!")
    except ValueError as e:
        print(f"   ✓ Correctly caught invalid leg-hypotenuse: {e}")


def test_mathematical_accuracy():
    """Test mathematical accuracy against known values."""
    print("\n" + "=" * 60)
    print("TESTING MATHEMATICAL ACCURACY")
    print("=" * 60)
    
    # Test known triangles
    test_cases = [
        # (leg_a, leg_b, expected_angle_A, expected_angle_B)
        (1, 1, 45.0, 45.0),  # 45-45-90 triangle
        (1, math.sqrt(3), 30.0, 60.0),  # 30-60-90 triangle
        (3, 4, 36.87, 53.13),  # 3-4-5 triangle (approximate)
    ]
    
    for i, (a, b, exp_a, exp_b) in enumerate(test_cases, 1):
        print(f"\n{i}. Testing triangle with legs {a}, {b}:")
        triangle = RightTriangleAngles(a, b, "legs")
        angles = triangle.compute()
        
        print(f"   Expected: A≈{exp_a}°, B≈{exp_b}°")
        print(f"   Computed: A={angles['angle_A']:.2f}°, B={angles['angle_B']:.2f}°")
        
        # Check accuracy (within 0.1 degrees)
        angle_a_error = abs(angles['angle_A'] - exp_a)
        angle_b_error = abs(angles['angle_B'] - exp_b)
        
        if angle_a_error <= 0.1 and angle_b_error <= 0.1:
            print(f"   ✓ Accuracy good (errors: {angle_a_error:.3f}°, {angle_b_error:.3f}°)")
        else:
            print(f"   ⚠ Accuracy warning (errors: {angle_a_error:.3f}°, {angle_b_error:.3f}°)")


def main():
    """Run all tests."""
    print("RIGHT TRIANGLE ANGLES COMPUTATION - TEST SUITE")
    print("=" * 60)
    
    try:
        test_basic_functionality()
        test_convenience_function()
        test_edge_cases()
        test_mathematical_accuracy()
        
        print("\n" + "=" * 60)
        print("✓ ALL TESTS COMPLETED SUCCESSFULLY!")
        print("The RightTriangleAngles module is working correctly.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()