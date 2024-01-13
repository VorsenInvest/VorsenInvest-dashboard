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
    import Basic from "./Basic.svelte";
    import Datetime from "./Datetime.svelte";
    import ImagesChart from "./ImagesChart.svelte";
</script>

<svelte:head>
    <title>Apex Scatter Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Scatter Charts" pageTitle="Apexcharts" />
        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Basic Scatter Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <Basic
                            dataColors={[
                                "--vz-primary",
                                "--vz-success",
                                "--vz-info",
                            ]}
                        />
                    </CardBody>
                </Card>
            </Col>

            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">
                            Scatter - Datetime Chart
                        </h4>
                    </CardHeader>
                    <CardBody>
                        <Datetime
                            dataColors={[
                                "--vz-primary",
                                "--vz-success",
                                "--vz-secondary",
                                "--vz-warning",
                                "--vz-info",
                            ]}
                        />
                    </CardBody>
                </Card>
            </Col>
        </Row>
        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Scatter Images Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <ImagesChart
                            dataColors={["--vz-primary", "--vz-info"]}
                        />
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
