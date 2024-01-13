<script>
	import { Card, CardBody, Col, Row } from "sveltestrap";
	import Flatpickr from "svelte-flatpickr";
	import Select from "svelte-select";
	import CryptoData from "../../../common/data/cryptoPage";
	import Link from "svelte-link";

	const ordeType = [
		{ value: "Active", label: "Active" },
		{ value: "Ended", label: "Ended" },
		{ value: "Upcoming", label: "Upcoming" },
	];
	const rating = [
		{ value: "Select Rating", label: "Select Rating" },
		{ value: "1", label: "1" },
		{ value: "2", label: "2" },
		{ value: "3", label: "3" },
		{ value: "4", label: "4" },
		{ value: "5", label: "5" },
	];
</script>

<Card>
	<CardBody>
		<Row class="g-3">
			<Col xxl={4} lg={6}>
				<div class="search-box">
					<input
						type="text"
						class="form-control"
						placeholder="Search to ICOs..."
					/>
					<i class="ri-search-line search-icon" />
				</div>
			</Col>
			<!--end col-->
			<Col xxl={3} lg={6}>
				<Flatpickr
					class="form-control"
					options={{
						dateFormat: "d M, Y",
					}}
					placeholder="Selact Date"
				/>
			</Col>
			<Col xxl={2} lg={4}>
				<div class="select-single">
					<Select
						class="form-control"
						name="choices-single-default2"
						id="choices-single-default2"
						items={ordeType}
					/>
				</div>
			</Col>
			<!--end col-->
			<Col xxl={2} lg={4}>
				<div class="select-single">
					<Select
						class="form-control"
						name="choices-single-default"
						id="choices-single-default"
						items={rating}
					/>
				</div>
			</Col>
			<!--end col-->
			<div class="col-xxl-1 col-lg-4">
				<button class="btn btn-primary w-100"
					><i class="ri-equalizer-line align-bottom me-1" /> Filters</button
				>
			</div>
		</Row>
		<!--end row-->
	</CardBody>
</Card>

<Row>
	{#each CryptoData.icoWidgetsList as item}
		{#if item.title == "Active ICOs"}
			<Col xxl={3} md={6}>
				<Card class="overflow-hidden">
					<CardBody class="bg-success-subtle">
						<h5 class="fs-17 text-center mb-0">{item.title}</h5>
					</CardBody>
				</Card>
				{#each item.subItem as subItem}
					<Card class="mb-2">
						<CardBody>
							<div class="d-flex mb-3">
								<div class="flex-shrink-0 avatar-sm">
									<div class="avatar-title bg-light rounded">
										<img
											src={subItem.img}
											alt=""
											class="avatar-xxs"
										/>
									</div>
								</div>
								<div class="flex-grow-1 ms-3">
									<h5 class="fs-15 mb-1">{subItem.label}</h5>
									<p class="text-muted mb-2">
										{subItem.caption}
									</p>
								</div>
								<div>
									<Link
										href={null}
										class="badge bg-primary-subtle text-primary"
										>Visit Website <i
											class="ri-arrow-right-up-line align-bottom"
										/></Link
									>
								</div>
							</div>
							<h6 class="text-muted mb-0">
								{subItem.amount}
								<span
									class="badge bg-success-subtle text-success"
									>89.97%</span
								>
							</h6>
						</CardBody>
						<CardBody class="border-top border-top-dashed">
							<div class="d-flex">
								<div class="flex-grow-1">
									<h6 class="mb-0">
										{subItem.rating}
										<i
											class="ri-star-fill align-bottom text-warning"
										/>
									</h6>
								</div>
								<h6
									class={"flex-shrink-0 text-" +
										subItem.dateClass +
										" mb-0"}
								>
									<i class="ri-time-line align-bottom" />
									{subItem.date}
								</h6>
							</div>
						</CardBody>
					</Card>
				{/each}
			</Col>
		{:else if item.title == "Ended ICOs"}
			<Col xxl={3} md={6}>
				<Card class="overflow-hidden">
					<CardBody class="bg-danger-subtle">
						<h5 class="fs-17 text-center mb-0">{item.title}</h5>
					</CardBody>
				</Card>
				{#each item.subItem as subItem}
					<Card class="mb-2">
						<CardBody>
							<div class="d-flex mb-3">
								<div class="flex-shrink-0 avatar-sm">
									<div class="avatar-title bg-light rounded">
										<img
											src={subItem.img}
											alt=""
											class="avatar-xxs"
										/>
									</div>
								</div>
								<div class="flex-grow-1 ms-3">
									<h5 class="fs-15 mb-1">{subItem.label}</h5>
									<p class="text-muted mb-2">
										{subItem.caption}
									</p>
								</div>
								<div>
									<Link
										href={null}
										class="badge bg-primary-subtle text-primary"
										>Visit Website <i
											class="ri-arrow-right-up-line align-bottom"
										/></Link
									>
								</div>
							</div>
							<h6 class="text-muted mb-0">
								{subItem.amount}
								<span
									class="badge bg-success-subtle text-success"
									>{subItem.percentage}</span
								>
							</h6>
						</CardBody>
						<CardBody class="border-top border-top-dashed">
							<div class="d-flex">
								<div class="flex-grow-1">
									<h6 class="mb-0">
										{subItem.rating}
										<i
											class="ri-star-fill align-bottom text-warning"
										/>
									</h6>
								</div>
								<h6
									class={"flex-shrink-0 text-" +
										subItem.dateClass +
										" mb-0"}
								>
									<i class="ri-time-line align-bottom" />
									{subItem.date}
								</h6>
							</div>
						</CardBody>
					</Card>
				{/each}
			</Col>
		{:else if item.title == "Upcoming ICOs"}
			<Col xxl={3} md={6}>
				<Card class="overflow-hidden">
					<CardBody class="bg-primary-subtle">
						<h5 class="fs-17 text-center mb-0">{item.title}</h5>
					</CardBody>
				</Card>
				{#each item.subItem as subItem}
					<Card class="mb-2">
						<CardBody>
							<div class="d-flex mb-3">
								<div class="flex-shrink-0 avatar-sm">
									<div class="avatar-title bg-light rounded">
										<img
											src={subItem.img}
											alt=""
											class="avatar-xxs"
										/>
									</div>
								</div>
								<div class="flex-grow-1 ms-3">
									<h5 class="fs-15 mb-1">{subItem.label}</h5>
									<p class="text-muted mb-2">
										{subItem.caption}
									</p>
								</div>
								<div>
									<Link
										href={null}
										class="badge bg-primary-subtle text-primary"
										>Visit Website <i
											class="ri-arrow-right-up-line align-bottom"
										/></Link
									>
								</div>
							</div>
							<h6 class="text-muted mb-0">
								{subItem.amount}
								{#if subItem.percentage}
									<span
										class="badge bg-success-subtle text-success"
										>{subItem.percentage}</span
									>
								{/if}
							</h6>
						</CardBody>
						<CardBody class="border-top border-top-dashed">
							<div class="d-flex">
								<div class="flex-grow-1">
									<h6 class="mb-0">
										{subItem.rating}
										<i
											class="ri-star-fill align-bottom text-warning"
										/>
									</h6>
								</div>
								<h6
									class={"flex-shrink-0 text-" +
										subItem.dateClass +
										" mb-0"}
								>
									<i class="ri-time-line align-bottom" />
									{subItem.date}
								</h6>
							</div>
						</CardBody>
					</Card>
				{/each}
			</Col>
		{:else if item.title == "Trading ICOs"}
			<Col xxl={3} md={6}>
				<Card class="overflow-hidden">
					<CardBody class="bg-info-subtle">
						<h5 class="fs-17 text-center mb-0">{item.title}</h5>
					</CardBody>
				</Card>
				{#each item.subItem as subItem}
					<Card class="mb-2 ribbon-box ribbon-fill right">
						<div class="ribbon ribbon-info shadow-none">
							<i
								class="ri-flashlight-fill me-1"
							/>{subItem.ribbonNumber}
						</div>
						<CardBody>
							<div class="d-flex mb-3">
								<div class="flex-shrink-0 avatar-sm">
									<div class="avatar-title bg-light rounded">
										<img
											src={subItem.img}
											alt=""
											class="avatar-xxs"
										/>
									</div>
								</div>
								<div class="flex-grow-1 ms-3">
									<h5 class="fs-15 mb-1">{subItem.label}</h5>
									<p class="text-muted mb-2">
										{subItem.caption}
									</p>
								</div>
								<div class="me-4">
									<Link
										href={null}
										class="badge bg-primary-subtle text-primary"
										>Visit Website <i
											class="ri-arrow-right-up-line align-bottom"
										/></Link
									>
								</div>
							</div>
							<h6 class="text-muted mb-0">
								{subItem.amount}
								<span
									class="badge bg-success-subtle text-success"
									>{subItem.percentage}</span
								>
							</h6>
						</CardBody>
						<CardBody class="border-top border-top-dashed">
							<div class="d-flex">
								<div class="flex-grow-1">
									<h6 class="mb-0">
										{subItem.rating}
										<i
											class="ri-star-fill align-bottom text-warning"
										/>
									</h6>
								</div>
								<h6
									class={"flex-shrink-0 text-" +
										subItem.dateClass +
										" mb-0"}
								>
									<i class="ri-time-line align-bottom" />
									{subItem.date}
								</h6>
							</div>
						</CardBody>
					</Card>
				{/each}
			</Col>
		{:else}
			{null}
		{/if}
	{/each}
</Row>
