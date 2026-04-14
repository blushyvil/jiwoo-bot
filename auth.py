LINE_TOKEN = ""
def get_client():
    global LINE_TOKEN
    if not LINE_TOKEN:
        print("❌ Run: python get_token.py")
        return None
    from linepy import LINE
    client = LINE(LINE_TOKEN)
    print("✅ Jiwoo connected!")
    return client