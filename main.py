from fastapi import FastAPI, Request
import logging

# =========================
# App FastAPI
# =========================
app = FastAPI()

# =========================
# Logger básico (Render mostra nos Logs)
# =========================
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("janaina-bot-kommo")

# =========================
# Healthcheck
# =========================
@app.get("/")
def healthcheck():
    return {
        "status": "ok",
        "service": "janaina-bot-kommo"
    }

# =========================
# Webhook Kommo
# =========================
@app.post("/kommo/webhook")
async def kommo_webhook(request: Request):
    payload = await request.json()

    logger.info("📩 Webhook recebido do Kommo")
    logger.info(payload)

    message_text = ""

    # Tentativa segura de extrair texto
    try:
        message_text = payload.get("message", {}).get("text", "").lower()
    except Exception:
        pass

    # Decisão inicial
    decision = "bot"

    if "p20" in message_text or "p45" in message_text:
        decision = "human"

    logger.info(f"🤖 Decisão tomada: {decision}")

    return {
        "status": "ok",
        "decision": decision
    }
