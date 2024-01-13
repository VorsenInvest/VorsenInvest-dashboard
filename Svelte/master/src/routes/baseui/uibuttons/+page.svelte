<script>
	import {
		Button,
		Card,
		CardBody,
		Col,
		Container,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Row,
		Dropdown,
		ButtonGroup,
		ButtonToolbar,
		Spinner,
        Label,
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";

	const favouriteBtn = (ele) => {
		if (ele.closest("button").classList.contains("active")) {
			ele.closest("button").classList.remove("active");
		} else {
			ele.closest("button").classList.add("active");
		}
	};

	// Default Buttons

	const defaultButtonsCode = `
<!-- Base Buttons -->
<Button color="primary"> Primary </Button>

<Button color="secondary"> Secondary </Button>

<Button color="success"> Success </Button>

<Button color="info"> Info </Button>

<Button color="warning"> Warning </Button>

<Button color="danger"> Danger </Button>

<Button color="dark"> Dark </Button>

<Button color="link"> Link </Button>

<Button color="light"> Light </Button>
`;

	// Outline Buttons

	const outlineButtonsCode = `
<!-- Outline Buttons -->
<Button color="primary" outline class="material-shadow-none" > primary </Button>

<Button color="secondary" outline class="material-shadow-none" > Secondary </Button>

<Button color="success" outline class="material-shadow-none" > Success </Button>

<Button color="info" outline class="material-shadow-none" > Info </Button>

<Button color="warning" outline class="material-shadow-none" > Warning </Button>

<Button color="danger" outline class="material-shadow-none" > Danger </Button>

<Button color="dark" outline class="material-shadow-none" > Dark </Button>

<Button color="light" outline class="material-shadow-none" > Light </Button>
`;

	// Rounded Buttons

	const roundedButtonsCode = `
<!-- Rounded Buttons -->
<Button color="primary" class="rounded-pill"> Primary </Button>

<Button color="secondary" class="rounded-pill"> Secondary </Button>

<Button color="success" class="rounded-pill"> Success </Button>

<Button color="info" class="rounded-pill"> Info </Button>

<Button color="warning" class="rounded-pill"> Warning </Button>

<Button color="danger" class="rounded-pill"> Danger </Button>

<Button color="dark" class="rounded-pill"> Dark </Button>

<Button color="light" class="rounded-pill"> Light </Button>
`;

	// Soft Buttons

	const softButtonsCode = `
<!-- Soft Buttons -->
<Button color="soft-primary" class="waves-effect waves-light material-shadow-none">Primary</Button>

<Button color="soft-secondary" class="waves-effect waves-light material-shadow-none" >Secondary</Button>

<Button color="soft-success" class="waves-effect waves-light material-shadow-none" >Success</Button>

<Button color="soft-info" class="waves-effect waves-light material-shadow-none" >Info</Button>

<Button color="soft-warning" class="waves-effect waves-light material-shadow-none" >Warning</Button>

<Button color="soft-danger" class="waves-effect waves-light material-shadow-none" >Danger</Button>

<Button color="soft-dark" class="waves-effect waves-light material-shadow-none" >Dark</Button>
`;

	// Gradient Buttons

	const gradientButtonsCode = `
<!-- Gradient Buttons -->
<Button color="primary" class="bg-gradient"> Primary </Button>

<Button color="secondary" class="bg-gradient"> Secondary </Button>

<Button color="success" class="bg-gradient"> Success </Button>

<Button color="info" class="bg-gradient"> Info </Button>

<Button color="warning" class="bg-gradient"> Warning </Button>

<Button color="danger" class="bg-gradient"> Danger </Button>

<Button color="dark" class="bg-gradient"> Dark </Button>

<Button color="light" class="bg-gradient"> Light </Button>
`;

	// Animation Buttons

	const animationButtonsCode = `
<!-- Animation Buttons -->
<Button color="primary" class="btn-animation" data-text="Primary"> <span>Primary</span> </Button>

<Button color="secondary" class="btn-animation" data-text="Secondary"> <span>Secondary</span> </Button>

<Button color="success" class="btn-animation" data-text="Success"> <span>Success</span> </Button>

<Button color="info" class="btn-animation" data-text="Info"> <span>Info</span> </Button>

<Button color="warning" class="btn-animation" data-text="Warning"> <span>Warning</span> </Button>

<Button color="danger" class="btn-animation" data-text="Danger"> <span>Danger</span> </Button>

<Button color="dark" class="btn-animation" data-text="Dark"> <span>Dark</span> </Button>
`;

	// Buttons with Label

	const labelButtonsCode = `
<!-- Buttons with Label -->
<Button color="primary" class="btn-label"> <i class="ri-user-smile-line label-icon align-middle fs-16 me-2"></i> Primary </Button>

<Button color="success" class="btn-label"> <i class="ri-check-double-line label-icon align-middle fs-16 me-2"></i> Success </Button>

<Button color="warning" class="btn-label"> <i class="ri-error-warning-line label-icon align-middle fs-16 me-2"></i> Warning </Button>

<!-- Rounded with Label -->
<Button color="primary" class="btn-label rounded-pill"> <i class="ri-user-smile-line label-icon align-middle fs-16 me-2 rounded-pill"></i> Primary </Button>

<Button color="success" class="btn-label rounded-pill"> <i class="ri-check-double-line label-icon align-middle fs-16 me-2 rounded-pill"></i> Success </Button>

<Button color="warning" class="btn-label rounded-pill"> <i class="ri-error-warning-line label-icon align-middle fs-16 me-2 rounded-pill"></i> Warning </Button>

<!-- Buttons with Label Right -->
<Button color="primary" class="btn-label right"> <i class="ri-user-smile-line label-icon align-middle fs-16 ms-2"></i> Primary </Button>

<Button color="success" class="btn-label right rounded-pill"> <i class="ri-check-double-line label-icon align-middle rounded-pill fs-16 ms-2"></i> Success </Button>
`;

	// Buttons Sizes

	const sizeButtonsCode = `
<!-- Large Button -->
<Button size="lg" color="primary"> Large button </Button>

<Button size="lg" color="light"> Large button </Button>

<!-- Small Button -->
<Button size="sm" color="primary"> Small button </Button>

<Button size="sm" color="light"> Small button </Button>
`;

	// Border Buttons
	const borderButtonsCode = `<!-- Border Buttons -->

<div class="hstack flex-wrap gap-2 mb-3 mb-lg-0">
    <Button color="primary" class="btn-border">Primary</Button>
    <Button color="secondary" class="btn-border">Secondary</Button>
    <Button color="success" class="btn-border">Success</Button>
    <Button color="warning" class="btn-border">Warning</Button>
    <Button color="danger" class="btn-border">Danger</Button>
</div>

<div class="hstack flex-wrap gap-2 mb-3 mb-lg-0">
    <Button color="primary" outline class="btn-border">Primary</Button>
    <Button color="secondary" outline class="btn-border">Secondary</Button>
    <Button color="success" outline class="btn-border">Success</Button>
    <Button class="btn-soft-warning btn-border">Warning</Button>
    <Button class="btn-soft-danger btn-border">Danger</Button>
    <Button class="btn-soft-dark btn-border">Dark</Button>
</div>
`;

	// Custom Toggle Buttons
	const customToggleButtonsCode = `<!-- Custom Toggle Buttons -->

<div class="d-flex flex-wrap align-items-center gap-2">
    <Button color='primary' class="custom-toggle active" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on"><i class="ri-alarm-line align-bottom"></i> Active</span>
        <span class="icon-off">Unactive</span>
    </Button>
    <Button color='secondary' class="custom-toggle active" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on"><i class="ri-user-add-line align-bottom me-1"></i> Connect</span>
        <span class="icon-off"><i class="ri-check-fill align-bottom me-1"></i> Unconnect</span>
    </Button>
    <Button color='success' class="custom-toggle" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on"><i class="ri-thumb-up-line align-bottom me-1"></i> Yes</span>
        <span class="icon-off"><i class="ri-thumb-down-line align-bottom me-1"></i> No</span>
    </Button>
    <Button color='warning' class="custom-toggle active" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on"><i class="ri-add-line align-bottom me-1"></i> Follow</span>
        <span class="icon-off"><i class="ri-user-unfollow-line align-bottom me-1"></i> Unfollow</span>
    </Button>
    <Button color='danger' class="custom-toggle" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on">On</span>
        <span class="icon-off">Off</span>
    </Button>
    <Button color='dark' class="custom-toggle" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on"><i class="ri-bookmark-line align-bottom me-1"></i> Bookmark</span>
        <span class="icon-off"><i class="ri-bookmark-3-fill align-bottom me-1"></i> Unbookmark</span>
    </Button>
</div>

<div class="d-flex flex-wrap align-items-center gap-2">
    <Button color="primary" outline class="custom-toggle" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on">Active</span>
        <span class="icon-off">Unactive</span>
    </Button>
    <Button color="secondary" outline class="custom-toggle" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on"><i class="ri-add-line align-bottom me-1"></i> Follow</span>
        <span class="icon-off"><i class="ri-user-unfollow-line align-bottom me-1"></i> Unfollow</span>
    </Button>
    <Button color="success" outline class="custom-toggle active" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on">On</span>
        <span class="icon-off">Off</span>
    </Button>
    <Button color="warning" outline class="btn-soft-danger custom-toggle" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on">Follow</span>
        <span class="icon-off">Unfollow</span>
    </Button>
    <Button color="danger" outline class="custom-toggle" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on">On</span>
        <span class="icon-off">Off</span>
    </Button>
    <Button class="btn-dark custom-toggle active" onClick={(e) => favouriteBtn(e.target)}>
        <span class="icon-on"><i class="ri-bookmark-line align-bottom"></i></span>
        <span class="icon-off"><i class="ri-bookmark-3-fill align-bottom"></i></span>
    </Button>
</div>
`;

	// Buttons Width

	const widthButtonsCode = `
<!-- Width Button -->
<Button color="primary" class="w-xs"> Xs </Button>

<Button color="danger" class="w-sm"> Small </Button>

<Button color="warning" class="w-md"> Medium </Button>

<Button color="success" class="w-lg"> Large </Button>
`;

	// Buttons Tag

	const tagButtonsCode = `
<!-- Tag Button -->
<Link href={null} class="btn btn-primary"> Link </Link>

<Button color="success" type="submit"> Button </Button>

<Button color="info" type="button"> Input </Button>

<Button color="danger" type="submit"> Submit </Button>

<Button color="warning" type="reset"> Reset </Button>
`;

	// Buttons Grid

	const gridButtonsCode = `
<!-- Buttons Grid -->
<div class="d-grid gap-2">
    <Button color="primary"> Button </Button>
    <Button color="primary"> Button </Button>
</div>
`;

	// Buttons Checkbox & Radio

	const checkButtonsCode = `
	<ButtonGroup>
		<input type="checkbox" class="btn-check" id="btncheck1" checked/>
		<Label class="btn btn-primary material-shadow-none mb-0" for="btncheck1">Checkbox 1</Label>

		<input type="checkbox" class="btn-check" id="btncheck2"/>
		<Label class="btn btn-primary material-shadow-none mb-0" for="btncheck2">Checkbox 2</Label>

		<input type="checkbox" class="btn-check" id="btncheck3"/>
		<Label class="btn btn-primary material-shadow-none mb-0" for="btncheck3">Checkbox 3</Label>

	</ButtonGroup>

	<ButtonGroup>
		<input type="radio" class="btn-check" name="btnradio" id="btnradio1" checked />
		<Label class="btn btn-outline-secondary material-shadow-none mb-0" for="btnradio1">Radio 1</Label>

		<input type="radio" class="btn-check" name="btnradio" id="btnradio2" />
		<Label class="btn btn-outline-secondary material-shadow-none mb-0" for="btnradio2">Radio 2</Label>

		<input type="radio" class="btn-check" name="btnradio" id="btnradio3" />
		<Label class="btn btn-outline-secondary material-shadow-none mb-0" for="btnradio3">Radio 3</Label>

	</ButtonGroup>
`;

	// Buttons Group

	const groupButtonsCode = `
<!-- Buttons Group -->
<ButtonGroup>
    <Button color="primary" class="material-shadow-none"> Left </Button>
    <Button color="primary" class="material-shadow-none"> Middle </Button>
    <Button color="primary" class="material-shadow-none"> Right </Button>
</ButtonGroup>

<!-- Radio Buttons -->
<ButtonGroup class="mt-4 mt-sm-0">
    <Button color="light" class="btn-icon material-shadow-none"> <i class="ri-align-right" /> </Button>
    <Button color="light" class="btn-icon material-shadow-none"> <i class="ri-align-center" /> </Button>
    <Button color="light" class="btn-icon material-shadow-none"> <i class="ri-align-left" /> </Button>
</ButtonGroup>
`;

	// Buttons Icon

	const iconButtonsCode = `
<!-- Buttons Group -->
<Button color="primary" class="btn-icon"> <i class="ri-map-pin-line" /> </Button>
<Button color="danger" class="btn-icon"> <i class="ri-delete-bin-5-line" /> </Button>
<Button color="success" class="btn-icon"> <i class="ri-check-double-line" /> </Button>
<Button color="light" class="btn-icon"> <i class="ri-brush-2-fill" /> </Button>

<Button color="primary" class="btn-icon material-shadow-none waves-effect waves-light" outline> <i class="ri-24-hours-fill" /> </Button>
<Button color="danger" class="btn-icon material-shadow-none waves-effect waves-light" outline> <i class="ri-customer-service-2-line" /> </Button>
<Button color="success" class="btn-icon material-shadow-none waves-effect waves-light" outline> <i class="ri-mail-send-line" /> </Button>
<Button color="warning" class="btn-icon material-shadow-none waves-effect waves-light" outline> <i class="ri-menu-2-line" /> </Button>
`;

	// Buttons Toolbar

	const toolbarButtonsCode = `
<!-- Buttons Toolbar -->
<ButtonToolbar class="material-shadow">
	<ButtonGroup class="me-2">
		<Button color="light" class="material-shadow-none">1</Button>
		<Button color="light" class="material-shadow-none">2</Button>
		<Button color="light" class="material-shadow-none">3</Button>
		<Button color="light" class="material-shadow-none">4</Button>
	</ButtonGroup>
	<ButtonGroup class="me-2 material-shadow">
		<Button color="light" class="material-shadow-none">5</Button>
		<Button color="light" class="material-shadow-none">6</Button>
		<Button color="light" class="material-shadow-none">7</Button>
	</ButtonGroup>
	<ButtonGroup  class="material-shadow">
		<Button color="light" class="material-shadow-none">8</Button>
	</ButtonGroup>
</ButtonToolbar>
`;

	// Group Buttons Sizing

	const groupSizingButtonsCode = `
<!-- Group Buttons Sizing -->
<ButtonGroup size="lg" class="material-shadow">
	<Button color="primary" class="material-shadow-none">Left</Button>
	<Button color="primary" class="material-shadow-none">Middle</Button>
	<Button color="primary" class="material-shadow-none">Right</Button>
</ButtonGroup>
<ButtonGroup class="mt-2 material-shadow">
	<Button color="light" class="material-shadow-none">Left</Button>
	<Button color="light" class="material-shadow-none">Middle</Button>
	<Button color="light" class="material-shadow-none">Right</Button>
</ButtonGroup>
<ButtonGroup size="sm" class="mt-2 material-shadow">
	<Button color="secondary" class="material-shadow-none">Left</Button>
	<Button color="secondary" class="material-shadow-none">Middle</Button>
	<Button color="secondary" class="material-shadow-none">Right</Button>
</ButtonGroup>
`;

	const verticalButtonsCode = `<Row>
<div class="col-auto">
    <ButtonGroup>
        <Button color="primary">1</Button>
        <Button color="primary">2</Button>
        <Dropdown id="btnGroupDrop1">
            <DropdownToggle color="primary" caret>
                Dropdown
            </DropdownToggle>
            <DropdownMenu>
                <DropdownItem> Dropdown link </DropdownItem>
                <DropdownItem> Dropdown link </DropdownItem>
            </DropdownMenu>
        </Dropdown>
    </ButtonGroup>
</div>
<div class="col-auto">
    <ButtonGroup vertical>
        <Button color="light">Button</Button>

        <Dropdown id="btnGroupVerticalDrop1">
            <DropdownToggle color="light" caret>
                Dropdown
            </DropdownToggle>
            <DropdownMenu>
                <DropdownItem> Dropdown link </DropdownItem>
                <DropdownItem> Dropdown link </DropdownItem>
            </DropdownMenu>
        </Dropdown>

        <Button color="light">Button</Button>
        <Button color="light">Button</Button>
    </ButtonGroup>
</div>
<div class="col-auto">
    <ButtonGroup vertical class="material-shadow">
		<input type="radio" class="btn-check" name="vbtn" id="vbtn-radio1" checked />
		<Label class="btn btn-outline-secondary material-shadow-none" for="vbtn-radio1">Radio 1</Label>
		
		<input type="radio" class="btn-check" name="vbtn" id="vbtn-radio2" /> 
		<Label class="btn btn-outline-secondary material-shadow-none" for="vbtn-radio2">Radio 2</Label>

		<input type="radio" class="btn-check" name="vbtn" id="vbtn-radio3" /> 
		<Label class="btn btn-outline-secondary material-shadow-none" for="vbtn-radio3">Radio 3</Label>
	</ButtonGroup>
</div>
</Row>
`;

	// Ghost Buttons
	const ghostButtonsCode = `
<!-- Ghost Buttons -->

<Button color="ghost-primary" class="waves-effect waves-light material-shadow-none">Primary</Button>

<Button color="ghost-secondary" class="waves-effect waves-light material-shadow-none">Secondary</Button>

<Button color="ghost-success" class="waves-effect waves-light material-shadow-none">Success</Button>

<Button color="ghost-info" class="waves-effect waves-light material-shadow-none">Info</Button>

<Button color="ghost-warning" class="waves-effect waves-light material-shadow-none">Warning</Button>

<Button color="ghost-danger" class="waves-effect waves-light material-shadow-none">Danger</Button>

<Button color="ghost-dark" class="waves-effect waves-light material-shadow-none">Dark</Button>
`;

	// Ghost Buttons
	const loadingbuttonsCode = `
<!-- Load More Buttons -->

<div class="hstack flex-wrap gap-2 mb-3 mb-lg-0">
    <Button color="primary" class="btn-load" outline>
        <span class="d-flex align-items-center">
            <Spinner size="sm" class="flex-shrink-0"> Loading... </Spinner>
            <span class="flex-grow-1 ms-2">
                Loading...
            </span>
        </span>
    </Button>
    <Button color="success" class="btn-load">
        <span class="d-flex align-items-center">
            <Spinner size="sm" class="flex-shrink-0"> Loading... </Spinner>
            <span class="flex-grow-1 ms-2">
                Loading...
            </span>
        </span>
    </Button>
    <Button color="secondary" class="btn-load" outline>
        <span class="d-flex align-items-center">
            <Spinner size="sm" type="grow" class="flex-shrink-0"> Loading... </Spinner>
            <span class="flex-grow-1 ms-2">
                Loading...
            </span>
        </span>
    </Button>
    <Button color="danger" class="btn-load">
        <span class="d-flex align-items-center">
            <Spinner size="sm" type="grow" class="flex-shrink-0"> Loading... </Spinner>
            <span class="flex-grow-1 ms-2">
                Loading...
            </span>
        </span>
    </Button>
</div>

<div class="d-flex flex-wrap gap-2 mb-3 mb-lg-0">
    <Button color="primary" class="btn-load" outline>
        <span class="d-flex align-items-center">
            <span class="flex-grow-1 me-2">
                Loading...
            </span>
            <Spinner size="sm" class="flex-shrink-0" role="status"> Loading... </Spinner>
        </span>
    </Button>
    <Button color="success" class="btn-load">
        <span class="d-flex align-items-center">
            <span class="flex-grow-1 me-2">
                Loading...
            </span>
            <Spinner size="sm" class="flex-shrink-0" role="status"> Loading... </Spinner>
        </span>
    </Button>
    <Button color="warning" class="btn-load" outline>
        <span class="d-flex align-items-center">
            <span class="flex-grow-1 me-2">
                Loading...
            </span>
            <Spinner size="sm" type="grow" class="flex-shrink-0" role="status"> Loading... </Spinner>
        </span>
    </Button>
    <Button color="info" class="btn-load">
        <span class="d-flex align-items-center">
            <span class="flex-grow-1 me-2">
                Loading...
            </span>
            <Spinner size="sm" type="grow" class="flex-shrink-0" role="status"> Loading... </Spinner>
        </span>
    </Button>
</div>
`;
</script>

<svelte:head>
	<title>Buttons | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Buttons" pageTitle="Base UI" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Default Buttons" />

					<CardBody>
						<p class="text-muted">
							Use the <code>Button</code> tag to show the default button
							style.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button color="primary">Primary</Button>
								<Button color="secondary">Secondary</Button>
								<Button color="success">Success</Button>
								<Button color="info">Info</Button>
								<Button color="warning">Warning</Button>
								<Button color="danger">Danger</Button>
								<Button color="dark">Dark</Button>
								<Button color="link">Link</Button>
								<Button color="light">Light</Button>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={defaultButtonsCode}
								id="defaultButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Outline Buttons" />
					<CardBody>
						<p class="text-muted">
							Use <code>outline</code> atrribute with the below-mentioned
							variation to create a button with the outline.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button color="primary" outline class="material-shadow-none">Primary</Button>
								<Button color="secondary" outline class="material-shadow-none"
									>Secondary</Button
								>
								<Button color="success" outline class="material-shadow-none">Success</Button>
								<Button color="info" outline class="material-shadow-none">Info</Button>
								<Button color="warning" outline class="material-shadow-none">Warning</Button>
								<Button color="danger" outline class="material-shadow-none">Danger</Button>
								<Button color="dark" outline class="material-shadow-none">Dark</Button>
								<Button color="light" outline class="material-shadow-none">Light</Button>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={outlineButtonsCode}
								id="outlineButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Rounded Buttons" />
					<CardBody>
						<p class="text-muted">
							Use the <code>rounded-pill </code>class to make a
							rounded button.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button color="primary" class="rounded-pill"
									>Primary</Button
								>
								<Button color="secondary" class="rounded-pill"
									>Secondary</Button
								>
								<Button color="success" class="rounded-pill"
									>Success</Button
								>
								<Button color="info" class="rounded-pill"
									>Info</Button
								>
								<Button color="warning" class="rounded-pill"
									>Warning</Button
								>
								<Button color="danger" class="rounded-pill"
									>Danger</Button
								>
								<Button color="dark" class="rounded-pill"
									>Dark</Button
								>
								<Button color="light" class="rounded-pill"
									>Light</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={roundedButtonsCode}
								id={roundedButtonsCode}
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Soft Buttons" />
					<CardBody>
						<p class="text-muted">
							Use <code>btn-soft-</code> class with the below-mentioned
							variation to create a button with the soft background.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button
									color="soft-primary"
									class="waves-effect waves-light material-shadow-none"
									>Primary</Button
								>
								<Button
								color="soft-secondary"
									class="waves-effect waves-light material-shadow-none"
									>Secondary</Button
								>
								<Button color="soft-success"
									class="waves-effect waves-light material-shadow-none"
									>Success</Button
								>
								<Button color="soft-info"
									class="waves-effect waves-light material-shadow-none"
									>Info</Button
								>
								<Button color="soft-warning"
									class="waves-effect waves-light material-shadow-none"
									>Warning</Button
								>
								<Button color="soft-danger"
									class="waves-effect waves-light material-shadow-none"
									>Danger</Button
								>
								<Button color="soft-dark"
									class="waves-effect waves-light material-shadow-none"
									>Dark</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={softButtonsCode}
								id="softButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Ghost Buttons" />
					<CardBody>
						<p class="text-muted">
							Use <code>btn-ghost-</code> class with the below-mentioned
							variation to create a button with the transparent background.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button
									color="ghost-primary"
									class="waves-effect waves-light material-shadow-none"
									>Primary</Button
								>
								<Button
									color="ghost-secondary"
									class="waves-effect waves-light material-shadow-none"
									>Secondary</Button
								>
								<Button
									color="ghost-success"
									class="waves-effect waves-light material-shadow-none"
									>Success</Button
								>
								<Button
									color="ghost-info"
									class="waves-effect waves-light material-shadow-none">Info</Button
								>
								<Button
									color="ghost-warning"
									class="waves-effect waves-light material-shadow-none"
									>Warning</Button
								>
								<Button
									color="ghost-danger"
									class="waves-effect waves-light material-shadow-none">Danger</Button
								>
								<Button
									color="ghost-dark"
									class="waves-effect waves-light material-shadow-none">Dark</Button
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={ghostButtonsCode}
								id="ghostButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Gradient Buttons" />

					<CardBody>
						<p class="text-muted">
							Use <code>bg-gradient </code>class to create a
							gradient button.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button color="primary" class="bg-gradient"
									>Primary</Button
								>
								<Button color="secondary" class="bg-gradient"
									>Secondary</Button
								>
								<Button color="success" class="bg-gradient"
									>Success</Button
								>
								<Button color="info" class="bg-gradient"
									>Info</Button
								>
								<Button color="warning" class="bg-gradient"
									>Warning</Button
								>
								<Button color="danger" class="bg-gradient"
									>Danger</Button
								>
								<Button color="dark" class="bg-gradient"
									>Dark</Button
								>
								<Button color="light" class="bg-gradient"
									>Light</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={gradientButtonsCode}
								id="gradientButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Animation Buttons" />
					<CardBody>
						<p class="text-muted">
							Use <code>bg-animation </code>class to create an
							animated button.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button
									color="primary"
									class="btn-animation"
									data-text="Primary"
								>
									<span>Primary</span>
								</Button>
								<Button
									color="secondary"
									class="btn-animation"
									data-text="Secondary"
								>
									<span>Secondary</span>
								</Button>
								<Button
									color="success"
									class="btn-animation"
									data-text="Success"
								>
									<span>Success</span>
								</Button>
								<Button
									color="info"
									class="btn-animation"
									data-text="Info"
								>
									<span>Info</span>
								</Button>
								<Button
									color="warning"
									class="btn-animation"
									data-text="Warning"
								>
									<span>Warning</span>
								</Button>
								<Button
									color="danger"
									class="btn-animation"
									data-text="Danger"
								>
									<span>Danger</span>
								</Button>
								<Button
									color="dark"
									class="btn-animation"
									data-text="Dark"
								>
									<span>Dark</span>
								</Button>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={animationButtonsCode}
								id="animationButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Buttons with Label" />

					<CardBody>
						<p class="text-muted">
							Use <code>btn-label </code>class to create a button
							with the label.
						</p>
						<div class="live-preview">
							<Row>
								<Col lg={4}>
									<div
										class="d-flex flex-wrap gap-2 mb-3 mb-lg-0"
									>
										<Button
											color="primary"
											class="btn-label"
										>
											<i
												class="ri-user-smile-line label-icon align-middle fs-16 me-2 "
											/> Primary
										</Button>
										<Button
											color="success"
											class="btn-label"
										>
											<i
												class="ri-check-double-line label-icon align-middle fs-16 me-2"
											/> Success
										</Button>
										<Button
											color="warning"
											class="btn-label"
										>
											<i
												class="ri-error-warning-line label-icon align-middle fs-16 me-2"
											/> Warning
										</Button>
									</div>
								</Col>
								<Col lg={4}>
									<div
										class="d-flex flex-wrap gap-2 mb-3 mb-lg-0"
									>
										<Button
											color="primary"
											class="btn-label rounded-pill"
										>
											<i
												class="ri-user-smile-line label-icon align-middle fs-16 me-2 rounded-pill"
											/> Primary
										</Button>
										<Button
											color="success"
											class="btn-label rounded-pill"
										>
											<i
												class="ri-check-double-line label-icon align-middle fs-16 me-2 rounded-pill"
											/> Success
										</Button>
										<Button
											color="warning"
											class="btn-label rounded-pill"
										>
											<i
												class="ri-error-warning-line label-icon align-middle fs-16 me-2 rounded-pill"
											/> Warning
										</Button>
									</div>
								</Col>
								<Col lg={4}>
									<div class="d-flex flex-wrap gap-2">
										<Button
											color="primary"
											class="btn-label right"
										>
											<i
												class="ri-user-smile-line label-icon align-middle fs-16 ms-2"
											/> Primary
										</Button>
										<Button
											color="success"
											class="btn-label right rounded-pill"
										>
											<i
												class="ri-check-double-line label-icon align-middle rounded-pill fs-16 ms-2"
											/> Success
										</Button>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={labelButtonsCode}
								id="labelButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Load More Buttons" />
					<CardBody>
						<p class="text-muted">Example of loading buttons.</p>
						<div class="live-preview">
							<Row>
								<Col lg={6}>
									<div
										class="hstack flex-wrap gap-2 mb-3 mb-lg-0"
									>
										<Button
											color="primary"
											class="btn-load"
											outline
										>
											<span
												class="d-flex align-items-center"
											>
												<Spinner
													size="sm"
													class="flex-shrink-0"
													>Loading...</Spinner
												>
												<span class="flex-grow-1 ms-2">
													Loading...
												</span>
											</span>
										</Button>
										<Button
											color="success"
											class="btn-load"
										>
											<span
												class="d-flex align-items-center"
											>
												<Spinner
													size="sm"
													class="flex-shrink-0"
													>Loading...</Spinner
												>
												<span class="flex-grow-1 ms-2">
													Loading...
												</span>
											</span>
										</Button>
										<Button
											color="secondary"
											class="btn-load"
											outline
										>
											<span
												class="d-flex align-items-center"
											>
												<Spinner
													size="sm"
													type="grow"
													class="flex-shrink-0"
													>Loading...</Spinner
												>
												<span class="flex-grow-1 ms-2">
													Loading...
												</span>
											</span>
										</Button>
										<Button color="danger" class="btn-load">
											<span
												class="d-flex align-items-center"
											>
												<Spinner
													size="sm"
													type="grow"
													class="flex-shrink-0"
													>Loading...</Spinner
												>
												<span class="flex-grow-1 ms-2">
													Loading...
												</span>
											</span>
										</Button>
									</div>
								</Col>

								<Col lg={6}>
									<div
										class="d-flex flex-wrap gap-2 mb-3 mb-lg-0"
									>
										<Button
											color="primary"
											class="btn-load"
											outline
										>
											<span
												class="d-flex align-items-center"
											>
												<span class="flex-grow-1 me-2">
													Loading...
												</span>
												<Spinner
													size="sm"
													class="flex-shrink-0"
													role="status"
													>Loading...</Spinner
												>
											</span>
										</Button>
										<Button
											color="success"
											class="btn-load"
										>
											<span
												class="d-flex align-items-center"
											>
												<span class="flex-grow-1 me-2">
													Loading...
												</span>
												<Spinner
													size="sm"
													class="flex-shrink-0"
													role="status"
													>Loading...</Spinner
												>
											</span>
										</Button>
										<Button
											color="warning"
											class="btn-load"
											outline
										>
											<span
												class="d-flex align-items-center"
											>
												<span class="flex-grow-1 me-2">
													Loading...
												</span>
												<Spinner
													size="sm"
													type="grow"
													class="flex-shrink-0"
													role="status"
												>
													Loading...
												</Spinner>
											</span>
										</Button>
										<Button color="info" class="btn-load">
											<span
												class="d-flex align-items-center"
											>
												<span class="flex-grow-1 me-2">
													Loading...
												</span>
												<Spinner
													size="sm"
													type="grow"
													class="flex-shrink-0"
													role="status"
												>
													Loading...
												</Spinner>
											</span>
										</Button>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={loadingbuttonsCode}
								id="loadingbuttonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Border Buttons" />
					<CardBody>
						<p class="text-muted">
							Example of simple bottom borderd buttons.
						</p>
						<div class="live-preview">
							<Row>
								<Col lg={6}>
									<div
										class="hstack flex-wrap gap-2 mb-3 mb-lg-0"
									>
										<Button
											color="primary"
											class="btn-border">Primary</Button
										>
										<Button
											color="secondary"
											class="btn-border">Secondary</Button
										>
										<Button
											color="success"
											class="btn-border">Success</Button
										>
										<Button
											color="warning"
											class="btn-border">Warning</Button
										>
										<Button
											color="danger"
											class="btn-border">Danger</Button
										>
									</div>
								</Col>
								<Col lg={6}>
									<div
										class="hstack flex-wrap gap-2 mb-3 mb-lg-0"
									>
										<Button
											color="primary"
											outline
											class="btn-border">Primary</Button
										>
										<Button
											color="secondary"
											outline
											class="btn-border">Secondary</Button
										>
										<Button
											color="success"
											outline
											class="btn-border">Success</Button
										>
										<Button
											class="btn-soft-warning btn-border"
											>Warning</Button
										>
										<Button
											class="btn-soft-danger btn-border"
											>Danger</Button
										>
										<Button class="btn-soft-dark btn-border"
											>Dark</Button
										>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={borderButtonsCode}
								id="borderButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Custom Toggle Buttons" />
					<CardBody>
						<p class="text-muted">Example of toggle buttons.</p>
						<div class="live-preview">
							<Row>
								<Col lg={6}>
									<div
										class="d-flex flex-wrap align-items-center gap-2"
									>
										<Button
											color="primary"
											class="custom-toggle active"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on"
												><i
													class="ri-alarm-line align-bottom"
												/> Active</span
											>
											<span class="icon-off"
												>Unactive</span
											>
										</Button>
										<Button
											color="secondary"
											class="custom-toggle active"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on"
												><i
													class="ri-user-add-line align-bottom me-1"
												/> Connect</span
											>
											<span class="icon-off"
												><i
													class="ri-check-fill align-bottom me-1"
												/> Unconnect</span
											>
										</Button>
										<Button
											color="success"
											class="custom-toggle"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on"
												><i
													class="ri-thumb-up-line align-bottom me-1"
												/> Yes</span
											>
											<span class="icon-off"
												><i
													class="ri-thumb-down-line align-bottom me-1"
												/> No</span
											>
										</Button>
										<Button
											color="warning"
											class="custom-toggle active"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on"
												><i
													class="ri-add-line align-bottom me-1"
												/> Follow</span
											>
											<span class="icon-off"
												><i
													class="ri-user-unfollow-line align-bottom me-1"
												/> Unfollow</span
											>
										</Button>
										<Button
											color="danger"
											class="custom-toggle"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on">On</span>
											<span class="icon-off">Off</span>
										</Button>
										<Button
											color="dark"
											class="custom-toggle"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on"
												><i
													class="ri-bookmark-line align-bottom me-1"
												/> Bookmark</span
											>
											<span class="icon-off"
												><i
													class="ri-bookmark-3-fill align-bottom me-1"
												/> Unbookmark</span
											>
										</Button>
									</div>
								</Col>
								<Col lg={6}>
									<div
										class="d-flex flex-wrap align-items-center gap-2"
									>
										<Button
											color="primary"
											outline
											class="custom-toggle"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on">Active</span>
											<span class="icon-off"
												>Unactive</span
											>
										</Button>
										<Button
											color="secondary"
											outline
											class="custom-toggle"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on"
												><i
													class="ri-add-line align-bottom me-1"
												/> Follow</span
											>
											<span class="icon-off"
												><i
													class="ri-user-unfollow-line align-bottom me-1"
												/> Unfollow</span
											>
										</Button>
										<Button
											color="success"
											outline
											class="custom-toggle active"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on">On</span>
											<span class="icon-off">Off</span>
										</Button>
										<Button
											color="warning"
											outline
											class="custom-toggle active"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on">Follow</span>
											<span class="icon-off"
												>Unfollow</span
											>
										</Button>
										<Button
											color="danger"
											outline
											class="btn-soft-danger custom-toggle"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on">On</span>
											<span class="icon-off">Off</span>
										</Button>
										<Button
											class="btn-dark custom-toggle active"
											on:click={(e) =>
												favouriteBtn(e.target)}
										>
											<span class="icon-on"
												><i
													class="ri-bookmark-line align-bottom"
												/></span
											>
											<span class="icon-off"
												><i
													class="ri-bookmark-3-fill align-bottom"
												/></span
											>
										</Button>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={customToggleButtonsCode}
								id="customToggleButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Buttons Sizes" />

					<CardBody>
						<p class="text-muted">
							Use <code>btn-lg</code> class to create a large size
							button and <code>btn-sm</code> class to create a small
							size button.
						</p>
						<div class="live-preview">
							<div
								class="d-flex flex-wrap align-items-center gap-2"
							>
								<Button size="lg" color="primary"
									>Large button</Button
								>
								<Button size="lg" color="light"
									>Large button</Button
								>

								<Button size="sm" color="primary"
									>Small button</Button
								>
								<Button size="sm" color="light"
									>Small button</Button
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={sizeButtonsCode}
								id="sizeButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Buttons Width" />

					<CardBody>
						<p class="text-muted">
							Use <code>w-xs,w-sm,w-md,w-lg</code> class to make different
							sized buttons respectively.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button color="primary" class="w-xs">Xs</Button>
								<Button color="danger" class="w-sm"
									>Small</Button
								>
								<Button color="warning" class="w-md"
									>Medium</Button
								>
								<Button color="success" class="w-lg"
									>Large</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={widthButtonsCode}
								id="widthButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Buttons Tag" />

					<CardBody>
						<p class="text-muted">
							Use <code>btn</code> class with different HTML elements.
							(though some browsers may apply a slightly different
							rendering)
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Link href={null} class="btn btn-primary"
									>Link</Link
								>
								<Button color="success" type="submit"
									>Button</Button
								>
								<Button color="info" type="button">Input</Button
								>
								<Button color="danger" type="submit"
									>Submit</Button
								>
								<Button color="warning" type="reset"
									>Reset</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={tagButtonsCode}
								id="tagButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<PreviewCardHeader title="Base class" />

					<CardBody>
						<p class="text-muted">
							Bootstrap has a base <code> .btn </code> class that sets up basic styles such as padding and content alignment. 
							By default, <code> .btn </code> controls have a transparent border and background color, and lack any explicit focus and hover styles.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button class="" color="">Base Class</Button>
							</div>
						</div>
						<div class="d-none code-view">
							<pre class="language-markup">
                                <code
									>&lt;Button class="" color=""&gt;Base Class&lt;/Button&gt;</code
								></pre>
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col lg={6}>
				<Card>
					<PreviewCardHeader title="Custom sizing with CSS variables" />

					<CardBody>
						<p class="text-muted">You can even roll your own custom sizing with CSS variables:</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button class="" color="primary" style="--vz-btn-padding-y: .25rem;--vz-btn-padding-x: .5rem;--vz-btn-font-size: .75rem;">Custom button</Button>
							</div>
						</div>
						<div class="d-none code-view">
							<pre class="language-markup">
                                <code
									>&lt;Button class="" color="primary" style="--vz-btn-padding-y: .25rem;--vz-btn-padding-x: .5rem;--vz-btn-font-size: .75rem;" &gt;Custom button&lt;/Button&gt;</code
								></pre>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Buttons Toggle Status" />

					<CardBody>
						<p class="text-muted">
							Use <code>data-bs-toggle="button"</code> to toggle a
							button’s active state.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button
									color="primary"
									data-bs-toggle="button"
									aria-pressed="false"
								>
									Single toggle
								</Button>
							</div>
						</div>
						<div class="d-none code-view">
							<pre class="language-markup">
                                <code
									>&lt;!-- Toggle Button Status --&gt;
                                    &lt;button type=&quot;button&quot; class=&quot;btn btn-primary waves-effect waves-light&quot; data-bs-toggle=&quot;button&quot; aria-pressed=&quot;false&quot;&gt;
                                    Single toggle
                                    &lt;/button&gt;</code
								></pre>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Buttons Grid" />

					<CardBody>
						<p class="text-muted">
							Use <code>d-grid</code> class to create a full-width
							block button.
						</p>
						<div class="live-preview">
							<div class="d-grid gap-2">
								<Button color="primary">Button</Button>
								<Button color="primary">Button</Button>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={gridButtonsCode}
								id="gridButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Checkbox & Radio Buttons" />

					<CardBody>
						<p class="text-muted">
							Combine button-like <code>checkbox and radio</code>
							<a
								href="//getbootstrap.com/docs/5.1/forms/checks-radios/"
								>toggle buttons</a
							> into a seamless looking button group.
						</p>
						<div class="live-preview">
							<div
								class="d-flex flex-wrap align-items-center gap-2"
							>
								<ButtonGroup>
									<input
										type="checkbox"
										class="btn-check"
										id="btncheck1"
										checked
									/>
									<Label class="btn btn-primary material-shadow-none mb-0" for="btncheck1">Checkbox 1</Label>

									<input
										type="checkbox"
										class="btn-check"
										id="btncheck2"
									/>
									<Label class="btn btn-primary material-shadow-none mb-0" for="btncheck2">Checkbox 2</Label>


									<input
										type="checkbox"
										class="btn-check"
										id="btncheck3"
									/>
									<Label class="btn btn-primary material-shadow-none mb-0" for="btncheck3">Checkbox 3</Label>

								</ButtonGroup>

								<ButtonGroup>
									<input
										type="radio"
										class="btn-check"
										name="btnradio"
										id="btnradio1"
										checked
									/>
									<Label class="btn btn-outline-secondary material-shadow-none mb-0" for="btnradio1">Radio 1</Label>

									<input
										type="radio"
										class="btn-check"
										name="btnradio"
										id="btnradio2"
									/>
									<Label class="btn btn-outline-secondary material-shadow-none mb-0" for="btnradio2">Radio 2</Label>


									<input
										type="radio"
										class="btn-check"
										name="btnradio"
										id="btnradio3"
									/>
									<Label class="btn btn-outline-secondary material-shadow-none mb-0" for="btnradio3">Radio 3</Label>

								</ButtonGroup>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={checkButtonsCode}
								id="checkButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<PreviewCardHeader title="Buttons Group" />

					<CardBody>
						<p class="text-muted">
							Use the <code>btn-group </code> class in the parent class
							to wrap a series of buttons.
						</p>
						<div class="live-preview">
							<Row>
								<Col sm={6}>
									<ButtonGroup>
										<Button color="primary" class="material-shadow-none">Left</Button>
										<Button color="primary" class="material-shadow-none">Middle</Button>
										<Button color="primary" class="material-shadow-none">Right</Button>
									</ButtonGroup>
								</Col>
								<Col sm={6}>
									<ButtonGroup class="mt-4 mt-sm-0">
										<Button color="light" class="btn-icon material-shadow-none"
											><i
												class="ri-align-right"
											/></Button
										>
										<Button color="light" class="btn-icon material-shadow-none"
											><i
												class="ri-align-center"
											/></Button
										>
										<Button color="light" class="btn-icon material-shadow-none"
											><i class="ri-align-left" /></Button
										>
									</ButtonGroup>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={groupButtonsCode}
								id="groupButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<PreviewCardHeader title="Icon Buttons" />

					<CardBody>
						<p class="text-muted">
							Use <code>btn-icon</code> class to wrap icon in button
						</p>
						<div class="live-preview">
							<Row>
								<Col sm={6}>
									<div class="hstack gap-2">
										<Button color="primary" class="btn-icon"
											><i
												class="ri-map-pin-line"
											/></Button
										>
										<Button color="danger" class="btn-icon">
											<i class="ri-delete-bin-5-line" />
										</Button>
										<Button
											color="success"
											class="btn-icon"
										>
											<i class="ri-check-double-line" />
										</Button>
										<Button color="light" class="btn-icon"
											><i
												class="ri-brush-2-fill"
											/></Button
										>
									</div>
								</Col>
								<Col sm={6}>
									<div class="hstack gap-2 mt-4 mt-sm-0">
										<Button
											color="primary"
											class="btn-icon material-shadow-none waves-effect waves-light"
											outline
										>
											<i class="ri-24-hours-fill" />
										</Button>
										<Button
											color="danger"
											class="btn-icon material-shadow-none waves-effect waves-light"
											outline
										>
											<i
												class="ri-customer-service-2-line"
											/>
										</Button>
										<Button
											color="success"
											class="btn-icon material-shadow-none waves-effect waves-light"
											outline
										>
											<i class="ri-mail-send-line" />
										</Button>
										<Button
											color="warning"
											class="btn-icon material-shadow-none waves-effect waves-light"
											outline
										>
											<i class="ri-menu-2-line" />
										</Button>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={iconButtonsCode}
								id="iconButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Buttons Toolbar" />
					<CardBody>
						<p class="text-muted">
							Use <code>btn-toolbar</code> class to combine sets of
							button groups into more complex components.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-3">
								<ButtonToolbar class="material-shadow">
									<ButtonGroup class="me-2">
										<Button color="light" class="material-shadow-none">1</Button>
										<Button color="light" class="material-shadow-none">2</Button>
										<Button color="light" class="material-shadow-none">3</Button>
										<Button color="light" class="material-shadow-none">4</Button>
									</ButtonGroup>
									<ButtonGroup class="me-2 material-shadow">
										<Button color="light" class="material-shadow-none">5</Button>
										<Button color="light" class="material-shadow-none">6</Button>
										<Button color="light" class="material-shadow-none">7</Button>
									</ButtonGroup>
									<ButtonGroup  class="material-shadow">
										<Button color="light" class="material-shadow-none">8</Button>
									</ButtonGroup>
								</ButtonToolbar>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={toolbarButtonsCode}
								id="toolbarButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Button Group Sizing" />

					<CardBody>
						<p class="text-muted">
							Use <code>btn-group-</code> class with the below-mentioned
							variation to set the different sizes of button groups.
						</p>

						<div class="live-preview">
							<div
								class="d-flex flex-wrap align-items-center gap-2"
							>
								<ButtonGroup size="lg" class="material-shadow">
									<Button color="primary" class="material-shadow-none">Left</Button>
									<Button color="primary" class="material-shadow-none">Middle</Button>
									<Button color="primary" class="material-shadow-none">Right</Button>
								</ButtonGroup>
								<ButtonGroup class="mt-2 material-shadow">
									<Button color="light" class="material-shadow-none">Left</Button>
									<Button color="light" class="material-shadow-none">Middle</Button>
									<Button color="light" class="material-shadow-none">Right</Button>
								</ButtonGroup>
								<ButtonGroup size="sm" class="mt-2 material-shadow">
									<Button color="secondary" class="material-shadow-none">Left</Button>
									<Button color="secondary" class="material-shadow-none">Middle</Button>
									<Button color="secondary" class="material-shadow-none">Right</Button>
								</ButtonGroup>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={groupSizingButtonsCode}
								id="groupSizingButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Vertical Variation" />

					<CardBody>
						<p class="text-muted">
							Make a set of buttons appear <code>vertically</code>
							stacked .Split button dropdowns are not supported here.
						</p>
						<div class="live-preview">
							<Row>
								<div class="col-auto">
									<ButtonGroup class="material-shadow">
										<Button color="primary" class="material-shadow-none">1</Button>
										<Button color="primary" class="material-shadow-none">2</Button>
										<Dropdown id="btnGroupDrop1">
											<DropdownToggle
												color="primary"
												class="material-shadow-none"
												caret>Dropdown</DropdownToggle
											>
											<DropdownMenu>
												<DropdownItem
													>Dropdown link</DropdownItem
												>
												<DropdownItem
													>Dropdown link</DropdownItem
												>
											</DropdownMenu>
										</Dropdown>
									</ButtonGroup>
								</div>
								<div class="col-auto">
									<ButtonGroup vertical class="material-shadow">
										<Button color="light">Button</Button>

										<Dropdown id="btnGroupVerticalDrop1">
											<DropdownToggle color="light" caret
												>Dropdown</DropdownToggle
											>
											<DropdownMenu>
												<DropdownItem
													>Dropdown link</DropdownItem
												>
												<DropdownItem
													>Dropdown link</DropdownItem
												>
											</DropdownMenu>
										</Dropdown>

										<Button color="light" class="material-shadow-none">Button</Button>
										<Button color="light" class="material-shadow-none">Button</Button>
									</ButtonGroup>
								</div>
								<div class="col-auto">
									<ButtonGroup vertical class="material-shadow">
										<input
											type="radio"
											class="btn-check"
											name="vbtn"
											id="vbtn-radio1"
											checked
										/>
										<Label class="btn btn-outline-secondary material-shadow-none" for="vbtn-radio1">Radio 1</Label>
										<input
											type="radio"
											class="btn-check"
											name="vbtn"
											id="vbtn-radio2"
										/>
										<Label class="btn btn-outline-secondary material-shadow-none" for="vbtn-radio2">Radio 2</Label>

										<input
											type="radio"
											class="btn-check"
											name="vbtn"
											id="vbtn-radio3"
										/>
										<Label class="btn btn-outline-secondary material-shadow-none" for="vbtn-radio3">Radio 3</Label>
									</ButtonGroup>
								</div>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={verticalButtonsCode}
								id="verticalButtonsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Focus Ring" />

					<CardBody>
						<p class="text-muted">
							Click directly on the link below to see the focus ring in action.
						</p>
						<div class="d-flex flex-wrap gap-2">
						<div class="live-preview">
							<Link href="#" class="d-inline-flex focus-ring py-1 px-2 text-decoration-none border rounded-2" >Focus Ring</Link>
							<Link href="#" class="d-inline-flex focus-ring py-1 px-2 text-decoration-none border rounded-2" style="--vz-focus-ring-color: rgba(118, 93, 255, .25)">Custom focus ring</Link>
							<Link href="#" class="d-inline-flex focus-ring py-1 px-2 text-decoration-none border rounded-2" style="--vz-focus-ring-x: 10px; --vz-focus-ring-y: 10px; --vz-focus-ring-blur: 4px">Blurry offset focus ring</Link>
						</div>
						<div class="d-none code-view">
							<pre class="language-markup">
                                <code>
&lt;Link href="#" class="d-inline-flex focus-ring py-1 px-2 text-decoration-none border rounded-2" &gt;Focus Ring&lt;/Link&gt;
&lt;Link href="#" class="d-inline-flex focus-ring py-1 px-2 text-decoration-none border rounded-2" style="--vz-focus-ring-color: rgba(118, 93, 255, .25)"&gt;Custom focus ring&lt;/Link&gt;
&lt;Link href="#" class="d-inline-flex focus-ring py-1 px-2 text-decoration-none border rounded-2" style="--vz-focus-ring-x: 10px; --vz-focus-ring-y: 10px; --vz-focus-ring-blur: 4px"&gt;Blurry offset focus ring&lt;/Link&gt;
								</code>
							</pre>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Focus Ring Utilities" />

					<CardBody>
						<p class="text-muted">
							In addition to <code> .focus-ring</code>, we have several <code> .focus-ring-* </code> utilities to modify the helper class defaults. Modify the color with any of our theme colors.
							 Note that the light and dark variants may not be visible on all background colors given current color mode support.
						</p>
						<div class="d-flex flex-wrap gap-2">
						<div class="live-preview">
							<Row>
								<Col lg={6}>
									<p>
										<Link href="#" class="d-inline-flex focus-ring focus-ring-primary py-1 px-2 text-decoration-none border rounded-2" >Primary focus</Link>
									</p>
									<p>
										<Link href="#" class="d-inline-flex focus-ring focus-ring-secondary py-1 px-2 text-decoration-none border rounded-2" >Secondary focus</Link>
									</p>
									<p>
										<Link href="#" class="d-inline-flex focus-ring focus-ring-success py-1 px-2 text-decoration-none border rounded-2" >Success focus</Link>
									</p>
									<p class="mb-lg-0">
										<Link href="#" class="d-inline-flex focus-ring focus-ring-danger py-1 px-2 text-decoration-none border rounded-2" >Danger focus</Link>
									</p>
								</Col>
								<Col lg={6}>
									<p>
										<Link href="#" class="d-inline-flex focus-ring focus-ring-warning  py-1 px-2 text-decoration-none border rounded-2" >Warning focus</Link>
									</p>
									<p>
										<Link href="#" class="d-inline-flex focus-ring focus-ring-info py-1 px-2 text-decoration-none border rounded-2" >Info focus</Link>
									</p>
									<p>
										<Link href="#" class="d-inline-flex focus-ring focus-ring-light py-1 px-2 text-decoration-none border rounded-2" >Light focus</Link>
									</p>
									<p>
										<Link href="#" class="d-inline-flex focus-ring focus-ring-dark py-1 px-2 text-decoration-none border rounded-2" >Dark focus</Link>
									</p>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<pre class="language-markup">
                                <code>
									&lt;p&gt;
										&lt;Link href="#" class="d-inline-flex focus-ring focus-ring-primary py-1 px-2 text-decoration-none border rounded-2" &gt;Primary focus&lt;/Link&gt;
									&lt;/p&gt;
									&lt;p&gt;
										&lt;Link href="#" class="d-inline-flex focus-ring focus-ring-secondary py-1 px-2 text-decoration-none border rounded-2" &gt;Secondary focus&lt;/Link&gt;
									&lt;/p&gt;
									&lt;p&gt;
										&lt;Link href="#" class="d-inline-flex focus-ring focus-ring-success py-1 px-2 text-decoration-none border rounded-2" &gt;Success focus&lt;/Link&gt;
									&lt;/p&gt;
									&lt;p class="mb-lg-0"&gt;
										&lt;Link href="#" class="d-inline-flex focus-ring focus-ring-danger py-1 px-2 text-decoration-none border rounded-2" &gt;Danger focus&lt;/Link&gt;
									&lt;/p&gt;
									&lt;p&gt;
										&lt;Link href="#" class="d-inline-flex focus-ring focus-ring-warning  py-1 px-2 text-decoration-none border rounded-2" &gt;Warning focus&lt;/Link&gt;
									&lt;/p&gt;
									&lt;p&gt;
										&lt;Link href="#" class="d-inline-flex focus-ring focus-ring-info py-1 px-2 text-decoration-none border rounded-2" &gt;Info focus&lt;/Link&gt;
									&lt;/p&gt;
									&lt;p&gt;
										&lt;Link href="#" class="d-inline-flex focus-ring focus-ring-light py-1 px-2 text-decoration-none border rounded-2" &gt;Light focus&lt;/Link&gt;
									&lt;/p&gt;
									&lt;p&gt;
										&lt;Link href="#" class="d-inline-flex focus-ring focus-ring-dark py-1 px-2 text-decoration-none border rounded-2" &gt;Dark focus&lt;/Link&gt;
									&lt;/p&gt;
								</code>
							</pre>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
