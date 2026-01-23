to_preverve: str = "{[}ENTRY 001{]} New quantum algorithm discovered\n\
{[}ENTRY 002{]} Efficiency increased by 347%\n\
{[}ENTRY 003{]} Archived by Data Archivist trainee"

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

file_name: str = " new_discovery.txt"

print(f"\nInitializing new storage unit: {file_name}")

try:
    with open(file_name, 'x') as file:
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...\n"
              f"{to_preverve}")
        file.write(to_preverve)
        file.close()
        print("\nData inscription complete. Storage unit sealed.\n"
              "Archive 'new_discovery.txt' ready for long-term preservation")
except FileExistsError:
    print("ERROR: A storage vault already exists")
