from fastapi import FastAPI, APIRouter
import datetime as dt

app = FastAPI()
router = APIRouter()   # tags=['Admin'], prefix="/admin")


@app.get("/")
async def read_root():
  return {"now": str(dt.datetime.now())}
