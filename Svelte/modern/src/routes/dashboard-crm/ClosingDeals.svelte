<script>
	import { Card, CardBody, CardHeader, Col } from 'sveltestrap';
	import data from '../../common/data/dashboardcrm';
</script>

<Col xxl={7}>
	<Card class="card-height-100">
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Closing Deals</h4>
			<div class="flex-shrink-0">
				<select class="form-select form-select-sm">
					<option defaultValue="">Closed Deals</option>
					<option value="1">Active Deals</option>
					<option value="2">Paused Deals</option>
					<option value="3">Canceled Deals</option>
				</select>
			</div>
		</CardHeader>
		<CardBody>
			<div class="table-responsive">
				<table class="table table-bordered table-nowrap align-middle mb-0">
					<thead>
						<tr>
							<th scope="col" style="width: 30%">Deal Name</th>
							<th scope="col" style="width: 30%">Sales Rep</th>
							<th scope="col" style="width: 20%">Amount</th>
							<th scope="col" style="width: 20%">Close Date</th>
						</tr>
					</thead>

					<tbody>
						{#each data.closingDeals as item}
							<tr>
								<td>{item.dealName}</td>
								<td
									><img src={item.img} alt="" class="avatar-xs rounded-circle me-2" />
									<a href="{null}" class="text-body fw-medium">{item.salesRep}</a></td
								>
								<td>${item.amount}K</td>
								<td>{item.closeDate}</td>
							</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</CardBody>
	</Card>
</Col>
