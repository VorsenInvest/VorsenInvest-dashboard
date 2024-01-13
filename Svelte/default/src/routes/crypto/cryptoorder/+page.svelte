<script>
	import { Container, Row } from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import Flatpickr from "svelte-flatpickr";
	import Select from "svelte-select";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";
	import cryptoData from "../../../common/data/cryptoPage";

	const ordeType = [
		{ value: "Select Type", label: "Select Type" },
		{ value: "Buy", label: "Buy" },
		{ value: "Sell", label: "Sell" },
	];

	const ordeStatus = [
		{ value: "Select Status", label: "Select Status" },
		{ value: "Successful", label: "Successful" },
		{ value: "Cancelled", label: "Cancelled" },
		{ value: "Pending", label: "Pending" },
	];

	const data = cryptoData.CryptoOrders;

	const columns = [
		{
			id: "time",
			hidden: true,
		},
		{
			name: "Date",
			id: "date",
			sort:true,
			formatter: (cell, row) =>
				html(
					`${cell} <small class="text-muted">${row.cells[0].data}</small>`
				),
		},
		{
			id: "coinName",
			hidden: true,
		},
		{
			name: "Name",
			id: "img",
			sort:true,
			formatter: (cell, row) =>
				html(`<div class="d-flex align-items-center">
                        <div class="flex-shrink-0">
                            <img src=${cell} alt="" class="avatar-xxs" />
                        </div>
                        <a href={null} class="currency_name flex-grow-1 ms-2">${row.cells[2].data}</a>
                    </div>`),
		},
		{
			name: "Type",
			id: "type",
			sort:true,
			formatter: (cell) => {
				{
					if (cell == "Buy") {
						return html(
							`<span class="type text-success">${cell}</span>`
						);
					} else {
						return html(
							`<span class="type text-danger">${cell}</span>`
						);
					}
				}
			},
		},
		{
			id: "quantity",
			name: "Quantity",
			sort:true,
		},
		{
			id: "orderValue",
			name: "Order Value",
			sort:true,
		},
		{
			id: "avgPrice",
			name: "Avg Price",
			sort:true,
		},
		{
			id: "price",
			name: "Price",
			sort:true,
		},
		{
			id: "status",
			name: "Status",
			sort:true,
			formatter: (cell) => {
				if (cell == "Pending") {
					return html(
						`<span class="badge bg-warning-subtle text-warning text-uppercase">${cell}</span>`
					);
				} else if (cell == "Successful") {
					return html(
						`<span class="badge bg-success-subtle text-success text-uppercase">${cell}</span>`
					);
				} else if (cell == "Cancelled") {
					return html(
						`<span class="badge bg-danger-subtle text-danger text-uppercase">${cell}</span>`
					);
				} else {
					return null;
				}
			},
		},
	];
</script>

<svelte:head>
	<title>Orders | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Orders" pageTitle="Crypto" />

		<div class="row" id="contactList">
			<div class="col-lg-12">
				<div class="card">
					<div class="card-header d-flex align-items-center border-0">
						<h5 class="card-title mb-0 flex-grow-1">All Orders</h5>
						<div class="flex-shrink-0">
							<div class="flax-shrink-0 hstack gap-2">
								<button class="btn btn-primary"
									>Today's Orders</button
								>
								<button class="btn btn-soft-info"
									>Past Orders</button
								>
							</div>
						</div>
					</div>
					<div
						class="card-body border border-dashed border-end-0 border-start-0"
					>
						<div class="row g-2">
							<div class="col-xl-4 col-md-6">
								<div class="search-box">
									<input
										type="text"
										class="form-control search"
										placeholder="Search to orders..."
									/>
									<i class="ri-search-line search-icon" />
								</div>
							</div>
							<!--end col-->
							<div class="col-xl-3 col-md-6">
								<div class="input-group">
									<span
										class="input-group-text"
										id="basic-addon1"
										><i class="ri-calendar-2-line" /></span
									>
									<Flatpickr
										class="form-control"
										options={{
											dateFormat: "d M, Y",
										}}
										placeholder="Selact Date"
									/>
								</div>
							</div>
							<!--end col-->
							<div class="col-xl-2 col-md-4">
								<div class="select-single">
									<Select
										class="form-control"
										id="choices-single-default"
										placeholder="Select Type"
										items={ordeType}
									/>
								</div>
							</div>
							<!--end col-->
							<div class="col-xl-2 col-md-4">
								<div class="select-single">
									<Select
										class="form-control"
										id="choices-single-default2"
										placeholder="Select Status"
										items={ordeStatus}
									/>
								</div>
							</div>
							<!--end col-->
							<div class="col-xl-1 col-md-4">
								<button class="btn btn-success w-100"
									>Filters</button
								>
							</div>
						</div>
						<!--end row-->
					</div>
					<div class="card-body">
						<div
							class="table-responsive table-card gridjs-border-none"
						>
							{#if cryptoData.CryptoOrders.length > 0}
								<Grid
									{data}
									{columns}
									pagination={{ enabled: true, limit: 10 }}
								/>
							{:else}
								<div class="noresult" style="display: none">
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
										<p class="text-muted mb-0">
											We've searched more than 150+ orders
											We did not find any orders for you
											search.
										</p>
									</div>
								</div>
							{/if}
						</div>
					</div>
				</div>
				<!--end card-->
			</div>
			<!--end col-->
		</div>
	</Container>
</div>
