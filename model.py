import base64
import requests
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

def analyze_text_and_generate_recipe(text_query):
    prompt = (
        f"{text_query}\n\n"
        "Identify the name of the dish as 'Item', then list ingredients, explain preparation steps, "
        "and suggest 2–3 related dishes. Format your response with these headings:\n"
        "Item:\nIngredients:\nPreparation:\nOther Recipes:"
    )

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        headers=headers,
        json=payload
    )
    data = response.json()
    if "candidates" in data and data["candidates"]:
        response_text = data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        print("API response error or unexpected format:", data)
        response_text = "Sorry, could not get a valid response from the model."

    return parse_response(response_text)

def parse_response(text):
    sections = {"item": "", "ingredients": "", "preparation": "", "related_recipes": ""}
    lower_text = text.lower()

    try:
        # Split by headings
        item_split = text.split("Item:")[-1].split("Ingredients:")
        sections["item"] = item_split[0].strip()
        ing_split = item_split[1].split("Preparation:")
        sections["ingredients"] = ing_split[0].strip()
        prep_split = ing_split[1].split("Other Recipes:")
        sections["preparation"] = prep_split[0].strip()
        sections["related_recipes"] = prep_split[1].strip()
    except Exception:
        sections["ingredients"] = text

    return sections
