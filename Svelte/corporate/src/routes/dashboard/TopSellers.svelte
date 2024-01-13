<script>
    import {
        Card,
        CardBody,
        CardHeader,
        Col,
        DropdownItem,
        DropdownMenu,
        DropdownToggle,
        Dropdown,
    } from "sveltestrap";
    import data from "../../common/data/dashboardEcommerce";
</script>

<Col xl={6}>
    <Card class="card-height-100">
        <CardHeader class="align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">Top Sellers</h4>
            <div class="flex-shrink-0">
                <Dropdown class="card-header-dropdown">
                    <DropdownToggle
                        tag="a"
                        color=""
                        class="text-reset dropdown-btn p-0"
                        role="button"
                    >
                        <span class="text-muted"
                            >Report<i class="mdi mdi-chevron-down ms-1" /></span
                        >
                    </DropdownToggle>
                    <DropdownMenu class="dropdown-menu dropdown-menu-end" end>
                        <DropdownItem>Download Report</DropdownItem>
                        <DropdownItem>Export</DropdownItem>
                        <DropdownItem>Import</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </div>
        </CardHeader>

        <CardBody>
            <div class="table-responsive table-card">
                <table
                    class="table table-centered table-hover align-middle table-nowrap mb-0"
                >
                    <tbody>
                        {#each data.topSellers as item}
                            <tr>
                                <td>
                                    <div class="d-flex align-items-center">
                                        <div class="flex-shrink-0 me-2">
                                            <img
                                                src={item.img}
                                                alt=""
                                                class="avatar-sm p-2"
                                            />
                                        </div>
                                        <div>
                                            <h5 class="fs-14 my-1 fw-medium">
                                                <a
                                                    href="/ecommerce/apps-ecommerce-seller-details"
                                                    class="text-reset"
                                                    >{item.label}</a
                                                >
                                            </h5>
                                            <span class="text-muted"
                                                >{item.name}</span
                                            >
                                        </div>
                                    </div>
                                </td>
                                <td>
                                    <span class="text-muted"
                                        >{item.product}</span
                                    >
                                </td>
                                <td>
                                    <p class="mb-0">{item.stock}</p>
                                    <span class="text-muted">Stock</span>
                                </td>
                                <td>
                                    <span class="text-muted"
                                        >${item.amount}</span
                                    >
                                </td>
                                <td>
                                    <h5 class="fs-14 mb-0">
                                        {item.percentage}%<i
                                            class="ri-bar-chart-fill text-success fs-16 align-middle ms-2"
                                        />
                                    </h5>
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
            <div class="align-items-center mt-4 pt-2 justify-content-between d-flex">
                <div class="flex-shrink-0">
                    <div class="text-muted">
                        Showing <span class="fw-semibold">5</span> of <span class="fw-semibold">25</span> Results
                    </div>
                </div>
                <ul class="pagination pagination-separated pagination-sm mb-0">
                    <li class="page-item disabled">
                        <a href="!#" class="page-link">←</a>
                    </li>
                    <li class="page-item">
                        <a href="!#" class="page-link">1</a>
                    </li>
                    <li class="page-item active">
                        <a href="!#" class="page-link">2</a>
                    </li>
                    <li class="page-item">
                        <a href="!#" class="page-link">3</a>
                    </li>
                    <li class="page-item">
                        <a href="!#" class="page-link">→</a>
                    </li>
                </ul>
            </div>
        </CardBody>
    </Card>
</Col>
