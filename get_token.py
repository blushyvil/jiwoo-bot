from linepy import LINE
print("🔐 Scan QR with LINE app")
client = LINE()
client.loginWithQrCode()
with open("token.txt","w") as f:
    f.write(client.authToken)
print("✅ TOKEN SAVED to token.txt")