<script>
	import {
		Button,
		Card,
		CardBody,
		Col,
		Container,
		Progress,
		Row,
	} from "sveltestrap";

	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";

	// Default Progress

	const defaultProgressCode = `
<!-- Base Examples -->
<div class="mb-4">
    <Progress value={0} />
</div>

<div class="mb-4">
    <Progress value={25} />
</div>

<div class="mb-4">
    <Progress value={50} />
</div>

<div class="mb-4">
    <Progress value={75} />
</div>

<div>
    <Progress value={100} />
</div>`;

	// Progress with background color

	const backgroundColorCode = `
<!-- Backgrounds -->
<div class="mb-4">
    <Progress color="primary" value={15} />
</div>

<div class="mb-4">
    <Progress color="success" value={25} />
</div>

<div class="mb-4">
    <Progress color="info" value={50} />
</div>

<div class="mb-4">
    <Progress color="warning" value={75} />
</div>

<div>
    <Progress color="danger" value={100} />
</div>`;

	// Progress with Label

	const labelCode = `
<!-- Labels Example -->
<Progress color="primary" value={25}> 25% </Progress>
`;

	// Multiple Bars
	const multipleBarsCode = `
<!-- Multiple Bars -->
<Progress multi>
    <Progress bar value="15" />
    <Progress bar color="success" value="30" />
    <Progress bar color="info" value="20" />
</Progress>
`;

	// Height
	const heightCode = `
<!-- Prgress sm -->
<div class="mb-4">
    <h5 class="fs-13">Small Progress</h5>
    <Progress color="primary" value={25} class="progress-sm" />
</div>

<!-- Prgress Default -->
<div class="mb-4">
    <h5 class="fs-13">Default Progress </h5>
    <Progress color="success" value={40} class="progress-md" />
</div>

<!-- Prgress lg -->
<div class="mb-4">
    <h5 class="fs-13">Large Progress</h5>
    <Progress color="warning" value={50} class="progress-lg" />
</div>

<!-- Prgress xl -->
<div>
    <h5 class="fs-13">Extra Large Progress</h5>
    <Progress color="danger" value={70} class="progress-xl" />
</div>
`;

	// Striped Progress
	const stripedCode = `
<!-- Striped Prgress -->
<div class="mb-4">
    <Progress striped value={25} />
</div>
<div>
    <Progress color="success" striped value={40} />
</div>
`;

	// Animated Striped Progress
	const animatedStripedCode = `
<!-- Animated Striped Progress -->
<div>
    <Progress value={75} striped animated />
</div>
`;

	// Gradient Progress
	const gradientCode = `
<!-- Gradient -->
<div class="mb-4">
    <Progress value={15} class="bg-gradient" />
</div>
<div class="mb-4">
    <Progress color="success" value={25} class="bg-gradient" />
</div>
<div class="mb-4">
    <Progress color="info" value={50} class="bg-gradient" />
</div>
<div class="mb-4">
    <Progress color="warning" value={75} class="bg-gradient" />
</div>
<div>
    <Progress color="danger" value={100} class="bg-gradient" />
</div>
`;

	// Animated Progress
	const animatedCode = `
<!-- Animated Progress -->
<div class="mb-4">
    <Progress value={15} class="animated-progess" />
</div>
<div class="mb-4">
    <Progress value={25} color="success" class="animated-progess" />
</div>
<div class="mb-4">
    <Progress value={50} color="info" class="animated-progess" />
</div>
<div class="mb-4">
    <Progress value={75} color="warning" class="animated-progess" />
</div>
<div>
    <Progress value={100} color="danger" class="animated-progess" />
</div>
`;

	// Custom Progress
	const customCode = `
<!-- Custom Progress -->
<div class="mb-4">
    <Progress value={15} color="primary" class="animated-progess custom-progress" />
</div>
<div class="mb-4">
    <Progress value={25} color="success" class="animated-progess custom-progress" />
</div>
<div class="mb-4">
    <Progress value={50} color="info" class="animated-progess custom-progress" />
</div>
<div class="mb-4">
    <Progress value={75} color="warning" class="animated-progess custom-progress" />
</div>
<div>
    <Progress value={100} color="danger" class="animated-progess custom-progress" />
</div>
`;

	// Custom Progress with Label
	const customProgressCode = `
<!-- Custom Progress with Label -->
<div class="d-flex align-items-center pb-2 mt-4">
    <div class="flex-shrink-0 me-3">
        <div class="avatar-xs">
            <div class="avatar-title bg-light rounded-circle text-muted fs-16">
                <i class="mdi mdi-facebook"></i>
            </div>
        </div>
    </div>
    <div class="flex-grow-1">
        <div>
            <Progress value={15} color="primary" class="animated-progess custom-progress progress-label" ><div class="label">15%</div> </Progress>
        </div>
    </div>
</div>

<div class="d-flex align-items-center py-2">
    <div class="flex-shrink-0 me-3">
        <div class="avatar-xs">
            <div class="avatar-title bg-light rounded-circle text-muted fs-16">
                <i class="mdi mdi-twitter"></i>
            </div>
        </div>
    </div>
    <div class="flex-grow-1">
        <div>
            <Progress value={25} color="success" class="animated-progess custom-progress progress-label" ><div class="label">25%</div> </Progress>
        </div>
    </div>
</div>

<div class="d-flex align-items-center py-2">
    <div class="flex-shrink-0 me-3">
        <div class="avatar-xs">
            <div class="avatar-title bg-light rounded-circle text-muted fs-16">
                <i class="mdi mdi-github"></i>
            </div>
        </div>
    </div>
    <div class="flex-grow-1">
        <div>
            <Progress value={50} color="info" class="animated-progess custom-progress progress-label" ><div class="label">30%</div> </Progress>
        </div>
    </div>
</div>
`;

	// Content Progress
	const contentCode = `
<!-- Content Progress -->
<Card class="bg-light overflow-hidden shadow-none">
    <CardBody>
        <div class="d-flex">
            <div class="flex-grow-1">
                <h6 class="mb-0"><b class="text-secondary">30%</b> Update in
                    progress...</h6>
            </div>
            <div class="flex-shrink-0">
                <h6 class="mb-0">1 min left</h6>
            </div>
        </div>
    </CardBody>
    <div >
        <Progress value={30} color="info" class="bg-info-subtle rounded-0" />
    </div>
</Card>

<Card class="bg-light overflow-hidden shadow-none">
    <CardBody>
        <div class="d-flex">
            <div class="flex-grow-1">
                <h6 class="mb-0"><b class="text-success">60%</b> Update in
                    progress...</h6>
            </div>
            <div class="flex-shrink-0">
                <h6 class="mb-0">45s left</h6>
            </div>
        </div>
    </CardBody>
    <div>
        <Progress value={60} color="success" class="bg-success-subtle rounded-0" />
    </div>
</Card>

<Card class="bg-light overflow-hidden shadow-none">
    <CardBody>
        <div class="d-flex">
            <div class="flex-grow-1">
                <h6 class="mb-0"><b class="text-danger">82%</b> Update in
                    progress...</h6>
            </div>
            <div class="flex-shrink-0">
                <h6 class="mb-0">25s left</h6>
            </div>
        </div>
    </CardBody>
    <div>
        <Progress value={82} color="danger" class="bg-danger-subtle rounded-0" />
    </div>
</Card>
`;

	// Progress with Steps
	const progressWithStepCode = `
<!-- Progress with Steps -->
<div class="position-relative m-4">
    <Progress value={50} style="height: 1px" />
    <Button size="sm" color="primary" class="position-absolute top-0 start-0 translate-middle rounded-pill" style="width: 2rem; height: 2rem">1</Button>
    <Button size="sm" color="primary" class="position-absolute top-0 start-50 translate-middle rounded-pill" style="width: 2rem; height: 2rem">2</Button>
    <Button size="sm" color="light" class="position-absolute top-0 start-100 translate-middle rounded-pill" style="width: 2rem; height: 2rem">3</Button>
</div>
`;

	// Step Progress with Arrow
	const stepProgressArrowCode = `
<!-- Step Progress with Arrow -->
<Progress multi class='progress-step-arrow progress-info'>
    <Progress bar value="35"> Step 1 </Progress>
    <Progress bar value="35"> Step 2 </Progress>
    <Progress bar value="35" color="light" class="text-dark"> Step 3 </Progress>
</Progress>
`;
</script>

<svelte:head>
	<title>Progress | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Progress" pageTitle="Base UI" />
		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Default Progress" />

					<CardBody>
						<p class="text-muted">A Default Progress Example.</p>

						<div class="live-preview">
							<div class="mb-4">
								<Progress value={0} />
							</div>
							<div class="mb-4">
								<Progress value={25} />
							</div>
							<div class="mb-4">
								<Progress value={50} />
							</div>
							<div class="mb-4">
								<Progress value={75} />
							</div>
							<div>
								<Progress value={100} />
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={defaultProgressCode}
								id="defaultProgressCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Progress with background color" />

					<CardBody>
						<p class="text-muted">
							Use <code>color="Required Color"</code> attribute to
							progress bar class with the below-mentioned color variation
							to set the background color progress bar.
						</p>

						<div class="live-preview">
							<div class="mb-4">
								<Progress color="primary" value={15} />
							</div>
							<div class="mb-4">
								<Progress color="success" value={25} />
							</div>
							<div class="mb-4">
								<Progress color="info" value={50} />
							</div>
							<div class="mb-4">
								<Progress color="warning" value={75} />
							</div>
							<div>
								<Progress color="danger" value={100} />
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={backgroundColorCode}
								id="backgroundColorCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Progress with Label" />

					<CardBody>
						<p class="text-muted">
							Add labels to your progress bars by placing text
							within the progress-bar.
						</p>

						<div class="live-preview">
							<Progress color="primary" value={25}>25%</Progress>
						</div>

						<div class="d-none code-view">
							<PrismCode code={labelCode} id="labelCode" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Multiple Bars" />

					<CardBody>
						<p class="text-muted">
							Multiple bar color to change the appearance of
							individual progress bars.
						</p>

						<div class="live-preview">
							<div>
								<Progress multi>
									<Progress bar value="15" />
									<Progress bar color="success" value="30" />
									<Progress bar color="info" value="20" />
								</Progress>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={multipleBarsCode}
								id="multipleBarsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Height" />

					<CardBody>
						<p class="text-muted">
							Use <code>progress-sm</code>,
							<code>progress-lg</code>, or
							<code>progress-xl</code> class to set the different heights
							of progress.
						</p>
						<div class="live-preview">
							<div class="mb-4">
								<h5 class="fs-13">Small Progress</h5>
								<Progress
									color="primary"
									value={25}
									class="progress-sm"
								/>
							</div>
							<div class="mb-4">
								<h5 class="fs-13">Default Progress</h5>
								<Progress
									color="success"
									value={40}
									class="progress-md"
								/>
							</div>
							<div class="mb-4">
								<h5 class="fs-13">Large Progress</h5>
								<Progress
									color="warning"
									value={50}
									class="progress-lg"
								/>
							</div>
							<div>
								<h5 class="fs-13">Extra Large Progress</h5>
								<Progress
									color="danger"
									value={70}
									class="progress-xl"
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode code={heightCode} id="heightCode" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Striped Progress" />

					<CardBody>
						<p class="text-muted">
							Use <code>striped</code> attribute to add strip to the
							progress.
						</p>
						<div class="live-preview">
							<div class="mb-4">
								<Progress striped value={25} />
							</div>
							<div>
								<Progress color="success" striped value={40} />
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode code={stripedCode} id="stripedCode" />
						</div>
					</CardBody>
				</Card>

				<Card>
					<PreviewCardHeader title="Animated Striped Progress" />

					<CardBody>
						<p class="text-muted">
							Use <code>striped animated</code> attribute to add strip
							with animation to the progress.
						</p>

						<div class="live-preview">
							<div>
								<Progress value={75} striped animated />
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={animatedStripedCode}
								id="animatedStripedCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Gradient Progress" />

					<CardBody>
						<p class="text-muted">
							Use <code>bg-gradient</code> class to show gradient progress
							bar.
						</p>

						<div class="live-preview">
							<div class="mb-4">
								<Progress value={15} class="bg-gradient" />
							</div>
							<div class="mb-4">
								<Progress
									color="success"
									value={25}
									class="bg-gradient"
								/>
							</div>
							<div class="mb-4">
								<Progress
									color="info"
									value={50}
									class="bg-gradient"
								/>
							</div>
							<div class="mb-4">
								<Progress
									color="warning"
									value={75}
									class="bg-gradient"
								/>
							</div>
							<div>
								<Progress
									color="danger"
									value={100}
									class="bg-gradient"
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode code={gradientCode} id="gradientCode" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Animated Progress" />

					<CardBody>
						<p class="text-muted">
							Use <code>animated-progess</code> class to show progress
							with animation.
						</p>
						<div class="live-preview">
							<div class="mb-4">
								<Progress value={15} class="animated-progess" />
							</div>
							<div class="mb-4">
								<Progress
									value={25}
									color="success"
									class="animated-progess"
								/>
							</div>
							<div class="mb-4">
								<Progress
									value={50}
									color="info"
									class="animated-progess"
								/>
							</div>
							<div class="mb-4">
								<Progress
									value={75}
									color="warning"
									class="animated-progess"
								/>
							</div>
							<div>
								<Progress
									value={100}
									color="danger"
									class="animated-progess"
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode code={animatedCode} id="animatedCode" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Custom Progress" />

					<CardBody>
						<p class="text-muted">
							Use <code>animated-progess custom-progess </code> class
							to show custom progress with animation.
						</p>
						<div class="live-preview">
							<div class="mb-4">
								<Progress
									value={15}
									color="primary"
									class="animated-progess custom-progress"
								/>
							</div>
							<div class="mb-4">
								<Progress
									value={25}
									color="success"
									class="animated-progess custom-progress"
								/>
							</div>
							<div class="mb-4">
								<Progress
									value={50}
									color="info"
									class="animated-progess custom-progress"
								/>
							</div>
							<div class="mb-4">
								<Progress
									value={75}
									color="warning"
									class="animated-progess custom-progress"
								/>
							</div>
							<div>
								<Progress
									value={100}
									color="danger"
									class="animated-progess custom-progress"
								/>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode code={customCode} id="customCode" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Custom Progress with Label" />

					<CardBody>
						<p class="text-muted">
							Use <code
								>animated-progess custom-progess progress-label</code
							> class to show custom progress with animation and label.
						</p>
						<div class="live-preview">
							<div class="d-flex align-items-center pb-2 mt-4">
								<div class="flex-shrink-0 me-3">
									<div class="avatar-xs">
										<div
											class="avatar-title bg-light rounded-circle text-muted fs-16"
										>
											<i class="mdi mdi-facebook" />
										</div>
									</div>
								</div>
								<div class="flex-grow-1">
									<div>
										<Progress
											value={15}
											color="primary"
											class="animated-progess custom-progress progress-label"
											><div class="label">15%</div>
										</Progress>
									</div>
								</div>
							</div>

							<div class="d-flex align-items-center py-2">
								<div class="flex-shrink-0 me-3">
									<div class="avatar-xs">
										<div
											class="avatar-title bg-light rounded-circle text-muted fs-16"
										>
											<i class="mdi mdi-twitter" />
										</div>
									</div>
								</div>
								<div class="flex-grow-1">
									<div>
										<Progress
											value={25}
											color="success"
											class="animated-progess custom-progress progress-label"
											><div class="label">25%</div>
										</Progress>
									</div>
								</div>
							</div>

							<div class="d-flex align-items-center py-2">
								<div class="flex-shrink-0 me-3">
									<div class="avatar-xs">
										<div
											class="avatar-title bg-light rounded-circle text-muted fs-16"
										>
											<i class="mdi mdi-github" />
										</div>
									</div>
								</div>
								<div class="flex-grow-1">
									<div>
										<Progress
											value={50}
											color="info"
											class="animated-progess custom-progress progress-label"
											><div class="label">30%</div>
										</Progress>
									</div>
								</div>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={customProgressCode}
								id="customProgressCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Content Progress" />
					<CardBody>
						<p class="text-muted pb-2">
							Example of progress with content wrapped in
							progress.
						</p>

						<div class="live-preview">
							<Card class="bg-light overflow-hidden shadow-none">
								<CardBody>
									<div class="d-flex">
										<div class="flex-grow-1">
											<h6 class="mb-0">
												<b class="text-secondary">30%</b
												> Update in progress...
											</h6>
										</div>
										<div class="flex-shrink-0">
											<h6 class="mb-0">1 min left</h6>
										</div>
									</div>
								</CardBody>
								<div>
									<Progress
										value={30}
										color="secondary"
										class="bg-secondary-subtle rounded-0"
									/>
								</div>
							</Card>

							<Card class="bg-light overflow-hidden shadow-none">
								<CardBody>
									<div class="d-flex">
										<div class="flex-grow-1">
											<h6 class="mb-0">
												<b class="text-success">60%</b> Update
												in progress...
											</h6>
										</div>
										<div class="flex-shrink-0">
											<h6 class="mb-0">45s left</h6>
										</div>
									</div>
								</CardBody>
								<div>
									<Progress
										value={60}
										color="success"
										class="bg-success-subtle rounded-0"
									/>
								</div>
							</Card>

							<Card class="bg-light overflow-hidden shadow-none">
								<CardBody>
									<div class="d-flex">
										<div class="flex-grow-1">
											<h6 class="mb-0">
												<b class="text-danger">82%</b> Update
												in progress...
											</h6>
										</div>
										<div class="flex-shrink-0">
											<h6 class="mb-0">25s left</h6>
										</div>
									</div>
								</CardBody>
								<div>
									<Progress
										value={82}
										color="danger"
										class="bg-danger-subtle rounded-0"
									/>
								</div>
							</Card>
						</div>

						<div class="d-none code-view">
							<PrismCode code={contentCode} id="contentCode" />
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Progress with Steps" />

					<CardBody>
						<p class="text-muted pb-2">
							Here is the example of progress which is represented
							by steps completion.
						</p>

						<div class="live-preview">
							<div class="position-relative m-4">
								<Progress value={50} style="height: 1px" />
								<Button
									size="sm"
									color="primary"
									class="position-absolute top-0 start-0 translate-middle rounded-pill"
									style="width: 2rem; height: 2rem">1</Button
								>
								<Button
									size="sm"
									color="primary"
									class="position-absolute top-0 start-50 translate-middle rounded-pill"
									style="width: 2rem; height: 2rem">2</Button
								>
								<Button
									size="sm"
									color="light"
									class="position-absolute top-0 start-100 translate-middle rounded-pill"
									style="width: 2rem; height: 2rem">3</Button
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={progressWithStepCode}
								id="progressWithStepCode"
							/>
						</div>
					</CardBody>
				</Card>

				<Card>
					<PreviewCardHeader title="Step Progress with Arrow" />

					<CardBody>
						<p class="text-muted pb-2">
							Use <code>progress-step-arrow </code>class to create
							step progress with an arrow.
						</p>
						<div class="live-preview">
							<Progress
								multi
								class="progress-step-arrow progress-info"
							>
								<Progress bar value="35">Step 1</Progress>
								<Progress bar value="35">Step 2</Progress>
								<Progress
									bar
									value="35"
									color="light"
									class="text-dark">Step 3</Progress
								>
							</Progress>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={stepProgressArrowCode}
								id="stepProgressArrowCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
