from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
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

testingData = [
    {
        'title': 'testing title1',
        'image': 'https://media.s-bol.com/x8yYkMN4qAzz/oVwM53N/168x108.jpg',
        'href': 'www.google.com',
        'price': '12.00'  
    },
    {
        'title': 'testing title2',
        'image': 'https://media.s-bol.com/Gx1xz2Vr9pX5/np5pxp/168x177.jpg',
        'href': 'www.google.com',
        'price': '9.00'  
    }
]

@app.post("/")
async def getItems(search: str):
    print(f"-> Search query: {search}")
    return testingData