"""Right triangle angles computation module."""

import math
from typing import Union, Tuple, Dict, Optional
from .base import BaseCompute


class RightTriangleAngles(BaseCompute):
    """Compute angles of a right triangle given two sides.
    
    This class can compute all three angles of a right triangle when given:
    - Two legs (adjacent and opposite sides)
    - One leg and the hypotenuse
    - Any two sides of the triangle
    
    All angles are returned in degrees by default, with an option for radians.
    """
    
    def __init__(self, side_a: Union[int, float], side_b: Union[int, float], 
                 side_type: str = "legs") -> null:
        """Initialize the right triangle angles calculator.
        
        Args:
            side_a: First side length
            side_b: Second side length  
            side_type: Type of sides provided ("legs", "leg_hyp", or "auto")
                - "legs": Both sides are legs (adjacent/opposite to the angles)
                - "leg_hyp": side_a is a leg, side_b is hypotenuse
                - "auto": Automatically determine based on side lengths
                
        Raises:
            ValueError: If sides are not positive or configuration is invalid
        """
        super().__init__(side_a, side_b)
        self._validate_triangle_sides(side_a, side_b)
        self.side_type = side_type.lower()
        self._determine_triangle_configuration()
    
    def _validate_triangle_sides(self, a: Union[int, float], b: Union[int, float]) -> null:
        """Validate that the provided sides can form a valid right triangle.
        
        Args:
            a: First side length
            b: Second side length
            
        Raises:
            ValueError: If sides are not positive
        """
        if a <= 0 or b <= 0:
            raise ValueError("All sides must be positive values")
    
    def _determine_triangle_configuration(self) -> null:
        """Determine the configuration of the triangle based on input."""
        if self.side_type == "auto":
            # If one side is significantly larger, assume it's the hypotenuse
            if self.x > self.y * 1.1:
                self.side_type = "leg_hyp"
                self._leg = self.y
                self._hypotenuse = self.x
            elif self.y > self.x * 1.1:
                self.side_type = "leg_hyp" 
                self._leg = self.x
                self._hypotenuse = self.y
            else:
                self.side_type = "legs"
                self._leg_a = self.x
                self._leg_b = self.y
        elif self.side_type == "legs":
            self._leg_a = self.x
            self._leg_b = self.y
        elif self.side_type == "leg_hyp":
            self._leg = self.x
            self._hypotenuse = self.y
        else:
            raise ValueError("side_type must be 'legs', 'leg_hyp', or 'auto'")
    
    def compute(self) -> Dict[str, float]:
        """Compute all three angles of the right triangle.
        
        Returns:
            Dict[str, float]: Dictionary containing:
                - 'angle_A': First acute angle in degrees
                - 'angle_B': Second acute angle in degrees  
                - 'angle_C': Right angle (always 90 degrees)
                - 'angle_A_rad': First acute angle in radians
                - 'angle_B_rad': Second acute angle in radians
                - 'angle_C_rad': Right angle in radians
        """
        if self.side_type == "legs":
            return self._compute_from_legs()
        else:
            return self._compute_from_leg_and_hypotenuse()
    
    def _compute_from_legs(self) -> Dict[str, float]:
        """Compute angles when both legs are provided."""
        # Calculate angles using arctangent
        angle_A_rad = math.atan(self._leg_b / self._leg_a)
        angle_B_rad = math.atan(self._leg_a / self._leg_b)
        angle_C_rad = math.pi / 2  # 90 degrees
        
        # Convert to degrees
        angle_A = math.degrees(angle_A_rad)
        angle_B = math.degrees(angle_B_rad)
        angle_C = 90.0
        
        return {
            'angle_A': round(angle_A, 6),
            'angle_B': round(angle_B, 6),
            'angle_C': angle_C,
            'angle_A_rad': round(angle_A_rad, 6),
            'angle_B_rad': round(angle_B_rad, 6),
            'angle_C_rad': round(angle_C_rad, 6)
        }
    
    def _compute_from_leg_and_hypotenuse(self) -> Dict[str, float]:
        """Compute angles when one leg and hypotenuse are provided."""
        # Validate that leg < hypotenuse
        if self._leg >= self._hypotenuse:
            raise ValueError("Leg must be shorter than hypotenuse")
        
        # Calculate the acute angle using arcsine
        angle_A_rad = math.asin(self._leg / self._hypotenuse)
        angle_B_rad = math.pi / 2 - angle_A_rad  # Complementary angle
        angle_C_rad = math.pi / 2  # Right angle
        
        # Convert to degrees
        angle_A = math.degrees(angle_A_rad)
        angle_B = math.degrees(angle_B_rad)
        angle_C = 90.0
        
        return {
            'angle_A': round(angle_A, 6),
            'angle_B': round(angle_B, 6), 
            'angle_C': angle_C,
            'angle_A_rad': round(angle_A_rad, 6),
            'angle_B_rad': round(angle_B_rad, 6),
            'angle_C_rad': round(angle_C_rad, 6)
        }
    
    def get_triangle_info(self) -> Dict[str, Union[float, str]]:
        """Get complete information about the triangle.
        
        Returns:
            Dict containing triangle sides, angles, area, and perimeter.
        """
        angles = self.compute()
        
        if self.side_type == "legs":
            leg_a, leg_b = self._leg_a, self._leg_b
            hypotenuse = math.sqrt(leg_a**2 + leg_b**2)
        else:
            leg_a = self._leg
            hypotenuse = self._hypotenuse
            leg_b = math.sqrt(hypotenuse**2 - leg_a**2)
        
        area = 0.5 * leg_a * leg_b
        perimeter = leg_a + leg_b + hypotenuse
        
        return {
            'side_a': round(leg_a, 6),
            'side_b': round(leg_b, 6),
            'hypotenuse': round(hypotenuse, 6),
            'area': round(area, 6),
            'perimeter': round(perimeter, 6),
            'configuration': self.side_type,
            **angles
        }
    
    def __str__(self) -> str:
        """String representation of the triangle."""
        info = self.get_triangle_info()
        return (f"RightTriangle(a={info['side_a']}, b={info['side_b']}, "
                f"c={info['hypotenuse']}, ∠A={info['angle_A']:.1f}°, "
                f"∠B={info['angle_B']:.1f}°, ∠C={info['angle_C']:.1f}°)")


def compute_right_triangle_angles(side_a: Union[int, float], 
                                side_b: Union[int, float],
                                side_type: str = "legs") -> Dict[str, float]:
    """Convenience function to compute right triangle angles.
    
    Args:
        side_a: First side length
        side_b: Second side length
        side_type: Type of sides ("legs", "leg_hyp", or "auto")
        
    Returns:
        Dict containing all angle measurements
    """
    calculator = RightTriangleAngles(side_a, side_b, side_type)
    return calculator.compute()


# Example usage and demonstrations
if __name__ == "__main__":
    # Example 1: Both legs provided
    print("Example 1: Right triangle with legs 3 and 4")
    triangle1 = RightTriangleAngles(3, 4, "legs")
    print(triangle1)
    print("Angles:", triangle1.compute())
    print("Complete info:", triangle1.get_triangle_info())
    print()
    
    # Example 2: Leg and hypotenuse provided  
    print("Example 2: Right triangle with leg 5 and hypotenuse 13")
    triangle2 = RightTriangleAngles(5, 13, "leg_hyp")
    print(triangle2)
    print("Angles:", triangle2.compute())
    print()
    
    # Example 3: Auto-detection
    print("Example 3: Auto-detect configuration (6, 10)")
    triangle3 = RightTriangleAngles(6, 10, "auto")
    print(triangle3)
    print("Angles:", triangle3.compute())