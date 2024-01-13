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
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";

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
        </Row>
    </Container>
</div>
