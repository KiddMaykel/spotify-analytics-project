import pandas as pd

# 1. Abrimos el archivo de datos
df = pd.read_csv('../data/spotify_clean.csv')

# 2. Dejamos los nombres de columnas bonitos y sin espacios
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 3. Nos aseguramos de que 'streams' sea un número
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

# 4. Quitamos filas sin información importante
df = df.dropna(subset=['track_name', 'artist_name', 'streams'])

# 5. Guardamos el resultado limpio
df.to_csv('../data/spotify_clean.csv', index=False)
print("¡Listo! Datos limpios y preparados con éxito.")