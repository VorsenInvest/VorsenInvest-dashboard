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
    import ComboCandlestick from "./ComboCandlestick.svelte";
    import ComboCandlestick1 from "./ComboCandlestick1.svelte";
    import Category from "./Category.svelte";
    import CandlestickLine from "./CandlestickLine.svelte";
</script>

<svelte:head>
    <title>Apex Canlestick Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Candlestick Charts" pageTitle="Apexcharts" />
        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Basic Candlestick Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <Basic dataColors={["--vz-success", "--vz-primary"]} />
                    </CardBody>
                </Card>
            </Col>

            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">
                            Candlestick Synced with Brush Chart (Combo)
                        </h4>
                    </CardHeader>
                    <CardBody>
                        <div>
                            <div id="combo_candlestick">
                                <ComboCandlestick
                                    dataColors={["--vz-info", "--vz-primary"]}
                                />
                            </div>
                            <div id="combo_candlestick_chart">
                                <ComboCandlestick1 dataColors={["--vz-success", "--vz-primary"]} />
                            </div>
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>

        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Category X-Axis</h4>
                    </CardHeader>
                    <CardBody>
                        <Category
                            dataColors={["--vz-success-rgb, 0.65", "--vz-danger-rgb, 0.65"]}
                        />
                    </CardBody>
                </Card>
            </Col>
            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Candlestick with line</h4>
                    </CardHeader>

                    <CardBody>
                        <CandlestickLine dataColors={["--vz-success", "--vz-danger", "--vz-info", "--vz-warning"]}/>
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
