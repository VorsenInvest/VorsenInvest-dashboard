<script>
    import {
        Card,
        CardBody,
        CardHeader,
        Col,
        Container,
        Row,
    } from "sveltestrap";
    import BreadCrumb from "../../../../Components/Common/BreadCrumb.svelte";
    import Funnel from "./Funnel.svelte";
    import Pyramid from "./Pyramid.svelte";
</script>

<svelte:head>
    <title>Apex Funnel Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Funnel Charts" pageTitle="Apexcharts" />
        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Funnel Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <Funnel dataColors={["--vz-success"]} />
                    </CardBody>
                </Card>
            </Col>

            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Pyramid</h4>
                    </CardHeader>
                    <CardBody>
                        <Pyramid
                            dataColors={["--vz-info", "--vz-danger", "--vz-primary", "--vz-secondary", "--vz-success", "--vz-dark", "--vz-warning"]}
                        />
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
