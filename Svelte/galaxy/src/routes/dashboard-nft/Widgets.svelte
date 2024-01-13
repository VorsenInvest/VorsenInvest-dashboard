<script>
    import { Card, CardBody, Col, Dropdown, DropdownItem, DropdownMenu, DropdownToggle, Row } from 'sveltestrap';
    import Bgd from "../../assets/images/bg-d.png";
    import Link from 'svelte-link';
    import Counter from '../../Components/Common/CounterPage.svelte';
</script>
<Counter />
<Row>
    <Col xl={6}>
    <Card class="overflow-hidden">
        <CardBody class="bg-marketplace d-flex">
            <div class="flex-grow-1">
                <h4 class="fs-18 lh-base mb-0">Discover, Collect, Sell and Create <br /> your own <span
                        class="text-primary">NFTs.</span> </h4>
                <p class="mb-0 mt-2 pt-1 text-muted">The world's first and largest digital marketplace.</p>
                <div class="d-flex gap-3 mt-4">
                    <Link href="/#" class="btn btn-primary">Discover Now </Link>
                    <Link href="/#" class="btn btn-soft-primary">Create Your Own</Link>
                </div>
            </div>
            <img src={Bgd} alt="" class="img-fluid" />
        </CardBody>
    </Card>
    </Col>
    <Col xl={3} md={6}>
    <Card class="card-height-100">
        <CardBody>
            <div class="float-end">
                <Dropdown class="card-header-dropdown" direction="start">
                    <DropdownToggle tag="a" class="text-reset dropdown-btn p-0" color="" role="button">
                        <span class="text-muted fs-18"><i class="mdi mdi-dots-vertical align-middle"></i></span>
                    </DropdownToggle>
                    <DropdownMenu class="dropdown-menu-end" end>
                        <DropdownItem>Today</DropdownItem>
                        <DropdownItem>Last Week</DropdownItem>
                        <DropdownItem>Last Month</DropdownItem>
                        <DropdownItem>Current Year</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </div>
            <div class="d-flex align-items-center">
                <div class="avatar-sm flex-shrink-0">
                    <span class="avatar-title bg-primary-subtle rounded fs-3">
                        <i class="bx bx-dollar-circle text-primary"></i>
                    </span>
                </div>
                <div class="flex-grow-1 ps-3">
                    <h5 class="text-muted text-uppercase fs-13 mb-0">Total Revenue</h5>
                </div>
            </div>
            <div class="mt-4 pt-1">
                <h4 class="fs-22 fw-semibold ff-secondary mb-0">$<span class="counter-value"
                        data-target="559526.564"></span> </h4>
                <p class="mt-4 mb-0 text-muted"><span class="badge bg-danger-subtle text-danger mb-0 me-1"> <i
                            class="ri-arrow-down-line align-middle"></i> 3.96 % </span> vs. previous month</p>
            </div>
        </CardBody>
    </Card>
    </Col>
    <Col xl={3} md={6}>
    <Card class="card-height-100">
        <CardBody>
            <div class="float-end">
                <Dropdown class="card-header-dropdown" direction="start">
                    <DropdownToggle tag="a" class="text-reset dropdown-btn p-0" color="" role="button">
                        <span class="text-muted fs-18"><i class="mdi mdi-dots-vertical align-middle"></i></span>
                    </DropdownToggle>
                    <DropdownMenu class="dropdown-menu-end" end>
                        <DropdownItem>Today</DropdownItem>
                        <DropdownItem>Last Week</DropdownItem>
                        <DropdownItem>Last Month</DropdownItem>
                        <DropdownItem>Current Year</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </div>
            <div class="d-flex align-items-center">
                <div class="avatar-sm flex-shrink-0">
                    <span class="avatar-title bg-primary-subtle rounded fs-3">
                        <i class="bx bx-wallet text-primary"></i>
                    </span>
                </div>
                <div class="flex-grow-1 ps-3">
                    <h5 class="text-muted text-uppercase fs-13 mb-0">Estimated</h5>
                </div>
            </div>
            <div class="mt-4 pt-1">
                <h4 class="fs-22 fw-semibold ff-secondary mb-0">$<span class="counter-value"
                        data-target="624562.564"></span> </h4>
                <p class="mt-4 mb-0 text-muted"><span class="badge bg-success-subtle text-success mb-0"> <i
                            class="ri-arrow-up-line align-middle"></i> 16.24 % </span> vs. previous month</p>
            </div>
        </CardBody>
    </Card>
    </Col>
</Row>