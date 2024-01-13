<script>
    import { Container, Row, Col, Card, CardBody } from 'sveltestrap';
    import Link from 'svelte-link';
    import data from '../../../common/data/LandingNFT';
</script>
<section class="section" id="wallet">
    <Container>
        <Row class="justify-content-center">
            <Col lg={8}>
                <div class="text-center mb-5">
                    <h2 class="mb-3 fw-semibold lh-base">Connect NFT Marketplace</h2>
                    <p class="text-muted">A non-fungible token is a non-interchangeable unit of data stored on a blockchain, a form of digital ledger, that can be sold and traded.</p>
                </div>
            </Col>
        </Row>

        <Row class="g-4">
            {#each data.connectData as item}
                <Col lg={4}>
                    <Card class="text-center border shadow-none material-shadow">
                        <CardBody class="py-5 px-4">
                            <img src={item.img} alt="" height="55" class="mb-3 pb-2" />
                            <h5>{item.title}</h5>
                            <p class="text-muted pb-1">{item.textContent}</p>
                            <Link href={null} class={item.bgColor ? "btn btn-info" : "btn btn-soft-info" }>Connect Wallet</Link>
                        </CardBody>
                    </Card>
                </Col>
            {/each}
        </Row>
    </Container>
</section>