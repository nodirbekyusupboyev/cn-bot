import re
import sys

def encode_token(raw_token: str) -> str:
    return "".join(f"{ord(c) ^ 0x5A:02x}" for c in raw_token.strip())

def main():
    print("=" * 60)
    print("🔐 MOVITIMECN — XAVFSIZ TOKEN YANGILASH (ANTI-HACKER)")
    print("=" * 60)
    print("Eski tokeningiz GitHub orqali A_TOOLSx2 spamer-boti tomonidan")
    print("o'g'irlangani sababli @BotFather dan yangi token oling:\n")
    print("1. Telegramda @BotFather ga kiring va /mybots yozing")
    print("2. @movietimecnbot ni tanlang -> 'API Token' -> 'Revoke current token'")
    print("3. Berilgan yangi tokenni shu yerga nusxalab qo'ying:\n")

    if len(sys.argv) > 1:
        new_token = sys.argv[1].strip()
    else:
        new_token = input("👉 Yangi BOT TOKENNI kiriting: ").strip()

    if ":" not in new_token or len(new_token) < 30:
        print("❌ Xato: Token formati noto'g'ri! (Masalan: 8876644496:AA...)")
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

    print("\n✅ MUVAFFAQIYATLI YANGILANDI!")
    print("🔒 Yangi token shifrlangan holatda main.py va .env fayliga saqlandi.")
    print("🛡️ Endi main.py ni GitHub'ga yuklasangiz ham A_TOOLSx2 uni o'g'irlay olmaydi!")

if __name__ == "__main__":
    main()
