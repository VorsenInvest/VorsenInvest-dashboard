<svelte:head>
  <title>Order Details | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import { Container, Row, Col, Card, CardBody, CardHeader, Collapse } from 'sveltestrap';
	import Link from 'svelte-link';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import img8 from '../../../assets/images/products/img-8.png'
	import img7 from '../../../assets/images/products/img-7.png'
	import img3 from '../../../assets/images/products/img-3.png'
	import avatar3 from '../../../assets/images/users/avatar-3.jpg'
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Order Details" pageTitle="Ecommerce" />

		<Row>
			<Col xl={9}>
				<Card>
					<CardHeader>
						<div class="d-flex align-items-center">
							<h5 class="card-title flex-grow-1 mb-0">Order #VL2667</h5>
							<div class="flex-shrink-0">
								<Link href="/invoices/apps-invoices-details" class="btn btn-primary btn-sm">
									<i class="ri-download-2-fill align-middle me-1" /> Invoice</Link
								>
							</div>
						</div>
					</CardHeader>
					<CardBody>
						<div class="table-responsive table-card">
							<table class="table table-nowrap align-middle table-borderless mb-0">
								<thead class="table-light text-muted">
									<tr>
										<th scope="col">Product Details</th>
										<th scope="col">Item Price</th>
										<th scope="col">Quantity</th>
										<th scope="col">Rating</th>
										<th scope="col" class="text-end">Total Amount</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>
											<div class="d-flex">
												<div class="flex-shrink-0 avatar-md bg-light rounded p-1">
													<img
														src={img8}
														alt=""
														class="img-fluid d-block"
													/>
												</div>
												<div class="flex-grow-1 ms-3">
													<h5 class="fs-15">
														<Link href="/ecommerce/apps-ecommerce-product-details" class="link-primary"
															>Sweatshirt for Men (Pink)</Link
														>
													</h5>
													<p class="text-muted mb-0">Color: <span class="fw-medium">Pink</span></p>
													<p class="text-muted mb-0">Size: <span class="fw-medium">M</span></p>
												</div>
											</div>
										</td>
										<td>$119.99</td>
										<td>02</td>
										<td>
											<div class="text-warning fs-15">
												<i class="ri-star-fill" /><i class="ri-star-fill" /><i
													class="ri-star-fill"
												/><i class="ri-star-fill" /><i class="ri-star-half-fill" />
											</div>
										</td>
										<td class="fw-medium text-end"> $239.98 </td>
									</tr>
									<tr>
										<td>
											<div class="d-flex">
												<div class="flex-shrink-0 avatar-md bg-light rounded p-1">
													<img
														src={img7}
														alt=""
														class="img-fluid d-block"
													/>
												</div>
												<div class="flex-grow-1 ms-3">
													<h5 class="fs-15">
														<Link href="/ecommerce/apps-ecommerce-product-details" class="link-primary"
															>Noise NoiseFit Endure Smart Watch</Link
														>
													</h5>
													<p class="text-muted mb-0">Color: <span class="fw-medium">Black</span></p>
													<p class="text-muted mb-0">Size: <span class="fw-medium">32.5mm</span></p>
												</div>
											</div>
										</td>
										<td>$94.99</td>
										<td>01</td>
										<td>
											<div class="text-warning fs-15">
												<i class="ri-star-fill" /><i class="ri-star-fill" /><i
													class="ri-star-fill"
												/><i class="ri-star-fill" /><i class="ri-star-half-fill" />
											</div>
										</td>
										<td class="fw-medium text-end"> $94.99 </td>
									</tr>
									<tr>
										<td>
											<div class="d-flex">
												<div class="flex-shrink-0 avatar-md bg-light rounded p-1">
													<img
														src={img3}
														alt=""
														class="img-fluid d-block"
													/>
												</div>
												<div class="flex-grow-1 ms-3">
													<h5 class="fs-15">
														<Link href="/ecommerce/apps-ecommerce-product-details" class="link-primary"
															>350 ml Glass Grocery Container</Link
														>
													</h5>
													<p class="text-muted mb-0">Color: <span class="fw-medium">White</span></p>
													<p class="text-muted mb-0">Size: <span class="fw-medium">350 ml</span></p>
												</div>
											</div>
										</td>
										<td>$24.99</td>
										<td>01</td>
										<td>
											<div class="text-warning fs-15">
												<i class="ri-star-fill" /><i class="ri-star-fill" /><i
													class="ri-star-half-fill"
												/><i class="ri-star-line" /><i class="ri-star-line" />
											</div>
										</td>
										<td class="fw-medium text-end"> $24.99 </td>
									</tr>
									<tr class="border-top border-top-dashed">
										<td colspan="3" />
										<td colspan="2" class="fw-medium p-0">
											<table class="table table-borderless mb-0">
												<tbody>
													<tr>
														<td>Sub Total :</td>
														<td class="text-end">$359.96</td>
													</tr>
													<tr>
														<td>Discount <span class="text-muted">(VELZON15)</span> : : </td>
														<td class="text-end">-$53.99</td>
													</tr>
													<tr>
														<td>Shipping Charge :</td>
														<td class="text-end">$65.00</td>
													</tr>
													<tr>
														<td>Estimated Tax :</td>
														<td class="text-end">$44.99</td>
													</tr>
													<tr class="border-top border-top-dashed">
														<th scope="row">Total (USD) :</th>
														<th class="text-end">$415.96</th>
													</tr>
												</tbody>
											</table>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
					</CardBody>
				</Card>
				<!--end card-->
				<Card>
					<CardHeader>
						<div class="d-sm-flex align-items-center">
							<h5 class="card-title flex-grow-1 mb-0">Order Status</h5>
							<div class="flex-shrink-0 mt-2 mt-sm-0">
								<Link href="#" class="btn btn-soft-primary btn-sm mt-2 mt-sm-0"
									><i class="ri-map-pin-line align-middle me-1" /> Change Address</Link
								>
								<Link href="#" class="btn btn-soft-secondary btn-sm mt-2 mt-sm-0"
									><i class="mdi mdi-archive-remove-outline align-middle me-1" /> Cancel Order</Link
								>
							</div>
						</div>
					</CardHeader>
					<CardBody>
						<div class="profile-timeline">
							<div class="accordion accordion-flush" id="accordionFlushExample">
								<div class="accordion-item border-0">
									<div class="accordion-header" id="headingOne">
										<Link class="accordion-button p-2 shadow-none" id="collapseOne">
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0 avatar-xs">
													<div class="avatar-title bg-primary rounded-circle">
														<i class="ri-shopping-bag-line" />
													</div>
												</div>
												<div class="flex-grow-1 ms-3">
													<h6 class="fs-15 mb-0 fw-semibold">
														Order Placed - <span class="fw-normal">Wed, 15 Dec 2021</span>
													</h6>
												</div>
											</div>
										</Link>
									</div>
									<Collapse toggler="collapseOne" class="accordion-collapse" isOpen>
										<div class="accordion-body ms-2 ps-5 pt-0">
											<h6 class="mb-1">An order has been placed.</h6>
											<p class="text-muted">Wed, 15 Dec 2021 - 05:34PM</p>

											<h6 class="mb-1">Seller has proccessed your order.</h6>
											<p class="text-muted mb-0">Thu, 16 Dec 2021 - 5:48AM</p>
										</div>
									</Collapse>
								</div>
								<div class="accordion-item border-0">
									<div class="accordion-header" id="headingTwo">
										<Link class="accordion-button p-2 shadow-none" id="collapseTwo">
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0 avatar-xs">
													<div class="avatar-title bg-primary rounded-circle">
														<i class="mdi mdi-gift-outline" />
													</div>
												</div>
												<div class="flex-grow-1 ms-3">
													<h6 class="fs-15 mb-1 fw-semibold">
														Packed - <span class="fw-normal">Thu, 16 Dec 2021</span>
													</h6>
												</div>
											</div>
										</Link>
									</div>
									<Collapse toggler="collapseTwo" class="accordion-collapse" isOpen>
										<div class="accordion-body ms-2 ps-5 pt-0">
											<h6 class="mb-1">Your Item has been picked up by courier patner</h6>
											<p class="text-muted mb-0">Fri, 17 Dec 2021 - 9:45AM</p>
										</div>
									</Collapse>
								</div>
								<div class="accordion-item border-0">
									<div class="accordion-header" id="headingThree">
										<Link class="accordion-button p-2 shadow-none" id="collapseThree">
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0 avatar-xs">
													<div class="avatar-title bg-primary rounded-circle">
														<i class="ri-truck-line" />
													</div>
												</div>
												<div class="flex-grow-1 ms-3">
													<h6 class="fs-15 mb-1 fw-semibold">
														Shipping - <span class="fw-normal">Thu, 16 Dec 2021</span>
													</h6>
												</div>
											</div>
										</Link>
									</div>
									<Collapse toggler="collapseThree" class="accordion-collapse" isOpen>
										<div class="accordion-body ms-2 ps-5 pt-0">
											<h6 class="fs-14">RQK Logistics - MFDS1400457854</h6>
											<h6 class="mb-1">Your item has been shipped.</h6>
											<p class="text-muted mb-0">Sat, 18 Dec 2021 - 4.54PM</p>
										</div>
									</Collapse>
								</div>
								<div class="accordion-item border-0">
									<div class="accordion-header" id="headingFour">
										<Link
											class="accordion-button p-2 shadow-none"
											data-bs-toggle="collapse"
											href="#collapseFour"
											aria-expanded="false"
										>
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0 avatar-xs">
													<div class="avatar-title bg-light text-primary rounded-circle">
														<i class="ri-takeaway-fill" />
													</div>
												</div>
												<div class="flex-grow-1 ms-3">
													<h6 class="fs-14 mb-0 fw-semibold">Out For Delivery</h6>
												</div>
											</div>
										</Link>
									</div>
								</div>
								<div class="accordion-item border-0">
									<div class="accordion-header" id="headingFive">
										<Link
											class="accordion-button p-2 shadow-none"
											data-bs-toggle="collapse"
											href="#collapseFile"
											aria-expanded="false"
										>
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0 avatar-xs">
													<div class="avatar-title bg-light text-primary rounded-circle">
														<i class="mdi mdi-package-variant" />
													</div>
												</div>
												<div class="flex-grow-1 ms-3">
													<h6 class="fs-14 mb-0 fw-semibold">Delivered</h6>
												</div>
											</div>
										</Link>
									</div>
								</div>
							</div>
							<!--end accordion-->
						</div>
					</CardBody>
				</Card>
				<!--end card-->
			</Col>
			<!--end col-->
			<div class="col-xl-3">
				<Card>
					<CardHeader>
						<div class="d-flex">
							<h5 class="card-title flex-grow-1 mb-0">
								<i class="mdi mdi-truck-fast-outline align-middle me-1 text-muted" />
								Logistics Details
							</h5>
							<div class="flex-shrink-0">
								<Link href="{null}" class="badge bg-primary-subtle text-primary fs-11">Track Order</Link>
							</div>
						</div>
					</CardHeader>
					<CardBody>
						<div class="text-center">
							<lord-icon
								src="//cdn.lordicon.com/uetqnvvg.json"
								trigger="loop"
								colors="primary:#8c68cd,secondary:#4788ff"
								style="width:80px;height:86px"
							/>

							<h5 class="fs-16 mt-2">RQK Logistics</h5>
							<p class="text-muted mb-0">ID: MFDS1400457854</p>
							<p class="text-muted mb-0">Payment Mode : Debit Card</p>
						</div>
					</CardBody>
				</Card>
				<!--end card-->

				<Card>
					<CardHeader>
						<div class="d-flex">
							<h5 class="card-title flex-grow-1 mb-0">Customer Details</h5>
							<div class="flex-shrink-0">
								<Link href="{null}" class="link-secondary">View Profile</Link>
							</div>
						</div>
					</CardHeader>
					<CardBody>
						<ul class="list-unstyled mb-0 vstack gap-3">
							<li>
								<div class="d-flex align-items-center">
									<div class="flex-shrink-0">
										<img
											src={avatar3}
											alt=""
											class="avatar-sm rounded"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="fs-14 mb-1">Joseph Parkers</h6>
										<p class="text-muted mb-0">Customer</p>
									</div>
								</div>
							</li>
							<li>
								<i class="ri-mail-line me-2 align-middle text-muted fs-16" />josephparker@gmail.com
							</li>
							<li>
								<i class="ri-phone-line me-2 align-middle text-muted fs-16" />+(256) 245451 441
							</li>
						</ul>
					</CardBody>
				</Card>
				<!--end card-->
				<Card>
					<CardHeader>
						<h5 class="card-title mb-0">
							<i class="ri-map-pin-line align-middle me-1 text-muted" /> Billing Address
						</h5>
					</CardHeader>
					<CardBody>
						<ul class="list-unstyled vstack gap-2 fs-13 mb-0">
							<li class="fw-medium fs-14">Joseph Parker</li>
							<li>+(256) 245451 451</li>
							<li>2186 Joyce Street Rocky Mount</li>
							<li>New York - 25645</li>
							<li>United States</li>
						</ul>
					</CardBody>
				</Card>
				<!--end card-->
				<Card>
					<CardHeader>
						<h5 class="card-title mb-0">
							<i class="ri-map-pin-line align-middle me-1 text-muted" /> Shipping Address
						</h5>
					</CardHeader>
					<CardBody>
						<ul class="list-unstyled vstack gap-2 fs-13 mb-0">
							<li class="fw-medium fs-14">Joseph Parker</li>
							<li>+(256) 245451 451</li>
							<li>2186 Joyce Street Rocky Mount</li>
							<li>California - 24567</li>
							<li>United States</li>
						</ul>
					</CardBody>
				</Card>
				<!--end card-->

				<Card>
					<CardHeader>
						<h5 class="card-title mb-0">
							<i class="ri-secure-payment-line align-bottom me-1 text-muted" /> Payment Details
						</h5>
					</CardHeader>
					<CardBody>
						<div class="d-flex align-items-center mb-2">
							<div class="flex-shrink-0">
								<p class="text-muted mb-0">Transactions:</p>
							</div>
							<div class="flex-grow-1 ms-2">
								<h6 class="mb-0">#VLZ124561278124</h6>
							</div>
						</div>
						<div class="d-flex align-items-center mb-2">
							<div class="flex-shrink-0">
								<p class="text-muted mb-0">Payment Method:</p>
							</div>
							<div class="flex-grow-1 ms-2">
								<h6 class="mb-0">Debit Card</h6>
							</div>
						</div>
						<div class="d-flex align-items-center mb-2">
							<div class="flex-shrink-0">
								<p class="text-muted mb-0">Card Holder Name:</p>
							</div>
							<div class="flex-grow-1 ms-2">
								<h6 class="mb-0">Joseph Parker</h6>
							</div>
						</div>
						<div class="d-flex align-items-center mb-2">
							<div class="flex-shrink-0">
								<p class="text-muted mb-0">Card Number:</p>
							</div>
							<div class="flex-grow-1 ms-2">
								<h6 class="mb-0">xxxx xxxx xxxx 2456</h6>
							</div>
						</div>
						<div class="d-flex align-items-center">
							<div class="flex-shrink-0">
								<p class="text-muted mb-0">Total Amount:</p>
							</div>
							<div class="flex-grow-1 ms-2">
								<h6 class="mb-0">$415.96</h6>
							</div>
						</div>
					</CardBody>
				</Card>
				<!--end card-->
			</div>
			<!--end col-->
		</Row>
	</Container>
</div>