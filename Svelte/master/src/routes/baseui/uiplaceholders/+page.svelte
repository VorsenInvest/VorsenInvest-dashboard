<script>
	import { Card, CardBody, Col, Container, Row } from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";

	import img1 from '../../../assets/images/small/img-1.jpg';
	import img2 from '../../../assets/images/small/img-2.jpg';

	// Default Placeholder

	const defaultPlaceholderCode = `
<!-- Base Examples -->
<Card>
	<img
		src={img1}
		class="card-img-top"
		alt="card img"
	/>

	<CardBody>
		<h5 class="card-title">
			Card title
		</h5>
		<p class="card-text">
			Some quick example text
			to build on the card
			title and make up the
			bulk of the card's
			content.
		</p>
		<Link
			href={null}
			class="btn btn-primary"
			>Go somewhere</Link
		>
	</CardBody>
</Card>
<Card>
	<img
		src={img2}
		class="card-img-top"
		alt="card dummy img"
	/>
	<CardBody>
		<h5
			class="card-title placeholder-glow"
		>
			<span
				class="placeholder col-6"
			/>
		</h5>
		<p
			class="card-text placeholder-glow"
		>
			<span
				class="placeholder col-7"
			/>
			<span
				class="placeholder col-4"
			/>
			<span
				class="placeholder col-4"
			/>
			<span
				class="placeholder col-6"
			/>
		</p>
		<Link
			href={null}
			tabIndex="-1"
			class="btn btn-primary disabled placeholder col-6"
		/>
	</CardBody>
</Card>

`;
	// Width

	const widthCode = `
<!-- Width Sizing-->
<div class="live-preview">
    <span class="placeholder col-6"></span>
    <span class="placeholder w-75"></span>
    <span class="placeholder" style="width: 25%"></span>
</div>
`;

	// Sizing

	const sizingCode = `
<!-- Sizing -->
<span class="placeholder col-12 placeholder-lg"></span>

<span class="placeholder col-12"></span>

<span class="placeholder col-12 placeholder-sm"></span>

<span class="placeholder col-12 placeholder-xs"></span>
`;

	// Color

	const colorCode = `
<!-- Color -->
<span class="placeholder col-12 mb-3"></span>

<span class="placeholder col-12 mb-3 bg-primary"></span>

<span class="placeholder col-12 mb-3 bg-secondary"></span>

<span class="placeholder col-12 mb-3 bg-success"></span>

<span class="placeholder col-12 mb-3 bg-danger"></span>

<span class="placeholder col-12 mb-3 bg-warning"></span>

<span class="placeholder col-12 mb-3 bg-info"></span>

<span class="placeholder col-12 mb-3 bg-light"></span>

<span class="placeholder col-12 mb-3 bg-dark"></span>
`;
</script>

<svelte:head>
	<title>Placeholders | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Placeholders" pageTitle="Base UI" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Default Placeholder" />
					<CardBody>
						<p class="text-muted">
							In the example below, we take a typical card
							component and recreate it with placeholders applied
							to create a “loading card”.
						</p>

						<div class="live-preview">
							<Row class="justify-content-center">
								<Col xl={7}>
									<Row class="justify-content-between">
										<Col lg={5} sm={6}>
											<Card>
												<img
													src={img1}
													class="card-img-top"
													alt="card img"
												/>

												<CardBody>
													<h5 class="card-title">
														Card title
													</h5>
													<p class="card-text">
														Some quick example text
														to build on the card
														title and make up the
														bulk of the card's
														content.
													</p>
													<Link
														href={null}
														class="btn btn-primary"
														>Go somewhere</Link
													>
												</CardBody>
											</Card>
										</Col>
										<Col lg={5} sm={6}>
											<Card>
												<img
													src={img2}
													class="card-img-top"
													alt="card dummy img"
												/>
												<CardBody>
													<h5
														class="card-title placeholder-glow"
													>
														<span
															class="placeholder col-6"
														/>
													</h5>
													<p
														class="card-text placeholder-glow"
													>
														<span
															class="placeholder col-7"
														/>
														<span
															class="placeholder col-4"
														/>
														<span
															class="placeholder col-4"
														/>
														<span
															class="placeholder col-6"
														/>
													</p>
													<Link
														href={null}
														tabIndex="-1"
														class="btn btn-primary disabled placeholder col-6"
													/>
												</CardBody>
											</Card>
										</Col>
									</Row>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={defaultPlaceholderCode}
								id="defaultPlaceholderCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Width" />
					<CardBody>
						<p class="text-muted">
							Use <code>w-25,w-50,w-75</code> or
							<code>w-100</code> class to placeholder class to set
							different widths to the placeholder.
						</p>
						<div class="live-preview">
							<span class="placeholder w-50" />
							<span class="placeholder w-75" />
							<span class="placeholder w-25" />
							<span class="placeholder w-100" />
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={widthCode}
								id="widthCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Sizing" />
					<CardBody>
						<p class="text-muted">
							Use <code>placeholder-lg</code>,
							<code>placeholder-sm</code>, or
							<code>placeholder-xs</code> class to placeholder class
							to set different size placeholder.
						</p>
						<div class="live-preview">
							<Row class="gap-0">
								<Col class="col-12">
									<span
										class="placeholder placeholder-lg w-100"
									/>
								</Col>
								<Col class="col-12">
									<span class="placeholder w-100" />
								</Col>
								<Col class="col-12">
									<span
										class="placeholder placeholder-sm w-100"
									/>
								</Col>
								<Col class="col-12">
									<span
										class="placeholder placeholder-xs w-100"
									/>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={sizingCode}
								id="sizingCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Color" />
					<CardBody>
						<p class="text-muted">
							Use <code>bg-</code> class with the below-mentioned color
							variation to set a custom color.
						</p>
						<div class="live-preview">
							<Row class="g-2">
								<Col class="col-12">
									<span class="placeholder w-100" />
								</Col>
								<Col class="col-12">
									<span
										class="placeholder bg-primary w-100"
									/>
								</Col>
								<Col class="col-12">
									<span
										class="placeholder bg-secondary w-100"
									/>
								</Col>
								<Col class="col-12">
									<span
										class="placeholder bg-success w-100"
									/>
								</Col>
								<Col class="col-12">
									<span class="placeholder bg-danger w-100" />
								</Col>
								<Col class="col-12">
									<span
										class="placeholder bg-warning w-100"
									/>
								</Col>
								<Col class="col-12">
									<span class="placeholder bg-info w-100" />
								</Col>
								<Col class="col-12">
									<span class="placeholder bg-light w-100" />
								</Col>
								<Col class="col-12">
									<span class="placeholder bg-dark w-100" />
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={colorCode}
								id="colorCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
