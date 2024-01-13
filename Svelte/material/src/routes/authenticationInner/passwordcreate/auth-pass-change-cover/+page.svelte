<script>
import { Button, Card, Col, Container, Row, Form, Label, Input } from 'sveltestrap';

import AuthSlider from '../../AuthSlider.svelte';
import Link from 'svelte-link'
let passwordShow = false;
let confrimPasswordShow = false;
const setPasswordShow = () => {
    passwordShow = !passwordShow;
}
const setConfrimPasswordShow = () => {
    confrimPasswordShow = !confrimPasswordShow;
}
</script>
<div class="auth-page-wrapper auth-bg-cover py-5 d-flex justify-content-center align-items-center min-vh-100">
    <div class="bg-overlay"></div>
    <div class="auth-page-content overflow-hidden pt-lg-5">
        <Container>
            <Row>
                <Col lg={12}>
                    <Card class="overflow-hidden">
                        <Row class="justify-content-center g-0">
                            <AuthSlider />
                            <Col lg={6}>
                                <div class="p-lg-5 p-4">
                                    <h5 class="text-primary">Create new password</h5>
                                    <p class="text-muted">Your new password must be different from previous used password.</p>

                                    <div class="p-2">
                                        <Form>
                                            <div class="mb-3">
                                                <Label class="form-label" htmlfor="password-input">Password</Label>
                                                <div class="position-relative auth-pass-inputgroup">
                                                    <Input
                                                        type={passwordShow ? "text" : "password"}
                                                        class="form-control pe-5 password-input"
                                                        placeholder="Enter password"
                                                        id="password-input"
                                                        name="password"
                                                    />
                                                    <Button color="link" on:click={() => setPasswordShow()} class="position-absolute end-0 top-0 text-decoration-none text-muted password-addon shadow-none"
                                                        id="password-addon"><i class="ri-eye-fill align-middle"></i></Button>
                                                </div>
                                                <div id="passwordInput" class="form-text">Must be at least 8 characters.</div>
                                            </div>

                                            <div class="mb-3">
                                                <Label class="form-label" htmlfor="confirm-password-input">Confirm Password</Label>
                                                <div class="position-relative auth-pass-inputgroup mb-3">
                                                    <Input
                                                        type={confrimPasswordShow ? "text" : "password"}
                                                        class="form-control pe-5 password-input"
                                                        placeholder="Confirm password"
                                                        id="confirm-password-input"
                                                        name="confrim_password"
                                                        />
                                                    <Button color="link" on:click={() => setConfrimPasswordShow()} class="position-absolute end-0 top-0 text-decoration-none text-muted password-addon shadow-none">
                                                    <i class="ri-eye-fill align-middle"></i></Button>
                                                </div>
                                            </div>

                                            <div id="password-contain" class="p-3 bg-light mb-2 rounded">
                                                <h5 class="fs-13">Password must contain:</h5>
                                                <p id="pass-length" class="invalid fs-12 mb-2">Minimum <b>8 characters</b></p>
                                                <p id="pass-lower" class="invalid fs-12 mb-2">At <b>lowercase</b> letter (a-z)</p>
                                                <p id="pass-upper" class="invalid fs-12 mb-2">At least <b>uppercase</b> letter (A-Z)</p>
                                                <p id="pass-number" class="invalid fs-12 mb-0">A least <b>number</b> (0-9)</p>
                                            </div>

                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" value="" id="auth-remember-check" />
                                                <Label class="form-check-label" htmlfor="auth-remember-check">Remember me</Label>
                                            </div>

                                            <div class="mt-4">
                                                <Button color="success" class="w-100" type="submit">Reset Password</Button>
                                            </div>
                                        </Form>
                                    </div>

                                    <div class="mt-5 text-center">
                                        <p class="mb-0">Wait, I remember my password... <Link href="/authenticationInner/login/auth-signin-cover" class="fw-semibold text-primary text-decoration-underline"> Click here </Link> </p>
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
                        <p class="mb-0">&copy; {new Date().getFullYear()} Velzon. Crafted with <i class="mdi mdi-heart text-danger"></i> by Themesbrand</p>
                    </div>
                </Col>
            </Row>
        </Container>
    </footer>
</div>