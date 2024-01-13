<script>
    import {
        Card,
        CardBody,
        CardHeader,
        Col,
        DropdownItem,
        DropdownMenu,
        DropdownToggle,
        Row,
        Dropdown,
    } from "sveltestrap";
    import data from "../../common/data/dashboardNFT";
    // Import Images
    import usFlag from "../../assets/images/flags/us.svg";
    import russiaFlag from "../../assets/images/flags/russia.svg";
    import spainFlag from "../../assets/images/flags/spain.svg";
    import italyFlag from "../../assets/images/flags/italy.svg";
    import germanyFlag from "../../assets/images/flags/germany.svg";

    // Swiper
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import "swiper/css";
    import "swiper/css/pagination";
    import "swiper/css/navigation";
    import { Pagination, Navigation, Autoplay } from "swiper";
    import Link from "svelte-link";
    import Map from "./WorldWideTopCreatorsMap.svelte";
</script>

<Row>
    <Col xxl={6}>
        <Card>
            <CardHeader class="align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">Recent NFTs</h4>
                <div class="flex-shrink-0">
                    <Dropdown class="card-header-dropdown">
                        <DropdownToggle
                            tag="a"
                            class="text-reset dropdown-btn p-0"
                            role="button"
                            color=""
                        >
                            <span class="fw-semibold text-uppercase fs-12"
                                >Sort by:
                            </span><span class="text-muted"
                                >Popular <i
                                    class="mdi mdi-chevron-down ms-1"
                                /></span
                            >
                        </DropdownToggle>
                        <DropdownMenu class="dropdown-menu-end" end>
                            <DropdownItem href={null}>Popular</DropdownItem>
                            <DropdownItem href={null}>Newest</DropdownItem>
                            <DropdownItem href={null}>Oldest</DropdownItem>
                        </DropdownMenu>
                    </Dropdown>
                </div>
            </CardHeader>
            <CardBody>
                <div class="table-responsive table-card">
                    <table
                        class="table table-borderless table-centered align-middle table-nowrap mb-0"
                    >
                        <thead class="text-muted bg-light-subtle">
                            <tr>
                                <th>Collection</th>
                                <th>Volume</th>
                                <th>24h %</th>
                                <th>Creators</th>
                                <th>Items</th>
                            </tr>
                        </thead>
                        <tbody>
                            {#each data.recentNFTsData as item}
                                <tr>
                                    <td>
                                        <div class="d-flex align-items-center">
                                            <div class="me-2">
                                                <img
                                                    src={item.img}
                                                    alt=""
                                                    class="avatar-xs rounded-circle"
                                                />
                                            </div>
                                            <div class="flex-grow-1">
                                                <h6 class="mb-1">
                                                    <Link
                                                        href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                                        class="text-body"
                                                        >{item.title}</Link
                                                    >
                                                </h6>
                                                <p
                                                    class="text-muted fs-13 mb-0"
                                                >
                                                    {item.category}
                                                </p>
                                            </div>
                                        </div>
                                    </td>
                                    <td
                                        ><img
                                            src={item.icon}
                                            class="avatar-xxs me-2"
                                            alt=""
                                        />{item.volume}</td
                                    >
                                    <td>
                                        <span
                                            class={item.textColor
                                                ? "text-danger mb-0"
                                                : "text-success mb-0"}
                                            ><i
                                                class="mdi mdi-trending-up align-middle me-1"
                                            />{item.hours}
                                        </span>
                                    </td>
                                    <td>{item.creators}</td>
                                    <td>{item.items}</td>
                                </tr>
                            {/each}
                        </tbody>
                    </table>
                </div>
            </CardBody>
        </Card>
    </Col>
    <Col xxl={3} lg={6}>
        <Card class="card-height-100">
            <CardHeader class="align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">
                    Worldwide Top Creators
                </h4>
                <div class="flex-shrink-0">
                    <button type="button" class="btn btn-soft-primary btn-sm">
                        Export Report
                    </button>
                </div>
            </CardHeader>
            <CardBody>
                <div style="height: 265px">
                    <Map
                        dataColor={[
                            "--vz-light",
                            "--vz-success",
                            "--vz-primary",
                        ]}
                    />
                </div>
                <div class="mt-1">
                    <p class="mb-1">
                        <img
                            src={usFlag}
                            alt=""
                            height="15"
                            class="rounded me-2"
                        />
                        United States <span class="float-end">34%</span>
                    </p>
                    <p class="mb-1">
                        <img
                            src={russiaFlag}
                            alt=""
                            height="15"
                            class="rounded me-2"
                        />
                        Russia <span class="float-end">27%</span>
                    </p>
                    <p class="mb-1">
                        <img
                            src={spainFlag}
                            alt=""
                            height="15"
                            class="rounded me-2"
                        />
                        Spain <span class="float-end">21%</span>
                    </p>
                    <p class="mb-1">
                        <img
                            src={italyFlag}
                            alt=""
                            height="15"
                            class="rounded me-2"
                        />
                        Italy <span class="float-end">13%</span>
                    </p>
                    <p class="mb-0">
                        <img
                            src={germanyFlag}
                            alt=""
                            height="15"
                            class="rounded me-2"
                        />
                        Germany <span class="float-end">5%</span>
                    </p>
                </div>
            </CardBody>
        </Card>
    </Col>
    <Col xxl={3} lg={6}>
        <Card>
            <CardHeader class="d-flex align-items-center">
                <h6 class="card-title flex-grow-1 mb-0">Top Collections</h6>
                <Link
                    href="/NFTmarketplace/Collections/apps-nft-collections"
                    type="button"
                    class="btn btn-soft-primary btn-sm flex-shrink-0"
                >
                    See All <i class="ri-arrow-right-line align-bottom" />
                </Link>
            </CardHeader>
            <CardBody>
                <Swiper
                    modules={[Autoplay, Pagination, Navigation]}
                    slidesPerView={1}
                    spaceBetween={10}
                    pagination={{
                        el: ".swiper-pagination",
                        clickable: true,
                    }}
                    navigation={{
                        nextEl: ".swiper-button-next",
                        prevEl: ".swiper-button-prev",
                    }}
                    loop={true}
                    autoplay={{ delay: 2500, disableOnInteraction: false }}
                    class="mySwiper swiper collection-slider"
                >
                    {#each data.topCollectionData as item}
                        <SwiperSlide>
                            <div
                                class="dash-collection overflow-hidden rounded-top position-relative"
                            >
                                <img
                                    src={item.img}
                                    alt=""
                                    height="220"
                                    class="object-fit-cover w-100"
                                />
                                <div
                                    class="content position-absolute bottom-0 m-2 p-2 start-0 end-0 rounded d-flex align-items-center"
                                >
                                    <div class="flex-grow-1">
                                        <Link href={null}>
                                            <h5 class="text-white fs-16 mb-1">
                                                {item.category}
                                            </h5>
                                        </Link>
                                        <p class="text-white-75 mb-0">
                                            {item.items} Items
                                        </p>
                                    </div>
                                    <div class="avatar-xxs">
                                        <div
                                            class="avatar-title bg-white rounded-circle"
                                        >
                                            <Link
                                                href={null}
                                                class="link-success"
                                                ><i
                                                    class="ri-arrow-right-line"
                                                /></Link
                                            >
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </SwiperSlide>
                    {/each}
                </Swiper>
            </CardBody>
        </Card>
        <Card>
            <CardHeader class="d-flex align-items-center">
                <h5 class="card-title flex-grow-1 mb-0">Popular Creators</h5>
                <Link
                    href="/NFTmarketplace/Creators/apps-nft-creators"
                    type="button"
                    class="btn btn-soft-primary btn-sm flex-shrink-0"
                >
                    See All <i class="ri-arrow-right-line align-bottom" />
                </Link>
            </CardHeader>
            <CardBody>
                <Swiper
                    modules={[Autoplay, Pagination, Navigation]}
                    slidesPerView={1}
                    spaceBetween={10}
                    pagination={{
                        el: ".swiper-pagination",
                        clickable: true,
                    }}
                    navigation={{
                        nextEl: ".swiper-button-next",
                        prevEl: ".swiper-button-prev",
                    }}
                    loop={true}
                    autoplay={{ delay: 2500, disableOnInteraction: false }}
                    class="mySwiper swiper collection-slider"
                >
                    {#each data.popularCreatorsData as item}
                        <SwiperSlide>
                            <div class="d-flex">
                                <div class="flex-shink-0">
                                    <img
                                        src={item.img}
                                        alt=""
                                        class="avatar-sm object-cover rounded"
                                    />
                                </div>
                                <div class="ms-3 flex-grow-1">
                                    <Link href="/pages/profile/simple">
                                        <h5 class="mb-1">{item.author}</h5>
                                    </Link>
                                    <p class="text-muted mb-0">
                                        <i
                                            class="mdi mdi-ethereum text-primary fs-14"
                                        />
                                        {item.price}
                                    </p>
                                </div>
                                <div>
                                    <Dropdown class="float-end">
                                        <DropdownToggle
                                            tag="a"
                                            class="btn btn-ghost-primary btn-icon dropdown p-0"
                                            role="button"
                                            color=""
                                        >
                                            <i
                                                class="ri-more-fill align-middle fs-16"
                                            />
                                        </DropdownToggle>
                                        <DropdownMenu
                                            class="dropdown-menu-end"
                                            end
                                        >
                                            <DropdownItem href={null}
                                                >View</DropdownItem
                                            >
                                            <DropdownItem href={null}
                                                >Share</DropdownItem
                                            >
                                            <DropdownItem href={null}
                                                >Report</DropdownItem
                                            >
                                        </DropdownMenu>
                                    </Dropdown>
                                </div>
                            </div>
                        </SwiperSlide>
                    {/each}
                </Swiper>
            </CardBody>
        </Card>
    </Col>
</Row>
