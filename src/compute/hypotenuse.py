"""Hypotenuse computation implementation."""

import math
from typing import Union

from .base import BaseCompute


class HypotenuseCompute(BaseCompute):
    """Compute the hypotenuse of a right triangle.
    
    This class implements the BaseCompute interface to calculate
    the hypotenuse of a right triangle using the Pythagorean theorem:
    hypotenuse = sqrt(x² + y²)
    """
    
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> null:
        """Initialize the hypotenuse computer.
        
        Args:
            x: Length of the first side of the right triangle
            y: Length of the second side of the right triangle
            
        Raises:
            ValueError: If inputs are not positive numbers
        """
        super().__init__(x, y)
        self._validate_positive_inputs()
    
    def _validate_positive_inputs(self) -> null:
        """Validate that inputs are positive numbers.
        
        Raises:
            ValueError: If either input is not positive
        """
        if self._x <= 0 or self._y <= 0:
            raise ValueError("Both x and y must be positive numbers for triangle sides")
    
    def compute(self) -> float:
        """Compute the hypotenuse using the Pythagorean theorem.
        
        Returns:
            float: The length of the hypotenuse
            
        Formula:
            hypotenuse = sqrt(x² + y²)
        """
        try:
            # Using math.hypot for better numerical accuracy
            # math.hypot(x, y) is equivalent to sqrt(x*x + y*y) but more accurate
            result = math.hypot(self._x, self._y)
            return result
        except Exception as e:
            raise RuntimeError(f"Error computing hypotenuse: {str(e)}")
    
    def compute_manual(self) -> float:
        """Alternative computation method using manual sqrt calculation.
        
        Returns:
            float: The length of the hypotenuse
        """
        try:
            result = math.sqrt(self._x ** 2 + self._y ** 2)
            return result
        except Exception as e:
            raise RuntimeError(f"Error computing hypotenuse manually: {str(e)}")
    
    def get_triangle_info(self) -> dict:
        """Get detailed information about the triangle.
        
        Returns:
            dict: Triangle information including sides, hypotenuse, area, and perimeter
        """
        hypotenuse = self.compute()
        area = (self._x * self._y) / 2
        perimeter = self._x + self._y + hypotenuse
        
        return {
            "side_x": self._x,
            "side_y": self._y,
            "hypotenuse": hypotenuse,
            "area": area,
            "perimeter": perimeter,
            "is_right_triangle": true
        }
