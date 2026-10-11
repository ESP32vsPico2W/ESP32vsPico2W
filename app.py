
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>RAIGOTECH CINEMA</title>

<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    background: #070b18;
    color: white;
    font-family: Arial, sans-serif;
}

header {
    padding: 22px;
    text-align: center;
    background: #10182d;
    border-bottom: 2px solid #00e5ff;
}

.logo {
    color: #00e5ff;
    font-size: 28px;
    font-weight: bold;
}

.subtitle {
    color: #a5b4fc;
    margin-top: 8px;
}

main {
    max-width: 1050px;
    margin: auto;
    padding: 30px 16px;
}

h1 {
    text-align: center;
    font-size: clamp(25px, 5vw, 44px);
}

.screen {
    background: #000;
    border: 2px solid #334155;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 0 35px #00e5ff22;
}

video {
    display: block;
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #000;
}

.empty {
    padding: 16px;
    text-align: center;
    color: #94a3b8;
}

.info {
    margin-top: 28px;
    padding: 25px;
    background: #141f36;
    border-radius: 15px;
}

.status {
    color: #67e8f9;
}

footer {
    text-align: center;
    padding: 35px;
    color: #94a3b8;
}
</style>
</head>

<body>

<header>
    <div class="logo">🎬 RAIGOTECH CINEMA</div>
    <div class="subtitle">ANIME AI MOVIE STUDIO</div>
</header>

<main>
    <h1>ESP32 VS PICO 2 W</h1>
    <h2 style="text-align:center;color:#a5b4fc">
        THE FINAL BATTLE
    </h2>

    <div class="screen">
        <video controls playsinline preload="metadata">
            <source src="/static/movie.mp4" type="video/mp4">
            Your browser does not support video.
        </video>
        <div class="empty">
            🎥 Movie coming soon!
        </div>
    </div>

    <div class="info">
        <h2>⚔️ ALPHA VS BETA</h2>
        <p>
            Two powerful robots.
            One futuristic city.
            The ultimate battle begins.
        </p>

        <p class="status">
            ● MOVIE STATUS: IN PRODUCTION
        </p>

        <p>🎬 Directed by R. Grenman</p>
        <p>🤖 ESP32 ALPHA — Green warrior</p>
        <p>🤖 PICO 2 W BETA — Blue warrior</p>
    </div>
</main>

<footer>
    © 2026 RAIGOTECH STUDIOS
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)
