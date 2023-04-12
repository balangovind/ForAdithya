from fastapi import FastAPI
from .database import connect_to_mongo, close_mongo_connection
from .routers import user_router

app = FastAPI()

# Connect to MongoDB when the application starts up
app.add_event_handler("startup", connect_to_mongo)

# Close the MongoDB connection when the application shuts down
app.add_event_handler("shutdown", close_mongo_connection)

# Mount the user router
app.include_router(user_router)

