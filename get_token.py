import os
from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()

CA_BUNDLE_PATH = os.getenv("CA_BUNDLE_PATH", "russian_trusted_root_ca.cer")

def get_gigachat_token():
    credentials = os.getenv("GIGACHAT_API_KEY")
    if not credentials:
        raise ValueError("GIGACHAT_API_KEY не найден в .env")
    giga = GigaChat(credentials=credentials, ca_buntle_file=CA_BUNDLE_PATH)
    return giga.get_token()

if __name__ == "__main__":
    token = get_gigachat_token()
    print(token)