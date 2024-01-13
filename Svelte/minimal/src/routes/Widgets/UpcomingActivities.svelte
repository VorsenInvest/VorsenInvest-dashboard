<script>
	import {
		Button,
		Card,
		CardBody,
		CardHeader,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		ListGroup,
		ListGroupItem,
		Pagination,
		PaginationItem,
		PaginationLink,
		Row,
		Dropdown,
		Label,
	} from "sveltestrap";
	import OtherWidgetsCharts from "./WidgetsCharts.svelte";
	import Link from "svelte-link";
	export let widgetsActivities, widgetsTasks;
	import avatar2 from "../../assets/images/users/avatar-2.jpg";
	import avatar3 from "../../assets/images/users/avatar-3.jpg";
	import img2 from "../../assets/images/products/img-2.png";
	import img8 from "../../assets/images/products/img-8.png";
	import img10 from "../../assets/images/products/img-10.png";

	const chartDataOptions = [
		{
			id: 1,
			title: "Application",
			persantage: "16.24",
			series: [
				{
					name: "Results",
					data: [0, 68, 35, 90, 99],
				},
			],
			dataColors: '["--vz-success" , "--vz-transparent"]',
		},
		{
			id: 2,
			title: "Interviewed",
			persantage: "34.24",
			series: [
				{
					name: "Results",
					data: [0, 98, 85, 90, 67],
				},
			],
			dataColors: '["--vz-danger" , "--vz-transparent"]',
		},
		{
			id: 3,
			title: "Hired",
			persantage: "6.67",
			series: [
				{
					name: "Results",
					data: [0, 65, 103, 75, 120],
				},
			],
			dataColors: '["--vz-success" , "--vz-transparent"]',
		},
	];
</script>

<Row>
	<Col xxl={5}>
		<Card class="card-height-100">
			<CardHeader class="align-items-center d-flex">
				<h4 class="card-title mb-0 flex-grow-1">Upcoming Activities</h4>
				<div class="flex-shrink-0">
					<Dropdown class="card-header-dropdown" direction="start">
						<DropdownToggle
							tag="a"
							class="text-reset dropdown-btn p-0"
							role="button"
							color=""
						>
							<span class="text-muted fs-18"
								><i class="mdi mdi-dots-vertical" /></span
							>
						</DropdownToggle>
						<DropdownMenu class="dropdown-menu-end">
							<DropdownItem>Edit</DropdownItem>
							<DropdownItem>Remove</DropdownItem>
						</DropdownMenu>
					</Dropdown>
				</div>
			</CardHeader>

			<CardBody class="pt-0">
				<ListGroup class="border-dashed" flush>
					{#each widgetsActivities as item}
						<ListGroupItem class="ps-0">
							<Row class="align-items-center g-3">
								<Col class="col-auto">
									<div
										class="avatar-sm p-1 py-2 h-auto bg-light rounded-3"
									>
										<div class="text-center">
											<h5 class="mb-0">{item.date}</h5>
											<div class="text-muted">
												{item.weekDay}
											</div>
										</div>
									</div>
								</Col>
								<Col class="col">
									<h5 class="text-muted mt-0 mb-1 fs-13">
										{item.time}
									</h5>
									<Link
										href={null}
										class="text-reset fs-14 mb-0"
										>{item.caption}</Link
									>
								</Col>
								<Col class="col-sm-auto">
									<div class="avatar-group">
										{#each item.subItem as item}
											{#if item.img}
												<div class="avatar-group-item">
													<Link
														href={null}
														class="d-inline-block"
														id={item.targetId}
													>
														<img
															src={item.img}
															alt=""
															class="rounded-circle avatar-xxs"
														/>
													</Link>
												</div>
											{:else}
												<div class="avatar-group-item">
													<Link href={null}>
														<div class="avatar-xxs">
															<span
																class={"avatar-title rounded-circle text-white " +
																	item.bgcolor}
															>
																{item.imgNumber}
															</span>
														</div>
													</Link>
												</div>
											{/if}
										{/each}
									</div>
								</Col>
							</Row>
						</ListGroupItem>
					{/each}
				</ListGroup>

				<Row class="align-items-center mt-2 text-center text-sm-start">
					<Col class="col-sm">
						<div class="text-muted">
							Showing<span class="fw-semibold">4</span> of
							<span class="fw-semibold">125</span> Results
						</div>
					</Col>
					<Col class="col-sm-auto">
						<Pagination
							size="sm"
							class="pagination-separated pagination-sm justify-content-center justify-content-sm-start mb-0"
						>
							<PaginationItem
								><PaginationLink href={null}>←</PaginationLink
								></PaginationItem
							>
							<PaginationItem
								><PaginationLink href={null}>1</PaginationLink
								></PaginationItem
							>
							<PaginationItem active
								><PaginationLink href={null}>2</PaginationLink
								></PaginationItem
							>
							<PaginationItem
								><PaginationLink href={null}>3</PaginationLink
								></PaginationItem
							>
							<PaginationItem
								><PaginationLink href={null}>→</PaginationLink
								></PaginationItem
							>
						</Pagination>
					</Col>
				</Row>
			</CardBody>
		</Card>
	</Col>
	<Col xxl={7}>
		<Row>
			<Col xl={6}>
				<Card class="card-height-100">
					<CardHeader class="align-items-center d-flex">
						<h4 class="card-title mb-0 flex-grow-1">My Tasks</h4>
						<div class="flex-shrink-0">
							<Dropdown class="card-header-dropdown">
								<DropdownToggle
									tag="a"
									class="text-reset dropdown-btn p-0"
									role="button"
									color=""
								>
									<span class="text-muted"
										><i
											class="ri-settings-4-line align-middle me-1 fs-15"
										/>Settings</span
									>
								</DropdownToggle>
								<DropdownMenu class="dropdown-menu-end">
									<DropdownItem>Edit</DropdownItem>
									<DropdownItem>Remove</DropdownItem>
								</DropdownMenu>
							</Dropdown>
						</div>
					</CardHeader>

					<CardBody class="p-0">
						<div
							class="align-items-center p-3 justify-content-between d-flex"
						>
							<div class="flex-shrink-0">
								<div class="text-muted">
									<span class="fw-semibold">4</span> of
									<span class="fw-semibold">10</span> remaining
								</div>
							</div>
							<Button color="primary" size="sm"
								><i class="ri-add-line align-middle me-1" /> Add
								Task</Button
							>
						</div>

						<div data-simplebar style="max-height: 257px;">
							<ListGroup class="border-dashed px-3" flush>
								{#each widgetsTasks as item}
									<ListGroupItem class="ps-0">
										<div class="d-flex align-items-start">
											<div
												class="form-check ps-0 flex-sharink-0"
											>
												<input
													type="checkbox"
													class="form-check-input ms-0"
													id={item.forId}
												/>
											</div>
											<div class="flex-grow-1">
												<Label
													class="form-check-label mb-0 ps-2"
													for={item.forId}
													>{item.text}</Label
												>
											</div>
											<div class="flex-shrink-0 ms-2">
												<p
													class="text-muted fs-12 mb-0"
												>
													{item.date}
												</p>
											</div>
										</div>
									</ListGroupItem>
								{/each}
							</ListGroup>
						</div>
						<div class="p-3">
							<Link
								href={null}
								class="text-muted text-decoration-underline"
								>Show more...</Link
							>
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col xl={6}>
				<Card class="card-height-100">
					<CardHeader
						class="border-bottom-dashed align-items-center d-flex"
					>
						<h4 class="card-title mb-0 flex-grow-1">
							Recent Activity
						</h4>
						<div class="flex-shrink-0">
							<button
								type="button"
								class="btn btn-soft-primary btn-sm"
							>
								View All Activity
							</button>
						</div>
					</CardHeader>
					<CardBody class="p-0">
						<div
							data-simplebar
							style="max-height: 364px;"
							class="p-3"
						>
							<div class="acitivity-timeline acitivity-main m-0">
								<div class="acitivity-item d-flex">
									<div
										class="flex-shrink-0 avatar-xs acitivity-avatar"
									>
										<div
											class="avatar-title bg-primary-subtle text-success rounded-circle"
										>
											<i
												class="ri-shopping-cart-2-line"
											/>
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1">
											Purchase by James Price
										</h6>
										<p class="text-muted mb-1">
											Product noise evolve smartwatch
										</p>
										<small class="mb-0 text-muted"
											>02:14 PM Today</small
										>
									</div>
								</div>
								<div class="acitivity-item py-3 d-flex">
									<div
										class="flex-shrink-0 avatar-xs acitivity-avatar"
									>
										<div
											class="avatar-title bg-primary-subtle text-primary rounded-circle"
										>
											<i class="ri-stack-fill" />
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1">
											Added new <span class="fw-semibold"
												>style collection</span
											>
										</h6>
										<p class="text-muted mb-1">
											By Nesta Technologies
										</p>
										<div
											class="d-inline-flex gap-2 border border-dashed p-2 mb-2 w-75"
										>
											<Link
												href="/ecommerce/apps-ecommerce-product-details"
												class="bg-light rounded p-1"
											>
												<img
													src={img8}
													alt=""
													class="img-fluid d-block"
												/>
											</Link>
											<Link
												href="/ecommerce/apps-ecommerce-product-details"
												class="bg-light rounded p-1"
											>
												<img
													src={img2}
													alt=""
													class="img-fluid d-block"
												/>
											</Link>
											<Link
												href="/ecommerce/apps-ecommerce-product-details"
												class="bg-light rounded p-1"
											>
												<img
													src={img10}
													alt=""
													class="img-fluid d-block"
												/>
											</Link>
										</div>
										<p class="mb-0 text-muted">
											<small>9:47 PM Yesterday</small>
										</p>
									</div>
								</div>
								<div class="acitivity-item py-3 d-flex">
									<div class="flex-shrink-0">
										<img
											src={avatar2}
											alt=""
											class="avatar-xs rounded-circle acitivity-avatar"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1">
											Natasha Carey have liked the
											products
										</h6>
										<p class="text-muted mb-1">
											Allow users to like products in your
											WooCommerce store.
										</p>
										<small class="mb-0 text-muted"
											>25 Dec, 2021</small
										>
									</div>
								</div>
								<div class="acitivity-item py-3 d-flex">
									<div class="flex-shrink-0">
										<div class="avatar-xs acitivity-avatar">
											<div
												class="avatar-title rounded-circle bg-secondary"
											>
												<i class="mdi mdi-sale fs-14" />
											</div>
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1">
											Today offers by <Link
												href="/ecommerce/apps-ecommerce-seller-details"
												class="link-secondary"
												>Digitech Galaxy</Link
											>
										</h6>
										<p class="text-muted mb-2">
											Offer is valid on orders of Rs.500
											Or above for selected products only.
										</p>
										<small class="mb-0 text-muted"
											>12 Dec, 2021</small
										>
									</div>
								</div>
								<div class="acitivity-item py-3 d-flex">
									<div class="flex-shrink-0">
										<div class="avatar-xs acitivity-avatar">
											<div
												class="avatar-title rounded-circle bg-danger-subtle text-danger"
											>
												<i class="ri-bookmark-fill" />
											</div>
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1">Favoried Product</h6>
										<p class="text-muted mb-2">
											Esther James have favorited product.
										</p>
										<small class="mb-0 text-muted"
											>25 Nov, 2021</small
										>
									</div>
								</div>
								<div class="acitivity-item py-3 d-flex">
									<div class="flex-shrink-0">
										<div class="avatar-xs acitivity-avatar">
											<div
												class="avatar-title rounded-circle bg-secondary"
											>
												<i class="mdi mdi-sale fs-14" />
											</div>
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1">
											Flash sale starting <span
												class="text-primary"
												>Tomorrow.</span
											>
										</h6>
										<p class="text-muted mb-0">
											Flash sale by <Link
												href={null}
												class="link-secondary fw-medium"
												>Zoetic Fashion</Link
											>
										</p>
										<small class="mb-0 text-muted"
											>22 Oct, 2021</small
										>
									</div>
								</div>
								<div class="acitivity-item py-3 d-flex">
									<div class="flex-shrink-0">
										<div class="avatar-xs acitivity-avatar">
											<div
												class="avatar-title rounded-circle bg-info-subtle text-info"
											>
												<i class="ri-line-chart-line" />
											</div>
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1">
											Monthly sales report
										</h6>
										<p class="text-muted mb-2">
											<span class="text-danger"
												>2 days left</span
											>
											notification to submit the monthly
											sales report. <Link
												href={null}
												class="link-warning text-decoration-underline"
												>Reports Builder</Link
											>
										</p>
										<small class="mb-0 text-muted"
											>15 Oct</small
										>
									</div>
								</div>
								<div class="acitivity-item d-flex">
									<div class="flex-shrink-0">
										<img
											src={avatar3}
											alt=""
											class="avatar-xs rounded-circle acitivity-avatar"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1">
											Frank Hook Commented
										</h6>
										<p class="text-muted mb-2 fst-italic">
											" A product that has reviews is more
											likable to be sold than a product. "
										</p>
										<small class="mb-0 text-muted"
											>26 Aug, 2021</small
										>
									</div>
								</div>
							</div>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Col>
</Row>
<Row>
	{#each chartDataOptions as item}
		<Col xl={4} md={6}>
			<Card class="card-height-100">
				<div class="d-flex">
					<div class="flex-grow-1 p-3">
						<h5 class="mb-3">{item.title}</h5>
						<p class="mb-0 text-muted">
							<span class="badge bg-light text-success mb-0">
								<i class="ri-arrow-up-line align-middle" />
								{item.persantage} %
							</span> vs. previous month
						</p>
					</div>
					<div>
						<OtherWidgetsCharts
							dataColors={item.dataColors}
							id={item.id}
							seriesData={item.series}
						/>
					</div>
				</div>
			</Card>
		</Col>
	{/each}
</Row>
