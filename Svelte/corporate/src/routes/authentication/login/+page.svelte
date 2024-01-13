<script>
	import { Container, Row, Col, Card, CardBody, Label } from "sveltestrap";
	import Link from "svelte-link";
	import ParticlesAuth from "../../authenticationInner/ParticlesAuth.svelte";
	import logolight from '../../../assets/images/logo-light.png'
	import { goto } from '$app/navigation';

	let username = 'admin@themesbrand.com';
	let password = '123456';
	async function onSubmit() {
		try {
			const response = await fetch('https://api-node.themesbrand.website/auth/signin', {
				method: 'POST',
				body: JSON.stringify({ email: username, password: password }),
				headers: {
					'Content-Type': 'application/json'
				}
			});

			const data = await response.json();

			if (response.ok && data.status === "success") {
				localStorage.setItem('authUser', JSON.stringify(data));
				// window.location.pathname = "/dashboard";
				goto("/dashboard")
			} else {
				const error = data.message || 'An error occurred';
				return error;
			}
		} catch (error) {
			console.error('Error:', error);
			return 'An error occurred';
		}
	}

</script>

<svelte:head>
	<title>Sign In | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<ParticlesAuth>
	<div class="auth-page-content">
		<Container>
			<Row>
				<Col lg={12}>
				<div class="text-center mt-sm-5 mb-4 text-white-50">
					<div>
						<Link href="/dashboard" class="d-inline-block auth-logo">
						<img src={logolight} alt="" height="20" />
						</Link>
					</div>
					<p class="mt-3 fs-15 fw-medium">
						Premium Admin & Dashboard Template
					</p>
				</div>
				</Col>
			</Row>
			<!-- end row -->

			<Row class="justify-content-center">
				<Col md={8} lg={6} xl={5}>
				<Card class="mt-4">
					<CardBody class="p-4">
						<div class="text-center mt-2">
							<h5 class="text-primary">Welcome Back !</h5>
							<p class="text-muted">
								Sign in to continue to Velzon.
							</p>
						</div>
						<div class="p-2 mt-4">
							<form class="form" on:submit|preventDefault={onSubmit}>
								<div class="mb-3">
									<Label for="username" class="form-label">Username</Label>
									<input type="text" class="form-control" id="username" placeholder="Enter username"
										bind:value={username} />
								</div>

								<div class="mb-3">
									<div class="float-end">
										<Link href="auth-pass-reset-basic" class="text-muted">Forgot password?</Link>
									</div>
									<Label class="form-label" for="password-input">Password</Label>
									<div class="position-relative auth-pass-inputgroup mb-3">
										<input type="password" class="form-control pe-5" placeholder="Enter password"
											id="password-input" bind:value={password} />
										<button
											class="btn btn-link position-absolute end-0 top-0 text-decoration-none text-muted"
											type="button" id="password-addon"><i
												class="ri-eye-fill align-middle" /></button>
									</div>
								</div>

								<div class="form-check">
									<input class="form-check-input" type="checkbox" value="" id="auth-remember-check" />
									<Label class="form-check-label" for="auth-remember-check">Remember me</Label>
								</div>

								<div class="mt-4">
									<button class="btn btn-success w-100" type="submit">Sign In</button>
								</div>
							</form>
						</div>
					</CardBody>
					<!-- end card body -->
				</Card>
				<!-- end card -->

				<div class="mt-4 text-center">
					<p class="mb-0">
						Don't have an account ?
						<Link href="/authenticationInner/register/auth-signup-basic"
							class="fw-semibold text-primary text-decoration-underline">
						Signup
						</Link>
					</p>
				</div>
				</Col>
			</Row>
			<!-- end row -->
		</Container>
		<!-- end container -->
	</div>
</ParticlesAuth>