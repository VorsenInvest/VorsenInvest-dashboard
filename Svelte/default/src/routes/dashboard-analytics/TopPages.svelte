<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Dropdown,
		DropdownItem,
		DropdownMenu,
		DropdownToggle
	} from 'sveltestrap';

	import data from '../../common/data/analytics';

</script>

<Col xl={4} md={6}>
	<Card class="card-height-100">
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Top Pages</h4>
			<div class="flex-shrink-0">
				<Dropdown class="card-header-dropdown">
					<DropdownToggle tag="div" color="" class="text-reset dropdown-btn p-0" role="button">
						<span class="text-muted fs-16"><i class="mdi mdi-dots-vertical align-middle" /></span>
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
		<CardBody>
			<div class="table-responsive table-card">
				<table class="table align-middle table-borderless table-centered table-nowrap mb-0">
					<thead class="text-muted table-light">
						<tr>
							<th scope="col" style="width: 62">Active Page</th>
							<th scope="col">Active</th>
							<th scope="col">Users</th>
						</tr>
					</thead>
					<tbody>
						{#each data.analytucsTopPages as item}
                        <tr>
                            <td>
                                <a href="{null}">{item.page}</a>
                            </td>
                            <td>{item.active}</td>
                            <td>{item.user}</td>
                        </tr>
                        {/each}
					</tbody>
				</table>
			</div>
		</CardBody>
	</Card>
</Col>
