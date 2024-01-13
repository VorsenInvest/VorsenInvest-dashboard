<script>
    import { Card, Col, DropdownItem, DropdownMenu, DropdownToggle, Dropdown } from 'sveltestrap';

import DealTypeCharts from "./DealTypeCharts.svelte";

</script>
<Col xxl={3} md={6}>
    <Card class="card-height-100">
        <div class="card-header align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">Deal Type</h4>
            <div class="flex-shrink-0">
                <Dropdown class="card-header-dropdown">
                    <DropdownToggle tag="a" color="" class="text-reset dropdown-btn p-0" role="button">
                        <span class="fw-semibold text-uppercase fs-12">Sort by: </span><span class="text-muted">Monthly<i class="mdi mdi-chevron-down ms-1"></i></span>
                    </DropdownToggle>
                    <DropdownMenu class="dropdown-menu-end" end>
                        <DropdownItem>Today</DropdownItem>
                        <DropdownItem>Weekly</DropdownItem>
                        <DropdownItem>Monthly</DropdownItem>
                        <DropdownItem>Yearly</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </div>
        </div>
        <div lass="card-body pb-0">
            <div id="deal-type-charts" dir="ltr">
                <DealTypeCharts dataColors={["--vz-warning", "--vz-danger", "--vz-success"]} />
            </div>
        </div>
    </Card>
</Col>