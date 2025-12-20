import os
import logging
from typing import Optional

logger = logging.getLogger("llm_client")

LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "mock")  # "openai" or "mock"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")

# Only import openai if provider is openai, avoid heavy deps in mock flow
_openai = None
if LLM_PROVIDER == "openai":
    try:
        import openai as _openai
        _openai.api_key = OPENAI_API_KEY
    except Exception as e:
        logger.error("Failed to import openai: %s", e)
        _openai = None

class LLMClient:
    """
    Minimal LLM client wrapper.
    - If LLM_PROVIDER=openai and key present, calls OpenAI ChatCompletions (gpt-3.5-turbo or configurable).
    - Otherwise, runs in mock mode (returns input or a simple templated reply).
    """

    def __init__(self):
        self.provider = LLM_PROVIDER
        self.model = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")
        self.max_tokens = int(os.environ.get("LLM_MAX_TOKENS", "512"))

    def generate_reply_in_telugu(self, user_text: str, context: Optional[str] = None) -> str:
        """
        Generate a natural Telugu response. system_prompt enforces Telugu-only replies and briefness.
        """
        if self.provider != "openai" or _openai is None:
            # Mock behavior: just echo with a Telugu prefix (POC only)
            mock_reply = "సరే — నేను సహాయపడతాను: " + (context or user_text)
            return mock_reply

        system_prompt = (
            "మీ రెస్పాన్స్‌లు తప్పకుండా తెలుగు లో మాత్రమే ఉండాలి. "
            "సంపూర్ణ వాక్యాలలో సున్నితంగా మరియు స్పష్టంగా వ్యవహరించండి. "
            "సమాధానం సంక్షిప్తంగా, తెలియచేసే రూపంలో ఉండాలి."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"సందర్భం: {context or 'ప్రస్తుత సంభాషణ'}\nచివరి వినియోగదారుడు వాక్యం: {user_text}\nదయచేసి సంక్షిప్తంగా మరియు స్పష్టంగా తెలుగులో స్పందించండి."}
        ]

        try:
            resp = _openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                temperature=0.2,
            )
            txt = resp["choices"][0]["message"]["content"].strip()
            return txt
        except Exception as e:
            logger.exception("LLM call failed: %s", e)
            # Fallback: return mock reply
            return "క్షమించండి — ప్రస్తుతం వివరణ సిద్ధంగా లేదు. దయచేసి మరింత వివరించండి."