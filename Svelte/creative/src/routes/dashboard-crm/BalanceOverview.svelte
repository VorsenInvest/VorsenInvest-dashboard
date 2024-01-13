<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Dropdown
	} from 'sveltestrap';
	import BalanceOverviewCharts from './BalanceOverviewCharts.svelte';
</script>

<Col xxl={6}>
	<Card class="card-height-100">
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Balance Overview</h4>
			<div class="flex-shrink-0">
				<Dropdown class="card-header-dropdown">
					<DropdownToggle class="text-reset dropdown-btn p-0" color="" tag="a" role="button">
						<span class="fw-bold text-uppercase fs-12">Sort by: </span><span class="text-muted">Current Year<i class="mdi mdi-chevron-down ms-1" /></span
						>
					</DropdownToggle>
					<DropdownMenu class="dropdown-menu-end" end>
						<DropdownItem>Today</DropdownItem>
						<DropdownItem>Last Week</DropdownItem>
						<DropdownItem>Last Month</DropdownItem>
						<DropdownItem>Current Year</DropdownItem>
					</DropdownMenu>
				</Dropdown>
			</div>
		</CardHeader>
		<CardBody class="px-0">
			<ul class="list-inline main-chart text-center mb-0">
				<li class="list-inline-item chart-border-left me-0 border-0">
					<h4 class="text-primary">
						$584k <span class="text-muted d-inline-block fs-14 align-middle ms-2">Revenue</span>
					</h4>
				</li>
				<li class="list-inline-item chart-border-left me-0">
					<h4>
						$497k<span class="text-muted d-inline-block fs-14 align-middle ms-2">Expenses</span>
					</h4>
				</li>
				<li class="list-inline-item chart-border-left me-0">
					<h4>
						<span data-plugin="counterup">3.6</span>%<span
							class="text-muted d-inline-block fs-14 align-middle ms-2">Profit Ratio</span
						>
					</h4>
				</li>
			</ul>

			<div id="revenue-expenses-charts" dir="ltr">
				<BalanceOverviewCharts dataColors={["--vz-success", "--vz-danger"]} />
			</div>
		</CardBody>
	</Card>
</Col>
