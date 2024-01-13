<script>
	import {
		Button,
		Label,
		Input,
		Row,
		Col,
	} from "sveltestrap";
	import Flatpickr from "svelte-flatpickr";
	import { createForm } from "svelte-forms-lib";
	import { onMount } from "svelte";
	import * as yup from "yup";
	import { taskdata } from "./stores.js";
	export let show;
	export let onDeleteClick;
	export let onCloseClick;
	export let data;
	import {
		getTaskList,
		addNewTask,
		updateTask,
		deleteTask,
	} from "../../helpers/fakebackend_helper";
	import Modal from "../../Components/Common/Modal.svelte";
	let showTaskModal = false;
    const TaskModalToggle = () => (showTaskModal = !showTaskModal);

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

	let task = [];
	var setDate = defaultdate();
	var isEdit = false;
	const Assigned = [
		{ id: 1, imgId: "anna-adame", img: "avatar-1.jpg", name: "Anna Adame" },
		{ id: 2, imgId: "frank-hook", img: "avatar-3.jpg", name: "Frank Hook" },
		{
			id: 3,
			imgId: "alexis-clarke",
			img: "avatar-6.jpg",
			name: "Alexis Clarke",
		},
		{
			id: 4,
			imgId: "herbert-stokes",
			img: "avatar-2.jpg",
			name: "Herbert Stokes",
		},
		{
			id: 5,
			imgId: "michael-morris",
			img: "avatar-7.jpg",
			name: "Michael Morris",
		},
		{
			id: 6,
			imgId: "nancy-martino",
			img: "avatar-5.jpg",
			name: "Nancy Martino",
		},
		{
			id: 7,
			imgId: "thomas-taylor",
			img: "avatar-8.jpg",
			name: "Thomas Taylor",
		},
		{
			id: 8,
			imgId: "tonya-noble",
			img: "avatar-10.jpg",
			name: "Tonya Noble",
		},
	];

	const { form, handleChange, handleSubmit, handleReset } = createForm({
		initialValues: {
			taskId: (task && task.taskId) || "",
			project: (task && task.project) || "",
			task: (task && task.task) || "",
			creater: (task && task.creater) || "",
			dueDate: (task && task.dueDate) || "",
			status: (task && task.status) || "New",
			priority: (task && task.priority) || "High",
			subItem: (task && task.subItem) || [],
		},
		validationSchema: yup.object().shape({
			taskId: yup.string().required("Please Enter Task Id"),
			project: yup.string().required("Please Enter Project Name"),
			task: yup.string().required("Please Enter Your Task"),
			creater: yup.string().required("Please Enter Creater Name"),
			// dueDate: yup.string().required("Please Enter Due Date"),
			status: yup.string().required("Please Enter Status"),
			priority: yup.string().required("Please Enter Priority"),
			// subItem: yup.array().of.required("Please Enter")
		}),

		onSubmit: (values) => {
			if (isEdit) {
				var updatedTask = {
					_id: task ? task._id : 0,
					taskId: values.taskId,
					project: values.project,
					task: values.task,
					creater: values.creater,
					dueDate: setDate,
					status: values.status,
					priority: values.priority,
					subItem: values.subItem,
				};

				const newres = waitforResponse("update", updatedTask);
				handleReset();
				show = false;
			} else {
				var newTask = {
					_id: (
						Math.floor(Math.random() * (30 - 20)) + 20
					).toString(),
					taskId: values["taskId"],
					project: values["project"],
					task: values["task"],
					creater: values["creater"],
					dueDate: setDate,
					status: values["status"],
					priority: values["priority"],
					subItem: [
						{ id: "1", img: "avatar-3.jpg" },
						{ id: "2", img: "avatar-2.jpg" },
						{ id: "3", img: "avatar-1.jpg" },
					],
				};

				const newres = waitforResponse("create", newTask);
				handleReset();
				show = false;
			}
		},
	});

	async function waitforResponse(action, newTask) {
		if (action == "update") {
			const res = await updateLead(newTask);
			data.map((alltask) =>
				alltask._id.toString() === res._id.toString()
					? { ...alltask, ...res }
					: alltask
			);
		} else {
			const res = await addNewTask(newTask);
			taskdata.update((data) => [...data, res]);
		}

		return true;
	}
</script>

<Modal isOpen={show} className="modal-dialog-centered modal-lg">
    <div class="modal-header p-3 bg-info-subtle">
        <h5 class="modal-title" id="createFileModalLabel">Add Task</h5>
        <button type="button" class="btn-close" on:click={onCloseClick}></button>
    </div>
    <div class="modal-body">
		<Row class="g-3">
			<Col lg={12}>
				<Label for="projectName-field" class="form-label"
					>Project Name</Label
				>
				<Input
					type="text"
					id="projectName-field"
					name="project"
					class="form-control"
					placeholder="Project name"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.project}
					required
				/>
			</Col>
			<!--end col-->
			<Col lg={12}>
				<div>
					<Label for="tasksTitle-field" class="form-label"
						>Title</Label
					>
					<input
						type="text"
						name="task"
						id="tasksTitle-field"
						class="form-control"
						placeholder="Title"
						on:change={handleChange}
						on:blur={handleChange}
						bind:value={$form.name}
						required
					/>
				</div>
			</Col>
			<!--end col-->
			<Col lg={12}>
				<Label for="clientName-field" class="form-label"
					>Client Name</Label
				>
				<Input
					type="text"
					id="clientName-field"
					name="creater"
					class="form-control"
					placeholder="Client name"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.creater}
					required
				/>
			</Col>
			<!--end col-->
			<Col lg={12}>
				<Label class="form-label">Assigned To</Label>
				<div data-simplebar style="height: 95px;">
					<ul class="list-unstyled vstack gap-2 mb-0">
						{#each Assigned as item}
							<li>
								<div
									class="form-check d-flex align-items-center"
								>
									<input
										type="checkbox"
										name="subItem[]"
										class="form-check-input me-3"
										on:change={handleChange}
										on:blur={handleChange}
										bind:value={item.img}
										id={item.imgId}
									/>
									<Label
										class=" d-flex align-items-center"
										for={item.imgId}
									>
										<span class="flex-shrink-0">
											<img
												src="{import.meta.env
													.VITE_PUBLIC_BASE_PATH}/images/users/{item.img}"
												alt=""
												class="avatar-xxs rounded-circle"
											/>
										</span>
										<span class="flex-grow-1 ms-2">
											{item.name}
										</span>
									</Label>
								</div>
							</li>
						{/each}
					</ul>
				</div>
			</Col>
			<!--end col-->
			<div class="col-lg-6">
				<Label for="duedate-field" class="form-label"
					>Due Date</Label
				>
				<Flatpickr
					name="dueDate"
					id="duedate-field"
					class="form-control"
					options={{
						altInput: true,
						altFormat: "d M, Y",
						dateFormat: "d M, Y",
					}}
					placeholder="Select Date"
					bind:value={$form.dueDate}
				/>
			</div>
			<!--end col-->
			<div class="col-lg-6">
				<Label for="ticket-status" class="form-label">Status</Label>
				<Input
					name="status"
					type="select"
					class="form-select"
					id="ticket-field"
					on:change={handleChange}
					on:blur={handleChange}
					bind:value={$form.status}
				>
					<option value="">Status</option>
					<option value="New">New</option>
					<option value="Inprogress">Inprogress</option>
					<option value="Pending">Pending</option>
					<option value="Completed">Completed</option>
				</Input>
			</div>
			<!--end col-->
			<Col lg={12}>
				<Label for="priority-field" class="form-label"
					>Priority</Label
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
			<!--end col-->
		</Row>
    </div>
	<div class="modal-footer">
		<div class="hstack gap-2 justify-content-end">
			<Button color="light" on:click={onCloseClick}>Close</Button>
			<button class="btn btn-success" type="submit" id="add-btn"
				>Add Task</button
			>
		</div>
	</div>
</Modal>