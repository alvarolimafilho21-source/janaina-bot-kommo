from fastapi import FastAPI, Request

app = FastAPI(title="Janaina Bot - Kommo Middleware")

@app.get("/")
async def healthcheck():
    return {"status": "ok", "service": "janaina-bot-kommo"}

@app.post("/webhook/kommo")
async def kommo_webhook(request: Request):
    payload = await request.json()
    print("Webhook recebido do Kommo:")
    print(payload)

    return {"result": "received"}
