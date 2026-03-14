import sys
import os
import site

is_venv = sys.prefix != sys.base_prefix

matrix_status = "You're still plugged in" if not is_venv \
    else "Welcome to the construct"

if not is_venv:
    result_mes = (
        "Virtual Environment: None detected\n"

        "\nWARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n"

        "\nTo enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\n"
        "Scripts\n"
        "activate # On Windows\n"

        "\nThen run this program again."
    )
else:
    result_mes = (
        f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
        f"Environment Path: {sys.prefix}\n"

        "\nSUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n"

        "\nPackage installation path:\n"
        f"{site.getsitepackages()[0]}"
    )

print(f"\nMATRIX STATUS: {matrix_status}\n"

      f"\nCurrent Python: {sys.executable}\n"
      f"{result_mes}")
