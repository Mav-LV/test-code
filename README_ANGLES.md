# Right Triangle Angles Computation

This feature adds comprehensive right triangle angles computation functionality to the existing API.

## 🆕 New Features

### RightTriangleAngles Class
A new class that extends the base `BaseCompute` class to calculate all angles of a right triangle given two sides.

**Capabilities:**
- **Both legs provided**: Calculate angles when you know both legs of the triangle
- **Leg + hypotenuse**: Calculate angles when you know one leg and the hypotenuse  
- **Auto-detection**: Automatically determine the configuration based on side lengths
- **Complete triangle info**: Get all sides, angles, area, and perimeter

### New API Endpoints

#### `/angles` - POST
Calculate all angles of a right triangle with detailed information.

**Request Body:**
```json
{
  "side_a": 3.0,
  "side_b": 4.0,
  "side_type": "legs"
}
```

**Response:**
```json
{
  "input_sides": {"side_a": 3.0, "side_b": 4.0},
  "computed_sides": {"side_a": 3.0, "side_b": 4.0, "hypotenuse": 5.0},
  "angles_degrees": {"angle_A": 36.87, "angle_B": 53.13, "angle_C": 90.0},
  "angles_radians": {"angle_A": 0.6435, "angle_B": 0.9273, "angle_C": 1.5708},
  "triangle_properties": {"area": 6.0, "perimeter": 12.0},
  "configuration": "legs",
  "message": "Right triangle angles computed: A=36.87°, B=53.13°, C=90.0°"
}
```

#### `/examples` - GET  
Get example requests for both endpoints (hypotenuse and angles).

## 📊 Side Type Options

- **`"legs"`**: Both provided sides are legs of the triangle
- **`"leg_hyp"`**: First side is a leg, second side is the hypotenuse
- **`"auto"`**: Automatically detect the configuration

## 🧮 Mathematical Features

- **Accurate calculations** using trigonometric functions (`atan`, `asin`)
- **Multiple input configurations** for maximum flexibility
- **Error handling** for invalid inputs (negative values, impossible triangles)
- **Precision control** with rounding to 6 decimal places
- **Angle sum validation** ensures results sum to 180°

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test_angles.py
```

**Test Coverage:**
- Basic functionality with known triangles (3-4-5, etc.)
- Edge cases (very small/large triangles, isosceles right triangles)
- Error handling (negative inputs, invalid configurations)
- Mathematical accuracy validation
- Convenience function testing

## 📝 Examples

### Example 1: Both Legs Known
```python
from src.compute.angles import RightTriangleAngles

# Classic 3-4-5 triangle
triangle = RightTriangleAngles(3, 4, "legs")
angles = triangle.compute()
print(angles)
# {'angle_A': 36.87, 'angle_B': 53.13, 'angle_C': 90.0, ...}
```

### Example 2: Leg and Hypotenuse
```python
# 5-12-13 triangle (knowing one leg and hypotenuse)
triangle = RightTriangleAngles(5, 13, "leg_hyp") 
angles = triangle.compute()
print(f"Angles: {angles['angle_A']:.1f}°, {angles['angle_B']:.1f}°")
# Angles: 22.6°, 67.4°
```

### Example 3: Auto-Detection
```python
# Let the system determine the configuration
triangle = RightTriangleAngles(6, 10, "auto")
info = triangle.get_triangle_info()
print(f"Configuration: {info['configuration']}")
print(f"Area: {info['area']}")
```

## 🔄 Integration with Existing API

The new functionality seamlessly integrates with the existing hypotenuse computation:
- **Same base class** (`BaseCompute`) ensures consistency
- **Compatible error handling** using the same patterns
- **Enhanced API** with backward compatibility
- **Updated documentation** and examples

## ⚡ Performance

- **O(1) complexity** for all calculations
- **Minimal memory footprint** 
- **Fast trigonometric operations** using Python's `math` module
- **Efficient validation** with early error detection

## 🔧 API Version Update

The API has been updated to **version 2.0.0** to reflect the new angles computation capabilities while maintaining full backward compatibility with existing hypotenuse endpoints.

---

**Ready for production use!** ✨