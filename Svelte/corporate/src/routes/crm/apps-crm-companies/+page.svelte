<script>
	import {
		Col,
		Container,
		Row,
		Card,
		CardHeader,
		CardBody,
		ModalBody,
		Label,
		Input,
		Form,
		Button,
		Dropdown,
		DropdownToggle,
		DropdownMenu,
		DropdownItem,
		Table,
	} from "sveltestrap";
	import Select from "svelte-select";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";
	import * as yup from "yup";
	import { SvelteWrapper } from "gridjs-svelte/plugins";
	import CompanyAction from "../CompanyAction.svelte";
	import { onMount } from "svelte";
	import { createForm } from "svelte-forms-lib";
	import Modal from "../../../Components/Common/Modal.svelte";
	import {
		getCompanies,
		addNewCompanies,
		updateCompanies,
	} from "../../../helpers/fakebackend_helper";

	import mail_chimp from "../../../assets/images/brands/mail_chimp.png";

	let open = false;
	const toggle = () => (open = !open);

	let sortBy = "Owner";
	const sortbyname = [
		{ label: "Owner", value: "Owner" },
		{ label: "Company", value: "Company" },
		{ label: "Location", value: "Location" },
	];

	const industrytype = [
		{ label: "Select industry type", value: "Select industry type" },
		{ label: "Computer Industry", value: "Computer Industry" },
		{ label: "Chemical Industries", value: "Chemical Industries" },
		{ label: "Health Services", value: "Health Services" },
		{
			label: "Telecommunications Services",
			value: "Telecommunications Services",
		},
		{
			label: "Textiles: Clothing, Footwear",
			value: "Textiles: Clothing, Footwear",
		},
	];

	let data = [];
	let isEdit = false;
	let company = [];

	onMount(async () => {
		const res = await getCompanies();
		data = res;
	});

	const columns = [
		{
			name: "#",
			width: "40px",
			formatter: (cell) =>
				html(`<div class="form-check">
              <input class="form-check-input" type="checkbox" name="checkAll" value="option1" />
            </div>`),
		},
		{
			id: "image_src",
			hidden: true,
		},
		{
			id: "name",
			name: "Company Name",
			sort: true,
			formatter: (cell, row) => {
				if (row.cells[1].data) {
					return html(`<div class="d-flex align-items-center">
				<div class="flex-shrink-0">
					<img
					src="${import.meta.env.VITE_PUBLIC_BASE_PATH + "/images/" + row.cells[1].data}"
					alt=""
					class="avatar-xxs rounded-circle"
					/>
				</div>
				<div class="flex-grow-1 ms-2 name">
					${cell}
				</div>
				</div>`);
				} else {
					return html(`<div class="d-flex align-items-center">
						<div class="flex-shrink-0 avatar-xs me-2">
							<div class="avatar-title bg-success-subtle text-success rounded-circle fs-13">
							${cell.charAt(0)}
							</div>
						</div>
						<div class="flex-grow-1 ms-2 name">
							${cell}
						</div>
				</div>`);
				}
			},
		},
		{
			id: "owner",
			name: "Owner",
			sort: true,
		},
		{
			id: "industry_type",
			name: "Industry Type",
			sort: true,
		},
		{
			id: "star_value",
			name: "Rating",
			sort: true,
			formatter: (cell) => {
				if (cell) {
					return html(
						`<span class="star_value">${cell}</span> <i class="ri-star-fill text-warning align-bottom"></i>`
					);
				}
			},
		},
		{
			id: "location",
			name: "Location",
			sort: true,
		},
		{
			name: "Action",
			formatter: (cell, row) =>
				html(`<ul class="list-inline hstack gap-2 mb-0">
                <li class="list-inline-item edit">
                    <Link href={null} class="text-muted d-inline-block">
                        <i class="ri-phone-line fs-16"></i>
                    </Link>
                </li>
                <li class="list-inline-item edit">
                    <Link href={null} class="text-muted d-inline-block">
                        <i class="ri-question-answer-line fs-16"></i>
                    </Link>
                </li>
                <li class="list-inline-item">
                    <Link href={null}>
                        <i class="ri-eye-fill align-bottom text-muted"></i>
                    </Link>
                </li>
                <li class="list-inline-item">
                    <Link class="edit-item-btn" href={null}>
                        <i class="ri-pencil-fill align-bottom text-muted"></i>
                    </Link>
                </li>
                <li class="list-inline-item">
                    <Link class="remove-item-btn" href={null}>
                        <i class="ri-delete-bin-fill align-bottom text-muted"></i>
                    </Link>
                </li>
            </ul>`),
		},
	];

	const { form, handleChange, handleSubmit, handleReset } = createForm({
		initialValues: {
			name: (company && company.name) || "",
			owner: (company && company.owner) || "",
			industry_type: (company && company.industry_type) || "",
			star_value: (company && company.star_value) || "",
			location: (company && company.location) || "",
			employee: (company && company.employee) || "",
			website: (company && company.website) || "",
			contact_email: (company && company.contact_email) || "",
			since: (company && company.since) || "",
		},
		validationSchema: yup.object().shape({
			name: yup.string().required("Please Enter Company Name"),
			owner: yup.string().required("Please Enter Owner name"),
			// industry_type: yup.string().required("Please Enter Industry Type"),
			star_value: yup.string().required("Please Enter Rating"),
			location: yup.string().required("Please Enter Location"),
			employee: yup.string().required("Please Enter Employee"),
			website: yup.string().required("Please Enter Website"),
			contact_email: yup.string().required("Please Enter Contact Email"),
			since: yup.string().required("Please Enter Since"),
		}),

		onSubmit: (values) => {
			if (isEdit) {
				console.lo;
				var updatedCompany = {
					_id: company ? company._id : 0,
					name: values.name,
					owner: values.owner,
					industry_type: values.industry_type,
					star_value: values.star_value,
					location: values.location,
					employee: values.employee,
					website: values.website,
					contact_email: values.contact_email,
					since: values.since,
				};

				const newres = waitforResponse("update", updatedCompany);
				handleReset();
				open = false;
			} else {
				var newcompany = {
					_id: (
						Math.floor(Math.random() * (30 - 20)) + 20
					).toString(),
					name: values["name"],
					owner: values["owner"],
					industry_type: values["industry_type"].value,
					star_value: values["star_value"],
					location: values["location"],
					employee: values["employee"],
					website: values["website"],
					contact_email: values["contact_email"],
					since: values["since"],
				};

				const newres = waitforResponse("create", newcompany);
				handleReset();
				open = false;
			}
		},
	});

	async function waitforResponse(action, newcompany) {
		if (action == "update") {
			const res = await updateCompanies(newcompany);
			data.map((allcompany) =>
				allcompany._id.toString() === res._id.toString()
					? { ...allcompany, ...res }
					: allcompany
			);
		} else {
			const res = await addNewCompanies(newcompany);
			data = [...data, res];
		}
		return true;
	}
</script>

<svelte:head>
	<title>Companies | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Companies" pageTitle="CRM" />
		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader>
						<div class="d-flex align-items-center flex-wrap gap-2">
							<div class="flex-grow-1">
								<Button
									class="btn btn-secondary add-btn"
									on:click={toggle}
									><i class="ri-add-fill me-1 align-bottom" />
									Add Company</Button
								>
							</div>
							<div class="flex-shrink-0">
								<div class="hstack text-nowrap gap-2">
									<Button
										color=""
										class="btn btn-soft-danger"
										id="remove-actions"
										><i
											class="ri-delete-bin-2-line"
										/></Button
									>
									<Button
										color="primary"
										data-bs-toggle="modal"
										data-bs-target="#addmembers"
										><i
											class="ri-filter-2-line me-1 align-bottom"
										/> Filters</Button
									>
									<Button
										color=""
										class="btn btn-soft-success"
										>Import</Button
									>
									<Dropdown>
										<DropdownToggle
											href={null}
											class="btn btn-soft-info"
											color=""
										>
											<i class="ri-more-2-fill" />
										</DropdownToggle>
										<DropdownMenu class="dropdown-menu-end">
											<DropdownItem href={null}
												>All</DropdownItem
											>
											<DropdownItem href={null}
												>Last Week</DropdownItem
											>
											<DropdownItem href={null}
												>Last Month</DropdownItem
											>
											<DropdownItem href={null}
												>Last Year</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</div>
							</div>
						</div>
					</CardHeader>
				</Card>
			</Col>
			<!--end col-->
			<Col xxl={9}>
				<Card id="companyList">
					<CardHeader>
						<Row class="g-2">
							<Col md={3}>
								<div class="search-box">
									<Input
										type="text"
										class="form-control search"
										placeholder="Search for company..."
									/>
									<i class="ri-search-line search-icon" />
								</div>
							</Col>
							<div class="col-md-auto ms-auto">
								<div class="d-flex align-items-center gap-2">
									<span class="text-muted">Sort by: </span>
									<div class="select-single">
										<Select
											id="choices-single-default"
											value={sortBy}
											items={sortbyname}
										/>
									</div>
								</div>
							</div>
						</Row>
					</CardHeader>
					<CardBody>
						<div>
							<div
								class="table-responsive table-card gridjs-border-none"
							>
								{#if (data.length || []) > 0}
									<Grid
										{data}
										{columns}
										class={{ th: "text-muted" }}
										pagination={{
											enabled: true,
											limit: 10,
										}}
									/>
								{:else}
									<div class="noresult">
										<div class="text-center">
											<lord-icon
												src="//cdn.lordicon.com/msoeawqm.json"
												trigger="loop"
												colors="primary:#121331,secondary:#08a88a"
												style="width:75px;height:75px"
											/>
											<h5 class="mt-2">
												Sorry! No Result Found
											</h5>
											<p class="text-muted mb-0">
												We've searched more than 150+
												companies We did not find any
												companies for you search.
											</p>
										</div>
									</div>
								{/if}
							</div>
						</div>

						<Modal isOpen={open} className="modal-dialog-centered modal-lg">
							<div class="modal-header p-3 bg-info-subtle">
								<h5
									class="modal-title"
									id="createFileModalLabel"
								>
									Create Folder
								</h5>
								<button
									type="button"
									class="btn-close"
									on:click={toggle}
								/>
							</div>
							<div class="modal-body">
								<Input type="hidden" id="id-field" />
								<div class="row g-3">
									<Col lg={12}>
										<div>
											<Label
												for="name-field"
												class="form-label">Name</Label
											>
											<Input
												type="text"
												id="customername-field"
												class="form-control"
												placeholder="Enter company name"
												name="name"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.name}
												required
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div>
											<Label
												for="owner-field"
												class="form-label"
												>Owner Name</Label
											>
											<Input
												type="text"
												id="owner-field"
												class="form-control"
												placeholder="Enter owner name"
												required
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.owner}
												name="owner"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div>
											<Label
												for="industry_type-field"
												class="form-label"
												>Industry Type</Label
											>
											<Select
												id="industry_type-field"
												items={industrytype}
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.industry_type}
												name="industry_type"
											/>
										</div>
									</Col>
									<Col lg={4}>
										<div>
											<Label
												for="star_value-field"
												class="form-label">Rating</Label
											>
											<Input
												type="text"
												id="star_value-field"
												class="form-control"
												placeholder="Enter rating"
												required
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.star_value}
												name="star_value"
											/>
										</div>
									</Col>
									<Col lg={4}>
										<div>
											<Label
												for="location-field"
												class="form-label"
												>location</Label
											>
											<Input
												type="text"
												id="location-field"
												class="form-control"
												placeholder="Enter location"
												required
												name="location"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.location}
											/>
										</div>
									</Col>
									<Col lg={4}>
										<div>
											<Label
												for="employee-field"
												class="form-label"
												>Employee</Label
											>
											<Input
												type="text"
												id="employee-field"
												class="form-control"
												placeholder="Enter employee"
												required
												name="employee"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.employee}
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div>
											<Label
												for="website-field"
												class="form-label"
												>Website</Label
											>
											<Input
												type="text"
												id="website-field"
												class="form-control"
												placeholder="Enter website"
												required
												name="website"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.website}
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div>
											<Label
												for="contact_email-field"
												class="form-label"
												>Contact Email</Label
											>
											<Input
												type="text"
												id="contact_email-field"
												class="form-control"
												placeholder="Enter contact email"
												required
												name="contact_email"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.contact_email}
											/>
										</div>
									</Col>
									<Col lg={12}>
										<div>
											<Label
												for="since-field"
												class="form-label">Since</Label
											>
											<Input
												type="text"
												id="since-field"
												class="form-control"
												placeholder="Enter since"
												required
												name="since"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.since}
											/>
										</div>
									</Col>
								</div>
							</div>
							<div class="modal-footer">
								<div class="hstack gap-2 justify-content-end">
									<Button
										class="btn btn-light"
										on:click={toggle}>Close</Button
									>
									<button
										class="btn btn-success"
										id="add-btn"
										type="submit"
										>{!!isEdit
											? "Update"
											: "Add Company"}</button
									>
								</div>
							</div>
						</Modal>
						<!--end add modal-->
					</CardBody>
				</Card>
				<!--end card-->
			</Col>
			<!--end col-->
			<Col xxl={3}>
				<Card id="company-view-detail">
					<CardBody class="text-center">
						<div class="position-relative d-inline-block">
							<div class="avatar-md">
								<div
									class="avatar-title bg-light rounded-circle"
								>
									<img
										src={mail_chimp}
										alt=""
										class="avatar-sm"
									/>
								</div>
							</div>
						</div>
						<h5 class="mt-3 mb-1">Syntyce Solution</h5>
						<p class="text-muted">Michael Morris</p>

						<ul class="list-inline mb-0">
							<li class="list-inline-item avatar-xs">
								<a
									href={null}
									class="avatar-title bg-success-subtle text-success fs-15 rounded"
								>
									<i class="ri-global-line" />
								</a>
							</li>
							<li class="list-inline-item avatar-xs">
								<a
									href={null}
									class="avatar-title bg-danger-subtle text-danger fs-15 rounded"
								>
									<i class="ri-mail-line" />
								</a>
							</li>
							<li class="list-inline-item avatar-xs">
								<a
									href={null}
									class="avatar-title bg-warning-subtle text-warning fs-15 rounded"
								>
									<i class="ri-question-answer-line" />
								</a>
							</li>
						</ul>
					</CardBody>
					<CardBody>
						<h6 class="text-muted text-uppercase fw-semibold mb-3">
							Information
						</h6>
						<p class="text-muted mb-4">
							A company incurs fixed and variable costs such as
							the purchase of raw materials, salaries and
							overhead, as explained by AccountingTools, Inc.
							Business owners have the discretion to determine the
							actions.
						</p>
						<div class="table-responsive table-card">
							<Table class="table table-borderless mb-0">
								<tbody>
									<tr>
										<td class="fw-medium">Industry Type</td>
										<td>Chemical Industries</td>
									</tr>
									<tr>
										<td class="fw-medium">Location</td>
										<td>Damascus, Syria</td>
									</tr>
									<tr>
										<td class="fw-medium">Employee</td>
										<td>10-50</td>
									</tr>
									<tr>
										<td class="fw-medium">Rating</td>
										<td
											>4.0 <i
												class="ri-star-fill text-warning align-bottom"
											/></td
										>
									</tr>
									<tr>
										<td class="fw-medium">Website</td>
										<td>
											<a
												href={null}
												class="link-primary text-decoration-underline"
												>www.syntycesolution.com</a
											>
										</td>
									</tr>
									<tr>
										<td class="fw-medium">Contact Email</td>
										<td>info@syntycesolution.com</td>
									</tr>
									<tr>
										<td class="fw-medium">Since</td>
										<td>1995</td>
									</tr>
								</tbody>
							</Table>
						</div>
					</CardBody>
				</Card>
				<!--end card-->
			</Col>
			<!--end col-->
		</Row>
	</Container>
</div>
