import platform
import socket
import os

print("=== SYSTEM DASHBOARD ===")

print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Machine: {platform.machine()}")

print(f"Hostname: {socket.gethostname()}")

print(f"Current Directory: {os.getcwd()}")
