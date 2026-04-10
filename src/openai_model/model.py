from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from loguru import logger
load_dotenv()

apikey =os.getenv('OPENAI_API_KEY')
logger.info(f"Using API key: {apikey}")



model = init_chat_model(
    model="gpt-5.3-codex",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL"),
    default_headers={
        "User-Agent": "codex_vscode/0.118.0-alpha.2 (Mac OS 26.2.0; arm64) unknown (VS Code; 26.325.31654)",
        "x-stainless-os": "Unknown",
        "x-stainless-lang": "python",
    },
    use_responses_api=True,
    reasoning_effort="xhigh",
)

logger.info(
  f"Initialized chat model : {model}"
)