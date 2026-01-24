to_preverve: str = "{[}ENTRY 001{]} New quantum algorithm discovered\n\
{[}ENTRY 002{]} Efficiency increased by 347%\n\
{[}ENTRY 003{]} Archived by Data Archivist trainee"

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

file_name: str = "new_discovery.txt"

print(f"\nInitializing new storage unit: {file_name}")

try:
    file = open(file_name, 'x')
    print("Storage unit created successfully...")
    try:
        print("\nInscribing preservation data...\n"
              f"{to_preverve}")
        file.write(to_preverve)
    finally:
        file.close()
        print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation")
except FileExistsError:
    print("ERROR: A storage vault already exists")
