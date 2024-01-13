<script>
    import { Card, CardBody, Col, Container, Row } from 'sveltestrap';
    import Link from 'svelte-link';

    // Import Images
    import avatar2 from "../../../assets/images/users/avatar-2.jpg";
    import avatar3 from "../../../assets/images/users/avatar-3.jpg";
    import avatar4 from "../../../assets/images/users/avatar-4.jpg";
    import avatar5 from "../../../assets/images/users/avatar-5.jpg";
    import avatar6 from "../../../assets/images/users/avatar-6.jpg";
    import avatar7 from "../../../assets/images/users/avatar-7.jpg";
    import avatar8 from "../../../assets/images/users/avatar-8.jpg";
    import avatar10 from "../../../assets/images/users/avatar-10.jpg";

</script>
<section class="section bg-light" id="team">
    <Container>
        <Row class="justify-content-center">
            <Col lg={8}>
                <div class="text-center mb-5">
                    <h3 class="mb-3 fw-semibold">Our <span class="text-primary">Team</span></h3>
                    <p class="text-muted mb-4 ff-secondary">To achieve this, it would be necessary to have uniform grammar,
                        pronunciation and more common words. If several languages coalesce the grammar.</p>
                </div>
            </Col>
        </Row>
        <Row>
            <Col lg={3} sm={6}>
                <Card>
                    <CardBody class="text-center p-4">
                        <div class="avatar-xl mx-auto mb-4 position-relative">
                            <img src={avatar2} alt="" class="img-fluid rounded-circle" />
                            <Link href="/emailInbox/apps-mailbox"
                                class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle avatar-xs">
                                <div class="avatar-title bg-transparent">
                                    <i class="ri-mail-fill align-bottom"></i>
                                </div>
                            </Link>
                        </div>

                        <h5 class="mb-1"><Link href="/pages/profile/simple" class="text-body">Nancy Martino</Link></h5>
                        <p class="text-muted mb-0 ff-secondary">Team Leader</p>
                    </CardBody>
                </Card>

            </Col>

            <Col lg={3} sm={6}>
                <Card>
                    <CardBody class="text-center p-4">
                        <div class="avatar-xl mx-auto mb-4 position-relative">
                            <img src={avatar10} alt="" class="img-fluid rounded-circle" />
                            <Link href="/emailInbox/apps-mailbox"
                                class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle avatar-xs">
                                <div class="avatar-title bg-transparent">
                                    <i class="ri-mail-fill align-bottom"></i>
                                </div>
                            </Link>
                        </div>

                        <h5 class="mb-1"><Link href="/pages/profile/simple" class="text-body">Henry Baird</Link></h5>
                        <p class="text-muted mb-0 ff-secondary">Full Stack Developer</p>
                    </CardBody>
                </Card>

            </Col>

            <Col lg={3} sm={6}>
                <Card>
                    <CardBody class="text-center p-4">
                        <div class="avatar-xl mx-auto mb-4 position-relative">
                            <img src={avatar3} alt="" class="img-fluid rounded-circle" />
                            <Link href="/emailInbox/apps-mailbox"
                                class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle avatar-xs">
                                <div class="avatar-title bg-transparent">
                                    <i class="ri-mail-fill align-bottom"></i>
                                </div>
                            </Link>
                        </div>

                        <h5 class="mb-1"><Link href="/pages/profile/simple" class="text-body">Frank Hook</Link></h5>
                        <p class="text-muted mb-0 ff-secondary">Project Manager</p>
                    </CardBody>
                </Card>

            </Col>

            <Col lg={3} sm={6}>
                <Card>
                    <CardBody class="text-center p-4">
                        <div class="avatar-xl mx-auto mb-4 position-relative">
                            <img src={avatar8} alt="" class="img-fluid rounded-circle" />
                            <Link href="/emailInbox/apps-mailbox"
                                class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle avatar-xs">
                                <div class="avatar-title bg-transparent">
                                    <i class="ri-mail-fill align-bottom"></i>
                                </div>
                            </Link>
                        </div>

                        <h5 class="mb-1"><Link href="/pages/profile/simple" class="text-body">Donald Palmer</Link></h5>
                        <p class="text-muted mb-0 ff-secondary">UI/UX Designer</p>
                    </CardBody>
                </Card>

            </Col>

        </Row>

        <Row>
            <Col lg={3} sm={6}>
                <Card>
                    <CardBody class="text-center p-4">
                        <div class="avatar-xl mx-auto mb-4 position-relative">
                            <img src={avatar5} alt="" class="img-fluid rounded-circle" />
                            <Link href="/emailInbox/apps-mailbox"
                                class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle avatar-xs">
                                <div class="avatar-title bg-transparent">
                                    <i class="ri-mail-fill align-bottom"></i>
                                </div>
                            </Link>
                        </div>

                        <h5 class="mb-1"><Link href="/pages/profile/simple" class="text-body">Erica Kernan</Link></h5>
                        <p class="text-muted mb-0 ff-secondary">Web Designer</p>
                    </CardBody>
                </Card>

            </Col>

            <Col lg={3} sm={6}>
                <Card>
                    <CardBody class="text-center p-4">
                        <div class="avatar-xl mx-auto mb-4 position-relative">
                            <img src={avatar4} alt="" class="img-fluid rounded-circle" />
                            <Link href="/emailInbox/apps-mailbox"
                                class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle avatar-xs">
                                <div class="avatar-title bg-transparent">
                                    <i class="ri-mail-fill align-bottom"></i>
                                </div>
                            </Link>
                        </div>

                        <h5 class="mb-1"><Link href="/pages/profile/simple" class="text-body">Alexis Clarke</Link></h5>
                        <p class="text-muted mb-0 ff-secondary">Backend Developer</p>
                    </CardBody>
                </Card>

            </Col>

            <Col lg={3} sm={6}>
                <Card>
                    <CardBody class="text-center p-4">
                        <div class="avatar-xl mx-auto mb-4 position-relative">
                            <img src={avatar6} alt="" class="img-fluid rounded-circle" />
                            <Link href="/emailInbox/apps-mailbox"
                                class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle avatar-xs">
                                <div class="avatar-title bg-transparent">
                                    <i class="ri-mail-fill align-bottom"></i>
                                </div>
                            </Link>
                        </div>

                        <h5 class="mb-1"><Link href="/pages/profile/simple" class="text-body">Marie Ward</Link></h5>
                        <p class="text-muted mb-0 ff-secondary">Full Stack Developer</p>
                    </CardBody>
                </Card>

            </Col>


            <Col lg={3} sm={6}>
                <Card>
                    <CardBody class="text-center p-4">
                        <div class="avatar-xl mx-auto mb-4 position-relative">
                            <img src={avatar7} alt="" class="img-fluid rounded-circle" />
                            <Link href="/emailInbox/apps-mailbox"
                                class="btn btn-primary btn-sm position-absolute bottom-0 end-0 rounded-circle avatar-xs">
                                <div class="avatar-title bg-transparent">
                                    <i class="ri-mail-fill align-bottom"></i>
                                </div>
                            </Link>
                        </div>

                        <h5 class="mb-1"><Link href="/pages/profile/simple" class="text-body">Jack Gough</Link></h5>
                        <p class="text-muted mb-0 ff-secondary">React Js Developer</p>
                    </CardBody>
                </Card>

            </Col>

        </Row>

        <Row>
            <div class="col-lg-12">
                <div class="text-center mt-2">
                    <Link href="/pages/team/team" class="btn btn-primary">View All Members <i
                        class="ri-arrow-right-line ms-1 align-bottom"></i></Link>
                </div>
            </div>
        </Row>

    </Container>
</section>