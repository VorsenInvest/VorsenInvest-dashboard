<script>

	import { Col, Card, CardBody } from 'sveltestrap';
	import data from '../../common/data/dashboardEcommerce';

</script>

{#each data.ecomWidgets as item}
<Col xl={3} md={6}>
<Card class="card-animate">
	<CardBody>
		<div class="d-flex align-items-center">
			<div class="flex-grow-1 overflow-hidden">
				<p class="text-uppercase fw-medium text-muted text-truncate mb-0">{item.label}</p>
			</div>
			<div class="flex-shrink-0">
				<h5 class={'fs-14 mb-0 text-' + item.badgeClass}>
					{#if item.badge}
					<i class={'fs-13 align-middle ' + item.badge} />
							{/if}
							{item.percentage} %
						</h5>
					</div>
				</div>
				<div class="d-flex align-items-end justify-content-between mt-4">
					<div>
						<h4 class="fs-22 fw-semibold ff-secondary mb-4">
                            {item.prefix}<span class="counter-value" data-target={item.counter}>0</span>{item.suffix}
						</h4>
						<a href="{null}" class="text-decoration-underline link-secondary">{item.link}</a>
					</div>
					<div class="avatar-sm flex-shrink-0">
						<span class={' avatar-title rounded fs-3 bg-' + item.bgcolor+'-subtle'}>
						<i class={`text-${item.bgcolor} ${item.icon}`} />
						</span>
			</div>
		</div>
	</CardBody>
</Card>
</Col>
{/each}