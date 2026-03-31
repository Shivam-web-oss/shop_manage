from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI( 
    title="Shop Management System - Shivam Gupta",
    version="1.0.0",
    description="Production backend for inventory, sales & reports"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend Running"}
