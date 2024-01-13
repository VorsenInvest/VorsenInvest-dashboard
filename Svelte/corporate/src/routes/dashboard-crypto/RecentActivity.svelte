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
	import { ArrowDownCircleIcon, SendIcon, ArrowUpCircleIcon } from 'svelte-feather-icons';

</script>

<Col xxl={4} lg={5}>
	<Card class="card-height-100">
		<CardHeader class="card-header align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Recent Activity</h4>
			<div class="flex-shrink-0">
				<Dropdown class="card-header-dropdown">
					<DropdownToggle tag="a" class="text-reset dropdown-btn p-0" color="" role="button">
						<span class="fw-semibold text-uppercase fs-12">Sort by: </span><span class="text-muted">Current Week<i class="mdi mdi-chevron-down ms-1" /></span
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
		<CardBody class="p-0">
			<div data-simplebar style="height: 390px;">
				<div class="p-3">
					<h6 class="text-muted text-uppercase mb-3 fs-11">25 Dec 2021</h6>
					<div class="d-flex align-items-center">
						<div class="avatar-xs flex-shrink-0">
							<span class="avatar-title bg-light rounded-circle">
								<ArrowDownCircleIcon class="icon-dual-success icon-sm" />
							</span>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-14 mb-1">Bought Bitcoin</h6>
							<p class="text-muted fs-12 mb-0">
								<i class="mdi mdi-circle-medium text-success fs-15 align-middle" />
								Visa Debit Card ***6
							</p>
						</div>
						<div class="flex-shrink-0 text-end">
							<h6 class="mb-1 text-success">
								+0.04025745<span class="text-uppercase ms-1">Btc</span>
							</h6>
							<p class="text-muted fs-13 mb-0">+878.52 USD</p>
						</div>
					</div>
					<div class="d-flex align-items-center mt-3">
						<div class="avatar-xs flex-shrink-0">
							<span class="avatar-title bg-light rounded-circle">
								<SendIcon class="icon-dual-warning icon-sm" />
							</span>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-14 mb-1">Sent Ethereum</h6>
							<p class="text-muted fs-12 mb-0">
								<i class="mdi mdi-circle-medium text-warning fs-15 align-middle" />
								Sofia Cunha
							</p>
						</div>
						<div class="flex-shrink-0 text-end">
							<h6 class="mb-1 text-muted">
								-0.09025182<span class="text-uppercase ms-1">Eth</span>
							</h6>
							<p class="text-muted fs-13 mb-0">-659.35 USD</p>
						</div>
					</div>

					<h6 class="text-muted text-uppercase mb-3 mt-4 fs-11">24 Dec 2021</h6>
					<div class="d-flex align-items-center">
						<div class="avatar-xs flex-shrink-0">
							<span class="avatar-title bg-light rounded-circle">
								<ArrowUpCircleIcon class="icon-dual-danger icon-sm" />
							</span>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-14 mb-1">Sell Dash</h6>
							<p class="text-muted fs-12 mb-0">
								<i class="mdi mdi-circle-medium text-danger fs-15 align-middle" />
								www.cryptomarket.com
							</p>
						</div>
						<div class="flex-shrink-0 text-end">
							<h6 class="mb-1 text-danger">
								-98.6025422<span class="text-uppercase ms-1">Dash</span>
							</h6>
							<p class="text-muted fs-13 mb-0">-1508.98 USD</p>
						</div>
					</div>
					<div class="d-flex align-items-center mt-3">
						<div class="avatar-xs flex-shrink-0">
							<span class="avatar-title bg-light rounded-circle">
								<ArrowUpCircleIcon class="icon-dual-danger icon-sm" />
							</span>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-14 mb-1">Sell Dogecoin</h6>
							<p class="text-muted fs-12 mb-0">
								<i class="mdi mdi-circle-medium text-success fs-15 align-middle" />
								www.coinmarket.com
							</p>
						</div>
						<div class="flex-shrink-0 text-end">
							<h6 class="mb-1 text-danger">
								-1058.08025142<span class="text-uppercase ms-1">Doge</span>
							</h6>
							<p class="text-muted fs-13 mb-0">-89.36 USD</p>
						</div>
					</div>
					<div class="d-flex align-items-center mt-3">
						<div class="avatar-xs flex-shrink-0">
							<span class="avatar-title bg-light rounded-circle">
								<ArrowUpCircleIcon class="icon-dual-success icon-sm" />
							</span>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-14 mb-1">Bought Litecoin</h6>
							<p class="text-muted fs-12 mb-0">
								<i class="mdi mdi-circle-medium text-warning fs-15 align-middle" />
								Payment via Wallet
							</p>
						</div>
						<div class="flex-shrink-0 text-end">
							<h6 class="mb-1 text-success">
								+0.07225912<span class="text-uppercase ms-1">Ltc</span>
							</h6>
							<p class="text-muted fs-13 mb-0">+759.45 USD</p>
						</div>
					</div>

					<h6 class="text-muted text-uppercase mb-3 mt-4 fs-11">20 Dec 2021</h6>
					<div class="d-flex align-items-center">
						<div class="avatar-xs flex-shrink-0">
							<span class="avatar-title bg-light rounded-circle">
								<SendIcon class="icon-dual-warning icon-sm" />
							</span>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-14 mb-1">Sent Ethereum</h6>
							<p class="text-muted fs-12 mb-0">
								<i class="mdi mdi-circle-medium text-warning fs-15 align-middle" />
								Sofia Cunha
							</p>
						</div>
						<div class="flex-shrink-0 text-end">
							<h6 class="mb-1 text-muted">
								-0.09025182<span class="text-uppercase ms-1">Eth</span>
							</h6>
							<p class="text-muted fs-13 mb-0">-659.35 USD</p>
						</div>
					</div>

					<div class="d-flex align-items-center mt-3">
						<div class="avatar-xs flex-shrink-0">
							<span class="avatar-title bg-light rounded-circle">
								<ArrowDownCircleIcon class="icon-dual-success icon-sm" />
							</span>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-14 mb-1">Bought Bitcoin</h6>
							<p class="text-muted fs-12 mb-0">
								<i class="mdi mdi-circle-medium text-success fs-15 align-middle" />
								Visa Debit Card ***6
							</p>
						</div>
						<div class="flex-shrink-0 text-end">
							<h6 class="mb-1 text-success">
								+0.04025745<span class="text-uppercase ms-1">Btc</span>
							</h6>
							<p class="text-muted fs-13 mb-0">+878.52 USD</p>
						</div>
					</div>

					<div class="mt-3 text-center">
						<a href="{null}" class="text-muted text-decoration-underline">Load More</a>
					</div>
				</div>
			</div>
		</CardBody>
	</Card>
</Col>