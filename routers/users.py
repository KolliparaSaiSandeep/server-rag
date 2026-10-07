import os
from fastapi import APIRouter, HTTPException
from database import supabase
from supabase import Client
from pydantic import BaseModel

router= APIRouter(tags=["users"])
@router.post("/create-user")
async def clerk_webhook(webhook_data: dict):
    try:
        event_type = webhook_data.get("type")
        if event_type == "user.created":
            clerk_id = webhook_data.get("data", {}).get("id", {})
            if not clerk_id:
                raise HTTPException(status_code=500, detail="Clerk ID not found in webhook data.")
            result= supabase.table("users").insert({"clerk_id": clerk_id}).execute()
            return {"message": "User created successfully", "clerk_id": clerk_id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/posts")
async def get_all_posts():
    try:
        response = supabase.table("posts").select("*").order("created_at", desc=True).execute()
        error = getattr(response, "error", None)
        if error is not None:
            message = getattr(error, "message", str(error))
            return {"error": message}
        return {"data": getattr(response, "data", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))