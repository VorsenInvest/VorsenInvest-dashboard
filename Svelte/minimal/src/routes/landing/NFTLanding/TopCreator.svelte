<script>
    import { Container, Row, Col, Card, CardBody, Dropdown, DropdownToggle, DropdownMenu, DropdownItem} from 'sveltestrap';
    import Link from 'svelte-link';
    import data from '../../../common/data/LandingNFT';
</script>
<section class="section bg-light" id="creators">
    <Container>
        <Row class="justify-content-center">
            <Col lg={8}>
                <div class="text-center mb-5">
                    <h2 class="mb-3 fw-bold lh-base">Top Creator This Week</h2>
                    <p class="text-muted">NFTs are valuable because they verify the authenticity of a non-fungible asset. This makes these assets unique and one of a kind.</p>
                </div>
            </Col>
        </Row>
        <Row>
        {#each data.topCreatorData as item}
            <Col xl={4} md={6}>
                <Card>
                    <CardBody>
                        <div class="d-flex">
                            <div class="flex-shink-0">
                                <img src={item.img} alt="" class="avatar-sm object-cover rounded" />
                            </div>
                            <div class="ms-3 flex-grow-1">
                                <Link href="pages-profile">
                                    <h5 class="mb-1 fs-16">{item.title}</h5>
                                </Link>
                                <p class="text-muted fs-14 mb-0"><i class="mdi mdi-ethereum text-primary fs-14"></i> {item.price}</p>
                            </div>
                            <div>
                            <Dropdown class="float-end">
                                <DropdownToggle tag="button" class="btn btn-ghost-primary btn-icon" color="">
                                <i class="ri-more-fill align-middle fs-16"></i>
                                </DropdownToggle>
                                <DropdownMenu class="dropdown-menu-end" end>
                                    <DropdownItem class="view-item-btn">Share</DropdownItem>
                                    <DropdownItem class="edit-item-btn">Report</DropdownItem>
                                </DropdownMenu>
                            </Dropdown>
                            </div>
                        </div>
                    </CardBody>
                </Card>
            </Col>
            {/each}                     
        </Row>
    </Container>
</section>