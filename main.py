from fastapi import FastAPI, Request
import logging

app = FastAPI()

# Logger básico (Render mostra isso em Logs)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("janaina-bot-kommo")

@app.get("/")
def healthcheck():
    return {"status": "ok", "service": "janaina-bot-kommo"}

@app.post("/kommo/webhook")
async def kommo_webhook(request: Request):
    payload = await request.json()

    logger.info("📩 Webhook recebido do Kommo:")
    logger.info(payload)

    # Aqui futuramente:
    # - identificar produto (P13 / P20 / P45)
    # - decidir automático vs humano
    # - chamar API do Kommo para mover funil

    return {"status": "ok"}
