<svelte:head>
  <title>Vector Map | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
import { Card, CardBody, CardHeader, Col, Container, Row } from 'sveltestrap';
import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
import LineMarkers from './LineMarkers.svelte';
import Markers from './Markers.svelte';
import ImageMarkers from './ImageMarkers.svelte';
</script>

<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Vector" pageTitle="Maps" />

        <Row>
            <Col lg={12}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">Markers</h4>
                    </CardHeader>
                    <CardBody>
                        <div style="height: 400px">
                            <LineMarkers dataColors={["--vz-light"]} />
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>
        <Row>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">World Vector Map with Markers</h4>
                    </CardHeader>
                    <CardBody>
                        <div style="height: 350px">
                            <Markers dataColors={["--vz-light"]} />
                        </div>
                    </CardBody>
                </Card>
            </Col>
            <Col lg={6}>
                <Card>
                    <CardHeader>
                        <h4 class="card-title mb-0">World Vector Map with Image Markers</h4>
                    </CardHeader>
                    <CardBody>
                        <div style="height: 350px">
                            <ImageMarkers dataColors={["--vz-light"]} />
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>
       
    </Container>
</div>