import aiohttp_jinja2

#Dashboards Pages

@aiohttp_jinja2.template('layouts/layouts-horizontal.html')
async def layouts_horizontal(request):
    pass

@aiohttp_jinja2.template('layouts/layouts-detached.html')
async def layouts_detached(request):
    pass

@aiohttp_jinja2.template('layouts/layouts-twocolumn.html')
async def layouts_twocolumn(request):
    pass

@aiohttp_jinja2.template('layouts/layouts-hovered.html')
async def layouts_hovered(request):
    pass