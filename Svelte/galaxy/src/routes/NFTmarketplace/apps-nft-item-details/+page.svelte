<script>
    import { onMount } from "svelte";
    import {
        Card,
        CardBody,
        Col,
        Container,
        DropdownItem,
        DropdownMenu,
        DropdownToggle,
        Nav,
        NavItem,
        NavLink,
        Row,
        TabContent,
        TabPane,
        Dropdown,
    } from "sveltestrap";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import Link from "svelte-link";

    // Import Images
    import Img1 from "../../../assets/images/nft/img-01.jpg";
    import Img2 from "../../../assets/images/nft/img-02.jpg";
    import Img3 from "../../../assets/images/nft/img-03.jpg";
    import Img5 from "../../../assets/images/nft/img-05.jpg";
    import Img6 from "../../../assets/images/nft/img-06.jpg";

    import avatar1 from "../../../assets/images/users/avatar-1.jpg";
    import avatar3 from "../../../assets/images/users/avatar-3.jpg";
    import avatar5 from "../../../assets/images/users/avatar-5.jpg";
    import avatar8 from "../../../assets/images/users/avatar-8.jpg";

    import SImg10 from "../../../assets/images/small/img-10.jpg";
    import SImg11 from "../../../assets/images/small/img-11.jpg";
    import SImg12 from "../../../assets/images/small/img-12.jpg";

    let customActiveTab = 1;

    onMount(() => {
        try {
            var setEndDate1 = "March 19, 2024 6:0:0";

            function startCountDownDate(dateVal) {
                var countDownDate = new Date(dateVal).getTime();
                return countDownDate;
            }

            function countDownTimer(start, targetDOM) {
                // Get todays date and time
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = start - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor(
                    (distance % (1000 * 60 * 60)) / (1000 * 60)
                );
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // add 0 at the beginning if days, hours, minutes, seconds values are less than 10
                days = days < 10 ? "0" + days : days;
                hours = hours < 10 ? "0" + hours : hours;
                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                // Output the result in an element with auction-item-x"
                if (document.querySelector("#" + targetDOM)) {
                    document.querySelector("#" + targetDOM).textContent =
                        days +
                        " : " +
                        hours +
                        " : " +
                        minutes +
                        " : " +
                        seconds;
                }
                // If the count down is over, write some text
                if (distance < 0) {
                    // clearInterval();
                    document.querySelector("#" + targetDOM).textContent =
                        "00 : 00 : 00 : 00";
                }
            }

            var cdd1 = startCountDownDate(setEndDate1);

            if (document.getElementById("auction-time-1"))
                setInterval(function () {
                    countDownTimer(cdd1, "auction-time-1");
                }, 1000);
        } catch (error) {}
    });
</script>

<svelte:head>
    <title>Item Details | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Item Details" pageTitle="NFT Marketplace" />
        <Card>
            <CardBody>
                <Row class="g-4">
                    <Col lg={4}>
                        <div class="sticky-side-div">
                            <Card class="ribbon-box border shadow-none right">
                                <div class="ribbon-two ribbon-two-danger">
                                    <span
                                        ><i class="ri-fire-fill align-bottom" />
                                        Hot</span
                                    >
                                </div>
                                <img
                                    src={Img5}
                                    alt=""
                                    class="img-fluid rounded"
                                />
                                <div class="position-absolute bottom-0 p-3">
                                    <div
                                        class="position-absolute top-0 end-0 start-0 bottom-0 bg-white opacity-25"
                                    />
                                    <Row class="justify-content-center">
                                        <Col class="col-3">
                                            <img
                                                src={Img2}
                                                alt=""
                                                class="img-fluid rounded"
                                            />
                                        </Col>
                                        <Col class="col-3">
                                            <img
                                                src={Img3}
                                                alt=""
                                                class="img-fluid rounded"
                                            />
                                        </Col>
                                        <Col class="col-3">
                                            <img
                                                src="https://img.themesbrand.com/velzon/images/img-3.gif"
                                                alt=""
                                                class="img-fluid rounded h-100 object-cover"
                                            />
                                        </Col>
                                        <Col class="col-3">
                                            <img
                                                src={Img6}
                                                alt=""
                                                class="img-fluid rounded"
                                            />
                                        </Col>
                                    </Row>
                                </div>
                            </Card>
                            <div class="hstack gap-2">
                                <button class="btn btn-primary w-100"
                                    >Place Bid</button
                                >
                            </div>
                        </div>
                    </Col>
                    <Col lg={8}>
                        <div>
                            <Dropdown class="float-end">
                                <DropdownToggle
                                    tag="a"
                                    class="btn btn-ghost-primary btn-icon p-0"
                                    role="button"
                                    color=""
                                >
                                    <i
                                        class="ri-more-fill align-middle fs-16"
                                    />
                                </DropdownToggle>
                                <DropdownMenu class="dropdown-menu-end">
                                    <DropdownItem
                                        href={null}
                                        class="view-item-btn"
                                        ><i
                                            class="ri-eye-fill align-bottom me-2 text-muted"
                                        />View</DropdownItem
                                    >
                                    <DropdownItem
                                        href={null}
                                        class="edit-item-btn"
                                        ><i
                                            class="ri-pencil-fill align-bottom me-2 text-muted"
                                        /> Edit</DropdownItem
                                    >
                                    <DropdownItem
                                        href={null}
                                        class="remove-item-btn"
                                        ><i
                                            class="ri-delete-bin-fill align-bottom me-2 text-muted"
                                        /> Delete</DropdownItem
                                    >
                                </DropdownMenu>
                            </Dropdown>

                            <span
                                class="badge bg-primary-subtle text-primary mb-3 fs-12"
                                ><i class="ri-eye-line me-1 align-bottom" /> 8,634
                                people views this</span
                            >
                            <h4>Patterns Arts & Culture</h4>
                            <div class="hstack gap-3 flex-wrap">
                                <div class="text-muted">
                                    Creators : <Link
                                        href={null}
                                        class="text-primary fw-medium"
                                        >Nancy Martino</Link
                                    >
                                </div>
                                <div class="vr" />
                                <div class="text-muted">
                                    Seller : <span class="text-body fw-medium"
                                        >Rickey Teran</span
                                    >
                                </div>
                                <div class="vr" />
                                <div class="text-muted">
                                    Published : <span
                                        class="text-body fw-medium"
                                        >29 April, 2022</span
                                    >
                                </div>
                            </div>
                            <div
                                class="d-flex flex-wrap gap-2 align-items-center mt-3"
                            >
                                <div class="text-muted fs-16">
                                    <span class="mdi mdi-star text-warning" />
                                    <span class="mdi mdi-star text-warning" />
                                    <span class="mdi mdi-star text-warning" />
                                    <span class="mdi mdi-star text-warning" />
                                    <span class="mdi mdi-star text-warning" />
                                </div>
                                <div class="text-muted">
                                    ( 5.50k Customer Review )
                                </div>
                            </div>
                            <Row class="mt-4">
                                <Col lg={3} sm={6}>
                                    <div
                                        class="p-2 border border-dashed rounded text-center"
                                    >
                                        <div>
                                            <p
                                                class="text-muted fw-medium mb-1"
                                            >
                                                Price :
                                            </p>
                                            <h5 class="fs-17 text-primary mb-0">
                                                <i
                                                    class="mdi mdi-ethereum me-1"
                                                /> 83.06 ETH
                                            </h5>
                                        </div>
                                    </div>
                                </Col>

                                <Col lg={3} sm={6}>
                                    <div
                                        class="p-2 border border-dashed rounded text-center"
                                    >
                                        <div>
                                            <p
                                                class="text-muted fw-medium mb-1"
                                            >
                                                Highest bid
                                            </p>
                                            <h5 class="fs-17 mb-0">
                                                104.63 ETH
                                            </h5>
                                        </div>
                                    </div>
                                </Col>

                                <Col lg={3} sm={6}>
                                    <div
                                        class="p-2 border border-dashed rounded text-center"
                                    >
                                        <div>
                                            <p
                                                class="text-muted fw-medium mb-1"
                                            >
                                                Stock
                                            </p>
                                            <h5 class="fs-17 mb-0">
                                                12/58 Sale
                                            </h5>
                                        </div>
                                    </div>
                                </Col>

                                <Col lg={3} sm={6}>
                                    <div
                                        class="p-2 border border-dashed rounded text-center"
                                    >
                                        <div>
                                            <p
                                                class="text-muted fw-medium mb-1"
                                            >
                                                Auction Ends:
                                            </p>
                                            <!-- svelte-ignore a11y-missing-content -->
                                            <h5
                                                id="auction-time-1"
                                                class="mb-0"
                                            />
                                        </div>
                                    </div>
                                </Col>
                            </Row>
                            <div class="mt-4 text-muted">
                                <h5 class="fs-14">Description :</h5>
                                <p>
                                    Cultural patterns are the similar behaviors
                                    within similar situations we witness due to
                                    shared beliefs, values, norms and social
                                    practices that are steady over time. In art,
                                    a pattern is a repetition of specific visual
                                    elements. The dictionary.com definition of
                                    "pattern" is: an arrangement of repeated or
                                    corresponding parts, decorative motifs, etc.
                                </p>
                            </div>
                            <div class="product-content mt-5">
                                <h5 class="fs-14 mb-3">
                                    Product Description :
                                </h5>

                                <Nav tabs class="nav-tabs-custom nav-primary">
                                    <NavItem>
                                        <NavLink
                                            style="cursor: pointer"
                                            class={customActiveTab == 1
                                                ? "active"
                                                : ""}
                                            on:click={() =>
                                                (customActiveTab = 1)}
                                        >
                                            Place Bids
                                        </NavLink>
                                    </NavItem>
                                    <NavItem>
                                        <NavLink
                                            style="cursor: pointer"
                                            class={customActiveTab == 2
                                                ? "active"
                                                : ""}
                                            on:click={() =>
                                                (customActiveTab = 2)}
                                        >
                                            Additional Information
                                        </NavLink>
                                    </NavItem>
                                    <NavItem>
                                        <NavLink
                                            style="cursor: pointer"
                                            class={customActiveTab == 3
                                                ? "active"
                                                : ""}
                                            on:click={() =>
                                                (customActiveTab = 3)}
                                        >
                                            Details
                                        </NavLink>
                                    </NavItem>
                                </Nav>
                                <TabContent
                                    class="border border-top-0 p-4"
                                    id="nav-tabContent"
                                >
                                    <TabPane
                                        id="nav-speci"
                                        class={customActiveTab == 1
                                            ? "active"
                                            : ""}
                                    >
                                        <div class="table-responsive">
                                            <table
                                                class="table align-middle table-nowrap mb-0"
                                            >
                                                <tbody>
                                                    <tr>
                                                        <th scope="row">
                                                            <div
                                                                class="d-flex align-items-center"
                                                            >
                                                                <img
                                                                    src={Img1}
                                                                    alt=""
                                                                    class="avatar-xs rounded object-cover"
                                                                />
                                                                <Link
                                                                    href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                                                    class="link-body"
                                                                    ><span
                                                                        class="mb-0 ms-2"
                                                                        >Brave
                                                                        Tigers
                                                                        NFT</span
                                                                    ></Link
                                                                >
                                                            </div>
                                                        </th>
                                                        <td>0.235 ETH</td>
                                                        <td>
                                                            <div
                                                                class="d-flex align-items-center"
                                                            >
                                                                <img
                                                                    src={avatar1}
                                                                    alt=""
                                                                    class="avatar-xs rounded object-cover"
                                                                />
                                                                <div
                                                                    class="ms-2"
                                                                >
                                                                    <Link
                                                                        href={null}
                                                                        ><h6
                                                                            class="mb-1"
                                                                        >
                                                                            Alexis
                                                                            Clarke
                                                                        </h6></Link
                                                                    >
                                                                    <p
                                                                        class="text-muted mb-0"
                                                                    >
                                                                        Creators
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </td>
                                                        <td>29 min ago</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">
                                                            <div
                                                                class="d-flex align-items-center"
                                                            >
                                                                <img
                                                                    src={Img3}
                                                                    alt=""
                                                                    class="avatar-xs rounded object-cover"
                                                                />
                                                                <Link
                                                                    href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                                                    class="link-body"
                                                                    ><span
                                                                        class="mb-0 ms-2"
                                                                        >Creative
                                                                        filtered
                                                                        portrait</span
                                                                    ></Link
                                                                >
                                                            </div>
                                                        </th>
                                                        <td>571.24 ETH</td>
                                                        <td>
                                                            <div
                                                                class="d-flex align-items-center"
                                                            >
                                                                <img
                                                                    src={avatar3}
                                                                    alt=""
                                                                    class="avatar-xs rounded object-cover"
                                                                />
                                                                <div
                                                                    class="ms-2"
                                                                >
                                                                    <Link
                                                                        href={null}
                                                                        ><h6
                                                                            class="mb-1"
                                                                        >
                                                                            Glen
                                                                            Matney
                                                                        </h6></Link
                                                                    >
                                                                    <p
                                                                        class="text-muted mb-0"
                                                                    >
                                                                        Creators
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </td>
                                                        <td>37 min ago</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">
                                                            <div
                                                                class="d-flex align-items-center"
                                                            >
                                                                <img
                                                                    src="https://img.themesbrand.com/velzon/images/img-4.gif"
                                                                    alt=""
                                                                    class="avatar-xs rounded object-cover"
                                                                />
                                                                <Link
                                                                    href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                                                    class="link-body"
                                                                    ><span
                                                                        class="mb-0 ms-2"
                                                                        >Evolved
                                                                        Reality</span
                                                                    ></Link
                                                                >
                                                            </div>
                                                        </th>
                                                        <td>130.39 ETH</td>
                                                        <td>
                                                            <div
                                                                class="d-flex align-items-center"
                                                            >
                                                                <img
                                                                    src={avatar5}
                                                                    alt=""
                                                                    class="avatar-xs rounded object-cover"
                                                                />
                                                                <div
                                                                    class="ms-2"
                                                                >
                                                                    <Link
                                                                        href={null}
                                                                        ><h6
                                                                            class="mb-1"
                                                                        >
                                                                            Herbert
                                                                            Stokes
                                                                        </h6></Link
                                                                    >
                                                                    <p
                                                                        class="text-muted mb-0"
                                                                    >
                                                                        Creators
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </td>
                                                        <td>1 hrs ago</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">
                                                            <div
                                                                class="d-flex align-items-center"
                                                            >
                                                                <img
                                                                    src={Img6}
                                                                    alt=""
                                                                    class="avatar-xs rounded object-cover"
                                                                />
                                                                <Link
                                                                    href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                                                    class="link-body"
                                                                    ><span
                                                                        class="mb-0 ms-2"
                                                                        >Robotic
                                                                        Body Art</span
                                                                    ></Link
                                                                >
                                                            </div>
                                                        </th>
                                                        <td>81.72 ETH</td>
                                                        <td>
                                                            <div
                                                                class="d-flex align-items-center"
                                                            >
                                                                <img
                                                                    src={avatar8}
                                                                    alt=""
                                                                    class="avatar-xs rounded object-cover"
                                                                />
                                                                <div
                                                                    class="ms-2"
                                                                >
                                                                    <Link
                                                                        href={null}
                                                                        ><h6
                                                                            class="mb-1"
                                                                        >
                                                                            Michael
                                                                            Morris
                                                                        </h6></Link
                                                                    >
                                                                    <p
                                                                        class="text-muted mb-0"
                                                                    >
                                                                        Creators
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </td>
                                                        <td>1 hrs ago</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </TabPane>
                                    <TabPane
                                        id="nav-detail"
                                        class={customActiveTab == 2
                                            ? "active"
                                            : ""}
                                    >
                                        <div class="table-responsive">
                                            <table class="table mb-0">
                                                <tbody>
                                                    <tr>
                                                        <th
                                                            scope="row"
                                                            style="width: 200px;">Size</th
                                                        >
                                                        <td
                                                            >650 x 650px (66.8
                                                            KB)</td
                                                        >
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"
                                                        style="width: 200px;"
                                                            >Brand</th
                                                        >
                                                        <td
                                                            >Patterns arts &
                                                            culture
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"
                                                        style="width: 200px;"
                                                            >Formats</th
                                                        >
                                                        <td>JPEG / PNG / PDF</td
                                                        >
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"
                                                        style="width: 200px;"
                                                            >Token</th
                                                        >
                                                        <td>VLZ74516523</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"
                                                        style="width: 200px;"
                                                            >Blockchain</th
                                                        >
                                                        <td>Ethereum</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"
                                                        style="width: 200px;"
                                                            >Contacts</th
                                                        >
                                                        <td
                                                            >E545D145S5646544DS541SFDB213C5Z</td
                                                        >
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </TabPane>
                                    <TabPane
                                        id="nav-detail"
                                        class={customActiveTab == 3
                                            ? "active"
                                            : ""}
                                    >
                                        <div>
                                            <h5 class="font-size-16 mb-3">
                                                Patterns arts & culture
                                            </h5>
                                            <p>
                                                Cultural patterns are the
                                                similar behaviors within similar
                                                situations we witness due to
                                                shared beliefs, values, norms
                                                and social practices that are
                                                steady over time. In art, a
                                                pattern is a repetition of
                                                specific visual elements. The
                                                dictionary.com definition of
                                                "pattern" is: an arrangement of
                                                repeated or corresponding parts,
                                                decorative motifs, etc.
                                            </p>
                                            <div>
                                                <p class="mb-2">
                                                    <i
                                                        class="mdi mdi-circle-medium me-1 text-muted align-middle"
                                                    /> On digital or printed media
                                                </p>
                                                <p class="mb-2">
                                                    <i
                                                        class="mdi mdi-circle-medium me-1 text-muted align-middle"
                                                    /> For commercial and personal
                                                    projects
                                                </p>
                                                <p class="mb-2">
                                                    <i
                                                        class="mdi mdi-circle-medium me-1 text-muted align-middle"
                                                    /> From anywhere in the world
                                                </p>
                                                <p class="mb-0">
                                                    <i
                                                        class="mdi mdi-circle-medium me-1 text-muted align-middle"
                                                    /> Full copyrights sale
                                                </p>
                                            </div>
                                        </div>
                                    </TabPane>
                                </TabContent>
                            </div>
                            <div class="mt-5">
                                <div>
                                    <h5 class="fs-14 mb-3">
                                        Ratings & Reviews
                                    </h5>
                                </div>
                                <Row class="gy-4 gx-0">
                                    <Col lg={4}>
                                        <div>
                                            <div class="pb-3">
                                                <div
                                                    class="bg-light px-3 py-2 rounded-2 mb-2"
                                                >
                                                    <div
                                                        class="d-flex align-items-center"
                                                    >
                                                        <div
                                                            class="flex-grow-1"
                                                        >
                                                            <div
                                                                class="fs-16 align-middle text-warning"
                                                            >
                                                                <i
                                                                    class="ri-star-fill"
                                                                />
                                                                <i
                                                                    class="ri-star-fill"
                                                                />
                                                                <i
                                                                    class="ri-star-fill"
                                                                />
                                                                <i
                                                                    class="ri-star-fill"
                                                                />
                                                                <i
                                                                    class="ri-star-half-fill"
                                                                />
                                                            </div>
                                                        </div>
                                                        <div
                                                            class="flex-shrink-0"
                                                        >
                                                            <h6 class="mb-0">
                                                                4.8 out of 5
                                                            </h6>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="text-center">
                                                    <div class="text-muted">
                                                        Total <span
                                                            class="fw-medium"
                                                            >7.32k</span
                                                        > reviews
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="mt-3">
                                                <Row
                                                    class="align-items-center g-2"
                                                >
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6 class="mb-0">
                                                                5 star
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                    <Col>
                                                        <div class="p-2">
                                                            <div
                                                                class="progress animated-progress progress-sm"
                                                            >
                                                                <div
                                                                    class="progress-bar bg-priamry"
                                                                    role="progressbar"
                                                                    style="width: 50.16%"
                                                                    aria-valuenow="50.16"
                                                                    aria-valuemin="0"
                                                                    aria-valuemax="100"
                                                                />
                                                            </div>
                                                        </div>
                                                    </Col>
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6
                                                                class="mb-0 text-muted"
                                                            >
                                                                2758
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                </Row>

                                                <Row
                                                    class="align-items-center g-2"
                                                >
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6 class="mb-0">
                                                                4 star
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                    <Col>
                                                        <div class="p-2">
                                                            <div
                                                                class="progress animated-progress progress-sm"
                                                            >
                                                                <div
                                                                    class="progress-bar bg-priamry"
                                                                    role="progressbar"
                                                                    style="width: 19.32%"
                                                                    aria-valuenow="19.32"
                                                                    aria-valuemin="0"
                                                                    aria-valuemax="100"
                                                                />
                                                            </div>
                                                        </div>
                                                    </Col>
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6
                                                                class="mb-0 text-muted"
                                                            >
                                                                1063
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                </Row>

                                                <Row
                                                    class="align-items-center g-2"
                                                >
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6 class="mb-0">
                                                                3 star
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                    <Col>
                                                        <div class="p-2">
                                                            <div
                                                                class="progress animated-progress progress-sm"
                                                            >
                                                                <div
                                                                    class="progress-bar bg-success"
                                                                    role="progressbar"
                                                                    style="width: 18.12%"
                                                                    aria-valuenow="18.12"
                                                                    aria-valuemin="0"
                                                                    aria-valuemax="100"
                                                                />
                                                            </div>
                                                        </div>
                                                    </Col>
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6
                                                                class="mb-0 text-muted"
                                                            >
                                                                997
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                </Row>

                                                <Row
                                                    class="align-items-center g-2"
                                                >
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6 class="mb-0">
                                                                2 star
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                    <Col>
                                                        <div class="p-2">
                                                            <div
                                                                class="progress animated-progress progress-sm"
                                                            >
                                                                <div
                                                                    class="progress-bar bg-warning"
                                                                    role="progressbar"
                                                                    style="width: 7.42%"
                                                                    aria-valuenow="7.42"
                                                                    aria-valuemin="0"
                                                                    aria-valuemax="100"
                                                                />
                                                            </div>
                                                        </div>
                                                    </Col>

                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6
                                                                class="mb-0 text-muted"
                                                            >
                                                                408
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                </Row>

                                                <Row
                                                    class="align-items-center g-2"
                                                >
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6 class="mb-0">
                                                                1 star
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                    <Col>
                                                        <div class="p-2">
                                                            <div
                                                                class="progress animated-progress progress-sm"
                                                            >
                                                                <div
                                                                    class="progress-bar bg-danger"
                                                                    role="progressbar"
                                                                    style="width: 4.98%"
                                                                    aria-valuenow="4.98"
                                                                    aria-valuemin="0"
                                                                    aria-valuemax="100"
                                                                />
                                                            </div>
                                                        </div>
                                                    </Col>
                                                    <Col class="col-auto">
                                                        <div class="p-2">
                                                            <h6
                                                                class="mb-0 text-muted"
                                                            >
                                                                274
                                                            </h6>
                                                        </div>
                                                    </Col>
                                                </Row>
                                            </div>
                                        </div>
                                    </Col>

                                    <Col lg={8}>
                                        <div class="ps-lg-4">
                                            <div
                                                class="d-flex flex-wrap align-items-start gap-3"
                                            >
                                                <h5 class="fs-14">Reviews:</h5>
                                            </div>

                                            <div
                                                class="me-lg-n3 pe-lg-4"
                                                data-simplebar
                                                style="max-height: 225px;"
                                            >
                                                <ul class="list-unstyled mb-0">
                                                    <li class="py-2">
                                                        <div
                                                            class="border border-dashed rounded p-3"
                                                        >
                                                            <div
                                                                class="d-flex align-items-start mb-3"
                                                            >
                                                                <div
                                                                    class="hstack gap-3"
                                                                >
                                                                    <div
                                                                        class="text-warning"
                                                                    >
                                                                        <i
                                                                            class="mdi mdi-star"
                                                                        />
                                                                        <i
                                                                            class="mdi mdi-star"
                                                                        />
                                                                        <i
                                                                            class="mdi mdi-star"
                                                                        />
                                                                        <i
                                                                            class="mdi mdi-star"
                                                                        />
                                                                        <i
                                                                            class="mdi mdi-star"
                                                                        />
                                                                    </div>
                                                                    <div
                                                                        class="vr"
                                                                    />
                                                                    <div
                                                                        class="flex-grow-1"
                                                                    >
                                                                        <h6
                                                                            class="mb-0"
                                                                        >
                                                                            Superb
                                                                            Artwork
                                                                        </h6>
                                                                    </div>
                                                                </div>
                                                            </div>

                                                            <div
                                                                class="d-flex flex-grow-1 gap-2 mb-3"
                                                            >
                                                                <Link
                                                                    href={null}
                                                                    class="d-block"
                                                                >
                                                                    <img
                                                                        src={SImg12}
                                                                        alt=""
                                                                        class="avatar-sm rounded object-fit-cover"
                                                                    />
                                                                </Link>
                                                                <Link
                                                                    href={null}
                                                                    class="d-block"
                                                                >
                                                                    <img
                                                                        src={SImg11}
                                                                        alt=""
                                                                        class="avatar-sm rounded object-fit-cover"
                                                                    />
                                                                </Link>
                                                                <Link
                                                                    href={null}
                                                                    class="d-block"
                                                                >
                                                                    <img
                                                                        src={SImg10}
                                                                        alt=""
                                                                        class="avatar-sm rounded object-fit-cover"
                                                                    />
                                                                </Link>
                                                            </div>

                                                            <div
                                                                class="d-flex align-items-end"
                                                            >
                                                                <div
                                                                    class="flex-grow-1"
                                                                >
                                                                    <h5
                                                                        class="fs-14 mb-0"
                                                                    >
                                                                        Henry
                                                                    </h5>
                                                                </div>

                                                                <div
                                                                    class="flex-shrink-0"
                                                                >
                                                                    <p
                                                                        class="text-muted fs-13 mb-0"
                                                                    >
                                                                        12 Jul,
                                                                        21
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </li>
                                                    <li class="py-2">
                                                        <div
                                                            class="border border-dashed rounded p-3"
                                                        >
                                                            <div
                                                                class="d-flex align-items-start mb-3"
                                                            >
                                                                <div
                                                                    class="hstack gap-3"
                                                                >
                                                                    <div
                                                                        class="badge rounded-pill bg-success mb-0"
                                                                    >
                                                                        <i
                                                                            class="mdi mdi-star"
                                                                        /> 4.0
                                                                    </div>
                                                                    <div
                                                                        class="vr"
                                                                    />
                                                                    <div
                                                                        class="flex-grow-1"
                                                                    >
                                                                        <p
                                                                            class="text-muted mb-0"
                                                                        >
                                                                            Great
                                                                            at
                                                                            this
                                                                            price,
                                                                            Product
                                                                            quality
                                                                            and
                                                                            look
                                                                            is
                                                                            awesome.
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div
                                                                class="d-flex align-items-end"
                                                            >
                                                                <div
                                                                    class="flex-grow-1"
                                                                >
                                                                    <h5
                                                                        class="fs-14 mb-0"
                                                                    >
                                                                        Nancy
                                                                    </h5>
                                                                </div>

                                                                <div
                                                                    class="flex-shrink-0"
                                                                >
                                                                    <p
                                                                        class="text-muted fs-13 mb-0"
                                                                    >
                                                                        06 Jul,
                                                                        21
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </li>
                                                    <li class="py-2">
                                                        <div
                                                            class="border border-dashed rounded p-3"
                                                        >
                                                            <div
                                                                class="d-flex align-items-start mb-3"
                                                            >
                                                                <div
                                                                    class="hstack gap-3"
                                                                >
                                                                    <div
                                                                        class="badge rounded-pill bg-success mb-0"
                                                                    >
                                                                        <i
                                                                            class="mdi mdi-star"
                                                                        /> 4.2
                                                                    </div>
                                                                    <div
                                                                        class="vr"
                                                                    />
                                                                    <div
                                                                        class="flex-grow-1"
                                                                    >
                                                                        <p
                                                                            class="text-muted mb-0"
                                                                        >
                                                                            Good
                                                                            product.
                                                                            I am
                                                                            so
                                                                            happy.
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div
                                                                class="d-flex align-items-end"
                                                            >
                                                                <div
                                                                    class="flex-grow-1"
                                                                >
                                                                    <h5
                                                                        class="fs-14 mb-0"
                                                                    >
                                                                        Joseph
                                                                    </h5>
                                                                </div>

                                                                <div
                                                                    class="flex-shrink-0"
                                                                >
                                                                    <p
                                                                        class="text-muted fs-13 mb-0"
                                                                    >
                                                                        06 Jul,
                                                                        21
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </li>
                                                    <li class="py-2">
                                                        <div
                                                            class="border border-dashed rounded p-3"
                                                        >
                                                            <div
                                                                class="d-flex align-items-start mb-3"
                                                            >
                                                                <div
                                                                    class="hstack gap-3"
                                                                >
                                                                    <div
                                                                        class="badge rounded-pill bg-success mb-0"
                                                                    >
                                                                        <i
                                                                            class="mdi mdi-star"
                                                                        /> 4.1
                                                                    </div>
                                                                    <div
                                                                        class="vr"
                                                                    />
                                                                    <div
                                                                        class="flex-grow-1"
                                                                    >
                                                                        <p
                                                                            class="text-muted mb-0"
                                                                        >
                                                                            Nice
                                                                            Product,
                                                                            Good
                                                                            Quality.
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                            <div
                                                                class="d-flex align-items-end"
                                                            >
                                                                <div
                                                                    class="flex-grow-1"
                                                                >
                                                                    <h5
                                                                        class="fs-14 mb-0"
                                                                    >
                                                                        Jimmy
                                                                    </h5>
                                                                </div>

                                                                <div
                                                                    class="flex-shrink-0"
                                                                >
                                                                    <p
                                                                        class="text-muted fs-13 mb-0"
                                                                    >
                                                                        24 Jun,
                                                                        21
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </Col>
                                </Row>
                            </div>
                        </div>
                    </Col>
                </Row>
            </CardBody>
        </Card>
    </Container>
</div>
