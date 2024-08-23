
from fastapi import FastAPI
import string

app = FastAPI()


@app.get("/")
async def get_details(x1: str, x2: str):
    return int(x2)*int(x1)


@app.get("/second_route")
async def hello_char():
    return "hurrrrrrrrr"


@app.get('/gaurav')
async def division(x1: int,x2 : int):
    return x1/x2
if __name__=="__main__":
 uvicorn.run("main:app")
