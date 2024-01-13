<script>
	import { Card, CardBody, Col, Container, Row } from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";

	// Rounded Ribbon

	const roundedRibbonCode = `
<!-- Rounded Ribbon -->
<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody>
        <div class="ribbon ribbon-primary round-shape">Primary</div>
            <h5 class="fs-14 text-end">Rounded Ribbon</h5>
        <div class="ribbon-content mt-4 text-muted">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</Card>

<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody>
        <div class="ribbon ribbon-success round-shape">Success</div>
            <h5 class="fs-14 text-end">Rounded Ribbon</h5>
        <div class="ribbon-content mt-4 text-muted">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</Card>

<!-- Right Ribbon -->
<Card class="ribbon-box border shadow-none right mb-lg-0 material-shadow">
    <CardBody>
        <div class="ribbon ribbon-info round-shape">Info</div>
            <h5 class="fs-14 text-start">Rounded Ribbon Right</h5>
        <div class="ribbon-content mt-4 text-muted">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</Card>
`;

	// Ribbon Shape

	const ribbonShapeCode = `
<!-- Ribbon Shape -->
<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody>
        <div class="ribbon ribbon-primary ribbon-shape">Primary</div>
        <h5 class="fs-14 text-end">Ribbon Shape</h5>
        <div class="ribbon-content text-muted mt-4">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</Card>

<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody>
        <div class="ribbon ribbon-success ribbon-shape">Success</div>
        <h5 class="fs-14 text-end">Ribbon Shape</h5>
        <div class="ribbon-content text-muted mt-4">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</Card>

<Card class="ribbon-box border shadow-none mb-lg-0 right material-shadow">
    <CardBody>
        <div class="ribbon ribbon-info ribbon-shape">Info</div>
        <h5 class="fs-14 text-start">Ribbon Shape Right</h5>
        <div class="ribbon-content text-muted mt-4">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</Card>
`;

	// Filled Ribbons

	const filledRibbonsCode = `
<!-- Filled Ribbons -->
<Card class="ribbon-box border ribbon-fill shadow-none mb-lg-0 material-shadow">
    <CardBody>
        <div class="ribbon ribbon-primary">- 10 %</div>
        <h5 class="fs-14 text-end">Fill Ribbon</h5>
        <div class="ribbon-content mt-5 text-muted">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</Card>

<Card class="ribbon-box border ribbon-fill shadow-none mb-lg-0 material-shadow">
    <CardBody>
        <div class="ribbon ribbon-success">- 20 %</div>
        <h5 class="fs-14 text-end">Fill Ribbon</h5>
        <div class="ribbon-content mt-5 text-muted">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</Card>

<!-- Right Ribbon -->
<Card class="ribbon-box border ribbon-fill shadow-none right mb-lg-0 material-shadow">
    <CardBody>
        <div class="ribbon ribbon-info">- 30 %</div>
        <h5 class="fs-14 text-start">Fill Ribbon Right</h5>
        <div class="ribbon-content mt-5 text-muted">
            <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas
                mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio.</p>
        </div>
    </CardBody>
</div>
`;

	// Boxed Ribbons

	const boxedRibbonsCode = `
<!-- Boxed Ribbons -->
<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <div class="ribbon-two ribbon-two-primary"><span>Primary</span></div>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </CardBody>
</Card>

<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <div class="ribbon-two ribbon-two-success"><span>Success</span></div>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </CardBody>
</Card>

<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <div class="ribbon-two ribbon-two-success"><span>Success</span></div>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </CardBody>
</Card>
`;

	// Ribbons

	const ribbonsCode = `
<!-- Ribbons -->
<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <span class="ribbon-three ribbon-three-primary"><span>Primary</span></span>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </CardBody>
</Card>

<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <div class="ribbon-three ribbon-three-success"><span>Success</span></div>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </CardBody>
</Card>

<Card class="ribbon-box border shadow-none mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <div class="ribbon-three ribbon-three-info"><span>Success</span></div>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </CardBody>
</Card>
`;

	// Ribbons Hover

	const ribbonsHoverCode = `
<!-- Ribbons Hover -->
<Card class="ribbon-box border shadow-none overflow-hidden mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <div class="ribbon ribbon-info ribbon-shape trending-ribbon">
            <span class="trending-ribbon-text">Trending</span> <i class="ri-flashlight-fill text-white align-bottom float-end ms-1"></i>
        </div>
        <h5 class="fs-14 text-end mb-3">Ribbon Shape</h5>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </div>
</Card>

<Card class="ribbon-box border shadow-none overflow-hidden mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <div class="ribbon ribbon-info ribbon-shape trending-ribbon">
            <span class="trending-ribbon-text">Trending</span> <i class="ri-flashlight-fill text-white align-bottom float-end ms-1"></i>
        </div>
        <h5 class="fs-14 text-end mb-3">Ribbon Shape</h5>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </div>
</Card>

<Card class="ribbon-box right border shadow-none overflow-hidden mb-lg-0 material-shadow">
    <CardBody class="text-muted">
        <div class="ribbon ribbon-info ribbon-shape trending-ribbon">
            <i class="ri-flashlight-fill text-white align-bottom float-start me-1"></i> <span class="trending-ribbon-text">Trending</span>
        </div>
        <h5 class="fs-14 mb-3">Ribbon Right Shape</h5>
        <p class="mb-0">Quisque nec turpis at urna dictum luctus. Suspendisse convallis dignissim eros at volutpat. In egestas mattis dui. Aliquam mattis dictum aliquet. Nulla sapien mauris, eleifend et sem ac, commodo dapibus odio. Vivamus pretium nec odio cursus.</p>
    </div>
</Card>
`;
</script>

<svelte:head>
	<title>Ribbons | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Ribbons" pageTitle="Base UI" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Rounded Ribbon" />
					<CardBody>
						<div class="live-preview">
							<Row class="g-3">
								<p class="text-muted">
									Use <code>round-shape</code> class to show round-shaped
									ribbon.
								</p>
								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-primary round-shape"
											>
												Primary
											</div>
											<h5 class="fs-14 text-end">
												Rounded Ribbon
											</h5>

											<div class="ribbon-content mt-4 text-muted"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-success round-shape"
											>
												Success
											</div>
											<h5 class="fs-14 text-end">
												Rounded Ribbon
											</h5>
											<div class="ribbon-content mt-4 text-muted"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none right mb-lg-0 material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-info round-shape"
											>
												Info
											</div>
											<h5 class="fs-14 text-start">
												Rounded Ribbon Right
											</h5>
											<div class="ribbon-content mt-4 text-muted"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={roundedRibbonCode}
								id="roundedRibbonCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Ribbon Shape" />

					<CardBody>
						<div class="live-preview">
							<Row class="g-3">
								<p class="text-muted">
									Use <code>ribbon-shape</code> class to show ribbon
									shaped ribbon.
								</p>
								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-primary ribbon-shape"
											>
												Primary
											</div>
											<h5 class="fs-14 text-end">
												Ribbon Shape
											</h5>
											<div class="ribbon-content text-muted mt-4"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-success ribbon-shape"
											>
												Success
											</div>
											<h5 class="fs-14 text-end">
												Ribbon Shape
											</h5>
											<div class="ribbon-content text-muted mt-4"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 right material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-info ribbon-shape"
											>
												Info
											</div>
											<h5 class="fs-14 text-start">
												Ribbon Shape Right
											</h5>
											<div class="ribbon-content text-muted mt-4"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={ribbonShapeCode}
								id="ribbonShapeCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Filled Ribbons" />

					<CardBody>
						<div class="live-preview">
							<Row class="g-3">
								<p class="text-muted">
									Use <code>ribbon-fill</code> class to show fill-shaped
									ribbon.
								</p>
								<Col xxl={4}>
									<div class="card ribbon-box border ribbon-fill shadow-none mb-lg-0 material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-primary">
												New
											</div>
											<h5 class="fs-14 text-end">
												Fill Ribbon
											</h5>
											<div class="ribbon-content mt-3 text-muted"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border ribbon-fill shadow-none mb-lg-0 material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-success">
												Sale
											</div>
											<h5 class="fs-14 text-end">
												Fill Ribbon
											</h5>
											<div class="ribbon-content mt-3 text-muted"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border ribbon-fill shadow-none right mb-lg-0 material-shadow"
									>
										<CardBody>
											<div class="ribbon ribbon-info">
												New
											</div>
											<h5 class="fs-14 text-start">
												Fill Ribbon Right
											</h5>
											<div class="ribbon-content mt-3 text-muted"
											>
												<p class="mb-0">
													Quisque nec turpis at urna
													dictum luctus. Suspendisse
													convallis dignissim eros at
													volutpat. In egestas mattis
													dui. Aliquam mattis dictum
													aliquet. Nulla sapien
													mauris, eleifend et sem ac,
													commodo dapibus odio.
												</p>
											</div>
										</CardBody>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={filledRibbonsCode}
								id="filledRibbonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Boxed Ribbons" />

					<CardBody>
						<div class="live-preview">
							<Row class="g-3">
								<p class="text-muted">
									Use <code>ribbon-box</code> class with
									<code>ribbon-two</code> class at child element
									to show below-mentioned shaped ribbon.
								</p>
								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow"
									>
										<div class="card-body text-muted">
											<div class="ribbon-two ribbon-two-primary"
											>
												<span>Basic</span>
											</div>
											<h5 class="fs-14 text-end mb-3">
												Box Ribbon
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus.
											</p>
										</div>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow"
									>
										<div class="card-body text-muted">
											<div class="ribbon-two ribbon-two-success"
											>
												<span>Standard</span>
											</div>
											<h5 class="fs-14 text-end mb-3">
												Box Ribbon
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus.
											</p>
										</div>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow right"
									>
										<div class="card-body text-muted">
											<div class="ribbon-two ribbon-two-info"
											>
												<span>Premium</span>
											</div>
											<h5 class="fs-14 mb-3">
												Box Ribbon Right
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus
												elementum ornare.
											</p>
										</div>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={boxedRibbonsCode}
								id="boxedRibbonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Ribbons" />

					<CardBody>
						<div class="live-preview">
							<Row class="g-3">
								<p class="text-muted">
									Use <code>ribbon-box</code> class with
									<code>ribbon-three</code> class at child element
									to show below-mentioned shaped ribbon.
								</p>
								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow"
									>
										<div class="card-body text-muted">
											<span
												class="ribbon-three ribbon-three-primary"
												><span>Featured</span></span
											>
											<h5 class="fs-14 text-end mb-3">
												Ribbon Shape
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus.
											</p>
										</div>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow"
									>
										<div class="card-body text-muted">
											<span
												class="ribbon-three ribbon-three-success"
												><span>Featured</span></span
											>
											<h5 class="fs-14 text-end mb-3">
												Ribbon Shape
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus.
											</p>
										</div>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none mb-lg-0 material-shadow right"
									>
										<div class="card-body text-muted">
											<span
												class="ribbon-three ribbon-three-info"
												><span>Featured</span></span
											>
											<h5 class="fs-14 mb-3">
												Ribbon Right Shape
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus.
											</p>
										</div>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={ribbonsCode}
								id="ribbonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Ribbons Hover" />

					<CardBody>
						<div class="live-preview">
							<Row class="g-3">
								<p class="text-muted">
									Use <code>trending-ribbon</code> class to show
									ribbon with hovering effect.
								</p>
								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none overflow-hidden mb-lg-0 material-shadow"
									>
										<div class="card-body text-muted">
											<div class="ribbon ribbon-info ribbon-shape trending-ribbon"
											>
												<span
													class="trending-ribbon-text"
													>Trending</span
												>
												<i
													class="ri-flashlight-fill text-white align-bottom float-end ms-1"
												/>
											</div>
											<h5 class="fs-14 text-end mb-3">
												Ribbon Shape
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus.
											</p>
										</div>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box border shadow-none overflow-hidden mb-lg-0 material-shadow"
									>
										<div class="card-body text-muted">
											<div class="ribbon ribbon-info ribbon-shape trending-ribbon"
											>
												<span
													class="trending-ribbon-text"
													>Trending</span
												>
												<i
													class="ri-flashlight-fill text-white align-bottom float-end ms-1"
												/>
											</div>
											<h5 class="fs-14 text-end mb-3">
												Ribbon Shape
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus.
											</p>
										</div>
									</div>
								</Col>

								<Col xxl={4}>
									<div class="card ribbon-box right border shadow-none overflow-hidden mb-lg-0 material-shadow"
									>
										<div class="card-body text-muted">
											<div class="ribbon ribbon-info ribbon-shape trending-ribbon"
											>
												<i
													class="ri-flashlight-fill text-white align-bottom float-start me-1"
												/>
												<span
													class="trending-ribbon-text"
													>Trending</span
												>
											</div>
											<h5 class="fs-14 mb-3">
												Ribbon Right Shape
											</h5>
											<p class="mb-0">
												Quisque nec turpis at urna
												dictum luctus. Suspendisse
												convallis dignissim eros at
												volutpat. In egestas mattis dui.
												Aliquam mattis dictum aliquet.
												Nulla sapien mauris, eleifend et
												sem ac, commodo dapibus odio.
												Vivamus pretium nec odio cursus.
											</p>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={ribbonsHoverCode}
								id="ribbonsHoverCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
