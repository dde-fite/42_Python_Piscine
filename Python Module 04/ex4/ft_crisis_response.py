print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

file_name: str = "lost_archive.txt"
file_name2: str = "classified_vault.txt"  # To test this, you must create a \
# file without read permissions.
file_name3: str = "standard_archive.txt"

try:
    print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
    with open(file_name) as file:
        print("Oops, this was not expected to happen. :v")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
finally:
    print("STATUS: Crisis handled, system stable")

try:
    print(f"\nCRISIS ALERT: Attempting access to '{file_name2}'...")
    with open(file_name2) as file:
        print("Oops, this was not expected to happen. :v")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix\n"
          "\nIf you want to test the error of the subject, create a file "
          "without read permissions\n")
except PermissionError:
    print("RESPONSE: Security protocols deny access")
finally:
    print("STATUS: Crisis handled, security maintained")

try:
    print(f"\nROUTINE ALERT: Attempting access to '{file_name3}'...")
    with open(file_name3) as file:
        print(f"SUCCESS: Archive recovered - ``{file.read()}''")
except FileNotFoundError:
    print("RESPONSE: Archive not found in storage matrix\n"
          "\nIf you want to test the error of the subject, use the generator "
          f"and copy the file {file_name3}\n")
except PermissionError:
    print("RESPONSE: Security protocols deny access\n"
          "\nWhat have you done?\n")
finally:
    print("STATUS: Normal operations resumed")
