<script>
	import {
		Card,
		CardBody,
		Button,
		Col,
		Input,
		Label,
		Row,
	} from "sveltestrap";
	import Select from "svelte-select";
	import Flatpickr from "svelte-flatpickr";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";
	import { onMount } from "svelte";
	import { createForm } from "svelte-forms-lib";
	import * as yup from "yup";
	import {
		getTicketsList,
		addNewTicket,
		updateTicket,
	} from "../../../helpers/fakebackend_helper";
	import Modal from "../../../Components/Common/Modal.svelte";

	const allStatus = [
		{ label: "Status", value: "Status" },
		{ label: "All", value: "All" },
		{ label: "Open", value: "Open" },
		{ label: "Inprogress", value: "Inprogress" },
		{ label: "Closed", value: "Closed" },
		{ label: "New", value: "New" },
	];

	let data = [];

	onMount(async () => {
		const res = await getTicketsList();
		data = res;
	});

	const isEdit = false;
	let open = false;
	const toggle = () => (open = !open);
	let ticket = [];

	const dateFormat = () => {
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

	let credate = dateFormat();
	let duedate = dateFormat();

	const { form, handleChange, handleSubmit, handleReset } = createForm({
		initialValues: {
			id: (ticket && ticket.id) || "",
			title: (ticket && ticket.title) || "",
			client: (ticket && ticket.client) || "",
			assigned: (ticket && ticket.assigned) || "",
			create: (ticket && ticket.create) || "",
			due: (ticket && ticket.due) || "",
			status: (ticket && ticket.status) || "",
			priority: (ticket && ticket.priority) || "",
		},
		validationSchema: yup.object().shape({
			id: yup.string().required("Please Enter id"),
			title: yup.string().required("Please Enter Title"),
			client: yup.string().required("Please Enter Client Name"),
			assigned: yup.string().required("Please Enter Assigned Name"),
			status: yup.string().required("Please Enter Your Joining status"),
			priority: yup.string().required("Please Enter Your Priority"),
		}),

		onSubmit: (values) => {
			if (isEdit) {
				var updatedTask = {
					_id: ticket ? ticket._id : 0,
					id: values.id,
					title: values.title,
					client: values.client,
					assigned: values.assigned,
					create: credate,
					due: duedate,
					status: values.status,
					priority: values.priority,
				};

				const newres = waitforResponse("update", updatedTask);
				handleReset();
				open = false;
			} else {
				var newcticket = {
					_id: (
						Math.floor(Math.random() * (30 - 20)) + 20
					).toString(),
					id: values["id"],
					title: values["title"],
					client: values["client"],
					assigned: values["assigned"],
					create: credate,
					due: duedate,
					status: values["status"],
					priority: values["priority"],
				};

				const newres = waitforResponse("create", newcticket);
				handleReset();
				open = false;
			}
		},
	});

	async function waitforResponse(action, newcticket) {
		if (action == "update") {
			const res = await updateTicket(newcticket);
			data.map((allticket) =>
				allticket._id.toString() === res._id.toString()
					? { ...allticket, ...res }
					: allticket
			);
		} else {
			const res = await addNewTicket(newcticket);
			data = [...data, res];
		}
		return true;
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
			id: "id",
			name: "ID",
			formatter: (cell) =>
				html(
					`<a href="/support/ticketsdetails/apps-tickets-details" class="fw-medium link-primary">${cell}</a>`
				),
		},
		{
			id: "title",
			name: "Title",
		},
		{
			id: "client",
			name: "Client",
		},
		{
			id: "assigned",
			name: "Assigned To",
		},
		{
			id: "create",
			name: "Create Date",
		},
		{
			id: "due",
			name: "Due Date",
		},
		{
			id: "status",
			name: "Status",
			formatter: (cell) => {
				if (cell == "Inprogress") {
					return html(
						`<span class="badge bg-warning-subtle text-warning text-uppercase">${cell}</span>`
					);
				} else if (cell == "Open") {
					return html(
						`<span class="badge bg-success-subtle text-success text-uppercase">${cell}</span>`
					);
				} else if (cell == "New") {
					return html(
						`<span class="badge bg-info-subtle text-info text-uppercase">${cell}</span>`
					);
				} else if (cell == "Closed") {
					return html(
						`<span class="badge bg-danger-subtle text-danger text-uppercase">${cell}</span>`
					);
				} else {
					return null;
				}
			},
		},
		{
			id: "priority",
			name: "Priority",
			formatter: (cell) => {
				if (cell == "Medium") {
					return html(
						`<span class="badge bg-warning text-uppercase">${cell}</span>`
					);
				} else if (cell == "High") {
					return html(
						`<span class="badge bg-danger text-uppercase">${cell}</span>`
					);
				} else if (cell == "Low") {
					return html(
						`<span class="badge bg-success text-uppercase">${cell}</span>`
					);
				} else {
					return null;
				}
			},
		},
		{
			name: "Action",
			formatter: (cell, row) =>
				html(`<ul class="list-inline hstack gap-2 mb-0">
				<li class="list-inline-item edit">
					<a href={null} class="text-muted d-inline-block">
						<i class="ri-eye-fill align-bottom me-2 text-muted"></i>
					</a>
				</li>
				<li class="list-inline-item edit">
					<a href={null} class="text-muted d-inline-block">
						<i class="ri-pencil-fill align-bottom me-2 text-muted"></i>
					</a>
				</li>
				<li class="list-inline-item">
					<a href={null}>
						<i class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>
					</a>
				</li>
			</ul>`),
		},
	];
</script>

<Row>
	<Col lg={12}>
		<Card id="ticketsList">
			<div class="card-header border-0">
				<div class="d-flex align-items-center">
					<h5 class="card-title mb-0 flex-grow-1">Tickets</h5>
					<div class="flex-shrink-0">
						<div class="d-flex flex-wrap gap-2">
							<button
								class="btn btn-danger add-btn"
								on:click={toggle}
								><i class="ri-add-line align-bottom me-1" /> Create
								Tickets</button
							>
							<!-- <button class="btn btn-success"
								><i class="ri-delete-bin-2-line" /></button
							> -->
						</div>
					</div>
				</div>
			</div>
			<CardBody class="border border-dashed border-end-0 border-start-0">
				<form>
					<Row class="g-3">
						<Col xxl={5} sm={12}>
							<div class="search-box">
								<input
									type="text"
									class="form-control search bg-light border-light"
									placeholder="Search for ticket details or something..."
								/>
								<i class="ri-search-line search-icon" />
							</div>
						</Col>
						<!--end col-->

						<Col xxl={3} sm={4}>
							<Flatpickr
								class="form-control bg-light border-light"
								options={{
									dateFormat: "d M, Y",
								}}
								placeholder="Selact Date"
							/>
						</Col>
						<!--end col-->

						<Col xxl={3} sm={4}>
							<div class="select-single">
								<Select id="idStatus" items={allStatus} />
							</div>
						</Col>
						<!--end col-->
						<div class="col-xxl-1 col-sm-4">
							<button type="button" class="btn btn-primary w-100">
								<i
									class="ri-equalizer-fill me-1 align-bottom"
								/>
								Filters
							</button>
						</div>
						<!--end col-->
					</Row>
					<!--end row-->
				</form>
			</CardBody>
			<!--end card-body-->
			<CardBody>
				<div class="table-card gridjs-border-none">
					{#if (data.length || []) > 0}
						<Grid
							{data}
							{columns}
							class={{ th: "text-muted" }}
							pagination={{ enabled: true, limit: 10 }}
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
								<h5 class="mt-2">Sorry! No Result Found</h5>
								<p class="text-muted mb-0">
									We've searched more than 200k+ tasks We did
									not find any tasks for you search.
								</p>
							</div>
						</div>
					{/if}
				</div>

				<Modal isOpen={open} className="modal-dialog-centered modal-lg">
					<div class="modal-header p-3 bg-info-subtle">
						<h5 class="modal-title"> {!!isEdit ? "Edit Ticket" : "Add Ticket"} </h5>
						<button
							type="button"
							class="btn-close"
							on:click={toggle}
						/>
					</div>
					<form on:submit|preventDefault={handleSubmit}>
					<div class="modal-body">
						<Row class="g-3">
							<Col lg={12}>
								<div>
									<Label
										htmlFor="tasksTitle-field"
										class="form-label">Title</Label
									>
									<Input
										name="title"
										id="tasksTitle-field"
										class="form-control"
										placeholder="Enter Title"
										type="text"
										on:change={handleChange}
										on:blur={handleChange}
										bind:value={$form.title}
									/>
								</div>
							</Col>
							<Col lg={6}>
								<div>
									<Label
										htmlFor="client_nameName-field"
										class="form-label">Client</Label
									>
									<Input
										name="client"
										type="text"
										id="client_nameName-field"
										placeholder="Enter Client Name"
										on:change={handleChange}
										on:blur={handleChange}
										bind:value={$form.client}
									/>
								</div>
							</Col>
							<Col lg={6}>
								<div>
									<Label
										htmlFor="assignedtoName-field"
										class="form-label"
										>Assigned To</Label
									>
									<Input
										name="assigned"
										type="text"
										id="assignedtoName-field"
										placeholder="Enter Assigned Name"
										on:change={handleChange}
										on:blur={handleChange}
										bind:value={$form.assigned}
									/>
								</div>
							</Col>
							<Col lg={6}>
								<Label
									htmlFor="date-field"
									class="form-label">Create Date</Label
								>
								<Flatpickr
									name="create"
									id="date-field"
									class="form-control"
									placeholder="Select a date"
									bind:value={$form.create}
								/>
							</Col>
							<Col lg={6}>
								<Label
									htmlFor="duedate-field"
									class="form-label">Due Date</Label
								>
								<Flatpickr
									name="due"
									id="date-field"
									class="form-control"
									placeholder="Select a date"
									bind:value={$form.due}
								/>
							</Col>
							<Col lg={6}>
								<Label
									htmlFor="ticket-status"
									class="form-label">Status</Label
								>
								<Input
									name="status"
									type="select"
									class="form-select"
									id="status-field"
									on:change={handleChange}
									on:blur={handleChange}
									bind:value={$form.due}
								>
									<option value="">Status</option>
									<option value="New">New</option>
									<option value="Inprogress"
										>Inprogress</option
									>
									<option value="Closed">Closed</option>
									<option value="Open">Open</option>
								</Input>
							</Col>
							<Col lg={6}>
								<Label
									htmlFor="priority-field"
									class="form-label">Priority</Label
								>
								<Input
									name="priority"
									type="select"
									class="form-select"
									id="priority-field"
									on:change={handleChange}
									on:blur={handleChange}
									bind:value={$form.priority}
								>
									<option value="">Priority</option>
									<option value="High">High</option>
									<option value="Medium">Medium</option>
									<option value="Low">Low</option>
								</Input>
							</Col>
						</Row>
					</div>
					<div class="modal-footer">
						<div class="hstack gap-2 justify-content-end">
							<Button
								on:click={toggle}
								type="button"
								class="btn btn-light"
								data-bs-dismiss="modal">Close</Button
							>
							<Button
								type="submit"
								class="btn btn-success"
								id="add-btn"
								>{!!isEdit
									? "Update"
									: "Add Ticket"}</Button
							>
						</div>
					</div>
				</form>
				</Modal>
				<!--end modal -->
			</CardBody>
			<!--end card-body-->
		</Card>
		<!--end card-->
	</Col>
	<!--end col-->
</Row>
