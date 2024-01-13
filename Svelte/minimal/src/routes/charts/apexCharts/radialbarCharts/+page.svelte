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
    import SimpleRadialbar from "./SimpleRadialbar.svelte";
    import MultipleRadialbar from "./MultipleRadialbar.svelte";
    import CircleRadialbar from "./CircleRadialbar.svelte";
    import GradientCircleRadialbar from "./GradientCircleRadialbar.svelte";
    import StrokedCircleRadial from "./StrokedCircleRadial.svelte";
    import SemiCircularRadial from "./SemiCircularRadial.svelte";
    import ImageRadialbar from './ImageRadialbar.svelte'
</script>

<svelte:head>
    <title>Apex Radial Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Radialbar Charts" pageTitle="Apexcharts" />
        <Row>
            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Simple Radialbar Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <SimpleRadialbar dataColors={["--vz-primary"]} />
                    </CardBody>
                </Card>
            </Col>

            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Multiple Radialbar</h4>
                    </CardHeader>
                    <CardBody>
                        <MultipleRadialbar
                            dataColors={[
                                "--vz-primary",
                                "--vz-success",
                                "--vz-secondary",
                                "--vz-info",
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
                        <h4 class="card-title mb-0">
                            Circle Chart - Custom Angle
                        </h4>
                    </CardHeader>
                    <CardBody>
                        <CircleRadialbar
                            dataColors={[
                                "--vz-primary",
                                "--vz-primary-rgb, 0.65",
                                "--vz-primary-rgb, 0.45",
                                "--vz-primary-rgb, 0.30",
                            ]}
                        />
                    </CardBody>
                </Card>
            </Col>

            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Gradient Circle Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <GradientCircleRadialbar
                            dataColors={["--vz-primary"]}
                        />
                    </CardBody>
                </Card>
            </Col>
        </Row>

        <Row>
            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Stroked Circle Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <StrokedCircleRadial dataColors={["--vz-success"]} />
                    </CardBody>
                </Card>
            </Col>

            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Radialbars with Image</h4>
                    </CardHeader>

                    <CardBody>
                        <ImageRadialbar dataColors={["--vz-success"]}/>
                    </CardBody>
                </Card>
            </Col>
        </Row>
        <Row>
            <Col xl={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Semi Circular Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <SemiCircularRadial dataColors={["--vz-primary"]} />
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
