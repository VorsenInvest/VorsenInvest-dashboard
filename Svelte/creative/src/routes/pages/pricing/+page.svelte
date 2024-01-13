<svelte:head>
  <title>Pricing | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import {
		Card,
		CardBody,
		Col,
		Container,
		Nav,
		NavItem,
		NavLink,
		Row,
	} from 'sveltestrap';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import Link from 'svelte-link';

	const pricing1 = [
		{
			id: 1,
			type: 'Starter',
			rate: 19,
			description: 'The perfect way to get started and get used to our tools.',
			projects: 3,
			Customers: 299,
			FTP: 5,
			supportClass: 'danger',
			supportClassSymbol: 'close',
			storageClass: 'danger',
			storageClassSymbol: 'close',
			domainClass: 'danger',
			domainClassSymbol: 'close',
			ribbon: false,
			planButtonClassname: 'danger',
			btntxt: 'Your Current Plan',
			btnstatus: ' disabled ',
			rateYear: '171',
			delrateYear: '228'
		},
		{
			id: 2,
			type: 'Professional',
			rate: 29,
			description: 'Excellent for scalling teams to build culture. Special plan for professional business.',
			projects: 8,
			Customers: 499,
			FTP: 7,
			supportClass: 'success',
			supportClassSymbol: 'checkbox',
			storageClass: 'danger',
			storageClassSymbol: 'close',
			domainClass: 'danger',
			domainClassSymbol: 'close',
			ribbon: false,
			planButtonClassname: 'info',
			btntxt: 'Change Plan',
			rateYear: '261',
			delrateYear: '348'
		},
		{
			id: 3,
			type: 'Enterprise',
			rate: 39,
			description: 'This plan is for those who have a team alredy and running a large business.',
			projects: 15,
			Customers: 'Unlimited',
			FTP: 12,
			supportClass: 'success',
			supportClassSymbol: 'checkbox',
			storageClass: 'success',
			storageClassSymbol: 'checkbox',
			domainClass: 'danger',
			domainClassSymbol: 'close',
			ribbon: true,
			planButtonClassname: 'info',
			btntxt: 'Change Plan',
			rateYear: '351',
			delrateYear: '468'
		},
		{
			id: 4,
			type: 'Unlimited',
			rate: 49,
			description: 'For most businesses that want to optimize web queries.',
			projects: 'Unlimited',
			Customers: 'Unlimited',
			FTP: 'Unlimited ',
			supportClass: 'success',
			supportClassSymbol: 'checkbox',
			storageClass: 'success',
			storageClassSymbol: 'checkbox',
			domainClass: 'success',
			domainClassSymbol: 'checkbox',
			ribbon: false,
			planButtonClassname: 'info',
			btntxt: 'Change Plan',
			rateYear: '441',
			delrateYear: '588'
		}
	];

	const pricing2 = [
		{
			id: 1,
			type: 'Basic Plan',
			purpose: 'For Startup',
			planIcon: 'ri-book-mark-line',
			rate: 19,
			projects: 3,
			Customers: 299,
			FTP: 5,
			supportClass: 'danger',
			supportClassSymbol: 'close',
			storageClass: 'danger',
			storageClassSymbol: 'close',
			domainClass: 'danger',
			domainClassSymbol: 'close',
			ribbon: false,
			planButtonClassname: 'soft-success',
			icon: 'ri-book-mark-line',
			btntxt: 'Sign up free'
		},
		{
			id: 2,
			type: 'Pro Business',
			purpose: 'Professional plans',
			planIcon: 'ri-medal-line',
			rate: 29,
			projects: 15,
			Customers: 'unlimited',
			FTP: 12,
			supportClass: 'success',
			supportClassSymbol: 'checkbox',
			storageClass: 'danger',
			storageClassSymbol: 'close',
			domainClass: 'danger',
			domainClassSymbol: 'close',
			ribbon: true,
			planButtonClassname: 'success',
			icon: 'ri-medal-line',
			btntxt: 'Get started'
		},
		{
			id: 3,
			type: 'Platinum Plan',
			purpose: 'Enterprise Businesses',
			planIcon: 'ri-stack-line',
			rate: 39,
			projects: 'unlimited',
			Customers: 'unlimited',
			FTP: 'unlimited',
			supportClass: 'success',
			supportClassSymbol: 'checkbox',
			storageClass: 'success',
			storageClassSymbol: 'checkbox',
			domainClass: 'success',
			domainClassSymbol: 'checkbox',
			ribbon: false,
			planButtonClassname: 'soft-success',
			icon: 'ri-stack-line',
			btntxt: 'Get started'
		}
	];

	const pricing3 = [
		{
			id: 1,
			type: 'Starter',
			purpose: 'Starter plans',
			rate: 22,
			users: 1,
			storage: '01',
			domain: 'No',
			support: 'No',
			ribbon: false
		},
		{
			id: 2,
			type: 'Professional',
			purpose: 'Professional plans',
			rate: 29,
			users: 3,
			storage: '10',
			domain: 'Yes',
			support: 'No',
			ribbon: true
		},
		{
			id: 3,
			type: 'Enterprise',
			purpose: 'Enterprise plans',
			rate: 39,
			users: 3,
			storage: '20',
			domain: 'Yes',
			support: 'Yes',
			ribbon: true
		},
		{
			id: 4,
			type: 'Unlimited',
			purpose: 'Unlimited plans',
			rate: 49,
			users: 5,
			storage: '40',
			domain: 'Yes',
			support: 'Yes',
			ribbon: false
		}
	];

	let activeTab = 1;

	function changepricingTable(active) {
		activeTab = active;
	}
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Pricing" pageTitle="Pages" />

		<Row class="justify-content-center mt-4">
			<Col lg={5}>
				<div class="text-center mb-4">
					<h4 class="fw-bold fs-22">Plans & Pricing</h4>
					<p class="text-muted mb-4 fs-15">
						Simple pricing. No hidden fees. Advanced features for you business.
					</p>

					<div class="d-inline-flex">
						<Nav class="nav-pills arrow-navtabs plan-nav rounded mb-3 p-1" id="pills-tab">
							<NavItem>
								<NavLink
									class="fw-semibold"
									id="month-tab"
									on:click={() => changepricingTable(1)}
									active={activeTab == 1}
									aria-selected="true">Monthly</NavLink
								>
							</NavItem>
							<NavItem>
								<NavLink
									class="fw-semibold"
									id="annual-tab"
									on:click={() => changepricingTable(2)}
									active={activeTab == 2}
									aria-selected="false"
									>Annually <span class="badge bg-success">25% Off</span></NavLink
								>
							</NavItem>
						</Nav>
					</div>
				</div>
			</Col>
		</Row>

		<Row>
			{#each pricing1 as price1}
				<Col xxl={3} lg={6}>
					<Card class={price1.ribbon === true ? "pricing-box ribbon-box right" : "pricing-box"}>
						{#if price1.ribbon === true}
							<div class="ribbon-two ribbon-two-danger">
								<span>Popular</span>
							</div>
						{/if}
						<CardBody class="bg-light m-2 p-4">
							<div class="d-flex align-items-center mb-3">
								<div class="flex-grow-1">
									<h5 class="mb-0 fw-bold">{price1.type}</h5>
								</div>
								<div class="ms-auto">
									{#if activeTab == 1}
										<h2 class="month mb-0">
											${price1.rate} <small class="fs-13 text-muted">/Month</small>
										</h2>
									{:else}
										<h2 class="annual mb-0">
											<small class="fs-16"><del>${price1.delrateYear}</del></small>
											${price1.rateYear}
											<small class="fs-13 text-muted">/Year</small>
										</h2>
									{/if}
								</div>
							</div>

							<p class="text-muted">{price1.description}</p>
							<ul class="list-unstyled vstack gap-3">
								<li>
									<div class="d-flex">
										<div class="flex-shrink-0 text-success me-1">
											<i class="ri-checkbox-circle-fill fs-15 align-middle" />
										</div>
										<div class="flex-grow-1">
											<b>{price1.projects}</b> Projects
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<div class="flex-shrink-0 text-success me-1">
											<i class="ri-checkbox-circle-fill fs-15 align-middle" />
										</div>
										<div class="flex-grow-1">
											<b>{price1.Customers}</b> Customers
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<div class="flex-shrink-0 text-success me-1">
											<i class="ri-checkbox-circle-fill fs-15 align-middle" />
										</div>
										<div class="flex-grow-1">Scalable Bandwidth</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<div class="flex-shrink-0 text-success me-1">
											<i class="ri-checkbox-circle-fill fs-15 align-middle" />
										</div>
										<div class="flex-grow-1">
											<b>{price1.FTP}</b> FTP Login
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<div class="flex-shrink-0 text-{price1.supportClass} me-1">
											<i class="ri-{price1.supportClassSymbol}-circle-fill fs-15 align-middle" />
										</div>
										<div class="flex-grow-1">
											<b>24/7</b> Support
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<div class="flex-shrink-0 text-{price1.storageClass} me-1">
											<i class="ri-{price1.storageClassSymbol}-circle-fill fs-15 align-middle" />
										</div>
										<div class="flex-grow-1">
											<b>Unlimited</b> Storage
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<div class="flex-shrink-0 text-{price1.domainClass} me-1">
											<i class="ri-{price1.domainClassSymbol}-circle-fill fs-15 align-middle" />
										</div>
										<div class="flex-grow-1">Domain</div>
									</div>
								</li>
							</ul>
							<div class="mt-3 pt-2">
								<Link
									href="{null}"
									class="btn btn-{price1.planButtonClassname} {price1.btnstatus} w-100"
									>{price1.btntxt}</Link
								>
							</div>
						</CardBody>
					</Card>
				</Col>
			{/each}
		</Row>

		<Row class="justify-content-center mt-5">
			<Col lg={5}>
				<div class="text-center mb-4 pb-2">
					<h4 class="fw-bold fs-22">Choose the plan that's right for you</h4>
					<p class="text-muted mb-4 fs-15">
						Simple pricing. No hidden fees. Advanced features for you business.
					</p>
				</div>
			</Col>
		</Row>

		<Row class="justify-content-center">
			<Col xl={9}>
				<Row>
					{#each pricing2 as price2}
						<Col lg={4}>
							<Card class={price2.ribbon === true ? "pricing-box ribbon-box right" : "pricing-box"}>
								{#if price2.ribbon === true}<div class="ribbon-two ribbon-two-danger">
										<span>Popular</span>
									</div>{/if}
								<CardBody class="p-4 m-2">
									<div class="d-flex align-items-center">
										<div class="flex-grow-1">
											<h5 class="mb-1 fw-bold">{price2.type}</h5>
											<p class="text-muted mb-0">{price2.purpose}</p>
										</div>
										<div class="avatar-sm">
											<div class="avatar-title bg-light rounded-circle text-primary">
												<i class="{price2.icon} fs-20" />
											</div>
										</div>
									</div>
									<div class="pt-4">
										<h2>
											<sup><small>$</small></sup>{price2.rate}
											<span class="fs-14 text-muted">/Month</span>
										</h2>
									</div>
									<hr class="my-4 text-muted" />
									<div>
										<ul class="list-unstyled text-muted vstack gap-3">
											<li>
												<div class="d-flex">
													<div class="flex-shrink-0 text-success me-1">
														<i class="ri-checkbox-circle-fill fs-15 align-middle" />
													</div>
													<div class="flex-grow-1">
														Upto <b>{price2.projects}</b> Projects
													</div>
												</div>
											</li>
											<li>
												<div class="d-flex">
													<div class="flex-shrink-0 text-success me-1">
														<i class="ri-checkbox-circle-fill fs-15 align-middle" />
													</div>
													<div class="flex-grow-1">
														Upto <b>{price2.Customers}</b> Customers
													</div>
												</div>
											</li>
											<li>
												<div class="d-flex">
													<div class="flex-shrink-0 text-success me-1">
														<i class="ri-checkbox-circle-fill fs-15 align-middle" />
													</div>
													<div class="flex-grow-1">Scalable Bandwidth</div>
												</div>
											</li>
											<li>
												<div class="d-flex">
													<div class="flex-shrink-0 text-success me-1">
														<i class="ri-checkbox-circle-fill fs-15 align-middle" />
													</div>
													<div class="flex-grow-1">
														<b>{price2.FTP}</b> FTP Login
													</div>
												</div>
											</li>
											<li>
												<div class="d-flex">
													<div class="flex-shrink-0 text-{price2.supportClass} me-1">
														<i
															class="ri-{price2.supportClassSymbol}-circle-fill fs-15 align-middle"
														/>
													</div>
													<div class="flex-grow-1">
														<b>24/7</b> Support
													</div>
												</div>
											</li>
											<li>
												<div class="d-flex">
													<div class="flex-shrink-0 text-{price2.storageClass} me-1">
														<i
															class="ri-{price2.storageClassSymbol}-circle-fill fs-15 align-middle"
														/>
													</div>
													<div class="flex-grow-1">
														<b>Unlimited</b> Storage
													</div>
												</div>
											</li>
											<li>
												<div class="d-flex">
													<div class="flex-shrink-0 text-{price2.domainClass} me-1">
														<i
															class="ri-{price2.domainClassSymbol}-circle-fill fs-15 align-middle"
														/>
													</div>
													<div class="flex-grow-1">Domain</div>
												</div>
											</li>
										</ul>
										<div class="mt-4">
											<a
												href="{null}"
												class="btn btn-{price2.planButtonClassname} w-100 waves-effect waves-light"
												>{price2.btntxt}</a
											>
										</div>
									</div>
								</CardBody>
							</Card>
						</Col>
					{/each}
				</Row>
			</Col>
		</Row>

		<Row class="justify-content-center mt-5">
			<div class="col-lg-4">
				<div class="text-center mb-4 pb-2">
					<h4 class="fw-bold fs-22">Simple Pricing Plan</h4>
					<p class="text-muted mb-4 fs-15">
						Simple pricing. No hidden fees. Advanced features for you business.
					</p>
				</div>
			</div>
		</Row>

		<Row>
			{#each pricing3 as price3}
				<Col lg={6}>
					<Card class={price3.ribbon === true ? "pricing-box text-center ribbon-box ribbon-fill" : "pricing-box text-center"}>
						{#if price3.ribbon == true}
							<div class="ribbon ribbon-primary">New</div>{/if}
						<Row class="g-0">
							<Col lg={6}>
								<CardBody class="h-100">
									<div>
										<h5 class="mb-1">{price3.type}</h5>
										<p class="text-muted">{price3.purpose}</p>
									</div>

									<div class="py-4">
										<h2>
											<sup><small>$</small></sup>{price3.rate}
											<span class="fs-13 text-muted"> /Per month</span>
										</h2>
									</div>

									<div class="text-center plan-btn mt-2">
										<a href="{null}" class="btn btn-success w-sm waves-effect waves-light">Sign up</a>
									</div>
								</CardBody>
							</Col>

							<Col lg={6}>
								<CardBody class="border-start mt-4 mt-lg-0">
									<div class="card-header bg-light">
										<h5 class="fs-15 mb-0">Plan Features:</h5>
									</div>
									<CardBody class="pb-0">
										<ul class="list-unstyled vstack gap-3 mb-0">
											<li>Users: <span class="text-success fw-semibold">{price3.users}</span></li>
											<li>
												Storage: <span class="text-success fw-semibold">{price3.storage} GB</span>
											</li>
											<li>Domain: <span class="text-success fw-semibold">{price3.domain}</span></li>
											<li>
												Support: <span class="text-success fw-semibold">{price3.support}</span>
											</li>
										</ul>
									</CardBody>
								</CardBody>
							</Col>
						</Row>
					</Card>
				</Col>
			{/each}
		</Row>
	</Container>
</div>
