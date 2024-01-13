<script>
    import Link from "svelte-link";
    import { Card, Col, Container, Row, Label } from "sveltestrap";

    import AuthSlider from "../../AuthSlider.svelte";
</script>

<svelte:head>
    <title>Sign Up | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="auth-page-wrapper auth-bg-cover py-5 d-flex justify-content-center align-items-center min-vh-100">
    <div class="bg-overlay" />
    <div class="auth-page-content overflow-hidden pt-lg-5">
        <Container>
            <Row>
                <Col lg={12}>
                <Card class="overflow-hidden m-0">
                    <Row class="justify-content-center g-0">
                        <AuthSlider />

                        <div class="col-lg-6">
                            <div class="p-lg-5 p-4">
                                <div>
                                    <h5 class="text-primary">
                                        Register Account
                                    </h5>
                                    <p class="text-muted">
                                        Get your Free Velzon account now.
                                    </p>
                                </div>

                                <div class="mt-4">
                                    <form class="needs-validation" noValidate action="/dashboard">
                                        <div class="mb-3">
                                            <Label for="useremail" class="form-label">Email <span
                                                    class="text-danger">*</span></Label>
                                            <input type="email" class="form-control" id="useremail"
                                                placeholder="Enter email address" required />
                                            <div class="invalid-feedback">
                                                Please enter email
                                            </div>
                                        </div>
                                        <div class="mb-3">
                                            <Label for="username" class="form-label">Username <span
                                                    class="text-danger">*</span></Label>
                                            <input type="text" class="form-control" id="username"
                                                placeholder="Enter username" required />
                                            <div class="invalid-feedback">
                                                Please enter username
                                            </div>
                                        </div>

                                        <div class="mb-3">
                                            <Label for="userpassword" class="form-label">Password <span
                                                    class="text-danger">*</span></Label>
                                            <input type="password" class="form-control" id="userpassword"
                                                placeholder="Enter password" required />
                                            <div class="invalid-feedback">
                                                Please enter password
                                            </div>
                                        </div>

                                        <div class="mb-4">
                                            <p class="mb-0 fs-13 text-muted fst-italic">
                                                By registering you agree to
                                                the Velzon
                                                <Link href={null}
                                                    class="text-primary text-decoration-underline fst-normal fw-semibold">
                                                Terms of Use</Link>
                                            </p>
                                        </div>
                                        <div id="password-contain" class="p-3 bg-light mb-2 rounded">
                                            <h5 class="fs-13">Password must contain:</h5>
                                            <p id="pass-length" class="invalid fs-13 mb-2">Minimum <b>8 characters</b></p>
                                            <p id="pass-lower" class="invalid fs-13 mb-2">At <b>lowercase</b> letter (a-z)</p>
                                            <p id="pass-upper" class="invalid fs-13 mb-2">At least <b>uppercase</b> letter (A-Z)</p>
                                            <p id="pass-number" class="invalid fs-13 mb-0">A least <b>number</b> (0-9)</p>
                                        </div>
                                        <div class="mt-4">
                                            <button class="btn btn-success w-100" type="submit">Sign Up</button>
                                        </div>
                                        

                                        <div class="mt-4 text-center">
                                            <div class="signin-other-title">
                                                <h5 class="fs-14 mb-4 title text-muted">
                                                    Create account with
                                                </h5>
                                            </div>

                                            <div>
                                                <button type="button"
                                                    class="btn btn-primary btn-icon waves-effect waves-light"><i
                                                        class="ri-facebook-fill fs-16" /></button>
                                                <button type="button"
                                                    class="btn btn-danger btn-icon waves-effect waves-light"><i
                                                        class="ri-google-fill fs-16" /></button>
                                                <button type="button"
                                                    class="btn btn-dark btn-icon waves-effect waves-light"><i
                                                        class="ri-github-fill fs-16" /></button>
                                                <button type="button"
                                                    class="btn btn-info btn-icon waves-effect waves-light"><i
                                                        class="ri-twitter-fill fs-16" /></button>
                                            </div>
                                        </div>
                                    </form>
                                </div>

                                <div class="mt-5 text-center">
                                    <p class="mb-0">
                                        Already have an account ?
                                        <Link href="/authenticationInner/login/auth-signin-cover"
                                            class="fw-bold text-primary text-decoration-underline">
                                        Signin</Link>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </Row>
                </Card>
                </Col>
            </Row>
        </Container>
    </div>

    <footer class="footer">
        <Container>
            <div class="row">
                <div class="col-lg-12">
                    <div class="text-center">
                        <p class="mb-0">
                            &copy; {new Date().getFullYear()} Velzon. Crafted with
                            <i class="mdi mdi-heart text-danger" /> by Themesbrand
                        </p>
                    </div>
                </div>
            </div>
        </Container>
    </footer>
</div>