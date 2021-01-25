import os

from flask_api import FlaskAPI

app = FlaskAPI(__name__)
app.config.from_json(
    os.getenv("APPLICATION_SETTINGS", "../settings.json")
)
