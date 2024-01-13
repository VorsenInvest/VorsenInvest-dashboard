<svelte:head>
  <title>Datatables | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import Grid from 'gridjs-svelte';
	import {
		Card,
		CardBody,
		Col,
		Container,
		Row,
		CardHeader
	} from 'sveltestrap';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import { DataHandler, Datatable, Th, ThFilter }from '@vincjo/datatables'
	

	const data = [
	{
        "sr_no": "01",
        "id": "VLZ-452",
        "purchase_id": "VLZ1400087402",
        "title": "Post launch reminder/ post list",
        "user": "Joseph Parker",
        "assign_to": "Alexis Clarke",
        "created_by": "Joseph Parker",
        "created_date": "03 Oct, 2021",
        "status": "Re-open"
    },
    {
        "sr_no": "02",
        "id": "VLZ-453",
        "purchase_id": "VLZ1400087425",
        "title": "Additional Calendar",
        "user": "Diana Kohler",
        "assign_to": "Admin",
        "created_by": "Mary Rucker",
        "created_date": "05 Oct, 2021",
        "status": "On-Hold"
    },
    {
        "sr_no": "03",
        "id": "VLZ-454",
        "purchase_id": "VLZ1400087438",
        "title": "Make a creating an account profile",
        "user": "Tonya Noble",
        "assign_to": "Admin",
        "created_by": "Tonya Noble",
        "created_date": "27 April, 2022",
        "status": "Closed"
    },
	{
        "sr_no": "04",
        "id": "VLZ-452",
        "purchase_id": "VLZ1400087402",
        "title": "Post launch reminder/ post list",
        "user": "Joseph Parker",
        "assign_to": "Alexis Clarke",
        "created_by": "Joseph Parker",
        "created_date": "03 Oct, 2021",
        "status": "Re-open"
    },
    {
        "sr_no": "05",
        "id": "VLZ-453",
        "purchase_id": "VLZ1400087425",
        "title": "Additional Calendar",
        "user": "Diana Kohler",
        "assign_to": "Admin",
        "created_by": "Mary Rucker",
        "created_date": "05 Oct, 2021",
        "status": "On-Hold"
    },
    {
        "sr_no": "06",
        "id": "VLZ-454",
        "purchase_id": "VLZ1400087438",
        "title": "Make a creating an account profile",
        "user": "Tonya Noble",
        "assign_to": "Admin",
        "created_by": "Tonya Noble",
        "created_date": "27 April, 2022",
        "status": "Closed"
    },
	{
        "sr_no": "07",
        "id": "VLZ-452",
        "purchase_id": "VLZ1400087402",
        "title": "Post launch reminder/ post list",
        "user": "Joseph Parker",
        "assign_to": "Alexis Clarke",
        "created_by": "Joseph Parker",
        "created_date": "03 Oct, 2021",
        "status": "Re-open"
    },
    {
        "sr_no": "08",
        "id": "VLZ-453",
        "purchase_id": "VLZ1400087425",
        "title": "Additional Calendar",
        "user": "Diana Kohler",
        "assign_to": "Admin",
        "created_by": "Mary Rucker",
        "created_date": "05 Oct, 2021",
        "status": "On-Hold"
    },
    {
        "sr_no": "09",
        "id": "VLZ-454",
        "purchase_id": "VLZ1400087438",
        "title": "Make a creating an account profile",
        "user": "Tonya Noble",
        "assign_to": "Admin",
        "created_by": "Tonya Noble",
        "created_date": "27 April, 2022",
        "status": "Closed"
    },
	{
        "sr_no": "10",
        "id": "VLZ-452",
        "purchase_id": "VLZ1400087402",
        "title": "Post launch reminder/ post list",
        "user": "Joseph Parker",
        "assign_to": "Alexis Clarke",
        "created_by": "Joseph Parker",
        "created_date": "03 Oct, 2021",
        "status": "Re-open"
    },
    {
        "sr_no": "11",
        "id": "VLZ-453",
        "purchase_id": "VLZ1400087425",
        "title": "Additional Calendar",
        "user": "Diana Kohler",
        "assign_to": "Admin",
        "created_by": "Mary Rucker",
        "created_date": "05 Oct, 2021",
        "status": "On-Hold"
    },
    {
        "sr_no": "12",
        "id": "VLZ-454",
        "purchase_id": "VLZ1400087438",
        "title": "Make a creating an account profile",
        "user": "Tonya Noble",
        "assign_to": "Admin",
        "created_by": "Tonya Noble",
        "created_date": "27 April, 2022",
        "status": "Closed"
    },
	{
        "sr_no": "13",
        "id": "VLZ-452",
        "purchase_id": "VLZ1400087402",
        "title": "Post launch reminder/ post list",
        "user": "Joseph Parker",
        "assign_to": "Alexis Clarke",
        "created_by": "Joseph Parker",
        "created_date": "03 Oct, 2021",
        "status": "Re-open"
    },
    {
        "sr_no": "14",
        "id": "VLZ-453",
        "purchase_id": "VLZ1400087425",
        "title": "Additional Calendar",
        "user": "Diana Kohler",
        "assign_to": "Admin",
        "created_by": "Mary Rucker",
        "created_date": "05 Oct, 2021",
        "status": "On-Hold"
    },
    {
        "sr_no": "15",
        "id": "VLZ-454",
        "purchase_id": "VLZ1400087438",
        "title": "Make a creating an account profile",
        "user": "Tonya Noble",
        "assign_to": "Admin",
        "created_by": "Tonya Noble",
        "created_date": "27 April, 2022",
        "status": "Closed"
    },
]

	const data1 = [
		['#VL2111', 'Jonathan', '07 Oct, 2021', '$24.05', 'Paid'],
		['#VL2110', 'Harold', '07 Oct, 2021', '$26.15', 'Paid'],
		['#VL2109', 'Shannon', '06 Oct, 2021', '$21.25', 'Refund'],
		['#VL2108', 'Robert', '05 Oct, 2021', '$25.03', 'Paid'],
		['#VL2107', 'Noel', '05 Oct, 2021', '$22.61', 'Paid'],
		['#VL2106', 'Traci', '04 Oct, 2021', '$24.05', 'Paid'],
		['#VL2105', 'Kerry', '04 Oct, 2021', '$26.15', 'Paid'],
		['#VL2104', 'Patsy', '04 Oct, 2021', '$21.25', 'Refund'],
		['#VL2103', 'Cathy', '03 Oct, 2021', '$22.61', 'Paid'],
		['#VL2102', 'Tyrone', '03 Oct, 2021', '$25.03', 'Paid']
	];

	const data2 = [
		[
			'Jonathan',
			'jonathan@example.com',
			'Senior Implementation Architect',
			'Hauck Inc',
			'Holy See'
		],
		['Harold', 'harold@example.com', 'Forward Creative Coordinator', 'Metz Inc', 'Iran'],
		[
			'Shannon',
			'shannon@example.com',
			'Legacy Functionality Associate',
			'Zemlak Group',
			'South Georgia'
		],
		['Robert', 'robert@example.com', 'Product Accounts Technician', 'Hoeger', 'San Marino'],
		['Noel', 'noel@example.com', 'Customer Data Director', 'Howell - Rippin', 'Germany'],
		['Traci', 'traci@example.com', 'Corporate Identity Director', 'Koelpin - Goldner', 'Vanuatu'],
		[
			'Kerry',
			'kerry@example.com',
			'Lead Applications Associate',
			'Feeney, Langworth and Tremblay',
			'Niger'
		],
		['Patsy', 'patsy@example.com', 'Dynamic Assurance Director', 'Streich Group', 'Niue'],
		[
			'Cathy',
			'cathy@example.com',
			'Customer Data Director',
			'Ebert, Schamberger and Johnston',
			'Mexico'
		],
		[
			'Tyrone',
			'tyrone@example.com',
			'Senior Response Liaison',
			'Raynor, Rolfson and Daugherty',
			'Qatar'
		]
	];
	const handler = new DataHandler(data, { rowsPerPage: 10 })
    const rows = handler.getRows()
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Datatables" pageTitle="Tables" />

		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0 flex-grow-1">Base Datatables</h4>
					</CardHeader>

					<CardBody>
						<div id="">
							<Datatable {handler}>
								<table class="table table-bordered dt-responsive nowrap table-striped align-middle" style="width: 100%;">
									<thead>
										<tr>
											<Th {handler} orderBy="sr_no">Sr No</Th>
											<Th {handler} orderBy="id">ID</Th>
											<Th {handler} orderBy="purchase_id">Purcase Id</Th>
											<Th {handler} orderBy="title">Title</Th>
											<Th {handler} orderBy="user">User</Th>
											<Th {handler} orderBy="assign_to">Assign To</Th>
											<Th {handler} orderBy="created_by">Created By</Th>
											<Th {handler} orderBy="created_date">Created Date</Th>
											<Th {handler} orderBy="status">status</Th>
										</tr>
									</thead>
									<tbody>
										{#each $rows as row}
											<tr>
												<td>{row.sr_no}</td>
												<td>{row.id}</td>
												<td>{row.purchase_id}</td>
												<td>{row.title}</td>
												<td>{row.user}</td>
												<td>{row.assign_to}</td>
												<td>{row.created_by}</td>
												<td>{row.created_date}</td>
												<td>{row.status}</td>
											</tr>
										{/each}
									</tbody>
								</table>
							</Datatable>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

	</Container>
</div>

<style global>
	@import '//cdn.jsdelivr.net/npm/gridjs/dist/theme/mermaid.min.css';
</style>
