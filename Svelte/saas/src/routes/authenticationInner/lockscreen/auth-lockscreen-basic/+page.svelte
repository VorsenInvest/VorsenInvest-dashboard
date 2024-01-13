<script>
    import { Button, Card, CardBody, Col, Container, Row,Label } from "sveltestrap";
    import ParticlesAuth from "../../ParticlesAuth.svelte";
    import Link from "svelte-link";
    import logoLight from "../../../../assets/images/logo-light.png";
    import avatar1 from "../../../../assets/images/users/avatar-1.jpg";
</script>

<svelte:head>
    <title>Lock Screen | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
        <ParticlesAuth>
            <div class="auth-page-content pt-5">
                <Container>
                    <Row>
                        <Col lg={12}>
                            <div class="text-center mt-sm-5 mb-4 text-white-50">
                                <div>
                                    <Link
                                        href="/dashboard"
                                        class="d-inline-block auth-logo"
                                    >
                                        <img
                                            src={logoLight}
                                            alt=""
                                            height="20"
                                        />
                                    </Link>
                                </div>
                                <p class="mt-3 fs-15 fw-medium">
                                    Premium Admin & Dashboard Template
                                </p>
                            </div>
                        </Col>
                    </Row>

                    <Row class="justify-content-center">
                        <Col md={8} lg={6} xl={5}>
                            <Card class="mt-4">
                                <CardBody class="p-4">
                                    <div class="text-center mt-2">
                                        <h5 class="text-primary">
                                            Lock Screen
                                        </h5>
                                        <p class="text-muted">
                                            Enter your password to unlock the
                                            screen!
                                        </p>
                                    </div>
                                    <div class="user-thumb text-center">
                                        <img
                                            src={avatar1}
                                            class="rounded-circle img-thumbnail avatar-lg"
                                            alt="thumbnail"
                                        />
                                        <h5 class="font-size-15 mt-3">
                                            Anna Adame
                                        </h5>
                                    </div>
                                    <div class="p-2 mt-4">
                                        <form>
                                            <div class="mb-3">
                                                <Label
                                                    class="form-label"
                                                    for="userpassword"
                                                    >Password</Label
                                                >
                                                <input
                                                    type="password"
                                                    class="form-control"
                                                    id="userpassword"
                                                    placeholder="Enter password"
                                                    required
                                                />
                                            </div>
                                            <div class="mb-2 mt-4">
                                                <Button
                                                    color="success"
                                                    class="w-100"
                                                    type="submit">Unlock</Button
                                                >
                                            </div>
                                        </form>
                                    </div>
                                </CardBody>
                            </Card>
                            <div class="mt-4 text-center">
                                <p class="mb-0">
                                    Not you ? return <Link
                                        href="/authenticationInner/login/auth-signin-basic"
                                        class="fw-semibold text-primary text-decoration-underline"
                                    >
                                        Signin
                                    </Link>
                                </p>
                            </div>
                        </Col>
                    </Row>
                </Container>
            </div>
        </ParticlesAuth>