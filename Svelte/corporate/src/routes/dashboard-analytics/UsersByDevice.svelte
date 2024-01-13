<script>
import { Card, CardHeader, Col, DropdownMenu, DropdownToggle, Dropdown, DropdownItem, CardBody } from 'sveltestrap';
import UsersByDeviceCharts from "./UsersByDeviceCharts.svelte"
import { UsersIcon } from 'svelte-feather-icons'

</script>
<Col xl={4}>
    <Card class="card-height-100">
        <CardHeader class="align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">Users by Device</h4>
            <div class="flex-shrink-0">
                <Dropdown class="card-header-dropdown">
                    <DropdownToggle tag="a" class="text-reset dropdown-btn p-0" color="" role="button">
                        <span class="text-muted fs-16"><i class="mdi mdi-dots-vertical align-middle"></i></span>
                    </DropdownToggle>
                    <DropdownMenu class="dropdown-menu-end" end>
                        <DropdownItem>Today</DropdownItem>
                        <DropdownItem>Last Week</DropdownItem>
                        <DropdownItem>Last Month</DropdownItem>
                        <DropdownItem>Current Year</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </div>
        </CardHeader>
        <CardBody>
            <div dir="ltr">
                <UsersByDeviceCharts dataColors={["--vz-primary", "--vz-secondary", "--vz-success"]} />
            </div>

            <div class="table-responsive mt-3">
                <table class="table table-borderless table-sm table-centered align-middle table-nowrap mb-0">
                    <tbody class="border-0">
                        <tr>
                            <td><h4 class="text-truncate fs-14 fs-medium mb-0"><i class="ri-stop-fill align-middle fs-18 text-primary me-2"></i>Desktop Users</h4></td>
                            <td><p class="text-muted mb-0">
                                <UsersIcon
                                    class="me-2 icon-sm"
                                />
                                78.56k</p></td>
                            <td class="text-end"><p class="text-success fw-medium fs-12 mb-0"><i class="ri-arrow-up-s-fill fs-5 align-middle"></i>2.08%</p></td>
                        </tr>
                        <tr>
                            <td><h4 class="text-truncate fs-14 fs-medium mb-0"><i class="ri-stop-fill align-middle fs-18 text-warning me-2"></i>Mobile Users</h4></td>
                            <td><p class="text-muted mb-0">
                                <UsersIcon
                                    class="me-2 icon-sm"
                                />
                                105.02k</p></td>
                            <td class="text-end"><p class="text-danger fw-medium fs-12 mb-0"><i class="ri-arrow-down-s-fill fs-5 align-middle"></i>10.52%</p></td>
                        </tr>
                        <tr>
                            <td><h4 class="text-truncate fs-14 fs-medium mb-0"><i class="ri-stop-fill align-middle fs-18 text-info me-2"></i>Tablet Users</h4></td>
                            <td><p class="text-muted mb-0">
                                <UsersIcon
                                    class="me-2 icon-sm"
                                />
                                42.89k</p></td>
                            <td class="text-end"><p class="text-danger fw-medium fs-12 mb-0"><i class="ri-arrow-down-s-fill fs-5 align-middle"></i>7.36%</p></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </CardBody>
    </Card>
</Col>