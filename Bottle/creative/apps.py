from bottle import route, run, template

#Calendar page
@route('/calendar')
def calendar():
    title = "Calendar"
    return template('apps/calendar/calendar',title=title)

@route('/calendar')
def month_grid_calendar():
    title = "Month Grid"
    return template('apps/calendar/apps-calendar-month-grid',title=title) 

#Chat Page
@route('/chat')
def chat():
    title = "Chat"
    return template('apps/chat/chat',title=title)    

#Email Pages   

@route('/apps-mailbox')
def mailbox():
    title = "Mailbox"
    return template('apps/email/apps-mailbox',title=title)     

@route('/apps-basicaction')
def basicaction():
    title = "Basic Action"
    return template('apps/email/apps-basicaction',title=title)     

@route('/apps-invoiceaction')
def invoiceaction():
    title = "Invoice Action"
    return template('apps/email/apps-invoiceaction',title=title)    

#Ecommerce pages    
@route('/ecommerce/products')
def ecommerce_products():
    title = "Products"
    return template('apps/ecommerce/apps-ecommerce-products',title=title) 

@route('/ecommerce/products-details')
def ecommerce_products_details():
    title = "Products Details"
    return template('apps/ecommerce/apps-ecommerce-products-details',title=title)     

@route('/ecommerce/add-product')
def ecommerce_add_product():
    title = "Add Product"
    return template('apps/ecommerce/apps-ecommerce-add-product',title=title)     

@route('/ecommerce/orders')
def ecommerce_orders():
    title = "Orders"
    return template('apps/ecommerce/apps-ecommerce-orders',title=title)    

@route('/ecommerce/orders-details')
def ecommerce_orders_details():
    title = "Orders Details"
    return template('apps/ecommerce/apps-ecommerce-orders-details',title=title)    

@route('/ecommerce/customers')
def ecommerce_customers():
    title = "Customers"
    return template('apps/ecommerce/apps-ecommerce-customers',title=title)   

@route('/ecommerce/cart')
def ecommerce_cart():
    title = "Cart"
    return template('apps/ecommerce/apps-ecommerce-cart',title=title)   

@route('/ecommerce/checkout')
def ecommerce_checkout():
    title = "Checkout"
    return template('apps/ecommerce/apps-ecommerce-checkout',title=title)         

@route('/ecommerce/sellers')
def ecommerce_sellers():
    title = "Sellers"
    return template('apps/ecommerce/apps-ecommerce-sellers',title=title)

@route('/ecommerce/sellers-details')
def ecommerce_sellers_details():
    title = "Sellers Details"
    return template('apps/ecommerce/apps-ecommerce-sellers-details',title=title)    

#Projects pages
@route('/projects/list')
def projects_list():
    title = "Projects List"
    return template('apps/projects/apps-projects-list',title=title)

@route('/projects/overview')
def projects_overview():
    title = "Projects Overview"
    return template('apps/projects/apps-projects-overview',title=title)

@route('/projects/create')
def projects_create():
    title = "Projects Create"
    return template('apps/projects/apps-projects-create',title=title)    

#Task pages    
@route('/tasks/kanban')
def tasks_kanban():
    title = "Kanban Board"
    return template('apps/tasks/apps-tasks-kanban',title=title) 

@route('/tasks/list-view')
def tasks_list_view():
    title = "Tasks List"
    return template('apps/tasks/apps-tasks-list-view',title=title)     

@route('/tasks/details')
def tasks_details():
    title = "Tasks Details"
    return template('apps/tasks/apps-tasks-details',title=title)  

#CRM Pages    
@route('/crm/contacts')
def crm_contacts():
    title = "Contacts"
    return template('apps/crm/apps-crm-contacts',title=title) 

@route('/crm/companies')
def crm_companies():
    title = "Companies"
    return template('apps/crm/apps-crm-companies',title=title)    

@route('/crm/deals')
def crm_deals():
    title = "Deals"
    return template('apps/crm/apps-crm-deals',title=title)    

@route('/crm/leads')
def crm_leads():
    title = "Leads"
    return template('apps/crm/apps-crm-leads',title=title)   

#Crypto Pages  
@route('/crypto/transactions')
def crypto_transactions():
    title = "Transactions"
    return template('apps/crypto/apps-crypto-transactions',title=title) 

@route('/crypto/buy-sell')
def crypto_buy_sell():
    title = "Buy & Sell"
    return template('apps/crypto/apps-crypto-buy-sell',title=title)       

@route('/crypto/orders')
def crypto_orders():
    title = "Orders"
    return template('apps/crypto/apps-crypto-orders',title=title)     

@route('/crypto/wallet')
def crypto_wallet():
    title = "Wallet"
    return template('apps/crypto/apps-crypto-wallet',title=title)    

@route('/crypto/ico')
def crypto_ico():
    title = "ICO List"
    return template('apps/crypto/apps-crypto-ico',title=title)  

@route('/crypto/kyc')
def crypto_kyc():
    title = "KYC Application"
    return template('apps/crypto/apps-crypto-kyc',title=title)   

#Invoices Pages        
@route('/invoices/list')
def invoices_list():
    title = "Invoices List"
    return template('apps/invoices/apps-invoices-list',title=title)

@route('/invoices/details')
def invoices_details():
    title = "Invoices Details"
    return template('apps/invoices/apps-invoices-details',title=title)    

@route('/invoices/create')
def invoices_create():
    title = "Create Invoices"
    return template('apps/invoices/apps-invoices-create',title=title)  

#Supports Tickets Pages      
@route('/support-tickets/list')
def tickets_list():
    title = "Tickets List"
    return template('apps/support-tickets/apps-tickets-list',title=title) 

@route('/support-tickets/details')
def tickets_details():
    title = "Tickets Details"
    return template('apps/support-tickets/apps-tickets-details',title=title) 

#NFT Marketplace 
@route('/nft/marketplace')
def nft_marketplace():
    title = "Marketplace"
    return template('apps/nft/apps-nft-marketplace',title=title)   

@route('/nft/explore')
def nft_explore():
    title = "Explore Now"
    return template('apps/nft/apps-nft-explore',title=title)

@route('/nft/auction')
def nft_auction():
    title = "Live Auction"
    return template('apps/nft/apps-nft-auction',title=title)

@route('/nft/item-details')
def nft_item_details():
    title = "Item Details"
    return template('apps/nft/apps-nft-item-details',title=title)    

@route('/nft/collections')
def nft_collections():
    title = "Collections"
    return template('apps/nft/apps-nft-collections',title=title)    

@route('/nft/creators')
def nft_creators():
    title = "Creators"
    return template('apps/nft/apps-nft-creators',title=title)     

@route('/nft/ranking')
def nft_ranking():
    title = "Ranking"
    return template('apps/nft/apps-nft-ranking',title=title)     

@route('/nft/wallet')
def nft_wallet():
    title = "Wallet Connect"
    return template('apps/nft/apps-nft-wallet',title=title)    

@route('/nft/create')
def nft_create():
    title = "Create NFT"
    return template('apps/nft/apps-nft-create',title=title) 

#Jobs pages 
@route('/job/statistics')
def job_statistics():
    title = "Statistics"
    return template('apps/job/apps-job-statistics',title=title)       

@route('/job/lists')
def job_lists():
    title = "Job Lists"
    return template('apps/job/apps-job-lists',title=title)    

@route('/job/grid-lists')
def job_grid_lists():
    title = "Job Grid Lists"
    return template('apps/job/apps-job-grid-lists',title=title)   
  
@route('/job/job-overview')
def job_overview():
    title = "Job Overview"
    return template('apps/job/apps-job-overview',title=title)   

@route('/job/candidate-lists')
def candidate_lists():
    title = "Candidate Lists View"
    return template('apps/job/apps-job-candidate-lists',title=title) 

@route('/job/candidate-grid')
def candidate_grid():
    title = "Candidate Grid View"
    return template('apps/job/apps-job-candidate-grid',title=title)

@route('/job/application')
def job_application():
    title = "Job Application"
    return template('apps/job/apps-job-application',title=title)     

@route('/job/new')
def job_new():
    title = "New Job"
    return template('apps/job/apps-job-new',title=title)    

@route('/job/companies-lists')
def job_companies_lists():
    title = "Companies List"
    return template('apps/job/apps-job-companies-lists',title=title)    

@route('/job/categories')
def job_categories():
    title = "Job Categories"
    return template('apps/job/apps-job-categories',title=title)    


#File Manager
@route('/filemanager')
def filemanager():
    title = "File Manager"
    return template('apps/filemanager/filemanager',title=title)    

#Todo pages
@route('/todo')
def todo():
    title = "Todo Lists"
    return template('apps/todo/todo',title=title)

#API Key    
@route('/api-key')
def apikey():
    title = "API key"
    return template('apps/apikey/apikey',title=title)
  