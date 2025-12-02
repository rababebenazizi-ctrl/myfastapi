from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()

# ============================
# WEBHOOK URLs (n8n)
# ============================

N8N_SMART_SOLUTION = "https://n8n-production-56fbf.up.railway.app/webhook/save-solution"
N8N_ASSISTANT = "https://n8n-production-56fbf.up.railway.app/webhook/ab8dd537-7c64-47d7-adf0-42152d1f8f68"
N8N_DOCS_UPLOADER = "https://n8n-production-56fbf.up.railway.app/webhook/Google_Drive"

# ============================
# Request Models
# ============================

class UserRequest(BaseModel):
    message: str
    user_id: str = "default"

# ============================
# API ROUTES
# ============================

# 1) Smart Solution
@app.post("/api/smart-solution")
async def smart_solution(req: UserRequest):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(N8N_SMART_SOLUTION, json=req.dict())
        return {"status": "sent_to_n8n", "n8n_response": r.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 2) Assistant
@app.post("/api/assistant")
async def assistant(req: UserRequest):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(N8N_ASSISTANT, json=req.dict())
        return {"status": "sent_to_n8n", "n8n_response": r.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 3) Docs Uploader
@app.post("/api/docs-uploader")
async def docs_uploader(req: UserRequest):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.post(N8N_DOCS_UPLOADER, json=req.dict())
        return {"status": "sent_to_n8n", "n8n_response": r.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
