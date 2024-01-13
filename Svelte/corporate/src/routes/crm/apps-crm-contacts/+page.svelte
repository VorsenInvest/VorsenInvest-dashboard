<script>
	import {
		Col,
		Container,
		Row,
		Card,
		CardHeader,
		CardBody,
		Dropdown,
		DropdownToggle,
		DropdownMenu,
		DropdownItem,
		Label,
		Input,
		Form,
		Table,
		Button,
	} from "sveltestrap";

	import Select from "svelte-select";
	import DeleteModal from "../../../Components/Common/CDeleteModal.svelte";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import Link from "svelte-link";
	import dayjs from "dayjs";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";
	import { createForm } from "svelte-forms-lib";
	import * as yup from "yup";
	import { onMount } from "svelte";
	import {
		getContacts,
		addNewContact,
		updateContact,
	} from "../../../helpers/fakebackend_helper";
	import Modal from "../../../Components/Common/Modal.svelte";

	import avatar10 from "../../../assets/images/users/avatar-10.jpg";
	let deleteModal = false;

	let open = false;
	const toggle = () => (open = !open);

	let sortBy = "Name";

	const sortbyname = [
		{ label: "Owner", value: "Owner" },
		{ label: "Company", value: "Company" },
		{ label: "Location", value: "Location" },
	];

	const tags = [
		{ label: "Exiting", value: "Exiting" },
		{ label: "Lead", value: "Lead" },
		{ label: "Long-term", value: "Long-term" },
		{ label: "Partner", value: "Partner" },
	];

	let tag = [];
	let assignTag = [];

	const handlestag = (tags) => {
		tag = tags;
		const assigned = tags.map((item) => item.value);
		assignTag = assigned;
	};

	const setDeleteModal = (status) => {
		deleteModal = status;
	};

	const handleValidTime = (time) => {
		const time1 = new Date(time);
		const getHour = time1.getUTCHours();
		const getMin = time1.getUTCMinutes();
		const getTime = `${getHour}:${getMin}`;
		var meridiem = "";
		if (getHour >= 12) {
			meridiem = "PM";
		} else {
			meridiem = "AM";
		}
		const updateTime = getTime + " " + meridiem;
		return updateTime;
	};

	function handleValidDate(todaydate) {
		const datwe = dayjs(todaydate).format("DD MMM YYYY");
		return datwe;
	}

	let data = [];

	onMount(async () => {
		const res = await getContacts();
		data = res;
	});

	const columns = [
		{
			name: "#",
			width: "40px",
			// sort:false,
			formatter: (cell) =>
				html(
					`<div class="form-check"><input type="checkbox" class="form-check-input"/></div>`
				),
		},
		{
			id: "image_src",
			hidden: true,
		},
		{
			id: "name",
			name: "Name",
			// sort:true,
			formatter: (cell, row) => {
				if (row.cells[1].data) {
					return html(`<div class="d-flex align-items-center">
					<div class="flex-shrink-0"><img src="${
						import.meta.env.VITE_PUBLIC_BASE_PATH
					}/images/users/${
						row.cells[1].data
					}" alt="" class="avatar-xs rounded-circle"></div>
					<div class="flex-grow-1 ms-2 name">${cell}</div>
				</div>`);
				} else {
					return html(`<div class="d-flex align-items-center">
					<div class="flex-shrink-0"><div class="flex-shrink-0 avatar-xs me-2">
							<div class="avatar-title bg-success-subtle text-success rounded-circle fs-13">
								${cell.charAt(0)}
							</div>
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
			id: "company",
			name: "Company",
			// sort:true,
		},
		{
			id: "email",
			name: "Email id",
			// sort:true,
		},
		{
			id: "phone",
			name: "Phone No",
			// sort:true,
		},
		{
			id: "lead_score",
			name: "Lead Score",
			// sort:true,
		},
		{
			id: "last_contacted",
			name: "Last Contacted",
			// sort:true,
			formatter: (cell, row) =>
				html(`${handleValidDate(cell)},
            <small class="text-muted"> ${handleValidTime(cell)}</small>`),
		},

		{
			name: "Action", 
			sort: false,
			formatter: (cell, row) =>
				html(`<ul class="list-inline hstack gap-2 mb-0">
              <li class="list-inline-item">
                <a
                  href="/#"
                  class="text-primary d-inline-block"
                >
                  <i class="ri-eye-fill fs-16"></i>
                </a>
              </li>
              <li class="list-inline-item edit">
                <a
                  href="/#"
                  class="text-primary d-inline-block edit-item-btn"
                >
                  <i class="ri-pencil-fill fs-16"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a
                  href="/#"
                  class="text-danger d-inline-block remove-item-btn"
                >
                  <i class="ri-delete-bin-5-fill fs-16"></i>
                </a>
              </li>
            </ul>`),
		}
	];

	let contact = [];
	var isEdit = false;
	let ticket = [];
	// Date & Time Format

	const dateFormat = () => {
		var d = new Date(),
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
			d.getDate() + " " + months[d.getMonth()] + ", " + d.getFullYear()
		);
	};

	const { form, handleChange, handleSubmit, handleReset } = createForm({
		initialValues: {
			name: (contact && contact.name) || "",
			company: (contact && contact.company) || "",
			designation: (contact && contact.designation) || "",
			email: (contact && contact.email) || "",
			phone: (contact && contact.phone) || "",
			// lead_score: (contact && contact.lead_score) || '',
			// tags: (contact && contact.tags) || [],
		},
		validationSchema: yup.object().shape({
			name: yup.string().required("Please Enter Name"),
			company: yup.string().required("Please Enter Company"),
			designation: yup.string().required("Please Enter Designation"),
			email: yup.string().required("Please Enter Email"),
			phone: yup.string().required("Please Enter Phone"),
			// lead_score: yup.string().required("Please Enter lead_score"),
		}),

		onSubmit: (values) => {
			if (isEdit) {
				var updatedTask = {
					_id: contact ? contact._id : 0,
					name: values.name,
					company: values.company,
					designation: values.designation,
					email: values.email,
					phone: values.phone,
					lead_score: values.lead_score,
					last_contacted: dateFormat(),
					// tags: assignTag,
				};

				const newres = waitforResponse("update", updatedTask);
				handleReset();
			} else {
				var newcontact = {
					_id: (
						Math.floor(Math.random() * (30 - 20)) + 20
					).toString(),
					name: values["name"],
					company: values["company"],
					designation: values["designation"],
					email: values["email"],
					phone: values["phone"],
					lead_score: values["lead_score"],
					last_contacted: dateFormat(),
				};

				const newres = waitforResponse("create", newcontact);
				handleReset();
			}
		},
	});

	async function waitforResponse(action, newcontact) {
		if (action == "update") {
			const res = await updateContact(newcontact);
			data.map((allcontacts) =>
				allcontacts._id.toString() === res._id.toString()
					? { ...allcontacts, ...res }
					: allcontacts
			);
		} else {
			const res = await addNewContact(newcontact);
			data = [...data, res];
		}
		return true;
	}
</script>

<svelte:head>
	<title>Contacts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Contacts" pageTitle="CRM" />

		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader>
						<div class="d-flex align-items-center flex-wrap gap-2">
							<div class="flex-grow-1">
								<Button
									color=""
									class="btn btn-primary add-btn"
									on:click={toggle}
								>
									<i class="ri-add-fill me-1 align-bottom" /> Add
									Contacts
								</Button>
							</div>
							<div class="flex-shrink-0">
								<div class="hstack text-nowrap gap-2">
									<Button color="secondary">
										<i
											class="ri-filter-2-line me-1 align-bottom"
										/>{" "}
										Filters
									</Button>
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
			<Col xxl={9}>
				<Card id="contactList">
					<CardHeader>
						<Row class="g-3">
							<Col md={4}>
								<div class="search-box">
									<Input
										type="text"
										class="form-control search"
										placeholder="Search for contact..."
									/>
									<i class="ri-search-line search-icon" />
								</div>
							</Col>
							<div class="col-md-auto ms-auto">
								<div class="d-flex align-items-center gap-2">
									<span class="text-muted">Sort by: </span>
									<div class="select-single">
										<Select
											value={sortBy}
											items={sortbyname}
											id="choices-single-default"
										/>
									</div>
								</div>
							</div>
						</Row>
					</CardHeader>
					<CardBody>
						<div>
							{#if (data.length || []) > 0}
								<div class="table-card gridjs-border-none">
									<Grid
										{data}
										{columns}
										class={{ th: "text-muted" }}
										pagination={{
											enabled: true,
											limit: 8,
										}}
									/>
								</div>
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
											contacts We did not find any
											contacts for you search.
										</p>
									</div>
								</div>
							{/if}
						</div>

						<Modal isOpen={open}  className="modal-dialog-centered">
							<div class="modal-header p-3 bg-info-subtle">
								<h5 class="modal-title" id="createFileModalLabel">Add Contact</h5>
								<button type="button" class="btn-close" on:click={toggle} ></button>
							</div>
							<div class="modal-body">
								<Input type="hidden" id="id-field" />
									<Row class="g-3">
										<Col lg={12}>
											<div>
												<Label
													for="name-field"
													class="form-label"
													>Name</Label
												>
												<Input
													type="text"
													id="customername-field"
													class="form-control"
													name="name"
													placeholder="Enter name"
													on:change={handleChange}
													on:blur={handleChange}
													bind:value={$form.name}
												/>
											</div>
										</Col>
										<Col lg={12}>
											<div>
												<Label
													for="company_name-field"
													class="form-label"
													>Company Name</Label
												>
												<Input
													type="text"
													id="company_name-field"
													class="form-control"
													name="company"
													placeholder="Enter company name"
													on:change={handleChange}
													on:blur={handleChange}
													bind:value={$form.company}
												/>
											</div>
										</Col>
										<Col lg={12}>
											<div>
												<Label
													for="designation-field"
													class="form-label"
												>
													Designation
												</Label>

												<Input
													name="designation"
													id="designation-field"
													class="form-control"
													placeholder="Enter Designation"
													type="text"
													on:change={handleChange}
													on:blur={handleChange}
													bind:value={$form.designation}
												/>
											</div>
										</Col>
										<Col lg={12}>
											<div>
												<Label
													for="email_id-field"
													class="form-label"
													>Email ID</Label
												>
												<Input
													type="text"
													id="email_id-field"
													name="email"
													class="form-control"
													placeholder="Enter email"
													on:change={handleChange}
													on:blur={handleChange}
													bind:value={$form.email}
												/>
											</div>
										</Col>
										<Col lg={6}>
											<div>
												<Label
													for="phone-field"
													class="form-label"
													>Phone</Label
												>
												<Input
													type="text"
													name="phone"
													id="phone-field"
													class="form-control"
													placeholder="Enter phone no"
													on:change={handleChange}
													on:blur={handleChange}
													bind:value={$form.phone}
												/>
											</div>
										</Col>
										<Col lg={6}>
											<div>
												<Label
													for="lead_score-field"
													class="form-label"
													>Lead Score</Label
												>
												<Input
													type="text"
													name="lead_score"
													id="lead_score-field"
													class="form-control"
													placeholder="Enter value"
													on:change={handleChange}
													on:blur={handleChange}
													bind:value={$form.lead_score}
												/>
											</div>
										</Col>
										<Col lg={12}>
											<div>
												<Label
													for="taginput-choices"
													class="form-label font-size-13 text-muted"
												>
													Tags
												</Label>
												<Select
													isMulti
													on:change={(e) => {
														handlestag(e);
													}}
													class="mb-0"
													items={tags}
													id="taginput-choices"
												/>
											</div>
										</Col>
									</Row>
							</div>
							<div class="modal-footer">
								<div
										class="hstack gap-2 justify-content-end"
									>
										<Button color="light" on:click={toggle}
											>Close</Button
										>
										<Button
											type="submit"
											class="btn btn-success"
											id="add-btn"
										>
											Add Contact
										</Button>
										<Button
											color="success"
											id="edit-btn"
											class="d-none"
											on:click={toggle}>Update</Button
										>
									</div>
							</div>
						</Modal>

						<DeleteModal
							show={deleteModal}
							onCloseClick={() => setDeleteModal(false)}
						/>
					</CardBody>
				</Card>
			</Col>
			<Col xxl={3}>
				<Card>
					<CardBody class="text-center">
						<div class="position-relative d-inline-block">
							<img
								src={avatar10}
								alt=""
								class="avatar-lg rounded-circle img-thumbnail"
							/>
							<span
								class="contact-active position-absolute rounded-circle bg-success"
							>
								<span class="visually-hidden" />
							</span>
						</div>
						<h5 class="mt-4 mb-1">Tonya Noble</h5>
						<p class="text-muted">Nesta Technologies</p>

						<ul class="list-inline mb-0">
							<li class="list-inline-item avatar-xs">
								<Link
									href={null}
									class="avatar-title bg-success-subtle text-success fs-15 rounded"
								>
									<i class="ri-phone-line" />
								</Link>
							</li>
							<li class="list-inline-item avatar-xs">
								<Link
									href={null}
									class="avatar-title bg-danger-subtle text-danger fs-15 rounded"
								>
									<i class="ri-mail-line" />
								</Link>
							</li>
							<li class="list-inline-item avatar-xs">
								<Link
									href={null}
									class="avatar-title bg-warning-subtle text-warning fs-15 rounded"
								>
									<i class="ri-question-answer-line" />
								</Link>
							</li>
						</ul>
					</CardBody>
					<CardBody>
						<h6 class="text-muted text-uppercase fw-semibold mb-3">
							Personal Information
						</h6>
						<p class="text-muted mb-4">
							Hello, I'm Tonya Noble, The most effective objective
							is one that is tailored to the job you are applying
							for. It states what kind of career you are seeking,
							and what skills and experiences.
						</p>
						<div class="table-responsive table-card">
							<Table class="table table-borderless mb-0">
								<tbody>
									<tr>
										<td class="fw-medium"> Designation </td>
										<td>Lead Designer / Developer</td>
									</tr>
									<tr>
										<td class="fw-medium"> Email ID </td>
										<td>tonyanoble@velzon.com</td>
									</tr>
									<tr>
										<td class="fw-medium"> Phone No </td>
										<td>414-453-5725</td>
									</tr>
									<tr>
										<td class="fw-medium"> Lead Score </td>
										<td>154</td>
									</tr>
									<tr>
										<td class="fw-medium"> Tags </td>
										<td>
											<span
												class="badge bg-primary-subtle text-primary"
											>
												Lead
											</span>
											<span
												class="badge bg-primary-subtle text-primary"
											>
												Partner
											</span>
										</td>
									</tr>
									<tr>
										<td class="fw-medium">
											Last Contacted
										</td>
										<td>
											15 Dec, 2021{" "}
											<small class="text-muted"
												>08:58AM</small
											>
										</td>
									</tr>
								</tbody>
							</Table>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
