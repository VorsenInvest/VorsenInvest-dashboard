<script>
    import { Button, Card, CardBody, CardHeader, Col, Row } from 'sveltestrap';
    import MarkerCharts from './MarkerCharts.svelte';

</script>
<Row>
    <Col xl={12}>
    <Card>
        <CardHeader class="border-0 align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">Market Graph</h4>
            <div class="">
                <Button type="button" color="soft-secondary" size="sm" class="material-shadow-none">
                    1H
                </Button>
                <Button type="button" color="soft-secondary" size="sm" class="material-shadow-none">
                    7D
                </Button>
                <Button type="button" color="soft-secondary" size="sm" class="material-shadow-none">
                    1M
                </Button>
                <Button type="button" color="soft-secondary" size="sm" class="material-shadow-none">
                    1Y
                </Button>
                <Button type="button" color="soft-primary" size="sm" class="material-shadow-none">
                    ALL
                </Button>
            </div>
        </CardHeader>
        <CardBody class="p-0">
            <div
                class="bg-light-subtle border-top-dashed border border-start-0 border-end-0 border-bottom-dashed py-3 px-4">
                <Row class="align-items-center">
                    <Col xs={6}>
                    <div class="d-flex flex-wrap gap-4 align-items-center">
                        <h5 class="fs-19 mb-0">0.014756</h5>
                        <p class="fw-medium text-muted mb-0">$75.69 <span class="text-success fs-11 ms-1">+1.99%</span>
                        </p>
                        <p class="fw-medium text-muted mb-0">High <span class="text-dark fs-11 ms-1">0.014578</span></p>
                        <p class="fw-medium text-muted mb-0">Low <span class="text-dark fs-11 ms-1">0.0175489</span></p>
                    </div>
                    </Col>
                    <Col xs={6}>
                    <div class="d-flex">
                        <div class="d-flex justify-content-end text-end flex-wrap gap-4 ms-auto">
                            <div class="pe-3">
                                <h6 class="mb-2 text-truncate text-muted">Total Balance</h6>
                                <h5 class="mb-0">$72.8k</h5>

                            </div>
                            <div class="pe-3">
                                <h6 class="mb-2 text-muted">Profit</h6>
                                <h5 class="text-success mb-0">+$49.7k</h5>
                            </div>
                            <div class="pe-3">
                                <h6 class="mb-2 text-muted">Loss</h6>
                                <h5 class="text-danger mb-0">-$23.1k</h5>
                            </div>
                        </div>
                    </div>
                    </Col>
                </Row>
            </div>
        </CardBody>
        <div class="card-body p-0 pb-3">
            <div id="Market_chart" class="apex-charts" dir="ltr">
                <MarkerCharts dataColors={["--vz-success", "--vz-danger" ]} />
            </div>
        </div>
    </Card>
    </Col>
</Row>