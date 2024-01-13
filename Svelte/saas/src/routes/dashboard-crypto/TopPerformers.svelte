<script>
	import { Card, CardBody, CardHeader, Col } from 'sveltestrap';
	import data from '../../common/data/crypto';
</script>

<Col xxl={4} lg={6}>
	<Card class="card-height-100">
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Top Performers</h4>
			<div>
				<button type="button" class="btn btn-soft-info btn-sm"> 1H </button>
				<button type="button" class="btn btn-soft-info btn-sm"> 1D </button>
				<button type="button" class="btn btn-soft-info btn-sm"> 7D </button>
				<button type="button" class="btn btn-soft-primary btn-sm"> 1M </button>
			</div>
		</CardHeader>
		<CardBody class="p-0">
			<ul class="list-group list-group-flush border-dashed mb-0">
				{#each data.topPerformers as item}
					<li class="list-group-item d-flex align-items-center">
						<div class="flex-shrink-0">
							<img src={item.img} class="avatar-xs" alt="" />
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-13 mb-1">{item.coinName}</h6>
							<p class="text-muted mb-0">${item.marketCap} Billions</p>
						</div>
						<div class="flex-shrink-0 text-end">
							<h6 class="fs-13 mb-1">${item.price}</h6>
							<p class={'fs-12 mb-0 text-' + item.textColor}>{item.change} ({item.percentage})</p>
						</div>
					</li>
				{/each}
			</ul>
		</CardBody>
	</Card>
</Col>
