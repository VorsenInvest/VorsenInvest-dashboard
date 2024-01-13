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
    import DifferentColor from "./DifferentColor.svelte";
    import MultiSeries from "./MultiSeries.svelte";
    import Advanced from "./Advanced.svelte";
    import MultipleSeries from "./MultipleSeries.svelte";
    import Dumbbell from "./Dumbbell.svelte";
</script>

<svelte:head>
    <title>Apex Timeline Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="TimeLine Charts" pageTitle="Apexcharts" />
        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Basic TimeLine Charts</h4>
                    </CardHeader>
                    <CardBody>
                        <Basic dataColors={["--vz-primary"]} />
                    </CardBody>
                </Card>
            </Col>

            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">
                            Different Color For Each Bar
                        </h4>
                    </CardHeader>
                    <CardBody>
                        <DifferentColor
                            dataColors={[
                                "--vz-primary",
                                "--vz-danger",
                                "--vz-success",
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
                        <h4 class="card-title mb-0">Multi Series Timeline</h4>
                    </CardHeader>
                    <CardBody>
                        <MultiSeries
                            dataColors={["--vz-primary", "--vz-success"]}
                        />
                    </CardBody>
                </Card>
            </Col>

            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">
                            Advanced Timeline (Multiple Range)
                        </h4>
                    </CardHeader>
                    <CardBody>
                        <Advanced
                            dataColors={[
                                "--vz-primary",
                                "--vz-success",
                                "--vz-warning",
                            ]}
                        />
                    </CardBody>
                </Card>
            </Col>
        </Row>
        <Row>
            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Multiple series - Group rows</h4>
                    </CardHeader>

                    <CardBody>
                        <MultipleSeries dataColors={["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-info","--vz-gray","--vz-pink","--vz-purple","--vz-secondary", "--vz-dark"]} />
                    </CardBody>
                </Card>
            </Col>
            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Dumbbell Chart (Horizontal)</h4>
                    </CardHeader>

                    <CardBody>
                        <Dumbbell dataColors={["--vz-primary", "--vz-success"]} />
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
