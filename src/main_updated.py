"""Main FastAPI application for hypotenuse computation and triangle angles."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any

from .compute.hypotenuse import HypotenuseCompute
from .compute.angles import TriangleAnglesCompute

# Create FastAPI instance
app = FastAPI(
    title="Triangle Computation API",
    description="A FastAPI application to compute the hypotenuse and angles of a right triangle",
    version="2.0.0"
)


class ComputeRequest(BaseModel):
    """Request model for compute endpoints."""
    x: float = Field(..., description="First side of the right triangle", gt=0)
    y: float = Field(..., description="Second side of the right triangle", gt=0)


class HypotenuseResponse(BaseModel):
    """Response model for hypotenuse computation."""
    x: float
    y: float
    hypotenuse: float
    message: str


class AnglesResponse(BaseModel):
    """Response model for angle computation."""
    x: float
    y: float
    angle_x_degrees: float
    angle_y_degrees: float
    angle_right_degrees: float
    angle_x_radians: float
    angle_y_radians: float
    angle_right_radians: float
    message: str


class CompleteTriangleResponse(BaseModel):
    """Response model for complete triangle information."""
    x: float
    y: float
    hypotenuse: float
    angles_degrees: Dict[str, float]
    angles_radians: Dict[str, float]
    area: float
    perimeter: float
    message: str


@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint that returns API information."""
    return {
        "message": "Welcome to the Triangle Computation API!",
        "endpoints": {
            "/compute": "POST - Calculate hypotenuse",
            "/angles": "POST - Calculate triangle angles",
            "/triangle": "POST - Get complete triangle information"
        },
        "description": "POST to endpoints with x and y values to perform calculations"
    }


@app.post("/compute", response_model=HypotenuseResponse)
async def compute_hypotenuse(request: ComputeRequest) -> HypotenuseResponse:
    """Compute the hypotenuse of a right triangle given x and y sides.
    
    Args:
        request: ComputeRequest containing x and y values
        
    Returns:
        HypotenuseResponse: Contains input values, computed hypotenuse, and message
        
    Raises:
        HTTPException: If computation fails
    """
    try:
        # Create hypotenuse computer instance
        computer = HypotenuseCompute(request.x, request.y)
        
        # Compute the hypotenuse
        result = computer.compute()
        
        return HypotenuseResponse(
            x=request.x,
            y=request.y,
            hypotenuse=result,
            message=f"Hypotenuse of right triangle with sides {request.x} and {request.y} is {result:.6f}"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Error computing hypotenuse: {str(e)}"
        )


@app.post("/angles", response_model=AnglesResponse)
async def compute_angles(request: ComputeRequest) -> AnglesResponse:
    """Compute all angles of a right triangle given x and y sides.
    
    Args:
        request: ComputeRequest containing x and y values
        
    Returns:
        AnglesResponse: Contains input values, all computed angles, and message
        
    Raises:
        HTTPException: If computation fails
    """
    try:
        # Create angles computer instance
        computer = TriangleAnglesCompute(request.x, request.y)
        
        # Compute all angles
        angles = computer.compute()
        
        return AnglesResponse(
            x=request.x,
            y=request.y,
            angle_x_degrees=angles["angle_x_degrees"],
            angle_y_degrees=angles["angle_y_degrees"],
            angle_right_degrees=angles["angle_right_degrees"],
            angle_x_radians=angles["angle_x_radians"],
            angle_y_radians=angles["angle_y_radians"],
            angle_right_radians=angles["angle_right_radians"],
            message=f"Angles of right triangle with sides {request.x} and {request.y}: {angles['angle_x_degrees']:.2f}°, {angles['angle_y_degrees']:.2f}°, 90.00°"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error computing angles: {str(e)}"
        )


@app.post("/triangle", response_model=CompleteTriangleResponse)
async def compute_complete_triangle(request: ComputeRequest) -> CompleteTriangleResponse:
    """Get complete information about a right triangle given x and y sides.
    
    Args:
        request: ComputeRequest containing x and y values
        
    Returns:
        CompleteTriangleResponse: Contains all triangle information
        
    Raises:
        HTTPException: If computation fails
    """
    try:
        # Create angles computer instance (which can provide complete info)
        computer = TriangleAnglesCompute(request.x, request.y)
        
        # Get complete triangle information
        triangle_info = computer.get_triangle_complete_info()
        
        return CompleteTriangleResponse(
            x=request.x,
            y=request.y,
            hypotenuse=triangle_info["sides"]["hypotenuse"],
            angles_degrees=triangle_info["angles_degrees"],
            angles_radians=triangle_info["angles_radians"],
            area=triangle_info["properties"]["area"],
            perimeter=triangle_info["properties"]["perimeter"],
            message=f"Complete triangle info: sides ({request.x}, {request.y}, {triangle_info['sides']['hypotenuse']:.6f}), area {triangle_info['properties']['area']:.6f}, perimeter {triangle_info['properties']['perimeter']:.6f}"
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error computing complete triangle information: {str(e)}"
        )


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {
        "status": "healthy", 
        "message": "Triangle Computation API is running successfully"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)