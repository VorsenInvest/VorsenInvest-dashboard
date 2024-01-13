<script>
	import { Card, CardBody, Col, Row } from 'sveltestrap';
	import { UsersIcon, ActivityIcon, ClockIcon, ExternalLinkIcon } from 'svelte-feather-icons';
</script>

<Row>
	<Col md={6}>
	<Card class="card-animate">
		<CardBody>
			<div class="d-flex justify-content-between">
				<div>
					<p class="fw-medium text-muted mb-0">Users</p>
					<h2 class="mt-4 ff-secondary fw-semibold">
						<span class="counter-value" data-target="28.05">0</span>k
					</h2>
					<p class="mb-0 text-muted text-truncate">
						<span class="badge bg-light text-success mb-0">
							<i class="ri-arrow-up-line align-middle" /> 16.24 %
						</span> vs. previous month
					</p>
				</div>
				<div>
					<div class="avatar-sm flex-shrink-0">
						<span class="avatar-title bg-info-subtle rounded-circle fs-2">
							<UsersIcon class="text-info" size="24" />
						</span>
					</div>
				</div>
			</div>
		</CardBody>
	</Card>
	</Col>

	<Col md={6}>
	<Card class="card-animate">
		<CardBody>
			<div class="d-flex justify-content-between">
				<div>
					<p class="fw-medium text-muted mb-0">Sessions</p>
					<h2 class="mt-4 ff-secondary fw-semibold">
						<span class="counter-value" data-target="97.66">0</span>k
					</h2>
					<p class="mb-0 text-muted text-truncate">
						<span class="badge bg-light text-danger mb-0">
							<i class="ri-arrow-down-line align-middle" /> 3.96 %
						</span> vs. previous month
					</p>
				</div>
				<div>
					<div class="avatar-sm flex-shrink-0">
						<span class="avatar-title bg-info-subtle rounded-circle fs-2">
							<ActivityIcon class="text-info" size="24" />
						</span>
					</div>
				</div>
			</div>
		</CardBody>
	</Card>
	</Col>
</Row>

<Row>
	<Col md={6}>
	<Card class="card-animate">
		<CardBody>
			<div class="d-flex justify-content-between">
				<div>
					<p class="fw-medium text-muted mb-0">Avg. Visit Duration</p>
					<h2 class="mt-4 ff-secondary fw-semibold">
						<span class="counter-value" data-target="3">0</span>m
						<span class="counter-value" data-target="40">0</span>sec
					</h2>
					<p class="mb-0 text-muted text-truncate">
						<span class="badge bg-light text-danger mb-0">
							<i class="ri-arrow-down-line align-middle" /> 0.24 %
						</span> vs. previous month
					</p>
				</div>
				<div>
					<div class="avatar-sm flex-shrink-0">
						<span class="avatar-title bg-info-subtle rounded-circle fs-2">
							<ClockIcon class="text-info" size="24" />
						</span>
					</div>
				</div>
			</div>
		</CardBody>
	</Card>
	</Col>

	<Col md={6}>
	<Card class="card-animate">
		<CardBody>
			<div class="d-flex justify-content-between">
				<div>
					<p class="fw-medium text-muted mb-0">Bounce Rate</p>
					<h2 class="mt-4 ff-secondary fw-semibold">
						<span class="counter-value" data-target="33.48">0</span>%
					</h2>

					<p class="mb-0 text-muted text-truncate">
						<span class="badge bg-light text-success mb-0">
							<i class="ri-arrow-up-line align-middle" /> 7.05 %
						</span> vs. previous month
					</p>
				</div>
				<div>
					<div class="avatar-sm flex-shrink-0">
						<span class="avatar-title bg-info-subtle rounded-circle fs-2">
							<ExternalLinkIcon class="text-info" size="24" />
						</span>
					</div>
				</div>
			</div>
		</CardBody>
	</Card>
	</Col>
</Row>