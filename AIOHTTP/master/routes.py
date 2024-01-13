# aiohttpdemo_polls/routes.py

import pathlib
from views import *

PROJECT_ROOT = pathlib.Path(__file__).parent


def setup_routes(app):
    #dashboard pages
    app.router.add_get('/', index)
    app.router.add_get('/dashboard-analytics', dashboard_analytics)
    app.router.add_get('/dashboard-crm', dashboard_crm)
    app.router.add_get('/dashboard-crypto', dashboard_crypto)
    app.router.add_get('/dashboard-projects', dashboard_projects)
    app.router.add_get('/dashboard-nft', dashboard_nft)
    app.router.add_get('/dashboard-job', dashboard_job)

    #calendar page
    app.router.add_get('/calendar', calendar)
    app.router.add_get('/calendar_month_grid', calendar_month_grid)

    #chat page
    app.router.add_get('/chat', chat)

    #file manager page
    app.router.add_get('/filemanager', filemanager)

    #todo page
    app.router.add_get('/todo', todo)

    #API KEY page
    app.router.add_get('/api-key', apikey)

    #Email pages
    app.router.add_get('/apps-mailbox', mailbox)
    app.router.add_get('/apps-basicaction', basicaction)
    app.router.add_get('/apps-invoiceaction', invoiceaction)

    #Ecommerce Pages
    app.router.add_get('/ecommerce/products', ecommerce_products)
    app.router.add_get('/ecommerce/products-details', ecommerce_products_details)
    app.router.add_get('/ecommerce/add-product', ecommerce_add_product)
    app.router.add_get('/ecommerce/orders', ecommerce_orders)
    app.router.add_get('/ecommerce/orders-details', ecommerce_orders_details)
    app.router.add_get('/ecommerce/customers', ecommerce_customers)
    app.router.add_get('/ecommerce/cart', ecommerce_cart)
    app.router.add_get('/ecommerce/checkout', ecommerce_checkout)
    app.router.add_get('/ecommerce/sellers', ecommerce_sellers)
    app.router.add_get('/ecommerce/sellers-details', ecommerce_sellers_details)

    #Projects pages
    app.router.add_get('/projects/list', projects_list)
    app.router.add_get('/projects/overview', projects_overview)
    app.router.add_get('/projects/create', projects_create)

    #Tasks Pages
    app.router.add_get('/tasks/kanban', tasks_kanban)
    app.router.add_get('/tasks/list-view', tasks_list_view)
    app.router.add_get('/tasks/details', tasks_details)

    #CRM Pages
    app.router.add_get('/crm/contacts', crm_contacts)
    app.router.add_get('/crm/companies', crm_companies)
    app.router.add_get('/crm/deals', crm_deals)
    app.router.add_get('/crm/leads', crm_leads)

    #Crypto pages
    app.router.add_get('/crypto/transactions', crypto_transactions)
    app.router.add_get('/crypto/buy-sell', crypto_buy_sell)
    app.router.add_get('/crypto/orders', crypto_orders)
    app.router.add_get('/crypto/wallet', crypto_wallet)
    app.router.add_get('/crypto/ico', crypto_ico)
    app.router.add_get('/crypto/kyc', crypto_kyc)

    #Invoice pages
    app.router.add_get('/invoices/list', invoices_list)
    app.router.add_get('/invoices/details', invoices_details)
    app.router.add_get('/invoices/create', invoices_create)
   
    #Support Tickets
    app.router.add_get('/support-tickets/list', tickets_list)
    app.router.add_get('/support-tickets/details', tickets_details)

    #NFT MarketPlace
    app.router.add_get('/nft/marketplace', nft_marketplace)
    app.router.add_get('/nft/explore', nft_explore)
    app.router.add_get('/nft/auction', nft_auction)
    app.router.add_get('/nft/item-details', nft_item_details)
    app.router.add_get('/nft/collections', nft_collections)
    app.router.add_get('/nft/creators', nft_creators)
    app.router.add_get('/nft/ranking', nft_ranking)
    app.router.add_get('/nft/wallet', nft_wallet)
    app.router.add_get('/nft/create', nft_create)

    #Job pages
    app.router.add_get('/job/statistics', job_statistics)
    app.router.add_get('/job/lists', job_lists)
    app.router.add_get('/job/grid-lists', job_grid_lists)
    app.router.add_get('/job/overview', job_overview)
    app.router.add_get('/job/candidate-lists', job_candidate_lists)
    app.router.add_get('/job/candidate-grid', job_candidate_grid)
    app.router.add_get('/job/job-application', job_application)
    app.router.add_get('/job/job-new', job_new)
    app.router.add_get('/job/job-companies-lists', job_companies_lists)
    app.router.add_get('/job/job-categories', job_categories)

    #layouts
    app.router.add_get('/layouts/horizontal', layouts_horizontal)
    app.router.add_get('/layouts/detached', layouts_detached)
    app.router.add_get('/layouts/twocolumn', layouts_twocolumn)
    app.router.add_get('/layouts/hovered', layouts_hovered)

    #Pages Pages
    app.router.add_get('/pages/auth-signin-basic', auth_signin_basic)
    app.router.add_get('/pages/auth-signin-cover', auth_signin_cover)
    app.router.add_get('/pages/auth-signup-basic', auth_signup_basic)
    app.router.add_get('/pages/auth-signup-cover', auth_signup_cover)
    app.router.add_get('/pages/auth-pass-reset-basic', auth_pass_reset_basic)
    app.router.add_get('/pages/auth-pass-reset-cover', auth_pass_reset_cover)
    app.router.add_get('/pages/auth-pass-change-basic', auth_pass_change_basic)
    app.router.add_get('/pages/auth-pass-change-cover', auth_pass_change_cover)
    app.router.add_get('/pages/auth-lockscreen-basic', auth_lockscreen_basic)
    app.router.add_get('/pages/auth-lockscreen-cover', auth_lockscreen_cover)
    app.router.add_get('/pages/auth-logout-basic', auth_logout_basic)
    app.router.add_get('/pages/auth-logout-cover', auth_logout_cover)
    app.router.add_get('/pages/auth-success-msg-basic', auth_success_msg_basic)
    app.router.add_get('/pages/auth-success-msg-cover', auth_success_msg_cover)
    app.router.add_get('/pages/auth-twostep-basic', auth_twostep_basic)
    app.router.add_get('/pages/auth-twostep-cover', auth_twostep_cover)
    app.router.add_get('/pages/auth-404-basic', auth_404_basic)
    app.router.add_get('/pages/auth-404-cover', auth_404_cover)
    app.router.add_get('/pages/auth-404-alt', auth_404_alt)
    app.router.add_get('/pages/auth-500', auth_500)
    app.router.add_get('/pages/auth-offline', auth_offline)


    app.router.add_get('/pages/starter', pages_starter)
    app.router.add_get('/pages/profile', pages_profile)
    app.router.add_get('/pages/profile-settings', pages_profile_settings)
    app.router.add_get('/pages/team', pages_team)
    app.router.add_get('/pages/timeline', pages_timeline)
    app.router.add_get('/pages/faqs', pages_faqs)
    app.router.add_get('/pages/pricing', pages_pricing)
    app.router.add_get('/pages/gallery', pages_gallery)
    app.router.add_get('/pages/maintenance', pages_maintenance)
    app.router.add_get('/pages/comingsoon', pages_comingsoon)
    app.router.add_get('/pages/sitemap', pages_sitemap)
    app.router.add_get('/pages/search_results', pages_search_results)
    app.router.add_get('/pages/privacy_policy', pages_privacy_policy)
    app.router.add_get('/pages/term_conditions', pages_term_conditions)

    app.router.add_get('/landing', pages_landing)
    app.router.add_get('/nft-landing', pages_nft_landing)
    app.router.add_get('/job-landing', pages_job_landing)

    #Component pages
    app.router.add_get('/components/base-ui/ui-alerts', base_ui_alerts)
    app.router.add_get('/components/base-ui/ui-badges', base_ui_badges)
    app.router.add_get('/components/base-ui/ui-buttons', base_ui_buttons)
    app.router.add_get('/components/base-ui/ui-colors', base_ui_colors)
    app.router.add_get('/components/base-ui/ui-cards', base_ui_cards)
    app.router.add_get('/components/base-ui/ui-carousel', base_ui_carousel)
    app.router.add_get('/components/base-ui/ui-dropdowns', base_ui_dropdowns)
    app.router.add_get('/components/base-ui/ui-grid', base_ui_grid)
    app.router.add_get('/components/base-ui/ui-images', base_ui_images)
    app.router.add_get('/components/base-ui/ui-links', base_ui_links)
    app.router.add_get('/components/base-ui/ui-tabs', base_ui_tabs)
    app.router.add_get('/components/base-ui/ui-accordian', base_ui_accordian)
    app.router.add_get('/components/base-ui/ui-modals', base_ui_modals)
    app.router.add_get('/components/base-ui/ui-offcanvas', base_ui_offcanvas)
    app.router.add_get('/components/base-ui/ui-placeholders', base_ui_placeholders)
    app.router.add_get('/components/base-ui/ui-progress', base_ui_progress)
    app.router.add_get('/components/base-ui/ui-notifications', base_ui_notifications)
    app.router.add_get('/components/base-ui/ui-media', base_ui_media)
    app.router.add_get('/components/base-ui/ui-embed-video', base_ui_embed_video)
    app.router.add_get('/components/base-ui/ui-typography', base_ui_typography)
    app.router.add_get('/components/base-ui/ui-list', base_ui_list)
    app.router.add_get('/components/base-ui/ui-general', base_ui_general)
    app.router.add_get('/components/base-ui/ui-ribbons', base_ui_ribbons)
    app.router.add_get('/components/base-ui/ui-utilities', base_ui_utilities)

    #Advance UI pages
    app.router.add_get('/components/advance-ui/ui-sweetalerts', advance_ui_sweetalerts)
    app.router.add_get('/components/advance-ui/ui-nestable', advance_ui_nestable)
    app.router.add_get('/components/advance-ui/ui-scrollbar', advance_ui_scrollbar)
    app.router.add_get('/components/advance-ui/ui-animation', advance_ui_animation)
    app.router.add_get('/components/advance-ui/ui-tour', advance_ui_tour)
    app.router.add_get('/components/advance-ui/ui-swiper', advance_ui_swiper)
    app.router.add_get('/components/advance-ui/ui-rating', advance_ui_rating)
    app.router.add_get('/components/advance-ui/ui-highlight', advance_ui_highlight)
    app.router.add_get('/components/advance-ui/ui-scrollspy', advance_ui_scrollspy)

    #Widgets Pages
    app.router.add_get('/widgets', widgets)

    #Forms Pages
    app.router.add_get('/components/forms/forms-elements', forms_elements)
    app.router.add_get('/components/forms/forms-select', forms_select)
    app.router.add_get('/components/forms/forms-checkboxs-radios', forms_checkboxs_radios)
    app.router.add_get('/components/forms/forms-pickers', forms_pickers)
    app.router.add_get('/components/forms/forms-input-masks', forms_input_masks)
    app.router.add_get('/components/forms/forms-advanced', forms_advanced)
    app.router.add_get('/components/forms/forms-range-sliders', forms_range_sliders)
    app.router.add_get('/components/forms/forms-validation', forms_validation)
    app.router.add_get('/components/forms/forms-wizard', forms_wizard)
    app.router.add_get('/components/forms/forms-editors', forms_editors)
    app.router.add_get('/components/forms/forms-file-uploads', forms_file_uploads)
    app.router.add_get('/components/forms/forms-layouts', forms_layouts)
    app.router.add_get('/components/forms/forms-select2', forms_select2)

    #Tables Pages
    app.router.add_get('/components/tables/tables-basic', tables_basic)
    app.router.add_get('/components/tables/tables-gridjs', tables_gridjs)
    app.router.add_get('/components/tables/tables-listjs', tables_listjs)
    app.router.add_get('/components/tables/tables-datatables', tables_datatables)

    #charts pages
    app.router.add_get('/components/charts/charts-apex-line', charts_apex_line)
    app.router.add_get('/components/charts/charts-apex-area', charts_apex_area)
    app.router.add_get('/components/charts/charts-apex-column', charts_apex_column)
    app.router.add_get('/components/charts/charts-apex-funnel', charts_apex_funnel)
    app.router.add_get('/components/charts/charts-apex-bar', charts_apex_bar)
    app.router.add_get('/components/charts/charts-apex-mixed', charts_apex_mixed)
    app.router.add_get('/components/charts/charts-apex-timeline', charts_apex_timeline)
    app.router.add_get('/components/charts/charts-apex-candlestick', charts_apex_candlestick)
    app.router.add_get('/components/charts/charts-apex-boxplot', charts_apex_boxplot)
    app.router.add_get('/components/charts/charts-apex-bubble', charts_apex_bubble)
    app.router.add_get('/components/charts/charts-apex-scatter', charts_apex_scatter)
    app.router.add_get('/components/charts/charts-apex-heatmap', charts_apex_heatmap)
    app.router.add_get('/components/charts/charts-apex-treemap', charts_apex_treemap)
    app.router.add_get('/components/charts/charts-apex-pie', charts_apex_pie)
    app.router.add_get('/components/charts/charts-apex-radialbar', charts_apex_radialbar)
    app.router.add_get('/components/charts/charts-apex-range-area', charts_apex_range_area)
    app.router.add_get('/components/charts/charts-apex-radar', charts_apex_radar)
    app.router.add_get('/components/charts/charts-apex-polar', charts_apex_polar)

    app.router.add_get('/components/charts/chartsjs', charts_chartsjs)
    app.router.add_get('/components/charts/echarts', charts_echarts)

    #Icons Pages
    app.router.add_get('/components/icons/remix', icons_remix)
    app.router.add_get('/components/icons/boxicons', icons_boxicons)
    app.router.add_get('/components/icons/materialdesign', icons_materialdesign)
    app.router.add_get('/components/icons/lineawesome', icons_lineawesome)
    app.router.add_get('/components/icons/feather', icons_feather)
    app.router.add_get('/components/icons/crypto', icons_crypto)

    #Maps Pages
    app.router.add_get('/components/maps/google', maps_google)
    app.router.add_get('/components/maps/vector', maps_vector)
    app.router.add_get('/components/maps/leaflet', maps_leaflet)


    app.router.add_static('/static/', path=PROJECT_ROOT / 'static', name='static')


    