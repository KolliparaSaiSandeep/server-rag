from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from supabase import create_client, Client
import os
from routers import users

load_dotenv()  # Load environment variables from .env file

supabase_url = os.getenv("SUPABASE_API_URL")
supabase_key = os.getenv("SUPABASE_API_KEY")

if not supabase_url or not supabase_key:
    raise ValueError("SUPABASE_API_URL and SUPABASE_API_KEY must be set in the .env file")

supabase: Client = create_client(supabase_url, supabase_key)