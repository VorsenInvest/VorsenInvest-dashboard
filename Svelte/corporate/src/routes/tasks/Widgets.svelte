<script>
	import { Card, CardBody, Col } from 'sveltestrap';
	import Counter from '../../Components/Common/CounterPage.svelte';
	import Task from '../../common/data/taskList';
</script>

<Counter />

{#each Task.taskWidgets as item}
	<Col sm={6} xxl={3}>
		<Card class="card-animate">
			<CardBody>
				<div class="d-flex justify-content-between">
					<div>
						<p class="fw-medium text-muted mb-0">{item.label}</p>
						<h4 class="mt-4 ff-secondary fw-semibold">
							<span class="counter-value" data-target="{item.counter}">0</span>{item.suffix}
						</h4>
						<p class="mb-0 text-muted">
							<span class="badge bg-light text-{item.badgeClass} mb-0">
								<i class="{item.badge} align-middle" /> {item.percentage}
							</span> vs. previous month
						</p>
					</div>
					<div>
						<div class="avatar-sm flex-shrink-0">
							<span class="avatar-title bg-{item.iconClass}-subtle text-{item.iconClass} rounded-circle fs-4">
								<i class={item.icon} />
							</span>
						</div>
					</div>
				</div>
			</CardBody>
		</Card>
	</Col>
{/each}