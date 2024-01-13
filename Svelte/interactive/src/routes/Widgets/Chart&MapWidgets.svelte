<script>
import { Alert, Button, Card, CardBody, CardHeader, Col, DropdownItem, DropdownMenu, DropdownToggle, ListGroup, ListGroupItem, Progress, Row, Dropdown } from 'sveltestrap';
import Link from 'svelte-link';
export let widgetsAudiences,widgetsPortfolio;
import SessionsByCountriesCharts from './sessionsByCountries.svelte';
import AudiencesMetricsCharts from './audiencesMetrics.svelte';
import MyPortfolioCharts from './myPortfolio.svelte';
import TopReferralsPagesCharts from './topReferralsPages.svelte';
import Map from '../../Components/Common/Map.svelte'

</script>
<Row>
    <Col class="col-12">
        <h5 class="text-decoration-underline mb-3 mt-2 pb-3">Chart & Map Widgets</h5>
    </Col>
</Row>

<Row>
    <Col xxl={4} xl={6}>
        <Card class="card-height-100">
            <CardHeader class="align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">Live Users By Country</h4>
                <div class="flex-shrink-0">
                    <Button color="primary" size='sm' class="btn-soft-primary">
                        Export Report
                    </Button>
                </div>
            </CardHeader>
            <CardBody>
                    <div
                        class="text-center"
                        style="height: 252px"
                    >
                        <Map latitude={-34.397} longitude={150.644} MapType={'world_merc'} dataColor={["--vz-light"]}></Map>
                    </div>

                <div class="table-responsive table-card mt-3">
                    <table class="table table-borderless table-sm table-centered align-middle table-nowrap mb-1">
                        <thead class="text-muted border-dashed border border-start-0 border-end-0 bg-soft-light">
                            <tr>
                                <th>Duration (Secs)</th>
                                <th style="width:30%">Sessions</th>
                                <th style="width:30%">Views</th>
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

    <Col xxl={4} xl={6}>
        <Card class="card-height-100">
            <CardHeader class="align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">Sessions by Countries</h4>
                <div>
                    <Button color="info" size="sm" class="btn-soft-info me-1">
                        ALL
                    </Button>
                    <Button color="primary" size="sm" class="btn-soft-primary me-1">
                        1M
                    </Button>
                    <Button color="info" size="sm" class="btn-soft-info">
                        6M
                    </Button>
                </div>
            </CardHeader>
            <CardBody class="p-0">
                <div>
                    <div id="countries_charts" class="apex-charts" dir="ltr">
                        <SessionsByCountriesCharts dataColors={["--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-primary", "--vz-info", "--vz-info", "--vz-info", "--vz-info", "--vz-info"]} />
                        
                    </div>
                </div>
            </CardBody>
        </Card>
    </Col>

    <Col xxl={4}>
        <Card class="card-height-100">
            <CardHeader class="border-0 align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">Audiences Metrics</h4>
                <div>
                    <Button color="info" size="sm" class="btn-soft-info me-1">
                        ALL
                    </Button>
                    <Button color="info" size="sm" class="btn-soft-info me-1">
                        1M
                    </Button>
                    <Button color="info" size="sm" class="btn-soft-info me-1">
                        6M
                    </Button>
                    <Button color="primary" size="sm" class="btn-soft-primary">
                        1Y
                    </Button>
                </div>
            </CardHeader>

            <CardHeader class="p-0">
                <Alert color="warning" class="alert-solid alert-label-icon border-0 rounded-0 m-0 d-flex align-items-center" role="alert">
                    <i class="ri-error-warning-line label-icon"></i>
                    <div class="flex-grow-1 text-truncate">
                        Your free trial expired in <b>17</b> days.
                    </div>
                    <div class="flex-shrink-0">
                        <Link href="/pages/pricing/pages-pricing" class="text-reset text-decoration-underline"><b>Upgrade</b></Link>
                    </div>
                </Alert>
            </CardHeader>
            <CardHeader class="p-0 border-0 bg-soft-light">
                <Row class="g-0 text-center">
                    {#each widgetsAudiences as item}
                    <div class="col-6 col-sm-4">
                        <div class="p-3 border border-dashed border-start-0">
                            <h5 class="mb-1">
                                {#each item.subCounter as item}
                                    {item.prefix}<span class="counter-value" data-target="{item.counter}">0</span>{item.suffix}
                                   
                                {/each}
                                {#if item.percentage}
                                    <span class="text-success ms-1 fs-13">{item.percentage}<i class="ri-arrow-right-up-line ms-1 align-middle"></i></span>
                                {/if}
                            </h5>
                            <p class="text-muted mb-0">{item.caption}</p>
                        </div>
                    </div>
                    {/each}
                </Row>
            </CardHeader>

            <CardBody class="p-0 pb-2">
                <div>
                    <div id="audiences_metrics_charts" class="apex-charts" dir="ltr">
                        
                        <AudiencesMetricsCharts dataColors={["--vz-primary", "--vz-gray-300"]} />
                    </div>
                </div>
            </CardBody>
        </Card>
    </Col>
</Row>

<Row>
    <Col xxl={4} xl={6}>
        <Card class="card-height-100">
            <CardHeader class="align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">Sales by Locations</h4>
                <div class="flex-shrink-0">
                    <Button color="primary" size="sm" class="btn-soft-primary">
                        Export Report
                    </Button>
                </div>
            </CardHeader>

            <CardBody>
                <div id="sales-by-locations" style="height: 269px">
                    <!-- <Map latitude={-34.397} longitude={150.644}></Map> -->
                </div>
                <div class="px-2 py-2 mt-1">
                    <p class="mb-1">New Maxico <span class="float-end">75%</span></p>
                    <Progress color="primary" value={75} striped class="mt-2" style="height: 6px" />

                    <p class="mt-3 mb-1">California <span class="float-end">47%</span></p>
                    <Progress color="primary" value={47} striped class="mt-2" style="height: 6px" />

                    <p class="mt-3 mb-1">Texas <span class="float-end">82%</span></p>
                    <Progress color="primary" value={82} striped class="mt-2" style="height: 6px" />
                </div>
            </CardBody>
        </Card>
    </Col>

    <Col xxl={4} xl={6}>
        <Card class="card-height-100">
            <CardHeader class="border-bottom-dashed align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">My Portfolio</h4>
                <div>

                    <Dropdown class="card-header-dropdown" direction='left'>
                        <DropdownToggle tag="button" class="btn btn-soft-primary btn-sm" >
                            <span class="text-uppercase">Btc<i class="mdi mdi-chevron-down align-middle ms-1"></i></span>
                        </DropdownToggle>
                        <DropdownMenu class="dropdown-menu-end">
                            <DropdownItem>BTC</DropdownItem>
                            <DropdownItem>USD</DropdownItem>
                            <DropdownItem>Euro</DropdownItem>
                        </DropdownMenu>
                    </Dropdown>

                </div>
            </CardHeader>

            <CardBody>
                <div id="portfolio_donut_charts" dir="ltr">
                    <MyPortfolioCharts dataColors={["--vz-primary", "--vz-primary-rgb, 0.80", "--vz-primary-rgb, 0.6", "--vz-primary-rgb, 0.4"]} />
                </div>

                <ListGroup class="border-dashed mb-0" flush>
                    {#each widgetsPortfolio as item}
                    <ListGroupItem class="px-0">
                        <div class="d-flex">
                            <div class="flex-shrink-0 avatar-xs">
                                <span class="avatar-title bg-light p-1 rounded-circle">
                                    <img src={item.img} class="img-fluid" alt="" />
                                </span>
                            </div>
                            <div class="flex-grow-1 ms-2">
                                <h6 class="mb-1">{item.label}</h6>
                                <p class="fs-13 mb-0 text-muted"><i class={"mdi mdi-circle fs-10 align-middle me-1 text-" + item.coinNameClass}></i>{item.coinName}</p>
                            </div>
                            <div class="flex-shrink-0 text-end">
                                <h6 class="mb-1">{item.coinName} {item.coinVolume}</h6>
                                <p class={"fs-12 mb-0 text-" + item.priceClass}>{item.price}</p>
                            </div>
                        </div>
                    </ListGroupItem>
                    {/each}
                </ListGroup>
            </CardBody>
        </Card>
    </Col>

    <Col xxl={4}>
        <Card class="card-height-100">
            <CardHeader class="align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">Top Referrals Pages</h4>
                <div class="flex-shrink-0">
                    <Button color="primary" size="sm" class="btn-soft-primary">
                        Export Report
                    </Button>
                </div>
            </CardHeader>

            <CardBody>
                <div id="color_heatmap" class="apex-charts mt-n3" dir="ltr">
                    <TopReferralsPagesCharts dataColors={["--vz-info", "--vz-success", "--vz-primary", "--vz-warning", "--vz-secondary"]}/>
                </div>

                <Row class="g-3">
                    <Col md={6}>
                        <div class="d-flex mb-3">
                            <div class="flex-grow-1">
                                <p class="text-truncate text-muted fs-15 mb-0"><i class="mdi mdi-circle align-middle text-primary me-2"></i>www.google.com</p>
                            </div>
                            <div class="flex-shrink-0">
                                <p class="mb-0">24.58%</p>
                            </div>
                        </div>
                        <div class="d-flex mb-3">
                            <div class="flex-grow-1">
                                <p class="text-truncate text-muted fs-15 mb-0"><i class="mdi mdi-circle align-middle text-warning me-2"></i>www.medium.com</p>
                            </div>
                            <div class="flex-shrink-0">
                                <p class="mb-0">12.22%</p>
                            </div>
                        </div>
                        <div class="d-flex">
                            <div class="flex-grow-1">
                                <p class="text-truncate text-muted fs-15 mb-0"><i class="mdi mdi-circle align-middle text-secondary me-2"></i>Other</p>
                            </div>
                            <div class="flex-shrink-0">
                                <p class="mb-0">17.58%</p>
                            </div>
                        </div>
                    </Col>
                    <Col md={6}>
                        <div class="d-flex mb-3">
                            <div class="flex-grow-1">
                                <p class="text-truncate text-muted fs-14 mb-0"><i class="mdi mdi-circle align-middle text-info me-2"></i>www.youtube.com</p>
                            </div>
                            <div class="flex-shrink-0">
                                <p class="mb-0">17.51%</p>
                            </div>
                        </div>
                        <div class="d-flex mb-3">
                            <div class="flex-grow-1">
                                <p class="text-truncate text-muted fs-14 mb-0"><i class="mdi mdi-circle align-middle text-success me-2"></i>www.meta.com</p>
                            </div>
                            <div class="flex-shrink-0">
                                <p class="mb-0">23.05%</p>
                            </div>
                        </div>
                    </Col>
                </Row>

                <div class="mt-2 text-center">
                    <Link href={null} class="text-muted text-decoration-underline">Show All</Link>
                </div>
            </CardBody>
        </Card>
    </Col>
</Row>