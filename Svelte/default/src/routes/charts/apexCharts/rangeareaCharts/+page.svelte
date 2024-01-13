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
    import Combo from "./Combo.svelte";
</script>

<svelte:head>
    <title>Apex Range Area Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Range Area Charts" pageTitle="Apexcharts" />
        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Basic Range Area Chart</h4>
                    </CardHeader>
                    <CardBody>
                        <Basic dataColors={["--vz-primary", "--vz-success"]} />
                    </CardBody>
                </Card>
            </Col>

            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Combo</h4>
                    </CardHeader>
                    <CardBody>
                        <Combo
                            dataColors={["--vz-info", "--vz-danger"]}
                        />
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
