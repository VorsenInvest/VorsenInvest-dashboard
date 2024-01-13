<script>
	import {
		Container,
		Card,
		CardHeader,
		Row,
		Col,
		Dropdown,
		DropdownToggle,
		DropdownMenu,
		DropdownItem,
		CardBody,
		Button,
		Input,
		Label,
	} from "sveltestrap";
	import { onMount } from "svelte";
	import * as yup from "yup";
	import {
		getLeads,
		addNewLead,
		updateLead,
		deleteLead,
	} from "../../../helpers/fakebackend_helper";
	import { createForm } from "svelte-forms-lib";
	import DeleteModal from "../../../Components/Common/CDeleteModal.svelte";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import crmData from "../../../common/data/crm";
	import dayjs from "dayjs";
	import Grid from "gridjs-svelte";
	import { html } from "gridjs";
	import Flatpickr from "svelte-flatpickr";
	import CrmFilter from "../CrmFilter.svelte";
	import Modal from "../../../Components/Common/Modal.svelte";

	let open = false;
	let filteropen = false;
	let deleteModal = false;

	let data = [];

	onMount(async () => {
		const res = await getLeads();
		data = res;
	});

	function handleValidDate(todaydate) {
		const datwe = dayjs(todaydate).format("DD MMM YYYY");
		return datwe;
	}

	const columns = [
		{
			name: "#",
			width: "40px",
			formatter: (cell) =>
				html(
					`<div class="form-check"><input type="checkbox" class="form-check-input"/></div>`
				),
		},
		{
			id: "name",
			name: "Name",
			sort: true,
		},
		{
			id: "company",
			name: "Company",
			sort: true,
		},
		{
			id: "score",
			name: "Leads Score",
			sort: true,
		},
		{
			id: "phone",
			name: "Phone No",
			sort: true,
		},
		{
			id: "location",
			name: "Location",
			sort: true,
		},
		{
			id: "date",
			name: "Create Date",
			sort: true,
			formatter: (cell, row) => html(`${handleValidDate(cell)}`),
		},
		{
			name: "Action",
			formatter: (cell, row) =>
				html(`<ul class="list-inline hstack gap-2 mb-0">
				<li class="list-inline-item edit">
					<a href={null} class="text-muted d-inline-block">
						<i class="ri-phone-line fs-16"></i>
					</a>
				</li>
				<li class="list-inline-item edit">
					<a href={null} class="text-muted d-inline-block">
						<i class="ri-question-answer-line fs-16"></i>
					</a>
				</li>
				<li class="list-inline-item">
					<a href={null}>
						<i class="ri-eye-fill align-bottom text-muted"></i>
					</a>
				</li>
				<li class="list-inline-item">
					<a class="edit-item-btn" href={null}>
						<i class="ri-pencil-fill align-bottom text-muted"></i>
					</a>
				</li>
				<li class="list-inline-item">
					<a class="remove-item-btn" href={null}>
						<i class="ri-delete-bin-fill align-bottom text-muted"></i>
					</a>
				</li>
			</ul>`),
		},
	];

	const setDeleteModal = (status) => {
		deleteModal = status;
	};

	const setIsInfoDetails = (status) => {
		filteropen = status;
	};

	const defaultdate = () => {
		let d = new Date(),
			months = [
				"Jan",
				"Feb",
				"Mar",
				"Apr",
				"May",
				"Jun",
				"Jul",
				"Aug",
				"Sep",
				"Oct",
				"Nov",
				"Dec",
			];
		return (
			d.getDate() +
			" " +
			months[d.getMonth()] +
			", " +
			d.getFullYear()
		).toString();
	};

	const dateformate = (e) => {
		const date = e.toString().split(" ");
		const joinDate = (date[2] + " " + date[1] + ", " + date[3]).toString();
		setDate = joinDate;
	};

	var setDate = defaultdate();
	var lead = [];
	var isEdit = false;

	const toggle = () => {
		open = !open;
		setDate = defaultdate();
		isEdit = false;
	};
	const filterToggle = () => (filteropen = !filteropen);

	const { form, errors, handleChange, handleSubmit, handleReset } = createForm({
		initialValues: {
			name: "",
			company: "",
			score: "",
			phone: "",
			location: "",
			date: "",
		},
		validationSchema: yup.object().shape({
			name: yup.string().required("Please Enter Valid Name"),
			company: yup.string().required("Please Enter Valid company"),
			score: yup.string().required("Please Enter score"),
			phone: yup.string().required("Please Enter phone"),
			location: yup.string().required("Please Enter location"),
		}),
		onSubmit: (values) => {
			if (isEdit) {
				var updateLead = {
					_id: lead ? lead._id : 0,
					name: values.name,
					company: values.company,
					score: values.score,
					phone: values.phone,
					location: values.location,
					date: setDate,
				};

				const newres = waitforResponse("update", updateLead);
				handleReset();
				open = false;
			} else {
				var newLead = {
					_id: (
						Math.floor(Math.random() * (30 - 20)) + 20
					).toString(),
					name: values["name"],
					company: values["company"],
					score: values["score"],
					phone: values["phone"],
					location: values["location"],
					date: setDate,
				};

				const newres = waitforResponse("create", newLead);
				handleReset();
				open = false;
			}
		},
	});

	async function waitforResponse(action, newLead) {
		if (action == "update") {
			const res = await updateLead(newLead);
			data.map((alllead) =>
				alllead._id.toString() === res._id.toString()
					? { ...alllead, ...res }
					: alllead
			);
		} else {
			const res = await addNewLead(newLead);
			data = [...data, res];
		}

		return true;
	}
</script>

<svelte:head>
	<title>Leads | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Leads" pageTitle="CRM" />
		<Row>
			<Col lg={12}>
				<Card id="leadsList">
					<CardHeader class="border-0">
						<Row class="g-4 align-items-center">
							<Col sm={3}>
								<div class="search-box">
									<Input
										type="text"
										class="form-control search"
										placeholder="Search for..."
									/>
									<i class="ri-search-line search-icon" />
								</div>
							</Col>
							<div class="col-sm-auto ms-auto">
								<div class="hstack gap-2">
									<Button 
										type="button"
										class="btn btn-secondary"
										on:click={filterToggle}
									>
										<i
											class="ri-filter-3-line align-bottom me-1"
										/> Fliters</Button
									>
									<Button color="primary"
										type="button"
										class="add-btn"
										on:click={toggle}
										><i
											class="ri-add-line align-bottom me-1"
										/> Add Leads</Button
									>
									<Dropdown>
										<DropdownToggle
											class="btn btn-soft-primary btn-icon fs-14"
											color=""
											id="dropdownMenuButton1"
										>
											<i class="ri-settings-4-line" />
										</DropdownToggle>
										<DropdownMenu>
											<DropdownItem href={null}
												>Copy</DropdownItem
											>
											<DropdownItem href={null}
												>Move to pipline</DropdownItem
											>
											<DropdownItem href={null}
												>Add to exceptions</DropdownItem
											>
											<DropdownItem href={null}
												>Switch to common form view</DropdownItem
											>
											<DropdownItem href={null}
												>Reset form view to default</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</div>
							</div>
						</Row>
					</CardHeader>
					<CardBody>
						<div>
							<div
								class="table-responsive table-card gridjs-border-none"
							>
								{#if crmData.leads.length > 0}
									<Grid
										{data}
										{columns}
										class={{ th: "text-muted" }}
										pagination={{
											enabled: true,
											limit: 8,
										}}
									/>
								{:else}
									<div class="noresult">
										<div class="text-center">
											<lord-icon
												src="//cdn.lordicon.com/msoeawqm.json"
												trigger="loop"
												colors="primary:#8c68cd,secondary:#4788ff"
												style="width:75px;height:75px"
											/>
											<h5 class="mt-2">
												Sorry! No Result Found
											</h5>
											<p class="text-muted mb-0">
												We've searched more than 150+
												leads We did not find any leads
												for you search.
											</p>
										</div>
									</div>
								{/if}
							</div>
						</div>

						<Modal isOpen={open} className="modal-dialog-centered">
							<div class="modal-header p-3 bg-light">
								<h5 class="modal-title">Add Leads</h5>
								<button
									type="button"
									class="btn-close"
									on:click={toggle}
								/>
							</div>
							<div class="modal-body">
								<Input type="hidden" id="id-field" />
								<Row class="g-3">
									<div class="col-lg-12">
										<div>
											<Label
												for="name-field"
												class="form-label">Name</Label
											>
											<Input
												type="text"
												id="customername-field"
												name="name"
												class="form-control"
												placeholder="Enter Name"
												on:change={handleChange}
												on:blur={handleChange}
												required
											/>
										</div>
									</div>
									<!--end col-->
									<div class="col-lg-12">
										<div>
											<Label
												for="company_name-field"
												class="form-label"
												>Company Name</Label
											>
											<Input
												type="text"
												name="company"
												id="company_name-field"
												class="form-control"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.company}
												placeholder="Enter company name"
												required
											/>
										</div>
									</div>
									<!--end col-->
									<div class="col-lg-6">
										<div>
											<Label
												for="leads_score-field"
												class="form-label"
												>Leads Score</Label
											>
											<Input
												type="text"
												name="score"
												id="leads_score-field"
												class="form-control"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.score}
												placeholder="Enter lead score"
												required
											/>
										</div>
									</div>
									<!--end col-->
									<div class="col-lg-6">
										<div>
											<Label
												for="phone-field"
												class="form-label">Phone</Label
											>
											<Input
												type="text"
												id="phone-field"
												name="phone"
												class="form-control"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.phone}
												placeholder="Enter phone no"
												required
											/>
										</div>
									</div>
									<!--end col-->
									<div class="col-lg-12">
										<div>
											<Label
												for="location-field"
												class="form-label"
												>Location</Label
											>
											<Input
												type="text"
												id="location-field"
												class="form-control"
												name="location"
												on:change={handleChange}
												on:blur={handleChange}
												bind:value={$form.location}
												placeholder="Enter location"
												required
											/>
										</div>
									</div>
									<!--end col-->
									<div class="col-lg-12">
										<div>
											<Label
												for="date-field"
												class="form-label"
												>Created Date</Label
											>
											<Flatpickr
												class="form-control"
												id="datepicker-publish-input"
												name="date"
												on:blur={handleChange}
												placeholder="Select a date"
												items={{
													altInput: true,
													altFormat: "F j, Y",
													mode: "multiple",
													dateFormat: "d.m.y",
												}}
											/>
										</div>
									</div>
									<!--end col-->
								</Row>
							</div>
							<div class="modal-footer">
								<div class="hstack gap-2 justify-content-end">
									<Button
										type="button"
										class="btn btn-light"
										on:click={toggle}>Close</Button
									>
									<button
										class="btn btn-success"
										id="add-btn"
										type="submit">Add leads</button
									>
								</div>
							</div>
						</Modal>
						<!--end modal-->

						<DeleteModal
							show={deleteModal}
							onCloseClick={() => setDeleteModal(false)}
						/>

						<CrmFilter
							show={filteropen}
							onCloseClick={() => setIsInfoDetails(false)}
						/>

						<!--end offcanvas-->
					</CardBody>
				</Card>
			</Col>
			<!--end col-->
		</Row>
	</Container>
</div>
