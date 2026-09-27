from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

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


@app.get("/jra")
def jra_test():
    url = "https://www.jra.go.jp/JRADB/accessD.html"

    try:
        response = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = soup.title.string if soup.title else ""

        return {
            "status": "ok",
            "http_status": response.status_code,
            "title": title,
            "message": "JRAへの接続テスト成功"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }