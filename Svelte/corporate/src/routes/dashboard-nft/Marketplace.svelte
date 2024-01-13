<script>
import { Card, CardBody, CardHeader, Col, DropdownItem, DropdownMenu, DropdownToggle, Row, Dropdown } from 'sveltestrap';
import Counter from '../../Components/Common/CounterPage.svelte';
import MarketplaceChart from "./DashboardNFTCharts.svelte";
import { browser } from "$app/environment";
import Link from 'svelte-link'

 // Set the date we're counting down to
 var countDownDate = new Date("Jan 1, 2025").getTime();

// Update the count down every 1 second
var countDown = setInterval(function () {
    // Get today's date and time
    var currentTime = new Date().getTime();

    // Find the distance between currentTime and the count down date
    var distance = countDownDate - currentTime;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor(
        (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
    );
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    var countDownBlock =
        '<div class="countdownlist-item">' +
        '<div class="count-title">Days</div>' +
        '<div class="count-num">' +
        days +
        "</div>" +
        "</div>" +
        '<div class="countdownlist-item">' +
        '<div class="count-title">Hours</div>' +
        '<div class="count-num">' +
        hours +
        "</div>" +
        "</div>" +
        '<div class="countdownlist-item">' +
        '<div class="count-title">Minutes</div>' +
        '<div class="count-num">' +
        minutes +
        "</div>" +
        "</div>" +
        '<div class="countdownlist-item">' +
        '<div class="count-title">Seconds</div>' +
        '<div class="count-num">' +
        seconds +
        "</div>" +
        "</div>";
    if (browser) {
        // Output the result in an element with id="countDownBlock"
        document.getElementById("countdown").innerHTML = countDownBlock;

        // If the count down is over, write some text
        if (distance < 0) {
            clearInterval(countDown);
            document.getElementById("countdown").innerHTML =
                '<div class="countdown-endtxt">The countdown has ended!</div>';
        }
    }
}, 1000);
</script>
<Counter />
<Row>
    <Col xxl={12}>
        <Card>
            <CardBody class="p-0">
                <Row class="g-0">
                    <Col xxl={8}>
                        <div class="">
                            <CardHeader class="border-0 align-items-center d-flex">
                                <h4 class="card-title mb-0 flex-grow-1">Marketplace</h4>
                                <div>
                                    <button type="button" class="btn btn-soft-secondary btn-sm">
                                        ALL
                                    </button>
                                    <button type="button" class="btn btn-soft-secondary btn-sm">
                                        1M
                                    </button>
                                    <button type="button" class="btn btn-soft-secondary btn-sm">
                                        6M
                                    </button>
                                    <button type="button" class="btn btn-soft-primary btn-sm">
                                        1Y
                                    </button>
                                </div>
                            </CardHeader>
                            <Row class="g-0 text-center">
                                <Col sm={4} class="col-6">
                                    <div class="p-3 border border-dashed border-start-0">
                                        <h5 class="mb-1 fs-16"><span class="counter-value" data-target="36.48">0</span>k</h5>
                                        <p class="text-muted mb-0">Aetworks</p>
                                    </div>
                                </Col>
                                <Col sm={4} class="col-6">
                                    <div class="p-3 border border-dashed border-start-0">
                                        <h5 class="mb-1 fs-16"><span class="counter-value" data-target="92.54">0</span>k</h5>
                                        <p class="text-muted mb-0">Auction</p>
                                    </div>
                                </Col>
                                <Col sm={4} class="col-6">
                                    <div class="p-3 border border-dashed border-end-0">
                                        <h5 class="mb-1 fs-16"><span class="counter-value" data-target="8.62">0</span>k</h5>
                                        <p class="text-muted mb-0">Creators</p>
                                    </div>
                                </Col>
                            </Row>
                            <MarketplaceChart dataColors={["--vz-primary","--vz-secondary", "--vz-light"]} />
                        </div>
                    </Col>

                    <Col xxl={4}>
                        <div class="border-start p-4 h-100 d-flex flex-column">

                            <div class="w-100">
                                <div class="d-flex align-items-center">
                                    <img src="https://img.themesbrand.com/velzon/images/img-2.gif" class="img-fluid avatar-xs rounded-circle object-fit-cover" alt="" />
                                    <div class="ms-3 flex-grow-1">
                                        <h5 class="fs-16 mb-1">Trendy Fashion Portraits</h5>
                                        <p class="text-muted mb-0">Artwork</p>
                                    </div>

                                    <Dropdown>
                                        <DropdownToggle tag="a" class="text-muted dropdown-btn p-0" color="" role="button">
                                            <i class="ri-share-line fs-18"></i>
                                        </DropdownToggle>
                                        <DropdownMenu class="dropdown-menu-end" end>
                                            <DropdownItem href={null}><i class="ri-twitter-fill text-primary align-bottom me-1"></i> Twitter</DropdownItem>
                                            <DropdownItem href={null}><i class="ri-facebook-circle-fill text-info align-bottom me-1"></i> Facebook</DropdownItem>
                                            <DropdownItem href={null}><i class="ri-google-fill text-danger align-bottom me-1"></i> Google</DropdownItem>
                                        </DropdownMenu>
                                    </Dropdown>

                                </div>

                                <h4 class="ff-secondary fw-bold mt-4"><i class="mdi mdi-ethereum text-primary"></i> 346.12 ETH</h4>
                                <p class="text-success mb-3">+586.85 (40.6%)</p>

                                <p class="text-muted">NFT art is a digital asset that is collectable, unique, and non-transferrable, Cortes explained Every NFT is unique duplicated.</p>

                                <div class="d-flex align-items-end justify-content-between mt-4">
                                    <div>
                                        <p class="fs-14 text-muted mb-1">Current Bid</p>
                                        <h4 class="fs-18 ff-secondary fw-semibold mb-0">342.74 ETH</h4>
                                    </div>

                                    <div>
                                        <p class="fs-14 text-muted mb-1">Highest Bid</p>
                                        <h4 class="fs-18 ff-secondary fw-semibold mb-0">346.67 ETH</h4>
                                    </div>
                                </div>

                                <div class="dash-countdown mt-4 pt-1">
                                    <div id="countdown" class="countdownlist"></div>
                                </div>

                                <Row class="mt-4 pt-2">
                                    <Col>
                                        <Link href="/NFTmarketplace/Itemdetails/apps-nft-item-details" class="btn btn-primary w-100">View Details</Link>
                                    </Col>
                                    <Col>
                                        <button class="btn btn-info w-100">Bid Now</button>
                                    </Col>
                                </Row>
                            </div>
                        </div>
                    </Col>
                </Row>
            </CardBody>
        </Card>
    </Col>
</Row>