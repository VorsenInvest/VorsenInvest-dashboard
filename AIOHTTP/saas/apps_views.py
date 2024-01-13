#Calendar Page
import aiohttp_jinja2

#calendar page
@aiohttp_jinja2.template('apps/apps-calendar.html')
async def calendar(request):
    pass

@aiohttp_jinja2.template('apps/apps-calendar-month-grid.html')
async def calendar_month_grid(request):
    pass

#Chat page
@aiohttp_jinja2.template('apps/apps-chat.html')
async def chat(request):
    pass

#File Manager page
@aiohttp_jinja2.template('apps/apps-file-manager.html')
async def filemanager(request):
    pass

#Todo page
@aiohttp_jinja2.template('apps/apps-todo.html')
async def todo(request):
    pass

#Todo page
@aiohttp_jinja2.template('apps/apps-api-key.html')
async def apikey(request):
    pass

#Email pages
@aiohttp_jinja2.template('apps/email/apps-mailbox.html')
async def mailbox(request):
    pass

@aiohttp_jinja2.template('apps/email/apps-email-basic.html')
async def basicaction(request):
    pass

@aiohttp_jinja2.template('apps/email/apps-email-ecommerce.html')
async def invoiceaction(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-products.html')
async def ecommerce_products(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-products-details.html')
async def ecommerce_products_details(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-add-product.html')
async def ecommerce_add_product(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-orders.html')
async def ecommerce_orders(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-orders-details.html')
async def ecommerce_orders_details(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-customers.html')
async def ecommerce_customers(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-cart.html')
async def ecommerce_cart(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-checkout.html')
async def ecommerce_checkout(request):
    pass

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-sellers.html')
async def ecommerce_sellers(request):
    pass  

@aiohttp_jinja2.template('apps/ecommerce/apps-ecommerce-sellers-details.html')
async def ecommerce_sellers_details(request):
    pass  

#Projects Pages
@aiohttp_jinja2.template('apps/projects/apps-projects-list.html')
async def projects_list(request):
    pass 

@aiohttp_jinja2.template('apps/projects/apps-projects-overview.html')
async def projects_overview(request):
    pass 

@aiohttp_jinja2.template('apps/projects/apps-projects-create.html')
async def projects_create(request):
    pass 

#Tasks Pages
@aiohttp_jinja2.template('apps/tasks/apps-tasks-kanban.html')
async def tasks_kanban(request):
    pass 

@aiohttp_jinja2.template('apps/tasks/apps-tasks-list-view.html')
async def tasks_list_view(request):
    pass 

@aiohttp_jinja2.template('apps/tasks/apps-tasks-details.html')
async def tasks_details(request):
    pass 

#CRM pages
@aiohttp_jinja2.template('apps/crm/apps-crm-contacts.html')
async def crm_contacts(request):
    pass 

#CRM pages
@aiohttp_jinja2.template('apps/crm/apps-crm-companies.html')
async def crm_companies(request):
    pass 

@aiohttp_jinja2.template('apps/crm/apps-crm-deals.html')
async def crm_deals(request):
    pass 

@aiohttp_jinja2.template('apps/crm/apps-crm-leads.html')
async def crm_leads(request):
    pass 

#Crypto Pages
@aiohttp_jinja2.template('apps/crypto/apps-crypto-transactions.html')
async def crypto_transactions(request):
    pass 

@aiohttp_jinja2.template('apps/crypto/apps-crypto-buy-sell.html')
async def crypto_buy_sell(request):
    pass 

@aiohttp_jinja2.template('apps/crypto/apps-crypto-orders.html')
async def crypto_orders(request):
    pass 

@aiohttp_jinja2.template('apps/crypto/apps-crypto-wallet.html')
async def crypto_wallet(request):
    pass 

@aiohttp_jinja2.template('apps/crypto/apps-crypto-ico.html')
async def crypto_ico(request):
    pass 

@aiohttp_jinja2.template('apps/crypto/apps-crypto-kyc.html')
async def crypto_kyc(request):
    pass 

#Invoice pages
@aiohttp_jinja2.template('apps/invoices/apps-invoices-list.html')
async def invoices_list(request):
    pass 

@aiohttp_jinja2.template('apps/invoices/apps-invoices-details.html')
async def invoices_details(request):
    pass 

@aiohttp_jinja2.template('apps/invoices/apps-invoices-create.html')
async def invoices_create(request):
    pass 

#Support Tickets
@aiohttp_jinja2.template('apps/support-tickets/apps-tickets-list.html')
async def tickets_list(request):
    pass 

@aiohttp_jinja2.template('apps/support-tickets/apps-tickets-details.html')
async def tickets_details(request):
    pass 

#NFT Pages
@aiohttp_jinja2.template('apps/nft/apps-nft-marketplace.html')
async def nft_marketplace(request):
    pass 

@aiohttp_jinja2.template('apps/nft/apps-nft-explore.html')
async def nft_explore(request):
    pass

@aiohttp_jinja2.template('apps/nft/apps-nft-auction.html')
async def nft_auction(request):
    pass

@aiohttp_jinja2.template('apps/nft/apps-nft-item-details.html')
async def nft_item_details(request):
    pass

@aiohttp_jinja2.template('apps/nft/apps-nft-collections.html')
async def nft_collections(request):
    pass

@aiohttp_jinja2.template('apps/nft/apps-nft-creators.html')
async def nft_creators(request):
    pass

@aiohttp_jinja2.template('apps/nft/apps-nft-ranking.html')
async def nft_ranking(request):
    pass

@aiohttp_jinja2.template('apps/nft/apps-nft-wallet.html')
async def nft_wallet(request):
    pass

@aiohttp_jinja2.template('apps/nft/apps-nft-create.html')
async def nft_create(request):
    pass

#Jobs Pages
@aiohttp_jinja2.template('apps/job/apps-job-statistics.html')
async def job_statistics(request):
    pass    

@aiohttp_jinja2.template('apps/job/apps-job-lists.html')
async def job_lists(request):
    pass        

@aiohttp_jinja2.template('apps/job/apps-job-grid-lists.html')
async def job_grid_lists(request):
    pass      

@aiohttp_jinja2.template('apps/job/apps-job-overview.html')
async def job_overview(request):
    pass      

@aiohttp_jinja2.template('apps/job/apps-job-candidate-lists.html')
async def job_candidate_lists(request):
    pass      

@aiohttp_jinja2.template('apps/job/apps-job-candidate-grid.html')
async def job_candidate_grid(request):
    pass        

@aiohttp_jinja2.template('apps/job/apps-job-application.html')
async def job_application(request):
    pass       

@aiohttp_jinja2.template('apps/job/apps-job-new.html')
async def job_new(request):
    pass         

@aiohttp_jinja2.template('apps/job/apps-job-companies-lists.html')
async def job_companies_lists(request):
    pass     

@aiohttp_jinja2.template('apps/job/apps-job-categories.html')
async def job_categories(request):
    pass    