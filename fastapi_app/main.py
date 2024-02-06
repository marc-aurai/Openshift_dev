from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

def generate_random_color():
    """Generate a random hexadecimal color code."""
    return '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

color = generate_random_color()

@app.get("/", response_class=HTMLResponse)
async def get_random_color_page():
    """Return a simple HTML page with a random background color."""
    
    page_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Random Background Color</title>
        <style>
            body {{
                background-color: {color};
            }}
            h1 {{
                color: white;
                text-align: center;
                margin-top: 40vh;
            }}
        </style>
    </head>
    <body>
        <h1>This page has a random background color</h1>
    </body>
    </html>
    """
    return page_content
