<script>
	import {
		Card,
		CardBody,
		Col,
		Row,
		Dropdown,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
	} from "sveltestrap";
	import Link from "svelte-link";
	import Counter from "../../Components/Common/CounterPage.svelte";
	import {
		UsersIcon,
		ActivityIcon,
		ClockIcon,
		ExternalLinkIcon,
	} from "svelte-feather-icons";
	export let WidgetData;
</script>

<Counter />
<Row>
	<Col class="col-12">
		<h5 class="text-decoration-underline mb-3 pb-1">Tile Boxs</h5>
	</Col>
</Row>

<Row>
	{#each WidgetData.tileBoxs1 as item}
		<Col xl={3} md={6}>
			<Card class={"card-animate " + item.bgColor}>
				<CardBody>
					<div class="d-flex align-items-center">
						<div class="flex-grow-1">
							<p
								class={"text-uppercase fw-medium mb-0 text-" +
									item.labelClass}
							>
								{item.label}
							</p>
						</div>
						<div class="flex-shrink-0">
							<h5
								class={"fs-14 mb-0 text-" +
									item.percentageClass}
							>
								<i
									class={"fs-13 align-middle " +
										item.percentageIcon}
								/>
								{item.percentage}
							</h5>
						</div>
					</div>
					<div
						class="d-flex align-items-end justify-content-between mt-4"
					>
						<div>
							<h4
								class="fs-22 fw-secondary ff-secondary mb-4 {item.counterClass}"
							>
								{item.prefix}<span
									class="counter-value"
									data-target={item.counter}>0</span
								>{item.suffix}
							</h4>
							<Link
								href={null}
								class={"text-decoration-underline " +
									item.captionClass}>{item.caption}</Link
							>
						</div>
						<div class="avatar-sm flex-shrink-0">
							<span
								class={item.iconClass == "white"
									? "avatar-title rounded fs-3 bg-" +
									  item.iconClass +
									  " bg-opacity-25"
									: "avatar-title rounded fs-3 bg-" +
									  item.iconClass +
									  "-subtle"}
							>
								<i
									class={item.icon +
										" text-" +
										item.iconClass}
								/>
							</span>
						</div>
					</div>
				</CardBody>
			</Card>
		</Col>
	{/each}
</Row>

<Row>
	<Col xl={12}>
		<Card class="crm-widget">
			<CardBody class="p-0">
				<Row class="row-cols-md-3 row-cols-1">
					{#each WidgetData.tileBoxs2 as item}
						<Col
							class={item.id === 4
								? "col-lg"
								: "col-lg border-end"}
						>
							<div class="mt-3 mt-md-0 py-4 px-3">
								<h5 class="text-muted text-uppercase fs-14">
									{item.label}
									<i
										class={"fs-18 float-end align-middle " +
											item.badge}
									/>
								</h5>
								<div class="d-flex align-items-center">
									<div class="flex-shrink-0">
										<i
											class={"display-6 text-muted " +
												item.icon}
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										<h2 class="mb-0">
											{item.prefix}<span
												class="counter-value"
												data-target={item.counter}
												>0</span
											>{item.suffix}
										</h2>
									</div>
								</div>
							</div>
						</Col>
					{/each}
				</Row>
			</CardBody>
		</Card>
	</Col>
</Row>

<Row>
	{#each WidgetData.tileBoxs3 as item}
		<Col xl={3} md={6}>
			<Card class={"card-animate " + item.bgColor}>
				<CardBody>
					<div class="d-flex justify-content-between">
						<div>
							<p
								class={"fw-semibold mb-0 text-" +
									item.labelClass}
							>
								{item.label}
							</p>
							<h2
								class={"mt-4 ff-secondary fw-secondary " +
									item.counterClass}
							>
								{#each item.subCounter as item}
									{item.prefix}<span
										class="counter-value"
										data-target={item.counter}>0</span
									>{item.suffix}
								{/each}
							</h2>
							<p class={"mb-0 text-" + item.labelClass}>
								<span class={"mb-0 badge " + item.badgeClass}>
									<i class={"align-middle " + item.badge} />
									{item.percentage}
								</span> vs. previous month
							</p>
						</div>
						<div>
							<div class="avatar-sm flex-shrink-0">
								<span
									class={item.iconClass == "white"
										? "avatar-title rounded-circle fs-2 bg-" +
										  item.iconClass +
										  " bg-opacity-25"
										: "avatar-title rounded-circle fs-2 bg-" +
										  item.iconClass +
										  "-subtle"}
								>
									{#if item.feaIcon === "activity"}
										<ActivityIcon
											class={"text-" + item.iconClass}
											size="24"
										/>
									{:else if item.feaIcon === "clock"}
										<ClockIcon
											class={"text-" + item.iconClass}
											size="24"
										/>
									{:else if item.feaIcon === "external-link"}
										<ExternalLinkIcon
											class={"text-" + item.iconClass}
											size="24"
										/>
									{:else}
										<UsersIcon
											class={"text-" + item.iconClass}
											size="24"
										/>
									{/if}
								</span>
							</div>
						</div>
					</div>
				</CardBody>
			</Card>
		</Col>
	{/each}
</Row>

<Row>
	{#each WidgetData.tileBoxes4 as item}
		<Col xl={3} md={6}>
			<Card class={"card-height-100 " + item.bgColor}>
				<CardBody>
					<div class="d-flex align-items-center">
						<div class="avatar-sm flex-shrink-0">
							<span
								class={"avatar-title rounded-2 fs-2 bg-" +item.iconClass +"-subtle text-" +item.iconClass}>
								<i class={item.icon} />
							</span>
						</div>
						<div class="flex-grow-1 ms-3">
							<p
								class={"text-uppercase fw-semibold mb-3 text-" +
									item.labelClass}
							>
								{item.label}
							</p>
							<h4 class={"fs-4 mb-3 " + item.counterClass}>
								{item.prefix}<span
									class="counter-value"
									data-target={item.counter}>0</span
								>{item.suffix}
							</h4>
							<p class={"mb-0 text-" + item.captionClass}>
								{item.caption}
							</p>
						</div>
						<div class="flex-shrink-0 align-self-center">
							<span
								class={"fs-12 badge badge-soft-" +
									item.percentageClass}
								><i
									class={"fs-13 align-middle me-1 " +
										item.badge}
								/>{item.percentage}<span /></span
							>
						</div>
					</div>
				</CardBody>
			</Card>
		</Col>
	{/each}
</Row>
<Row>
	{#each WidgetData.tileBoxes5 as item}
		<Col xl={3} ms={6}>
			<Card class={"card-height-100 " + item.class}>
				<CardBody>
					<Dropdown class="float-end">
						<DropdownToggle
							tag="a"
							class="text-reset dropdown-btn p-0"
							href={null}
							color=""
						>
							<span class="text-muted fs-18"
								><i class="mdi mdi-dots-vertical" /></span
							>
						</DropdownToggle>
						<DropdownMenu class="dropdown-menu-end">
							<DropdownItem>Favorite</DropdownItem>
							<DropdownItem>Apply Now</DropdownItem>
						</DropdownMenu>
					</Dropdown>
					<div class="mb-4 pb-2">
						<img src={item.img} alt="" class="avatar-sm" />
					</div>
					<Link href={null}>
						<h6 class="fs-15 fw-bold">
							{item.title}
							<span class="text-muted fs-13">{item.year}</span>
						</h6>
					</Link>
					<p class="text-muted mb-0">
						<i class="ri-building-line align-bottom" /> Themesbrand
						<span class="ms-2"
							><i class="ri-map-pin-2-line align-bottom" /> California</span
						>
					</p>
				</CardBody>
			</Card>
		</Col>
	{/each}
</Row>
