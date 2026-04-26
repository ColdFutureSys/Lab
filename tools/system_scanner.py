import platform
import socket
from datetime import datetime

print("=== ColdFutureSys System Scanner ===\n")

print(f"Machine Name: {socket.gethostname()}")
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Processor: {platform.processor()}")
print(f"Python Version: {platform.python_version()}")
print(f"Current Time: {datetime.now()}")

print("\nScan Complete.")
