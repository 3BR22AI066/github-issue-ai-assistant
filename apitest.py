import os
import json
import google.generativeai as genai

# 🔥 TEMPORARY HARD CHECK (FOR DEBUGGING)
print("DEBUG GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))

# ❗ FORCE SET (Windows-safe)
os.environ["GOOGLE_API_KEY"] = "PASTE_YOUR_GEMINI_API_KEY_HERE"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")
