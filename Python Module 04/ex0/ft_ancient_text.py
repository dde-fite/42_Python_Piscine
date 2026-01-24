print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

file_name: str = "ancient_fragment.txt"

print(f"\nAccessing Storage Vault: {file_name}")
try:
    file = open(file_name, 'r')
    print("Connection established...")
    try:
        print("\nRECOVERED DATA:\n"
              f"{file.read()}")
    finally:
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found")
