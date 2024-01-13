<script>
    import {
        Col,
        Container,
        Row,
        Card,
        CardHeader,
        CardBody,
    } from "sveltestrap";
    import Editor from "@tinymce/tinymce-svelte";
    // import CKEditor from "ckeditor5-svelte";
    // import DecoupledEditor from "@ckeditor/ckeditor5-build-decoupled-document/build/ckeditor";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";

    // let editor;
    // let editorInstance = null;
    // let editorData = "Hello World";

    // let editorConfig = {
    //     toolbar: {
    //         items: [
    //             "heading",
    //             "|",
    //             "fontFamily",
    //             "fontSize",
    //             "bold",
    //             "italic",
    //             "underline",
    //         ],
    //     },
    // };

    // onMount(() => {
    //     editor = new DecoupledEditor(
    //         document.querySelector("#editor"),
    //         editorConfig
    //     );
    //     editor.setData(editorData);
    //     editorInstance = editor.ui.view.editable;
    // });
</script>

<svelte:head>
    <link href="//cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet" />
</svelte:head>

<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Form Editor" pageTitle="Forms" />

        <Row>
            <Col lg={12}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Tinymce Editor</h4>
                    </CardHeader>

                    <CardBody>
                        <Editor />
                    </CardBody>
                </Card>
            </Col>
            <!-- <Col lg={12}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Tinymce Editor</h4>
                    </CardHeader>

                    <CardBody> -->
                        <!-- <CKEditor
                            bind:editor
                            bind:config={editorConfig}
                            bind:value={editorData}
                        /> -->
                    <!-- </CardBody>
                </Card>
            </Col> -->
        </Row>
    </Container>
</div>
