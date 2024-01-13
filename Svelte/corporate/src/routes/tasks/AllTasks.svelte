<script>
	import {
		Col,
		Row,
		Input,
		Button,
		Card,
		CardHeader,
		CardBody,
	} from "sveltestrap";
	import { onMount } from "svelte";
	import Flatpickr from "svelte-flatpickr";
	import Select from "svelte-select";
	import * as yup from "yup";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";
	import CreateTaskModal from "./createTaskModal.svelte";
	import { taskdata } from "./stores.js";
	import { getTaskList } from "../../helpers/fakebackend_helper";

	let isOpen = false;
	let createModal = false;
	const toggle = () => (isOpen = !isOpen);
	const setCloseModal = (status) => {
		createModal = status;
	};
	let data = [];

	onMount(async () => {
		const res = await getTaskList();
		$taskdata = res;
		data = $taskdata;
	});

	if ($taskdata != []) {
		taskdata.subscribe((task) => {
			data = task;
		});
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
			id: "taskId",
			name: "Order ID",
			formatter: (cell) =>
				html(
					`<a href="/tasks/apps-tasks-details" class="fw-medium link-primary">${cell}</a>`
				),
		},
		{
			id: "project",
			name: "Project",
			formatter: (cell) =>
				html(
					`<a href="/projects/apps-projects-overview" class="fw-medium link-primary">${cell}</a>`
				),
		},
		{
			id: "task",
			hidden: true,
		},
		{
			name: "Tasks",
			formatter: (cell, row) =>
				html(`<div class="d-flex" id="${cell}">
					<div class="flex-grow-1 tasks_name">${row.cell(3).data}</div>
						<div class="flex-shrink-0 ms-4">
							<ul class="list-inline tasks-list-menu mb-0">
								<li class="list-inline-item">
									<a href="/tasks/apps-tasks-details">
										<i class="ri-eye-fill align-bottom me-2 text-muted"></i>
									</a>
								</li>
								<li class="list-inline-item">
									<a href="/#">
										<i class="ri-pencil-fill align-bottom me-2 text-muted"></i>
									</a>
								</li>
								<li class="list-inline-item">
									<a href="/#" class="remove-item-btn">
										<i class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>
									</a>
								</li>
							</ul>
						</div>
				</div>`),
		},
		{
			name: "Created By",
			id: "creater",
		},
		{
			id: "subItem",
			hidden: true,
		},
		{
			name: "Assigned To",
			formatter: (cell, row) => {
				var items = row.cell(6).data;
				var demo = `<div class="avatar-group">`;
				items.forEach(function (item) {
					demo +=
						'<a href={null} class="avatar-group-item" id="avatar' +
						item.id +
						'">';
					demo +=
						"<img src=" +
						import.meta.env.VITE_PUBLIC_BASE_PATH +
						"/images/users/" +
						item.img +
						' alt="" class="rounded-circle avatar-xxs" />';
					demo += "</a>";
				});
				return html(demo);
			},
		},
		{
			name: "Due Date",
			id: "dueDate",
		},
		{
			name: "Status",
			id: "status",
			formatter: (cell) => {
				if (cell === "Inprogress") {
					return html(
						`<span class='badge bg-secondary-subtle text-secondary text-uppercase'>${cell}</span>`
					);
				} else if (cell === "New") {
					return html(
						`<span class='badge bg-info-subtle text-info text-uppercase'>${cell}</span>`
					);
				} else if (cell === "Completed") {
					return html(
						`<span class='badge bg-success-subtle text-success text-uppercase'>${cell}</span>`
					);
				} else if (cell === "Pending") {
					return html(
						`<span class='badge bg-warning-subtle text-warning text-uppercase'>${cell}</span>`
					);
				} else {
					return null;
				}
			},
		},
		{
			name: "Priority",
			id: "priority",
			formatter: (cell, row) => {
				if (cell === "Medium") {
					return html(
						`<span class="badge bg-warning text-uppercase">${cell}</span>`
					);
				} else if (cell === "High") {
					return html(
						`<span class="badge bg-danger text-uppercase">${cell}</span>`
					);
				} else if (cell === "Low") {
					return html(
						`<span class="badge bg-success text-uppercase">${cell}</span>`
					);
				} else {
					return null;
				}
			},
		},
	];

	const statusOption = [
		{
			value: "Status",
			label: "Status",
		},
		{
			value: "all",
			label: "All",
		},
		{
			value: "New",
			label: "New",
		},
		{
			value: "Pending",
			label: "Pending",
		},
		{
			value: "Inprogress",
			label: "Inprogress",
		},
		{
			value: "Completed",
			label: "Completed",
		},
	];
</script>

<CreateTaskModal
	show={createModal}
	onDeleteClick={toggle}
	onCloseClick={() => setCloseModal(false)}
	data={$taskdata}
/>

<Row>
	<Col lg={12}>
		<Card id="tasksList">
			<CardHeader class="border-0">
				<div class="d-flex align-items-center">
					<h5 class="card-title mb-0 flex-grow-1">All Tasks</h5>
					<div class="flex-shrink-0">
						<div class="d-flex flex-wrap gap-2">
							<Button
								color="secondary"
								class="add-btn"
								on:click={() => setCloseModal(true)}
								><i class="ri-add-line align-bottom me-1" /> Create
								Task</Button
							>
							<Button color="" class="btn btn-soft-danger"
								><i class="ri-delete-bin-2-line" /></Button
							>
						</div>
					</div>
				</div>
			</CardHeader>
			<CardBody class="border border-dashed border-end-0 border-start-0">
				<form>
					<Row class="g-3">
						<Col sm={12} xxl={5}>
							<div class="search-box">
								<Input
									type="text"
									class="form-control search bg-light border-light"
									placeholder="Search for tasks or something..."
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
							<Select
								class="form-control"
								id="idStatus"
								items={statusOption}
							/>
						</Col>
						<!--end col-->
						<Col xxl={1} sm={4}>
							<Button color="primary" class="w-100">
								<i
									class="ri-equalizer-fill me-1 align-bottom"
								/>
								Filters
							</Button>
						</Col>
						<!--end col-->
					</Row>
					<!--end row-->
				</form>
			</CardBody>
			<!--end card-body-->
			<CardBody>
				<div class="table-responsive table-card gridjs-border-none">
					{#if (data.length || []) > 0}
						<Grid
							{data}
							{columns}
							pagination={{ enabled: true, limit: 10 }}
						/>
					{:else}
						<!--end table-->
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
			</CardBody>
			<!--end card-body-->
		</Card>
		<!--end card-->
	</Col>
	<!--end col-->
</Row>
