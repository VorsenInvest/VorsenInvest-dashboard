<script>
	import {
		Button,
		Card,
		CardBody,
		Col,
		Container,
		Row,
		Popover,
		Tooltip,
		Spinner,
		Pagination,
		PaginationItem,
		PaginationLink,
		Breadcrumb,
		BreadcrumbItem,
	} from "sveltestrap";

	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";

	// Popovers

	const popoversCode = `
<!-- Popovers -->
<div class="hstack flex-wrap gap-2">
	<Button color="light" id="PopoverTop"
		>Popover on top</Button
	>
	<Popover
		placement="top"
		target="PopoverTop"
		title="Top Popover"
	>
		Vivamus sagittis lacus vel augue laoreet
		rutrum faucibus.
	</Popover>
	<Button color="light" id="PopoverRight"
		>Popover on right</Button
	>
	<Popover
		placement="right"
		target="PopoverRight"
		title="Right Popover"
	>
		Vivamus sagittis lacus vel augue laoreet
		rutrum faucibus.
	</Popover>

	<Button color="light" id="PopoverBottom"
		>Popover on right</Button
	>
	<Popover
		placement="bottom"
		target="PopoverBottom"
		title="Bottom Popover"
	>
		Vivamus sagittis lacus vel augue laoreet
		rutrum faucibus.
	</Popover>

	<Button color="light" id="PopoverLeft"
		>Popover on right</Button
	>
	<Popover
		placement="left"
		target="PopoverLeft"
		title="Left Popover"
	>
		Vivamus sagittis lacus vel augue laoreet
		rutrum faucibus.
	</Popover>

	<Button color="success" id="PopoverDismissible"
		>Dismissible popover</Button
	>
	<Popover
		placement="right"
		target="PopoverDismissible"
		title="Dismissible popover"
	>
		And here's some amazing content. It's very
		engaging. Right?
	</Popover>
</div>
`;

	// Tooltips
	const tooltipsCode = `
<!-- Tooltips -->
<div class="hstack flex-wrap gap-2">
	<Button color="light" id="tooltipTop"
		>Tooltip on top</Button
	>
	<Tooltip placement="top" target="tooltipTop"
		>Tooltip on top</Tooltip
	>

	<Button color="light" id="tooltipRight"
		>Tooltip on right</Button
	>
	<Tooltip placement="right" target="tooltipRight"
		>Tooltip on right</Tooltip
	>

	<Button color="light" id="tooltipBottom"
		>Tooltip on bottom</Button
	>
	<Tooltip
		placement="bottom"
		target="tooltipBottom"
		>Tooltip on bottom</Tooltip
	>

	<Button color="light" id="tooltipLeft"
		>Tooltip on left</Button
	>
	<Tooltip placement="left" target="tooltipLeft"
		>Tooltip on left</Tooltip
	>

	<Button color="primary" id="tooltipwithHtml"
		>Tooltip with HTML</Button
	>
	<Tooltip
		placement="top"
		target="tooltipwithHtml"
	>
		<em>Tooltip</em> <u>with</u> <b>HTML</b>
	</Tooltip>
</div>
`;

	// Breadcrumb
	const breadcrumbCode = `
<Breadcrumb listClassName="p-3 py-2 bg-light">
	<BreadcrumbItem active>Home</BreadcrumbItem>
</Breadcrumb>

<Breadcrumb listClassName="p-3 py-2 bg-light">
	<BreadcrumbItem
		><Link href={null}>Home</Link></BreadcrumbItem
	>
	<BreadcrumbItem active>Library</BreadcrumbItem>
</Breadcrumb>

<Breadcrumb listClassName="p-3 py-2 bg-light">
	<BreadcrumbItem
		><Link href={null}>Home</Link></BreadcrumbItem
	>
	<BreadcrumbItem
		><Link href={null}>Base UI</Link
		></BreadcrumbItem
	>
	<BreadcrumbItem active>General</BreadcrumbItem>
</Breadcrumb>

<Breadcrumb listClassName="p-3 py-2 bg-light mb-0">
	<BreadcrumbItem
		><Link href={null}
			><i class="ri-home-5-fill" /></Link
		></BreadcrumbItem
	>
	<BreadcrumbItem
		><Link href={null}>Base UI</Link
		></BreadcrumbItem
	>
	<BreadcrumbItem active>General</BreadcrumbItem>
</Breadcrumb>
`;

	// Pagination
	const paginationCode = `
<Pagination class="mb-3">
	<PaginationItem>
		<PaginationLink href={null}
			>Previous</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>2</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>Next</PaginationLink
		></PaginationItem
	>
</Pagination>

<Pagination class="mb-3">
	<PaginationItem>
		<PaginationLink href={null}
			>← &nbsp; Prev</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>2</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem>
		<PaginationLink href={null}
			>Next &nbsp; →</PaginationLink
		>
	</PaginationItem>
</Pagination>


<!-- Pagination Disabled & Active -->
<Pagination class="mb-3">
	<PaginationItem disabled>
		<PaginationLink href={null}
			>← &nbsp; Prev</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem active>
		<PaginationLink href={null}
			>2</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem>
		<PaginationLink href={null}
			>Next &nbsp; →</PaginationLink
		>
	</PaginationItem>
</Pagination>

<Pagination class="mb-3">
	<PaginationItem disabled>
		<PaginationLink href={null}
			><i
				class="mdi mdi-chevron-left"
			/></PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem active>
		<PaginationLink href={null}
			>2</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem>
		<PaginationLink href={null}
			><i
				class="mdi mdi-chevron-right"
			/></PaginationLink
		>
	</PaginationItem>
</Pagination>


<!-- Pagination sizing -->

<!-- Pagination Large -->
<Pagination size="lg">
	<PaginationItem disabled>
		<PaginationLink href={null}
			>← &nbsp; Prev</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>2</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem>
		<PaginationLink href={null}
			>Next &nbsp; →</PaginationLink
		>
	</PaginationItem>
</Pagination>

<Pagination size="sm">
	<PaginationItem disabled>
		<PaginationLink href={null}
			>← &nbsp; Prev</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>2</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem>
		<PaginationLink href={null}
			>Next &nbsp; →</PaginationLink
		>
	</PaginationItem>
</Pagination>


<!-- Pagination Alignment -->

<!-- Center Alignment -->
<Pagination
	listClassName="justify-content-center"
>
	<PaginationItem disabled>
		<PaginationLink href={null}
			>← &nbsp; Prev</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>2</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem>
		<PaginationLink href={null}
			>Next &nbsp; →</PaginationLink
		>
	</PaginationItem>
</Pagination>

<Pagination
	listClassName="justify-content-end"
>
	<PaginationItem disabled>
		<PaginationLink href={null}
			>← &nbsp; Prev</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>2</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem>
		<PaginationLink href={null}
			>Next &nbsp; →</PaginationLink
		>
	</PaginationItem>
</Pagination>

<!-- Pagination Custom -->
<Pagination
	class="pagination-lg pagination-separated"
>
	<PaginationItem disabled>
		<PaginationLink href={null}
			>←</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem active>
		<PaginationLink href={null}
			>2</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>4</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>5</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>→</PaginationLink
		></PaginationItem
	>
</Pagination>

<Pagination
	class="pagination-separated"
>
	<PaginationItem disabled>
		<PaginationLink href={null}
			>←</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem active>
		<PaginationLink href={null}
			>2</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>4</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>5</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>→</PaginationLink
		></PaginationItem
	>
</Pagination>

<Pagination
	class="pagination-sm pagination-separated"
>
	<PaginationItem disabled>
		<PaginationLink href={null}
			>←</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem active>
		<PaginationLink href={null}
			>2</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>4</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>5</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>→</PaginationLink
		></PaginationItem
	>
</Pagination>

<!-- Pagination Rounded -->
<Pagination
	class="pagination-lg pagination-rounded"
>
	<PaginationItem disabled>
		<PaginationLink href={null}
			>←</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem active>
		<PaginationLink href={null}
			>2</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>4</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>5</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>→</PaginationLink
		></PaginationItem
	>
</Pagination>

<Pagination class="pagination-rounded">
	<PaginationItem disabled>
		<PaginationLink href={null}
			>←</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem active>
		<PaginationLink href={null}
			>2</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>4</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>5</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>→</PaginationLink
		></PaginationItem
	>
</Pagination>

<Pagination
	class="pagination-sm pagination-rounded"
>
	<PaginationItem disabled>
		<PaginationLink href={null}
			>←</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>1</PaginationLink
		></PaginationItem
	>
	<PaginationItem active>
		<PaginationLink href={null}
			>2</PaginationLink
		>
	</PaginationItem>
	<PaginationItem
		><PaginationLink href={null}
			>3</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>4</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>5</PaginationLink
		></PaginationItem
	>
	<PaginationItem
		><PaginationLink href={null}
			>→</PaginationLink
		></PaginationItem
	>
</Pagination>
`;

	// Spinners
	const spinnersCode = `
<!-- Border spinner -->

<Spinner color="primary"> Loading... </Spinner>

<Spinner color="secondary"> Loading... </Spinner>

<Spinner color="success"> Loading... </Spinner>

<Spinner color="info"> Loading... </Spinner>

<Spinner color="warning"> Loading... </Spinner>

<Spinner color="danger"> Loading... </Spinner>

<Spinner color="dark"> Loading... </Spinner>

<Spinner color="light"> Loading... </Spinner>


<!-- Growing spinner -->

<Spinner color="primary" type="grow" > Loading... </Spinner>

<Spinner color="secondary" type="grow" > Loading... </Spinner>

<Spinner color="success" type="grow" > Loading... </Spinner>

<Spinner color="info" type="grow" > Loading... </Spinner>

<Spinner color="warning" type="grow" > Loading... </Spinner>

<Spinner color="danger" type="grow" > Loading... </Spinner>

<Spinner color="dark" type="grow" > Loading... </Spinner>

<Spinner color="light" type="grow" > Loading... </Spinner>
`;
</script>

<svelte:head>
	<title>General | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="General" pageTitle="Base UI" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Popovers" />
					<CardBody>
						<p class="text-muted">
							Popovers example are available with follwing options
							, Directions are mirrored when using Bootstrap in
							RTL.
						</p>
						<div class="live-preview">
							<div class="hstack flex-wrap gap-2">
								<Button color="light" id="PopoverTop"
									>Popover on top</Button
								>
								<Popover
									placement="top"
									target="PopoverTop"
									title="Top Popover"
								>
									Vivamus sagittis lacus vel augue laoreet
									rutrum faucibus.
								</Popover>
								<Button color="light" id="PopoverRight"
									>Popover on right</Button
								>
								<Popover
									placement="right"
									target="PopoverRight"
									title="Right Popover"
								>
									Vivamus sagittis lacus vel augue laoreet
									rutrum faucibus.
								</Popover>

								<Button color="light" id="PopoverBottom"
									>Popover on bottom</Button
								>
								<Popover
									placement="bottom"
									target="PopoverBottom"
									title="Bottom Popover"
								>
									Vivamus sagittis lacus vel augue laoreet
									rutrum faucibus.
								</Popover>

								<Button color="light" id="PopoverLeft"
									>Popover on left</Button
								>
								<Popover
									placement="left"
									target="PopoverLeft"
									title="Left Popover"
								>
									Vivamus sagittis lacus vel augue laoreet
									rutrum faucibus.
								</Popover>

								<Button color="success" id="PopoverDismissible"
									>Dismissible popover</Button
								>
								<Popover
									placement="right"
									target="PopoverDismissible"
									title="Dismissible popover"
								>
									And here's some amazing content. It's very
									engaging. Right?
								</Popover>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={popoversCode}
								id="popoversCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Tooltips" />

					<CardBody>
						<p class="text-muted">
							Tooltip example are available with follwing options,
							Directions are mirrored when using Bootstrap in RTL.
						</p>
						<div class="live-preview">
							<div class="hstack flex-wrap gap-2">
								<Button color="light" id="tooltipTop"
									>Tooltip on top</Button
								>
								<Tooltip placement="top" target="tooltipTop"
									>Tooltip on top</Tooltip
								>

								<Button color="light" id="tooltipRight"
									>Tooltip on right</Button
								>
								<Tooltip placement="right" target="tooltipRight"
									>Tooltip on right</Tooltip
								>

								<Button color="light" id="tooltipBottom"
									>Tooltip on bottom</Button
								>
								<Tooltip
									placement="bottom"
									target="tooltipBottom"
									>Tooltip on bottom</Tooltip
								>

								<Button color="light" id="tooltipLeft"
									>Tooltip on left</Button
								>
								<Tooltip placement="left" target="tooltipLeft"
									>Tooltip on left</Tooltip
								>

								<Button color="primary" id="tooltipwithHtml"
									>Tooltip with HTML</Button
								>
								<Tooltip
									placement="top"
									target="tooltipwithHtml"
								>
									<em>Tooltip</em> <u>with</u> <b>HTML</b>
								</Tooltip>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={tooltipsCode}
								id="tooltipsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Breadcrumb" />

					<CardBody>
						<p class="text-muted">
							Indicate the current page’s location within a
							navigational hierarchy
						</p>
						<div class="live-preview">
							<Breadcrumb listClassName="p-3 py-2 bg-light">
								<BreadcrumbItem active>Home</BreadcrumbItem>
							</Breadcrumb>

							<Breadcrumb listClassName="p-3 py-2 bg-light">
								<BreadcrumbItem
									><Link href={null}>Home</Link></BreadcrumbItem
								>
								<BreadcrumbItem active>Library</BreadcrumbItem>
							</Breadcrumb>

							<Breadcrumb listClassName="p-3 py-2 bg-light">
								<BreadcrumbItem
									><Link href={null}>Home</Link></BreadcrumbItem
								>
								<BreadcrumbItem
									><Link href={null}>Base UI</Link
									></BreadcrumbItem
								>
								<BreadcrumbItem active>General</BreadcrumbItem>
							</Breadcrumb>

							<Breadcrumb listClassName="p-3 py-2 bg-light mb-0">
								<BreadcrumbItem
									><Link href={null}
										><i class="ri-home-5-fill" /></Link
									></BreadcrumbItem
								>
								<BreadcrumbItem
									><Link href={null}>Base UI</Link
									></BreadcrumbItem
								>
								<BreadcrumbItem active>General</BreadcrumbItem>
							</Breadcrumb>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={breadcrumbCode}
								id="breadcrumbCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Pagination" />

					<CardBody>
						<div class="live-preview">
							<Row>
								<Col lg={6}>
									<h5 class="fs-15">Default Pagination</h5>
									<p class="text-muted">
										Use <code>Pagination</code> attribute to
										ul element to indicate a series of related
										content exists across multiple pages.
									</p>
									<Pagination class="mb-3">
										<PaginationItem>
											<PaginationLink href={null}
												>Previous</PaginationLink
											>
										</PaginationItem>
										<PaginationItem
											><PaginationLink href={null}
												>1</PaginationLink
											></PaginationItem
										>
										<PaginationItem
											><PaginationLink href={null}
												>2</PaginationLink
											></PaginationItem
										>
										<PaginationItem
											><PaginationLink href={null}
												>3</PaginationLink
											></PaginationItem
										>
										<PaginationItem
											><PaginationLink href={null}
												>Next</PaginationLink
											></PaginationItem
										>
									</Pagination>

									<Pagination class="mb-3">
										<PaginationItem>
											<PaginationLink href={null}
												>← &nbsp; Prev</PaginationLink
											>
										</PaginationItem>
										<PaginationItem
											><PaginationLink href={null}
												>1</PaginationLink
											></PaginationItem
										>
										<PaginationItem
											><PaginationLink href={null}
												>2</PaginationLink
											></PaginationItem
										>
										<PaginationItem
											><PaginationLink href={null}
												>3</PaginationLink
											></PaginationItem
										>
										<PaginationItem>
											<PaginationLink href={null}
												>Next &nbsp; →</PaginationLink
											>
										</PaginationItem>
									</Pagination>
								</Col>

								<Col lg={6}>
									<div class="mt-4 mt-lg-0">
										<h5 class="fs-15">
											Disabled and Active states
										</h5>
										<p class="text-muted">
											Use <code>disabled</code> attribute
											to PaginationItem to links that
											appear un-clickable and
											<code>active</code> class to indicate
											the current page.
										</p>
										<Pagination class="mb-3">
											<PaginationItem disabled>
												<PaginationLink href={null}
													>← &nbsp; Prev</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem active>
												<PaginationLink href={null}
													>2</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem>
												<PaginationLink href={null}
													>Next &nbsp; →</PaginationLink
												>
											</PaginationItem>
										</Pagination>

										<Pagination class="mb-3">
											<PaginationItem disabled>
												<PaginationLink href={null}
													><i
														class="mdi mdi-chevron-left"
													/></PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem active>
												<PaginationLink href={null}
													>2</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem>
												<PaginationLink href={null}
													><i
														class="mdi mdi-chevron-right"
													/></PaginationLink
												>
											</PaginationItem>
										</Pagination>
									</div>
								</Col>
							</Row>

							<Row>
								<Col lg={6}>
									<div class="mt-4">
										<h5 class="fs-15">Sizing</h5>
										<p class="text-muted">
											Use <code>pagination-lg</code> or
											<code>pagination-sm</code> to set different
											pagination sizes.
										</p>

										<Pagination class="mb-3" size="lg">
											<PaginationItem disabled>
												<PaginationLink href={null}
													>← &nbsp; Prev</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>2</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem>
												<PaginationLink href={null}
													>Next &nbsp; →</PaginationLink
												>
											</PaginationItem>
										</Pagination>

										<Pagination class="mb-3" size="sm">
											<PaginationItem disabled>
												<PaginationLink href={null}
													>← &nbsp; Prev</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>2</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem>
												<PaginationLink href={null}
													>Next &nbsp; →</PaginationLink
												>
											</PaginationItem>
										</Pagination>
									</div>
								</Col>

								<Col lg={6}>
									<div class="mt-4">
										<h5 class="fs-15">Alignment</h5>

										<p class="text-muted">
											Use <code
												>justify-content-start</code
											>,
											<code>justify-content-start</code>,
											or
											<code>justify-content-start</code>,
											class to pagination class to change
											the alignment of pagination
											respectively.
										</p>

										<Pagination
											listClassName="justify-content-center"
										>
											<PaginationItem disabled>
												<PaginationLink href={null}
													>← &nbsp; Prev</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>2</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem>
												<PaginationLink href={null}
													>Next &nbsp; →</PaginationLink
												>
											</PaginationItem>
										</Pagination>

										<Pagination
											listClassName="justify-content-end"
										>
											<PaginationItem disabled>
												<PaginationLink href={null}
													>← &nbsp; Prev</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>2</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem>
												<PaginationLink href={null}
													>Next &nbsp; →</PaginationLink
												>
											</PaginationItem>
										</Pagination>
									</div>
								</Col>
							</Row>

							<Row>
								<Col lg={6}>
									<div class="mt-4">
										<h5 class="fs-15">
											Custom Separated Pagination
										</h5>
										<p class="text-muted">
											Use <code>pagination-separated</code
											> class to pagination class to set custom
											separated pagination.
										</p>

										<Pagination
											size="lg"
											class="mb-3 pagination-lg pagination-separated"
										>
											<PaginationItem disabled>
												<PaginationLink href={null}
													>←</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem active>
												<PaginationLink href={null}
													>2</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>4</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>5</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>→</PaginationLink
												></PaginationItem
											>
										</Pagination>

										<Pagination
											class="mb-3 pagination-separated"
										>
											<PaginationItem disabled>
												<PaginationLink href={null}
													>←</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem active>
												<PaginationLink href={null}
													>2</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>4</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>5</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>→</PaginationLink
												></PaginationItem
											>
										</Pagination>

										<Pagination
											size="sm"
											class="mb-3 pagination-sm pagination-separated"
										>
											<PaginationItem disabled>
												<PaginationLink href={null}
													>←</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem active>
												<PaginationLink href={null}
													>2</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>4</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>5</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>→</PaginationLink
												></PaginationItem
											>
										</Pagination>
									</div>
								</Col>

								<Col lg={6}>
									<div class="mt-4">
										<h5 class="fs-15">
											Custom Rounded Pagination
										</h5>
										<p class="text-muted">
											Use <code>pagination-rounded</code> class
											to pagination class to set custom rounded
											pagination.
										</p>

										<Pagination size="lg"
											class="pagination-lg pagination-rounded mb-3"
										>
											<PaginationItem disabled>
												<PaginationLink href={null}
													>←</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem active>
												<PaginationLink href={null}
													>2</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>4</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>5</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>→</PaginationLink
												></PaginationItem
											>
										</Pagination>

										<Pagination class="pagination-rounded mb-3">
											<PaginationItem disabled>
												<PaginationLink href={null}
													>←</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem active>
												<PaginationLink href={null}
													>2</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>4</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>5</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>→</PaginationLink
												></PaginationItem
											>
										</Pagination>

										<Pagination
											size="sm"
											class="pagination-sm pagination-rounded mb-3"
										>
											<PaginationItem disabled>
												<PaginationLink href={null}
													>←</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>1</PaginationLink
												></PaginationItem
											>
											<PaginationItem active>
												<PaginationLink href={null}
													>2</PaginationLink
												>
											</PaginationItem>
											<PaginationItem
												><PaginationLink href={null}
													>3</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>4</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>5</PaginationLink
												></PaginationItem
											>
											<PaginationItem
												><PaginationLink href={null}
													>→</PaginationLink
												></PaginationItem
											>
										</Pagination>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={paginationCode}
								id="paginationCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Spinners" />

					<CardBody>
						<div class="live-preview">
							<Row>
								<Col lg={6}>
									<div>
										<h5 class="fs-15">Border spinner</h5>
										<p class="text-muted">
											Use <code>Spinner</code> attribute for
											a lightweight loading indicator.
										</p>
										<div class="d-flex flex-wrap gap-3 mb-2"
										>
											<Spinner color="primary"
												>Loading...</Spinner
											>
											<Spinner color="secondary"
												>Loading...</Spinner
											>
											<Spinner color="success"
												>Loading...</Spinner
											>
											<Spinner color="info"
												>Loading...</Spinner
											>
											<Spinner color="warning"
												>Loading...</Spinner
											>
											<Spinner color="danger"
												>Loading...</Spinner
											>
											<Spinner color="dark"
												>Loading...</Spinner
											>
											<Spinner color="light"
												>Loading...</Spinner
											>
										</div>
									</div>
								</Col>

								<Col lg={6}>
									<div>
										<h5 class="fs-15">Growing spinner</h5>
										<p class="text-muted">
											Use <code>spinner-grow</code> class for
											a lightweight spinner with growing effect.
										</p>
										<div class="d-flex flex-wrap gap-3 mb-2"
										>
											<Spinner color="primary" type="grow"
												>Loading...</Spinner
											>
											<Spinner
												color="secondary"
												type="grow">Loading...</Spinner
											>
											<Spinner color="success" type="grow"
												>Loading...</Spinner
											>
											<Spinner color="info" type="grow"
												>Loading...</Spinner
											>
											<Spinner color="warning" type="grow"
												>Loading...</Spinner
											>
											<Spinner color="danger" type="grow"
												>Loading...</Spinner
											>
											<Spinner color="dark" type="grow"
												>Loading...</Spinner
											>
											<Spinner color="light" type="grow"
												>Loading...</Spinner
											>
										</div>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={spinnersCode}
								id="spinnersCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
