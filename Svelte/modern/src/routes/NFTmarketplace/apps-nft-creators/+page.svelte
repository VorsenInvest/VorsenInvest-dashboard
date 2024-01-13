<svelte:head>
  <title>Creators | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import { Card, CardBody, Col, Container, DropdownItem, DropdownMenu, DropdownToggle, Row, Dropdown } from "sveltestrap";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import Link from "svelte-link";
    import data from "../../../common/data/NFTMarketplace";
    import Select from "svelte-select";
    let sortBy = "All";

    const sortbyname = [
        { label: "All", value: "All" },
        { label: "Today", value: "Today" },
        { label: "Yesterday", value: "Yesterday" },
        { label: "Last 7 Days", value: "Last 7 Days" },
        { label: "Last 30 Days", value: "Last 30 Days" },
        { label: "This Month", value: "This Month" },
        { label: "Last Year", value: "Last Year" },
    ];
</script>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Creators" pageTitle="NFT Marketplace" />
        <Row class="g-4 mb-3">
            <Col class="col-sm-auto">
                <div>
                    <Link href="/projects/apps-projects-create" class="btn btn-success"><i class="ri-add-line align-bottom me-1"></i> Add New</Link>
                </div>
            </Col>
            <Col class="col-sm">
                <div class="d-flex justify-content-sm-end gap-2">
                    <div class="search-box ms-2">
                        <input type="text" class="form-control" placeholder="Search..." />
                        <i class="ri-search-line search-icon"></i>
                    </div>
                    <div class="choices">
                        <Select
                            id="choices-single-default"
                            class="form-control w-md"
                            value={sortBy}
                            items={sortbyname}
                        />
                    </div>
                </div>
            </Col>
        </Row>

        <Row>
            {#each data.creatorsData as item}
                <Col xl={3} lg={4} md={6}>
                    <Card>
                        <CardBody>
                            <div class="d-flex">
                                <div class="flex-shrink-0">
                                    <img src={item.img} alt="" class="avatar-sm object-cover rounded" />
                                </div>
                                <div class="ms-3 flex-grow-1">
                                    <Link href="/pages/profile/simple">
                                        <h5 class="mb-1">{item.title}</h5>
                                    </Link>
                                    <p class="text-muted mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> {item.price}</p>
                                </div>
                                <div>
                                    <Dropdown direction="start" class="float-end">
                                        <DropdownToggle tag="button" class="btn btn-ghost-primary btn-icon" color="">
                                            <i class="ri-more-fill align-middle fs-16"></i>
                                        </DropdownToggle>
                                        <DropdownMenu class="dropdown-menu-end">
                                            <DropdownItem class="view-item-btn">Share</DropdownItem>
                                            <DropdownItem class="edit-item-btn">Report</DropdownItem>
                                        </DropdownMenu>
                                    </Dropdown>
                                </div>
                            </div>
                        </CardBody>
                    </Card>
                </Col>
            {/each}
        </Row>

        <Row>
            <Col lg={12}>
                <h5 class="card-title mb-4 fw-bold fs-17">Creators Grid Lists</h5>
            </Col>
        </Row>

        <Row class="row-cols-xl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
            {#each data.creatorsListData as subitem}
                <Col>
                    <Card>
                        <img src={subitem.cardImg} alt="" class="object-fit-cover card-img-top" height="120" />
                        <div class="card-body text-center">
                            <img src={subitem.img} alt="" class="avatar-md rounded-circle object-cover mt-n5 img-thumbnail border-light mx-auto d-block" />
                            <Link href="/pages/profile/simple">
                                <h5 class="mt-2 mb-1">{subitem.title}</h5>
                            </Link>
                            <p class="text-muted mb-2">{subitem.products} Products</p>
                            <p class="text-muted">You can make an NFT of a digital painting, a text, a piece of music, a video.</p>
                            <button class={subitem.isFollowBtn ? "btn btn-success w-100" : "btn btn-soft-success w-100"}>{subitem.isFollowBtn ? "Follow" : "UnFollow"} </button>
                        </div>
                    </Card>
                </Col>
            {/each}
        </Row>

        <Row class="g-0 text-center text-sm-start align-items-center mb-4">
            <Col sm={6}>
                <div>
                    <p class="mb-sm-0 text-muted">Showing <span class="fw-semibold">1</span> to <span class="fw-semibold">10</span> of <span class="fw-semibold text-decoration-underline">12</span> entries</p>
                </div>
            </Col>

            <Col sm={6}>
                <ul class="pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0">
                    <li class="page-item disabled">
                        <Link href={null} class="page-link">Previous</Link>
                    </li>
                    <li class="page-item active">
                        <Link href={null} class="page-link">1</Link>
                    </li>
                    <li class="page-item ">
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