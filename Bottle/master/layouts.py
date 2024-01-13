from bottle import route, run, template

@route('/layouts/horizontal')
def layouts_horizotnal():
    title = "Horizontal Layout"
    return template('layouts/layouts-horizontal',title=title)

@route('/layouts/detached')
def layouts_detached():
    title = "Detached Layout"
    return template('layouts/layouts-detached',title=title)   
    
@route('/layouts/twocolumn')
def layouts_horizotnal():
    title = "Two Column Layout"
    return template('layouts/layouts-twocolumn',title=title)     

@route('/layouts/hovered')
def layouts_hovered():
    title = "Vertical Hovered Layout"
    return template('layouts/layouts-hovered',title=title)     