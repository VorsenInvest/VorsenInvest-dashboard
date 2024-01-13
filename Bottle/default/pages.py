from bottle import route, run, template

#Pages Page
@route('/pages/starter')
def starter():
    title = "Starter"
    return template('pages/pages-starter',title=title)

@route('/pages/profile')
def profile():
    title = "Profile"
    return template('pages/pages-profile',title=title)    

@route('/pages/profile-settings')
def profile_settings():
    title = "Profile Settings"
    return template('pages/pages-profile-settings',title=title)        

@route('/pages/team')
def team():
    title = "Team"
    return template('pages/pages-team',title=title)     

@route('/pages/timeline')
def timeline():
    title = "Timeline"
    return template('pages/pages-timeline',title=title)     

@route('/pages/faqs')
def faqs():
    title = "FAQs"
    return template('pages/pages-faqs',title=title)   

@route('/pages/pricing')
def pricing():
    title = "Pricing"
    return template('pages/pages-pricing',title=title)      

@route('/pages/gallery')
def gallery():
    title = "Gallery"
    return template('pages/pages-gallery',title=title)    

@route('/pages/maintenance')
def maintenance():
    title = "Maintenance"
    return template('pages/pages-maintenance',title=title)    

@route('/pages/comingsoon')
def comingsoon():
    title = "Coming Soon"
    return template('pages/pages-comingsoon',title=title)    

@route('/pages/sitemap')
def sitemap():
    title = "Sitemap"
    return template('pages/pages-sitemap',title=title)    

@route('/pages/search_results')
def search_results():
    title = "Search Results"
    return template('pages/pages-search-results',title=title)  

@route('/pages/privacy_policy')
def privacy_policy():
    title = "Privacy Policy"
    return template('pages/pages-privacy-policy',title=title)  

@route('/pages/term_conditions')
def term_conditions():
    title = "Term Conditions"
    return template('pages/pages-term-conditions',title=title)       

@route('/landing')
def landing():
    title = "Landing"
    return template('pages/pages-landing',title=title)      

@route('/nft-landing')
def nft_landing():
    title = "NFT Landing"
    return template('pages/pages-nft-landing',title=title)    

@route('/job-landing')
def job_landing():
    title = "Job Landing"
    return template('pages/pages-job-landing',title=title)      

#Authentication Pages
@route('/pages/auth-signin-basic')
def auth_signin_basic():
    title = "Signin Basic"
    return template('pages/authentication/auth-signin-basic',title=title)    

@route('/pages/auth-signin-cover')
def auth_signin_cover():
    title = "Signin Cover"
    return template('pages/authentication/auth-signin-cover',title=title) 

@route('/pages/auth-signup-basic')
def auth_signup_basic():
    title = "SignUp Basic"
    return template('pages/authentication/auth-signup-basic',title=title)     

@route('/pages/auth-signup-cover')
def auth_signup_cover():
    title = "SignUp Cover"
    return template('pages/authentication/auth-signup-cover',title=title)   

@route('/pages/auth-pass-reset-basic')
def auth_pass_reset_basic():
    title = "Reset Password"
    return template('pages/authentication/auth-pass-reset-basic',title=title)      

@route('/pages/auth-pass-reset-cover')
def auth_pass_reset_cover():
    title = "Reset Password"
    return template('pages/authentication/auth-pass-reset-cover',title=title)  
    
@route('/pages/auth-pass-change-basic')
def auth_pass_change_basic():
    title = "Create New Password"
    return template('pages/authentication/auth-pass-change-basic',title=title)    

@route('/pages/auth-pass-change-cover')
def auth_pass_change_cover():
    title = "Create New Password"
    return template('pages/authentication/auth-pass-change-cover',title=title)   

@route('/pages/auth-lockscreen-basic')
def auth_lockscreen_basic():
    title = "Lock Screen"
    return template('pages/authentication/auth-lockscreen-basic',title=title)     

@route('/pages/auth-lockscreen-cover')
def auth_lockscreen_cover():
    title = "Lock Screen"
    return template('pages/authentication/auth-lockscreen-cover',title=title)    

@route('/pages/auth-logout-basic')
def auth_logout_basic():
    title = "Lock Out"
    return template('pages/authentication/auth-logout-basic',title=title)  

@route('/pages/auth-logout-cover')
def auth_logout_cover():
    title = "Log Out"
    return template('pages/authentication/auth-logout-cover',title=title)      

@route('/pages/auth-success-msg-basic')
def auth_success_msg_basic():
    title = "Success Message"
    return template('pages/authentication/auth-success-msg-basic',title=title) 

@route('/pages/auth-success-msg-cover')
def auth_success_msg_cover():
    title = "Success Message"
    return template('pages/authentication/auth-success-msg-cover',title=title)     

@route('/pages/auth-twostep-basic')
def auth_twostep_basic():
    title = "Two Step Verification"
    return template('pages/authentication/auth-twostep-basic',title=title) 

@route('/pages/auth-twostep-cover')
def auth_twostep_cover():
    title = "Two Step Verification"
    return template('pages/authentication/auth-twostep-cover',title=title)     

@route('/pages/auth-404-basic')
def auth_404_basic():
    title = "404 Error Basic"
    return template('pages/authentication/auth-404-basic',title=title)       

@route('/pages/auth-404-cover')
def auth_404_cover():
    title = "404 Error Cover"
    return template('pages/authentication/auth-404-cover',title=title)    

@route('/pages/auth-404-alt')
def auth_404_alt():
    title = "404 Error alt"
    return template('pages/authentication/auth-404-alt',title=title)     

@route('/pages/auth-500')
def auth_500():
    title = "500 Error"
    return template('pages/authentication/auth-500',title=title)    

@route('/pages/auth-offline')
def auth_offline():
    title = "Offline Page"
    return template('pages/authentication/auth-offline',title=title)       