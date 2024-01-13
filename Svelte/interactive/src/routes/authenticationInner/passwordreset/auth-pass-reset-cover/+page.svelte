<script>
	import { Button, Card, Col, Container, Row,Label } from "sveltestrap";

	import AuthSlider from "../../AuthSlider.svelte";
	import Link from "svelte-link";
</script>

<svelte:head>
	<title>Reset Password | Velzon - Svelte Admin & Dashboard Template</title>
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
									<h5 class="text-primary">
										Forgot Password?
									</h5>
									<p class="text-muted">
										Reset password with velzon
									</p>

									<div class="mt-2 text-center">
										<lord-icon
											src="//cdn.lordicon.com/rhvddzym.json"
											trigger="loop"
											colors="primary:#0ab39c"
											class="avatar-xl"
											style="width: 120px;height: 120px"
										/>
									</div>

									<div class="alert alert-borderless alert-warning text-center mb-2 mx-2"
										role="alert"
									>
										Enter your email and instructions will
										be sent to you!
									</div>
									<div class="p-2">
										<form>
											<div class="mb-4">
												<Label
													class="form-label"
													for="email">Email</Label
												>
												<input
													type="email"
													class="form-control"
													id="email"
													placeholder="Enter email address"
												/>
											</div>

											<div class="text-center mt-4">
												<Button
													color="info"
													class="w-100"
													type="submit"
													>Send Reset Link</Button
												>
											</div>
										</form>
									</div>

									<div class="mt-5 text-center">
										<p class="mb-0">
											Wait, I remember my password... <Link
												href="/authenticationInner/login/auth-signin-cover"
												class="fw-semibold text-primary text-decoration-underline"
											>
												Click here
											</Link>
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
