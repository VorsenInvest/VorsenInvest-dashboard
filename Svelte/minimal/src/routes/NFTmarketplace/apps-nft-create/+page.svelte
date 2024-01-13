<script>
    import {
        Card,
        CardBody,
        CardHeader,
        Col,
        Container,
        Form,
        Row,
        Label,
    } from "sveltestrap";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import FilePond, { registerPlugin, supported } from "svelte-filepond";
    import "filepond/dist/filepond.min.css";

    import FilePondPluginImageExifOrientation from "filepond-plugin-image-exif-orientation";
    import FilePondPluginImagePreview from "filepond-plugin-image-preview";
    import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css";

    // Register the plugins
    registerPlugin(
        FilePondPluginImageExifOrientation,
        FilePondPluginImagePreview
    );

    // a reference to the component, used to call FilePond methods
    let pond;

    // pond.getFiles() will return the active files

    // the name to use for the internal file input
    let name = "filepond";

    // handle filepond events
    function handleInit() {
        console.log("FilePond has initialised");
    }

    function handleAddFile(err, fileItem) {
        console.log("A file has been added", fileItem);
    }
</script>

<svelte:head>
    <title>Create NFT | Velzon - Svelte Admin & Dashboard Template</title>
    <!-- <style>
        @import "../filepond/dist/filepond.css";
        @import "filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css";
    </style> -->
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Create NFT" pageTitle="NFT Marketplace" />
        <Row>
            <Col lg={12}>
                <Card>
                    <CardHeader>
                        <h5 class="card-title mb-0">Create New File</h5>
                    </CardHeader>
                    <CardBody>
                        <Form>
                            <Row class="g-3">
                                <Col lg={12}>
                                    <h5 class="fw-semibold mb-3">
                                        Image, Video, Audio, or 3D Model
                                    </h5>
                                    <FilePond
                                        bind:this={pond}
                                        {name}
                                        allowMultiple={true}
                                        oninit={handleInit}
                                        onaddfile={handleAddFile}
                                    />
                                </Col>
                                <Col lg={12}>
                                    <Label
                                        htmlfor="productName"
                                        class="form-label">Product Name</Label
                                    >
                                    <input
                                        type="text"
                                        class="form-control"
                                        id="productName"
                                        placeholder="Enter product name"
                                    />
                                </Col>
                                <Col lg={12}>
                                    <Label
                                        htmlfor="discription"
                                        class="form-label">Discription</Label
                                    >
                                    <textarea
                                        class="form-control"
                                        id="discription"
                                        rows="3"
                                        placeholder="Enter discription"
                                    />
                                </Col>
                                <Col lg={12}>
                                    <Label
                                        htmlfor="externalLink"
                                        class="form-label">External link</Label
                                    >
                                    <input
                                        type="text"
                                        class="form-control"
                                        id="externalLink"
                                        placeholder="Enter external link"
                                    />
                                </Col>
                                <Col lg={4}>
                                    <Label
                                        htmlfor="itemPrice"
                                        class="form-label">Item Price</Label
                                    >
                                    <input
                                        type="text"
                                        class="form-control"
                                        id="itemPrice"
                                        placeholder="Price"
                                    />
                                </Col>
                                <Col lg={4}>
                                    <Label htmlfor="size" class="form-label"
                                        >Size</Label
                                    >
                                    <input
                                        type="text"
                                        class="form-control"
                                        id="size"
                                        placeholder="Size"
                                    />
                                </Col>
                                <Col lg={4}>
                                    <Label
                                        htmlfor="properties"
                                        class="form-label">Properties</Label
                                    >
                                    <input
                                        type="text"
                                        class="form-control"
                                        id="properties"
                                        placeholder="Properties"
                                    />
                                </Col>
                                <Col lg={12}>
                                    <div>
                                        <div
                                            class="form-check form-check-inline"
                                        >
                                            <input
                                                class="form-check-input"
                                                type="checkbox"
                                                id="inlineCheckbox1"
                                                value="option1"
                                            />
                                            <Label
                                                class="form-check-label"
                                                htmlfor="inlineCheckbox1"
                                                >Put on sale</Label
                                            >
                                        </div>
                                        <div
                                            class="form-check form-check-inline"
                                        >
                                            <input
                                                class="form-check-input"
                                                type="checkbox"
                                                id="inlineCheckbox2"
                                                value="option2"
                                            />
                                            <Label
                                                class="form-check-label"
                                                htmlfor="inlineCheckbox2"
                                                >Instant sale price</Label
                                            >
                                        </div>
                                        <div
                                            class="form-check form-check-inline"
                                        >
                                            <input
                                                class="form-check-input"
                                                type="checkbox"
                                                id="inlineCheckbox3"
                                                value="option3"
                                            />
                                            <Label
                                                class="form-check-label"
                                                htmlfor="inlineCheckbox3"
                                                >Unlock one purchased</Label
                                            >
                                        </div>
                                    </div>
                                </Col>
                                <Col lg={12}>
                                    <div class="text-end">
                                        <button class="btn btn-primary"
                                            >Create Item</button
                                        >
                                    </div>
                                </Col>
                            </Row>
                        </Form>
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
