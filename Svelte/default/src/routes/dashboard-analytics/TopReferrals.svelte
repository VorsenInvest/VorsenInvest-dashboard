<script>
    import { Card, CardBody, CardHeader, Col, Row, Progress } from 'sveltestrap';
    import illustrator from '../../assets/images/illustrator-1.png'
</script>
<Col xl={4} md={6}>
<Card class="card-height-100">
    <CardHeader class="align-items-center d-flex">
        <h4 class="card-title mb-0 flex-grow-1">Top Referrals Pages</h4>
        <div class="flex-shrink-0">
            <button type="button" class="btn btn-soft-primary btn-sm">
                Export Report
            </button>
        </div>
    </CardHeader>

    <CardBody>

        <Row class="align-items-center">
            <Col xs={6}>
            <h6 class="text-muted text-uppercase fw-semibold text-truncate fs-12 mb-3">Total Referrals Page</h6>
            <h4 class="fs- mb-0">725,800</h4>
            <p class="mb-0 mt-2 text-muted"><span class="badge bg-success-subtle text-success mb-0">
                    <i class="ri-arrow-up-line align-middle"></i> 15.72 %
                </span> vs. previous month</p>
            </Col>
            <Col xs={6}>
            <div class="text-center">
                <img src={illustrator} class="img-fluid" alt="" />
            </div>
            </Col>
        </Row>
        <div class="mt-3 pt-2">
            <div class="progress progress-lg rounded-pill">
                <Progress bar color="primary" value="25" />
                <Progress bar color="info" value="18" />
                <Progress bar color="success" value="22" />
                <Progress bar color="warning" value="16" />
                <Progress bar color="danger" value="19" />
            </div>
        </div>

        <div class="mt-3 pt-2">
            <div class="d-flex mb-2">
                <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0"><i
                            class="mdi mdi-circle align-middle text-primary me-2"></i>www.google.com</p>
                </div>
                <div class="flex-shrink-0">
                    <p class="mb-0">24.58%</p>
                </div>
            </div>
            <div class="d-flex mb-2">
                <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0"><i
                            class="mdi mdi-circle align-middle text-info me-2"></i>www.youtube.com</p>
                </div>
                <div class="flex-shrink-0">
                    <p class="mb-0">17.51%</p>
                </div>
            </div>
            <div class="d-flex mb-2">
                <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0"><i
                            class="mdi mdi-circle align-middle text-success me-2"></i>www.meta.com</p>
                </div>
                <div class="flex-shrink-0">
                    <p class="mb-0">23.05%</p>
                </div>
            </div>
            <div class="d-flex mb-2">
                <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0"><i
                            class="mdi mdi-circle align-middle text-warning me-2"></i>www.medium.com</p>
                </div>
                <div class="flex-shrink-0">
                    <p class="mb-0">12.22%</p>
                </div>
            </div>
            <div class="d-flex">
                <div class="flex-grow-1">
                    <p class="text-truncate text-muted fs-14 mb-0"><i
                            class="mdi mdi-circle align-middle text-danger me-2"></i>Other</p>
                </div>
                <div class="flex-shrink-0">
                    <p class="mb-0">17.58%</p>
                </div>
            </div>
        </div>

        <div class="mt-2 text-center">
            <a href="{null}" class="text-muted text-decoration-underline">Show All</a>
        </div>

    </CardBody>
</Card>
</Col>