import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

    GEMINI_VISION_MODEL = "gemini-2.5-flash"  # For vision/image analysis (Stable Gemini 2.5 Flash - fast and supports vision)
    # Alternatives: "gemini-2.5-pro" (more capable, slower), "gemini-2.5-flash-image" (image-optimized)
    OPENAI_MODEL = "gpt-4"  

    CONFIDENCE_THRESHOLD = 75 
    DIFFERENTIAL_DIAGNOSIS_COUNT = 3

    MAX_RETRIES = 3
    RETRY_DELAY = 2 

    OUTPUT_DIR = "data/outputs"
    AUDIO_DIR = "data/outputs/audio"

    # Medical Disclaimer
    DISCLAIMER = """
    ⚠️ MEDICAL DISCLAIMER
    This is an AI tool for informational purposes only.
    NOT a substitute for professional medical advice.
    Always consult a healthcare provider for medical concerns.
    """