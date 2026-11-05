import re
import sys

def encode_token(raw_token: str) -> str:
    return "".join(f"{ord(c) ^ 0x5A:02x}" for c in raw_token.strip())

def main():
    if len(sys.argv) > 1:
        new_token = sys.argv[1].strip()
    else:
        new_token = input("Yangi BOT TOKENNI kiriting: ").strip()

    if ":" not in new_token or len(new_token) < 30:
        print("Xato: Token formati noto'g'ri!")
        return

    enc_hex = encode_token(new_token)

    with open("main.py", "r", encoding="utf-8") as f:
        code = f.read()

    updated_code = re.sub(
        r'_ENC_TOKEN\s*=\s*"[0-9a-fA-F]+"',
        f'_ENC_TOKEN = "{enc_hex}"',
        code
    )

    with open("main.py", "w", encoding="utf-8") as f:
        f.write(updated_code)

    with open(".env", "w", encoding="utf-8") as f:
        f.write(f"BOT_TOKEN={new_token}\n")

    print("MUVAFFAQIYATLI YANGILANDI!")

if __name__ == "__main__":
    main()
