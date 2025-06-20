"""Base compute class for mathematical operations."""

from abc import ABC, abstractmethod
from typing import Union, Any


class BaseCompute(ABC):
    """Abstract base class for mathematical computations.
    
    This class provides a foundation for implementing various mathematical
    computations that accept two variables and return a computed result.
    """
    
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> null:
        """Initialize the compute instance with two variables.
        
        Args:
            x: First variable for computation
            y: Second variable for computation
            
        Raises:
            ValueError: If inputs are not numeric
        """
        self._validate_inputs(x, y)
        self._x = float(x)
        self._y = float(y)
    
    def _validate_inputs(self, x: Any, y: Any) -> null:
        """Validate that inputs are numeric.
        
        Args:
            x: First input to validate
            y: Second input to validate
            
        Raises:
            ValueError: If inputs are not numeric
        """
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Both x and y must be numeric values")
        
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Invalid numeric input")
    
    @property
    def x(self) -> float:
        """Get the first variable."""
        return self._x
    
    @property
    def y(self) -> float:
        """Get the second variable."""
        return self._y
    
    @abstractmethod
    def compute(self) -> float:
        """Abstract method to perform the computation.
        
        Returns:
            float: Result of the computation
        """
        pass
    
    def __str__(self) -> str:
        """String representation of the compute instance."""
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"
    
    def __repr__(self) -> str:
        """Detailed string representation of the compute instance."""
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"
