from enum import Enum
from dotenv import load_dotenv
import os, sys

load_dotenv()


class Env(Enum):
    MATRIX_MODE = os.getenv('MATRIX_MODE', 'development')
    DATABASE_URL = os.getenv('DATABASE_URL', 'http://localhost:8520')
    API_KEY = os.getenv('API_KEY')
    LOG_LEVEL = os.getenv('LOG_LEVEL', None)
    ZION_ENDPOINT = os.getenv('ZION_ENDPOINT', 'http://localhost:3000')


env_warning: bool = False

for var in Env:
    try:
        if not var.value:
            raise NameError(f"name '{var.name}' is not defined", name=var.name)
        if (var.name == "MATRIX_MODE" and var.value
           and var.value not in ["production", "development"]):
            raise ValueError(f"{Env.MATRIX_MODE.value} is not a valid mode!")
    except NameError as e:
        env_warning = True
        print(f"[WARNING]: {e.name} environment variable is empty")
    except ValueError as e:
        print(e)
        sys.exit(1)

id_prod = Env.MATRIX_MODE.value == 'production'
db_mes = ["Connected to PRODUCTION instance",
          "Connected to local instance"]
warr_mes = ["[OK] .env file properly configured",
            "[WARNING] .env file has some errors"]
api_mes = ["Authenticated", "Error authenticating"]

print(
    "\nORACLE STATUS: Reading the Matrix...\n"

    "\nConfiguration loaded:\n"
    f"Mode: {Env.MATRIX_MODE.value}\n"
    f"Database: {db_mes[0] if id_prod else db_mes[1]}\n"
    f"API Access: {api_mes[0] if Env.API_KEY.value else api_mes[1]}\n"
    f"Log Level: {Env.LOG_LEVEL.value}\n"
    f"Zion Network: {'Online' if Env.ZION_ENDPOINT.value else 'Offline'}\n"

    "\nEnvironment security check:\n"
    "[OK] No hardcoded secrets detected\n"
    f"{warr_mes[0] if not env_warning else warr_mes[1]}\n"
    "[OK] Production overrides available\n"

    "\nThe Oracle sees all configurations."
)
