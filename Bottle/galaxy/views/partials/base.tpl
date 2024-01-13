
<html lang="en" data-layout="vertical" data-topbar="light" data-sidebar="dark" data-sidebar-size="lg" data-sidebar-image="none" data-bs-theme="dark" data-body-image="img-1" data-preloader="disable">

    <head>
    
        <meta charset="utf-8" />
        <title>{{title}} | Velzon - Admin & Dashboard Template</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta content="Premium Multipurpose Admin & Dashboard Template" name="description" />
        <meta content="Themesbrand" name="author" />
        <!-- App favicon -->
        <link rel="shortcut icon" href="/static/images/favicon.ico">
    
    
        %extra_css()
    
        <!-- Layout config Js -->
        <script src="/static/js/layout.js"></script>
        <!-- Bootstrap Css -->
        <link href="/static/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
        <!-- Icons Css -->
        <link href="/static/css/icons.min.css" rel="stylesheet" type="text/css" />
        <!-- App Css-->
        <link href="/static/css/app.min.css" rel="stylesheet" type="text/css" />
        <!-- custom Css-->
        <link href="/static/css/custom.min.css" rel="stylesheet" type="text/css" />
        
    </head>
    
    <body>
        <!-- Begin page -->
        <div id="layout-wrapper">
            
        % include('partials/topbar')         
           
        % include('partials/sidebar')

        <div class="main-content">

            <div class="page-content">
                <div class="container-fluid">
           
        %content()

        % include('partials/footer')
                      
        </div>
        <!-- END layout-wrapper -->

       %extra_content()
        
        
        % include('partials/customizer')
        
        
        <!-- JAVASCRIPT -->
        <script src="/static/libs/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
        <script src="/static/libs/simplebar/dist/simplebar.min.js"></script>
        <script src="/static/libs/node-waves/dist/waves.min.js"></script>
        <script src="/static/libs/feather-icons/dist/feather.min.js"></script>
        <script src="/static/js/pages/plugins/lord-icon-2.1.0.js"></script>
        <script src="/static/js/plugins.js"></script>
        
        %extra_js()
                
        <!-- App js -->
        <script src="/static/js/app.js"></script>
        
    </body>
    
    </html>