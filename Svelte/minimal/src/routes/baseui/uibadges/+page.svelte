<script>
	import {
		Badge,
		Button,
		Card,
		CardBody,
		Col,
		Container,
		Row,
	} from "sveltestrap";

	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";

	// Default Badges
	const defaultBadgesCode = `
<Badge color="primary"> Primary </Badge>

<Badge color="secondary"> Secondary </Badge>

<Badge color="success"> Success </Badge>

<Badge color="info"> Info </Badge>

<Badge color="warning"> Warning </Badge>

<Badge color="danger"> Danger </Badge>

<Badge color="dark"> Dark </Badge>

<Badge color="light" class="text-dark"> Light </Badge>
`;

	// Soft Badges
	const softBadgesCode = `
<span class="badge bg-primary-subtle text-primary">Primary</span>

<span class="badge bg-secondary-subtle text-secondary">Secondary</span>

<span class="badge bg-success-subtle text-success">Success</span>

<span class="badge bg-info-subtle text-info">Info</span>

<span class="badge bg-warning-subtle text-warning">Warning</span>

<span class="badge bg-danger-subtle text-danger">Danger</span>

<span class="badge bg-dark-subtle text-dark">Dark</span>

<span class="badge bg-light-subtle text-body">Light</span>
`;

	// Outline Badges
	const outlineBadgesCode = `
<span class="badge border border-primary text-primary">Primary</span>

<span class="badge border border-secondary text-secondary">Secondary</span>

<span class="badge border border-success text-success">Success</span>

<span class="badge border border-info text-info">Info</span>

<span class="badge border border-warning text-warning">Warning</span>

<span class="badge border border-danger text-danger">Danger</span>

<span class="badge border border-dark text-dark">Dark</span>    
`;

	// Rounded Pill Badges
	const roundedPillBadgesCode = `
<Badge color="primary" pill> Primary </Badge>

<Badge color="secondary" pill> Secondary </Badge>

<Badge color="success" pill> Success </Badge>

<Badge color="info" pill> Info </Badge>

<Badge color="warning" pill> Warning </Badge>

<Badge color="danger" pill> Danger </Badge>

<Badge color="dark" pill> Dark </Badge>

<Badge color="light" class="text-dark" pill> Light </Badge>

`;

	// Label Badges
	const labelPillBadgesCode = `
<Badge color="primary" pill> Primary </Badge>

<Badge color="secondary" pill> Secondary </Badge>

<Badge color="success" pill> Success </Badge>

<Badge color="info" pill> Info </Badge>

<Badge color="warning" pill> Warning </Badge>

<Badge color="danger" pill> Danger </Badge>

<Badge color="dark" pill> Dark </Badge>

<Badge color="light" class="text-dark" pill> Light </Badge>

`;

	// Example of the badge used in the HTML Heading
	const htmlBadgesCode = `
<h1>Example heading  <Badge color="secondary"> New </Badge> </h1>

<h2>Example heading  <Badge color="secondary"> New </Badge> </h2>

<h3>Example heading  <Badge color="secondary"> New </Badge> </h3>

<h4>Example heading  <Badge color="secondary"> New </Badge> </h4>

<h5>Example heading  <Badge color="secondary"> New </Badge> </h5>

<h6 class="mb-0">Example heading  <Badge color="secondary"> New </Badge> </h6>

`;

	// Rounded Pill Badges with soft effect
	const roundSoftBadgesCode = `
<span class="badge rounded-pill bg-primary-subtle text-primary">Primary</span>

<span class="badge rounded-pill bg-secondary-subtle text-secondary">Secondary</span>

<span class="badge rounded-pill bg-success-subtle text-success">Success</span>

<span class="badge rounded-pill bg-info-subtle text-info">Info</span>

<span class="badge rounded-pill bg-warning-subtle text-warning">Warning</span>

<span class="badge rounded-pill bg-danger-subtle text-danger">Danger</span>

<span class="badge rounded-pill bg-dark-subtle text-dark">Dark</span>

<span class="badge rounded-pill bg-light-subtle text-body">Light</span>
`;

	// Soft Border Badges

	const softBorderBadgesCode = `
<span class="badge bg-primary-subtle text-primary badge-border">Primary</span>

<span class="badge bg-secondary-subtle text-secondary badge-border">Secondary</span>

<span class="badge bg-success-subtle text-success badge-border">Success</span>

<span class="badge bg-info-subtle text-info badge-border">Info</span>

<span class="badge bg-warning-subtle text-warning badge-border">Warning</span>

<span class="badge bg-danger-subtle text-danger badge-border">Danger</span>

<span class="badge bg-dark-subtle text-dark badge-border">Dark</span>

<span class="badge bg-light-subtle text-body badge-border">Light</span>
`;

	// Outline Pill Badges
	const outlinePillBadgesCode = `
<span class="badge rounded-pill border border-primary text-primary">Primary</span>

<span class="badge rounded-pill border border-secondary text-secondary">Secondary</span>

<span class="badge rounded-pill border border-success text-success">Success</span>

<span class="badge rounded-pill border border-info text-info">Info</span>

<span class="badge rounded-pill border border-warning text-warning">Warning</span>

<span class="badge rounded-pill border border-danger text-danger">Danger</span>

<span class="badge rounded-pill border border-dark text-dark">Dark</span>

<span class="badge rounded-pill border border-light text-light">Light</span>
`;

	// Button Position Badges
	const buttonPositionBadgesCode = `
<Button color="primary" class="position-relative">
    Mails 
    <Badge pill color="success" class="position-absolute top-0 start-100 translate-middle">+99
        <span class="visually-hidden">unread messages</span></Badge>
</Button>

<Button color="light" class="position-relative">
    Alerts <span
        class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-danger p-1"><span
            class="visually-hidden">unread messages</span></span>
</Button>

<Button type="button" color="primary" class="position-relative p-0 avatar-xs rounded">
    <span class="avatar-title bg-transparent">
        <i class="bx bxs-envelope"></i>
    </span>
    <span
        class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-danger p-1"><span
            class="visually-hidden">unread messages</span></span>
</Button>

<Button color="light" class="position-relative p-0 avatar-xs rounded-circle">
    <span class="avatar-title bg-transparent text-reset">
        <i class="bx bxs-bell"></i>
    </span>
</Button>

<Button color="light" class="position-relative p-0 avatar-xs rounded-circle">
    <span class="avatar-title bg-transparent text-reset">
        <i class="bx bx-menu"></i>
    </span>
    <span
        class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-success p-1"><span
            class="visually-hidden">unread messages</span></span>
</Button>
`;

	// Badges With Button

	const buttonBadgesCode = `
<Button color="primary">
    Notifications <Badge color="success" class="ms-1">4</Badge>
</Button>
<Button color="success">
    Messages <Badge color="danger" class="ms-1">2</Badge>
</Button>
<Button color="secondary" outline>
    Draft <Badge color="success" class="ms-1">2</Badge>
</Button>
`;

	// Gradient Badges

	const gradientBadgesCode = `
<Badge class="badge-gradient-primary">Primary</Badge>

<Badge class="badge-gradient-secondary">Secondary</Badge>

<Badge class="badge-gradient-success">Success</Badge>

<Badge class="badge-gradient-danger">Danger</Badge>

<Badge class="badge-gradient-warning">Warning</Badge>

<Badge class="badge-gradient-info">Info</Badge>

<Badge class="badge-gradient-dark">Dark</Badge>
`;
</script>

<svelte:head>
	<title>Badges | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Badges" pageTitle="Base UI" />
		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Default Badges" />
					<CardBody>
						<p class="text-muted">
							Use the <code>Badge</code> tag to set a default badge.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Badge color="primary">Primary</Badge>
								<Badge color="secondary">Secondary</Badge>
								<Badge color="success">Success</Badge>
								<Badge color="info">Info</Badge>
								<Badge color="warning">Warning</Badge>
								<Badge color="danger">Danger</Badge>
								<Badge color="dark">Dark</Badge>
								<Badge color="light" class="text-dark"
									>Light</Badge
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={defaultBadgesCode}
								id="defaultBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Soft Badges" />
					<CardBody>
						<p class="text-muted">
							Use the <code>bg-*-subtle text-*</code> class with the
							below-mentioned variation to create a softer badge.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<span
									class="badge bg-primary-subtle text-primary"
									>Primary</span
								>
								<span
									class="badge bg-secondary-subtle text-secondary"
									>Secondary</span
								>
								<span
									class="badge bg-success-subtle text-success"
									>Success</span
								>
								<span class="badge bg-info-subtle text-info"
									>Info</span
								>
								<span
									class="badge bg-warning-subtle text-warning"
									>Warning</span
								>
								<span class="badge bg-danger-subtle text-danger"
									>Danger</span
								>
								<span class="badge bg-dark-subtle text-dark"
									>Dark</span
								>
								<span
									class="badge bg-light-subtle text-body text-dark"
									>Light</span
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={softBadgesCode}
								id="softBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Outline Badges" />
					<CardBody>
						<p class="text-muted">
							Use the <code>border, border-* text-*</code> class with
							the below-mentioned variation to create a badge with
							the outline.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<span
									class="badge border border-primary text-primary"
									>Primary</span
								>
								<span
									class="badge border border-secondary text-secondary"
									>Secondary</span
								>
								<span
									class="badge border border-success text-success"
									>Success</span
								>
								<span class="badge border border-info text-info"
									>Info</span
								>
								<span
									class="badge border border-warning text-warning"
									>Warning</span
								>
								<span
									class="badge border border-danger text-danger"
									>Danger</span
								>
								<span class="badge border border-dark text-dark"
									>Dark</span
								>
								<span
									class="badge border border-light text-light text-dark"
									>Light</span
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={outlineBadgesCode}
								id="outlineBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Rounded Pill Badges" />
					<CardBody>
						<p class="text-muted">
							Use the <code>rounded-pill</code> class to make badges
							more rounded with a larger border-radius.
						</p>

						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Badge color="primary" pill>Primary</Badge>
								<Badge color="secondary" pill>Secondary</Badge>
								<Badge color="success" pill>Success</Badge>
								<Badge color="info" pill>Info</Badge>
								<Badge color="warning" pill>Warning</Badge>
								<Badge color="danger" pill>Danger</Badge>
								<Badge color="dark" pill>Dark</Badge>
								<Badge color="light" class="text-dark" pill
									>Light</Badge
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={roundedPillBadgesCode}
								id="roundedPillBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader
						title="Rounded Pill Badges with soft effect"
					/>
					<CardBody>
						<p class="text-muted">
							Use the <code>rounded-pill bg-*-subtle text-*</code>
							class with the below-mentioned variation to create a
							badge more rounded with a soft background.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<span
									class="badge rounded-pill bg-primary-subtle text-primary"
									>Primary</span
								>
								<span
									class="badge rounded-pill bg-secondary-subtle text-secondary"
									>Secondary</span
								>
								<span
									class="badge rounded-pill bg-success-subtle text-success"
									>Success</span
								>
								<span
									class="badge rounded-pill bg-info-subtle text-info"
									>Info</span
								>
								<span
									class="badge rounded-pill bg-warning-subtle text-warning"
									>Warning</span
								>
								<span
									class="badge rounded-pill bg-danger-subtle text-danger"
									>Danger</span
								>
								<span
									class="badge rounded-pill bg-dark-subtle text-dark"
									>Dark</span
								>
								<span
									class="badge rounded-pill badge-light-subtle text-body"
									>Light</span
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={roundSoftBadgesCode}
								id="roundSoftBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Soft Border Badges" />
					<CardBody>
						<p class="text-muted">
							Use the <code>badge-border</code> and
							<code>bg-*-subtle text-*</code> with below mentioned
							modifier classes to make badges with border & soft backgorund.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<span
									class="badge bg-primary-subtle text-primary badge-border"
									>Primary</span
								>
								<span
									class="badge bg-secondary-subtle text-secondary badge-border"
									>Secondary</span
								>
								<span
									class="badge bg-success-subtle text-success badge-border"
									>Success</span
								>
								<span
									class="badge bg-danger-subtle text-danger badge-border"
									>Danger</span
								>
								<span
									class="badge bg-warning-subtle text-warning badge-border"
									>Warning</span
								>
								<span
									class="badge bg-info-subtle text-info badge-border"
									>Info</span
								>
								<span
									class="badge bg-dark-subtle text-dark badge-border"
									>Dark</span
								>
								<span
									class="badge bg-light-subtle text-body badge-border text-dark"
									>Light</span
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={softBorderBadgesCode}
								id="softBorderBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Outline Pill Badges" />
					<CardBody>
						<p class="text-muted">
							Use the <code
								>rounded-pill border, border-* text-*</code
							> class with the below-mentioned variation to create
							a outline Pill badge.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<span
									class="badge rounded-pill border border-primary text-primary"
									>Primary</span
								>
								<span
									class="badge rounded-pill border border-secondary text-secondary"
									>Secondary</span
								>
								<span
									class="badge rounded-pill border border-success text-success"
									>Success</span
								>
								<span
									class="badge rounded-pill border border-info text-info"
									>Info</span
								>
								<span
									class="badge rounded-pill border border-warning text-warning"
									>Warning</span
								>
								<span
									class="badge rounded-pill border border-danger text-danger"
									>Danger</span
								>
								<span
									class="badge rounded-pill border border-dark text-dark"
									>Dark</span
								>
								<span
									class="badge rounded-pill border border-light text-light text-dark"
									>Light</span
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={outlinePillBadgesCode}
								id="outlinePillBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Label Badges" />

					<CardBody>
						<p class="text-muted">
							Use the <code>badge-label</code> class to create a badge
							with the label.
						</p>

						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Badge color="primary" class="badge-label bg-primary">
									<i class="mdi mdi-circle-medium" /> Primary
								</Badge>
								<Badge color="secondary" class="badge-label bg-secondary">
									<i class="mdi mdi-circle-medium" /> Secondary
								</Badge>
								<Badge color="success" class="badge-label bg-success">
									<i class="mdi mdi-circle-medium" /> Success
								</Badge>
								<Badge color="danger" class="badge-label bg-danger">
									<i class="mdi mdi-circle-medium" /> Danger
								</Badge>
								<Badge color="warning" class="badge-label bg-warning">
									<i class="mdi mdi-circle-medium" /> Warning
								</Badge>
								<Badge color="info" class="badge-label bg-info">
									<i class="mdi mdi-circle-medium" /> Info
								</Badge>
								<Badge color="dark" class="badge-label bg-dark">
									<i class="mdi mdi-circle-medium" /> Dark
								</Badge>
								<Badge
									color="light"
									class="badge-label bg-light text-body"
								>
									<i class="mdi mdi-circle-medium" /> Light
								</Badge>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={labelPillBadgesCode}
								id="labelPillBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={12}>
				<Card>
					<PreviewCardHeader title="Gradient Badges" />

					<CardBody>
						<p class="text-muted">
							Use the <code>badge-gradient-*</code> class to create
							a gradient styled badge.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Badge class="badge-gradient-primary"
									>Primary</Badge
								>
								<Badge class="badge-gradient-secondary"
									>Secondary</Badge
								>
								<Badge class="badge-gradient-success"
									>Success</Badge
								>
								<Badge class="badge-gradient-danger"
									>Danger</Badge
								>
								<Badge class="badge-gradient-warning"
									>Warning</Badge
								>
								<Badge class="badge-gradient-info">Info</Badge>
								<Badge class="badge-gradient-dark">Dark</Badge>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={labelPillBadgesCode}
								id="labelPillBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Button Position Badges" />

					<CardBody>
						<p class="text-muted">
							Use the below utilities to modify a badge and
							position it in the corner of a link or button.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-3">
								<Button
									color="primary"
									class="position-relative"
								>
									Mails <Badge
										pill
										color="success"
										class="position-absolute top-0 start-100 translate-middle"
										>+99
										<span class="visually-hidden"
											>unread messages</span
										></Badge
									>
								</Button>

								<Button color="light" class="position-relative">
									Alerts <span
										class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-danger p-1"
										><span class="visually-hidden"
											>unread messages</span
										></span
									>
								</Button>

								<Button
									type="button"
									color="primary"
									class="position-relative p-0 avatar-xs rounded"
								>
									<span class="avatar-title bg-transparent">
										<i class="bx bxs-envelope" />
									</span>
									<span
										class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-danger p-1"
										><span class="visually-hidden"
											>unread messages</span
										></span
									>
								</Button>

								<Button
									color="light"
									class="position-relative p-0 avatar-xs rounded-circle"
								>
									<span
										class="avatar-title bg-transparent text-reset"
									>
										<i class="bx bxs-bell" />
									</span>
								</Button>

								<Button
									color="light"
									class="position-relative p-0 avatar-xs rounded-circle"
								>
									<span
										class="avatar-title bg-transparent text-reset"
									>
										<i class="bx bx-menu" />
									</span>
									<span
										class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-success p-1"
										><span class="visually-hidden"
											>unread messages</span
										></span
									>
								</Button>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={buttonPositionBadgesCode}
								id="buttonPositionBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>

				<Card>
					<PreviewCardHeader title="Badges With Button" />
					<CardBody>
						<p class="text-muted">
							Badges can be used as part of buttons to provide a
							counter.
						</p>

						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button color="primary">
									Notifications <Badge
										color="success"
										class="ms-1">4</Badge
									>
								</Button>
								<Button color="success">
									Messages <Badge color="danger" class="ms-1"
										>2</Badge
									>
								</Button>
								<Button color="secondary" outline>
									Draft <Badge color="success" class="ms-1"
										>2</Badge
									>
								</Button>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={buttonBadgesCode}
								id="buttonBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Badges with Heading" />
					<CardBody>
						<p class="text-muted">
							Example of the badge used in the HTML Heading.
						</p>
						<div class="live-preview">
							<h1>
								Example heading <Badge color="secondary"
									>New</Badge
								>
							</h1>
							<h2>
								Example heading <Badge color="secondary"
									>New</Badge
								>
							</h2>
							<h3>
								Example heading <Badge color="secondary"
									>New</Badge
								>
							</h3>
							<h4>
								Example heading <Badge color="secondary"
									>New</Badge
								>
							</h4>
							<h5>
								Example heading <Badge color="secondary"
									>New</Badge
								>
							</h5>
							<h6 class="mb-0">
								Example heading <Badge color="secondary"
									>New</Badge
								>
							</h6>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={htmlBadgesCode}
								id="htmlBadgesCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
