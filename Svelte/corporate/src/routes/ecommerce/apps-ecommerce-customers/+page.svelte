<svelte:head>
	<title>Customers | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import {
		Container,
		Row,
		Col,
		Card,
		CardHeader,
		CardBody,
		Label,
		Input
	} from 'sveltestrap';
	import { onMount } from "svelte";
	import { createForm } from "svelte-forms-lib";
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import { html } from 'gridjs';
	import * as yup from "yup";
	import Grid from 'gridjs-svelte';
	import Flatpickr from 'svelte-flatpickr';
	import Select from 'svelte-select';
	import Modal from "../../../Components/Common/Modal.svelte";
	import {
		getCustomer,
		addNewCustomer,
		updateCustomer
	} from "../../../helpers/fakebackend_helper";

	let isOpen = false;
	const toggle = () => (isOpen = !isOpen);
	let showAddCustomerModal = false;
    const addCutomerToggle = () => (showAddCustomerModal = !showAddCustomerModal);

	const customermocalstatus = [
		{ label: 'Status', value: 'Status' },
		{ label: 'Active', value: 'Active' },
		{ label: 'Block', value: 'Block' }
	];

	const customerstatus = [
		{ label: 'Status', value: 'Status' },
		{ label: 'All', value: 'All' },
		{ label: 'Active', value: 'Active' },
		{ label: 'Block', value: 'Block' }
	];

	const defaultdate = () => {
		let d = new Date(),
			months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
		return ((d.getDate() + ' ' + months[d.getMonth()] + ', ' + d.getFullYear()).toString());
	};

	let data = [];
	var setDate = defaultdate();
	var allcustomer = [];
	var isEdit = false;

	onMount(async () => {
		const res = await getCustomer();
		data = res;
	});

	const { form,errors, handleChange, handleSubmit, handleReset } = createForm({
		initialValues: {
			customer: '',
			email: '',
			phone: '',
			date: '',
			status: '',
		},
		validationSchema: yup.object().shape({
			customer: yup.string().required("Please Enter Customer Name"),
			email: yup.string().required("Please Enter Your Email"),
			phone: yup.string().required("Please Enter Your Phone"),
			status: yup.string().required("Please Enter Your Status")
		}),
		onSubmit: values => {
			/*if (isEdit) {

				var updateLead = {
					_id: allcustomer ? allcustomer._id : 0,
					customer: values.customer,
					email: values.email,
					phone: values.phone,
					date: setDate,
					status: values.status
				};

				const newres = waitforResponse('update', updateLead);
				handleReset();
				open = false;
			} else {
				var newcustomer = {
					_id: (Math.floor(Math.random() * (30 - 20)) + 20).toString(),
					customer: values['customer'],
					email: values['email'],
					phone: values['phone'],
					date: setDate,
					status: values['status'],
				};

				const newres = waitforResponse('create', newcustomer);
				handleReset();
				open = false;
			}*/
		}
	});

	async function waitforResponse(action, newcustomer) {
		if (action == 'update') {
			const res = await updateCustomer(newcustomer);
			data.map(allcustomers => allcustomers._id.toString() === allcustomer._id.toString()
				? { ...allcustomers, ...allcustomer }
				: allcustomers);
		} else {
			const res = await addNewCustomer(newcustomer);
			data = [...data, res]
		}
		return true;
	}

	const columns = [
		{
			name: "#",
			width: '45px',
			formatter: (cell) => html(`<div class="form-check"><input type="checkbox" class="form-check-input"/></div>`),
			sort: false
		},
		'Customer',
		'Email',
		'Phone',
		{
			id:"date",
			name:"Joining Date",
			formatter: (cell) => {
				let date = new Date(cell);
				var month = date.toLocaleString('default', { month: 'short' });
				var day = date.toLocaleString('default', { day: '2-digit' });
				var year = date.toLocaleString('default', { year: 'numeric' });
				var formattedDate = day +' ' + month+', '+ year;
				return formattedDate;
			} 
		},
		{
			id: 'status',
			name: 'Delivery Status',
			formatter: (cell, row) => {
				switch (cell) {
					case "Active":
						return html(`<span class="badge text-uppercase bg-success-subtle text-success">${cell}</span>`);
					case "Block":
						return html(`<span class="badge text-uppercase bg-danger-subtle text-danger">${cell}</span>`);
					default:
						return html(`<span class="badge text-uppercase bg-info-subtle text-info">${cell}</span>`);
				}
			}
		},
		{
			name: 'Action',
			formatter: (cell, row) =>
				html(`<ul class="list-inline hstack gap-2 mb-0">
					<li class="list-inline-item edit" title="Edit">
						<a
						href="#"
						class="text-primary d-inline-block edit-item-btn"
						>
						<i class="ri-pencil-fill fs-16"></i>
						</a>
					</li>
					<li class="list-inline-item" title="Remove">
						<a
						href="#"
						class="text-danger d-inline-block remove-item-btn"
						>
						<i class="ri-delete-bin-5-fill fs-16"></i>
						</a>
					</li>
				</ul>`)
		}
	];
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Customers" pageTitle="Ecommerce" />

		<Row>
			<Col lg={12}>
			<Card id="customerList">
				<CardHeader class="border-bottom-dashed">
					<Row class="g-4 align-items-center">
						<div class="col-sm">
							<div>
								<h5 class="card-title mb-0">Customer List</h5>
							</div>
						</div>
						<div class="col-sm-auto">
							<div class="d-flex flex-wrap align-items-start gap-2">
								<button type="button" class="btn btn-success add-btn" id="create-btn" on:click={addCutomerToggle}>
									<i class="ri-add-line align-bottom me-1" /> Add Customer
								</button>{' '}
								<button type="button" class="btn btn-secondary">
									<i class="ri-file-download-line align-bottom me-1" />{' '}
									Import
								</button>
							</div>
						</div>
					</Row>
				</CardHeader>
				<CardBody class="border-bottom-dashed border-bottom">
					<form>
						<Row class="g-3">
							<Col xl={6}>
							<div class="search-box">
								<input type="text" class="form-control search /"
									placeholder="Search for customer, email, phone, status or something..." />
								<i class="ri-search-line search-icon" />
							</div>
							</Col>

							<Col xl={6}>
							<Row class="g-3">
								<Col sm={4}>
								<div class="">
									<Flatpickr class="form-control" placeholder="Select date" options={{ mode: 'range' ,
										dateFormat: 'd M, Y' , defaultDate: ['01 Jan 2022', '31 Jan 2022' ] }} />
								</div>
								</Col>

								<Col sm={4}>
								<div class="select-single">
									<Select class="form-control" name="choices-single-default" title="idStatus"
										items={customerstatus} />
								</div>
								</Col>

								<Col sm={4}>
								<div>
									<button type="button" class="btn btn-primary w-100">
										{' '}
										<i class="ri-equalizer-fill me-2 align-bottom" />
										Filters
									</button>
								</div>
								</Col>
							</Row>
							</Col>
						</Row>
					</form>
				</CardBody>
				<div class="card-body">
					<div class="table-card gridjs-border-none">
						<Grid {data} {columns} sort={true} class={{th: 'text-muted' }} pagination={{ enabled: true, limit: 8 }} />
					</div>
				</div>
			</Card>
			</Col>
		</Row>
	</Container>
</div>



<Modal isOpen={showAddCustomerModal} className="modal-dialog-centered">
    <div class="modal-header p-3 bg-light">
        <h5 class="modal-title" id="createFileModalLabel">Add Customer</h5>
        <button type="button" class="btn-close" on:click={addCutomerToggle} ></button>
    </div>
	<form class="tablelist-form" on:submit|preventDefault={handleSubmit}>
    <div class="modal-body">
			<input type="hidden" id="id-field" />

			<div class="mb-3" id="modal-id" style="display: none">
				<Label for="id-field1" class="form-label">ID</Label>
				<!-- <Input type="text" id="id-field1" class="form-control" name="id" on:blur={handleChange} on:change={handleChange} bind:value={$form.id} placeholder="ID" readOnly /> -->
			</div>

			<div class="mb-3">
				<Label for="customername-field" class="form-label">Customer Name</Label>
				<Input type="text" id="customername-field" name="customer" on:blur={handleChange}
					on:change={handleChange} bind:value={$form.customer} class="form-control"
					placeholder="Enter Name" />
					{#if $errors.customer}
						<small class="text-danger">{$errors.customer}</small>
					{/if}
			</div>

			<div class="mb-3">
				<Label for="email-field" class="form-label">Email</Label>
				<Input type="email" id="email-field" name="email" class="form-control" on:blur={handleChange}
					on:change={handleChange} bind:value={$form.email} placeholder="Enter Email" />
					{#if $errors.email}
						<small class="text-danger">{$errors.email}</small>
					{/if}
			</div>

			<div class="mb-3">
				<Label for="phone-field" class="form-label">Phone</Label>
				<Input type="text" id="phone-field" name="phone" class="form-control" on:blur={handleChange}
					on:change={handleChange} bind:value={$form.phone} placeholder="Enter Phone no." />
					{#if $errors.phone}
						<small class="text-danger">{$errors.phone}</small>
					{/if}
			</div>

			<div class="mb-3">
				<Label for="date-field" class="form-label">Joining Date</Label>
				<Flatpickr class="form-control" id="date-field" placeholder="Select Joining Date" options={{ altInput:
					true, altFormat: 'F j, Y' , dateFormat: 'd.m.y' }} on:blur={handleChange} on:change={handleChange}
					bind:value={$form.joindate} />
					{#if $errors.joindate}
						<small class="text-danger">{$errors.joindate}</small>
					{/if}
			</div>

			<div>
				<Label for="status-field" class="form-label">Status</Label>

				<Input name="status" type="select" class="form-select" id="status-field" on:blur={handleChange}
					on:change={handleChange} bind:value={$form.status}>
					{#each customermocalstatus as item}
					<option value={item.value}>{item.label}</option>
					{/each}
				</Input>
				{#if $errors.status}
						<small class="text-danger">{$errors.status}</small>
					{/if}
			</div>
			
    </div>
	<div class="modal-footer">
		<div class="hstack gap-2 justify-content-end">
			<button type="button" class="btn btn-light" on:click={addCutomerToggle}>
				Close
			</button>
			<button type="submit" class="btn btn-success" id="add-btn">
				Add Customer
			</button>
		</div>
	</div>
</form>
</Modal>