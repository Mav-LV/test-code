# Hypotenuse Computation API

A FastAPI application that computes the hypotenuse of a right triangle using object-oriented programming principles.

## Features

- Object-oriented design with base compute class
- FastAPI REST API with `/compute` endpoint
- Input validation and error handling
- Docker containerization
- Health check endpoint

## API Endpoints

### POST /compute

Compute the hypotenuse of a right triangle given two sides.

**Request Body:**
```json
{
  "x": 3.0,
  "y": 4.0
}
```

**Response:**
```json
{
  "x": 3.0,
  "y": 4.0,
  "hypotenuse": 5.0,
  "message": "Hypotenuse of right triangle with sides 3.0 and 4.0 is 5.000000"
}
```

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "message": "Hypotenuse Computation API is running successfully"
}
```

## Architecture

### Object-Oriented Structure

- **BaseCompute**: Abstract base class that accepts two variables
- **HypotenuseCompute**: Concrete implementation for hypotenuse calculation
- Follows SOLID principles with clear separation of concerns

### Directory Structure

```
src/
├── __init__.py
├── main.py              # FastAPI application
└── compute/
    ├── __init__.py
    ├── base.py          # BaseCompute abstract class
    └── hypotenuse.py    # HypotenuseCompute implementation
```

## Running the Application

### Using Docker

```bash
# Build the image
docker build -t hypotenuse-api .

# Run the container
docker run -p 8000:8000 hypotenuse-api
```

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## Testing the API

```bash
curl -X POST "http://localhost:8000/compute" \
     -H "Content-Type: application/json" \
     -d '{"x": 3, "y": 4}'
```

## Mathematical Formula

The hypotenuse is calculated using the Pythagorean theorem:

```
hypotenuse = √(x² + y²)
```

The implementation uses Python's `math.hypot()` function for better numerical accuracy.
