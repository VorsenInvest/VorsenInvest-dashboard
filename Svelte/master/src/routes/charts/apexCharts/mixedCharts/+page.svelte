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
    import Line from "./Line.svelte";
    import YAxis from "./YAxis.svelte";
    import Area from "./Area.svelte";
    import LineColumnArea from "./LineColumnArea.svelte";
</script>

<svelte:head>
    <title>Apex Mixed Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Mixed Charts" pageTitle="Apexcharts" />
        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Line & Column Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <Line dataColors={["--vz-primary", "--vz-success"]} />
                    </CardBody>
                </Card>
            </Col>

            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Multiple Y-Axis Charts</h4>
                    </CardHeader>
                    <CardBody>
                        <YAxis
                            dataColors={[
                                "--vz-primary",
                                "--vz-info",
                                "--vz-success",
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
                        <h4 class="card-title mb-0">Line & Area Charts</h4>
                    </CardHeader>
                    <CardBody>
                        <Area dataColors={["--vz-primary", "--vz-success"]} />
                    </CardBody>
                </Card>
            </Col>

            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">
                            Line, Column & Area Charts
                        </h4>
                    </CardHeader>
                    <CardBody>
                        <LineColumnArea
                            dataColors={[
                                "--vz-primary",
                                "--vz-success",
                                "--vz-danger",
                            ]}
                        />
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
