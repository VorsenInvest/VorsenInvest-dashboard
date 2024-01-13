from bottle import route, run, template

@route('/components/base-ui/ui-alerts')
def base_ui_alerts():
    title = "Alerts"
    return template('components/base-ui/ui-alert',title=title)

@route('/components/base-ui/ui-badges')
def base_ui_badges():
    title = "Badges"
    return template('components/base-ui/ui-badges',title=title)    

@route('/components/base-ui/ui-buttons')
def base_ui_buttons():
    title = "Buttons"
    return template('components/base-ui/ui-buttons',title=title)    

@route('/components/base-ui/ui-colors')
def base_ui_colors():
    title = "Colors"
    return template('components/base-ui/ui-colors',title=title)    

@route('/components/base-ui/ui-cards')
def base_ui_cards():
    title = "Cards"
    return template('components/base-ui/ui-cards',title=title)    

@route('/components/base-ui/ui-carousel')
def base_ui_carousel():
    title = "Carousel"
    return template('components/base-ui/ui-carousel',title=title)    

@route('/components/base-ui/ui-dropdowns')
def base_ui_dropdowns():
    title = "Dropdowns"
    return template('components/base-ui/ui-dropdowns',title=title)    

@route('/components/base-ui/ui-grid')
def base_ui_grid():
    title = "Grid"
    return template('components/base-ui/ui-grid',title=title)

@route('/components/base-ui/ui-images')
def base_ui_images():
    title = "Images"
    return template('components/base-ui/ui-images',title=title)

@route('/components/base-ui/ui-tabs')
def base_ui_tabs():
    title = "Tabs"
    return template('components/base-ui/ui-tabs',title=title)  

@route('/components/base-ui/ui-accordians')
def base_ui_accordians():
    title = "Accordians"
    return template('components/base-ui/ui-accordians',title=title)       

@route('/components/base-ui/ui-modals')
def base_ui_modals():
    title = "Modals"
    return template('components/base-ui/ui-modals',title=title)    

@route('/components/base-ui/ui-offcanvas')
def base_ui_offcanvas():
    title = "Offcanvas"
    return template('components/base-ui/ui-offcanvas',title=title)    

@route('/components/base-ui/ui-placeholders')
def base_ui_placeholders():
    title = "Placeholders"
    return template('components/base-ui/ui-placeholders',title=title)     

@route('/components/base-ui/ui-progress')
def base_ui_progress():
    title = "Progress"
    return template('components/base-ui/ui-progress',title=title)     

@route('/components/base-ui/ui-notifications')
def base_ui_notifications():
    title = "Notifications"
    return template('components/base-ui/ui-notifications',title=title)    

@route('/components/base-ui/ui-media')
def base_ui_media():
    title = "Media Object"
    return template('components/base-ui/ui-media',title=title)

@route('/components/base-ui/ui-embed-video')
def base_ui_embed_video():
    title = "Embed Video"
    return template('components/base-ui/ui-embed-video',title=title)    

@route('/components/base-ui/ui-typography')
def base_ui_typography():
    title = "Typography"
    return template('components/base-ui/ui-typography',title=title)    

@route('/components/base-ui/ui-lists')
def base_ui_lists():
    title = "Lists"
    return template('components/base-ui/ui-lists',title=title)    

@route('/components/base-ui/ui-general')
def base_ui_general():
    title = "General"
    return template('components/base-ui/ui-general',title=title)    

@route('/components/base-ui/ui-ribbons')
def base_ui_ribbons():
    title = "Ribbons"
    return template('components/base-ui/ui-ribbons',title=title)     

@route('/components/base-ui/ui-utilities')
def base_ui_utilities():
    title = "Utilities"
    return template('components/base-ui/ui-utilities',title=title)      

#Advance UI Pages    
@route('/components/advance-ui/ui-sweetalerts')
def base_ui_sweetalerts():
    title = "Sweet Alerts"
    return template('components/advance-ui/ui-sweetalerts',title=title)

@route('/components/advance-ui/ui-nestable')
def base_ui_nestable():
    title = "Nestable List"
    return template('components/advance-ui/ui-nestable',title=title)    

@route('/components/advance-ui/ui-scrollbar')
def base_ui_scrollbar():
    title = "Scrollbar"
    return template('components/advance-ui/ui-scrollbar',title=title)      

@route('/components/advance-ui/ui-animation')
def base_ui_animation():
    title = "Animation"
    return template('components/advance-ui/ui-animation',title=title)    

@route('/components/advance-ui/ui-tour')
def base_ui_tour():
    title = "Tour"
    return template('components/advance-ui/ui-tour',title=title)   

@route('/components/advance-ui/ui-swiper')
def base_ui_swiper():
    title = "Swiper Slider"
    return template('components/advance-ui/ui-swiper',title=title)     

@route('/components/advance-ui/ui-ratings')
def base_ui_ratings():
    title = "Ratings"
    return template('components/advance-ui/ui-ratings',title=title)     

@route('/components/advance-ui/ui-highlight')
def base_ui_highlight():
    title = "Highlight"
    return template('components/advance-ui/ui-highlight',title=title)   

@route('/components/advance-ui/ui-scrollspy')
def base_ui_scrollspy():
    title = "scrollspy"
    return template('components/advance-ui/ui-scrollspy',title=title)      

#Widgets
@route('/widgets')
def widgets():
    title = "Widgets"
    return template('components/widgets/widgets',title=title)     

#Forms pages
@route('/components/forms/forms-elements')
def forms_elements():
    title = "Basic Elements"
    return template('components/forms/forms-elements',title=title)

@route('/components/forms/forms-select')
def forms_select():
    title = "Forms Select"
    return template('components/forms/forms-select',title=title)   

@route('/components/forms/forms-checkboxs-radios')
def forms_checkboxs_radios():
    title = "Checkboxs & Radios"
    return template('components/forms/forms-checkboxs-radios',title=title)    

@route('/components/forms/forms-pickers')
def forms_pickers():
    title = "Pickers"
    return template('components/forms/forms-pickers',title=title)        

@route('/components/forms/forms-masks')
def forms_masks():
    title = "Input Masks"
    return template('components/forms/forms-masks',title=title)

@route('/components/forms/forms-advanced')
def forms_advanced():
    title = "Forms Advanced"
    return template('components/forms/forms-advanced',title=title)    

@route('/components/forms/forms-range-sliders')
def forms_range_sliders():
    title = "Range Sliders"
    return template('components/forms/forms-range-sliders',title=title)     

@route('/components/forms/forms-validation')
def forms_validation():
    title = "Forms Validation"
    return template('components/forms/forms-validation',title=title)    

@route('/components/forms/forms-wizard')
def forms_wizard():
    title = "Wizard"
    return template('components/forms/forms-wizard',title=title)     

@route('/components/forms/forms-editors')
def forms_editors():
    title = "Editors"
    return template('components/forms/forms-editors',title=title)    

@route('/components/forms/forms-file-uploads')
def forms_file_uploads():
    title = "File Uploads"
    return template('components/forms/forms-file-uploads',title=title)    

@route('/components/forms/forms-layouts')
def forms_layouts():
    title = "Forms Layouts"
    return template('components/forms/forms-layouts',title=title)    

@route('/components/forms/forms-select2')
def forms_select2():
    title = "Select2"
    return template('components/forms/forms-select2',title=title) 

#Tables Pages    
@route('/components/tables/tables-basic')
def tables_basic():
    title = "Basic Tables"
    return template('components/tables/tables-basic',title=title)      

@route('/components/tables/tables-gridjs')
def tables_gridjs():
    title = "Grid JS"
    return template('components/tables/tables-gridjs',title=title)    

@route('/components/tables/tables-listjs')
def tables_listjs():
    title = "Grid JS"
    return template('components/tables/tables-listjs',title=title)     

@route('/components/tables/tables-datatables')
def tables_datatables():
    title = "Datatables"
    return template('components/tables/tables-datatables',title=title)    

#Charts Pages    
@route('/components/charts/charts-apex-line')
def charts_apex_line():
    title = "Apex Line Charts"
    return template('components/charts/apexcharts/charts-apex-line',title=title)

@route('/components/charts/charts-apex-area')
def charts_apex_area():
    title = "Apex Area Charts"
    return template('components/charts/apexcharts/charts-apex-area',title=title)  

@route('/components/charts/charts-apex-column')
def charts_apex_column():
    title = "Apex Column Charts"
    return template('components/charts/apexcharts/charts-apex-column',title=title)      

@route('/components/charts/charts-apex-bar')
def charts_apex_bar():
    title = "Apex Bar Charts"
    return template('components/charts/apexcharts/charts-apex-bar',title=title)     

@route('/components/charts/charts-apex-mixed')
def charts_apex_mixed():
    title = "Apex Mixed Charts"
    return template('components/charts/apexcharts/charts-apex-mixed',title=title)   

@route('/components/charts/charts-apex-timeline')
def charts_apex_timeline():
    title = "Apex Timeline Charts"
    return template('components/charts/apexcharts/charts-apex-timeline',title=title)    

@route('/components/charts/charts-apex-candlestick')
def charts_apex_candlestick():
    title = "Apex Candlestick Charts"
    return template('components/charts/apexcharts/charts-apex-candlestick',title=title)    

@route('/components/charts/charts-apex-boxplot')
def charts_apex_boxplot():
    title = "Apex Boxplot Charts"
    return template('components/charts/apexcharts/charts-apex-boxplot',title=title)   

@route('/components/charts/charts-apex-bubble')
def charts_apex_bubble():
    title = "Apex Bubble Charts"
    return template('components/charts/apexcharts/charts-apex-bubble',title=title)     

@route('/components/charts/charts-apex-scatter')
def charts_apex_scatter():
    title = "Apex Scatter Charts"
    return template('components/charts/apexcharts/charts-apex-scatter',title=title)    

@route('/components/charts/charts-apex-heatmap')
def charts_apex_heatmap():
    title = "Apex Heatmap Charts"
    return template('components/charts/apexcharts/charts-apex-heatmap',title=title)     

@route('/components/charts/charts-apex-treemap')
def charts_apex_treemap():
    title = "Apex Treemap Charts"
    return template('components/charts/apexcharts/charts-apex-treemap',title=title)    

@route('/components/charts/charts-apex-pie')
def charts_apex_pie():
    title = "Apex Pie Charts"
    return template('components/charts/apexcharts/charts-apex-pie',title=title)    

@route('/components/charts/charts-apex-radialbar')
def charts_apex_radialbar():
    title = "Apex Radialbar Charts"
    return template('components/charts/apexcharts/charts-apex-radialbar',title=title)    

@route('/components/charts/charts-apex-radar')
def charts_apex_radar():
    title = "Apex Radar Charts"
    return template('components/charts/apexcharts/charts-apex-radar',title=title)    

@route('/components/charts/charts-apex-polar')
def charts_apex_polar():
    title = "Apex Polar Charts"
    return template('components/charts/apexcharts/charts-apex-polar',title=title)   

@route('/components/charts/chartsjs')
def charts_chartsjs():
    title = "Chartjs"
    return template('components/charts/charts-chartjs',title=title) 

@route('/components/charts/echarts')
def charts_echarts():
    title = "Echarts"
    return template('components/charts/charts-echarts',title=title)      

#Icons Pages      
@route('/components/icons/remix')
def icons_remix():
    title = "Remix Icons"
    return template('components/icons/icons-remix',title=title)
  
@route('/components/icons/boxicons')
def icons_boxicons():
    title = "Boxicons"
    return template('components/icons/icons-boxicons',title=title)  

@route('/components/icons/materialdesign')
def icons_materialdesign():
    title = "Material Design"
    return template('components/icons/icons-materialdesign',title=title)    

@route('/components/icons/lineawesome')
def icons_lineawesome():
    title = "Line Awesome Icons"
    return template('components/icons/icons-lineawesome',title=title)     

@route('/components/icons/feather')
def icons_feather():
    title = "Feather Icons"
    return template('components/icons/icons-feather',title=title)    

@route('/components/icons/crypto')
def icons_crypto():
    title = "Crypto Icons"
    return template('components/icons/icons-crypto',title=title)     

#Maps Pages    
@route('/components/maps/google')
def maps_google():
    title = "Google Maps"
    return template('components/maps/maps-google',title=title)

@route('/components/maps/vector')
def maps_vector():
    title = "Vector Maps"
    return template('components/maps/maps-vector',title=title)    

@route('/components/maps/leaflet')
def maps_leaflet():
    title = "Leaflet Maps"
    return template('components/maps/maps-leaflet',title=title)    