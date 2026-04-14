from linepy import LINE
client = LINE()
client.login(resend=True)  # QR login
print("=== SAVE THESE ===")
print("Token:", client.authToken)
print("Your MID:", client.profile.mid)
with open("config.py", "a") as f:
    f.write(f'\nOWNER_MID = "{client.profile.mid}"\n')
print("Config updated!")