"""gunicorn WSGI server configuration."""
import os
from multiprocessing import cpu_count

bind = f"0.0.0.0:{os.getenv('GUNICORN_PORT', 5000)}"
workers = os.getenv("GUNICORN_WORKER_COUNT", cpu_count() - 1)
