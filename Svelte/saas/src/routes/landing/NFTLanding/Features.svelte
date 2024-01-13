<script>
    import { Container, Row, Col, Card, CardBody } from 'sveltestrap';
    import Link from 'svelte-link';
    import data from '../../../common/data/LandingNFT';
</script>
<section class="section">
    <Container>
        <Row class="justify-content-center">
            <Col lg={8}>
                <div class="text-center mb-5">
                    <h2 class="mb-3 fw-bold lh-base">Create and Sell Your NFTs</h2>
                    <p class="text-muted">The process of creating an NFT may cost less than a dollar, but the process of selling it can cost up to a thousand dollars. For example, Allen Gannett, a software developer.</p>
                </div>
            </Col>
        </Row>
        
        <Row>
            {#each data.featuresData as item}
                <Col lg={3}>
                    <Card class="shadow-none">
                        <CardBody>
                            <img src={item.img} alt="" class="avatar-sm"/>
                            <h5 class="mt-4">{item.title}</h5>
                            <p class="text-muted fs-14">{item.textConent}</p>
                            <Link href={null} class="link-success fs-14">Read More <i class="ri-arrow-right-line align-bottom"></i></Link>
                        </CardBody>
                    </Card>
                </Col>
            {/each}                                 
        </Row>
    </Container>
</section>