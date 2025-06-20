from fastapi import FastAPI, Query
from abc import hello_world, get_greeting

# Create FastAPI instance
app = FastAPI(
    title="Simple Hello World API",
    description="A simple FastAPI implementation using functions from abc.py",
    version="1.0.0"
)


@app.get("/")
async def root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Hello World API!"}


@app.get("/hello")
async def hello():
    """
    Endpoint that returns Hello World using the function from abc.py
    """
    return {"message": hello_world()}


@app.get("/hello/{name}")
async def hello_name(name: str):
    """
    Endpoint that returns a personalized greeting.
    
    Args:
        name (str): Name to greet
    
    Returns:
        dict: Personalized greeting message
    """
    return {"message": get_greeting(name)}


@app.get("/greet")
async def greet_with_query(name: str = Query(default="World", description="Name to greet")):
    """
    Endpoint that returns a greeting using query parameters.
    
    Args:
        name (str): Name to greet (query parameter)
    
    Returns:
        dict: Greeting message
    """
    return {"message": get_greeting(name)}


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy", "message": "API is running successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)