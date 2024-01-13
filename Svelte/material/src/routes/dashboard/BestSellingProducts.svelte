<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Dropdown,
	} from "sveltestrap";
	import data from "../../common/data/dashboardEcommerce";
</script>

<Col xl={6}>
<Card>
	<CardHeader class="align-items-center d-flex">
		<h4 class="card-title mb-0 flex-grow-1">Best Selling Products</h4>
		<div class="flex-shrink-0">
			<Dropdown class="card-header-dropdown">
				<DropdownToggle tag="a" color="" class="text-reset p-0 shadow-none" role="button">
					<span class="fw-semibold text-uppercase fs-12">Sort by:
					</span><span class="text-muted">Today<i class="mdi mdi-chevron-down ms-1" /></span>
				</DropdownToggle>
				<DropdownMenu class="dropdown-menu-end" end>
					<DropdownItem>Today</DropdownItem>
					<DropdownItem>Yesterday</DropdownItem>
					<DropdownItem>Last 7 Days</DropdownItem>
					<DropdownItem>Last 30 Days</DropdownItem>
					<DropdownItem>This Month</DropdownItem>
					<DropdownItem>Last Month</DropdownItem>
				</DropdownMenu>
			</Dropdown>
		</div>
	</CardHeader>

	<CardBody>
		<div class="table-responsive table-card">
			<table class="table table-hover table-centered align-middle table-nowrap mb-0">
				<tbody>
					{#each data.bestSellingProducts as item}
					<tr>
						<td>
							<div class="d-flex align-items-center">
								<div class="avatar-sm bg-light rounded p-1 me-2">
									<img src={item.img} alt="" class="img-fluid d-block" />
								</div>
								<div>
									<h5 class="fs-14 my-1">
										<a href="/ecommerce/apps-ecommerce-product-details"
											class="text-reset">{item.label}</a>
									</h5>
									<span class="text-muted">{item.date}</span>
								</div>
							</div>
						</td>
						<td>
							<h5 class="fs-14 my-1 fw-normal">
								${item.price}
							</h5>
							<span class="text-muted">Price</span>
						</td>
						<td>
							<h5 class="fs-14 my-1 fw-normal">
								{item.orders}
							</h5>
							<span class="text-muted">Orders</span>
						</td>
						<td>
							<h5 class="fs-14 my-1 fw-normal">
								{#if item.stock}
								{item.stock}
								{:else}
								<span class="badge bg-danger-subtle text-danger">Out of stock</span>
								{/if}
							</h5>
							<span class="text-muted">Stock</span>
						</td>
						<td>
							<h5 class="fs-14 my-1 fw-normal">
								${item.amount}
							</h5>
							<span class="text-muted">Amount</span>
						</td>
					</tr>
					{/each}
				</tbody>
			</table>
		</div>

		<div class="align-items-center mt-4 pt-2 justify-content-between d-flex">
			<div class="flex-shrink-0">
				<div class="text-muted">
					Showing <span class="fw-semibold">5</span> of <span class="fw-semibold">25</span> Results
				</div>
			</div>
			<ul class="pagination pagination-separated pagination-sm mb-0">
				<li class="page-item disabled">
					<a href="!#" class="page-link">←</a>
				</li>
				<li class="page-item">
					<a href="!#" class="page-link">1</a>
				</li>
				<li class="page-item active">
					<a href="!#" class="page-link">2</a>
				</li>
				<li class="page-item">
					<a href="!#" class="page-link">3</a>
				</li>
				<li class="page-item">
					<a href="!#" class="page-link">→</a>
				</li>
			</ul>
		</div>
	</CardBody>
</Card>
</Col>