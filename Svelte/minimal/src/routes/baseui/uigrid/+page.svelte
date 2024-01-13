<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Container,
		Row,
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";

	const verticalStartCode = `
<!-- Vertical alignment (align-items-start) -->
<Row class="align-items-start">
    <Col sm={4}>
        ...
    </Col>
    <Col sm={4}>
        ...
    </Col>
    <Col sm={4}>
        ...
    </Col>
</Row>
`;

	// Vertical alignment (align-items-center)

	const verticalCenterCode = `
<!-- Vertical alignment (align-items-center) -->
<Row class="align-items-center">
    <Col sm={4}>
        ...
    </Col>
    <Col sm={4}>
        ...
    </Col>
    <Col sm={4}>
        ...
    </Col>
</Row>
`;

	// Vertical alignment (align-items-end)

	const verticalEndCode = `
<!-- Vertical alignment (align-items-end) -->
<Row class="align-items-end">
    <Col sm={4}>
        ...
    </Col>
    <Col sm={4}>
        ...
    </Col>
    <Col sm={4}>
        ...
    </Col>
</Row>
`;

	// Align Self

	const alignSelfCode = `
<!-- Align Self -->
<Row>
    <Col sm={4} class="align-self-start">
        ...
    </Col>
    <Col sm={4} class="align-self-center">
        ...
    </Col>
    <Col sm={4} class="align-self-end">
        ...
    </Col>
</Row>
`;

	// Horizontal Alignment

	const horizontalAlignCode = `
<!-- Horizontal Alignment -->
<Row class="justify-content-start">
    <Col sm={4}>
        ...
    </Col>
</Row>
<Row class="justify-content-center">
    <Col sm={4}>
        ...
    </Col>
</Row>
<Row class="justify-content-end">
<Col sm={4}>
        ...
</Col>
</Row>
`;
</script>

<svelte:head>
	<title>Grid | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Grid" pageTitle="Base UI" />
		<Row>
			<Col class="col-12">
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Grid Options</h4>
					</CardHeader>

					<CardBody>
						<p class="text-muted">
							See how aspects of the Bootstrap grid system work
							across multiple devices with a handy table.
						</p>
						<div class="table-responsive">
							<table
								class="table table-bordered table-nowrap mb-0"
							>
								<thead>
									<tr>
										<th scope="col" />
										<th scope="col" class="text-center">
											xs<br />
											<span class="fw-normal"
												>&lt;576px</span
											>
										</th>
										<th scope="col" class="text-center">
											sm<br />
											<span class="fw-normal">≥576px</span
											>
										</th>
										<th scope="col" class="text-center">
											md<br />
											<span class="fw-normal">≥768px</span
											>
										</th>
										<th scope="col" class="text-center">
											lg<br />
											<span class="fw-normal">≥992px</span
											>
										</th>
										<th scope="col" class="text-center">
											xl<br />
											<span class="fw-normal"
												>≥1200px</span
											>
										</th>
										<th scope="col" class="text-center">
											xxl<br />
											<span class="fw-normal"
												>≥1400px</span
											>
										</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<th class="text-nowrap" scope="row"
											>Grid behavior</th
										>
										<td>Horizontal at all times</td>
										<td colSpan="5"
											>Collapsed to start, horizontal
											above breakpoints</td
										>
									</tr>
									<tr>
										<th class="text-nowrap" scope="row"
											>Max container width</th
										>
										<td>None (auto)</td>
										<td>540px</td>
										<td>720px</td>
										<td>960px</td>
										<td>1140px</td>
										<td>1320px</td>
									</tr>
									<tr>
										<th class="text-nowrap" scope="row"
											>Class prefix</th
										>
										<td><code>col-</code></td>
										<td><code>col-sm-</code></td>
										<td><code>col-md-</code></td>
										<td><code>col-lg-</code></td>
										<td><code>col-xl-</code></td>
										<td><code>col-xxl-</code></td>
									</tr>
									<tr>
										<th class="text-nowrap" scope="row"
											># of columns</th
										>
										<td colSpan="6">12</td>
									</tr>
									<tr>
										<th class="text-nowrap" scope="row"
											>Gutter width</th
										>
										<td colSpan="6"
											>1.5rem (0.75rem on each side of a
											column)</td
										>
									</tr>
									<tr>
										<th class="text-nowrap" scope="row"
											>Custom gutters</th
										>
										<td colSpan="6">Yes</td>
									</tr>
									<tr>
										<th class="text-nowrap" scope="row"
											>Nestable</th
										>
										<td colSpan="6">Yes</td>
									</tr>
									<tr>
										<th class="text-nowrap" scope="row"
											>Offsets</th
										>
										<td colSpan="6">Yes</td>
									</tr>
									<tr>
										<th class="text-nowrap" scope="row"
											>Column ordering</th
										>
										<td colSpan="6">Yes</td>
									</tr>
								</tbody>
							</table>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader
						title="Vertical alignment (align-items-start)"
					/>

					<CardBody>
						<p class="text-muted">
							Use <code>align-items-start</code> class to vertically
							align-items at the start.
						</p>
						<div class="live-preview">
							<div class="bg-light p-3 text-center">
								<Row
									class="align-items-start"
									style="min-height: 6rem"
								>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2"
										>
											col-sm-4
										</div>
									</Col>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2 mt-2 mt-sm-0"
										>
											col-sm-4
										</div>
									</Col>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2 mt-2 mt-sm-0"
										>
											col-sm-4
										</div>
									</Col>
								</Row>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={verticalStartCode}
								id="verticalStartCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader
						title="Vertical alignment (align-items-center)"
					/>

					<CardBody>
						<p class="text-muted">
							Use <code>align-items-center</code> class to vertically
							align-items at the center.
						</p>

						<div class="live-preview">
							<div class="bg-light p-3 text-center">
								<Row
									class="align-items-center"
									style="min-height: 6rem"
								>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2"
										>
											col-sm-4
										</div>
									</Col>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2 mt-2 mt-sm-0"
										>
											col-sm-4
										</div>
									</Col>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2 mt-2 mt-sm-0"
										>
											col-sm-4
										</div>
									</Col>
								</Row>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={verticalCenterCode}
								id="verticalCenterCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader
						title="Vertical alignment (align-items-end)"
					/>

					<CardBody>
						<p class="text-muted">
							Use <code>align-items-end</code> class to vertically
							align-items at the end.
						</p>
						<div class="live-preview">
							<div class="bg-light p-3 text-center">
								<Row
									class="align-items-end"
									style="min-height: 6rem"
								>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2"
										>
											col-sm-4
										</div>
									</Col>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2 mt-2 mt-sm-0"
										>
											col-sm-4
										</div>
									</Col>
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2 mt-2 mt-sm-0"
										>
											col-sm-4
										</div>
									</Col>
								</Row>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={verticalEndCode}
								id="verticalEndCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Align Self" />

					<CardBody>
						<p class="text-muted">
							Use the <code>align-self-start</code>,<code
								>align-self-center</code
							>, or
							<code>align-self-end</code> class respectively to vertically
							align items with a different position.
						</p>

						<div class="live-preview">
							<div class="bg-light p-3 text-center">
								<Row class="g-2" style="min-height: 9rem">
									<div class="col-sm-4 align-self-start">
										<div
											class="bg-primary-subtle text-primary rounded p-2"
										>
											align-self-start
										</div>
									</div>
									<div class="col-sm-4 align-self-center">
										<div
											class="bg-primary-subtle text-primary rounded p-2"
										>
											align-self-center
										</div>
									</div>
									<div class="col-sm-4 align-self-end">
										<div
											class="bg-primary-subtle text-primary rounded p-2"
										>
											align-self-end
										</div>
									</div>
								</Row>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={alignSelfCode}
								id="alignSelfCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Horizontal Alignment" />

					<CardBody>
						<p class="text-muted">
							Use the <code>justify-content-start</code>,<code
								>justify-content-center</code
							>, or
							<code>justify-content-end</code> class respectively to
							horizontally align items with a different position.
						</p>
						<div class="live-preview">
							<div class="bg-light p-3 text-center">
								<Row class="justify-content-start">
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2"
										>
											justify-content-start
										</div>
									</Col>
								</Row>
								<Row class="justify-content-center">
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2 mt-2 mt-sm-0"
										>
											justify-content-center
										</div>
									</Col>
								</Row>
								<Row class="justify-content-end">
									<Col sm={4}>
										<div
											class="bg-primary-subtle text-primary rounded p-2 mt-2 mt-sm-0"
										>
											justify-content-end
										</div>
									</Col>
								</Row>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={horizontalAlignCode}
								id="horizontalAlignCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
