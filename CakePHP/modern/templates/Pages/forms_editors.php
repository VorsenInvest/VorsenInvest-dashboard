<?= $this->element('main') ?>

<head>

    <?= $this->element('title-meta', array('title' => 'Editors')) ?>

    <!-- quill css -->
    <link href="/libs/quill/quill.core.css" rel="stylesheet" type="text/css" />
    <link href="/libs/quill/quill.bubble.css" rel="stylesheet" type="text/css" />
    <link href="/libs/quill/quill.snow.css" rel="stylesheet" type="text/css" />

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

                    <?= $this->element('page-title', array('pagetitle' => 'Forms', 'title' => 'Editors')) ?>

                    <div class="row">
                        <div class="col-lg-12">
                            <div class="card">
                                <div class="card-header align-items-center d-flex">
                                    <h4 class="card-title mb-0">Ckeditor Classic Editor</h4>
                                </div><!-- end card header -->

                                <div class="card-body">
                                    <p class="text-muted">Use <code>ckeditor-classic</code> class to set ckeditor classic editor.</p>
                                    <div class="ckeditor-classic"></div>
                                </div><!-- end card-body -->
                            </div><!-- end card -->
                        </div>
                        <!-- end col -->
                    </div>
                    <!-- end row -->

                    <div class="row mt-2">
                        <div class="col-lg-12">

                            <div class="justify-content-between d-flex align-items-center mb-3">
                                <h5 class="mb-0 pb-1 text-decoration-underline">Quilljs Editor</h5>
                            </div>
                            <div class="card">
                                <div class="card-header">
                                    <h4 class="card-title mb-0">Snow Editor</h4>
                                </div><!-- end card header -->

                                <div class="card-body">
                                    <p class="text-muted">Use <code>snow-editor</code> class to set snow editor.</p>
                                    <div class="snow-editor" style="height: 300px;">
                                        <h3><span class="ql-size-large">Hello World!</span></h3>
                                        <p><br></p>
                                        <h3>This is an simple editable area.</h3>
                                        <p><br></p>
                                        <ul>
                                            <li>
                                                Select a text to reveal the toolbar.
                                            </li>
                                            <li>
                                                Edit rich document on-the-fly, so elastic!
                                            </li>
                                        </ul>
                                        <p><br></p>
                                        <p>
                                            End of simple area
                                        </p>

                                    </div> <!-- end Snow-editor-->
                                </div><!-- end card-body -->
                            </div><!-- end card -->

                            <div class="card">
                                <div class="card-header">
                                    <h4 class="card-title mb-0">Bubble Editor</h4>
                                </div><!-- end card header -->

                                <div class="card-body">
                                    <p class="text-muted">Use <code>bubble-editor</code> class to set bubble editor.</p>
                                    <div class="bubble-editor" style="height: 300px;">
                                        <h3><span class="ql-size-large">Hello World!</span></h3>
                                        <p><br></p>
                                        <h3>This is an simple editable area.</h3>
                                        <p><br></p>
                                        <ul>
                                            <li>
                                                Select a text to reveal the toolbar.
                                            </li>
                                            <li>
                                                Edit rich document on-the-fly, so elastic!
                                            </li>
                                        </ul>
                                        <p><br></p>
                                        <p>
                                            End of simple area
                                        </p>

                                    </div>
                                </div><!-- end card-body -->
                            </div><!-- end card -->
                        </div>
                        <!-- end col -->
                    </div>
                    <!-- end row -->

                </div> <!-- container-fluid -->
            </div>
            <!-- End Page-content -->


            <?= $this->element('footer') ?>
        </div>
        <!-- end main content-->

    </div>
    <!-- END layout-wrapper -->

    <?= $this->element('customizer') ?>

    <?= $this->element('vendor-scripts') ?>

    <!-- ckeditor -->
    <script src="/libs/@ckeditor/ckeditor5-build-classic/build/ckeditor.js"></script>

    <!-- quill js -->
    <script src="/libs/quill/quill.min.js"></script>

    <!-- init js -->
    <script src="/js/pages/form-editor.init.js"></script>

    <script src="/js/app.js"></script>

</body>

</html>
