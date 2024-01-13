<script>
	import { Card, CardBody, CardHeader } from "sveltestrap";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";
	import cryptoData from "../../../common/data/cryptoPage";

	const data = cryptoData.marketStatus;
	const columns = [
		{
			id: "img",
			hidden: true,
		},
		{
			id: "coinName",
			name: "Name",
			formatter: (cell, row) =>
				html(`
            <div class="d-flex align-items-center fw-medium">
                <img src=${row.cells[0].data} alt="" class="avatar-xxs me-2 material-shadow" />
                <a href={null} class="currency_name">${cell}</a>
            </div>
            `),
		},
		{
			id: "quantity",
			name: "Quantity",
		},
		{
			id: "avgPrice",
			name: "Avg. Price",
		},
		{
			id: "value",
			name: "Current Value",
		},
		{
			id: "returns",
			name: "Returns",
		},
		{
			id: "icon",
			hidden: true,
		},
		{
			id: "percentageClass",
			hidden: true,
		},
		{
			id: "percentage",
			name: "Returns %",
			formatter: (cell, row) =>
				html(`<h6 class="text-${row.cells[7].data} fs-13 mb-0">
                <i class="${row.cells[6].data} align-middle me-1"></i>
                ${cell}
            </h6> `),
		},
	];
</script>

<Card>
	<CardHeader class="border-bottom-dashed d-flex align-items-center">
		<h4 class="card-title mb-0 flex-grow-1">Market Status</h4>
		<div class="flex-shrink-0">
			<div class="btn-group" role="group" aria-label="Basic example">
				<button type="button" class="btn btn-primary btn-sm"
					>Today</button
				>
				<button type="button" class="btn btn-outline-primary btn-sm"
					>Overall</button
				>
			</div>
		</div>
	</CardHeader>
	<CardBody>
		<div class="table-card gridjs-border-none">
			<Grid {data} {columns} pagination={{ enabled: true, limit: 6 }} />
		</div>
	</CardBody>
</Card>
