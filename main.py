from fastapi import FastAPI, HTTPException
from keiba_scraping import EntryPageScraper

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


@app.get("/race/{race_id}")
def get_race(race_id: str):
    try:
        if not race_id.isdigit():
            raise HTTPException(
                status_code=400,
                detail="race_idは数字で入力してください"
            )

        scraper = EntryPageScraper(race_id)

        race_info = scraper.get_race_info()
        entry = scraper.get_entry()

        return {
            "status": "ok",
            "race_id": race_id,
            "race_info": race_info.to_dict(orient="records"),
            "horses": entry.to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )