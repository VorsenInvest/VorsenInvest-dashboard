<script>
    import { Container, Row, Col } from 'sveltestrap';
    import Link from 'svelte-link';
</script>
<section class="py-5 bg-primary position-relative bg-opacity-25">
    <div class="bg-overlay bg-overlay-pattern opacity-50"></div>
    <Container>
        <Row class="align-items-center gy-4">
            <Col class="col-sm">
                <div>
                    <h4 class="text-white mb-0 fw-semibold">Create and Sell Your NFT's</h4>
                </div>
            </Col>

            <Col class="col-sm-auto">
                <div>
                    <Link href="/NFTmarketplace/CreateNFT/apps-nft-create" class="btn bg-gradient btn-danger me-1">Create NFT</Link>
                    <Link href="/NFTmarketplace/ExploreNow/apps-nft-explore" class="btn bg-gradient btn-primary">Discover More</Link>
                </div>
            </Col>
        </Row>
    </Container>
</section>