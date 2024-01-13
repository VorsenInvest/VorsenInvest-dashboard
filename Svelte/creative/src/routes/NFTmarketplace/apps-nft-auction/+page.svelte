<script>
    import {
        Card,
        CardBody,
        CardHeader,
        Col,
        Container,
        Row,
    } from "sveltestrap";
    import { onMount } from "svelte";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import Link from "svelte-link";

    import data from "../../../common/data/NFTMarketplace";
    var displayCategory = "All";

    function setCategory(category) {
        displayCategory = category;
    }

    onMount(() => {
        try {
            var setEndDate1 = "March 19, 2024 6:0:0";
            var setEndDate2 = "April 16, 2024 5:3:1";
            var setEndDate3 = "Dec 01, 2024 1:0:1";
            var setEndDate4 = "Nov 26, 2024 1:2:1";
            var setEndDate5 = "May 27, 2024 1:6:6";
            var setEndDate6 = "May 20, 2024 2:5:5";
            var setEndDate7 = "June 10, 2024 5:1:4";
            var setEndDate8 = "June 25, 2024 1:6:3";
            var setEndDate9 = "July 08, 2024 1:5:2";

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
            var cdd2 = startCountDownDate(setEndDate2);
            var cdd3 = startCountDownDate(setEndDate3);
            var cdd4 = startCountDownDate(setEndDate4);
            var cdd5 = startCountDownDate(setEndDate5);
            var cdd6 = startCountDownDate(setEndDate6);
            var cdd7 = startCountDownDate(setEndDate7);
            var cdd8 = startCountDownDate(setEndDate8);
            var cdd9 = startCountDownDate(setEndDate9);

            if (document.getElementById("auction-time-1"))
                setInterval(function () {
                    countDownTimer(cdd1, "auction-time-1");
                }, 1000);
            if (document.getElementById("auction-time-2"))
                setInterval(function () {
                    countDownTimer(cdd2, "auction-time-2");
                }, 1000);
            if (document.getElementById("auction-time-3"))
                setInterval(function () {
                    countDownTimer(cdd3, "auction-time-3");
                }, 1000);
            if (document.getElementById("auction-time-4"))
                setInterval(function () {
                    countDownTimer(cdd4, "auction-time-4");
                }, 1000);
            if (document.getElementById("auction-time-5"))
                setInterval(function () {
                    countDownTimer(cdd5, "auction-time-5");
                }, 1000);
            if (document.getElementById("auction-time-6"))
                setInterval(function () {
                    countDownTimer(cdd6, "auction-time-6");
                }, 1000);
            if (document.getElementById("auction-time-7"))
                setInterval(function () {
                    countDownTimer(cdd7, "auction-time-7");
                }, 1000);
            if (document.getElementById("auction-time-8"))
                setInterval(function () {
                    countDownTimer(cdd8, "auction-time-8");
                }, 1000);
            if (document.getElementById("auction-time-9"))
                setInterval(function () {
                    countDownTimer(cdd9, "auction-time-9");
                }, 1000);
        } catch (error) {}
    });
</script>

<svelte:head>
    <title>Live Auction | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Live Auction" pageTitle="NFT Marketplace" />
        <Row>
            <Col xxl={9}>
                <Card>
                    <CardHeader class="border-0">
                        <div class="d-lg-flex align-items-center">
                            <div class="flex-grow-1">
                                <h5 class="card-title fw-bold mb-0">Live Auction</h5>
                            </div>

                            <div class="flex-shrink-0 mt-4 mt-lg-0">
                                <ul
                                    class="nav nav-pills filter-btns"
                                    role="tablist"
                                >
                                    <li class="nav-item" role="presentation">
                                        <button
                                            type="button"
                                            data-filter="all"
                                            on:click={() => setCategory("All")}
                                            class={displayCategory === "All"
                                                ? "nav-link fw-medium active"
                                                : "nav-link fw-medium"}
                                            >All Items</button
                                        >
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button
                                            type="button"
                                            data-filter="upto-15"
                                            on:click={() =>
                                                setCategory("upto-15")}
                                            class={displayCategory === "upto-15"
                                                ? "nav-link fw-medium active"
                                                : "nav-link fw-medium"}
                                            >Up to 15%</button
                                        >
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button
                                            type="button"
                                            data-filter="upto-30"
                                            on:click={() =>
                                                setCategory("upto-30")}
                                            class={displayCategory === "upto-30"
                                                ? "nav-link fw-medium active"
                                                : "nav-link fw-medium"}
                                            >Up to 30%</button
                                        >
                                    </li>
                                    <li class="nav-item" role="presentation">
                                        <button
                                            type="button"
                                            data-filter="upto-40"
                                            on:click={() =>
                                                setCategory("upto-40")}
                                            class={displayCategory === "upto-40"
                                                ? "nav-link fw-medium active"
                                                : "nav-link fw-medium"}
                                            >Up to 40%</button
                                        >
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </CardHeader>
                </Card>
                <Row>
                    {#each data.aution as item}
                        <Col xxl={3} lg={4} md={6} class="product-item upto-15">
                            <Card class="explore-box card-animate">
                                <div
                                    class="position-relative rounded overflow-hidden"
                                >
                                    <img
                                        src={item.img}
                                        alt=""
                                        class="card-img-top explore-img"
                                    />
                                    <div class="discount-time">
                                        <!-- svelte-ignore a11y-missing-content -->
                                        <h5
                                            id={"auction-time-" + item.id}
                                            class="mb-0 text-white"
                                        />
                                    </div>
                                </div>
                                <CardBody>
                                    <p class="fw-medium mb-0 float-end">
                                        <i
                                            class="mdi mdi-heart text-danger align-middle"
                                        />
                                        {item.likes}k
                                    </p>
                                    <h5 class="text-success">
                                        <i class="mdi mdi-ethereum" />
                                        {item.price} ETH
                                    </h5>
                                    <h6 class="fs-16 mb-3">
                                        <Link  class="text-body"
                                            href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                            >{item.title}</Link
                                        >
                                    </h6>
                                    <div>
                                        <span class="text-muted float-end"
                                            >Available: {item.available}</span
                                        >
                                        <span class="text-muted"
                                            >Sold: {item.sold}</span
                                        >
                                        <div class="progress progress-sm mt-2">
                                            <div
                                                class={"progress-bar progress-bar-striped bg-" +
                                                    item.progressClass}
                                                role="progressbar"
                                                style="width: {item.size}"
                                                aria-valuenow="67"
                                                aria-valuemin="0"
                                                aria-valuemax="100"
                                            />
                                        </div>
                                    </div>
                                </CardBody>
                            </Card>
                        </Col>
                    {/each}
                </Row>
                <Row>
                    <Col lg={12}>
                        <div class="text-center mb-3">
                            <button class="btn btn-link text-success mt-2"
                                ><i
                                    class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"
                                /> Load more
                            </button>
                        </div>
                    </Col>
                </Row>
            </Col>
            <Col xxl={3}>
                <Card>
                    <CardHeader class="d-flex align-items-center">
                        <h6 class="card-title mb-0 flex-grow-1 fw-bold">Top Drop</h6>
                        <Link class="text-muted" href={null}>
                            See All <i
                                class="ri-arrow-right-line align-bottom"
                            />
                        </Link>
                    </CardHeader>
                    <CardBody>
                        <div class="table-responsive table-card">
                            <table class="table table-borderless align-middle">
                                <tbody>
                                    {#each data.topDrop as item}
                                        <tr>
                                            <td>
                                                <div
                                                    class="d-flex align-items-center"
                                                >
                                                    <img
                                                        src={item.img}
                                                        alt=""
                                                        class="avatar-sm object-cover rounded-circle"
                                                    />
                                                    <div class="ms-2">
                                                        <Link
                                                            href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                                            ><h6
                                                                class="fs-15 mb-1"
                                                            >
                                                                {item.title}
                                                            </h6></Link
                                                        >
                                                        <p
                                                            class="mb-0 text-muted"
                                                        >
                                                            Sold at {item.price}
                                                            ETH
                                                        </p>
                                                    </div>
                                                </div>
                                            </td>
                                            <td><small>{item.time}</small></td>
                                        </tr>
                                    {/each}
                                </tbody>
                            </table>
                        </div>
                    </CardBody>
                </Card>
                <Card>
                    <CardHeader class="d-flex align-items-center">
                        <h6 class="card-title mb-0 flex-grow-1 fw-bold">Top Creator</h6>
                        <Link
                            class="text-muted"
                            href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                        >
                            See All <i
                                class="ri-arrow-right-line align-bottom"
                            />
                        </Link>
                    </CardHeader>
                    <CardBody>
                        <div class="table-responsive table-card">
                            <table class="table table-borderless align-middle">
                                <tbody>
                                    {#each data.topCreator as item}
                                        <tr>
                                            <td>
                                                <div
                                                    class="d-flex align-items-center"
                                                >
                                                    <img
                                                        src={item.img}
                                                        alt=""
                                                        class="avatar-sm object-fit-cover rounded-circle"
                                                    />
                                                    <div class="ms-2">
                                                        <Link href={null}
                                                            ><h6
                                                                class="fs-15 mb-1"
                                                            >
                                                                {item.name}
                                                            </h6></Link
                                                        >
                                                        <p
                                                            class="mb-0 text-muted"
                                                        >
                                                            {item.products} Products
                                                        </p>
                                                    </div>
                                                </div>
                                            </td>
                                            <td
                                                ><button
                                                    class={item.isFollow
                                                        ? "btn btn-sm btn-success"
                                                        : "btn btn-sm btn-soft-success"}
                                                    >{item.isFollow
                                                        ? "Follow"
                                                        : "Unfollow"}</button
                                                ></td
                                            >
                                        </tr>
                                    {/each}
                                </tbody>
                            </table>
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
