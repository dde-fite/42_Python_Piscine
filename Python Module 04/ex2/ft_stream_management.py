import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

id: str = input("\nInput Stream active. Enter archivist ID: ")
status: str = input("Input Stream active. Enter status report: ")

sys.stdout.write("\n{[}STANDARD{]} Archive status from "
                 f"{id}: {status}\n")
sys.stderr.write("{[}ALERT{]} System diagnostic: Communication channels "
                 "verified\n")
sys.stdout.write("{[}STANDARD{]} Data transmission complete\n")

print("\nThree-channel communication test successful")
