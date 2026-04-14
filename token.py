#!/usr/bin/env python3
import os
from linepy import LINE

print("🔐 Getting token...")

# Create LINE client
client = LINE()

# QR Login
print("📱 Scan QR with LINE app:")
client.login(resend=True)

# Save config
mid = client.profile.mid
token = client.authToken

config_content = f'''OWNER_MID = "{mid}"
ADMIN_MIDS = []
PROTECT = True
AUTOJOIN = True
'''

with open("config.py", "w") as f:
    f.write(config_content)

print("✅ SAVED!")
print("Token:", token[:20] + "...")
print("MID:", mid)
print("🎉 Run: python main.py")