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
	import data from '../../common/data/crypto';
</script>

<Col xl={8}>
<Card>
	<CardHeader class="align-items-center d-flex">
		<h4 class="card-title mb-0 flex-grow-1">My Currencies</h4>
		<div class="flex-shrink-0">
			<button class="btn btn-soft-primary btn-sm">24H</button>
		</div>
		<div class="flex-shrink-0 ms-2">
			<Dropdown class="card-header-dropdown dropdown-menu-end">
				<DropdownToggle class="btn btn-soft-primary btn-sm" color="" role="button" tag="a">
					Get Report<i class="mdi mdi-chevron-down align-middle ms-1" />
				</DropdownToggle>
				<DropdownMenu class="dropdown-menu dropdown-menu-end" end>
					<DropdownItem>Download Report</DropdownItem>
					<DropdownItem>Export</DropdownItem>
					<DropdownItem>Import</DropdownItem>
				</DropdownMenu>
			</Dropdown>
		</div>
	</CardHeader>
	<div class="card-body">
		<div class="table-responsive table-card">
			<table class="table table-hover table-borderless table-centered align-middle table-nowrap mb-0">
				<thead class="text-muted bg-light-subtle">
					<tr>
						<th>Coin Name</th>
						<th>Price</th>
						<th>24h Change</th>
						<th>Total Balance</th>
						<th>Total Coin</th>
						<th>Actions</th>
					</tr>
				</thead>
				<tbody>
					{#each data.currencies as item}
					<tr>
						<td>
							<div class="d-flex align-items-center">
								<div class="me-2">
									<img src={item.img} alt="" class="avatar-xxs" />
								</div>
								<div>
									<h6 class="fs-14 mb-0">{item.coinName}</h6>
								</div>
							</div>
						</td>
						<td>${item.price}</td>
						<td>
							<h6 class={'fs-13 mb-0 text-' + item.iconClass}>
								<i class={'align-middle me-1 ' + item.icon} />{item.change}
									</h6></td
								>
								<td>${item.balance}</td>
								<td>{item.totalCoin}</td>
								<td
									><a href="/crypto/buysell/apps-crypto-buy-sell" class="btn btn-sm btn-soft-primary">Trade</a
									></td
								>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>
	</Card>
</Col>