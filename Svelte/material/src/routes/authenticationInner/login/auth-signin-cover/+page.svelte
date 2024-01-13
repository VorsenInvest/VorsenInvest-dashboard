<script>
    import {
        Card,
        Col,
        Container,
        Input,
        Label,
        Row,
        Button,
    } from "sveltestrap";
    import AuthSlider from "../../AuthSlider.svelte";
    import Link from "svelte-link";
</script>

<svelte:head>
    <title>Sign In | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="auth-page-wrapper auth-bg-cover py-5 d-flex justify-content-center align-items-center min-vh-100">
    <div class="bg-overlay" />
    <div class="auth-page-content overflow-hidden pt-lg-5">
        <Container>
            <Row>
                <Col lg={12}>
                <Card class="overflow-hidden">
                    <Row class="g-0">
                        <AuthSlider />

                        <Col lg={6}>
                        <div class="p-lg-5 p-4">
                            <div>
                                <h5 class="text-primary">
                                    Welcome Back !
                                </h5>
                                <p class="text-muted">
                                    Sign in to continue to Velzon.
                                </p>
                            </div>

                            <div class="mt-4">
                                <form action="/">
                                    <div class="mb-3">
                                        <Label for="username" class="form-label">Username</Label>
                                        <Input type="text" class="form-control" id="username"
                                            placeholder="Enter username" />
                                    </div>

                                    <div class="mb-3">
                                        <div class="float-end">
                                            <Link href="/authenticationInner/passwordreset/auth-pass-reset-cover"
                                                class="text-muted">Forgot password?</Link>
                                        </div>
                                        <Label class="form-label" for="password-input">Password</Label>
                                        <div class="position-relative auth-pass-inputgroup mb-3">
                                            <Input type="password" class="form-control pe-5"
                                                placeholder="Enter password" id="password-input" />
                                            <button
                                                class="btn btn-link position-absolute end-0 top-0 text-decoration-none text-muted shadow-none"
                                                type="button" id="password-addon"><i
                                                    class="ri-eye-fill align-middle" /></button>
                                        </div>
                                    </div>

                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" value=""
                                            id="auth-remember-check" />
                                        <Label class="form-check-label" for="auth-remember-check">Remember me</Label>
                                    </div>

                                    <div class="mt-4">
                                        <Button color="success" class="w-100" type="submit">Sign In</Button>
                                    </div>

                                    <div class="mt-4 text-center">
                                        <div class="signin-other-title">
                                            <h5 class="fs-13 mb-4 title">
                                                Sign In with
                                            </h5>
                                        </div>

                                        <div>
                                            <Button color="primary" class="btn-icon"><i
                                                    class="ri-facebook-fill fs-16" /></Button>
                                            <Button color="danger" class="btn-icon"><i
                                                    class="ri-google-fill fs-16" /></Button>
                                            <Button color="dark" class="btn-icon"><i
                                                    class="ri-github-fill fs-16" /></Button>
                                            <Button color="info" class="btn-icon"><i
                                                    class="ri-twitter-fill fs-16" /></Button>
                                        </div>
                                    </div>
                                </form>
                            </div>

                            <div class="mt-5 text-center">
                                <p class="mb-0">
                                    Don't have an account ? <a href="/authenticationInner/register/auth-signup-cover"
                                        class="fw-semibold text-primary text-decoration-underline">
                                        Signup</a>
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

    <footer class="footer">
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