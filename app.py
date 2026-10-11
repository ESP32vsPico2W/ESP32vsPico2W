
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1">
        <title>ESP32 VS PICO 2 W</title>
        <style>
            body {
                background: #080d1c;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 40px 15px;
            }
            h1 { color: #00e5ff; }
            h2 { color: #a5b4fc; }
            .movie {
                margin: 35px auto;
                padding: 40px 15px;
                max-width: 650px;
                background: #17233c;
                border-radius: 18px;
            }
        </style>
    </head>
    <body>
        <h1>RAIGOTECH ANIME AI STUDIO</h1>
        <h2>ESP32 VS PICO 2 W</h2>
        <div class="movie">
            <h2>THE FINAL BATTLE</h2>
            <p>Our first 3D anime movie is coming soon!</p>
            <p>ALPHA vs BETA</p>
        </div>
        <p>Directed by R. Grenman</p>
        <p>© 2026 RAIGOTECH STUDIOS</p>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run()
