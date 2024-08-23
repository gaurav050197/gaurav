from fastapi import FastAPI
from fastapi.testclient import TestClient

app=FastAPI()

@app.get("/")
async def read_main():
    print("hellow")
    return {"msg": "hellow world"}


