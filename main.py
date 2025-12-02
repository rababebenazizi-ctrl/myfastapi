from fastapi import FastAPI, UploadFile, File, Form
import httpx

app = FastAPI()

# -------------------------
# 1) Route Home (juste pour tester)
# -------------------------
@app.get("/")
def home():
    return {"message": "Hello Rabab, FastAPI is running!"}


# -------------------------
# 2) Route 1 — DOCS UPLOADER
# -------------------------
@app.post("/api/docs-uploader")
async def docs_uploader(file: UploadFile = File(...)):

    n8n_webhook = "https://n8n-production-56fbf.up.railway.app/webhook/Google_Drive"

    async with httpx.AsyncClient() as client:
        response = await client.post(
            n8n_webhook,
            files={"file": (file.filename, await file.read(), file.content_type)},
        )

    return response.json()


# -------------------------
# 3) Route 2 — ASSISTANT
# -------------------------
@app.post("/api/assistant")
async def assistant(message: str = Form(...)):

    n8n_webhook = "https://n8n-production-56fbf.up.railway.app/webhook/ab8dd537-7c64-47d7-adf0-42152d1f8f68"

    async with httpx.AsyncClient() as client:
        response = await client.post(
            n8n_webhook,
            data={"message": message},
        )

    return response.json()


# -------------------------
# 4) Route 3 — SMART SOLUTION
# -------------------------
@app.post("/api/smart-solution")
async def smart_solution(text: str = Form(...)):

    n8n_webhook = "https://n8n-production-56fbf.up.railway.app/webhook/save-solution"

    async with httpx.AsyncClient() as client:
        response = await client.post(
            n8n_webhook,
            data={"text": text},
        )

    return response.json()
