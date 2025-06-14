# 🍽️ Smart Recipe Helper

A multimodal food assistant that takes either an image or a text input and generates:
- A list of ingredients
- Step-by-step preparation instructions
- Suggested other recipes using similar ingredients

Built using:
- **Google Gemini Pro Vision** for image-based recipe generation
- **Google Gemini Pro LLM** for text-based recipe generation
- **Streamlit** for a smooth and interactive UI
- **Python** (MCP architecture: Model-Controller-Presenter)

---

## 🧠 How It Works

### 🔍 Input Modes
- **📷 Upload an Image**: Upload a picture of a food item, and Gemini Vision will identify the dish, ingredients, and preparation.
- **💬 Text Prompt**: Enter a dish name or cooking query (e.g., _“How to make paneer biryani?”_), and Gemini LLM will return a full recipe.

Both modes can be used independently, with their own **"Generate Recipe"** buttons.

---

## 🧱 Architecture

This project follows the **MCP (Model-Controller-Presenter)** design pattern:
```
smart-recipe-helper/
├── app.py                      ← Streamlit UI (Presenter)
├── smartRecipeHelper/
│   ├── controller/
│   │   └── controller.py       ← Handles logic between model and UI
│   └── model/
│       └── model.py            ← Gemini API integration and parsing
├── .env                        ← Stores Gemini API Key
├── requirements.txt
└── README.md

```
---

## 🧠 Models Used

| Model                    | Purpose                                 | Provider         |
|-------------------------|-----------------------------------------|------------------|
| `gemini-pro-vision`     | Image + prompt → recipe                 | Google Gemini API |
| `gemini-pro`            | Text prompt → recipe                    | Google Gemini API |

These models were accessed via Gemini's `generateContent` API endpoint.

---

## 🚀 Setup & Run Locally

##Create .env File

Add your Gemini API key:
```
GEMINI_API_KEY=your-api-key-here
```
Install Requirements
```
pip install -r requirements.txt
```
Run the App

```
streamlit run app.py
```

---

## 📸 Example

Upload an Image:

Type a Query:

“How to make pasta carbonara?”

---

## 📦 Features
	•	Supports both text and image input (dual mode)
	•	Displays actual uploaded image and a sample dish image for text input
	•	Handles API failures gracefully
	•	Uses session_state to retain results without reprocessing

---

## 🛠️ Built With
	•	Streamlit
	•	Python
	•	Google Gemini API
	•	Pillow
	•	Requests

---

## 📄 License

MIT License © 2025 [VenkataSiva Naga Sai Aravind Kollipara]

---

## 🙌 Acknowledgements
	•	Food images: Unsplash
	•	LLM & Vision models: Google Gemini
