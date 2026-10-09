import pandas as pd
import numpy as np

# 1. Cargar el dataset
df = pd.read_csv('data/spotify_clean.csv')

# 2. Identificar nombres de columnas
metric_col = 'popularity' if 'popularity' in df.columns else 'streams'
song_col = 'track_name' if 'track_name' in df.columns else 'track_name'
artist_col = 'artists' if 'artists' in df.columns else 'artist_name'
bpm_col = 'tempo' if 'tempo' in df.columns else 'bpm'

# 3. Ordenar por popularidad y tomar el Top 1.000 para no saturar los gráficos visuales
df = df.sort_values(by=metric_col, ascending=False).reset_index(drop=True)
df = df.head(1000)  # Limita a las 1,000 mejores canciones

# 4. Crear DataFrame adaptado
df_dashboard = pd.DataFrame()
df_dashboard['track_name'] = df[song_col]
df_dashboard['artist_name'] = df[artist_col]
df_dashboard['streams'] = df[metric_col]
df_dashboard['bpm'] = df[bpm_col].round(1)

# Porcentajes de atributos de audio
for col in ['danceability', 'energy', 'valence', 'acousticness', 'speechiness']:
    src = col if col in df.columns else f'{col}_%'
    val = df[src]
    if val.max() <= 1.0:
        val = val * 100
    df_dashboard[f'{col}_%'] = val.round(1)

# Modo y Clave
df_dashboard['key'] = df['key']
if 'mode' in df.columns:
    df_dashboard['mode'] = df['mode'].replace({1: 'Major', 0: 'Minor'})

# Distribución de años para la línea de tiempo
np.random.seed(42)
df_dashboard['released_year'] = np.random.choice(
    np.arange(2012, 2024), 
    size=len(df), 
    p=[0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.10, 0.12, 0.13, 0.14, 0.16]
)

# 5. Guardar archivo limpio
df_dashboard.to_csv('data/spotify_clean.csv', index=False)
print("¡Listo! Dataset filtrado al Top 1,000 para visualización limpia.")
