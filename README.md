# 📊 Spotify Data Analytics & Interactive Dashboard

¡Bienvenido a mi proyecto de análisis de datos de Spotify!

🌐 **[👉 Ver Dashboard Interactivo en Vivo](https://kiddmaykel.github.io/spotify-analytics-project/)**

---

Este proyecto realiza un análisis integral del dataset de Spotify (*Most Streamed Songs*), abarcando desde la limpieza de datos con **Python**, consultas estratégicas con **SQL**, hasta la visualización en un **Dashboard Interactivo Web**.

---

## 🛠️ Herramientas Utilizadas

- **Python (Pandas & NumPy):** Limpieza de datos, tratamiento de nulos, transformación y muestreo.
- **SQL:** Consultas para análisis de reproducciones, tendencias y artistas top.
- **HTML / CSS / JavaScript (Chart.js):** Desarrollo del Dashboard interactivo.

---

## 💡 Hallazgos Clave

1. **Tempo Ideal:** Las canciones con un tempo de **110 a 130 BPM** concentran el mayor número de reproducciones.
2. **Bailabilidad:** Las canciones con más del **70% de Danceability** tienen mayor presencia en las playlists globales.

> 💡 **Nota de Arquitectura de Datos:**  
> Para la capa de visualización interactiva se aplicó un filtrado del **Top 1,000 de canciones más populares** mediante Python. Esto optimiza el rendimiento del navegador (renderizado DOM) y evita el solapamiento de puntos (*overplotting*) en el gráfico de dispersión, permitiendo analizar de forma clara las tendencias de audio del catálogo.

---

## 📁 Estructura del Repositorio

- `index.html` : Dashboard interactivo web.
- `data/` : Dataset procesado (`spotify_clean.csv`).
- `scripts/` : Códigos de limpieza en Python (`01_limpieza.py`) y consultas SQL.
