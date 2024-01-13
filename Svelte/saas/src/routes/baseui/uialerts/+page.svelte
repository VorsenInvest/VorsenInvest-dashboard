<script>
	import { Alert, Card, CardBody, Col, Container, Row } from "sveltestrap";

	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";

	const defaultAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary">
    <strong> Hi! </strong> A simple <b>Primary alert</b> —check it out!
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary">
    <strong> How are you! </strong> A simple <b>secondary alert</b> —check it out!
</Alert>

<!-- Success Alert -->
<Alert color="success">
    <strong> Yey! Everything worked! </strong> A simple <b>success alert</b> —check it out!
</Alert>

<!-- Danger Alert -->
<Alert color="danger">
    <strong> Something is very wrong! </strong> A simple <b>danger alert</b> —check it out!
</Alert>

<!-- Warning Alert -->
<Alert color="warning">
    <strong> Uh oh, something went wrong </strong> A simple <b>warning alert</b> —check it out!
</Alert>

<!-- Info Alert -->
<Alert color="info">
    <strong> Don't forget' it ! </strong> A simple <b>info alert</b> —check it out!
</Alert>

<!-- Light Alert -->
<Alert color="light">
    <strong> Mind Your Step! </strong> A simple <b>light alert</b> —check it out!
</Alert>

<!-- Dark Alert -->
<Alert color="dark">
    <strong> Did you know? </strong> A simple <b>dark alert</b> —check it out!
</Alert>
`;

	// Borderless Alerts

	const borderlessAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="alert-borderless">
    <strong> Hi! </strong> A simple <b>Primary alert</b> —check it out!
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary" class="alert-borderless">
    <strong> How are you! </strong> A simple <b>secondary alert</b> —check it out!
</Alert>

<!-- Success Alert -->
<Alert color="success" class="alert-borderless">
    <strong> Yey! Everything worked! </strong> A simple <b>success alert</b> —check it out!
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="alert-borderless mb-xl-0">
    <strong> Something is very wrong! </strong> A simple danger alert—check it out!
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="alert-borderless">
    <strong> Uh oh, something went wrong </strong> A simple <b>warning alert</b> —check it out!
</Alert>

<!-- Info Alert -->
<Alert color="info" class="alert-borderless">
    <strong>Don't forget' it !</strong> A simple <b>info alert</b> —check it out!
</Alert>

<!-- Light Alert -->
<Alert color="light" class="alert-borderless bg-light">
    <strong>Mind Your Step!</strong> A simple <b>light alert</b> —check it out!
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="alert-borderless mb-0">
    <strong>Did you know?</strong> A simple <b>dark alert</b> —check it out!
</Alert>`;

	const dismissingAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary">
    <strong> Hi! </strong> A simple <b>Dismissible primary Alert </b> — check it out!
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary">
    <strong> How are you! </strong> A simple <b>Dismissible secondary alert</b> —check it out!
</Alert>

<!-- Success Alert -->
<Alert color="success">
    <strong>Right Way !</strong> A simple <b>Dismissible success alert</b> —check it out!
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="mb-xl-0">
    <strong> Something is very wrong! </strong> A simple <b>Dismissible danger alert</b> —check it out!
</Alert>

<!-- Warning Alert -->
<Alert color="warning">
    <strong>Welcome Back!</strong> A simple <b>Dismissible warning alert</b> —check it out!
</Alert>

<!-- Info Alert -->
<Alert color="info">
    <strong>Don't forget' it !</strong> A simple <b>Dismissible info alert</b> —check it out!
</Alert>

<!-- Light Alert -->
<Alert color="light">
    <strong>Mind Your Step!</strong> A simple <b>Dismissible light alert</b> —check it out!
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="mb-0">
    <strong>Did you know?</strong> A simple <b>Dismissible dark alert</b> —check it out!
</Alert>`;

	const linkColorAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary">
    A simple Primary alert with <Link href={null} class="alert-link">an example link</Link>. Give it a click if you like.
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary">
    A simple Secondary alert with <Link href={null} class="alert-link">an example link</Link>.  Give it a click if you like.
</Alert>

<!-- Success Alert -->
<Alert color="success">
    A simple Success alert with <Link href={null} class="alert-link">an example link</Link>. Give it a click if you like.
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="mb-xl-0">
    A simple Danger alert with <Link href={null} class="alert-link">an example link</Link>. Give it a click if you like.
</Alert>

<!-- Warning Alert -->
<Alert color="warning">
    A simple Warning alert with <Link href={null} class="alert-link">an example link</Link>. Give  it a click if you like.
</Alert>

<!-- Info Alert -->
<Alert color="info">
    A simple Info alert with <Link href={null} class="alert-link">an example link</Link>. Give it  a click if you like.
</Alert>

<!-- Light Alert -->
<Alert color="light">
    A simple Light alert with <Link href={null} class="alert-link">an example link</Link>. Give it a click if you like.
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="mb-0">
    A simple Dark alert with <Link href={null} class="alert-link">an example link</Link>. Give it a click if you like.
</Alert>`;

	// Live Alert Example

	const liveAlertsCode = `
const [show, setShow] = useState(false);
<Alert color="success" isOpen={show} toggle={() => setShow(false)}>
    Nice, you triggered this alert message!
</Alert>
<button type="button" class="btn btn-primary" id="liveAlertBtn" onClick={() => setShow(true)}>Show live alert</button>`;

	// Outline Alerts

	const outlineAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="alert-outline">
    <strong> Hi! </strong> - Outline <b>primary alert</b> example
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary" class="alert-outline border-2 bg-body-secondary">
    <strong> How are you! </strong> - Outline <b>secondary alert</b> example
</Alert>

<!-- Success Alert -->
<Alert color="success" class="alert-outline border-2 bg-body-secondary">
    <strong> Yey! Everything worked! </strong> - Outline <b>success alert</b> example
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="alert-outline border-2 bg-body-secondary mb-xl-0">
    <strong> Something is very wrong! </strong> - Outline <b>danger alert</b> example
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="alert-outline border-2 bg-body-secondary">
    <strong> Uh oh, something went wrong! </strong> - Outline <b>warning alert</b> example
</Alert>

<!-- Info Alert -->
<Alert color="info" class="alert-outline border-2 bg-body-secondary">
    <strong>Don't forget' it !</strong> - Outline <b>info alert</b> example
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="alert-outline border-2 bg-body-secondary mb-0">
    <strong>Did you know?</strong> - Outline <b>dark alert</b> example
</Alert>`;

	const leftBorderAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="alert-border-left">
    <i class="ri-user-smile-line me-3 align-middle fs-16"></i><strong>Primary</strong> - Left border alert
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary" class="alert-border-left">
    <i class="ri-check-double-line me-3 align-middle fs-16"></i><strong>Secondary</strong> - Left border alert
</Alert>

<!-- Success Alert -->
<Alert color="success" class="alert-border-left">
    <i class="ri-notification-off-line me-3 align-middle fs-16"></i><strong>Success</strong> - Left border alert
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="alert-border-left mb-xl-0">
    <i class="ri-error-warning-line me-3 align-middle fs-16"></i><strong>Danger</strong> - Left border alert
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="alert-border-left">
    <i class="ri-alert-line me-3 align-middle fs-16"></i><strong>Warning</strong> - Left border alert
</Alert>

<!-- Info Alert -->
<Alert color="info" class="alert-border-left">
    <i class="ri-airplay-line me-3 align-middle fs-16"></i><strong>Info</strong> - Left border alert
</Alert>

<!-- Light Alert -->
<Alert color="light" class="alert-border-left">
    <i class="ri-mail-line me-3 align-middle fs-16"></i><strong>Light</strong> - Left border alert
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="alert-border-left mb-0">
    <i class="ri-refresh-line me-3  align-middle fs-16"></i><strong>Dark</strong> - Left border alert
</Alert>`;

	const labelIconAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="alert-solid alert-label-icon">
    <i class="ri-user-smile-line label-icon"></i><strong>Primary</strong> -Label icon alert 
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary" class="alert-solid alert-label-icon">
    <i class="ri-check-double-line label-icon"></i><strong>Secondary</strong> - Label icon alert
</Alert>

<!-- Success Alert -->
<Alert color="success" class="alert-solid alert-label-icon">
    <i class="ri-notification-off-line label-icon"></i><strong>Success</strong> - Label icon alert
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="alert-solid alert-label-icon mb-xl-0">
    <i class="ri-error-warning-line label-icon"></i><strong>Danger</strong> - Label icon alert
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="alert-solid alert-label-icon">
    <i class="ri-alert-line label-icon"></i><strong>warning</strong> - Label icon alert
</Alert>

<!-- Info Alert -->
<Alert color="info" class="alert-solid alert-label-icon">
    <i class="ri-airplay-line label-icon"></i><strong>Info</strong> - Label icon alert
</Alert>

<!-- Light Alert -->
<Alert color="light" class="alert-solid alert-label-icon">
    <i class="ri-mail-line label-icon"></i><strong>Light</strong> - Label icon alert
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="alert-solid alert-label-icon mb-0">
    <i class="ri-refresh-line label-icon"></i><strong>Dark</strong> - Label icon alert
</Alert>`;

	const topBarAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="alert-top-border">
    <i class="ri-user-smile-line me-3 align-middle fs-16 text-primary"></i><strong>Primary</strong> - Top border alert
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary" class="alert-top-border">
    <i class="ri-check-double-line me-3 align-middle fs-16 text-secondary"></i><strong>Secondary</strong> - Top border alert
</Alert>

<!-- Success Alert -->
<Alert color="success" class="alert-top-border">
    <i class="ri-notification-off-line me-3 align-middle fs-16 text-success"></i><strong>Success</strong> - Top border alert
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="alert-top-border mb-xl-0">
    <i class="ri-error-warning-line me-3 align-middle fs-16 text-danger "></i><strong>Danger</strong> - Top border alert
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="alert-top-border">
    <i class="ri-alert-line me-3 align-middle fs-16 text-warning"></i><strong>Warning</strong> - Top border alert
</Alert>

<!-- Info Alert -->
<Alert color="info" class="alert-top-border">
    <i class="ri-airplay-line me-3 align-middle fs-16 text-info"></i><strong>Info</strong> - Top border alert
</Alert>

<!-- Light Alert -->
<Alert color="light" class="alert-top-border">
    <i class="ri-mail-line me-3 align-middle fs-16 text-dark"></i><strong>Light</strong> - Top border alert
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="alert-top-border mb-0">
    <i class="ri-refresh-line me-3 align-middle fs-16 text-dark"></i><strong>Dark</strong> - Top border alert
</Alert>`;

	const labelIconArrowAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="alert-label-icon label-arrow ">
 <i class="ri-user-smile-line label-icon"></i><strong>Primary</strong> - Label icon arrow alert
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary" class="alert-label-icon label-arrow ">
    <i class="ri-check-double-line label-icon"></i><strong>Secondary</strong> - Label icon arrow alert
</Alert>

<!-- Success Alert -->
<Alert color="success" class="alert-label-icon label-arrow ">
    <i class="ri-notification-off-line label-icon"></i><strong>Success</strong> - Label icon arrow alert
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="alert-label-icon label-arrow mb-xl-0">
    <i class="ri-error-warning-line label-icon"></i><strong>Danger</strong> - Label icon arrow alert
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="alert-label-icon label-arrow ">
    <i class="ri-alert-line label-icon"></i><strong>Warning</strong> - Label icon arrow alert
</Alert>

<!-- Info Alert -->
<Alert color="info" class="alert-label-icon label-arrow ">
    <i class="ri-airplay-line label-icon"></i><strong>Info</strong> - Label icon arrow alert
</Alert>

<!-- Light Alert -->
<Alert color="light" class="alert-label-icon label-arrow ">
    <i class="ri-mail-line label-icon"></i><strong>Light</strong> - Label icon arrow alert
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="alert-label-icon label-arrow mb-0">
    <i class="ri-refresh-line label-icon"></i><strong>Dark</strong> - Label icon arrow alert
</Alert>`;

	// Rounded Label Icon Alerts

	const roundedLabelIconAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="alert-label-icon rounded-label">
    <i class="ri-user-smile-line label-icon"></i><strong>Primary</strong> - Rounded label alert 
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary" class="alert-label-icon rounded-label">
    <i class="ri-check-double-line label-icon"></i><strong>Secondary</strong> - Rounded label alert
</Alert>

<!-- Success Alert -->
<Alert color="success" class="alert-label-icon rounded-label">
    <i class="ri-notification-off-line label-icon"></i><strong>Success</strong> - Rounded label alert
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="alert-label-icon rounded-label">
    <i class="ri-error-warning-line label-icon"></i><strong>Danger</strong> - Rounded label alert
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="alert-label-icon rounded-label">
    <i class="ri-alert-line label-icon"></i><strong>Warning</strong> - Rounded label alert 
</Alert>

<!-- Info Alert -->
<Alert color="info" class="alert-label-icon rounded-label">
    <i class="ri-airplay-line label-icon"></i><strong>Info</strong> - Rounded label alert
</Alert>

<!-- Light Alert -->
<Alert color="light" class="alert-label-icon rounded-label">
    <i class="ri-mail-line label-icon"></i><strong>Light</strong> - Rounded label alert
</Alert>

<!-- Dark Alert -->
<Alert color="dark" class="alert-label-icon rounded-label">
    <i class="ri-refresh-line label-icon"></i><strong>Dark</strong> - Rounded label alert
</Alert>`;

	const additionalContentAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="alert-additional">
<div class="alert-body">
    <div class="d-flex">
        <div class="flex-shrink-0 me-3">
            <i class="ri-error-warning-line fs-16 align-middle"></i>
        </div>
        <div class="flex-grow-1">
        <h5 class="alert-heading">Well done !</h5>
            <p class="mb-0">Aww yeah, you successfully read this important alert message. </p>
        </div>
    </div>
</div>
<div class="alert-content">
    <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
</div>
</Alert>

<!-- Success Alert -->
<Alert color="success" class="alert-additional">
<div class="alert-body">
    <div class="d-flex">
        <div class="flex-shrink-0 me-3">
            <i class="ri-notification-off-line fs-16 align-middle"></i>
        </div>
        <div class="flex-grow-1">
        <h5 class="alert-heading">Yey! Everything worked!</h5>
            <p class="mb-0">This alert needs your attention, but it's not super important.</p>
        </div>
    </div>
</div>
<div class="alert-content">
    <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
</div>
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="alert-additional mb-xl-0">
<div class="alert-body">
    <div class="d-flex">
        <div class="flex-shrink-0 me-3">
            <i class="ri-alert-line fs-16 align-middle"></i>
        </div>
        <div class="flex-grow-1">
        <h5 class="alert-heading">Something is very wrong!</h5>
            <p class="mb-0">Change a few things up and try submitting again.</p>
        </div>
    </div>
</div>
<div class="alert-content">
    <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
</div>
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="alert-additional mb-0">
<div class="alert-body">
    <div class="d-flex">
        <div class="flex-shrink-0 me-3">
            <i class="ri-alert-line fs-16 align-middle"></i>
        </div>
        <div class="flex-grow-1">
        <h5 class="alert-heading">Uh oh, something went wrong!</h5>
            <p class="mb-0">Better check yourself, you're not looking too good.</p>
        </div>
    </div>
</div>
<div class="alert-content">
<p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
</div>
</Alert>
`;

	const solidAlertsCode = `
<!-- Primary Alert -->
<Alert color="primary" class="bg-primary border-primary text-white">  
<strong>Hi!</strong> - Solid
<b>primary alert</b> example
</Alert>

<!-- Secondary Alert -->
<Alert color="secondary" class="bg-secondary border-secondary text-white">
<strong>How are you!</strong> - Solid
<b>secondary alert</b> example
</Alert>

<!-- Success Alert -->
<Alert color="success" class="bg-success border-success text-white">
<strong >Yey! Everything worked! </strong>- Solid <b>success alert</b> example
</Alert>

<!-- Danger Alert -->
<Alert color="danger" class="bg-danger border-danger text-white mb-xl-0"><strong>Something is very wrong!</strong>- Solid <b>danger alert</b> example
</Alert>

<!-- Warning Alert -->
<Alert color="warning" class="bg-warning border-warning text-white">
<strong >Uh oh, something went wrong!</strong>- Solid <b>warning alert</b> example</Alert>

<!-- Info Alert -->
<Alert color="info" class="bg-info border-info text-white">
<strong>Don't forget' it !</strong> -
Solid <b>info alert</b> example
</Alert>

<!-- Light Alert -->
<Alert color="light" class="bg-light border-light text-body">
<strong>Mind Your Step!</strong> - Solid
<b>secondary alert</b> example
</Alert>

<!-- Dark Alert -->
<Alert
color="dark"
class="bg-dark border-primary text-white mb-0"
>
<strong>Did you know?</strong> - Solid
<b>dark alert</b> example
</Alert>`;
</script>

<svelte:head>
	<title>Alerts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid={true}>
		<BreadCrumb title="Alerts" pageTitle="Base UI" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Default Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>alert</code> class to show a default alert.
						</p>
						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>
									<Alert color="primary">
										<strong> Hi! </strong> A simple
										<b>Primary alert</b> —check it out!
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert color="secondary">
										<strong> How are you! </strong> A simple
										<b>secondary alert</b> —check it out!
									</Alert>

									<h6>Success Alert</h6>
									<Alert color="success">
										<strong>
											Yey! Everything worked!
										</strong>
										A simple <b>success alert</b> —check it out!
									</Alert>

									<h6>Danger Alert</h6>
									<Alert color="danger" class="mb-0">
										<strong>
											Something is very wrong!
										</strong>
										A simple <b>danger alert</b> —check it out!
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert color="warning">
										<strong>
											Uh oh, something went wrong
										</strong>
										A simple <b>warning alert</b> —check it out!
									</Alert>

									<h6>Info Alert</h6>
									<Alert color="info">
										<strong>Don't forget' it !</strong> A
										simple <b>info alert</b> —check it out!
									</Alert>

									<h6>Light Alert</h6>
									<Alert color="light">
										<strong>Mind Your Step!</strong> A
										simple <b>light alert</b> —check it out!
									</Alert>

									<h6>Dark Alert</h6>
									<Alert color="dark" class="mb-0">
										<strong>Did you know?</strong> A simple
										<b>dark alert</b> —check it out!
									</Alert>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={defaultAlertsCode}
								id="defaultAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Borderless Alerts" />

					<CardBody>
						<p class="text-muted">
							Use the <code>border-0</code> class to set alert
							without border.
						</p>

						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>
									<Alert
										color="primary"
										class="border-0"
									>
										<strong> Hi! </strong> A simple
										<b>Primary alert</b> —check it out!
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert
										color="secondary"
										class="border-0"
									>
										<strong> How are you! </strong> A simple
										<b>secondary alert</b> —check it out!
									</Alert>

									<h6>Success Alert</h6>
									<Alert
										color="success"
										class="border-0"
									>
										<strong>
											Yey! Everything worked!
										</strong>
										A simple <b>success alert</b> —check it out!
									</Alert>

									<h6>Danger Alert</h6>
									<Alert
										color="danger"
										class="border-0 mb-xl-0"
									>
										<strong>
											Something is very wrong!
										</strong> A simple danger alert—check it
										out!
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert
										color="warning"
										class="border-0"
									>
										<strong>
											Uh oh, something went wrong
										</strong>
										A simple <b>warning alert</b> —check it out!
									</Alert>

									<h6>Info Alert</h6>
									<Alert
										color="info"
										class="border-0"
									>
										<strong>Don't forget' it !</strong> A
										simple <b>info alert</b> —check it out!
									</Alert>

									<h6>Light Alert</h6>
									<Alert
										color="light"
										class="border-0 bg-light"
									>
										<strong>Mind Your Step!</strong> A
										simple <b>light alert</b> —check it out!
									</Alert>

									<h6>Dark Alert</h6>
									<Alert
										color="dark"
										class="border-0 mb-0"
									>
										<strong>Did you know?</strong> A simple
										<b>dark alert</b> —check it out!
									</Alert>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={borderlessAlertsCode}
								id="borderlessAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Dismissing Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>dismissible</code> tag to add dismissing button
							to the alert.
						</p>
						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>
									<Alert color="primary" dismissible>
										<strong> Hi! </strong> A simple
										<b>Dismissible primary Alert </b> — check
										it out!
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert color="secondary" dismissible>
										<strong> How are you! </strong> A simple
										<b>Dismissible secondary alert</b> —check
										it out!
									</Alert>

									<h6>Success Alert</h6>
									<Alert color="success" dismissible>
										<strong>Right Way !</strong> A simple
										<b>Dismissible success alert</b> —check it
										out!
									</Alert>

									<h6>Danger Alert</h6>
									<Alert
										color="danger"
										dismissible
										class="mb-xl-0"
									>
										<strong>
											Something is very wrong!
										</strong>
										A simple
										<b>Dismissible danger alert</b> —check it
										out!
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert color="warning" dismissible>
										<strong>Welcome Back!</strong> A simple
										<b>Dismissible warning alert</b> —check it
										out!
									</Alert>

									<h6>Info Alert</h6>
									<Alert color="info" dismissible>
										<strong>Don't forget' it !</strong> A
										simple <b>Dismissible info alert</b> —check
										it out!
									</Alert>

									<h6>Light Alert</h6>
									<Alert color="light" dismissible>
										<strong>Mind Your Step!</strong> A
										simple <b>Dismissible light alert</b> —check
										it out!
									</Alert>

									<h6>Dark Alert</h6>
									<Alert
										color="dark"
										dismissible
										class="mb-0"
									>
										<strong>Did you know?</strong> A simple
										<b>Dismissible dark alert</b> —check it out!
									</Alert>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={dismissingAlertsCode}
								id="dismissingAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Link Color Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>alert-link</code> class at &lt;a&gt; tag
							to show matching colored links within the given alert.
						</p>

						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>

									<Alert color="primary">
										A simple Primary alert with <Link
											href={null}
											class="alert-link"
											>an example link</Link
										>. Give it a click if you like.
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert color="secondary">
										A simple Secondary alert with <Link
											href={null}
											class="alert-link"
											>an example link</Link
										>. Give it a click if you like.
									</Alert>

									<h6>Success Alert</h6>
									<Alert color="success">
										A simple Success alert with <Link
											href={null}
											class="alert-link"
											>an example link</Link
										>. Give it a click if you like.
									</Alert>

									<h6>Danger Alert</h6>
									<Alert color="danger" class="mb-xl-0">
										A simple Danger alert with <Link
											href={null}
											class="alert-link"
											>an example link</Link
										>. Give it a click if you like.
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert color="warning">
										A simple Warning alert with <Link
											href={null}
											class="alert-link"
											>an example link</Link
										>. Give it a click if you like.
									</Alert>

									<h6>Info Alert</h6>
									<Alert color="info">
										A simple Info alert with <Link
											href={null}
											class="alert-link"
											>an example link</Link
										>. Give it a click if you like.
									</Alert>

									<h6>Light Alert</h6>
									<Alert color="light">
										A simple Light alert with <Link
											href={null}
											class="alert-link"
											>an example link</Link
										>. Give it a click if you like.
									</Alert>

									<h6>Dark Alert</h6>
									<Alert color="dark" class="mb-0">
										A simple Dark alert with <Link
											href={null}
											class="alert-link"
											>an example link</Link
										>. Give it a click if you like.
									</Alert>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={linkColorAlertsCode}
								id="linkColorAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Live Alert Example" />
					<CardBody>
						<p class="text-muted">
							Click the Show live alert button to show an alert on
							button click.
						</p>
						<div class="live-preview">
							<div id="liveAlertPlaceholder">
								<Alert color="success"
									>Nice, you triggered this alert message!</Alert
								>
								<button
									type="button"
									class="btn btn-primary"
									id="liveAlertBtn">Show live alert</button
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={liveAlertsCode}
								id="liveAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Outline Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>border-2 bg-body-secondary</code> class to set an alert
							with outline.
						</p>

						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Outline Alert</h6>

									<Alert
										color="primary"
										class="alert-outline border-2 bg-body-secondary"
										dismissible
									>
										<strong> Hi! </strong> - Outline
										<b>primary alert</b> example
									</Alert>

									<h6>Secondary Outline Alert</h6>
									<Alert
										color="secondary"
										class="alert-outline border-2 bg-body-secondary"
										dismissible
									>
										<strong> How are you! </strong> -
										Outline <b>secondary alert</b> example
									</Alert>

									<h6>Success Outline Alert</h6>
									<Alert
										color="success"
										class="alert-outline border-2 bg-body-secondary"
										dismissible
									>
										<strong>
											Yey! Everything worked!
										</strong>
										- Outline <b>success alert</b> example
									</Alert>

									<h6>Danger Outline Alert</h6>
									<Alert
										color="danger"
										class="alert-outline border-2 bg-body-secondary mb-xl-0"
										dismissible
									>
										<strong>
											Something is very wrong!
										</strong>
										- Outline <b>danger alert</b> example
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Outline Alert</h6>
									<Alert
										color="warning"
										class="alert-outline border-2 bg-body-secondary"
										dismissible
									>
										<strong>
											Uh oh, something went wrong!
										</strong>
										- Outline <b>warning alert</b> example
									</Alert>

									<h6>Info Outline Alert</h6>
									<Alert
										color="info"
										class="alert-outline border-2 bg-body-secondary"
										dismissible
									>
										<strong>Don't forget' it !</strong> -
										Outline <b>info alert</b> example
									</Alert>

									<h6>Dark Alert</h6>
									<Alert
										color="dark"
										class="alert-outline border-2 bg-body-secondary mb-0"
										dismissible
									>
										<strong>Did you know?</strong> - Outline
										<b>dark alert</b> example
									</Alert>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={outlineAlertsCode}
								id="outlineAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Left Border Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>alert-border-left </code> class to set
							an alert with the left border.
						</p>

						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>
									<Alert
										color="primary"
										class="alert-border-left"
										dismissible
									>
										<i
											class="ri-user-smile-line me-3 align-middle fs-16"
										/><strong>Primary</strong>
										- Left border alert
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert
										color="secondary"
										class="alert-border-left"
										dismissible
									>
										<i
											class="ri-check-double-line me-3 align-middle fs-16"
										/><strong>Secondary</strong>
										- Left border alert
									</Alert>

									<h6>Success Alert</h6>
									<Alert
										color="success"
										class="alert-border-left"
										dismissible
									>
										<i
											class="ri-notification-off-line me-3 align-middle fs-16"
										/><strong>Success</strong>
										- Left border alert
									</Alert>

									<h6>Danger Alert</h6>
									<Alert
										color="danger"
										class="alert-border-left mb-xl-0"
										dismissible
									>
										<i
											class="ri-error-warning-line me-3 align-middle fs-16"
										/><strong>Danger</strong>
										- Left border alert
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert
										color="warning"
										class="alert-border-left"
										dismissible
									>
										<i
											class="ri-alert-line me-3 align-middle fs-16"
										/><strong>Warning</strong>
										- Left border alert
									</Alert>

									<h6>Info Alert</h6>
									<Alert
										color="info"
										class="alert-border-left"
										dismissible
									>
										<i
											class="ri-airplay-line me-3 align-middle fs-16"
										/><strong>Info</strong>
										- Left border alert
									</Alert>

									<h6>Light Alert</h6>
									<Alert
										color="light"
										class="alert-border-left"
										dismissible
									>
										<i
											class="ri-mail-line me-3 align-middle fs-16"
										/><strong>Light</strong>
										- Left border alert
									</Alert>

									<h6>Dark Alert</h6>
									<Alert
										color="dark"
										class="alert-border-left mb-0"
										dismissible
									>
										<i
											class="ri-refresh-line me-3  align-middle fs-16"
										/><strong>Dark</strong>
										- Left border alert
									</Alert>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={leftBorderAlertsCode}
								id="leftBorderAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Label Icon Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>alert-label-icon</code> class to set an
							alert with a label icon.
						</p>
						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>
									<Alert
										color="primary"
										class=" alert-label-icon fade show bg-primary text-white"
										 dismissible
									>
										<i
											class="ri-user-smile-line label-icon"
										/><strong>Primary</strong> -Label icon alert
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert
										color="secondary"
										class=" alert-label-icon fade show bg-secondary text-white"
										dismissible
									>
										<i
											class="ri-check-double-line label-icon"
										/><strong>Secondary</strong>
										- Label icon alert
									</Alert>

									<h6>Success Alert</h6>
									<Alert
										color="success"
										class="alert-label-icon fade show bg-success text-white"
										dismissible
									>
										<i
											class="ri-notification-off-line label-icon"
										/><strong>Success</strong>
										- Label icon alert
									</Alert>

									<h6>Danger Alert</h6>
									<Alert
										color="danger"
										class="alert-label-icon fade show bg-danger text-white mb-xl-0"
										dismissible
									>
										<i
											class="ri-error-warning-line label-icon"
										/><strong>Danger</strong>
										- Label icon alert
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert
										color="warning"
										class="alert-label-icon fade show bg-warning text-white"
										dismissible
									>
										<i
											class="ri-alert-line label-icon"
										/><strong>warning</strong> - Label icon alert
									</Alert>

									<h6>Info Alert</h6>
									<Alert
										color="info"
										class="alert-label-icon fade show bg-info text-white"
										dismissible
									>
										<i
											class="ri-airplay-line label-icon"
										/><strong>Info</strong> - Label icon alert
									</Alert>

									<h6>Light Alert</h6>
									<Alert
										color="light"
										class="alert-label-icon fade show bg-light text-body"
										dismissible
									>
										<i
											class="ri-mail-line label-icon"
										/><strong>Light</strong> - Label icon alert
									</Alert>

									<h6>Dark Alert</h6>
									<Alert
										color="dark"
										class="alert-label-icon fade show bg-dark text-white mb-0"
										dismissible
									>
										<i
											class="ri-refresh-line label-icon"
										/><strong>Dark</strong> - Label icon alert
									</Alert>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={labelIconAlertsCode}
								id="labelIconAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Additional Content Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>alert-additional</code> class and Use
							the <code>alert-</code> class to HTML elements like headings,
							paragraphs, dividers etc.
						</p>
						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>

									<Alert
										color="primary"
										class="alert-additional"
										dismissible
									>
										<div class="alert-body">
											<div class="d-flex">
												<div class="flex-shrink-0 me-3">
													<i
														class="ri-error-warning-line fs-16 align-middle"
													/>
												</div>
												<div class="flex-grow-1">
													<h5 class="alert-heading">
														Well done !
													</h5>
													<p class="mb-0">
														Aww yeah, you
														successfully read this
														important alert message.
													</p>
												</div>
											</div>
										</div>
										<div class="alert-content">
											<p class="mb-0">
												Whenever you need to, be sure to
												use margin utilities to keep
												things nice and tidy.
											</p>
										</div>
									</Alert>

									<h6>Danger Alert</h6>
									<Alert
										color="danger"
										class="alert-additional mb-xl-0"
										dismissible
									>
										<div class="alert-body">
											<div class="d-flex">
												<div class="flex-shrink-0 me-3">
													<i
														class="ri-alert-line fs-16 align-middle"
													/>
												</div>
												<div class="flex-grow-1">
													<h5 class="alert-heading">
														Something is very wrong!
													</h5>
													<p class="mb-0">
														Change a few things up
														and try submitting
														again.
													</p>
												</div>
											</div>
										</div>
										<div class="alert-content">
											<p class="mb-0">
												Whenever you need to, be sure to
												use margin utilities to keep
												things nice and tidy.
											</p>
										</div>
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Success Alert</h6>
									<Alert
										color="success"
										class="alert-additional"
										dismissible
									>
										<div class="alert-body">
											<div class="d-flex">
												<div class="flex-shrink-0 me-3">
													<i
														class="ri-notification-off-line fs-16 align-middle"
													/>
												</div>
												<div class="flex-grow-1">
													<h5 class="alert-heading">
														Yey! Everything worked!
													</h5>
													<p class="mb-0">
														This alert needs your
														attention, but it"s not
														super important.
													</p>
												</div>
											</div>
										</div>
										<div class="alert-content">
											<p class="mb-0">
												Whenever you need to, be sure to
												use margin utilities to keep
												things nice and tidy.
											</p>
										</div>
									</Alert>

									<h6>Warning Alert</h6>
									<Alert
										color="warning"
										class="alert-additional mb-0"
										dismissible
									>
										<div class="alert-body">
											<div class="d-flex">
												<div class="flex-shrink-0 me-3">
													<i
														class="ri-alert-line fs-16 align-middle"
													/>
												</div>
												<div class="flex-grow-1">
													<h5 class="alert-heading">
														Uh oh, something went
														wrong!
													</h5>
													<p class="mb-0">
														Better check yourself,
														you're not looking too
														good.
													</p>
												</div>
											</div>
										</div>
										<div class="alert-content">
											<p class="mb-0">
												Whenever you need to, be sure to
												use margin utilities to keep
												things nice and tidy.
											</p>
										</div>
									</Alert>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={additionalContentAlertsCode}
								id="additionalContentAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Top Border with Outline Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>alert-top-border</code> class to set an
							alert with the top border and outline.
						</p>
						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>
									<Alert
										color="primary"
										class="alert-top-border"
										dismissible
									>
										<i
											class="ri-user-smile-line me-3 align-middle fs-16 text-primary"
										/><strong>Primary</strong>
										- Top border alert
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert
										color="secondary"
										class="alert-top-border"
										dismissible
									>
										<i
											class="ri-check-double-line me-3 align-middle fs-16 text-secondary"
										/><strong>Secondary</strong>
										- Top border alert
									</Alert>

									<h6>Success Alert</h6>
									<Alert
										color="success"
										class="alert-top-border"
										dismissible
									>
										<i
											class="ri-notification-off-line me-3 align-middle fs-16 text-success"
										/><strong>Success</strong>
										- Top border alert
									</Alert>

									<h6>Danger Alert</h6>
									<Alert
										color="danger"
										class="alert-top-border mb-xl-0"
										dismissible
									>
										<i
											class="ri-error-warning-line me-3 align-middle fs-16 text-danger "
										/><strong>Danger</strong>
										- Top border alert
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert
										color="warning"
										class="alert-top-border"
										dismissible
									>
										<i
											class="ri-alert-line me-3 align-middle fs-16 text-warning"
										/><strong>Warning</strong>
										- Top border alert
									</Alert>

									<h6>Info Alert</h6>
									<Alert
										color="info"
										class="alert-top-border"
										dismissible
									>
										<i
											class="ri-airplay-line me-3 align-middle fs-16 text-info"
										/><strong>Info</strong>
										- Top border alert
									</Alert>

									<h6>Light Alert</h6>
									<Alert
										color="light"
										class="alert-top-border"
										dismissible
									>
										<i
											class="ri-mail-line me-3 align-middle fs-16 text-body"
										/><strong>Light</strong>
										- Top border alert
									</Alert>

									<h6>Dark Alert</h6>
									<Alert
										color="dark"
										class="alert-top-border mb-0"
										dismissible
									>
										<i
											class="ri-refresh-line me-3 align-middle fs-16 text-body"
										/><strong>Dark</strong>
										- Top border alert
									</Alert>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={topBarAlertsCode}
								id="topBarAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Label Icon Arrow Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>alert-label-icon label-arrow</code> class
							to show an alert with label icon and arrow.
						</p>
						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>
									<Alert
										color="primary"
										class="alert-label-icon label-arrow "
										dismissible
									>
										<i
											class="ri-user-smile-line label-icon"
										/><strong>Primary</strong> - Label icon arrow
										alert
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert
										color="secondary"
										class="alert-label-icon label-arrow "
										dismissible
									>
										<i
											class="ri-check-double-line label-icon"
										/><strong>Secondary</strong> - Label icon
										arrow alert
									</Alert>

									<h6>Success Alert</h6>
									<Alert
										color="success"
										class="alert-label-icon label-arrow "
										dismissible
									>
										<i
											class="ri-notification-off-line label-icon"
										/><strong>Success</strong>
										- Label icon arrow alert
									</Alert>

									<h6>Danger Alert</h6>
									<Alert
										color="danger"
										class="alert-label-icon label-arrow mb-xl-0"
										dismissible
									>
										<i
											class="ri-error-warning-line label-icon"
										/><strong>Danger</strong>
										- Label icon arrow alert
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert
										color="warning"
										class="alert-label-icon label-arrow "
										dismissible
									>
										<i
											class="ri-alert-line label-icon"
										/><strong>Warning</strong> - Label icon arrow
										alert
									</Alert>

									<h6>info Alert</h6>
									<Alert
										color="info"
										class="alert-label-icon label-arrow "
										dismissible
									>
										<i
											class="ri-airplay-line label-icon"
										/><strong>Info</strong> - Label icon arrow
										alert
									</Alert>

									<h6>Light Alert</h6>
									<Alert
										color="light"
										class="alert-label-icon label-arrow "
										dismissible
									>
										<i
											class="ri-mail-line label-icon"
										/><strong>Light</strong>
										- Label icon arrow alert
									</Alert>

									<h6>Dark Alert</h6>
									<Alert
										color="dark"
										class="alert-label-icon label-arrow mb-0"
										dismissible
									>
										<i class="ri-refresh-line label-icon"/><strong>Dark</strong>
										- Label icon arrow alert
									</Alert>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={labelIconArrowAlertsCode}
								id="labelIconArrowAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Rounded Label Icon Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>alert-label-icon rounded-label</code> class
							to set an alert with a rounded label icon.
						</p>
						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Alert</h6>
									<Alert
										color="primary"
										class="alert-label-icon rounded-label"
										dismissible
									>
										<i
											class="ri-user-smile-line label-icon"
										/><strong>Primary</strong> - Rounded label
										alert
									</Alert>

									<h6>Secondary Alert</h6>
									<Alert
										color="secondary"
										class="alert-label-icon rounded-label"
										dismissible
									>
										<i
											class="ri-check-double-line label-icon"
										/><strong>Secondary</strong>
										- Rounded label alert
									</Alert>

									<h6>Success Alert</h6>
									<Alert
										color="success"
										class="alert-label-icon rounded-label"
										dismissible
									>
										<i
											class="ri-notification-off-line label-icon"
										/><strong>Success</strong>
										- Rounded label alert
									</Alert>

									<h6>Danger Alert</h6>
									<Alert
										color="danger"
										class="alert-label-icon rounded-label"
										dismissible
									>
										<i
											class="ri-error-warning-line label-icon"
										/><strong>Danger</strong>
										- Rounded label alert
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Alert</h6>
									<Alert
										color="warning"
										class="alert-label-icon rounded-label"
										dismissible
									>
										<i
											class="ri-alert-line label-icon"
										/><strong>Warning</strong> - Rounded label
										alert
									</Alert>

									<h6>Info Alert</h6>
									<Alert
										color="info"
										class="alert-label-icon rounded-label"
										dismissible
									>
										<i
											class="ri-airplay-line label-icon"
										/><strong>Info</strong> - Rounded label alert
									</Alert>

									<h6>Light Alert</h6>
									<Alert
										color="light"
										class="alert-label-icon rounded-label"
										dismissible
									>
										<i
											class="ri-mail-line label-icon"
										/><strong>Light</strong> - Rounded label
										alert
									</Alert>

									<h6>Dark Alert</h6>
									<Alert
										color="dark"
										class="alert-label-icon rounded-label"
										dismissible
									>
										<i
											class="ri-refresh-line label-icon"
										/><strong>Dark</strong> - Rounded label alert
									</Alert>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={roundedLabelIconAlertsCode}
								id="roundedLabelIconAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Solid Alerts" />
					<CardBody>
						<p class="text-muted">
							Use the <code>bg-*, border-*</code> & <code>text-white</code> class to set an alert
							with solid style.
						</p>

						<div class="live-preview">
							<Row>
								<Col xl={6}>
									<h6>Primary Solid Alert</h6>
									<Alert color="primary" class="bg-primary border-primary text-white">
										  
										<strong>Hi!</strong> - Solid
										<b>primary alert</b> example
									</Alert>

									<h6>Secondary Solid Alert</h6>
									<Alert
										color="secondary"
										class="bg-secondary border-secondary text-white"
									>
										<strong>How are you!</strong> - Solid
										<b>secondary alert</b> example
									</Alert>

									<h6>Success Solid Alert</h6>
									<Alert color="success" class="bg-success border-success text-white">
										<strong
											>Yey! Everything worked!
										</strong>
										- Solid <b>success alert</b> example
									</Alert>

									<h6>Danger Solid Alert</h6>
									<Alert
										color="danger"
										class="bg-danger border-danger text-white mb-xl-0"
									>
										<strong>Something is very wrong!</strong
										>
										- Solid <b>danger alert</b> example
									</Alert>
								</Col>

								<Col xl={6}>
									<h6>Warning Solid Alert</h6>
									<Alert color="warning" class="bg-warning border-warning text-white">
										<strong
											>Uh oh, something went wrong!</strong
										>
										- Solid <b>warning alert</b> example
									</Alert>

									<h6>Info Solid Alert</h6>
									<Alert color="info" class="bg-info border-info text-white">
										<strong>Don't forget' it !</strong> -
										Solid <b>info alert</b> example
									</Alert>

									<h6>Light Solid Alert</h6>
									<Alert color="light" class="bg-light border-light text-body">
										<strong>Mind Your Step!</strong> - Solid
										<b>secondary alert</b> example
									</Alert>

									<h6>Dark Solid Alert</h6>
									<Alert
										color="dark"
										class="bg-dark border-primary text-white mb-0"
									>
										<strong>Did you know?</strong> - Solid
										<b>dark alert</b> example
									</Alert>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={solidAlertsCode}
								id="solidAlertsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
