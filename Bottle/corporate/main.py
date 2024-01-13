from bottle import route, run, template,static_file
from dashboards import *
from apps import *
from pages import *
from components import *
from layouts import *

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

if __name__ == '__main__':
    run()