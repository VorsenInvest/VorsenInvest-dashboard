<script>
	import Link from "svelte-link";
	import { Card, Col, Container, Row } from "sveltestrap";

	import AuthSlider from "../../AuthSlider.svelte";
</script>

<svelte:head>
	<title>Log Out | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="auth-page-wrapper auth-bg-cover py-5 d-flex justify-content-center align-items-center min-vh-100">
	<div class="bg-overlay" />
	<div class="auth-page-content overflow-hidden pt-lg-5">
		<Container>
			<Row>
				<Col lg={12}>
				<Card class="overflow-hidden card-bg-fill border-0 card-border-effect-none">
					<Row class="justify-content-center g-0">
						<AuthSlider />

						<Col lg={6}>
						<div class="p-lg-5 p-4 text-center ">
							<lord-icon src="//cdn.lordicon.com/hzomhqxz.json" trigger="loop"
								colors="primary:#8c68cd,secondary:#4788ff" style="width: 180px; height: 180px" />

							<div class="mt-4 pt-2">
								<h5>You are Logged Out</h5>
								<p class="text-muted">
									Thank you for using <span class="fw-semibold">velzon</span> admin template
								</p>
								<div class="mt-4">
									<Link href="/authenticationInner/login/auth-signin-basic"
										class="btn btn-primary w-100">Sign In</Link>
								</div>
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