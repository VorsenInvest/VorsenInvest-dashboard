<script>
    import { Card, CardBody, Col, Container, Row } from "sveltestrap";
    import Marquee from "svelte-fast-marquee";
    import data from "../../../common/data/NFTMarketplace";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import Link from "svelte-link";
    import BgPattern from "../../../assets/images/nft/bg-pattern.png";
</script>

<svelte:head>
    <title>Marketplace | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Marketplace" pageTitle="NFT Marketplace" />
        <Row>
            <Col xl={8}>
                <Row>
                    {#each data.marketPlacewidget as item}
                        <Col lg={4} md={6}>
                            <Card>
                                <CardBody>
                                    <Row class="g-1 mb-3">
                                        {#each item.subItem as subitem}
                                            <Col lg={6}>
                                                {#each subitem.isChildren as subsubitem}
                                                    <img
                                                        src={subsubitem.img}
                                                        alt=""
                                                        class={"img-fluid rounded " +
                                                            subsubitem.imgClass}
                                                    />
                                                {/each}
                                            </Col>
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
            </Col>

            <Col xl={4}>
                <div class="alert alert-danger">
                    Up to <b>50% OFF</b>, Hurry up before the stock ends
                </div>
                <Card
                    class="bg-primary"
                    style="background-image: url({BgPattern})"
                >
                    <CardBody class="p-4">
                        <span class="badge bg-info fw-medium mb-3 fs-12"
                            >Trending Artwork</span
                        >
                        <h2 class="text-white lh-base">
                            Discover, Collect, Sell and Create your own NFT
                        </h2>
                        <p class="text-white text-opacity-75 mb-3">
                            Take advantage of the first text-based NFT. Select a
                            text or write your own and let it live forever on
                            the Ethereum blockchain you or future owners can add
                            text to an existing ChainText token..
                        </p>
                        <div class="hstack gap-2">
                            <Link
                                href="/NFTmarketplace/CreateNFT/apps-nft-create"
                                class="btn btn-success">Create NFT</Link
                            >
                            <Link
                                href="/NFTmarketplace/ExploreNow/apps-nft-explore"
                                class="btn btn-danger">Explore Now</Link
                            >
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>

        <Row>
            <Col lg={12}>
                <Card class="overflow-hidden shadow-none">
                    <CardBody
                        class="bg-success-subtle text-success fw-semibold d-flex"
                    >
                        <Marquee speed={50}>
                            NFT art is a digital asset that is collectable,
                            unique, and non-transferrable, Cortes explained.
                            Every NFT is unique in it's creative design and
                            cannot be duplicated, making them limited and rare.
                            NFTs get their value because the transaction proves
                            ownership of the art.
                        </Marquee>
                    </CardBody>
                </Card>
            </Col>
        </Row>

        <Row>
            <Col lg={12}>
                <div class="d-lg-flex align-items-center mb-4">
                    <div class="flex-grow-1">
                        <h5 class="card-title mb-0 fw-semibold fs-16">
                            Trending Artwork
                        </h5>
                    </div>
                    <div class="flex-shrink-0 mt-4 mt-lg-0">
                        <Link
                            href="/NFTmarketplace/ExploreNow/apps-nft-explore"
                            class="btn btn-soft-primary"
                            >View All <i
                                class="ri-arrow-right-line align-bottom"
                            /></Link
                        >
                    </div>
                </div>
            </Col>
        </Row>

        <Row class="row-cols-xl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
            {#each data.tradingArtworkData as item}
                <Col>
                    <Card class="explore-box">
                        <CardBody>
                            <div class="d-flex align-items-center mb-3">
                                <img
                                    src={item.img}
                                    alt=""
                                    class="avatar-xs rounded-circle"
                                />
                                <div class="ms-2 flex-grow-1">
                                    <h6 class="mb-0 fs-15">{item.author}</h6>
                                    <p class="mb-0 text-muted">{item.title}</p>
                                </div>
                                <div class="bookmark-icon">
                                    <button
                                        type="button"
                                        class={item.isActive
                                            ? "btn btn-icon active "
                                            : "btn btn-icon"}
                                        data-bs-toggle="button"
                                        aria-pressed="true"
                                    >
                                        <i class="mdi mdi-cards-heart fs-16" />
                                    </button>
                                </div>
                            </div>
                            <div
                                class="explore-place-bid-img overflow-hidden rounded"
                            >
                                <img
                                    src={item.cardImg}
                                    alt=""
                                    class="img-fluid explore-img"
                                />
                                <div class="bg-overlay" />
                                <div class="place-bid-btn">
                                    <Link href={null} class="btn btn-success"
                                        ><i
                                            class="ri-auction-fill align-bottom me-1"
                                        /> Place Bid</Link
                                    >
                                </div>
                            </div>
                            <div class="mt-3">
                                <p class="fw-medium mb-0 float-end">
                                    <i
                                        class="mdi mdi-heart text-danger align-middle"
                                    />
                                    {item.likes}
                                </p>
                                <h5 class="text-success">
                                    <i class="mdi mdi-ethereum" />
                                    {item.price}
                                </h5>
                                <h6 class="fs-16 mb-0">
                                    <Link
                                        href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                        class="text-body">{item.category}</Link
                                    >
                                </h6>
                            </div>
                        </CardBody>
                    </Card>
                </Col>
            {/each}
        </Row>

        <Row>
            <Col lg={12}>
                <div class="d-lg-flex align-items-center mb-4">
                    <div class="flex-grow-1">
                        <h5 class="card-title mb-0 fw-semibold fs-16">
                            Recent NFTs Artwork
                        </h5>
                    </div>
                    <div class="flex-shrink-0 mt-4 mt-lg-0">
                        <Link
                            href="/NFTmarketplace/Creators/apps-nft-creators"
                            class="btn btn-soft-primary"
                            >View All <i
                                class="ri-arrow-right-line align-bottom"
                            /></Link
                        >
                    </div>
                </div>
            </Col>
        </Row>

        <Row class="row-cols-xl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
            {#each data.nftArtworkData as item}
                <Col>
                    <Card class="explore-box card-animate">
                        <div
                            class="bookmark-icon position-absolute top-0 end-0 p-2"
                        >
                            <button
                                type="button"
                                class="btn btn-icon active"
                                data-bs-toggle="button"
                                aria-pressed="true"
                                ><i class="mdi mdi-cards-heart fs-16" /></button
                            >
                        </div>
                        <div class="explore-place-bid-img">
                            <img
                                src={item.img}
                                alt=""
                                class="card-img-top explore-img"
                            />
                            <div class="bg-overlay" />
                            <div class="place-bid-btn">
                                <Link href={null} class="btn btn-success"
                                    ><i
                                        class="ri-auction-fill align-bottom me-1"
                                    /> Place Bid</Link
                                >
                            </div>
                        </div>
                        <CardBody>
                            <p class="fw-medium mb-0 float-end">
                                <i
                                    class="mdi mdi-heart text-danger align-middle"
                                />
                                {item.likes}
                            </p>
                            <h5 class="mb-1">
                                <Link
                                    href="/NFTmarketplace/Itemdetails/apps-nft-item-details"
                                    class="text-body">{item.title}</Link
                                >
                            </h5>
                            <p class="text-muted mb-0">{item.category}</p>
                        </CardBody>
                        <div class="card-footer border-top border-top-dashed">
                            <div class="d-flex align-items-center">
                                <div class="flex-grow-1 fs-14">
                                    <i
                                        class="ri-price-tag-3-fill text-warning align-bottom me-1"
                                    />
                                    Highest:
                                    <span class="fw-medium">{item.highest}</span
                                    >
                                </div>
                                <h5
                                    class="flex-shrink-0 fs-14 text-primary mb-0"
                                >
                                    {item.price}
                                </h5>
                            </div>
                        </div>
                    </Card>
                </Col>
            {/each}
        </Row>

        <Row>
            <Col lg={12}>
                <div class="d-lg-flex align-items-center mb-4">
                    <div class="flex-grow-1">
                        <h5 class="card-title mb-0 fw-semibold fs-16">
                            Popular Creators
                        </h5>
                    </div>
                    <div class="flex-shrink-0 mt-4 mt-lg-0">
                        <Link
                            href="/NFTmarketplace/Creators/apps-nft-creators"
                            class="btn btn-soft-primary"
                            >View All <i
                                class="ri-arrow-right-line align-bottom"
                            /></Link
                        >
                    </div>
                </div>
            </Col>
        </Row>

        <Row class="row-cols-xl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
            {#each data.popularCreatorsNFT as item}
                <Col>
                    <Card>
                        <img
                            src={item.cardImg}
                            alt=""
                            class="card-img-top object-fit-cover"
                            height="120"
                        />
                        <CardBody class="text-center">
                            <img
                                src={item.img}
                                alt=""
                                class="avatar-md mt-n5 rounded-circle mx-auto d-block object-cover"
                            />
                            <h5 class="mt-3 mb-1">
                                <Link href={null} class="text-body"
                                    >{item.author}</Link
                                >
                            </h5>
                            <p class="text-muted">{item.products} Products</p>
                            <div>
                                <button
                                    class={item.isFollow
                                        ? "btn btn-primary btn-sm"
                                        : "btn btn-soft-primary btn-sm"}
                                    >{item.isFollow
                                        ? "Follow"
                                        : "Unfollow"}</button
                                >
                            </div>
                        </CardBody>
                    </Card>
                </Col>
            {/each}
        </Row>
    </Container>
</div>
