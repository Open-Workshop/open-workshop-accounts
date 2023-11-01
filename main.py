from fastapi import FastAPI
from starlette.responses import RedirectResponse
import aiohttp
import json
import gunicorn_config


SERVER_ADDRESS = "http://127.0.0.1:8000"


app = FastAPI(
    title="Open Workshop Accounts",
    contact={
        "name": "GitHub",
        "url": "https://github.com/Open-Workshop/open-workshop-accounts"
    },
    license_info={
        "name": "MPL-2.0 license",
        "identifier": "MPL-2.0",
    },
)


@app.get("/")
async def main():
    """
    Переадресация на `/docs`
    """
    return RedirectResponse(url="/docs")

@app.get("/test")
async def main():
    """
    Тестовая функция
    """
    try:
        async with aiohttp.ClientSession() as session:
            resource = await session.get(url=SERVER_ADDRESS + "/access/test/" + gunicorn_config.token_test, timeout=10)
            content = await resource.text()
            info = json.loads(content)

            return info
    except:
        return 500

