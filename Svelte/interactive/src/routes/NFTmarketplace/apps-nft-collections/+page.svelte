<script>
    import { Card, CardBody, Col, Container, Row } from "sveltestrap";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import Link from "svelte-link";
    import data from "../../../common/data/NFTMarketplace";
</script>

<svelte:head>
    <title>Collections | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Collections" pageTitle="NFT Marketplace" />
        <Row class="g-4 mb-3 align-items-center">
            <Col class="col-sm-auto">
                <div>
                    <h5 class="mb-0">Top Collections</h5>
                </div>
            </Col>
            <Col class="col-sm">
                <div class="d-flex justify-content-sm-end gap-2">
                    <div class="search-box ms-2">
                        <input
                            type="text"
                            class="form-control"
                            placeholder="Search..."
                        />
                        <i class="ri-search-line search-icon" />
                    </div>
                    <div class="choices">
                        <select class="form-control w-md">
                            <option value="All">All</option>
                            <option value="Today" defaultValue>Today</option>
                            <option value="Yesterday">Yesterday</option>
                            <option value="Last 7 Days">Last 7 Days</option>
                            <option value="Last 30 Days">Last 30 Days</option>
                            <option value="This Month">This Month</option>
                            <option value="Last Year">Last Year</option>
                        </select>
                    </div>
                </div>
            </Col>
        </Row>

        <Row>
            {#each data.topCollection as item}
                <Col class="col-xl-3 col-md-4 col-sm-6">
                    <Card>
                        <CardBody>
                            <Row class="g-1 mb-3">
                                {#each item.subItem as subitem}
                                    <div class="col-6">
                                        {#each subitem.isChildren as subsubitem}
                                            <img
                                                src={subsubitem.img}
                                                alt=""
                                                class={"img-fluid rounded " +
                                                    subsubitem.imgClass}
                                            />
                                        {/each}
                                    </div>
                                {/each}
                            </Row>
                            <Link href={null} class="float-end">
                                View All <i
                                    class="ri-arrow-right-line align-bottom"
                                /></Link
                            >
                            <h5 class="mb-0 fs-16">
                                <Link href={null} class="text-body"
                                    >{item.category}
                                    <span
                                        class="badge bg-success-subtle text-success"
                                        >{item.quantity}</span
                                    ></Link
                                >
                            </h5>
                        </CardBody>
                    </Card>
                </Col>
            {/each}
        </Row>

        <Row class="g-0 text-center text-sm-start align-items-center mb-4">
            <Col sm={6}>
                <div>
                    <p class="mb-sm-0 text-muted">
                        Showing <span class="fw-semibold">1</span> to
                        <span class="fw-semibold">8</span>
                        of
                        <span class="fw-semibold text-decoration-underline"
                            >12</span
                        > entries
                    </p>
                </div>
            </Col>

            <Col sm={6}>
                <ul
                    class="pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0"
                >
                    <li class="page-item disabled">
                        <Link href={null} class="page-link">Previous</Link>
                    </li>
                    <li class="page-item active">
                        <Link href={null} class="page-link">1</Link>
                    </li>
                    <li class="page-item">
                        <Link href={null} class="page-link">2</Link>
                    </li>
                    <li class="page-item">
                        <Link href={null} class="page-link">3</Link>
                    </li>
                    <li class="page-item">
                        <Link href={null} class="page-link">4</Link>
                    </li>
                    <li class="page-item">
                        <Link href={null} class="page-link">5</Link>
                    </li>
                    <li class="page-item">
                        <Link href={null} class="page-link">Next</Link>
                    </li>
                </ul>
            </Col>
        </Row>
    </Container>
</div>
