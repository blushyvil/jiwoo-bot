from linepy import LINE, OpType
from config import *
import sys, time

client = LINE()
client.login(token=OWNER_MID if OWNER_MID else None)

print("🤖 jiwoo-bot v2.0 | Owner:", OWNER_MID)
print("🛡️ Protection:", "ON" if PROTECT else "OFF")

def kick_inviter(op):
    try:
        if op.type == 13 and op.param3 == "1":  # Someone invited
            inviter = op.param2
            if inviter != OWNER_MID:
                client.kickoutFromGroup(op.param1, [inviter])
                print(f"👢 Kicked inviter: {inviter[:10]}...")
    except: pass

def ban_kicker(op):
    try:
        if op.type == 32:  # Member kicked
            kicker = op.param3
            if kicker and kicker != OWNER_MID:
                client.kickoutFromGroup(op.param1, [kicker])
                print(f"🚫 Banned kicker: {kicker[:10]}...")
    except: pass

def album_protect(op):
    try:
        if op.type == 140:  # Album created
            client.reissueGroupAlbum(op.param1)
            print("📸 Album removed")
    except: pass

def notes_protect(op):
    try:
        if op.type == 55:  # Notes changed
            client.updateGroupNote(op.param1, "[jiwoo-bot protected]")
            print("📝 Notes restored")
    except: pass

@client.on_message()
def on_message(op):
    try:
        if AUTOJOIN and op.type == 13:
            client.acceptGroupInvitation(op.param1)
        
        if PROTECT:
            kick_inviter(op)
            ban_kicker(op)
            album_protect(op)
            notes_protect(op)
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    try:
        client.runListener()
    except KeyboardInterrupt:
        print("\n👋 Bot stopped")
        sys.exit()