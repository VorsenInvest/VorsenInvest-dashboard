<script>
	import {
		Card,
		CardBody,
		Col,
		Nav,
		NavItem,
		NavLink,
		Row,
		TabContent,
		TabPane,
		Label,
		Input,
	} from "sveltestrap";
	import Dropzone from "svelte-file-dropzone";
	import Flatpickr from "svelte-flatpickr";
	import Select from "svelte-select";
	import Link from "svelte-link";
	import verificationimg from '../../../assets/images/verification-img.png'
	import Modal from "../../../Components/Common/Modal.svelte";

	let isKycVerification = false;

	const toggleKycVerification = () => {
		isKycVerification = !isKycVerification;
	};

	let files = {
		accepted: [],
		rejected: [],
	};

	function handleFilesSelect(e) {
		const { acceptedFiles, fileRejections } = e.detail;
		files.accepted = [...files.accepted, ...acceptedFiles];
		files.rejected = [...files.rejected, ...fileRejections];
	}

	let activeTab = 1;
	let selectCountry = "";
	const country = [
		{ label: "Select country", value: "Select country" },
		{ label: "Argentina", value: "Argentina" },
		{ label: "Belgium", value: "Belgium" },
		{ label: "Brazil", value: "Brazil" },
		{ label: "Colombia", value: "Colombia" },
		{ label: "Denmark", value: "Denmark" },
		{ label: "France", value: "France" },
		{ label: "Germany", value: "Germany" },
		{ label: "Mexico", value: "Mexico" },
		{ label: "Russia", value: "Russia" },
		{ label: "Spain", value: "Spain" },
		{ label: "Syria", value: "Syria" },
		{ label: "United Kingdom", value: "United Kingdom" },
		{
			label: "United States of America",
			value: "United States of America",
		},
	];

	const toggleTab = (active) => (activeTab = active);
</script>

<Row class="justify-content-center">
	<Col lg={6}>
		<Card>
			<CardBody>
				<div class="text-center">
					<Row class="justify-content-center">
						<Col lg={9}>
							<h4 class="mt-4 fw-semibold">KYC Verification</h4>
							<p class="text-muted mt-3">
								When you get your KYC verification process done,
								you have given the crypto exchange in this case,
								information.{" "}
							</p>
							<div class="mt-4">
								<button
									type="button"
									on:click={toggleKycVerification}
									class="btn btn-primary"
									data-bs-toggle="modal"
									data-bs-target="#exampleModal"
								>
									Click here for Verification
								</button>
							</div>
						</Col>
					</Row>

					<Row class="justify-content-center mt-5 mb-2">
						<Col sm={7} xs={8}>
							<img
								src={verificationimg}
								alt=""
								class="img-fluid"
							/>
						</Col>
					</Row>
				</div>
			</CardBody>
		</Card>
	</Col>
</Row>


<Modal isOpen={isKycVerification} className="modal-dialog-centered modal-lg">
	<div class="modal-header p-3 text-uppercase">
		<h5 class="modal-title" >Verify your Account</h5>
		<button type="button" class="btn-close" on:click={toggleKycVerification}
								/>
	</div>
	<div class="modal-body">
		<div class="step-arrow-nav">
			<Nav class="nav-pills nav-justified custom-nav" role="tablist">
				<NavItem>
					<NavLink
						class="p-3"
						on:click={() => (activeTab = 1)}
						active={activeTab == 1}>Personal Info</NavLink
					>
				</NavItem>
				<NavItem>
					<NavLink
						class="p-3"
						on:click={() => (activeTab = 2)}
						active={activeTab == 2}>Bank Details</NavLink
					>
				</NavItem>
				<NavItem>
					<NavLink
						class="p-3"
						on:click={() => (activeTab = 3)}
						active={activeTab == 3}>Document Verification</NavLink
					>
				</NavItem>
				<NavItem>
					<NavLink
						class="p-3"
						on:click={() => (activeTab = 4)}
						active={activeTab == 4}>Verified</NavLink
					>
				</NavItem>
			</Nav>
		</div>
	</div>
	<div class="modal-body">
		<TabContent>
			<TabPane tabId={1} class={activeTab == 1 ? "active" : ""}>
				<Row class="g-3">
					<Col lg={6}>
						<div>
							<Label for="firstName" class="form-label"
								>First Name</Label
							>
							<Input
								type="text"
								class="form-control"
								id="firstName"
								placeholder="Enter your firstname"
							/>
						</div>
					</Col>
					<Col lg={6}>
						<div>
							<Label for="lastName" class="form-label"
								>Last Name</Label
							>
							<Input
								type="text"
								class="form-control"
								id="lastName"
								placeholder="Enter your lastname"
							/>
						</div>
					</Col>
					<Col lg={6}>
						<div>
							<Label for="phoneNumber" class="form-label"
								>Phone</Label
							>
							<Input
								type="text"
								class="form-control"
								id="phoneNumber"
								placeholder="Enter your phone number"
							/>
						</div>
					</Col>
					<Col lg={6}>
						<div>
							<Label for="dateofBirth" class="form-label"
								>Date of Birth</Label
							>
							<Flatpickr
								class="form-control"
								options={{
									dateFormat: "d M, Y",
								}}
								placeholder="Enter your date of birth"
							/>
						</div>
					</Col>
					<Col lg={4}>
						<div>
							<Label for="emailID" class="form-label"
								>Email ID</Label
							>
							<Input
								type="email"
								class="form-control"
								id="emailID"
								placeholder="Enter your email"
							/>
						</div>
					</Col>
					<Col lg={4}>
						<div>
							<Label for="password" class="form-label"
								>Password</Label
							>
							<Input
								type="password"
								class="form-control"
								id="password"
								placeholder="Enter your password"
							/>
						</div>
					</Col>
					<Col lg={4}>
						<div>
							<Label for="confirmPassword" class="form-label"
								>Confirm Password</Label
							>
							<Input
								type="password"
								class="form-control"
								id="confirmPassword"
								placeholder="Enter your confirm password"
							/>
						</div>
					</Col>
					<Col lg={6}>
						<div>
							<Label for="vatNo" class="form-label"
								>VAT/TIN No.</Label
							>
							<Input
								type="text"
								class="form-control"
								id="vatNo"
								placeholder="Enter your VAT/TIN no"
							/>
						</div>
					</Col>
					<Col lg={6}>
						<div>
							<Label for="serviceTax" class="form-label"
								>Service Tax No.</Label
							>
							<Input
								type="text"
								class="form-control"
								id="serviceTax"
								placeholder="Enter your service tax no"
							/>
						</div>
					</Col>
					<Col lg={12}>
						<div>
							<Label for="country-select" class="form-label"
								>Country</Label
							>
							<Select
								class="mb-0"
								value={selectCountry}
								items={country}
								id="country-select"
							/>
						</div>
					</Col>
					<Col lg={12}>
						<div class="d-flex align-items-start gap-3 mt-3">
							<button
								on:click={toggleTab(activeTab + 1)}
								type="button"
								class="btn btn-primary btn-label right ms-auto nexttab"
							>
								<i
									class="ri-arrow-right-line label-icon align-middle fs-16 ms-2"
								/>{" "}
								Next Step
							</button>
						</div>
					</Col>
				</Row>
			</TabPane>

			<TabPane tabId={2} class={activeTab == 2 ? "active" : ""}>
				<Row>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="banknameInput" class="form-label"
								>Bank Name</Label
							>
							<Input
								type="text"
								class="form-control"
								id="banknameInput"
								placeholder="Enter your bank name"
							/>
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="branchInput" class="form-label"
								>Branch</Label
							>
							<Input
								type="text"
								class="form-control"
								id="branchInput"
								placeholder="Branch"
							/>
						</div>
					</Col>
					<Col lg={12}>
						<div class="mb-3">
							<Label for="accountnameInput" class="form-label"
								>Account Holder Name</Label
							>
							<Input
								type="text"
								class="form-control"
								id="accountnameInput"
								placeholder="Enter account holder name"
							/>
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label
								for="accountnumberInput"
								class="form-label">Account Number</Label
							>
							<Input
								type="number"
								class="form-control"
								id="accountnumberInput"
								placeholder="Enter account number"
							/>
						</div>
					</Col>
					<Col lg={6}>
						<div class="mb-3">
							<Label for="ifscInput" class="form-label"
								>IFSC</Label
							>
							<Input
								type="number"
								class="form-control"
								id="ifscInput"
								placeholder="IFSC"
							/>
						</div>
					</Col>
					<Col lg={12}>
						<div class="hstack align-items-start gap-3 mt-4">
							<button
								on:click={() => {
									toggleTab(activeTab - 1);
								}}
								type="button"
								class="btn btn-light btn-label previestab"
								data-previous="pills-bill-info-tab"
							>
								<i
									class="ri-arrow-left-line label-icon align-middle fs-16 me-2"
								/>
								Back to Personal Info
							</button>
							<button
								on:click={() => {
									toggleTab(activeTab + 1);
								}}
								type="button"
								class="btn btn-primary btn-label right ms-auto nexttab"
								data-nexttab="pills-payment-tab"
							>
								<i
									class="ri-arrow-right-line label-icon align-middle fs-16 ms-2"
								/>
								Next Step
							</button>
						</div>
					</Col>
				</Row>
			</TabPane>

			<TabPane tabId={3} class={activeTab == 3 ? "active" : ""}>
				<h5 class="mb-3">Choose Document Type</h5>

				<div class="d-flex gap-2">
					<div>
						<input
							type="radio"
							class="btn-check"
							id="passport"
							defaultChecked
							name="choose-document"
						/>
						<Label class="btn btn-outline-primary" for="passport"
							>Passport</Label>
					</div>
					<div>
						<input
							type="radio"
							class="btn-check"
							id="aadhar-card"
							name="choose-document"
						/>
						<Label
							class="btn btn-outline-primary"
							for="aadhar-card">Aadhar Card</Label>
					</div>
					<div>
						<input
							type="radio"
							class="btn-check"
							id="pan-card"
							name="choose-document"
						/>
						<Label class="btn btn-outline-primary" for="pan-card"
							>Pan Card</Label>
					</div>
					<div>
						<input
							type="radio"
							class="btn-check"
							id="other"
							name="choose-document"
						/>
						<Label class="btn btn-outline-primary" for="other"
							>Other</Label>
					</div>
				</div>

				<Dropzone on:drop={handleFilesSelect}>
					<div>
						<div class="dz-message needsclick">
							<div class="dz-message needsclick">
								<div class="mb-3">
									<i
										class="display-4 text-muted bx bxs-cloud-upload"
									/>
								</div>
								<h4>Drop files here or click to upload.</h4>
							</div>
						</div>
					</div>
				</Dropzone>
				<div class="dropzone-previews mt-3" id="file-previews">
					{#each files.accepted as item}
						<Card
							class="mt-1 mb-0 shadow-none border dz-processing dz-image-preview dz-success dz-complete">
							<div class="p-2">
								<Row class="align-items-center">
									<Col>
										<Link
											href={null}
											class="text-muted font-weight-bold"
										>
											{item.name}
										</Link>
										<p class="mb-0">
											<strong>{item.size}</strong>
										</p>
									</Col>
								</Row>
							</div>
						</Card>
					{/each}
				</div>

				<div class="d-flex align-items-start gap-3 mt-4">
					<button
						on:click={() => {
							toggleTab(activeTab - 1);
						}}
						type="button"
						class="btn btn-light btn-label previestab"
						data-previous="pills-bill-address-tab"
					>
						<i
							class="ri-arrow-left-line label-icon align-middle fs-16 me-2"
						/>
						Back to Bank Details
					</button>
					<button
						on:click={() => {
							toggleTab(activeTab + 1);
						}}
						type="button"
						class="btn btn-primary btn-label right ms-auto nexttab"
						data-nexttab="pills-finish-tab"
					>
						<i
							class="ri-save-line label-icon align-middle fs-16 ms-2"
						/>
						Submit
					</button>
				</div>
			</TabPane>

			<TabPane tabId={4} class={activeTab == 4 ? "active" : ""}>
				<Row class="text-center justify-content-center">
					<Col lg={12}>
						<div class="mb-4">
							<lord-icon
								src="//cdn.lordicon.com/lupuorrc.json"
								trigger="loop"
								colors="primary:#8c68cd,secondary:#4788ff"
								style="width:120px;height:120px"
							/>
						</div>
						<h5>Verification Completed</h5>
						<p class="text-muted mb-4">
							To stay verified, don't remove the meta tag form
							your site's home page. To avoid losing
							verification, you may want to add multiple
							methods form the{" "}
							<span class="fw-medium"
								>Crypto KYC Application.</span
							>
						</p>

						<div class="hstack justify-content-center gap-2">
							<button
								on:click={toggleKycVerification}
								type="button"
								class="btn btn-ghost-success"
								data-bs-dismiss="modal"
							>
								Done{" "}
								<i
									class="ri-thumb-up-fill align-bottom me-1"
								/>
							</button>
							<button
								type="button"
								class="btn btn-primary"
							>
								<i
									class="ri-home-4-line align-bottom ms-1"
								/>{" "}
								Back to Home
							</button>
						</div>
					</Col>
				</Row>
			</TabPane>
		</TabContent>
	</div>
</Modal>
