<script>
	import {
		Col,
		Container,
		Row,
		Card,
		CardBody,
		Input,
		Button,
		Dropdown,
		DropdownToggle,
		DropdownMenu,
		DropdownItem,
		Form,
		Label,
	} from "sveltestrap";

	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import Select from "svelte-select";
	import crmData from "../../../common/data/crm";
	import Flatpickr from "svelte-flatpickr";
	import LeadDiscover from "../leadDiscover.svelte";
	import Modal from "../../../Components/Common/Modal.svelte";

	let sortBy = "Owner";

	const sortbyname = [
		{ label: "Owner", value: "Owner" },
		{ label: "Company", value: "Company" },
		{ label: "Location", value: "Location" },
	];

	let open = false;
	const toggle = () => (open = !open);
</script>

<svelte:head>
	<title>Deals | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Deals" pageTitle="CRM" />
		<Card>
			<CardBody>
				<Row class="g-3">
					<Col md={3}>
						<div class="search-box">
							<Input
								type="text"
								class="form-control search"
								placeholder="Search for deals..."
							/>
							<i class="ri-search-line search-icon" />
						</div>
					</Col>
					<div class="col-md-auto ms-auto">
						<div class="d-flex hastck gap-2 flex-wrap">
							<div class="d-flex align-items-center gap-2">
								<span class="text-muted flex-shrink-0">Sort by: </span>
								<Select
									class="mb-0"
									value={sortBy}
									items={sortbyname}
									id="choices-single-default"
								/>
							</div>
							<button class="btn btn-success" on:click={toggle}>
								<i class="ri-add-fill align-bottom me-1" /> Add Deals
							</button>
							<Dropdown>
								<DropdownToggle
									href={null}
									class="btn-soft-info btn-icon fs-14"
									tag="button"
								>
									<i class="ri-settings-4-line" />
								</DropdownToggle>
								<DropdownMenu class="dropdown-menu-end">
									<DropdownItem
										class="dropdown-item"
										href={null}>Copy</DropdownItem
									>
									<DropdownItem
										class="dropdown-item"
										href={null}>Move to pipline</DropdownItem
									>
									<DropdownItem
										class="dropdown-item"
										href={null}
										>Add to exceptions</DropdownItem
									>
									<DropdownItem
										class="dropdown-item"
										href={null}
									>
										Switch to common form view
									</DropdownItem>
									<DropdownItem
										class="dropdown-item"
										href={null}
									>
										Reset form view to default
									</DropdownItem>
								</DropdownMenu>
							</Dropdown>
						</div>
					</div>
				</Row>
			</CardBody>
		</Card>

		<Row class="row-cols-xxl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
			{#each crmData.deals as deal, index}
				<LeadDiscover {deal} {index} />
			{/each}
		</Row>
	</Container>
</div>

<Modal isOpen={open}>
	<div class="modal-header bg-light p-3">
		<h5 class="modal-title" id="createFileModalLabel">Create Folder</h5>
		<button type="button" class="btn-close" on:click={toggle} />
	</div>
	<div class="modal-body">
		<div class="mb-3">
			<Label for="dealTitle" class="form-label">Deal Title</Label>
			<Input
				type="email"
				class="form-control"
				id="dealTitle"
				placeholder="Enter title"
			/>
		</div>
		<div class="mb-3">
			<Label for="dealValue" class="form-label">Value (USD)</Label>
			<Input
				type="text"
				class="form-control"
				id="dealValue"
				placeholder="Enter value"
			/>
		</div>
		<div class="mb-3">
			<Label for="dealOwner" class="form-label">Deals Owner</Label>
			<Input
				type="text"
				class="form-control"
				id="dealOwner"
				placeholder="Enter owner name"
			/>
		</div>
		<div class="mb-3">
			<Label for="dueDate" class="form-label">Due Date</Label>
			<Flatpickr
				class="form-control"
				id="datepicker-publish-input"
				placeholder="Select a date"
				items={{
					altInput: true,
					altFormat: "F j, Y",
					mode: "multiple",
					dateFormat: "d.m.y",
				}}
			/>
		</div>
		<div class="mb-3">
			<Label for="emailId" class="form-label">Email</Label>
			<Input
				type="text"
				class="form-control"
				id="emailId"
				placeholder="Enter email"
			/>
		</div>
		<div class="mb-3">
			<Label for="contactNumber" class="form-label">Contact</Label>
			<Input
				type="text"
				class="form-control"
				id="contactNumber"
				placeholder="Enter contact number"
			/>
		</div>
		<div class="mb-3">
			<Label for="contactNumber" class="form-label">Description</Label>
			<Input
				name="text"
				type="textarea"
				class="form-control"
				id="exampleFormControlTextarea1"
				rows="3"
				placeholder="Enter description"
			/>
		</div>
	</div>
	<div class="modal-footer">
		<Button color="light" on:click={toggle}>Close</Button>
		<Button color="success" on:click={toggle}>
			<i class="ri-save-line align-bottom me-1" /> Save
		</Button>
	</div>
</Modal>
