<script>
	export let deal, index;
	import { Card, CardBody, Collapse, CardFooter, Button } from "sveltestrap";
	import Link from "svelte-link";
</script>

<div class="col">
	<Card>
		<Link
			href={null}
			class={"card-header bg-" + deal.bgColor+"-subtle"}
			id={"leadDiscovered" + index}
		>
			<h5 class="card-title text-uppercase fw-semibold mb-1 fs-15">
				{deal.title}
			</h5>
			<p class="text-muted mb-0">
				{deal.price}{" "}
				<span class="fw-medium">{deal.deals} Deals</span>
			</p>
		</Link>
	</Card>
	<Collapse toggler={"#leadDiscovered" + index} isOpen={true}>
		{#each deal.subItems as subitem, subitemkey}
			<Card
				class={subitem.isRibbon
					? "mb-1 ribbon-box ribbon-fill ribbon-sm"
					: "mb-1"}
			>
				{#if subitem.isRibbon}
					<div class="ribbon ribbon-info">
						<i class="ri-flashlight-fill" />
					</div>
				{/if}
				<CardBody>
					<Link
						href={null}
						class="d-flex align-items-center"
						id={"leadInnerDiscovered" + index + subitemkey}>
						<div class="flex-shrink-0">
							<img
								src={subitem.img}
								alt=""
								class="avatar-xs rounded-circle material-shadow"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="fs-14 mb-1">{subitem.title}</h6>
							<p class="text-muted mb-0">
								{subitem.price} - {subitem.date}
							</p>
						</div>
					</Link>
				</CardBody>
				<Collapse
					class="border-top border-top-dashed"
					toggler={"#leadInnerDiscovered" + index + subitemkey}
					isOpen={subitem.isOpen === true ? true : false}
				>
					<CardBody>
						<h6 class="fs-14 mb-1">
							{subitem.subTitle}{" "}
							<small
								class={"badge bg-" +
									subitem.timeDurationClass+'-subtle text-' + subitem.timeDurationClass}>
								{subitem.timeDuration}
							</small>
						</h6>
						<p class="text-muted">
							As a company grows however, you find it's not as
							easy to shout across
						</p>
						<ul class="list-unstyled vstack gap-2 mb-0">
							<li>
								<div class="d-flex">
									<div class="flex-shrink-0 avatar-xxs text-muted"
									>
										<i class="ri-question-answer-line" />
									</div>
									<div class="flex-grow-1">
										<h6 class="mb-0">
											Meeting with Thomas
										</h6>
										<small class="text-muted">
											Yesterday at 9:12AM
										</small>
									</div>
								</div>
							</li>
							<li>
								<div class="d-flex">
									<div class="flex-shrink-0 avatar-xxs text-muted"
									>
										<i class="ri-mac-line" />
									</div>
									<div class="flex-grow-1">
										<h6 class="mb-0">Product Demo</h6>
										<small class="text-muted">
											Monday at 04:41PM
										</small>
									</div>
								</div>
							</li>
							<li>
								<div class="d-flex">
									<div class="flex-shrink-0 avatar-xxs text-muted"
									>
										<i class="ri-earth-line" />
									</div>
									<div class="flex-grow-1">
										<h6 class="mb-0">
											Marketing Team Meeting
										</h6>
										<small class="text-muted">
											Monday at 04:41PM
										</small>
									</div>
								</div>
							</li>
						</ul>
					</CardBody>
					<CardFooter class="hstack gap-2">
						<Button color="warning" class="btn-sm w-100">
							<i class="ri-phone-line align-bottom me-1" /> Call
						</Button>
						<Button color="info" class="btn-sm w-100">
							<i
								class="ri-question-answer-line align-bottom me-1"
							/>{" "}
							Message
						</Button>
					</CardFooter>
				</Collapse>
			</Card>
		{/each}
	</Collapse>
</div>