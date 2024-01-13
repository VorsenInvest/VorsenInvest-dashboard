<?= $this->element('main') ?>

<head>

    <?= $this->element('title-meta', array('title' => 'Remix Icons')) ?>

    <?= $this->element('head-css') ?>

</head>

<body>

    <!-- Begin page -->
    <div id="layout-wrapper">

        <?= $this->element('menu') ?>

        <!-- ============================================================== -->
        <!-- Start right Content here -->
        <!-- ============================================================== -->
        <div class="main-content">

            <div class="page-content">
                <div class="container-fluid">

                    <?= $this->element('page-title', array('pagetitle' => 'Icons', 'title' => 'Remix')) ?>

                    <div class="row">

                    </div><!-- end row -->

                    <div class="row">
                        <div class="col-12" id="icons"></div> <!-- end col-->
                    </div><!-- end row -->

                </div>
                <!-- container-fluid -->
            </div>
            <!-- End Page-content -->

            <?= $this->element('footer') ?>
        </div>
        <!-- end main content-->

    </div>
    <!-- END layout-wrapper -->



    <?= $this->element('customizer') ?>

    <?= $this->element('vendor-scripts') ?>

    <!-- materialdesign icon js-->
    <script src="/js/pages/remix-icons-listing.js"></script>

    <!-- App js -->
    <script src="/js/app.js"></script>
</body>

</html>
