from fastapi import FastAPI
from fastapi.testclient import TestClient

app=FastAPI()

@app.get("/")
async def read_main():
    return {"msg": "hellow world"}

Client= TestClient(app)

def test_read_main():
    response=Client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hellow world"}
