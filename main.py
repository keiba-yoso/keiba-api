from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "競馬APIは起動しています"
    }

@app.get("/test")
def test():
    return {
        "status": "ok",
        "message": "API接続テスト成功"
    }
}