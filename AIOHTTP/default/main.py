from aiohttp import web
import aiohttp_jinja2
import jinja2

from settings import  BASE_DIR
from routes import setup_routes

app = web.Application()

aiohttp_jinja2.setup(app,loader=jinja2.FileSystemLoader(str(BASE_DIR / 'default' / 'templates')))

setup_routes(app)

web.run_app(app, host="localhost", port=8080)