from app.core.config import DEFAULT_SYSTEM_MESSAGE
def get_system_message(adventure_type: str) -> dict:
    return{
        "role": "system",
        "content": DEFAULT_SYSTEM_MESSAGE.format(adventure_type=adventure_type)
    }