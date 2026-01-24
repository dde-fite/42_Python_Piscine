print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

# Even if these files are not mentioned in the subject, they are necessary.
file_name = "classified_data.txt"
file_name2 = "security_protocols.txt"

print("\nInitiating secure vault access...")

try:
    with open(file_name, 'r') as file, open(file_name2, 'r') as file2:
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:\n"
              f"{file.read()}")
        print("\nSECURE PRESERVATION:\n"
              f"{file2.read()}")
    print("Vault automatically sealed upon completion\n"
          "\nAll vault operations completed with maximum security.")
except FileNotFoundError:
    print(f"\nERROR: {file_name} or {file_name2} not found.\n"
          "You can get it with the 42's generator :)")
