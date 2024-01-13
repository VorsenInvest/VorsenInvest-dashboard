<svelte:head>
  <title>Wizard | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Container,
		Form,
		Input,
		Label,
		Nav,
		NavItem,
		NavLink,
		Row,
		TabContent,
		TabPane,
		Progress
	} from 'sveltestrap';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import userdummyimg from '../../../assets/images/users/user-dummy-img.jpg'
	import logodark from '../../../assets/images/logo-dark.png';
	let progressbarvalue = 0;
	let activeTab = 1;
	let activeArrowTab = 4;
	let activeVerticalTab = 7;
    let passedSteps = [1];
    let passedarrowSteps = [1];
    let passedverticalSteps = [1];
	function toggleTab(tab, value) {
		if (activeTab !== tab) {
			var modifiedSteps = [...passedSteps, tab];

			if (tab >= 1 && tab <= 4) {
				activeTab = tab;
				passedSteps = modifiedSteps;
			}
		}
		progressbarvalue = value;
	}

	function toggleArrowTab(tab) {
		if (activeArrowTab !== tab) {
			var modifiedSteps = [...passedarrowSteps, tab];

			if (tab >= 4 && tab <= 7) {
				activeArrowTab = tab;
				passedarrowSteps = modifiedSteps;
			}
		}
	}

	function toggleVerticalTab(tab) {
		if (activeVerticalTab !== tab) {
			var modifiedSteps = [...passedverticalSteps, tab];

			if (tab >= 7 && tab <= 11) {
				activeVerticalTab = tab;
				passedverticalSteps = modifiedSteps;
			}
		}
	}
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Forms" pageTitle="Wizard" />
		<Row>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Progress Nav Steps</h4>
					</CardHeader>
					<CardBody>
						<Form class="form-steps" action="#">
							<div class="text-center pt-3 pb-4 mb-1">
								<h5>Signup Your Account</h5>
							</div>

							<div class="progress-nav mb-4">
								<Progress value={progressbarvalue} style="height: 1px" />

								<Nav class="nav-pills progress-bar-tab custom-nav" role="tablist">
									<NavItem>
										<NavLink
											href={null}
											id="pills-gen-info-tab"
											class={activeTab <= 4 && activeTab >= 0
												? 'rounded-pill done d-flex justify-content-center align-items-center'
												: 'rounded-pill d-flex justify-content-center align-items-center'}
											active={activeTab == 1}
											on:click={() => {
												toggleTab(1, 0);
											}}
											tag="button"
										>
											1
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											href={null}
											id="pills-gen-info-tab"
											class={activeTab <= 4 && activeTab > 1 ? 'rounded-pill done d-flex justify-content-center align-items-center' : 'rounded-pill d-flex justify-content-center align-items-center'}
											active={activeTab == 2}
											on:click={() => {
												toggleTab(2, 50);
											}}
											tag="button"
										>
											2
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											href={null}
											id="pills-gen-info-tab"
											class={activeTab <= 4 && activeTab > 2 ? 'rounded-pill done d-flex justify-content-center align-items-center' : 'rounded-pill d-flex justify-content-center align-items-center'}
											active={activeTab == 3}
											on:click={() => {
												toggleTab(3, 100);
											}}
											tag="button"
										>
											3
										</NavLink>
									</NavItem>
								</Nav>
							</div>

							<TabContent>
								<TabPane class={activeTab == 1 ? 'active' : ''}>
									<div>
										<div class="mb-4">
											<div>
												<h5 class="mb-1">General Information</h5>
												<p class="text-muted">Fill all Information as below</p>
											</div>
										</div>
										<Row>
											<Col lg={6}>
												<div class="mb-3">
													<Label class="form-label" for="gen-info-email-input">Email</Label>
													<Input
														type="text"
														class="form-control"
														id="gen-info-email-input"
														placeholder="Enter Email"
													/>
												</div>
											</Col>
											<Col lg={6}>
												<div class="mb-3">
													<Label class="form-label" for="gen-info-username-input">
														User Name
													</Label>
													<Input
														type="text"
														class="form-control"
														id="gen-info-username-input"
														placeholder="Enter User Name"
													/>
												</div>
											</Col>
										</Row>
										<div class="mb-3">
											<Label class="form-label" for="gen-info-password-input">Password</Label>
											<Input
												type="password"
												class="form-control"
												id="gen-info-password-input"
												placeholder="Enter Password"
											/>
										</div>
									</div>
									<div class="d-flex align-items-start gap-3 mt-4">
										<button
											type="button"
											class="btn btn-success btn-label right ms-auto nexttab nexttab"
											on:click={() => {
												toggleTab(activeTab + 1, 50);
											}}
										>
											<i class="ri-arrow-right-line label-icon align-middle fs-16 ms-2" />
											Go to more info
										</button>
									</div>
								</TabPane>

								<TabPane class={activeTab == 2 ? 'active' : ''}>
									<div>
										<div class="text-center">
											<div class="profile-user position-relative d-inline-block mx-auto mb-2">
												<img
													src={userdummyimg}
													class="rounded-circle avatar-lg img-thumbnail user-profile-image"
													alt=""
												/>
												<div class="avatar-xs p-0 rounded-circle profile-photo-edit">
													<Input
														id="profile-img-file-input"
														type="file"
														class="profile-img-file-input"
														accept="image/png, image/jpeg"
													/>
													<Label
														for="profile-img-file-input"
														class="profile-photo-edit avatar-xs"
													>
														<span class="avatar-title rounded-circle bg-light text-body">
															<i class="ri-camera-fill" />
														</span>
													</Label>
												</div>
											</div>
											<h5 class="fs-14">Add Image</h5>
										</div>
										<div>
											<Label class="form-label" for="gen-info-description-input">
												Description
											</Label>
											<Input
												type="textarea"
												class="form-control"
												placeholder="Enter Description"
												id="gen-info-description-input"
												rows="2"
											/>
										</div>
									</div>
									<div class="d-flex align-items-start gap-3 mt-4">
										<button
											type="button"
											class="btn btn-link text-decoration-none btn-label previestab"
											on:click={() => {
												toggleTab(activeTab - 1, 0);
											}}
										>
											<i class="ri-arrow-left-line label-icon align-middle fs-16 me-2" />{' '}
											Back to General
										</button>
										<button
											type="button"
											class="btn btn-success btn-label right ms-auto nexttab nexttab"
											on:click={() => {
												toggleTab(activeTab + 1, 100);
											}}
										>
											<i class="ri-arrow-right-line label-icon align-middle fs-16 ms-2" />
											Submit
										</button>
									</div>
								</TabPane>

								<TabPane class={activeTab == 3 ? 'active' : ''}>
									<div>
										<div class="text-center">
											<div class="mb-4">
												<lord-icon
													src="//cdn.lordicon.com/lupuorrc.json"
													trigger="loop"
													colors="primary:#25a0e2,secondary:#00bd9d"
													style="width:120px;height:120px"
												/>
											</div>
											<h5>Well Done !</h5>
											<p class="text-muted">You have Successfully Signed Up</p>
										</div>
									</div>
								</TabPane>
							</TabContent>
						</Form>
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Arrow Nav Steps</h4>
					</CardHeader>
					<CardBody class="form-steps">
						<Form>
							<div class="text-center pt-3 pb-4 mb-1">
								<img src={logodark} alt="" height="17" />
							</div>
							<div class="step-arrow-nav mb-4">
								<Nav class="nav-pills custom-nav nav-justified" role="tablist">
									<NavItem>
										<NavLink
											href={null}
											id="steparrow-gen-info-tab"
											class={activeArrowTab <= 6 && activeArrowTab > 3 ? 'done' : ''}
											active={activeArrowTab == 4}
											on:click={() => {
												toggleArrowTab(4);
											}}
										>
											General
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											href={null}
											id="steparrow-gen-info-tab"
											class={activeArrowTab <= 6 && activeArrowTab > 4 ? 'done' : ''}
											active={activeArrowTab == 5}
											on:click={() => {
												toggleArrowTab(5);
											}}
										>
											Description
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											href={null}
											id="steparrow-gen-info-tab"
											class={activeArrowTab <= 6 && activeArrowTab > 5 ? 'done' : ''}
											active={activeArrowTab == 6}
											on:click={() => {
												toggleArrowTab(6);
											}}
										>
											Finish
										</NavLink>
									</NavItem>
								</Nav>
							</div>

							<TabContent>
								<TabPane id="steparrow-gen-info" class={activeArrowTab == 4 ? 'active' : ''}>
									<div>
										<Row>
											<Col lg={6}>
												<div class="mb-3">
													<Label class="form-label" for="steparrow-gen-info-email-input">
														Email
													</Label>
													<Input
														type="text"
														class="form-control"
														id="steparrow-gen-info-email-input"
														placeholder="Enter Email"
													/>
												</div>
											</Col>
											<Col lg={6}>
												<div class="mb-3">
													<Label class="form-label" for="steparrow-gen-info-username-input">
														User Name
													</Label>
													<Input
														type="text"
														class="form-control"
														id="steparrow-gen-info-username-input"
														placeholder="Enter User Name"
													/>
												</div>
											</Col>
										</Row>
										<div class="mb-3">
											<Label class="form-label" for="steparrow-gen-info-password-input">
												Password
											</Label>
											<Input
												type="password"
												class="form-control"
												id="steparrow-gen-info-password-input"
												placeholder="Enter Password"
											/>
										</div>
										<div>
											<Label class="form-label" for="steparrow-gen-info-confirm-password-input">
												Confirm Password
											</Label>
											<Input
												type="password"
												class="form-control"
												id="steparrow-gen-info-confirm-password-input"
												placeholder="Enter Confirm Password"
											/>
										</div>
									</div>
									<div class="d-flex align-items-start gap-3 mt-4">
										<button
											type="button"
											class="btn btn-success btn-label right ms-auto nexttab nexttab"
											on:click={() => {
												toggleArrowTab(activeArrowTab + 1);
											}}
										>
											<i class="ri-arrow-right-line label-icon align-middle fs-16 ms-2" />
											Go to more info
										</button>
									</div>
								</TabPane>

								<TabPane id="steparrow-description-info" class={activeArrowTab == 5 ? 'active' : ''}>
									<div>
										<div class="mb-3">
											<Label for="formFile" class="form-label">Upload Image</Label>
											<Input class="form-control" type="file" id="formFile" />
										</div>
										<div>
											<Label class="form-label" for="des-info-description-input">
												Description
											</Label>
											<textarea
												class="form-control"
												placeholder="Enter Description"
												id="des-info-description-input"
												rows="3"
											/>
										</div>
									</div>
									<div class="d-flex align-items-start gap-3 mt-4">
										<button
											type="button"
											class="btn btn-light btn-label previestab"
											on:click={() => {
												toggleArrowTab(activeArrowTab - 1);
											}}
										>
											<i class="ri-arrow-left-line label-icon align-middle fs-16 me-2" />{' '}
											Back to General
										</button>
										<button
											type="button"
											class="btn btn-success btn-label right ms-auto nexttab nexttab"
											on:click={() => {
												toggleArrowTab(activeArrowTab + 1);
											}}
										>
											<i class="ri-arrow-right-line label-icon align-middle fs-16 ms-2" />
											Submit
										</button>
									</div>
								</TabPane>

								<TabPane id="pills-experience" class={activeArrowTab == 6 ? 'active' : ''}>
									<div class="text-center">
										<div class="avatar-md mt-5 mb-4 mx-auto">
											<div class="avatar-title bg-light text-success display-4 rounded-circle">
												<i class="ri-checkbox-circle-fill" />
											</div>
										</div>
										<h5>Well Done !</h5>
										<p class="text-muted">You have Successfully Signed Up</p>
									</div>
								</TabPane>
							</TabContent>
						</Form>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xl={12}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Vertical nav Steps</h4>
					</CardHeader>
					<CardBody class="form-steps">
						<form class="vertical-navs-step">
							<Row class="gy-5">
								<Col lg={3}>
									<Nav class="flex-column custom-nav nav-pills">
										<NavItem>
											<NavLink
												href={null}
												class={activeVerticalTab <= 11 && activeVerticalTab > 7 ? 'done' : ''}
												active={activeVerticalTab == 7}
												on:click={() => {
													toggleVerticalTab(7);
												}}
											>
												<span class="step-title me-2">
													<i class="ri-close-circle-fill step-icon me-2" />
													Step 1
												</span>
												Billing Info
											</NavLink>
										</NavItem>
										<NavItem>
											<NavLink
												href={null}
												class={activeVerticalTab <= 11 && activeVerticalTab >= 8 ? 'done' : ''}
												active={activeVerticalTab == 8}
												on:click={() => {
													toggleVerticalTab(8);
												}}
											>
												<span class="step-title me-2">
													<i class="ri-close-circle-fill step-icon me-2" />
													Step 2
												</span>
												Address
											</NavLink>
										</NavItem>
										<NavItem>
											<NavLink
												href={null}
												class={activeVerticalTab <= 11 && activeVerticalTab >= 9 ? 'done' : ''}
												active={activeVerticalTab == 9}
												on:click={() => {
													toggleVerticalTab(9);
												}}
											>
												<span class="step-title me-2">
													<i class="ri-close-circle-fill step-icon me-2" />
													Step 3
												</span>
												Payment
											</NavLink>
										</NavItem>
										<NavItem>
											<NavLink
												href={null}
												class={activeVerticalTab <= 11 && activeVerticalTab >= 10 ? 'done' : ''}
												active={activeVerticalTab == 10}
												on:click={() => {
													toggleVerticalTab(10);
												}}
											>
												<span class="step-title me-2">
													<i class="ri-close-circle-fill step-icon me-2" />
													Step 4
												</span>
												Finish
											</NavLink>
										</NavItem>
									</Nav>
								</Col>
								<Col lg={6}>
									<div class="px-lg-4">
										<TabContent>
											<TabPane class={activeVerticalTab == 7 ? 'active' : ''}>
												<div>
													<h5>Billing Info</h5>
													<p class="text-muted">Fill all information below</p>
												</div>

												<div>
													<Row class="g-3">
														<Col sm={6}>
															<Label for="firstName" class="form-label">First name</Label>
															<Input
																type="text"
																class="form-control"
																id="firstName"
																placeholder="Enter First Name"
																defaultValue=""
															/>
														</Col>

														<Col sm={6}>
															<Label for="lastName" class="form-label">Last name</Label>
															<Input
																type="text"
																class="form-control"
																id="lastName"
																placeholder="Enter Last Name"
																defaultValue=""
															/>
														</Col>

														<Col xs={12}>
															<Label for="username" class="form-label">Username</Label>
															<div class="input-group">
																<span class="input-group-text"> @ </span>
																<Input
																	type="text"
																	class="form-control"
																	id="username"
																	placeholder="Username"
																/>
															</div>
														</Col>

														<Col xs={12}>
															<Label for="email" class="form-label">
																Email{' '}
																<span class="text-muted"> (Optional) </span>
															</Label>
															<Input
																type="email"
																class="form-control"
																id="email"
																placeholder="Enter Email"
															/>
														</Col>
													</Row>
												</div>

												<div class="d-flex align-items-start gap-3 mt-4">
													<button
														type="button"
														class="btn btn-success btn-label right ms-auto nexttab nexttab"
														on:click={() => {
															toggleVerticalTab(activeVerticalTab + 1);
														}}
													>
														<i class="ri-arrow-right-line label-icon align-middle fs-16 ms-2" />
														Go to Shipping
													</button>
												</div>
											</TabPane>

											<TabPane class={activeVerticalTab == 8 ? 'active' : ''}>
												<div>
													<h5>Shipping Address</h5>
													<p class="text-muted">Fill all information below</p>
												</div>

												<div>
													<Row class="g-3">
														<Col xs={12}>
															<Label for="address" class="form-label">Address</Label>
															<Input
																type="text"
																class="form-control"
																id="address"
																placeholder="1234 Main St"
															/>
														</Col>

														<Col xs={12}>
															<Label for="address2" class="form-label">
																Address 2{' '}
																<span class="text-muted"> (Optional) </span>
															</Label>
															<Input
																type="text"
																class="form-control"
																id="address2"
																placeholder="Apartment or suite"
															/>
														</Col>

														<Col md={5}>
															<Label for="country" class="form-label">Country</Label>
															<select class="form-select" id="country">
																<option defaultValue="">Choose...</option>
																<option>United States</option>
															</select>
														</Col>

														<Col md={4}>
															<Label for="state" class="form-label">State</Label>
															<select class="form-select" id="state">
																<option defaultValue="">Choose...</option>
																<option>California</option>
															</select>
														</Col>

														<Col md={3}>
															<Label for="zip" class="form-label">Zip</Label>
															<Input type="text" class="form-control" id="zip" placeholder="" />
														</Col>
													</Row>

													<hr class="my-4 text-muted" />

													<div class="form-check mb-2">
														<input type="checkbox" class="form-check-input" id="same-address" />
														<Label class="form-check-label" for="same-address">
															Shipping address is the same as my billing address
														</Label>
													</div>

													<div class="form-check">
														<input type="checkbox" class="form-check-input" id="save-info" />
														<Label class="form-check-label" for="save-info">
															Save this information for next time
														</Label>
													</div>
												</div>
												<div class="d-flex align-items-start gap-3 mt-4">
													<button
														type="button"
														class="btn btn-light btn-label previestab"
														on:click={() => {
															toggleVerticalTab(activeVerticalTab - 1);
														}}
													>
														<i class="ri-arrow-left-line label-icon align-middle fs-16 me-2" />{' '}
														Back to Billing Info
													</button>
													<button
														type="button"
														class="btn btn-success btn-label right ms-auto nexttab"
														on:click={() => {
															toggleVerticalTab(activeVerticalTab + 1);
														}}
													>
														<i class="ri-arrow-right-line label-icon align-middle fs-16 ms-2" />
														Go to Payment
													</button>
												</div>
											</TabPane>

											<TabPane class={activeVerticalTab == 9 ? 'active' : ''}>
												<div>
													<h5>Payment</h5>
													<p class="text-muted">Fill all information below</p>
												</div>

												<div>
													<div class="my-3">
														<div class="form-check form-check-inline">
															<input
																id="credit"
																name="paymentMethod"
																type="radio"
																class="form-check-input"
																defaultChecked
																required
															/>
															<Label class="form-check-label" for="credit">Credit card</Label>
														</div>
														<div class="form-check form-check-inline">
															<input
																id="debit"
																name="paymentMethod"
																type="radio"
																class="form-check-input"
																required
															/>
															<Label class="form-check-label" for="debit">Debit card</Label>
														</div>
														<div class="form-check form-check-inline">
															<input
																id="paypal"
																name="paymentMethod"
																type="radio"
																class="form-check-input"
																required
															/>
															<Label class="form-check-label" for="paypal">PayPal</Label>
														</div>
													</div>

													<Row class="gy-3">
														<Col md={12}>
															<Label for="cc-name" class="form-label">Name on card</Label>
															<Input
																type="text"
																class="form-control"
																id="cc-name"
																placeholder=""
																required
															/>
															<small class="text-muted"> Full name as displayed on card </small>
															<div class="invalid-feedback">Name on card is required</div>
														</Col>

														<Col md={6}>
															<Label for="cc-number" class="form-label">
																Credit card number
															</Label>
															<Input
																type="text"
																class="form-control"
																id="cc-number"
																placeholder=""
																required
															/>
															<div class="invalid-feedback">Credit card number is required</div>
														</Col>

														<Col md={3}>
															<Label for="cc-expiration" class="form-label">Expiration</Label>
															<Input
																type="text"
																class="form-control"
																id="cc-expiration"
																placeholder=""
																required
															/>
															<div class="invalid-feedback">Expiration date required</div>
														</Col>

														<Col md={3}>
															<Label for="cc-cvv" class="form-label">CVV</Label>
															<Input
																type="text"
																class="form-control"
																id="cc-cvv"
																placeholder=""
																required
															/>
															<div class="invalid-feedback">Security code required</div>
														</Col>
													</Row>
												</div>

												<div class="d-flex align-items-start gap-3 mt-4">
													<button
														type="button"
														class="btn btn-light btn-label previestab"
														on:click={() => {
															toggleVerticalTab(activeVerticalTab - 1);
														}}
													>
														<i class="ri-arrow-left-line label-icon align-middle fs-16 me-2" />{' '}
														Back to Shipping Info
													</button>
													<button
														type="button"
														class="btn btn-success btn-label right ms-auto nexttab"
														on:click={() => {
															toggleVerticalTab(activeVerticalTab + 1);
														}}
													>
														<i
															class="ri-arrow-right-line label-icon align-middle fs-16 ms-2"
														/>{' '}
														Order Complete
													</button>
												</div>
											</TabPane>

											<TabPane class={activeVerticalTab == 10 ? 'active' : ''}>
												<div class="text-center pt-4 pb-2">
													<div class="mb-4">
														<lord-icon
															src="//cdn.lordicon.com/lupuorrc.json"
															trigger="loop"
															colors="primary:#0ab39c,secondary:#405189"
															style="width:120px;height:120px"
														/>
													</div>
													<h5>Your Order is Completed !</h5>
													<p class="text-muted">
														You Will receive an order confirmation email with details of your order.
													</p>
												</div>
											</TabPane>
										</TabContent>
									</div>
								</Col>

								<Col lg={3}>
									<div class="d-flex justify-content-between align-items-center mb-3">
										<h5 class="fs-14 text-primary mb-0">
											<i class="ri-shopping-cart-fill align-middle me-2" />{' '}
											Your cart
										</h5>
										<span class="badge bg-primary rounded-pill"> 3 </span>
									</div>
									<ul class="list-group mb-3">
										<li class="list-group-item d-flex justify-content-between lh-sm">
											<div>
												<h6 class="my-0">Product name</h6>
												<small class="text-muted"> Brief description </small>
											</div>
											<span class="text-muted">$12</span>
										</li>
										<li class="list-group-item d-flex justify-content-between lh-sm">
											<div>
												<h6 class="my-0">Second product</h6>
												<small class="text-muted"> Brief description </small>
											</div>
											<span class="text-muted">$8</span>
										</li>
										<li class="list-group-item d-flex justify-content-between lh-sm">
											<div>
												<h6 class="my-0">Third item</h6>
												<small class="text-muted"> Brief description </small>
											</div>
											<span class="text-muted">$5</span>
										</li>
										<li class="list-group-item d-flex justify-content-between bg-light">
											<div class="text-success">
												<h6 class="my-0">Discount code</h6>
												<small>−$5 Discount</small>
											</div>
											<span class="text-success">−$5</span>
										</li>
										<li class="list-group-item d-flex justify-content-between">
											<span>Total (USD)</span>
											<strong>$20</strong>
										</li>
									</ul>
								</Col>
							</Row>
						</form>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
