from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
  return{"message": "Welcome to the Quote API!"}



#create main FastAPI entrypoint 
