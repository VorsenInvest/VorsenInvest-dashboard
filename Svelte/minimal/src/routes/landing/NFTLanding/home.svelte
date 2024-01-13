<script>
    import { Col, Container, Row } from 'sveltestrap';
    import Link from 'svelte-link';
</script>

<section class="section nft-hero" id="hero">
    <div class="bg-overlay"></div>
    <Container>
        <Row class="justify-content-center">
            <Col lg={8} sm={10}>
                <div class="text-center">
                    <h1 class="display-4 fw-medium mb-4 lh-base text-white">Discover Digital Art & Collect <span class="text-success">NFT Marketplace</span></h1>
                    <p class="lead text-white-50 lh-base mb-4 pb-2">Can artwork be NFT? NFTs (non-fungible tokens) are one-of-a-kind digital assets. Given they're digital in nature, can physical works of art be turned into NFTs?.</p>

                    <div class="hstack gap-2 justify-content-center">
                        <Link href="/NFTmarketplace/CreateNFT/apps-nft-create" class="btn btn-primary">Create Own <i class="ri-arrow-right-line align-middle ms-1"></i></Link>
                        <Link href="/NFTmarketplace/ExploreNow/apps-nft-explore" class="btn btn-secondary">Explore Now <i class="ri-arrow-right-line align-middle ms-1"></i></Link>
                    </div>
                </div>
            </Col>
        </Row>
    </Container>
</section>