from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from BolDriver import BolDriver

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
async def getItems(search: str, amount: int, sort: str):
    print(f"-> Search query: {search} width amount: {amount} with sorting: {sort}")
    bolDriver = BolDriver()
    bolDriver.search = search
    bolDriver.sort = bolDriver.dict_of_sort[sort.strip()]
    items = bolDriver.get_items(amount, [])
    bolDriver.close_browser()
    del bolDriver
    return items