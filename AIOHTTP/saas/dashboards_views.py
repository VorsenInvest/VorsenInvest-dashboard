import aiohttp_jinja2

#Dashboards Pages

@aiohttp_jinja2.template('dashboards/index.html')
async def index(request):
    pass

@aiohttp_jinja2.template('dashboards/dashboard-analytics.html')
async def dashboard_analytics(request):
    pass

@aiohttp_jinja2.template('dashboards/dashboard-crm.html')
async def dashboard_crm(request):
    pass

@aiohttp_jinja2.template('dashboards/dashboard-crypto.html')
async def dashboard_crypto(request):
    pass

@aiohttp_jinja2.template('dashboards/dashboard-projects.html')
async def dashboard_projects(request):
    pass

@aiohttp_jinja2.template('dashboards/dashboard-projects.html')
async def dashboard_projects(request):
    pass

@aiohttp_jinja2.template('dashboards/dashboard-nft.html')
async def dashboard_nft(request):
    pass

@aiohttp_jinja2.template('dashboards/dashboard-job.html')
async def dashboard_job(request):
    pass    