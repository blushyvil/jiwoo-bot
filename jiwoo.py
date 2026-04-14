from linepy import LINE
import time
with open("token.txt") as f:
    token = f.read().strip()
client = LINE(token)
print("🤖 Jiwoo Protection ACTIVE!")

def kick(gid,mid):
    try:
        client.kickoutFromGroup(gid,[mid])
        print(f"👢 Kicked {mid[:8]}")
    except:pass

while True:
    try:
        ops = client.fetchOperations(50,1)
        for op in ops:
            if op.type == 13:  # Invite
                kick(op.param1, op.param2)  # Inviter
                kick(op.param1, op.param3)  # Invited
            elif op.type in [25,26,140,141]:  # Notes/Album
                kick(op.param1, op.param2)
        time.sleep(0.2)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(3)