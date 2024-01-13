<script>
	import {
		Container,
		Row,
		Col,
		Card,
		CardBody,
		Input,
		ModalBody,
		Label,
		ModalHeader,
		Nav,
		NavItem,
		NavLink,
	} from "sveltestrap";
	import { onMount } from "svelte";
	import * as yup from "yup";
	import Flatpickr from "svelte-flatpickr";
	import dayjs from "dayjs";
	import Select from "svelte-select";
	import { createForm } from "svelte-forms-lib";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import Modal from "../../../Components/Common/Modal.svelte";
	import {
		getOrders,
		addNewOrder,
		updateOrder,
	} from "../../../helpers/fakebackend_helper";

	let showModal = false;
	const AddOrderToggle = () => (showModal = !showModal);

	let orderdata = [];
	let data = [];

	onMount(async () => {
		const res = await getOrders();
		orderdata = res;
		data = orderdata;
	});

	const options = [
		{ value: "all", label: "Status" },
		// { value: 'all', label: 'all' },
		{ value: "Pending", label: "Pending" },
		{ value: "Inprogress", label: "Inprogress" },
		{ value: "Cancelled", label: "Cancelled" },
		{ value: "Pickups", label: "Pickups" },
		{ value: "Returns", label: "Returns" },
		{ value: "Delivered", label: "Delivered" },
	];

	const optionpayments = [
		{ value: "all", label: "Payment" },
		// { value: 'all', label: 'all' },
		{ value: "Mastercard", label: "Mastercard" },
		{ value: "Paypal", label: "Paypal" },
		{ value: "Visa", label: "Visa" },
		{ value: "COD", label: "COD" },
	];

	let open = false;

	function handleValidDate(todaydate) {
		const datwe = dayjs(todaydate).format("DD MMM YYYY");
		return datwe;
	}

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

	const toggle = () => (open = !open);
	let activeTab = 1;
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
			name: "Order Id",
			id: "orderId",
			formatter: (cell) =>
				html(
					`<a href="/ecommerce/apps-ecommerce-order-details"><a>${cell}</a></a>`
				),
		},
		"Customer",
		{
			id: "product",
			name: "Product",
		},
		{
			name: "Order Date",
			formatter: (cell, row) =>
				html(`${handleValidDate(cell)},
            <small class="text-muted"> ${handleValidTime(cell)}</small>`),
		},
		"Amount",
		{
			id: "payment",
			name: "Payment Method",
		},
		{
			id: "status",
			hidden: true,
		},
		{
			id: "status",
			name: "Delivery Status",
			formatter: (cell, row) => {
				switch (cell) {
					case "Pending":
						return html(
							`<span class="badge text-uppercase bg-warning-subtle text-warning"> ${row.cells[7].data} </span>`
						);
					case "Cancelled":
						return html(
							`<span class="badge text-uppercase bg-danger-subtle text-danger"> ${row.cells[7].data} </span>`
						);
					case "Inprogress":
						return html(
							`<span class="badge text-uppercase bg-secondary-subtle text-secondary"> ${row.cells[7].data} </span>`
						);
					case "Pickups":
						return html(
							`<span class="badge text-uppercase bg-info-subtle text-info"> ${row.cells[7].data} </span>`
						);
					case "Returns":
						return html(
							`<span class="badge text-uppercase bg-primary-subtle text-primary"> ${row.cells[7].data} </span>`
						);
					case "Delivered":
						return html(
							`<span class="badge text-uppercase bg-success-subtle text-success"> ${row.cells[7].data} </span>`
						);
					default:
						return html(
							`<span class="badge text-uppercase bg-warning-subtle text-warning"> ${row.cells[7].data} </span>`
						);
				}
			},
		},
		{
			name: "Action",
			formatter: (cell, row) =>
				html(`<ul class="list-inline hstack gap-2 mb-0">
              <li class="list-inline-item">
                <a
                  href="/ecommerce/apps-ecommerce-order-details"
                  class="text-primary d-inline-block"
                >
                  <i class="ri-eye-fill fs-16"></i>
                </a>
              </li>
              <li class="list-inline-item edit">
                <a
                  href="#"
                  class="text-primary d-inline-block edit-item-btn"
                >
                  <i class="ri-pencil-fill fs-16"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a
                  href="#"
                  class="text-danger d-inline-block remove-item-btn"
                >
                  <i class="ri-delete-bin-5-fill fs-16"></i>
                </a>
              </li>
            </ul>`),
		},
	];

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

	var order = [];
	var isEdit = false;
	var setDate = defaultdate();

	const toggleTab = (tab, type) => {
		if (activeTab !== tab) {
			let filteredOrder = orderdata;
			if (type !== "all") {
				filteredOrder = orderdata.filter(
					(product) => product.status === type
				);
			}
			data = filteredOrder;
		}
	};

	const { form, errors, handleChange, handleSubmit, handleReset } =
		createForm({
			initialValues: {
				orderId: "",
				customer: "",
				product: "",
				orderDate: "",
				amount: "",
				payment: "",
				status: "",
			},
			validationSchema: yup.object().shape({
				orderId: yup.string().required("Please Enter Valid orderId"),
				customer: yup.string().required("Please Enter customer"),
				product: yup.string().required("Please Enter product"),
				orderDate: yup.string().required("Please Enter orderDate"),
				amount: yup.string().required("Please Enter amount"),
				payment: yup.string().required("Please Enter payment"),
				status: yup.string().required("Please Enter status"),
			}),
			onSubmit: (values) => {
			},
		});

	async function waitforResponse(action, newOrder) {
		if (action == "update") {
			const res = await updateOrder(newOrder);
			data.map((allorders) =>
				allorders._id.toString() === res._id.toString()
					? { ...allorders, ...res }
					: allorders
			);
			open = false;
		} else {
			const res = await addNewOrder(newOrder);
			data = [...data, res];
			open = false;
		}
		return true;
	}

	let search;
	let status;
	let paymenttype;
	const SearchData = () => {
		// if (status != null && paymenttype != null) {
		const FilterData = orderdata.filter((order) => {
			if (status == null) {
				status = "all";
			}
			if (paymenttype == null) {
				paymenttype = "all";
			}
			if (status != "all" && paymenttype != "all") {
				return order.status == status && order.payment == paymenttype;
			} else if (status != "all") {
				return order.status == status;
			} else if (paymenttype != "all") {

				return order.payment == paymenttype;
			} else {
				return orderdata;
			}
		});
		data = FilterData;
		// }
	};
</script>

<svelte:head>
	<title>Orders | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Orders" pageTitle="Ecommerce" />

		<Row>
			<Col lg={12}>
				<Card id="orderList">
					<div class="card-header border-0">
						<div class="row align-items-center gy-3">
							<div class="col-sm">
								<h5 class="card-title mb-0">Order History</h5>
							</div>
							<div class="col-sm-auto">
								<div class="d-flex gap-1 flex-wrap">
									<button
										type="button"
										class="btn btn-primary add-btn"
										on:click={AddOrderToggle}
										id="create-btn"
										><i
											class="ri-add-line align-bottom me-1"
										/> Create Order</button
									>
									<button type="button" class="btn btn-info"
										><i
											class="ri-file-download-line align-bottom me-1"
										/> Import</button
									>
									<button
										class="btn btn-soft-danger"
										id="remove-actions"
										onClick="deleteMultiple()"
										><i
											class="ri-delete-bin-2-line"
										/></button
									>
								</div>
							</div>
						</div>
					</div>
					<CardBody
						class="border border-dashed border-end-0 border-start-0"
					>
						<form>
							<Row class="g-3">
								<Col sm={6} class="col-xxl-5">
									<div class="search-box">
										<Input
											type="text"
											class="form-control search"
											placeholder="Search for order ID, customer, order status or something..."
											bind:value={search}
										/>
										<i class="ri-search-line search-icon" />
									</div>
								</Col>
								<!--end col-->
								<Col sm={6} class="col-xxl-2">
									<div>
										<Flatpickr class="form-control" placeholder="Select date" options={{ mode: 'range' ,
									dateFormat: 'd M, Y' , defaultDate: ['01 Jan 2022', '31 Jan 2022' ] }} />
									</div>
								</Col>
								<!--end col-->
								<Col sm={4} class="col-xxl-2">
									<div class="select-single">
										<Select
											class="form-control"
											placeholder="Choose ..."
											title="idStatus"
											items={options}
											name="status"
											bind:justValue={status}
										/>
									</div>
								</Col>
								<!--end col-->
								<Col sm={4} class="col-xxl-2">
									<div class="select-single">
										<Select
											class="form-control"
											placeholder="Choose ..."
											title="idStatus"
											items={optionpayments}
											bind:justValue={paymenttype}
										/>
									</div>
								</Col>
								<!--end col-->
								<Col sm={4} class="col-xxl-1">
									<div>
										<button
											type="button"
											class="btn btn-primary w-100"
											on:click={SearchData}
										>
											<i
												class="ri-equalizer-fill me-1 align-bottom"
											/>
											Filters
										</button>
									</div>
								</Col>
								<!--end col-->
							</Row>
							<!--end row-->
						</form>
					</CardBody>
					<CardBody class="pt-0">
						<div>
							<Nav
								class="nav-tabs nav-tabs-custom nav-primary mb-3"
								role="tablist"
							>
								<NavItem>
									<NavLink
										class="All py-3"
										on:click={() => {
											activeTab = 1;
											toggleTab("1", "all");
										}}
										active={activeTab == 1}
										data-bs-toggle="tab"
										id="All"
										href="#home1"
										role="tab"
										aria-selected="true"
									>
										<i
											class="ri-store-2-fill me-1 align-bottom"
										/> All Orders
									</NavLink>
								</NavItem>
								<NavItem>
									<NavLink
										class="py-3 Delivered"
										on:click={() => {
											activeTab = 2;
											toggleTab("2", "Delivered");
										}}
										active={activeTab == 2}
										data-bs-toggle="tab"
										id="Delivered"
										href="#delivered"
										role="tab"
										aria-selected="false"
									>
										<i
											class="ri-checkbox-circle-line me-1 align-bottom"
										/> Delivered
									</NavLink>
								</NavItem>
								<NavItem>
									<NavLink
										class="py-3 Pickups"
										on:click={() => {
											activeTab = 3;
											toggleTab("3", "Pickups");
										}}
										active={activeTab == 3}
										data-bs-toggle="tab"
										id="Pickups"
										href="#pickups"
										role="tab"
										aria-selected="false"
									>
										<i
											class="ri-truck-line me-1 align-bottom"
										/>
										Pickups
										<span
											class="badge bg-danger align-middle ms-1"
											>2</span
										>
									</NavLink>
								</NavItem>
								<NavItem>
									<NavLink
										class="py-3 Returns"
										on:click={() => {
											activeTab = 4;
											toggleTab("4", "Returns");
										}}
										active={activeTab == 4}
										data-bs-toggle="tab"
										id="Returns"
										href="#returns"
										role="tab"
										aria-selected="false"
									>
										<i
											class="ri-arrow-left-right-fill me-1 align-bottom"
										/> Returns
									</NavLink>
								</NavItem>
								<NavItem>
									<NavLink
										class="py-3 Cancelled"
										data-bs-toggle="tab"
										on:click={() => {
											activeTab = 5;
											toggleTab("5", "Cancelled");
										}}
										active={activeTab == 5}
										id="Cancelled"
										href="#cancelled"
										role="tab"
										aria-selected="false"
									>
										<i
											class="ri-close-circle-line me-1 align-bottom"
										/> Cancelled
									</NavLink>
								</NavItem>
							</Nav>

							<div
								class="table-responsive table-card gridjs-border-none"
							>
								{#if (data.length || []) > 0}
									<Grid
										{data}
										{columns}
										sort={true}
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
												colors="primary:#405189,secondary:#0ab39c"
												style="width:75px;height:75px"
											/>
											<h5 class="mt-2">
												Sorry! No Result Found
											</h5>
											<p class="text-muted">
												We've searched more than 150+
												Orders We did not find any
												orders for you search.
											</p>
										</div>
									</div>
								{/if}
							</div>
						</div>

						<!-- <Modal id="showModal" isOpen={open} {toggle} fade={true}>
						<ModalHeader {toggle} class="bg-light p-3">
							<h5 class="modal-title" id="exampleModalLabel">Add Order</h5>
						</ModalHeader>
						<form on:submit|preventDefault={handleSubmit}>
							<ModalBody>
								<Input type="hidden" id="id-field" />

								<div class="mb-3" id="modal-id">
									<Label for="orderId" class="form-label">Order Id</Label>
									<Input type="text" id="orderId" on:change={handleChange} on:blur={handleChange}
										bind:value={$form.orderId} required name="orderId" class="form-control"
										placeholder="ID" />
								</div>

								<div class="mb-3">
									<Label for="customername-field" class="form-label">Customer Name</Label>
									<Input type="text" id="customername-field" name="customer" on:change={handleChange}
										on:blur={handleChange} bind:value={$form.customer} required class="form-control"
										placeholder="Enter Name" />
								</div>

								<div class="mb-3">
									<Label for="productname-field" class="form-label">Product</Label>
									<select class="form-control" data-trigger bind:value={$form.product} name="product"
										on:change={handleChange} on:blur={handleChange} required id="productname-field">
										<option value="">Product</option>
										<option value="Puma Tshirt">Puma Tshirt</option>
										<option value="Adidas Sneakers">Adidas Sneakers</option>
										<option value="350 ml Glass Grocery Container">350 ml Glass Grocery Container
										</option>
										<option value="American egale outfitters Shirt">American egale outfitters Shirt
										</option>
										<option value="Galaxy Watch4">Galaxy Watch4</option>
										<option value="Apple iPhone 12">Apple iPhone 12</option>
										<option value="Funky Prints T-shirt">Funky Prints T-shirt</option>
										<option value="USB Flash Drive Personalized with 3D Print">
											USB Flash Drive Personalized with 3D Print</option>
										<option value="Oxford Button-Down Shirt">Oxford Button-Down Shirt</option>
										<option value="Classic Short Sleeve Shirt">Classic Short Sleeve Shirt</option>
										<option value="Half Sleeve T-Shirts (Blue)">Half Sleeve T-Shirts (Blue)</option>
										<option value="Noise Evolve Smartwatch">Noise Evolve Smartwatch</option>
									</select>
								</div>

								<div class="mb-3">
									<Label for="date-field" class="form-label">Order Date</Label>
									<Flatpickr name="orderDate" class="form-control" id="datepicker-publish-input"
										placeholder="Select a date" options={{ enableTime: true, altInput: true,
										altFormat: "d M, Y, G:i K" , dateFormat: "d M, Y, G:i K" , }}
										bind:value={$form.orderDate} on:change={handleChange} on:blur={handleChange} />
								</div>

								<div class="row gy-4 mb-3">
									<div class="col-md-6">
										<div>
											<Label for="amount-field" class="form-label">Amount</Label>
											<Input type="text" id="amount-field" bind:value={$form.amount} name="amount"
												on:change={handleChange} on:blur={handleChange} required
												class="form-control" placeholder="Total amount" />
										</div>
									</div>
									<div class="col-md-6">
										<div>
											<Label for="payment-field" class="form-label">Payment Method</Label>
											<select class="form-control" data-trigger bind:value={$form.payment}
												on:change={handleChange} on:blur={handleChange} required name="payment"
												id="payment-field">
												<option value="">Payment Method</option>
												<option value="Mastercard">Mastercard</option>
												<option value="Visa">Visa</option>
												<option value="COD">COD</option>
												<option value="Paypal">Paypal</option>
											</select>
										</div>
									</div>
								</div>

								<div>
									<Label for="delivered-status" class="form-label">Delivery Status</Label>
									<select class="form-control" data-trigger bind:value={$form.status} name="status"
										id="delivered-status">
										<option value="">Delivery Status</option>
										<option value="Pending">Pending</option>
										<option value="Inprogress">Inprogress</option>
										<option value="Cancelled">Cancelled</option>
										<option value="Pickups">Pickups</option>
										<option value="Delivered">Delivered</option>
										<option value="Returns">Returns</option>
									</select>
								</div>
							</ModalBody>
							<div class="modal-footer">
								<div class="hstack gap-2 justify-content-end">
									<button type="button" class="btn btn-light" on:click={toggle}>Close</button>
									<button type="submit" class="btn btn-success" id="add-btn">Add Order</button>
								</div>
							</div>
						</form>
					</Modal> -->
						<Modal isOpen={showModal} className="modal-dialog-centered">
							<div class="modal-header p-3 bg-light">
								<h5
									class="modal-title"
									id="createFileModalLabel"
								>
									Add Order
								</h5>
								<button
									type="button"
									class="btn-close"
									on:click={AddOrderToggle}
								/>
							</div>
							<form on:submit|preventDefault={handleSubmit}>
								<div class="modal-body">
									<Input type="hidden" id="id-field" />

									<div class="mb-3" id="modal-id">
										<Label for="orderId" class="form-label"
											>Order Id</Label
										>
										<Input
											type="text"
											id="orderId"
											on:change={handleChange}
											on:blur={handleChange}
											bind:value={$form.orderId}
											name="orderId"
											class="form-control"
											placeholder="ID"
										/>
										{#if $errors.orderId}
											<small class="text-danger">{$errors.orderId}</small>
										{/if}
									</div>

									<div class="mb-3">
										<Label
											for="customername-field"
											class="form-label"
											>Customer Name</Label
										>
										<Input
											type="text"
											id="customername-field"
											name="customer"
											on:change={handleChange}
											on:blur={handleChange}
											bind:value={$form.customer}
											class="form-control"
											placeholder="Enter Name"
										/>
										{#if $errors.customer}
											<small class="text-danger">{$errors.customer}</small>
										{/if}
									</div>

									<div class="mb-3">
										<Label
											for="productname-field"
											class="form-label">Product</Label
										>
										<select
											class="form-control"
											data-trigger
											bind:value={$form.product}
											name="product"
											on:change={handleChange}
											on:blur={handleChange}
											id="productname-field"
										>
											<option value="">Product</option>
											<option value="Puma Tshirt"
												>Puma Tshirt</option
											>
											<option value="Adidas Sneakers"
												>Adidas Sneakers</option
											>
											<option
												value="350 ml Glass Grocery Container"
												>350 ml Glass Grocery Container
											</option>
											<option
												value="American egale outfitters Shirt"
												>American egale outfitters Shirt
											</option>
											<option value="Galaxy Watch4"
												>Galaxy Watch4</option
											>
											<option value="Apple iPhone 12"
												>Apple iPhone 12</option
											>
											<option value="Funky Prints T-shirt"
												>Funky Prints T-shirt</option
											>
											<option
												value="USB Flash Drive Personalized with 3D Print"
											>
												USB Flash Drive Personalized
												with 3D Print</option
											>
											<option
												value="Oxford Button-Down Shirt"
												>Oxford Button-Down Shirt</option
											>
											<option
												value="Classic Short Sleeve Shirt"
												>Classic Short Sleeve Shirt</option
											>
											<option
												value="Half Sleeve T-Shirts (Blue)"
												>Half Sleeve T-Shirts (Blue)</option
											>
											<option
												value="Noise Evolve Smartwatch"
												>Noise Evolve Smartwatch</option
											>
										</select>
										{#if $errors.product}
											<small class="text-danger">{$errors.product}</small>
										{/if}
									</div>

									<div class="mb-3">
										<Label
											for="date-field"
											class="form-label">Order Date</Label
										>
										<Flatpickr
											class="form-control"
											name="ordeDate"
											id="datepicker-publish-input"
											placeholder="Select a date"
											options={{
												enableTime: true,
												altInput: true,
												altFormat: "d M, Y, G:i K",
												dateFormat: "d M, Y, G:i K",
											}}
											bind:value={$form.orderDate}
										/>
									</div>

									<div class="row gy-4 mb-3">
										<div class="col-md-6">
											<div>
												<Label
													for="amount-field"
													class="form-label"
													>Amount</Label
												>
												<Input
													type="text"
													id="amount-field"
													bind:value={$form.amount}
													name="amount"
													on:change={handleChange}
													on:blur={handleChange}
													class="form-control"
													placeholder="Total amount"
												/>
												{#if $errors.amount}
													<small class="text-danger">{$errors.amount}</small>
												{/if}
											</div>
										</div>
										<div class="col-md-6">
											<div>
												<Label
													for="payment-field"
													class="form-label"
													>Payment Method</Label
												>
												<select
													class="form-control"
													data-trigger
													bind:value={$form.payment}
													on:change={handleChange}
													on:blur={handleChange}
													name="payment"
													id="payment-field"
												>
													<option value=""
														>Payment Method</option
													>
													<option value="Mastercard"
														>Mastercard</option
													>
													<option value="Visa"
														>Visa</option
													>
													<option value="COD"
														>COD</option
													>
													<option value="Paypal"
														>Paypal</option
													>
												</select>
												{#if $errors.payment}
													<small class="text-danger">{$errors.payment}</small>
												{/if}
											</div>
										</div>
									</div>

									<div>
										<Label
											for="delivered-status"
											class="form-label"
											>Delivery Status</Label
										>
										<select
											class="form-control"
											data-trigger
											bind:value={$form.status}
											on:change={handleChange}
											on:blur={handleChange}
											name="status"
											id="delivered-status"
										>
											<option value=""
												>Delivery Status</option
											>
											<option value="Pending"
												>Pending</option
											>
											<option value="Inprogress"
												>Inprogress</option
											>
											<option value="Cancelled"
												>Cancelled</option
											>
											<option value="Pickups"
												>Pickups</option
											>
											<option value="Delivered"
												>Delivered</option
											>
											<option value="Returns"
												>Returns</option
											>
										</select>
										{#if $errors.status}
													<small class="text-danger">{$errors.status}</small>
												{/if}
									</div>
								</div>
								<div class="modal-footer">
									<div
										class="hstack gap-2 justify-content-end"
									>
										<button
											type="button"
											class="btn btn-light"
											on:click={AddOrderToggle}
											>Close</button
										>
										<button
											type="submit"
											class="btn btn-success"
											id="add-btn">Add Order</button
										>
									</div>
								</div>
							</form>
						</Modal>
						<!-- Modal -->
						<!-- <Modal class="flip" id="deleteOrder">
						<ModalBody class="p-5 text-center">
							<lord-icon src="//cdn.lordicon.com/gsqxdxog.json" trigger="loop"
								colors="primary:#405189,secondary:#f06548" style="width:90px;height:90px" />
							<div class="mt-4 text-center">
								<h4>You are about to delete a order ?</h4>
								<p class="text-muted fs-15 mb-4">
									Deleting your order will remove all of your information from our database.
								</p>
								<div class="hstack gap-2 justify-content-center remove">
									<button class="btn btn-link link-success fw-medium text-decoration-none"
										data-bs-dismiss="modal"><i class="ri-close-line me-1 align-middle" />
										Close</button>
									<button class="btn btn-danger" id="delete-record">Yes, Delete It</button>
								</div>
							</div>
						</ModalBody>
					</Modal> -->
						<!--end modal -->
					</CardBody>
				</Card>
			</Col>
			<!--end col-->
		</Row>
	</Container>
</div>

<style global>
	@import "//cdn.jsdelivr.net/npm/gridjs/dist/theme/mermaid.min.css";
</style>
