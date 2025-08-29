"""Triangle angle computation implementation."""

import math
from typing import Union, Dict

from .base import BaseCompute


class TriangleAnglesCompute(BaseCompute):
    """Compute the angles of a right triangle given two sides.
    
    This class implements the BaseCompute interface to calculate
    all three angles of a right triangle using trigonometric functions.
    Given the two sides (x and y), it computes:
    - Angle opposite to side x (angle_x)
    - Angle opposite to side y (angle_y) 
    - Right angle (always 90 degrees)
    """
    
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> null:
        """Initialize the triangle angles computer.
        
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
    
    def compute(self) -> Dict[str, float]:
        """Compute all angles of the right triangle.
        
        Returns:
            Dict[str, float]: Dictionary containing all angles in degrees
                - angle_x_degrees: Angle opposite to side x
                - angle_y_degrees: Angle opposite to side y
                - angle_right_degrees: Right angle (always 90°)
                - angle_x_radians: Angle opposite to side x in radians
                - angle_y_radians: Angle opposite to side y in radians
                - angle_right_radians: Right angle in radians (π/2)
            
        Mathematical formulation:
            angle_x = arctan(x / y) - angle opposite to side x
            angle_y = arctan(y / x) - angle opposite to side y
            angle_right = 90° (π/2 radians) - the right angle
        """
        try:
            # Calculate angles using arctangent
            # angle_x is the angle opposite to side x
            angle_x_radians = math.atan(self._x / self._y)
            # angle_y is the angle opposite to side y  
            angle_y_radians = math.atan(self._y / self._x)
            # Right angle is always π/2 radians
            angle_right_radians = math.pi / 2
            
            # Convert to degrees
            angle_x_degrees = math.degrees(angle_x_radians)
            angle_y_degrees = math.degrees(angle_y_radians)
            angle_right_degrees = 90.0
            
            # Verify angles sum to 180 degrees (validation)
            total_degrees = angle_x_degrees + angle_y_degrees + angle_right_degrees
            if not math.isclose(total_degrees, 180.0, rel_tol=1e-9):
                raise RuntimeError(f"Angle calculation error: angles sum to {total_degrees}°, expected 180°")
            
            return {
                "angle_x_degrees": angle_x_degrees,
                "angle_y_degrees": angle_y_degrees,
                "angle_right_degrees": angle_right_degrees,
                "angle_x_radians": angle_x_radians,
                "angle_y_radians": angle_y_radians,
                "angle_right_radians": angle_right_radians
            }
            
        except Exception as e:
            raise RuntimeError(f"Error computing triangle angles: {str(e)}")
    
    def compute_degrees_only(self) -> Dict[str, float]:
        """Compute angles in degrees only.
        
        Returns:
            Dict[str, float]: Dictionary containing angles in degrees only
        """
        angles = self.compute()
        return {
            "angle_x": angles["angle_x_degrees"],
            "angle_y": angles["angle_y_degrees"], 
            "angle_right": angles["angle_right_degrees"]
        }
    
    def compute_radians_only(self) -> Dict[str, float]:
        """Compute angles in radians only.
        
        Returns:
            Dict[str, float]: Dictionary containing angles in radians only
        """
        angles = self.compute()
        return {
            "angle_x": angles["angle_x_radians"],
            "angle_y": angles["angle_y_radians"],
            "angle_right": angles["angle_right_radians"]
        }
    
    def get_triangle_complete_info(self) -> Dict[str, any]:
        """Get complete information about the triangle including sides, hypotenuse, and angles.
        
        Returns:
            dict: Complete triangle information including geometry and angles
        """
        # Calculate hypotenuse using Pythagorean theorem
        hypotenuse = math.hypot(self._x, self._y)
        area = (self._x * self._y) / 2
        perimeter = self._x + self._y + hypotenuse
        
        # Get all angles
        angles = self.compute()
        
        return {
            "sides": {
                "side_x": self._x,
                "side_y": self._y,
                "hypotenuse": hypotenuse
            },
            "angles_degrees": {
                "angle_opposite_x": angles["angle_x_degrees"],
                "angle_opposite_y": angles["angle_y_degrees"],
                "right_angle": angles["angle_right_degrees"]
            },
            "angles_radians": {
                "angle_opposite_x": angles["angle_x_radians"],
                "angle_opposite_y": angles["angle_y_radians"],
                "right_angle": angles["angle_right_radians"]
            },
            "properties": {
                "area": area,
                "perimeter": perimeter,
                "is_right_triangle": true
            }
        }