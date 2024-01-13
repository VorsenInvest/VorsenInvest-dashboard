<script>
	import { Card, CardBody, Tooltip, Col, Container, Row } from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";

	import avatar2 from "../../../assets/images/users/avatar-2.jpg";
	import avatar3 from "../../../assets/images/users/avatar-3.jpg";
	import avatar4 from "../../../assets/images/users/avatar-4.jpg";
	import avatar5 from "../../../assets/images/users/avatar-5.jpg";
	import avatar8 from "../../../assets/images/users/avatar-8.jpg";
	import avatar10 from "../../../assets/images/users/avatar-10.jpg";
	import img2 from "../../../assets/images/small/img-2.jpg";
	import img3 from "../../../assets/images/small/img-3.jpg";
	import img4 from "../../../assets/images/small/img-4.jpg";
	import img5 from "../../../assets/images/small/img-5.jpg";

	// Image Rounded & Circle

	const imgRoundedCircleCode = `
<!-- Rounded Image -->
<img class="rounded shadow" alt="200x200" width="200" src={img4} />

<!-- Rounded-circle Image -->
<img class="rounded-circle avatar-xl shadow" alt="200x200" src={avatar4} />
`;

	// Image Thumbnails

	const imgThumbnailsCode = `
<!-- Thumbnails Images -->
<img class="img-thumbnail" alt="200x200" width="200" src={img3} />

<img class="img-thumbnail rounded-circle avatar-xl" alt="200x200" src={avatar3} />
`;

	// Image Sizes

	const imgSizesCode = `
<!-- Image Sizes -->
<img src={avatar2} alt="" class="rounded avatar-xxs shadow" />

<img src={avatar10} alt="" class="rounded avatar-xs shadow" />

<img src={avatar3} alt="" class="rounded avatar-sm shadow" />

<img src={avatar4} alt="" class="rounded avatar-md shadow" />

<img src={avatar5} alt="" class="rounded avatar-lg shadow" />

<img src={avatar8} alt="" class="rounded avatar-xl shadow" />

<img src={avatar2} alt="" class="rounded-circle avatar-xxs shadow" />

<img src={avatar10} alt="" class="rounded-circle avatar-xs shadow" />

<img src={avatar3} alt="" class="rounded-circle avatar-sm shadow" />

<img src={avatar4} alt="" class="rounded-circle avatar-md shadow" />

<img src={avatar5} alt="" class="rounded-circle avatar-lg shadow" />

<img src={avatar8} alt="" class="rounded-circle avatar-xl shadow" />
`;

	// Avatar With Content

	const avatarCode = `
<!-- Avatar With Content -->
<div class="avatar-xxs shadow">
    <div class="avatar-title rounded bg-primary-subtle text-primary">
    XXS
    </div>
</div>

<div class="avatar-xs shadow">
    <div class="avatar-title rounded bg-secondary-subtle text-secondary">
    XS
    </div>
</div>

<div class="avatar-sm shadow">
    <div class="avatar-title rounded bg-success-subtle text-success">
    Sm
    </div>
</div>

<div class="avatar-md shadow">
    <div class="avatar-title rounded bg-info-subtle text-info">
    Md
    </div>
</div>

<div class="avatar-lg shadow">
    <div class="avatar-title rounded bg-warning-subtle text-warning">
    Lg
    </div>
</div>

<div class="avatar-xl shadow">
    <div class="avatar-title rounded bg-danger-subtle text-danger">
    Xl
    </div>
</div>
`;

	// Avatar Group

	const avatarGroupCode = `
<!-- Simple Group -->
<div class="avatar-group">
    <div class="avatar-group-item shadow">
        <img src={avatar4} alt="" class="rounded-circle avatar-sm" />
    </div>
    <div class="avatar-group-item shadow">
    <img src={avatar5} alt="" class="rounded-circle avatar-sm" />
    </div>
    <div class="avatar-group-item shadow">
        <div class="avatar-sm">
            <div class="avatar-title rounded-circle bg-light text-primary">
                A
            </div>
        </div>
    </div>
    <div class="avatar-group-item shadow">
        <img src={avatar2} alt="" class="rounded-circle avatar-sm" />
    </div>
</div>

<!-- Avatar Group with Tooltip -->
<div class="mt-lg-0 mt-3">
    <p class="text-muted">Use <code>avatar-group</code> class with <code>data-bs-toggle="tooltip"</code> to show avatar group images with tooltip.</p>
    <div class="avatar-group">
        <Link href={null} class="avatar-group-item shadow" id="img1">
            <img src={avatar4} alt="" class="rounded-circle avatar-sm" />
        </Link>
        <Tooltip placement="top" target="img1" > Christi </Tooltip>
        <Link href={null} class="avatar-group-item shadow" id="img2">
            <img src={avatar3} alt="" class="rounded-circle avatar-sm" />
        </Link>
        <Tooltip placement="top" target="img2" > Frank Hook </Tooltip>
        <Link href={null} class="avatar-group-item shadow" id="img3">
            <div class="avatar-sm">
                <div class="avatar-title rounded-circle bg-light text-primary">
                    C
                </div>
            </div>
        </Link>
        <Tooltip placement="top" target="img3" > Christi </Tooltip>
        <Link href={null} class="avatar-group-item shadow" id="img4">
            <div class="avatar-sm">
                <div class="avatar-title rounded-circle">
                    2+
                </div>
            </div>  
        </Link>
        <Tooltip placement="top" target="img4" > mORE </Tooltip></div>
    </div>
`;

	// Figures

	const figuresCode = `
<!-- figures Images -->
<figure class="figure">
    <img src={img4} class="figure-img img-fluid rounded" alt="..." />
    <figcaption class="figure-caption">A caption for the above image.</figcaption>
</figure>

<figure class="figure mb-0">
    <img src={img5} class="figure-img img-fluid rounded" alt="..." />
    <figcaption class="figure-caption text-end">A caption for the above image.</figcaption>
</figure>
`;

	// Responsive Images

	const responsiveCode = `
<!-- Responsive Images -->
<img src={img2} class="img-fluid" alt="Responsive image" />
`;
</script>

<svelte:head>
	<title>Images | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Images" pageTitle="Base UI" />
		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Image Rounded & Circle" />
					<CardBody>
						<p class="text-muted">
							Use
							<code> rounded</code> class and
							<code>rounded-circle</code> class to show an image with
							a round border and rounded shape respectively.
						</p>

						<div class="live-preview">
							<Row class="align-items-center">
								<Col class="col-6">
									<img
										class="rounded  shadow"
										alt="200x200"
										width="200"
										src={img4}
									/>
								</Col>
								<Col class="col-6">
									<div class="mt-4 mt-md-0">
										<img
											class="rounded-circle avatar-xl shadow"
											alt="200x200"
											src={avatar4}
										/>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={imgRoundedCircleCode}
								id="imgRoundedCircleCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Image Thumbnails" />
					<CardBody>
						<p class="text-muted">
							Use <code>img-thumbnail</code> class to give an image
							rounded 1px border appearance.
						</p>

						<div class="live-preview">
							<Row>
								<Col class="col-6">
									<img
										class="img-thumbnail"
										alt="200x200"
										width="200"
										src={img3}
									/>
								</Col>
								<Col class="col-6">
									<div class="mt-4 mt-md-0">
										<img
											class="img-thumbnail rounded-circle avatar-xl"
											alt="200x200"
											src={avatar3}
										/>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={imgThumbnailsCode}
								id="imgThumbnailsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title=" shadow" />
					<CardBody>
						<p class="text-muted mb-4">
							Use <code>avatar-xxs</code>, <code>avatar-xs</code>,
							<code>avatar-sm</code>,
							<code>avatar-md</code>, <code>avatar-lg</code>,
							<code>avatar-xl</code> class for different image sizes.
						</p>

						<div class="live-preview">
							<Row>
								<Col md={12}>
									<Row class="g-3">
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar2}
													alt=""
													class="rounded avatar-xxs shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-xxs</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar10}
													alt=""
													class="rounded avatar-xs shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-xs</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar3}
													alt=""
													class="rounded avatar-sm shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-sm</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar4}
													alt=""
													class="rounded avatar-md shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-md</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar5}
													alt=""
													class="rounded avatar-lg shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-lg</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar8}
													alt=""
													class="rounded avatar-xl shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-xl</code>
												</p>
											</div>
										</Col>
									</Row>
								</Col>

								<Col md={12}>
									<Row class="g-3 mt-5">
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar2}
													alt=""
													class="rounded-circle avatar-xxs shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-xxs</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar10}
													alt=""
													class="rounded-circle avatar-xs shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-xs</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar3}
													alt=""
													class="rounded-circle avatar-sm shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-sm</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar4}
													alt=""
													class="rounded-circle avatar-md shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-md</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar5}
													alt=""
													class="rounded-circle avatar-lg shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-lg</code>
												</p>
											</div>
										</Col>
										<Col xxl={2} md={4} class="col-6">
											<div>
												<img
													src={avatar8}
													alt=""
													class="rounded-circle avatar-xl shadow"
												/>
												<p class="mt-2 mb-lg-0">
													<code>avatar-xl</code>
												</p>
											</div>
										</Col>
									</Row>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={imgSizesCode} id="imgSizesCode" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Avatar With Content" />

					<CardBody>
						<p class="text-muted">
							Use <code
								>avatar-xxs,
								avatar-xs,avatar-sm,avatar-md,avatar-lg,avatar-xl</code
							> class to set different avatar content.
						</p>

						<div class="live-preview">
							<Row class="g-3">
								<Col xxl={2} md={4} class="col-6">
									<div class="avatar-xxs mt-3 shadow">
										<div
											class="avatar-title rounded bg-primary-subtle text-primary fs-10"
										>
											XXS
										</div>
									</div>
								</Col>
								<Col xxl={2} md={4} class="col-6">
									<div class="avatar-xs mt-3 shadow">
										<div
											class="avatar-title rounded bg-secondary-subtle text-secondary"
										>
											XS
										</div>
									</div>
								</Col>
								<Col xxl={2} md={4} class="col-6">
									<div class="avatar-sm mt-3 shadow">
										<div
											class="avatar-title rounded bg-success-subtle text-success fs-14"
										>
											SM
										</div>
									</div>
								</Col>
								<Col xxl={2} md={4} class="col-6">
									<div class="avatar-md mt-3 shadow">
										<div
											class="avatar-title rounded bg-info-subtle text-info fs-16"
										>
											MD
										</div>
									</div>
								</Col>
								<Col xxl={2} md={4} class="col-6">
									<div class="avatar-lg mt-3 shadow">
										<div
											class="avatar-title rounded bg-warning-subtle text-warning fs-20"
										>
											LG
										</div>
									</div>
								</Col>
								<Col xxl={2} md={4} class="col-6">
									<div class="avatar-xl mt-3 shadow">
										<div
											class="avatar-title rounded bg-danger-subtle text-danger fs-22"
										>
											XL
										</div>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode code={avatarCode} id="avatarCode" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Avatar Group" />

					<CardBody>
						<div class="live-preview">
							<Row>
								<Col lg={6}>
									<div class="mt-lg-0 mt-3">
										<p class="text-muted">
											Use <code>avatar-group</code> class to
											show avatar images with the group.
										</p>
										<div class="avatar-group">
											<div class="avatar-group-item shadow">
												<img
													src={avatar4}
													alt=""
													class="rounded-circle avatar-sm"
												/>
											</div>
											<div class="avatar-group-item shadow">
												<img
													src={avatar5}
													alt=""
													class="rounded-circle avatar-sm"
												/>
											</div>
											<div class="avatar-group-item shadow">
												<div class="avatar-sm">
													<div
														class="avatar-title rounded-circle bg-light text-primary"
													>
														A
													</div>
												</div>
											</div>
											<div class="avatar-group-item shadow">
												<img
													src={avatar2}
													alt=""
													class="rounded-circle avatar-sm"
												/>
											</div>
										</div>
									</div>
								</Col>

								<Col lg={6}>
									<div class="mt-lg-0 mt-3">
										<p class="text-muted">
											Use <code>avatar-group</code> class
											with
											<code>data-bs-toggle="tooltip"</code
											>
											to show avatar group images with tooltip.
										</p>
										<div class="avatar-group">
											<Link
												href={null}
												class="avatar-group-item shadow"
												id="img1"
											>
												<img
													src={avatar4}
													alt=""
													class="rounded-circle avatar-sm"
												/>
											</Link>
											<Tooltip
												placement="top"
												target="img1">Christi</Tooltip
											>
											<Link
												href={null}
												class="avatar-group-item shadow"
												id="img2"
											>
												<img
													src={avatar3}
													alt=""
													class="rounded-circle avatar-sm"
												/>
											</Link>
											<Tooltip
												placement="top"
												target="img2"
												>Frank Hook</Tooltip
											>
											<Link
												href={null}
												class="avatar-group-item shadow"
												id="img3"
											>
												<div class="avatar-sm">
													<div
														class="avatar-title rounded-circle bg-light text-primary"
													>
														C
													</div>
												</div>
											</Link>
											<Tooltip
												placement="top"
												target="img3">Christi</Tooltip
											>
											<Link
												href={null}
												class="avatar-group-item shadow"
												id="img4"
											>
												<div class="avatar-sm">
													<div
														class="avatar-title rounded-circle"
													>
														2+
													</div>
												</div>
											</Link>
											<Tooltip
												placement="top"
												target="img4">More</Tooltip
											>
										</div>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={avatarGroupCode}
								id="avatarGroupCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xl={8}>
				<Card>
					<PreviewCardHeader title="Figures" />
					<CardBody>
						<p class="card-title-desc text-muted">
							Use the included <code>figure</code>,
							<code>figure-img</code>
							and
							<code>figure-caption</code>
							classes to provide some baseline styles for the HTML5
							<code>&lt;figure&gt;</code>
							and
							<code>&lt;figcaption&gt;</code> elements.
						</p>

						<div class="live-preview">
							<Row class="g-3">
								<Col sm={6}>
									<figure class="figure mb-0">
										<img
											src={img4}
											class="figure-img img-fluid rounded"
											alt="..."
										/>
										<figcaption class="figure-caption">
											A caption for the above image.
										</figcaption>
									</figure>
								</Col>
								<Col sm={6}>
									<figure class="figure mb-0">
										<img
											src={img5}
											class="figure-img img-fluid rounded"
											alt="..."
										/>
										<figcaption
											class="figure-caption text-end"
										>
											A caption for the above image.
										</figcaption>
									</figure>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode code={figuresCode} id="figuresCode" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xl={4}>
				<Card>
					<PreviewCardHeader title="Responsive Images" />

					<CardBody>
						<p class="card-title-desc text-muted">
							Responsive Images with <code
								>img-fluid,max-width: 100%; and height: auto;</code
							> to the image so that it scales with the parent width.
						</p>

						<div class="live-preview">
							<div>
								<img
									src={img2}
									class="img-fluid"
									alt="Responsive"
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={responsiveCode}
								id="responsiveCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
