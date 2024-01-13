from bottle import route, run, template

@route('/')
def index():
    title = "Dashboard"
    return template('dashboards/index',title=title)

@route('/dashboard-analytics')
def dashboard_analytics():
    title = "Analytics"
    return template('dashboards/dashboard-analytics',title=title) 

@route('/dashboard-crm')
def dashboard_crm():
    title = "CRM"
    return template('dashboards/dashboard-crm',title=title)       

@route('/dashboard-crypto')
def dashboard_crypto():
    title = "Crypto"
    return template('dashboards/dashboard-crypto',title=title)

@route('/dashboard-crypto')
def dashboard_crypto():
    title = "Crypto"
    return template('dashboards/dashboard-crypto',title=title)    

@route('/dashboard-projects')
def dashboard_projects():
    title = "Projects"
    return template('dashboards/dashboard-projects',title=title)     

@route('/dashboard-nft')
def dashboard_nft():
    title = "NFT Dashboard"
    return template('dashboards/dashboard-nft',title=title) 

@route('/dashboard-job')
def dashboard_job():
    title = "Job Dashboard"
    return template('dashboards/dashboard-job',title=title)          

    