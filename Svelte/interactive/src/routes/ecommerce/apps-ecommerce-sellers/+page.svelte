<svelte:head>
  <title>Sellers | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import {
		CardBody,
		CardHeader,
		Container,
		Card,
		Row,
		Col,
		TabContent,
		TabPane,
		Input,
		Label
	} from 'sveltestrap';
	import Select from 'svelte-select';
	import Link from 'svelte-link';
	import SellerChats from '../SellerChats.svelte';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
    import Modal from "../../../Components/Common/Modal.svelte";

	let showSellermodal = false;
    const SellerModalToggle = () => (showSellermodal = !showSellermodal);

	const optionvisibility = [
		{ value: 'Select Categories', label: 'Select Categories' },
		{ value: 'All', label: 'All' },
		{ value: 'Retailer', label: 'Retailer' },
		{ value: 'Health & Medicine', label: 'Health & Medicine' },
		{ value: 'Manufacturer', label: 'Manufacturer' },
		{ value: 'Food Service', label: 'Food Service' },
		{ value: 'Computers & Electronics', label: 'Computers & Electronics' }
	];

	import ecommerceData from '../../../common/data/ecommerce';
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Sellers" pageTitle="Ecommerce" />
		<Card>
			<CardHeader class="border-0 rounded">
				<Row class="g-2">
					<Col xxl={3}>
						<div class="search-box">
							<input
								type="text"
								class="form-control search"
								placeholder="Search for sellers & owner name or something..."
							/> <i class="ri-search-line search-icon" />
						</div>
					</Col>
					<Col xxl={3} class="ms-auto">
						<div class="select-single">
							<Select class="form-control" items={optionvisibility} placeholder="Select Categories" />
						</div>
					</Col>
					<div class="col-lg-auto">
						<div class="hstack gap-2">
							<button type="button" class="btn btn-danger"
								><i class="ri-equalizer-fill me-1 align-bottom" /> Filters</button>
							<button class="btn btn-primary" on:click={SellerModalToggle}><i class="ri-add-fill me-1 align-bottom" /> Add Seller</button>
						</div>
					</div>
				</Row><!--end row-->
			</CardHeader>
		</Card>

		<Row class="mt-4">
			{#each ecommerceData.sellersList as seller}
				<Col xl={3} lg={6}>
					<Card class="ribbon-box right overflow-hidden">
						<CardBody class="text-center p-4">
							{#if seller.isTrending}
								<div class="ribbon ribbon-info ribbon-shape trending-ribbon">
									<i class="ri-flashlight-fill text-white align-bottom" />
									<span class="trending-ribbon-text">Trending</span>
								</div>
							{/if}

							<img src={seller.img} alt="" height="45" />
							<h5 class="mb-1 mt-4">
								<Link href="/ecommerce/apps-ecommerce-seller-details" class="link-primary"
									>{seller.label}</Link
								>
							</h5>
							<p class="text-muted mb-4">{seller.name}</p>
							<Row class="justify-content-center">
								<div class="col-lg-8">
									<SellerChats color={seller.color} id={seller.id} data={seller.chartdata} />
								</div>
							</Row>
							<Row class="mt-4">
								<div class="col-lg-6 border-end-dashed border-end">
									<h5>{seller.stock}</h5>
									<span class="text-muted">Item Stock</span>
								</div>
								<div class="col-lg-6">
									<h5>{seller.balance}</h5>
									<span class="text-muted">Wallet Balance</span>
								</div>
							</Row>
							<div class="mt-4">
								<Link href="/ecommerce/apps-ecommerce-seller-details" class="btn btn-light w-100"
									>View Details</Link
								>
							</div>
						</CardBody>
					</Card>
				</Col>
			{/each}
		</Row>

		<Row class="g-0 text-center text-sm-start align-items-center mb-3">
			<div class="col-sm-6">
				<div>
					<p class="mb-sm-0">Showing 1 to 8 of 12 entries</p>
				</div>
			</div>
			<!-- end col -->
			<div class="col-sm-6">
				<ul
					class="pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0"
				>
					<li class="page-item disabled">
						<Link href="{null}" class="page-link"><i class="mdi mdi-chevron-left" /></Link>
					</li>
					<li class="page-item active"><Link href="{null}" class="page-link">1</Link></li>
					<li class="page-item "><Link href="{null}" class="page-link">2</Link></li>
					<li class="page-item"><Link href="{null}" class="page-link">3</Link></li>
					<li class="page-item"><Link href="{null}" class="page-link">4</Link></li>
					<li class="page-item"><Link href="{null}" class="page-link">5</Link></li>
					<li class="page-item">
						<Link href="{null}" class="page-link"><i class="mdi mdi-chevron-right" /></Link>
					</li>
				</ul>
			</div>
			<!-- end col -->
		</Row><!-- end row -->
	</Container>
</div>

<Modal isOpen={showSellermodal} className="modal-dialog-centered modal-lg">
    <div class="modal-header p-3 bg-light">
        <h5 class="modal-title" >Add Seller</h5>
        <button type="button" class="btn-close" on:click={SellerModalToggle} ></button>
    </div>
    <div class="modal-body">
        <TabContent pills class="nav-tabs-custom nav-success p-2 pb-0 ">
			<TabPane tabId="personaldetail" tab="Person Details" class="mt-4" active>
				<Row>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="firstnameInput" class="form-label">First Name</Label>
							<Input type="text" class="form-control" id="firstnameInput" placeholder="Enter your firstname" />
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="lastnameInput" class="form-label">Last Name</Label>
							<Input type="text" class="form-control" id="lastnameInput" placeholder="Enter your lastname" />
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="contactnumberInput" class="form-label">Contact Number</Label>
							<Input type="number" class="form-control" id="contactnumberInput" placeholder="Enter your number"/>
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="phonenumberInput" class="form-label">Phone Number</Label>
							<Input type="number" class="form-control" id="phonenumberInput" placeholder="Enter your number" />
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="emailidInput" class="form-label">Email</Label>
							<Input type="email" class="form-control" id="emailidInput" placeholder="Enter your email" />
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="birthdayidInput" class="form-label">Date of Birth</Label>
							<Input type="text" id="birthdayidInput" class="form-control flatpickr-input" data-provider="flatpickr" placeholder="Enter your date of birth" readonly="readonly" />
						</div>
					</Col>
					<Col lg={4}>
						<div class="mb-3">
							<Label for="cityidInput" class="form-label">City</Label>
							<Input type="text" class="form-control" id="cityidInput" placeholder="Enter your city"/>
						</div>
					</Col>
					<Col lg={4}>
						<div class="mb-3">
							<Label for="countryidInput" class="form-label">Country</Label>
							<Input type="text" class="form-control" id="countryidInput" placeholder="Enter your country"/>
						</div>
					</Col>
					<Col lg={4}>
						<div class="mb-3">
							<Label for="zipcodeidInput" class="form-label">Zip Code</Label>
							<Input type="text" class="form-control" id="zipcodeidInput" placeholder="Enter your zipcode"/>
						</div>
					</Col>
					<Col lg={12}>
						<div class="mb-3">
							<Label for="exampleFormControlTextarea1" class="form-label">Description</Label>
							<Input type="textarea" class="form-control" id="exampleFormControlTextarea1" rows="3" placeholder="Enter description"/>
						</div>
					</Col>
					<Col lg={12}>
						<div class="hstack gap-2 justify-content-end">
							<button class="btn btn-link link-success text-decoration-none fw-medium" on:click={SellerModalToggle}><i class="ri-close-line me-1 align-middle"></i> Close</button>
							<button type="submit" class="btn btn-primary"><i class="ri-save-3-line align-bottom me-1"></i> Save</button>
						</div>
					</Col>
				</Row>
			</TabPane>
			<TabPane tabId="businessdetail"  class="mt-4" tab="Business Details">
				<Row>
					<Col lg={12}>
						<div class="mb-3">
							<Label for="companynameInput" class="form-label">Company Name</Label>
							<Input type="text" class="form-control" id="companynameInput" placeholder="Enter your company name" />
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="choices-single-default" class="form-label">Company Type</Label>
							<select class="form-control" data-trigger name="choices-single-default" id="choices-single-default">
								<option value="">Select type</option>
								<option value="All" selected>All</option>
								<option value="Merchandising">Merchandising</option>
								<option value="Manufacturing">Manufacturing</option>
								<option value="Partnership">Partnership</option>
								<option value="Corporation">Corporation</option>
							</select>
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="pancardInput" class="form-label">Pan Card Number</Label>
							<Input type="text" class="form-control" id="pancardInput" placeholder="Enter your pan-card number" />
						</div>
					</Col>
					<Col lg={4}>
						<div class="mb-3">
							<Label for="websiteInput" class="form-label">Website</Label>
							<Input type="url" class="form-control" id="websiteInput" placeholder="Enter your URL" />
						</div>
					</Col>
					<Col lg={4}>
						<div class="mb-3">
							<Label for="faxInput" class="form-label">Fax</Label>
							<Input type="text" class="form-control" id="faxInput" placeholder="Enter your fax" />
						</div>
					</Col>
					<Col lg={4}>
						<div class="mb-3">
							<Label for="companyemailInput" class="form-label">Email</Label>
							<Input type="email" class="form-control" id="companyemailInput" placeholder="Enter your email" />
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="worknumberInput" class="form-label">Number</Label>
							<Input type="number" class="form-control" id="worknumberInput" placeholder="Enter your number" />
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="companylogoInput" class="form-label">Company Logo</Label>
							<Input type="file" class="form-control" id="companylogoInput" />
						</div>
					</Col>
					<Col lg={12}>
						<div class="hstack gap-2 justify-content-end">
							<button class="btn btn-link link-success text-decoration-none fw-medium" on:click={SellerModalToggle}><i class="ri-close-line me-1 align-middle"></i> Close</button>
							<button type="submit" class="btn btn-primary"><i class="ri-save-3-line align-bottom me-1"></i> Save</button>
						</div>
					</Col>
				</Row>
			</TabPane>
			<TabPane tabId="bankdetail" class="mt-4"  tab="Bank Details">
				<Row>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="banknameInput" class="form-label">Bank Name</Label>
							<Input type="text" class="form-control" id="banknameInput" placeholder="Enter your bank name" />
						</div>
					</Col>
					<!--end col-->
					<Col lg={6}>
						<div class="mb-3">
							<Label for="branchInput" class="form-label">Branch</Label>
							<Input type="text" class="form-control" id="branchInput" placeholder="Branch" />
						</div>
					</Col>
					<!--end col-->
					<Col lg={12}>
						<div class="mb-3">
							<Label for="accountnameInput" class="form-label">Account Holder Name</Label>
							<Input type="text" class="form-control" id="accountnameInput" placeholder="Enter account holder name" />
						</div>
					</Col>
					<!--end col-->
					<Col lg={6}>
						<div class="mb-3">
							<Label for="accountnumberInput" class="form-label">Account Number</Label>
							<Input type="number" class="form-control" id="accountnumberInput" placeholder="Enter account number" />
						</div>
					</Col>
					<!--end col-->
					<Col lg={6}>
						<div class="mb-3">
							<Label for="ifscInput" class="form-label">IFSC</Label>
							<Input type="number" class="form-control" id="ifscInput" placeholder="IFSC" />
						</div>
					</Col>
					<!--end col-->
					<Col lg={12}>
						<div class="hstack gap-2 justify-content-end">
							<button class="btn btn-link link-success text-decoration-none fw-medium" on:click={SellerModalToggle}><i class="ri-close-line me-1 align-middle"></i> Close</button>
							<button type="submit" class="btn btn-primary"><i class="ri-save-3-line align-bottom me-1"></i> Save</button>
						</div>
					</Col>
					<!--end col-->
				</Row>
			</TabPane>
		  </TabContent>
    </div>
</Modal>