from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# allow react frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/simulate")
def simulate():
    return {
        "particles": [
            {"id": 1, "type": "electron", "position": [0,0]},
            {"id": 1, "type": "proton", "position": [1,1]},
        ]
    }