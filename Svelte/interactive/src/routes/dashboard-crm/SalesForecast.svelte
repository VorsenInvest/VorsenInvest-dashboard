<script>
	import {
		Card,
		CardHeader,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Dropdown
	} from 'sveltestrap';
	import SalesForecastCharts from './DashboardCrmCharts.svelte';
</script>

<Col xxl={3} md={6}>
	<Card>
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Sales Forecast</h4>
			<div class="flex-shrink-0">
				<Dropdown class="card-header-dropdown">
					<DropdownToggle tag="a" color="" class="text-reset dropdown-btn p-0">
						<span class="fw-semibold text-uppercase fs-12">Sort by: </span><span class="text-muted">Nov 2021<i class="mdi mdi-chevron-down ms-1" /></span
						>
					</DropdownToggle>
					<DropdownMenu end >
						<DropdownItem>Oct 2021</DropdownItem>
						<DropdownItem>Nov 2021</DropdownItem>
						<DropdownItem>Dec 2021</DropdownItem>
						<DropdownItem>Jan 2022</DropdownItem>
					</DropdownMenu>
				</Dropdown>
			</div>
		</CardHeader>
		<div class="card-body pb-0">
			<div id="sales-forecast-chart" class="apex-charts" dir="ltr">
				<SalesForecastCharts dataColors={["--vz-primary", "--vz-info", "--vz-warning"]} />
			</div>
		</div>
	</Card>
</Col>
