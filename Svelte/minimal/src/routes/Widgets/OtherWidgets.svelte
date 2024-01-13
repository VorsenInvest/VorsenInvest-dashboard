<script>
	import { Alert, Card, CardBody, Col, Row } from 'sveltestrap';
	import Link from 'svelte-link';
	export let otherWidgets2;
	import { AlertTriangleIcon } from 'svelte-feather-icons';
	import userillustarator from '../../assets/images/user-illustarator-2.png'
	import userillustarator1 from '../../assets/images/user-illustarator-1.png'
</script>

<Row>
	<Col class="col-12">
		<h5 class="text-decoration-underline mb-3 mt-2 pb-3">Other Widgets</h5>
	</Col>
</Row>

<Row>
	<Col xl={4}>
		<Card>
			<CardBody class="p-0">
				<Alert color="primary" class="border-0 rounded-top rounded-0 m-0 d-flex align-items-center">
					<AlertTriangleIcon class="text-primary me-2 icon-sm" />
					<div class="flex-grow-1 text-truncate">
						Your free trial expired in <b>17</b> days.
					</div>
					<div class="flex-shrink-0">
						<Link href="/pages/pricing/pages-pricing" class="text-reset text-decoration-underline"><b>Upgrade</b></Link>
					</div>
				</Alert>

				<Row class="align-items-end">
					<Col sm={8}>
						<div class="p-3">
							<p class="fs-16 lh-base">
								Upgrade your plan from a <span class="fw-semibold">Free trial</span>, to ‘Premium
								Plan’ <i class="mdi mdi-arrow-right" />
							</p>
							<div class="mt-3">
								<Link href="/pages/pricing/pages-pricing" class="btn btn-primary">Upgrade Account!</Link>
							</div>
						</div>
					</Col>
					<Col sm={4}>
						<div class="px-3">
							<img src={userillustarator} class="img-fluid" alt="" />
						</div>
					</Col>
				</Row>
			</CardBody>
		</Card>
	</Col>
	<Col xl={4}>
		<Card class="bg-primary">
			<CardBody class="p-0">
				<Alert
					color="success"
					class="rounded-top alert-solid alert-label-icon border-0 rounded-0 m-0 d-flex align-items-center"
				>
					<i class="ri-error-warning-line label-icon" />
					<div class="flex-grow-1 text-truncate">
						Your free trial expired in <b>17</b> days.
					</div>
					<div class="flex-shrink-0">
						<Link href="/pages/pricing/pages-pricing" class="text-reset text-decoration-underline"><b>Upgrade</b></Link
						>
					</div>
				</Alert>

				<Row class="align-items-end">
					<Col sm={8}>
						<div class="p-3">
							<p class="fs-16 lh-base text-white">
								Upgrade your plan from a <span class="fw-semibold">Free trial</span>, to ‘Premium
								Plan’ <i class="mdi mdi-arrow-right" />
							</p>
							<div class="mt-3">
								<Link href="/pages/pricing/pages-pricing" class="btn btn-info">Upgrade Account!</Link>
							</div>
						</div>
					</Col>
					<Col sm={4}>
						<div class="px-3">
							<img src={userillustarator1} class="img-fluid" alt="" />
						</div>
					</Col>
				</Row>
			</CardBody>
		</Card>
	</Col>

	<Col xl={4}>
		<Card>
			<CardBody class="p-0">
				<Alert color="primary" class="border-0 rounded-top rounded-0 m-0 d-flex align-items-center">
					<div class="flex-grow-1 text-truncate">
						We will choose a gift for you in <b>5</b> days.
					</div>
					<div class="flex-shrink-0">
						<Link href="/pages/pricing/pages-pricing" class="text-reset text-decoration-underline"><b>Get Free Gift</b></Link
						>
					</div>
				</Alert>
				<div class="d-flex p-3">
					<div class="flex-shrink-0">
						<div class="avatar-md me-3">
							<span class="avatar-title bg-primary-subtle rounded-circle fs-1">
								<i class="ri-gift-2-line text-primary" />
							</span>
						</div>
					</div>
					<div>
						<p class="fs-16 lh-base">
							Personalized <span class="fw-semibold">Gift Boxes</span>, with attitude, Let's collect
							your Xmas box <i class="mdi mdi-arrow-right" />
						</p>
						<div class="mt-3">
							<Link href="/pages/pricing/pages-pricing" class="btn btn-secondary">Get a Free Gift</Link>
						</div>
					</div>
				</div>
			</CardBody>
		</Card>
	</Col>
</Row>

<Row>
	{#each otherWidgets2 as item}
		<Col lg={4}>
			<Card>
				<CardBody>
					<h5 class="fs-15 fw-semibold">{item.title}</h5>
					<p class="text-muted">{item.subTitle}</p>
					<div class="d-flex flex-wrap justify-content-evenly">
						{#each item.subItem as item}
							<p class="text-muted mb-0">
								<i
									class={'fs-18 align-middle me-2 ' + item.icon + ' text-' + item.iconClass}
								/>{item.label}
							</p>
						{/each}
					</div>
				</CardBody>
				<div class="progress animated-progess rounded-bottom rounded-0" style="height: 6px">
					{#each item.progressBar as item}
						<div class={'progress-bar rounded-0 ' + item.bgColor}
							role="progressbar"
							style="width: {item.width}"
							aria-valuenow="30"
							aria-valuemin="0"
							aria-valuemax="100"
						/>
					{/each}
				</div>
			</Card>
		</Col>
	{/each}
</Row>
