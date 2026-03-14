import requests
import pandas as pd
import matplotlib as mtl
import matplotlib.pyplot as plt


STATION_NAME = "MADRID-ATOCHA CERCANIAS"
FILE_NAME = "matrix_analysis.png"

print(
    "\nLOADING STATUS: Loading programs...\n"

    "\nChecking dependencies:\n"
    f"[OK] {pd.__name__} ({pd.__version__})"

    " - Data manipulation ready\n"
    f"[OK] {requests.__name__} ({requests.__version__})"
    " -  Network access ready\n"

    f"[OK] {mtl.__name__} ({mtl.__version__})"
    " -  Visualization ready\n"
    )

print("\nAnalyzing Matrix (Renfe's API for passenger traffic by time slot at"
      f" the {STATION_NAME} station) data...")
url = 'https://data.renfe.com/api/3/action/datastore_search'
data = {
    'resource_id': 'a269b1e5-2760-4296-9db8-3339c3dde005',
    'filters': f'{{"NOMBRE_ESTACION":"{STATION_NAME}"}}'
}
response = requests.get(url, data).json()
records = response["result"]["records"]

print(f"Processing {len(records)} data points...")
df = pd.DataFrame(records)
df["TRAMO_HORARIO"] = pd.Categorical(
    df["TRAMO_HORARIO"], ordered=True, categories=df["TRAMO_HORARIO"]
)

print("Generating visualization...")
plt.figure(figsize=(12, 6))
plt.plot(df["TRAMO_HORARIO"], df["VIAJEROS_SUBIDOS"], marker='o', label="Subidos")
plt.plot(df["TRAMO_HORARIO"], df["VIAJEROS_BAJADOS"], marker='o', label="Bajados")
plt.xticks(rotation=45)
plt.xlabel("Tramo horario")
plt.ylabel("Número de viajeros")
plt.title(f"Flujo de viajeros en {STATION_NAME}")
plt.legend()
plt.tight_layout()
print("Analysis complete!")

plt.savefig(FILE_NAME)
print(f"Results saved to: {FILE_NAME}")
