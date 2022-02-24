from fastapi import FastAPI

app = FastAPI()

#this is just a comment
@app.get("/")
def root():
    return "Hello from Cloud Run CD"
