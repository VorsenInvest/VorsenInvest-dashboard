<script>
	import { Card, CardBody, CardHeader, Col } from 'sveltestrap';
	import data from '../../common/data/dashboardEcommerce';
</script>

<Col xl={8}>
<Card>
	<CardHeader class="align-items-center d-flex">
		<h4 class="card-title mb-0 flex-grow-1">Recent Orders</h4>
		<div class="flex-shrink-0">
			<button type="button" class="btn btn-soft-info btn-sm shadow-none">
				<i class="ri-file-list-3-line align-middle" /> Generate Report
			</button>
		</div>
	</CardHeader>

	<CardBody>
		<div class="table-responsive table-card">
			<table class="table table-borderless table-centered align-middle table-nowrap mb-0">
				<thead class="text-muted table-light">
					<tr>
						<th scope="col">Order ID</th>
						<th scope="col">Customer</th>
						<th scope="col">Product</th>
						<th scope="col">Amount</th>
						<th scope="col">Vendor</th>
						<th scope="col">Status</th>
						<th scope="col">Rating</th>
					</tr>
				</thead>
				<tbody>
					{#each data.recentOrders as item}
					<tr>
						<td>
							<a href="/ecommerce/apps-ecommerce-order-details"
								class="fw-medium link-primary">{item.orderId}</a>
						</td>
						<td>
							<div class="d-flex align-items-center">
								<div class="flex-shrink-0 me-2">
									<img src={item.img} alt="" class="avatar-xs rounded-circle shadow" />
								</div>
								<div class="flex-grow-1">{item.name}</div>
							</div>
						</td>
						<td>{item.product}</td>
						<td>
							<span class="text-success">${item.amount}</span>
						</td>
						<td>{item.vendor}</td>
						<td>
							<span class={'badge bg-' + item.statusClass+'-subtle text-' + item.statusClass}>{item.status}</span>
						</td>
						<td>
							<h5 class="fs-14 fw-medium mb-0">
								{item.rating}<span class="text-muted fs-11 ms-1">({item.votes} votes)</span>
							</h5>
						</td>
					</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</CardBody>
</Card>
</Col>