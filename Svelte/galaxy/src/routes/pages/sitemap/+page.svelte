<svelte:head>
  <title>Sitemap | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import { Card, CardBody, CardHeader, Col, Container, Row } from 'sveltestrap';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import Link from 'svelte-link';
</script>

<div>
	<div class="page-content">
		<Container fluid>
			<BreadCrumb title="SiteMap" pageTitle="Pages" />
			<Row>
				<Col lg={12}>
					<Card>
						<CardHeader>
							<h4 class="card-title mb-0">Responsive Sitemap</h4>
						</CardHeader>
						<CardBody>
							<div class="sitemap-content">
								<figure class="sitemap-horizontal">
									<ul class="administration">
										<li>
											<ul class="director">
												<li>
													<Link href={null} class="fw-semibold"><span>Velzon Admin</span></Link>
													<ul class="subdirector">
														<li><Link href={null} class="fw-semibold"><span>Contact Us</span></Link></li>
													</ul>
													<ul class="departments">
														<li><Link href={null} class="fw-semibold"><span>Main Pages</span></Link></li>

														<li class="department">
															<Link href={null} class="fw-semibold"><span>Account Management</span></Link
															>
															<ul>
																<li><Link href={null}><span>Sign Up</span></Link></li>
																<li><Link href={null}><span>Login</span></Link></li>
																<li><Link href={null}><span>Profile Settings</span></Link></li>
																<li><Link href={null}><span>Modify Reservation</span></Link></li>
																<li><Link href={null}><span>Cancel Reservation</span></Link></li>
																<li><Link href={null}><span>Write Reviews</span></Link></li>
															</ul>
														</li>
														<li class="department">
															<Link href={null} class="fw-semibold"><span>About Us</span></Link>
															<ul>
																<li><Link href={null}><span>Overview</span></Link></li>
																<li><Link href={null}><span>Connect Via Social Media</span></Link></li>
																<li><Link href={null}><span>Careers</span></Link></li>
																<li><Link href={null}><span>Team Members</span></Link></li>
																<li><Link href={null}><span>Policies</span></Link></li>
															</ul>
														</li>
														<li class="department">
															<Link href={null} class="fw-semibold"><span>Book a Trip</span></Link>
															<ul>
																<li><Link href={null}><span>Travel Details</span></Link></li>
																<li><Link href={null}><span>Reservation Process</span></Link></li>
																<li><Link href={null}><span>Payment Option</span></Link></li>
																<li><Link href={null}><span>Comfirmation</span></Link></li>
															</ul>
														</li>
														<li class="department">
															<Link href={null} class="fw-semibold"><span>Destination</span></Link>
															<ul>
																<li><Link href={null}><span>Architecture</span></Link></li>
																<li><Link href={null}><span>Art</span></Link></li>
																<li><Link href={null}><span>Entertainment</span></Link></li>
																<li><Link href={null}><span>History</span></Link></li>
																<li><Link href={null}><span>Science</span></Link></li>
																<li><Link href={null}><span>Sports</span></Link></li>
																<li><Link href={null}><span>Music</span></Link></li>
																<li><Link href={null}><span>Tracking Camp</span></Link></li>
															</ul>
														</li>
														<li class="department">
															<Link href={null} class="fw-semibold"><span>Travel Tips</span></Link>
															<ul>
																<li><Link href={null}><span>General Travel</span></Link></li>
																<li><Link href={null}><span>Helpth Concerns</span></Link></li>
																<li><Link href={null}><span>Safety Measures</span></Link></li>
																<li><Link href={null}><span>FAQ's</span></Link></li>
															</ul>
														</li>
													</ul>
												</li>
											</ul>
										</li>
									</ul>
								</figure>
							</div>
						</CardBody>
					</Card>
				</Col>
			</Row>

			<Row>
				<Col lg={12}>
					<Card>
						<CardHeader>
							<h4 class="card-title mb-0">Horizontal</h4>
						</CardHeader>
						<CardBody>
							<div class="hori-sitemap">
								<ul class="list-unstyled mb-0">
									<li class="p-0 parent-title">
										<Link href={null} class="fw-semibold fs-14">My Account</Link>
									</li>
									<ul class="list-unstyled row g-0">
										<li class="col-sm-3">
											<Link href={null} class="fw-semibold sub-title">About Us</Link>
											<ul class="list-unstyled row g-0 second-list">
												<li class="col-sm-6">
													<Link href={null}>Overview</Link>
												</li>
												<li class="col-sm-6">
													<Link href={null}>History</Link>
												</li>
											</ul>
										</li>
										<li class="col-sm-3">
											<Link href={null} class="fw-semibold">My self-care Plan</Link>
											<ul class="list-unstyled second-list pt-0">
												<li>
													<div>
														<Link href={null}>Basic</Link>
														<Link href={null}>Early Physiotherapy</Link>
														<Link href={null}>Intermediate Physiotherapy</Link>
														<Link href={null}>Return to Normal Activity</Link>
													</div>
												</li>
											</ul>
										</li>
										<li class="col-sm-3">
											<Link href={null} class="fw-semibold sub-title">Support Us</Link>
											<ul class="list-unstyled row g-0 sub-list">
												<li class="col-sm-6">
													<Link href={null}>Contact Us</Link>
												</li>
												<li class="col-sm-6">
													<Link href={null}>Customer Services</Link>
													<ul class="list-unstyled second-list">
														<li>
															<div>
																<Link href={null}>Chat With Us</Link>
																<Link href={null}>Connect Information</Link>
																<Link href={null}>FAQ'S</Link>
															</div>
														</li>
													</ul>
												</li>
											</ul>
										</li>
										<li class="col-sm-3">
											<Link href={null} class="fw-semibold">Terms & Conditions</Link>
										</li>
									</ul>
								</ul>
							</div>
						</CardBody>
					</Card>
				</Col>
			</Row>

			<Row>
				<Col lg={12}>
					<Card>
						<CardHeader>
							<h4 class="card-title mb-0">Vertical</h4>
						</CardHeader>
						<CardBody>
							<Row>
								<Col sm={6}>
									<div class="verti-sitemap">
										<ul class="list-unstyled mb-0">
											<li class="p-0 parent-title">
												<Link href={null} class="fw-medium fs-14">Nancy Martino - Project Director</Link>
											</li>
											<li>
												<div class="first-list">
													<div class="list-wrap">
														<Link href={null} class="fw-medium text-primary"
															>Erica Kernan - Team Leader</Link
														>
													</div>
													<ul class="second-list list-unstyled">
														<li>
															<Link href={null}>Jason McQuaid - Member</Link>
														</li>
														<li>
															<Link href={null}>Elwood Arter - Member</Link>
														</li>
													</ul>
												</div>
												<div class="first-list">
													<div class="list-wrap">
														<Link href={null} class="fw-medium text-primary"
															>Mary Jones - Project Manager</Link
														>
													</div>
													<ul class="second-list list-unstyled">
														<li><Link href={null}>Jordyn Jones - Designer</Link></li>
														<li><Link href={null}>Ashlee Haney - Developer</Link></li>
														<li><Link href={null}>Rashad Charles - BackEnd Developer</Link></li>
														<li><Link href={null}>Walter Newman - Frontend Developer</Link></li>
														<li><Link href={null}>Adam Moss - Designer</Link></li>
													</ul>
												</div>
												<div class="first-list">
													<div class="list-wrap">
														<Link href={null} class="fw-medium text-primary"
															>Tilly Kent - Executive Manager</Link
														>
													</div>
													<ul class="second-list list-unstyled">
														<li>
															<Link href={null}>Tyler Porter - Account Executive</Link>
														</li>
														<li>
															<Link href={null}>Alicia Thompson - Sales Executive</Link>
															<ul class="third-list list-unstyled">
																<li><Link href={null}>Jack Coates - Member</Link></li>
																<li><Link href={null}>Owen Jarvis - Member</Link></li>
																<li><Link href={null}>Ashlee Haney - Member</Link></li>
																<li><Link href={null}>Archie Cook - Member</Link></li>
															</ul>
														</li>
													</ul>
												</div>
												<div class="first-list">
													<div class="list-wrap">
														<Link href={null} class="fw-medium text-primary">Rachel Rose - HR</Link>
													</div>
												</div>
											</li>
										</ul>
									</div>
								</Col>

								<Col sm={6}>
									<div class="verti-sitemap">
										<ul class="mb-0 list-unstyled">
											<li class="p-0 parent-title">
												<Link href={null} class="fw-medium fs-14">Velzon</Link>
											</li>
											<li>
												<div class="first-list">
													<div class="list-wrap">
														<Link href={null} class="fw-medium text-primary"
															><i class="ri-airplay-line me-1 align-bottom" /> Dashboards</Link>
													</div>
													<ul class="second-list list-unstyled">
														<li>
															<Link href={null}>Analytics</Link>
														</li>
														<li>
															<Link href={null}>CRM</Link>
														</li>
													</ul>
												</div>
												<div class="first-list">
													<div class="list-wrap">
														<Link href={null} class="fw-medium text-primary"
															><i class="ri-pencil-ruler-2-line me-1 align-bottom" /> App Pages</Link
														>
													</div>
													<ul class="second-list list-unstyled">
														<li><Link href={null}>Calender</Link></li>
														<li><Link href={null}>Chat</Link></li>
														<li><Link href={null}>Email</Link></li>
														<li><Link href={null}>Ecommerce</Link></li>
														<li><Link href={null}>Projects</Link></li>
														<li><Link href={null}>Tasks</Link></li>
													</ul>
												</div>
												<div class="first-list">
													<div class="list-wrap">
														<Link href={null} class="fw-medium text-primary"
															><i class="ri-file-list-3-line me-1 align-bottom" /> Pages</Link
														>
													</div>
												</div>
												<div class="first-list">
													<div class="list-wrap">
														<Link href={null} class="fw-medium text-primary"
															><i class="ri-stack-line me-1 align-bottom" /> Components</Link
														>
													</div>
													<ul class="second-list list-unstyled">
														<li>
															<Link href={null}>Base UI</Link>
														</li>
														<li>
															<Link href={null}>Advance UI</Link>
															<ul class="third-list list-unstyled">
																<li><Link href={null}>Sweet Alerts</Link></li>
																<li><Link href={null}>Range Slider</Link></li>
																<li><Link href={null}>Nestable List</Link></li>
															</ul>
														</li>
													</ul>
												</div>
											</li>
										</ul>
									</div>
								</Col>
							</Row>
						</CardBody>
					</Card>
				</Col>
			</Row>
		</Container>
	</div>
</div>