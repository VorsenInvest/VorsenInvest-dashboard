<svelte:head>
  <title>Create Invoice | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import { CardBody, Row, Col, Card, Container, Form, Input, Label, Table } from 'sveltestrap';
	import Select from 'svelte-select';
	import Link from 'svelte-link';
	import logodark from '../../../assets/images/logo-dark.png';
	import logolight from '../../../assets/images/logo-light.png';

	const paymentdetails = [
		{ label: 'Payment Method', value: 'Payment Method' },
		{ label: 'Mastercard', value: 'Mastercard' },
		{ label: 'Credit Card', value: 'Credit Card' },
		{ label: 'Visa', value: 'Visa' },
		{ label: 'Paypal', value: 'Paypal' }
	];

	const allstatus = [
		{ label: 'Select Payment Status', value: 'Select Payment Status' },
		{ label: 'Paid', value: 'Paid' },
		{ label: 'Unpaid', value: 'Unpaid' },
		{ label: 'Refund', value: 'Refund' }
	];

	const allcurrency = [
		{ label: '$', value: '($)' },
		{ label: '£', value: '(£)' },
		{ label: '₹', value: '(₹)' },
		{ label: '€', value: '(€)' }
	];

	let isStatus = 'Select Payment Status';
	let isCurrency = '$';
	let ispaymentDetails = 'Payment Method';
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Create Invoice" pageTitle="Invoices" />
		<Row class="justify-content-center">
			<Col xxl={9}>
				<Card>
					<Form class="needs-validation">
						<CardBody class="border-bottom border-bottom-dashed p-4">
							<Row>
								<Col lg={4}>
									<div class="profile-user mx-auto  mb-3">
										<Input id="profile-img-file-input" type="file" class="profile-img-file-input" />
										<Label for="profile-img-file-input" class="d-block">
											<span class="overflow-hidden border border-dashed d-flex align-items-center justify-content-center rounded" style="height: 60px; width: 256px;">
												<img
													src={logodark}
													class="card-logo card-logo-dark user-profile-image img-fluid"
													alt="logo dark"
												/>
												<img
													src={logolight}
													class="card-logo card-logo-light user-profile-image img-fluid"
													alt="logo light"
												/>
											</span>
										</Label>
									</div>
									<div>
										<div>
											<Label for="companyAddress">Address</Label>
										</div>
										<div class="mb-2">
											<Input
												type="textarea"
												class="form-control bg-light border-0"
												id="companyAddress"
												rows="3"
												placeholder="Company Address"
											/>
											<div class="invalid-feedback">Please enter a address</div>
										</div>
										<div>
											<Input
												type="text"
												class="form-control bg-light border-0"
												id="companyaddpostalcode"
												minLength="5"
												maxLength="6"
												placeholder="Enter Postal Code"
											/>
											<div class="invalid-feedback">
												The US zip code must contain 5 digits, Ex. 45678
											</div>
										</div>
									</div>
								</Col>
								<Col lg={4} class="ms-auto">
									<div class="mb-2">
										<Input
											type="text"
											class="form-control bg-light border-0"
											id="registrationNumber"
											maxLength="12"
											placeholder="Legal Registration No"
										/>
										<div class="invalid-feedback">
											Please enter a registration no, Ex., 012345678912
										</div>
									</div>
									<div class="mb-2">
										<Input
											type="email"
											class="form-control bg-light border-0"
											id="companyEmail"
											placeholder="Email Address"
										/>
										<div class="invalid-feedback">
											Please enter a valid email, Ex., example@gamil.com
										</div>
									</div>
									<div class="mb-2">
										<Input
											type="text"
											class="form-control bg-light border-0"
											id="companyWebsite"
											placeholder="Website"
										/>
										<div class="invalid-feedback">Please enter a website, Ex., www.example.com</div>
									</div>
									<div>
										<Input
											type="text"
											class="form-control bg-light border-0"
											data-plugin="cleave-phone"
											id="compnayContactno"
											placeholder="Contact No"
										/>
										<div class="invalid-feedback">Please enter a contact number</div>
									</div>
								</Col>
							</Row>
						</CardBody>
						<CardBody class="p-4">
							<Row class="g-3">
								<Col lg={3} sm={6}>
									<Label for="invoicenoInput">Invoice No</Label>
									<Input
										type="text"
										class="form-control bg-light border-0"
										id="invoicenoInput"
										placeholder="Invoice No"
										defaultValue="#VL25000355"
									/>
								</Col>
								<Col lg={3} sm={6}>
									<div>
										<Label for="date-field">Date</Label>
										<Input
											type="text"
											class="form-control bg-light border-0"
											id="date-field"
											data-provider="flatpickr"
											data-time="true"
											placeholder="Select Date-time"
										/>
									</div>
								</Col>
								<Col lg={3} sm={6}>
									<Label for="choices-payment-status">Payment Status</Label>
									<div class="input-light select-single">
										<Select
											value={isStatus}
											items={allstatus}
										/>
									</div>
								</Col>
								<Col lg={3} sm={6}>
									<div>
										<Label for="totalamountInput">Total Amount</Label>
										<Input
											type="text"
											class="form-control bg-light border-0"
											id="totalamountInput"
											placeholder="$0.00"
										/>
									</div>
								</Col>
							</Row>
						</CardBody>
						<CardBody class="p-4 border-top border-top-dashed">
							<Row>
								<Col lg={4} sm={6}>
									<div>
										<Label for="billingName" class="text-muted text-uppercase fw-semibold">
											Billing Address
										</Label>
									</div>
									<div class="mb-2">
										<Input
											type="text"
											class="form-control bg-light border-0"
											id="billingName"
											placeholder="Full Name"
										/>
										<div class="invalid-feedback">Please enter a full name</div>
									</div>
									<div class="mb-2">
										<Input
											type="textarea"
											class="form-control bg-light border-0"
											id="billingAddress"
											rows="3"
											placeholder="Address"
											defaultValue=""
										/>
										<div class="invalid-feedback">Please enter a address</div>
									</div>
									<div class="mb-2">
										<Input
											type="text"
											class="form-control bg-light border-0"
											data-plugin="cleave-phone"
											id="billingPhoneno"
											placeholder="(123)456-7890"
										/>
										<div class="invalid-feedback">Please enter a phone number</div>
									</div>
									<div class="mb-3">
										<Input
											type="text"
											class="form-control bg-light border-0"
											id="billingTaxno"
											placeholder="Tax Number"
										/>
										<div class="invalid-feedback">Please enter a tax number</div>
									</div>
									<div class="form-check">
										<input type="checkbox" class="form-check-input" id="same" name="same" />
										<Label class="form-check-label" for="same">
											Will your Billing and Shipping address same?
										</Label>
									</div>
								</Col>
								<Col sm={6} class="ms-auto">
									<Row>
										<Col lg={8}>
											<div>
												<Label for="shippingName" class="text-muted text-uppercase fw-semibold">
													Shipping Address
												</Label>
											</div>
											<div class="mb-2">
												<Input
													type="text"
													class="form-control bg-light border-0"
													id="shippingName"
													placeholder="Full Name"
												/>
												<div class="invalid-feedback">Please enter a full name</div>
											</div>
											<div class="mb-2">
												<Input
													type="textarea"
													class="form-control bg-light border-0"
													id="shippingAddress"
													rows="3"
													placeholder="Address"
													defaultValue=""
												/>
												<div class="invalid-feedback">Please enter a address</div>
											</div>
											<div class="mb-2">
												<Input
													type="text"
													class="form-control bg-light border-0"
													data-plugin="cleave-phone"
													id="shippingPhoneno"
													placeholder="(123)456-7890"
												/>
												<div class="invalid-feedback">Please enter a phone number</div>
											</div>
											<div>
												<Input
													type="text"
													class="form-control bg-light border-0"
													id="shippingTaxno"
													placeholder="Tax Number"
												/>
												<div class="invalid-feedback">Please enter a tax number</div>
											</div>
										</Col>
									</Row>
								</Col>
							</Row>
						</CardBody>
						<CardBody class="p-4">
							<div class="table-responsive">
								<Table class="invoice-table table-borderless table-nowrap mb-0">
									<thead class="align-middle">
										<tr class="table-active">
                                            <th scope="col" style="width: 50px;">#</th>
                                            <th scope="col">
                                                Product Details
                                            </th>
                                            <th scope="col" style="width: 120px;">
                                                <div class="d-flex currency-select input-light align-items-center">
                                                    Rate  
                                                <Select id="choices-payment-currency" value={isCurrency} items={allcurrency}></Select>
                                                </div>
                                            </th>
                                            <th scope="col" style="width: 120px;">Quantity</th>
                                            <th scope="col" class="text-end" style="width: 150px;">Amount</th>
                                            <th scope="col" class="text-end" style="width: 105px;"></th>
                                        </tr>
									</thead>
									<tbody id="newlink">
										<tr id="1" class="product">
											<th scope="row" class="product-id"> 1 </th>
											<td class="text-start">
												<div class="mb-2">
													<Input
														type="text"
														class="form-control bg-light border-0"
														id="productName"
														placeholder="Product Name"
													/>
													<div class="invalid-feedback">Please enter a product name</div>
												</div>
												<Input
													type="textarea"
													class="form-control bg-light border-0"
													id="productDetails"
													rows="2"
													placeholder="Product Details"
													defaultValue=""
												/>
											</td>
											<td>
												<Input
													type="number"
													class="form-control product-price bg-light border-0"
													placeholder="0.00"
												/>
												<div class="invalid-feedback">Please enter a rate</div>
											</td>
											<td>
												<div class="input-step">
													<button type="button" class="minus"> – </button>
													<Input type="number" class="product-quantity" defaultValue="0" readOnly />
													<button type="button" class="plus"> + </button>
												</div>
											</td>
											<td class="text-end">
												<div>
													<Input
														type="text"
														class="form-control bg-light border-0 product-line-price"
														placeholder="$0.00"
														readOnly
													/>
												</div>
											</td>
											<td class="product-removal">
												<Link href={null} class="btn btn-success">Delete</Link>
											</td>
										</tr>

										<tr id="newForm" style="display: none" />
										<tr>
											<td colSpan="9">
												<Link href={null} class="btn btn-soft-secondary fw-medium">
													<i class="ri-add-fill me-1 align-bottom" />
													Add Item
												</Link>
											</td>
										</tr>
										<tr class="border-top border-top-dashed mt-2">
											<td colSpan="3" />
											<td colSpan="2" class="p-0">
												<Table class="table-borderless table-sm table-nowrap align-middle mb-0">
													<tbody>
														<tr>
															<th scope="row">Sub Total</th>
															<td style="width: 150px">
																<Input
																	type="text"
																	class="form-control bg-light border-0"
																	id="cart-subtotal"
																	placeholder="$0.00"
																	readOnly
																/>
															</td>
														</tr>
														<tr>
															<th scope="row">Estimated Tax (12.5%)</th>
															<td>
																<Input
																	type="text"
																	class="form-control bg-light border-0"
																	id="cart-tax"
																	placeholder="$0.00"
																	readOnly
																/>
															</td>
														</tr>
														<tr>
															<th scope="row">
																Discount
																<small class="text-muted"> (VELZON15) </small>
															</th>
															<td>
																<Input
																	type="text"
																	class="form-control bg-light border-0"
																	id="cart-discount"
																	placeholder="$0.00"
																	readOnly
																/>
															</td>
														</tr>
														<tr>
															<th scope="row">Shipping Charge</th>
															<td>
																<Input
																	type="text"
																	class="form-control bg-light border-0"
																	id="cart-shipping"
																	placeholder="$0.00"
																	readOnly
																/>
															</td>
														</tr>
														<tr class="border-top border-top-dashed">
															<th scope="row">Total Amount</th>
															<td>
																<Input
																	type="text"
																	class="form-control bg-light border-0"
																	id="cart-total"
																	placeholder="$0.00"
																	readOnly
																/>
															</td>
														</tr>
													</tbody>
												</Table>
											</td>
										</tr>
									</tbody>
								</Table>
							</div>
							<Row class="mt-3">
								<Col lg={4}>
									<div class="mb-2">
										<Label
											for="choices-payment-type"
											class="form-label text-muted text-uppercase fw-semibold"
										>
											Payment Details
										</Label>
										<div class="select-single">
											<Select
												value={ispaymentDetails}
												items={paymentdetails}
												id="idStatus"
											/>
										</div>
									</div>
									<div class="mb-2">
										<Input
											class="form-control bg-light border-0"
											type="text"
											id="cardholderName"
											placeholder="Card Holder Name"
										/>
									</div>
									<div class="mb-2">
										<Input
											class="form-control bg-light border-0"
											type="text"
											id="cardNumber"
											placeholder="xxxx xxxx xxxx xxxx"
										/>
									</div>
									<div>
										<Input
											class="form-control  bg-light border-0"
											type="text"
											id="amountTotalPay"
											placeholder="$0.00"
											readOnly
										/>
									</div>
								</Col>
							</Row>
							<div class="mt-4">
								<Label
									for="exampleFormControlTextarea1"
									class="form-label text-muted text-uppercase fw-semibold"
								>
									NOTES
								</Label>
								<Input
									type="textarea"
									class="form-control alert alert-info"
									id="exampleFormControlTextarea1"
									placeholder="Notes"
									rows="2"
									value="All accounts are to be paid within 7 days from receipt of invoice. To be paid by cheque or credit card or direct payment online. If account is not paid within 7 days the credits details supplied as confirmation of work undertaken will be charged the agreed quoted fee noted above."
								/>
							</div>
							<div class="hstack gap-2 justify-content-end d-print-none mt-4">
								<button type="submit" class="btn btn-success">
									<i class="ri-printer-line align-bottom me-1" /> Save
								</button>
								<Link href={null} class="btn btn-primary">
									<i class="ri-download-2-line align-bottom me-1" />
									Download Invoice
								</Link>
								<Link href={null} class="btn btn-secondary">
									<i class="ri-send-plane-fill align-bottom me-1" />
									Send Invoice
								</Link>
							</div>
						</CardBody>
					</Form>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
