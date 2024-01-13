<script>
	import {
		CardBody,
		Row,
		Col,
		Card,
		Container,
		CardHeader,
		Form,
		Input,
		Button,
	} from "sveltestrap";

	import Link from "svelte-link";
	import Flatpickr from "svelte-flatpickr";
	import Select from "svelte-select";
	import Counter from "../../../Components/Common/CounterPage.svelte";

	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import invoiceData from "../../../common/data/invoiceList";
	import {
		FileTextIcon,
		CheckSquareIcon,
		ClockIcon,
		XOctagonIcon,
	} from "svelte-feather-icons";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";

	const allstatus = [
		{ label: "Status", value: "Status" },
		{ label: "All", value: "All" },
		{ label: "Unpaid", value: "Unpaid" },
		{ label: "Paid", value: "Paid" },
		{ label: "Cancel", value: "Cancel" },
		{ label: "Refund", value: "Refund" },
	];

	let isStatus = "Status";

	const data = invoiceData.invoiceTable;

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
			id: "invoiceId",
			name: "ID",
			formatter: (cell) =>
				html(
					`<a href="/invoices/apps-invoices-details" class="fw-medium link-primary">${cell}</a>`
				),
		},
		{
			id: "name",
			hidden: true,
		},
		{
			id: "img",
			name: "Customer",
			formatter: (cells, row) => {
				if (cells) {
					return html(`<div class="d-flex align-items-center">
                        <img
                src=${cells}
                alt=""
                class="avatar-xs rounded-circle me-2"
              />
              ${row.cells[2].data}
              </div>`);
				} else {
					return html(`<div class="d-flex align-items-center"><div class="flex-shrink-0 avatar-xs me-2">
                  <div class="avatar-title bg-success-subtle text-success rounded-circle fs-13">
                    ${
						row.cells[2].data.charAt(0) +
						row.cells[2].data
							.split(" ")
							.slice(-1)
							.toString()
							.charAt(0)
					}
                  </div>
                </div>
              ${row.cells[2].data}
            </div>`);
				}
			},
		},
		{
			id: "email",
			name: "Email",
		},
		{
			id: "country",
			name: "Country",
		},
		{
			id: "time",
			hidden: true,
		},
		{
			id: "date",
			name: "Date",
			formatter: (cells, row) =>
				html(`${cells},
            <small class="text-muted">${row.cells[6].data}</small>`),
		},
		{
			id: "amount",
			name: "Amount",
		},
		{
			id: "statusClass",
			hidden: true,
		},
		{
			id: "status",
			name: "PAYMENT STATUS",
			formatter: (cell, row) => {
				return html(`<span class="badge text-${row.cells[9].data} text-uppercase bg-${row.cells[9].data}-subtle">
                ${cell}
            </span>`);
			},
		},
		{
			name: "Action",
			formatter: (cell, row) =>
				html(`<ul class="list-inline hstack gap-2 mb-0">
				<li class="list-inline-item edit">
					<a href="/ecommerce/apps-ecommerce-product-details" class="text-muted d-inline-block">
						<i class="ri-eye-fill align-bottom me-2 text-muted"></i>
					</a>
				</li>
				<li class="list-inline-item edit">
					<a href="/invoices/apps-invoices-create" class="text-muted d-inline-block">
						<i class="ri-pencil-fill align-bottom me-2 text-muted"></i>
					</a>
				</li>
				<li class="list-inline-item">
					<a href="/ecommerce/apps-ecommerce-add-product">
						<i class="ri-download-2-line align-bottom me-2 text-muted"></i>
					</a>
				</li>
				<li class="list-inline-item">
					<a class="edit-item-btn" href={null}>
						<i class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>
					</a>
				</li>
			</ul>`),
		},
	];
</script>

<svelte:head>
	<title>Invoice List | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<Counter />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Invoice List" pageTitle="Invoices" />
		<Row>
			{#each invoiceData.invoiceWidgets as invoicewidget}
				<Col xl={3} md={6}>
					<Card class="card-animate">
						<CardBody>
							<div class="d-flex align-items-center">
								<div class="flex-grow-1">
									<p
										class="text-uppercase fw-medium text-muted mb-0"
									>
										{invoicewidget.label}
									</p>
								</div>
								<div class="flex-shrink-0">
									<h5
										class={"fs-14 mb-0 text-" +
											invoicewidget.percentageClass}
									>
										<i
											class="ri-arrow-right-up-line fs-13 align-middle"
										/>{" "}
										{invoicewidget.percentage}
									</h5>
								</div>
							</div>
							<div
								class="d-flex align-items-end justify-content-between mt-4"
							>
								<div>
									<h4
										class="fs-22 fw-semibold ff-secondary mb-4"
									>
										{invoicewidget.prefix}<span
											class="counter-value"
											data-target={invoicewidget.counter}
											>0</span
										>{invoicewidget.suffix}
									</h4>

									<span class="badge bg-warning me-1">
										{invoicewidget.badge}
									</span>{" "}
									<span class="text-muted">
										{" "}
										{invoicewidget.caption}
									</span>
								</div>
								<div class="avatar-sm flex-shrink-0">
									<span
										class="avatar-title bg-light rounded fs-3"
									>
										{#if invoicewidget.feaIcon === "file-text"}
											<FileTextIcon
												class="text-success icon-dual-success"
												size="24"
											/>
										{/if}
										{#if invoicewidget.feaIcon === "check-square"}
											<CheckSquareIcon
												class="text-success icon-dual-success"
												size="24"
											/>
										{/if}
										{#if invoicewidget.feaIcon === "clock"}
											<ClockIcon
												class="text-success icon-dual-success"
												size="24"
											/>
										{/if}
										{#if invoicewidget.feaIcon === "x-octagon"}
											<XOctagonIcon
												class="text-success icon-dual-success"
												size="24"
											/>
										{/if}
									</span>
								</div>
							</div>
						</CardBody>
					</Card>
				</Col>
			{/each}
		</Row>

		<Row>
			<Col lg={12}>
				<Card id="invoiceList">
					<CardHeader class="border-0">
						<div class="d-flex align-items-center">
							<h5 class="card-title mb-0 flex-grow-1">
								Invoices
							</h5>
							<div class="flex-shrink-0">
								<div class="d-flex gap-2 flex-wrap">
									<Link
										href="/invoices/apps-invoices-create"
										class="btn btn-secondary"
									>
										<i
											class="ri-add-line align-bottom me-1"
										/> Create Invoice
									</Link>
								</div>
							</div>
						</div>
					</CardHeader>
					<CardBody
						class="bg-light-subtle border border-dashed border-start-0 border-end-0"
					>
						<Form>
							<Row class="g-3">
								<Col sm={12} xxl={5}>
									<div class="search-box">
										<Input
											type="text"
											class="form-control search bg-light border-light"
											placeholder="Search for customer, email, country, status or something..."
										/>
										<i class="ri-search-line search-icon" />
									</div>
								</Col>

								<Col sm={4} xxl={3}>
									<Flatpickr
										class="form-control bg-light border-light"
										id="datepicker-publish-input"
										placeholder="Select a date"
										options={{
											altInput: true,
											altFormat: "F j, Y",
											mode: "multiple",
											dateFormat: "d.m.y",
										}}
									/>
								</Col>

								<Col sm={4} xxl={3}>
									<div class="select-single">
										<Select
											value={isStatus}
											items={allstatus}
											name="choices-single-default"
											id="idStatus"
										/>
									</div>
								</Col>

								<Col sm={4} xxl={1}>
									<Button color="primary" class="w-100" type="button">
										<i
											class="ri-equalizer-fill me-1 align-bottom"
										/>{" "}
										Filters
									</Button>
								</Col>
							</Row>
						</Form>
					</CardBody>
					<CardBody>
						<div>
							{#if invoiceData.invoiceTable.length > 0}
								<div class="table-card gridjs-border-none">
									<Grid
										{data}
										{columns}
										className={{ th: "text-muted" }}
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
											We've searched more than 200k+ tasks
											We did not find any tasks for you
											search.
										</p>
									</div>
								</div>
							{/if}
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
