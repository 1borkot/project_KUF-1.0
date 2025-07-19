from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Khayru Ummah Foundation"}

