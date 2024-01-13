<?= $this->element('main') ?>

<head>

    <?= $this->element('title-meta', array('title' => 'Chartjs')) ?>

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

                    <?= $this->element('page-title', array('pagetitle' => 'Charts', 'title' => 'Chartjs')) ?>

                    <div class="row">
                        <div class="col-xl-6">
                            <div class="card">
                                <div class="card-header">
                                    <h4 class="card-title mb-0">Line Chart</h4>
                                </div>
                                <div class="card-body">
                                    <canvas id="lineChart" class="chartjs-chart" data-colors='["--vz-primary-rgb, 0.2", "--vz-primary", "--vz-info-rgb, 0.2", "--vz-info"]'></canvas>
                                </div>
                            </div>
                        </div> <!-- end col -->

                        <div class="col-xl-6">
                            <div class="card">
                                <div class="card-header">
                                    <h4 class="card-title mb-0">Bar Chart</h4>
                                </div>
                                <div class="card-body">
                                    <canvas id="bar" class="chartjs-chart" data-colors='["--vz-primary"]'></canvas>

                                </div>
                            </div>
                        </div> <!-- end col -->
                    </div> <!-- end row -->

                    <div class="row">
                        <div class="col-xl-6">
                            <div class="card">
                                <div class="card-header">
                                    <h4 class="card-title mb-0">Pie Chart</h4>
                                </div>
                                <div class="card-body">
                                    <canvas id="pieChart" class="chartjs-chart" data-colors='["--vz-primary", "--vz-light"]'></canvas>
                                </div>
                            </div>
                        </div> <!-- end col -->

                        <div class="col-xl-6">
                            <div class="card">
                                <div class="card-header">
                                    <h4 class="card-title mb-0">Donut Chart</h4>
                                </div>
                                <div class="card-body">
                                    <canvas id="doughnut" class="chartjs-chart" data-colors='["--vz-primary", "--vz-light"]'></canvas>
                                </div>
                            </div>
                        </div> <!-- end col -->
                    </div> <!-- end row -->

                    <div class="row">
                        <div class="col-xl-6">
                            <div class="card">
                                <div class="card-header">
                                    <h4 class="card-title mb-0">Polar Chart</h4>
                                </div>
                                <div class="card-body">
                                    <canvas id="polarArea" class="chartjs-chart" data-colors='["--vz-info", "--vz-success", "--vz-light", "--vz-primary"]'> </canvas>
                                </div>
                            </div>
                        </div> <!-- end col -->

                        <div class="col-xl-6">
                            <div class="card">
                                <div class="card-header">
                                    <h4 class="card-title mb-0">Radar Chart</h4>
                                </div>
                                <div class="card-body">
                                    <canvas id="radar" class="chartjs-chart" data-colors='["--vz-info-rgb, 0.2", "--vz-info", "--vz-primary-rgb, 0.2", "--vz-primary"]'></canvas>
                                </div>
                            </div>
                        </div> <!-- end col -->
                    </div> <!-- end row -->

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

    <!-- Chart JS -->
    <script src="/libs/chart.js/chart.umd.js"></script>

    <!-- chartjs init -->
    <script src="/js/pages/chartjs.init.js"></script>

    <!-- App js -->
    <script src="/js/app.js"></script>
</body>

</html>
