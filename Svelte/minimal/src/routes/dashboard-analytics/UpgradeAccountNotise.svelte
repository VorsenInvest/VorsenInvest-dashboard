<script>
    import { AlertTriangleIcon } from 'svelte-feather-icons'
    import { Alert, Card, CardBody, Col, Row } from 'sveltestrap';
    import illustarator2 from '../../assets/images/user-illustarator-2.png'
</script>
<Row>
    <Col xs={12}>
        <Card>
            <CardBody class="p-0">
                <Alert color="primary" class="border-0 rounded-0 m-0 d-flex align-items-center" role="alert">
                    <AlertTriangleIcon class="text-primary me-2 icon-sm"/>
                    <div class="flex-grow-1 text-truncate">
                        Your free trial expired in <b>17</b> days.
                    </div>
                    <div class="flex-shrink-0">
                        <a href="/pages/pricing/pages-pricing" class="text-reset text-decoration-underline"><b>Upgrade</b></a>
                    </div>
                </Alert>

                <Row class="align-items-end">
                    <Col sm={8}>
                        <div class="p-3">
                            <p class="fs-16 lh-base">Upgrade your plan from a <span class="fw-semibold">Free
                                trial</span>, to ‘Premium Plan’ <i class="mdi mdi-arrow-right"></i></p>
                            <div class="mt-3">
                                <a href="/pages/pricing/pages-pricing" class="btn btn-primary">Upgrade Account!</a>
                            </div>
                        </div>
                    </Col>
                    <Col sm={4}>
                        <div class="px-3">
                            <img src={illustarator2} class="img-fluid" alt="" />
                        </div>
                    </Col>
                </Row>
            </CardBody>
        </Card>
    </Col>
</Row>