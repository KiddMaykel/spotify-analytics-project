-- 1. ¿Quiénes son los 5 artistas más escuchados en Spotify?
SELECT 
    artist_name,
    COUNT(track_name) AS total_canciones,
    SUM(streams) AS total_reproducciones
FROM spotify_clean
GROUP BY artist_name
ORDER BY total_reproducciones DESC
LIMIT 5;

-- 2. ¿Las canciones más rápidas (BPM) son más bailables?
SELECT 
    track_name,
    artist_name,
    bpm,
    danceability_percent
FROM spotify_clean
WHERE danceability_percent > 70
ORDER BY bpm DESC;