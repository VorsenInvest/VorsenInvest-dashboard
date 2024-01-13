<script>
	import { Card, CardBody, Col } from 'sveltestrap';
	import data from '../../common/data/crypto';
</script>

{#each data.cyptoWidgets as item}
	<Col lg={4} md={6}>
		<Card>
			<CardBody>
				<div class="d-flex align-items-center">
					<div class="avatar-sm flex-shrink-0">
						<span class="avatar-title bg-light text-primary  rounded-circle fs-3">
							<i class={'align-middle ' + item.icon} />
						</span>
					</div>
					<div class="flex-grow-1 ms-3">
						<p class="text-uppercase fw-semibold fs-12 text-muted mb-1">{item.label}</p>

						<h4 class=" mb-0">
							{item.prefix}<span class="counter-value" data-target={item.counter}>0</span>
						</h4>
					</div>
					<div class="flex-shrink-0 align-self-end">
						<span class={'badge bg-' + item.badgeColor+'-subtle text-'+ item.textColor}><i class={'align-middle me-1 ' + item.badge} />{item.percentage} %<span /></span
						>
					</div>
				</div>
			</CardBody>
		</Card>
	</Col>
{/each}
