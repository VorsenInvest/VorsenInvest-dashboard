<svelte:head>
  <title>Explore Now | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import {Card,CardBody,CardHeader,Col,Container,DropdownItem,DropdownMenu,DropdownToggle,Row,Collapse,Dropdown} from "sveltestrap";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import Link from "svelte-link";
    import data from '../../../common/data/NFTMarketplace'
    import RangeSlider from "svelte-range-slider-pips";
    let isOpen = true;
</script>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Explore Now" pageTitle="NFT Marketplace" />
        <Row>
            <Col lg={12}>
                <Card>
                    <CardHeader class="border-0">
                        <div class="d-flex align-items-center">
                            <h5 class="card-title mb-0 flex-grow-1">
                                Explore Product
                            </h5>
                            <div>
                                <Link
                                    class="btn btn-success"
                                    id="filtercollapse"
                                    data-bs-toggle="collapse"
                                    href="#collapseExample"
                                    on:click={() => (isOpen = !isOpen)}
                                >
                                    <i class="ri-filter-2-line align-bottom"></i>
                                    Filters
                                </Link>
                            </div>
                        </div>

                        <Collapse {isOpen}>
                            <Row class="row-cols-xxl-5 row-cols-lg-3 row-cols-md-2 row-cols-1 mt-3 g-3">
                                <Col>
                                    <h6 class="text-uppercase fs-12 mb-2">Search</h6>

                                    <input
                                        type="text"
                                        class="form-control"
                                        placeholder="Search product name"
                                        autoComplete="off"
                                        id="searchProductList"
                                    />
                                </Col>
                                <Col>
                                    <h6 class="text-uppercase fs-12 mb-2">
                                        Select Category
                                    </h6>
                                    <select
                                        class="form-control"
                                        data-choices
                                        name="select-category"
                                        data-choices-search-false
                                        id="select-category"
                                    >
                                        <option value="">Select Category</option>
                                        <option value="Artwork">Artwork</option>
                                        <option value="3d Style">3d Style</option>
                                        <option value="Photography">Photography</option>
                                        <option value="Collectibles">Collectibles</option>
                                        <option value="Crypto Card">Crypto Card</option>
                                        <option value="Games">Games</option>
                                        <option value="Music">Music</option>
                                    </select>
                                </Col>
                                <Col>
                                    <h6 class="text-uppercase fs-12 mb-2">File Type</h6>
                                    <select
                                        class="form-control"
                                        data-choices
                                        name="file-type"
                                        data-choices-search-false
                                        id="file-type"
                                    >
                                        <option value="">File Type</option>
                                        <option value="jpg">Images</option>
                                        <option value="mp4">Video</option>
                                        <option value="mp3">Audio</option>
                                        <option value="gif">Gif</option>
                                    </select>
                                </Col>
                                <Col>
                                    <h6 class="text-uppercase fs-12 mb-2">
                                        Sales Type
                                    </h6>
                                    <select
                                        class="form-control"
                                        data-choices
                                        name="all-sales-type"
                                        data-choices-search-false
                                        id="all-sales-type"
                                    >
                                        <option value="">All Sales Type</option>
                                        <option value="On Auction">On Auction</option>
                                        <option value="Has Offers">Has Offers</option>
                                    </select>
                                </Col>
                                <Col>
                                    <h6 class="text-uppercase fs-12 mb-4">Price</h6>

                                    <RangeSlider float step={10}  min={0} max={2000} range values={[0,1000]} hoverable />
                                </Col>
                            </Row>
                        </Collapse>
                    </CardHeader>
                </Card>
            </Col>
            <Col lg={12}>
                <div class="d-flex align-items-center mb-4">
                    <div class="flex-grow-1">
                        <p class="text-muted fs-14 mb-0">Result: 8745</p>
                    </div>
                    <div class="flex-shrink-0">
                        <Dropdown>
                            <DropdownToggle
                                tag="a"
                                class="text-muted fs-14" color=""
                            >
                                All View <i class="mdi mdi-chevron-down"></i>
                            </DropdownToggle>
                            <DropdownMenu class="dropdown-menu-end">
                                <DropdownItem href={null}>Action</DropdownItem>
                                <DropdownItem href={null}>Another action</DropdownItem>
                                <DropdownItem href={null}>Something else here</DropdownItem>
                            </DropdownMenu>
                        </Dropdown>
                    </div>
                </div>
            </Col>
        </Row>
        <Row class="row-cols-xxl-5 row-cols-xl-4 row-cols-lg-3 row-cols-md-2 row-cols-1" id="explorecard-list">
            {#each data.expolreNow as item}
                <Col class="list-element">
                    <Card class="explore-box card-animate">
                        <div class="explore-place-bid-img">
                            <input type="hidden" class="form-control" id="1" />
                            <div class="d-none">undefined</div>
                            <img
                                src={item.img}
                                alt=""
                                class="card-img-top explore-img"
                            />
                            <div class="bg-overlay"></div>
                            <div class="place-bid-btn">

                                <Link href={null} class="btn btn-success">
                                    <i class="ri-auction-fill align-bottom me-1"></i> Place
                                    Bid
                                </Link>
                            </div>
                        </div>
                        <div class="bookmark-icon position-absolute top-0 end-0 p-2">

                            <button
                                type="button"
                                class={item.isActive ? "btn btn-icon active" : "btn btn-icon"}
                                data-bs-toggle="button"
                                aria-pressed="true"
                            >
                                <i class="mdi mdi-cards-heart fs-16"></i>
                            </button>
                        </div>
                        <CardBody>

                            <p class="fw-medium mb-0 float-end">
                                <i class="mdi mdi-heart text-danger align-middle"></i>{" "}
                                {item.likes}k
                            </p>
                            <h5 class="mb-1">
                                <Link href="/NFTmarketplace/Itemdetails/apps-nft-item-details">{item.title}</Link>
                            </h5>
                            <p class="text-muted mb-0">{item.category}</p>
                        </CardBody>
                        <div class="card-footer border-top border-top-dashed">
                            <div class="d-flex align-items-center">
                                <div class="flex-grow-1 fs-14">

                                    <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i>
                                    Highest: <span class="fw-medium">{item.highestBid}ETH</span>
                                </div>
                                <h5 class="flex-shrink-0 fs-14 text-primary mb-0">
                                    {item.price}ETH
                                </h5>
                            </div>
                        </div>
                    </Card>
                </Col>
            {/each}
        </Row>
        <div
            class="py-4 text-center"
            id="noresult"
            style="display: none"
        >
            <lord-icon
                src="https://cdn.lordicon.com/msoeawqm.json"
                trigger="loop"
                colors="primary:#405189,secondary:#0ab39c"
                style="width: 72px; height: 72px;"
            ></lord-icon>
            <h5 class="mt-4">Sorry! No Result Found</h5>
        </div>
        <div class="text-center mb-3">
            <button class="btn btn-link text-success mt-2 material-shadow-none" id="loadmore">
                <i class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"></i>
                Load More
            </button>
        </div>
    </Container>
</div>