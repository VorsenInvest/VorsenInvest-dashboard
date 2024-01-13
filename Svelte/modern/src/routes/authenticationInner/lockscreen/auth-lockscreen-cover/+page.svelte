<script>
    import { Button, Card, Col, Container, Row,Label } from "sveltestrap";
    import avatar1 from "../../../../assets/images/users/avatar-1.jpg";
    import AuthSlider from "../../AuthSlider.svelte";
    import Link from "svelte-link";
</script>

<svelte:head>
    <title>Lock Screen | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div
    class="auth-page-wrapper auth-bg-cover py-5 d-flex justify-content-center align-items-center min-vh-100"
>
    <div class="bg-overlay" />

    <div class="auth-page-content overflow-hidden pt-lg-5">
        <Container>
            <Row>
                <Col lg={12}>
                    <Card class="overflow-hidden">
                        <Row class="justify-content-center g-0">
                            <AuthSlider />
                            <Col lg={6}>
                                <div class="p-lg-5 p-4">
                                    <div>
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

                                    <div class="mt-4">
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

                                    <div class="mt-5 text-center">
                                        <p class="mb-0">
                                            Not you ? return <Link
                                                href="/authenticationInner/login/auth-signin-cover"
                                                class="fw-semibold text-primary text-decoration-underline"
                                            >
                                                Signin</Link
                                            >
                                        </p>
                                    </div>
                                </div>
                            </Col>
                        </Row>
                    </Card>
                </Col>
            </Row>
        </Container>
    </div>

    <footer class="footer start-0">
        <Container>
            <Row>
                <Col lg={12}>
                    <div class="text-center">
                        <p class="mb-0">
                            &copy; {new Date().getFullYear()} Velzon. Crafted with
                            <i class="mdi mdi-heart text-danger" /> by Themesbrand
                        </p>
                    </div>
                </Col>
            </Row>
        </Container>
    </footer>
</div>
