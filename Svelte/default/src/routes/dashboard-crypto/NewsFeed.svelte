<script>
	import { Card, CardBody, CardHeader, Col } from 'sveltestrap';
	import data from '../../common/data/crypto';
</script>

<Col xxl={4}>
	<Card>
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">News Feed</h4>
			<div>
				<button type="button" class="btn btn-soft-primary btn-sm"> View all </button>
			</div>
		</CardHeader>

		<CardBody>
			{#each data.newsFeed as item}
				<div class={item.id === 1 ? 'd-flex align-middle' : 'd-flex mt-4'}>
					<div class="flex-shrink-0">
						<img src={item.img} class="rounded img-fluid" style='height: 60px' alt="" />
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1 lh-base"><a href="{null}" class="text-reset">{item.caption}</a></h6>
						<p class="text-muted fs-12 mb-0">
							{item.date} <i class="mdi mdi-circle-medium align-middle mx-1" />{item.time}
						</p>
					</div>
				</div>
			{/each}
			<div class="mt-3 text-center">
				<a href="{null}" class="text-muted text-decoration-underline">View all News</a>
			</div>
		</CardBody>
	</Card>
</Col>
