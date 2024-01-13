<script>
    import { Card, CardBody, CardHeader, Col, Row } from 'sveltestrap';
    import AudiencesCharts from "./AudiencesCharts.svelte"
</script>
<Col xl={6}>
<Card>
    <CardHeader class="border-0 align-items-center d-flex">
        <h4 class="card-title mb-0 flex-grow-1">Audiences Metrics</h4>
        <div class="">
            <button type="button" class="btn btn-soft-secondary btn-sm">
                ALL
            </button>
            <button type="button" class="btn btn-soft-secondary btn-sm">
                1M
            </button>
            <button type="button" class="btn btn-soft-secondary btn-sm">
                6M
            </button>
            <button type="button" class="btn btn-soft-primary btn-sm">
                1Y
            </button>
        </div>
    </CardHeader>
    <CardHeader class="p-0 border-0 bg-light-subtle">
        <Row class="g-0 text-center">
            <Col xs={6} sm={4}>
            <div class="p-3 border border-dashed border-start-0">
                <h5 class="mb-1"><span class="counter-value" data-target="854">0</span>
                    <span class="text-success ms-1 fs-13">49%<i
                            class="ri-arrow-right-up-line ms-1 align-middle"></i></span>
                </h5>
                <p class="text-muted mb-0">Avg. Session</p>
            </div>
            </Col>
            <Col xs={6} sm={4}>
            <div class="p-3 border border-dashed border-start-0">
                <h5 class="mb-1"><span class="counter-value" data-target="1278">0</span>
                    <span class="text-success ms-1 fs-13">60%<i
                            class="ri-arrow-right-up-line ms-1 align-middle"></i></span>
                </h5>
                <p class="text-muted mb-0">Conversion Rate</p>
            </div>
            </Col>
            <Col xs={6} sm={4}>
            <div class="p-3 border border-dashed border-start-0 border-end-0">
                <h5 class="mb-1"><span class="counter-value" data-target="3">0</span>m <span class="counter-value"
                        data-target="40">0</span>sec
                    <span class="text-success ms-1 fs-13">37%<i
                            class="ri-arrow-right-up-line ms-1 align-middle"></i></span>
                </h5>
                <p class="text-muted mb-0">Avg. Session Duration</p>
            </div>
            </Col>
        </Row>
    </CardHeader>
    <CardBody class="p-0 pb-2">
        <div>
            <AudiencesCharts dataColors={["--vz-secondary", "--vz-light"]} />
            <!-- <div id="audiences_metrics_charts">
            </div> -->
        </div>
    </CardBody>
</Card>
</Col>