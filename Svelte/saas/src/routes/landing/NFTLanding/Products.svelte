<script>
import { Container, Row, Col, Nav, NavItem, NavLink } from 'sveltestrap';
import Link from 'svelte-link';
import data from '../../../common/data/LandingNFT';
let nav = "All";
</script>
<section class="section bg-light" id="marketplace">
    <Container>
        <Row class="justify-content-center">
            <Col lg={8}>
                <div class="text-center mb-5">
                    <h2 class="mb-3 fw-bold lh-base">Explore Products</h2>
                    <p class="text-muted mb-4">Collection widgets specialize in displaying many elements of the same type, such as a collection of pictures from a collection of articles.</p>
                    <Nav pills class="nav-pills filter-btns justify-content-center" role="tablist">
                        <NavItem role="presentation">
                            <NavLink type="button" on:click={() => nav = "All"} class={nav === "All" ? " fw-medium active" : "fw-medium"}>All Items</NavLink>
                        </NavItem>
                        <NavItem role="presentation">
                            <NavLink type="button" on:click={() => nav = "artwork"} class={nav === "artwork" ? " fw-medium active" : "fw-medium"}>Artwork</NavLink>
                        </NavItem>
                        <NavItem role="presentation">
                            <NavLink type="button" on:click={() => nav = "music"} class={nav === "music" ? " fw-medium active" : "fw-medium"}>Music</NavLink>
                        </NavItem>
                        <NavItem role="presentation">
                            <NavLink type="button" on:click={() => nav = "games"} class={nav === "games" ? " fw-medium active" : "fw-medium"}>Games</NavLink>
                        </NavItem>
                        <NavItem role="presentation">
                            <NavLink type="button" on:click={() => nav = "crypto-card"} class={nav === "crypto-card" ? " fw-medium active" : "fw-medium"}>Crypto Card</NavLink>
                        </NavItem>
                        <NavItem role="presentation">
                            <NavLink type="button" on:click={() => nav = "3d-style"} class={nav === "3d-style" ? " fw-medium active" : "fw-medium"}>3d Style</NavLink>
                        </NavItem>
                    </Nav>
                </div>
            </Col>
        </Row>
        <Row>
            {#each data.productData as item}
                <Col lg={4} class={"product-item " + item.isClass}>
                    <div class="card explore-box card-animate">
                        <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                            <button type="button" class="btn btn-icon active" data-bs-toggle="button" aria-pressed="true"><i class="mdi mdi-cards-heart fs-16"></i></button>
                        </div>
                        <div class="explore-place-bid-img">
                            <img src={item.img} alt="" class="card-img-top explore-img" />
                            <div class="bg-overlay"></div>
                            <div class="place-bid-btn">
                                <Link href={null} class="btn btn-success"><i class="ri-auction-fill align-bottom me-1"></i> Place Bid</Link>
                            </div>
                        </div>
                        <div class="card-body">
                            <p class="fw-medium mb-0 float-end"><i class="mdi mdi-heart text-danger align-middle"></i> {item.likes} </p>
                            <h5 class="mb-1"><Link href="/NFTmarketplace/Itemdetails/apps-nft-item-details" class="text-body">{item.title}</Link></h5>
                            <p class="text-muted mb-0">{item.category}</p>
                        </div>
                        <div class="card-footer border-top border-top-dashed">
                            <div class="d-flex align-items-center">
                                <div class="flex-grow-1 fs-14">
                                    <i class="ri-price-tag-3-fill text-warning align-bottom me-1"></i> Highest: <span class="fw-medium">{item.highest}</span>
                                </div>
                                <h5 class="flex-shrink-0 fs-14 text-primary mb-0">{item.price}</h5>
                            </div>
                        </div>
                    </div>
                </Col>
            {/each}
        </Row>
    </Container>
</section>