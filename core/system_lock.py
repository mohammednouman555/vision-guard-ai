import os

def lock_system():
    print("🔒 SYSTEM LOCK TRIGGERED")

    # Windows lock
    os.system("rundll32.exe user32.dll,LockWorkStation")