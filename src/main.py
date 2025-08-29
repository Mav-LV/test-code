"""Main FastAPI application for hypotenuse computation."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any

from .compute.hypotenuse import HypotenuseCompute

# Create FastAPI instance
app = FastAPI(
    title="Hypotenuse Computation API",
    description="A FastAPI application to compute the hypotenuse of a right triangle",
    version="1.0.0"
)


class ComputeRequest(BaseModel):
    """Request model for compute endpoint."""
    x: float = Field(..., description="First side of the right triangle", gt=0)
    y: float = Field(..., description="Second side of the right triangle", gt=0)


class ComputeResponse(BaseModel):
    """Response model for compute endpoint."""
    x: float
    y: float
    hypotenuse: float
    message: str


@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint that returns API information."""
    return {
        "message": "Welcome to the Hypotenuse Computation API!",
        "endpoint": "/compute",
        "description": "POST to /compute with x and y values to calculate hypotenuse"
    }


@app.post("/compute", response_model=ComputeResponse)
async def compute_hypotenuse(request: ComputeRequest) -> ComputeResponse:
    """Compute the hypotenuse of a right triangle given x and y sides.
    
    Args:
        request: ComputeRequest containing x and y values
        
    Returns:
        ComputeResponse: Contains input values, computed hypotenuse, and message
        
    Raises:
        HTTPException: If computation fails
    """
    try:
        # Create hypotenuse computer instance
        computer = HypotenuseCompute(request.x, request.y)
        
        # Compute the hypotenuse
        result = computer.compute()
        
        return ComputeResponse(
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


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {
        "status": "healthy", 
        "message": "Hypotenuse Computation API is running successfully"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
