<script>
	import {
		Card,
		CardHeader,
		Col,
		DropdownMenu,
		DropdownToggle,
		Dropdown,
		DropdownItem
	} from 'sveltestrap';
	import AudiencesSessionsCharts from './AudiencesSessionsCharts.svelte';
</script>

<Col xl={6}>
	<Card class="card-height-100">
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Audiences Sessions by Country</h4>
			<div class="flex-shrink-0">
				<Dropdown class="card-header-dropdown">
					<DropdownToggle tag="a" color="" class="text-reset dropdown-btn p-0" role="button">
						<span class="fw-semibold text-uppercase fs-12">Sort by: </span><span class="text-muted">Current Week<i class="mdi mdi-chevron-down ms-1" /></span
						>
					</DropdownToggle>
					<DropdownMenu class="dropdown-menu-end">
						<DropdownItem>Today</DropdownItem>
						<DropdownItem>Last Week</DropdownItem>
						<DropdownItem>Last Month</DropdownItem>
						<DropdownItem>Current Year</DropdownItem>
					</DropdownMenu>
				</Dropdown>
			</div>
		</CardHeader>
		<div class="card-body p-0">
			<div>
				<div id="audiences-sessions-country-charts" class="apex-charts" dir="ltr">
					<AudiencesSessionsCharts dataColors={["--vz-primary", "--vz-secondary",  "--vz-secondary-bg"]}/>
				</div>
			</div>
		</div>
	</Card>
</Col>
