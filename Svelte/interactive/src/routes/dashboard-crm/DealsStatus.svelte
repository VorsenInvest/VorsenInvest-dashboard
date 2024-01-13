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
	import data from '../../common/data/dashboardcrm';
</script>

<Col xl={7}>
	<Card>
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Deals Status</h4>
			<div class="flex-shrink-0">
				<Dropdown class="card-header-dropdown">
					<DropdownToggle tag="a" class="text-reset dropdown-btn p-0" color="" role="button">
						<span class="text-muted">02 Nov 2021 to 31 Dec 2021<i class="mdi mdi-chevron-down ms-1" /></span
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

		<CardBody>
			<div class="table-responsive table-card">
				<table class="table table-borderless table-hover table-nowrap align-middle mb-0">
					<thead class="table-light">
						<tr class="text-muted">
							<th scope="col">Name</th>
							<th scope="col" style="width: 20%">Last Contacted</th>
							<th scope="col">Sales Representative</th>
							<th scope="col" style="width: 16%">Status</th>
							<th scope="col" style="width: 12%">Deal Value</th>
						</tr>
					</thead>

					<tbody>
						{#each data.dealsStatus as item}
							<tr>
								<td>{item.name}</td>
								<td>{item.date}</td>
								<td
									><img src={item.img} alt="" class="avatar-xs rounded-circle me-2" />
									<a href="{null}" class="text-body fw-medium">{item.representativeName}</a></td
								>
								<td
									><span class={'badge bg-' + item.badgeClass + '-subtle text-'+item.badgeClass+ ' p-2'}>{item.status}</span
									></td
								>
								<td><div class="text-nowrap">{item.statusValue}</div></td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</CardBody>
	</Card>
</Col>
