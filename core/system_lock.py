import os
import platform

def lock_system():
    try:
        if platform.system() == "Windows":
            os.system("rundll32.exe user32.dll,LockWorkStation")
    except Exception as e:
        print("❌ Lock failed:", e)