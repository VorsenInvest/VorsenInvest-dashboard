<script>
    import { Card, CardBody, Col, Row } from 'sveltestrap';
    import CountriesCharts from "./CountriesCharts.svelte"
    import Map from '../../Components/Common/Map.svelte'
</script>

<Col xxl={7}>
<Row class="h-100">
    <Col xl={6}>
    <Card class="card-height-100">
        <div class="card-header align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">Live Users By Country</h4>
            <div class="flex-shrink-0">
                <button type="button" class="btn btn-soft-primary btn-sm">
                    Export Report
                </button>
            </div>
        </div>

        <CardBody>
            <div class="text-center" style="height: 252px">
                <Map latitude={-34.397} longitude={150.644} MapType={'world_merc'} dataColor={["--vz-light"]}></Map>
            </div>

            <div class="table-responsive table-card mt-3">
                <table class="table table-borderless table-sm table-centered align-middle table-nowrap mb-1">
                    <thead class="text-muted border-dashed border border-start-0 border-end-0 bg-light-subtle">
                        <tr>
                            <th>Duration (Secs)</th>
                            <th style="width: 30%">Sessions</th>
                            <th style="width: 30%">Views</th>
                        </tr>
                    </thead>
                    <tbody class="border-0">
                        <tr>
                            <td>0-30</td>
                            <td>2,250</td>
                            <td>4,250</td>
                        </tr>
                        <tr>
                            <td>31-60</td>
                            <td>1,501</td>
                            <td>2,050</td>
                        </tr>
                        <tr>
                            <td>61-120</td>
                            <td>750</td>
                            <td>1,600</td>
                        </tr>
                        <tr>
                            <td>121-240</td>
                            <td>540</td>
                            <td>1,040</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </CardBody>

    </Card>
    </Col>

    <Col xl={6}>
    <Card class="card-height-100">
        <div class="card-header align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">Sessions by Countries</h4>
            <div class="">
                <button type="button" class="btn btn-soft-secondary btn-sm">
                    ALL
                </button>
                <button type="button" class="btn btn-soft-info btn-sm">
                    1M
                </button>
                <button type="button" class="btn btn-soft-secondary btn-sm">
                    6M
                </button>
            </div>
        </div>
        <div class="card-body p-0">
            <div>
                <div id="countries_charts" class="apex-charts" dir="ltr">
                    <CountriesCharts dataColors={["--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-secondary", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary", "--vz-primary" ]} />
                </div>
            </div>
        </div>
    </Card>
    </Col>
</Row>
</Col>