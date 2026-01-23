print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

file_name: str = "ancient_fragment.txt"

print(f"\nAccessing Storage Vault: {file_name}")
try:
    with open(file_name, 'r') as file:
        print("Connection established...")
        print("\nRECOVERED DATA:\n"
              f"{file.read()}")
        file.close()
        print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found")
