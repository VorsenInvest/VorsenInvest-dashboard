<script>
    import { Container, Row, Col, Card, CardBody } from 'sveltestrap';
    import Link from 'svelte-link';
    import data from '../../../common/data/LandingNFT';

    const favouriteBtn = (ele) => {
        if (ele.closest("button").classList.contains("active")) {
            ele.closest("button").classList.remove("active");
        } else {
            ele.closest("button").classList.add("active");
        }
    };
</script>
<section class="section">
    <Container>
        <Row class="justify-content-center">
            <Col lg={12}>
                <div class="d-flex align-items-center mb-5">
                    <h2 class="mb-0 fw-semibold lh-base flex-grow-1">Discover Items</h2>
                    <Link href="/NFTmarketplace/ExploreNow/apps-nft-explore" class="btn btn-primary">View All <i class="ri-arrow-right-line align-bottom"></i></Link>
                </div>
            </Col>
        </Row>
        <Row>
            {#each data.discoverItemsData as item}
            <Col lg={4}>
                <Card class="explore-box card-animate border">
                    <CardBody>
                        <div class="d-flex align-items-center mb-3">
                            <img src={item.cardImg} alt="" class="avatar-xs rounded-circle" />
                            <div class="ms-2 flex-grow-1">
                                <Link href={null}><h6 class="mb-0 fs-15">{item.author}</h6></Link>
                                <p class="mb-0 text-muted fs-13">{item.title}</p>
                            </div>
                            <div class="bookmark-icon">
                                <button type="button" class={item.isIcon ? "btn btn-icon" : "btn btn-icon active"} data-bs-toggle="button" aria-pressed="true" onClick={(e) => favouriteBtn(e.target)}>
                                    <i class="mdi mdi-cards-heart fs-16"></i></button>
                            </div>
                        </div>
                        <div class="explore-place-bid-img overflow-hidden rounded">
                            <img src={item.img} alt="" class="explore-img w-100" />
                            <div class="bg-overlay"></div>
                            <div class="place-bid-btn">
                                <Link href={null} class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i> Place Bid</Link>
                            </div>
                        </div>
                        <div class="mt-3">
                            <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i> {item.likes} </p>
                            <h5 class="text-success"><i class="mdi mdi-ethereum"></i> {item.price} </h5>
                            <h6 class="fs-16 mb-0"><Link href="/NFTmarketplace/Itemdetails/apps-nft-item-details" class="text-body">{item.category}</Link></h6>
                        </div>
                    </CardBody>
                </Card>
            </Col>
            {/each}
            
        </Row>
    </Container>
</section>