<script>
	import {
		Button,
		ButtonGroup,
		Card,
		CardBody,
		Col,
		Container,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Nav,
		NavItem,
		NavLink,
		Row,
		TabContent,
		TabPane,
		Dropdown,
		Label,
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";
	let activeTab = 1;
	let NotificationTab = 1;
	let Notification1Tab = 1;

	import avatar2 from "../../../assets/images/users/avatar-2.jpg";
	import avatar3 from "../../../assets/images/users/avatar-3.jpg";
	import avatar6 from "../../../assets/images/users/avatar-6.jpg";
	import avatar8 from "../../../assets/images/users/avatar-8.jpg";

	import bell from "../../../assets/images/svg/bell.svg";
	// Single Button Dropdown

	const singleButtonDropdownCode = `
<!-- Single Button Dropdown -->
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
		id="dropdownMenuButton"
	>
		Dropdown button <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="a"
		class="btn btn-secondary"
	>
		Dropdown link <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
`;

	// Dropdown Color Variant
	const colorDropdownCode = `
<!-- Dropdown Variant -->
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-primary"
	>
		Primary <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-success"
	>
		Success <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-light"
	>
		Light <i class="mdi mdi-chevron-down" />
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-info"
	>
		Info <i class="mdi mdi-chevron-down" />
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
	>
		Secondary <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-warning"
	>
		Warning <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-danger"
	>
		Danger <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-dark"
	>
		Dark <i class="mdi mdi-chevron-down" />
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>
`;

	// Split Button Dropdown
	const splitButtonDropdownCode = `
<!-- Split Button Dropdown -->
<ButtonGroup>
	<Dropdown>
		<Button color="primary">Primary</Button>
		<DropdownToggle
			tag="button"
			color="primary"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>

<ButtonGroup>
	<Dropdown>
		<Button color="success">Success</Button>
		<DropdownToggle
			tag="button"
			class="btn btn-success"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>

<ButtonGroup>
	<Dropdown>
		<Button color="light">Light</Button>
		<DropdownToggle
			tag="button"
			class="btn btn-light"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>

<ButtonGroup>
	<Dropdown>
		<Button color="info">Info</Button>
		<DropdownToggle
			tag="button"
			class="btn btn-info"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>

<ButtonGroup>
	<Dropdown>
		<Button color="secondary"
			>Secondary</Button
		>
		<DropdownToggle
			tag="button"
			class="btn btn-secondary"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>

<ButtonGroup>
	<Dropdown>
		<Button color="warning">Warning</Button>
		<DropdownToggle
			tag="button"
			class="btn btn-warning"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>

<ButtonGroup>
	<Dropdown>
		<Button color="danger">Danger</Button>
		<DropdownToggle
			tag="button"
			class="btn btn-danger"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>

<ButtonGroup>
	<Dropdown>
		<Button color="dark">Dark</Button>
		<DropdownToggle
			tag="button"
			class="btn btn-dark"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>
`;

	// Dropdown Sizing
	const sizingDropdownCode = `
<!-- Dropdown Sizing -->
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-primary btn-lg"
	>
		Large button <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>

<ButtonGroup>
	<Dropdown>
		<Button color="light" class="btn-lg"
			>Large split button</Button
		>
		<DropdownToggle
			tag="button"
			class="btn btn-light btn-lg"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-primary btn-sm"
	>
		Small button <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>

<ButtonGroup>
	<Dropdown>
		<Button color="light" class="btn-sm"
			>Small split button</Button
		>
		<DropdownToggle
			tag="button"
			class="btn btn-light btn-sm"
			split
		/>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>
`;

	// Dark Dropdowns
	const darkDropdownCode = `
<!-- Dark Dropdowns -->
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
		id="dropdownMenuButton2"
	>
		Dropdown button <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu class="dropdown-menu-dark">
		<DropdownItem active>Action</DropdownItem>
		<DropdownItem>Another action</DropdownItem>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem>Separated link</DropdownItem>
	</DropdownMenu>
</Dropdown>
`;

	// Alignment options
	const alignDropdownCode = `
<!-- Alignment options -->
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
		id="dropdownMenuButton"
	>
		Dropdown <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
	>
		Right-aligned menu <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu end={true}>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
	>
		Left-aligned, right-aligned lg <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu
		class="dropdown-menu-lg-end"
		end={true}
	>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
	>
		Right-aligned, left-aligned lg <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu
		class="dropdown-menu-lg-start"
	>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown direction="start">
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
	>
		Dropstart <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown direction="end">
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
	>
		Dropend <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown direction="up">
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
	>
		Dropup<i class="mdi mdi-chevron-down" />
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>
`;

	// Dropdown Options
	const optionDropdownCode = `
<!-- Dropdown Options -->
<Dropdown class="me-1">
	<DropdownToggle
		tag="button"
		class="btn btn-secondary"
		id="dropdownMenuOffset"
	>
		Dropup<i class="mdi mdi-chevron-down" />
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
	</DropdownMenu>
</Dropdown>

<ButtonGroup>
	<Dropdown>
		<Button color="secondary"
			>Reference</Button
		>
		<DropdownToggle
			tag="button"
			class="btn btn-secondary"
			id="dropdownMenuReference"
			split
		>
			<span class="visually-hidden"
				>Toggle Dropdown</span
			>
		</DropdownToggle>
		<DropdownMenu>
			<DropdownItem>Action</DropdownItem>
			<DropdownItem
				>Another action</DropdownItem
			>
			<DropdownItem
				>Something else here</DropdownItem
			>
			<DropdownItem divider />
			<DropdownItem
				>Separated link</DropdownItem
			>
		</DropdownMenu>
	</Dropdown>
</ButtonGroup>
`;

	// Auto Close Behavior
	const autoCloseDropdownCode = `
<!-- Default dropdown -->
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-light"
	>
		Default dropdown <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-light"
	>
		Clickable outside <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-light"
		id="dropdownMenuClickableInside"
	>
		Clickable inside <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-light"
		id="dropdownMenuClickable"
	>
		Manual close <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
		<DropdownItem>Menu item</DropdownItem>
	</DropdownMenu>
</Dropdown>
`;

	// Dropdown Menu Item Color
	const menuItemDropdownCode = `
<!-- Dropdown Menu Item Color -->
<Row>
	<Col xxl={3}>
		<div>
			<h6 class="font-size-13 mb-3">
				Dropdown Menu Success link example
			</h6>
			<div class="clearfix">
				<div
					class="dropdown-menu d-inline-block position-relative dropdownmenu-success"
					style="z-index: 1"
				>
					<Link
						href={null}
						class="dropdown-item"
						>Action</Link>
					<Link
						href={null}
						class="dropdown-item"
						>Another action</Link>
					<Link
						href={null}
						class="dropdown-item active"
						>Something else here</Link>
					<div class="dropdown-divider" />
					<Link
						href={null}
						class="dropdown-item"
						>Separated link</Link>
				</div>
			</div>
		</div>
	</Col>

	<Col lg={9}>
		<div class="mt-lg-0 mt-3">
			<h6 class="font-size-13 mb-0">
				Dropdown Menu link Color example
			</h6>
			<div>
				<Row>
					<Col lg={4} sm={6}>
						<div class="mt-3">
							<p
								class="font-size-13 mb-2">
								Dropdown menu
								Primary link
							</p>
							<Dropdown>
								<DropdownToggle
									tag="button"
									class="btn btn-primary"
								>
									Primary <i
										class="mdi mdi-chevron-down"
									/>
								</DropdownToggle>
								<DropdownMenu
									class="dropdownmenu-primary"
								>
									<DropdownItem
										>Action</DropdownItem
									>
									<DropdownItem
										>Another
										action</DropdownItem
									>
									<DropdownItem
										>Something
										else here</DropdownItem
									>
									<DropdownItem
										divider
									/>
									<DropdownItem
										>Separated
										link</DropdownItem
									>
								</DropdownMenu>
							</Dropdown>
						</div>
					</Col>
					<Col lg={4} sm={6}>
						<div class="mt-3">
							<p
								class="font-size-13 mb-2">
								Dropdown menu
								Secondary link
							</p>
							<Dropdown>
								<DropdownToggle
									tag="button"
									class="btn btn-secondary"
								>
									Secondary <i
										class="mdi mdi-chevron-down"
									/>
								</DropdownToggle>
								<DropdownMenu
									class="dropdownmenu-secondary"
								>
									<DropdownItem
										>Action</DropdownItem
									>
									<DropdownItem
										>Another
										action</DropdownItem
									>
									<DropdownItem
										>Something
										else here</DropdownItem
									>
									<DropdownItem
										divider
									/>
									<DropdownItem
										>Separated
										link</DropdownItem
									>
								</DropdownMenu>
							</Dropdown>
						</div>
					</Col>
					<Col lg={4} sm={6}>
						<div class="mt-3">
							<p
								class="font-size-13 mb-2">
								Dropdown menu
								Success link
							</p>
							<Dropdown>
								<DropdownToggle
									tag="button"
									class="btn btn-success"
								>
									Success <i
										class="mdi mdi-chevron-down"
									/>
								</DropdownToggle>
								<DropdownMenu
									class="dropdownmenu-success"
								>
									<DropdownItem
										>Action</DropdownItem
									>
									<DropdownItem
										>Another
										action</DropdownItem
									>
									<DropdownItem
										>Something
										else here</DropdownItem
									>
									<DropdownItem
										divider
									/>
									<DropdownItem
										>Separated
										link</DropdownItem
									>
								</DropdownMenu>
							</Dropdown>
						</div>
					</Col>
					<Col lg={4} sm={6}>
						<div class="mt-3">
							<p
								class="font-size-13 mb-2">
								Dropdown menu
								Warning link
							</p>
							<Dropdown>
								<DropdownToggle
									tag="button"
									class="btn btn-warning"
								>
									Warning <i
										class="mdi mdi-chevron-down"
									/>
								</DropdownToggle>
								<DropdownMenu
									class="dropdownmenu-warning"
								>
									<DropdownItem
										>Action</DropdownItem
									>
									<DropdownItem
										>Another
										action</DropdownItem
									>
									<DropdownItem
										>Something
										else here</DropdownItem
									>
									<DropdownItem
										divider
									/>
									<DropdownItem
										>Separated
										link</DropdownItem
									>
								</DropdownMenu>
							</Dropdown>
						</div>
					</Col>
					<Col lg={4} sm={6}>
						<div class="mt-3">
							<p
								class="font-size-13 mb-2">
								Dropdown menu Info
								link
							</p>
							<Dropdown>
								<DropdownToggle
									tag="button"
									class="btn btn-info"
								>
									Info <i
										class="mdi mdi-chevron-down"
									/>
								</DropdownToggle>
								<DropdownMenu
									class="dropdownmenu-info"
								>
									<DropdownItem
										>Action</DropdownItem
									>
									<DropdownItem
										>Another
										action</DropdownItem
									>
									<DropdownItem
										>Something
										else here</DropdownItem
									>
									<DropdownItem
										divider
									/>
									<DropdownItem
										>Separated
										link</DropdownItem
									>
								</DropdownMenu>
							</Dropdown>
						</div>
					</Col>
					<Col lg={4} sm={6}>
						<div class="mt-3">
							<p
								class="font-size-13 mb-2">
								Dropdown menu Danger
								link
							</p>
							<Dropdown>
								<DropdownToggle
									tag="button"
									class="btn btn-danger"
								>
									Danger <i
										class="mdi mdi-chevron-down"
									/>
								</DropdownToggle>
								<DropdownMenu
									class="dropdownmenu-danger"
								>
									<DropdownItem
										>Action</DropdownItem
									>
									<DropdownItem
										>Another
										action</DropdownItem
									>
									<DropdownItem
										>Something
										else here</DropdownItem
									>
									<DropdownItem
										divider
									/>
									<DropdownItem
										>Separated
										link</DropdownItem
									>
								</DropdownMenu>
							</Dropdown>
						</div>
					</Col>
				</Row>
			</div>
		</div>
	</Col>
	</Row>
`;

	// Menu Content
	const menuContentDropdownCode = `
<!-- Menu Content -->
<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-primary"
	>
		Header <i
			class="mdi mdi-chevron-down"
		/>
	</DropdownToggle>
	<DropdownMenu>
		<div class="dropdown-header noti-title">
			<h5
				class="fs-13 text-muted text-truncate mb-0"
			>
				Welcome Jessie!
			</h5>
		</div>
		<DropdownItem>Action</DropdownItem>
		<DropdownItem
			>Another action</DropdownItem
		>
		<DropdownItem
			>Something else here</DropdownItem
		>
		<DropdownItem divider />
		<DropdownItem
			>Separated link</DropdownItem
		>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-success"
	>
		Text <i class="mdi mdi-chevron-down" />
	</DropdownToggle>
	<DropdownMenu class="dropdown-menu-md p-3">
		<p>
			Some example text that's
			free-flowing within the dropdown
			menu.
		</p>
		<p class="mb-0">
			And this is more example text.
		</p>
	</DropdownMenu>
</Dropdown>

<Dropdown>
	<DropdownToggle
		tag="button"
		class="btn btn-light"
	>
		Forms <i class="mdi mdi-chevron-down" />
	</DropdownToggle>
	<DropdownMenu class="dropdown-menu-md p-4">
		<form>
			<div class="mb-2">
				<Label
					class="form-label"
					for="exampleDropdownFormEmail">Email address</Label
				>
				<input
					type="email"
					class="form-control"
					id="exampleDropdownFormEmail"
					placeholder="email@example.com"
				/>
			</div>
			<div class="mb-2">
				<Label
					class="form-label"
					for="exampleDropdownFormPassword">Password</Label
				>
				<input
					type="password"
					class="form-control"
					id="exampleDropdownFormPassword"
					placeholder="Password"
				/>
			</div>
			<div class="mb-2">
				<div
					class="form-check custom-checkbox"
				>
					<input
						type="checkbox"
						class="form-check-input"
						id="rememberdropdownCheck"
					/>
					<Label
						class="form-check-label"
						for="rememberdropdownCheck"
						>Remember me</Label>
				</div>
			</div>
			<Button
				type="submit"
				class="btn btn-primary"
				>Sign in</Button
			>
		</form>
	</DropdownMenu>
</Dropdown>
`;

	// Notifications
	const notificationDropdownCode = `
<!-- Notifications -->
<Row class="g-3">
	<Col xxl={3} lg={5} md={6}>
		<div
			class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0 d-inline-block position-relative w-100"
			aria-labelledby="page-header-notifications-dropdown"
			style="z-index: 1"
		>
			<div
				class="dropdown-head bg-primary bg-pattern rounded-top overflow-hidden"
			>
				<div class="p-3">
					<Row class="align-items-center">
						<Col>
							<h6
								class="m-0 fs-16 fw-semibold text-white">
								Notifications
							</h6>
						</Col>
						<div class="col-auto dropdown-tabs"
						>
							<span
								class="badge bg-light-subtle text-body fs-13">>4 New</span
							>
						</div>
					</Row>
				</div>

				<div class="px-2 pt-2">
					<Nav
						tabs
						class="dropdown-tabs nav-tabs-custom">
						<NavItem>
							<NavLink
								style="cursor: pointer"
								tabId={1}
								on:click={() =>
									(activeTab = 1)}
								active={activeTab ==
									1}>
								All (4)
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink
								style="cursor: pointer"
								tabId={2}
								on:click={() =>
									(activeTab = 2)}
								active={activeTab ==
									2}>
								Messages
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink
								style="cursor: pointer"
								tabId={3}
								on:click={() =>
									(activeTab = 3)}
								active={activeTab ==
									3}>
								Alerts
							</NavLink>
						</NavItem>
					</Nav>
				</div>
			</div>

			<TabContent
				id="notificationItemsTabContent4"
			>
				<TabPane
					tabId={1}
					class={activeTab == 1
						? "py-2 ps-2 active"
						: "py-2 ps-2"}
					id="all-noti-tab1"
				>
					<div data-simplebar
						style="max-height: 300px"
						class="pe-2">
						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<div class="flex-shrink-0 avatar-xs me-3"
								>
									<span
										class="avatar-title bg-info-subtle text-info rounded-circle fs-16"
									>
										<i
											class="bx bx-badge-check"
										/>
									</span>
								</div>
								<div class="flex-1">
									<h6
										class="mt-0 mb-2 lh-base"
									>
										Your <b
											>Elite</b
										>
										author
										Graphic
										Optimization
										<span
											class="text-secondary"
											>reward</span
										> is ready!
									</h6>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> Just 30
											sec ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar2}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Angela
											Bernier
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Answered
											to your
											comment
											on the
											cash
											flow
											forecast's
											graph
											🔔.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 48 min
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<div class="flex-shrink-0 avatar-xs me-3"
								>
									<span
										class="avatar-title bg-danger-subtle text-danger rounded-circle fs-16"
									>
										<i
											class="bx bx-message-square-dots"
										/>
									</span>
								</div>
								<div class="flex-1">
									<h6
										class="mt-0 mb-2 fs-13 lh-base"
									>
										You have
										received <b
											class="text-success"
											>20</b
										> new messages
										in the conversation
									</h6>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 2 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar8}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Maureen
											Gibson
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 4 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="my-3 text-center"
						>
							<button
								type="button"
								class="btn btn-soft-success waves-effect waves-light"
								>View All
								Notifications <i
									class="ri-arrow-right-line align-middle"
								/></button>
						</div>
					</div>
				</TabPane>

				<TabPane
					tabId={2}
					class={activeTab == 2
						? "py-2 ps-2 active"
						: "py-2 ps-2"}
					id="messages-tab1"
				>
					<div data-simplebar
						style="max-height: 300px"
						class="pe-2">
						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar3}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											James
											Lemire
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 30 min
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar2}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Angela
											Bernier
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Answered
											to your
											comment
											on the
											cash
											flow
											forecast's
											graph
											🔔.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 2 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar6}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Kenneth
											Brown
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Mentionned
											you in
											his
											comment
											on 📃
											invoice
											#12501.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 10 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar8}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Maureen
											Gibson
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 3 days
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="my-3 text-center"
						>
							<button
								type="button"
								class="btn btn-soft-success waves-effect waves-light"
								>View All Messages <i
									class="ri-arrow-right-line align-middle"
								/></button>
						</div>
					</div>
				</TabPane>

				<TabPane
					tabId={3}
					class={activeTab == 3
						? "p-4 active"
						: "p-4"}
					id="alerts-tab1"
				>
					<div class="w-50 pt-3 mx-auto">
						<img
							src={bell}
							class="img-fluid"
							alt="user-pic"
						/>
					</div>
					<div class="text-center pb-5 mt-2">
						<h6
							class="fs-18 fw-semibold lh-base"
						>
							Hey! You have no any
							notifications
						</h6>
					</div>
				</TabPane>
			</TabContent>
		</div>
	</Col>

	<Col xxl={3} lg={5} md={6}>
		<div
			class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0 d-inline-block position-relative w-100"
			aria-labelledby="page-header-notifications-dropdown"
			style="z-index: 1"
		>
			<div
				class="dropdown-head bg-success bg-pattern rounded-top overflow-hidden"
			>
				<div class="p-3">
					<Row class="align-items-center">
						<Col>
							<h6
								class="m-0 fs-16 fw-semibold text-white">
								Notifications
							</h6>
						</Col>
						<div class="col-auto dropdown-tabs"
						>
							<span
								class="badge bg-light-subtle text-body fs-13">>4 New</span
							>
						</div>
					</Row>
				</div>

				<div class="px-2 pt-2">
					<Nav
						tabs
						class="dropdown-tabs nav-tabs-custom">
						<NavItem>
							<NavLink
								style="cursor: pointer"
								on:click={() =>
									(NotificationTab = 1)}
								active={NotificationTab ==
									1}>
								All (4)
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink
								style="cursor: pointer"
								on:click={() =>
									(NotificationTab = 2)}
								active={NotificationTab ==
									2}>
								Messages
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink
								style="cursor: pointer"
								on:click={() =>
									(NotificationTab = 3)}
								active={NotificationTab ==
									3}>
								Alerts
							</NavLink>
						</NavItem>
					</Nav>
				</div>
			</div>

			<TabContent
				id="notificationItemsTabContent1"
			>
				<TabPane
					tabId={1}
					class={NotificationTab == 1
						? "active py-2 ps-2"
						: "py-2 ps-2"}
					id="all-noti-tab2"
				>
					<div data-simplebar
						style="max-height: 300px"
						class="pe-2">
						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<div class="flex-shrink-0 avatar-xs me-3"
								>
									<span
										class="avatar-title bg-info-subtle text-info rounded-circle fs-16"
									>
										<i
											class="bx bx-badge-check"
										/>
									</span>
								</div>
								<div class="flex-1">
									<h6
										class="mt-0 mb-2 lh-base"
									>
										Your <b
											>Elite</b
										>
										author
										Graphic
										Optimization
										<span
											class="text-secondary"
											>reward</span
										> is ready!
									</h6>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> Just 30
											sec ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar2}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Angela
											Bernier
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Answered
											to your
											comment
											on the
											cash
											flow
											forecast's
											graph
											🔔.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 48 min
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<div class="flex-shrink-0 avatar-xs me-3"
								>
									<span
										class="avatar-title bg-danger-subtle text-danger rounded-circle fs-16"
									>
										<i
											class="bx bx-message-square-dots"
										/>
									</span>
								</div>
								<div class="flex-1">
									<h6
										class="mt-0 mb-2 fs-13 lh-base"
									>
										You have
										received <b
											class="text-success"
											>20</b
										> new messages
										in the conversation
									</h6>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 2 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar8}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Maureen
											Gibson
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 4 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="my-3 text-center"
						>
							<Button
								color="success"
								class="btn btn-soft-success"
								>View All
								Notifications <i
									class="ri-arrow-right-line align-middle"
								/></Button>
						</div>
					</div>
				</TabPane>

				<TabPane
					tabId={2}
					class={NotificationTab == 2
						? "active py-2 ps-2"
						: "py-2 ps-2"}
					id="messages-tab2"
				>
					<div data-simplebar
						style="max-height: 300px"
						class="pe-2">
						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar3}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											James
											Lemire
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 30 min
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar2}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Angela
											Bernier
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Answered
											to your
											comment
											on the
											cash
											flow
											forecast's
											graph
											🔔.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 2 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar6}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Kenneth
											Brown
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Mentionned
											you in
											his
											comment
											on 📃
											invoice
											#12501.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 10 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar8}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Maureen
											Gibson
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 3 days
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="my-3 text-center"
						>
							<Button
								color="success"
								class="btn btn-soft-success"
								>View All Messages <i
									class="ri-arrow-right-line align-middle"
								/></Button>
						</div>
					</div>
				</TabPane>

				<TabPane
					tabId={1}
					class={NotificationTab == 3
						? "active p-4"
						: "p-4"}
					id="alerts-tab2"
				>
					<div class="w-50 pt-3 mx-auto">
						<img
							src={bell}
							class="img-fluid"
							alt="user-pic"
						/>
					</div>
					<div class="text-center pb-5 mt-2">
						<h6
							class="fs-18 fw-semibold lh-base"
						>
							Hey! You have no any
							notifications
						</h6>
					</div>
				</TabPane>
			</TabContent>
		</div>
	</Col>

	<Col xxl={3} lg={5} md={6}>
		<div
			class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0 d-inline-block position-relative w-100"
			aria-labelledby="page-header-notifications-dropdown"
			style="z-index: 1"
		>
			<div
				class="dropdown-head bg-secondary bg-pattern rounded-top overflow-hidden"
			>
				<div class="p-3">
					<Row class="align-items-center">
						<Col>
							<h6
								class="m-0 fs-16 fw-semibold text-white">
								Notifications
							</h6>
						</Col>
						<div class="col-auto dropdown-tabs"
						>
							<span
								class="badge bg-light-subtle text-body fs-13">>4 New</span
							>
						</div>
					</Row>
				</div>

				<div class="px-2 pt-2">
					<Nav
						tabs
						class="dropdown-tabs nav-tabs-custom">
						<NavItem>
							<NavLink
								style="cursor: pointer"
								on:click={() =>
									(Notification1Tab = 1)}
								active={Notification1Tab ==
									1}>
								All (4)
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink
								style="cursor: pointer"
								on:click={() =>
									(Notification1Tab = 2)}
								active={Notification1Tab ==
									2}>
								Messages
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink
								style="cursor: pointer"
								on:click={() =>
									(Notification1Tab = 3)}
								active={Notification1Tab ==
									3}>
								Alerts
							</NavLink>
						</NavItem>
					</Nav>
				</div>
			</div>

			<TabContent
				id="notificationItemsTabContent3"
			>
				<TabPane
					tabId={1}
					class={Notification1Tab == 1
						? "active py-2 ps-2"
						: "py-2 ps-2"}
					id="all-noti-tab1"
				>
					<div data-simplebar
						style="max-height: 300px"
						class="pe-2">
						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<div class="flex-shrink-0 avatar-xs me-3"
								>
									<span
										class="avatar-title bg-info-subtle text-info rounded-circle fs-16"
									>
										<i
											class="bx bx-badge-check"
										/>
									</span>
								</div>
								<div class="flex-1">
									<h6
										class="mt-0 mb-2 lh-base"
									>
										Your <b
											>Elite</b
										>
										author
										Graphic
										Optimization
										<span
											class="text-secondary"
											>reward</span
										> is ready!
									</h6>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> Just 30
											sec ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar2}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Angela
											Bernier
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Answered
											to your
											comment
											on the
											cash
											flow
											forecast's
											graph
											🔔.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 48 min
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<div class="flex-shrink-0 avatar-xs me-3"
								>
									<span
										class="avatar-title bg-danger-subtle text-danger rounded-circle fs-16"
									>
										<i
											class="bx bx-message-square-dots"
										/>
									</span>
								</div>
								<div class="flex-1">
									<h6
										class="mt-0 mb-2 fs-13 lh-base"
									>
										You have
										received <b
											class="text-success"
											>20</b
										> new messages
										in the conversation
									</h6>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 2 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar8}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Maureen
											Gibson
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 4 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="my-3 text-center"
						>
							<Button
								color="success"
								class="btn btn-soft-success"
								>View All
								Notifications <i
									class="ri-arrow-right-line align-middle"
								/></Button>
						</div>
					</div>
				</TabPane>

				<TabPane
					tabId={1}
					class={Notification1Tab == 2
						? "active py-2 ps-2"
						: "py-2 ps-2"}
					id="messages-tab3"
				>
					<div data-simplebar
						style="max-height: 300px"
						class="pe-2">
						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar3}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											James
											Lemire
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 30 min
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar2}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Angela
											Bernier
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Answered
											to your
											comment
											on the
											cash
											flow
											forecast's
											graph
											🔔.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 2 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar6}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Kenneth
											Brown
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											Mentionned
											you in
											his
											comment
											on 📃
											invoice
											#12501.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 10 hrs
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="text-reset notification-item d-block dropdown-item"
						>
							<div class="d-flex">
								<img
									src={avatar8}
									class="me-3 rounded-circle avatar-xs"
									alt="user-pic"
								/>
								<div class="flex-1">
									<Link href={null}
										><h6
											class="mt-0 mb-1 fs-13 fw-semibold"
										>
											Maureen
											Gibson
										</h6></Link
									>
									<div class="fs-13 text-muted"
									>
										<p
											class="mb-1"
										>
											We
											talked
											about a
											project
											on
											linkedin.
										</p>
									</div>
									<p
										class="mb-0 fs-11 fw-medium text-uppercase text-muted"
									>
										<span
											><i
												class="mdi mdi-clock-outline"
											/> 3 days
											ago</span
										>
									</p>
								</div>
								<div class="px-2 fs-16"
								>
									<input
										class="form-check-input"
										type="checkbox"
									/>
								</div>
							</div>
						</div>

						<div class="my-3 text-center"
						>
							<Button
								color="success"
								class="btn btn-soft-success"
								>View All Messages <i
									class="ri-arrow-right-line align-middle"
								/></Button>
						</div>
					</div>
				</TabPane>

				<TabPane
					tabId={1}
					class={Notification1Tab == 3
						? "active p-4"
						: "p-4"}
					id="alerts-tab3"
				>
					<div class="w-50 pt-3 mx-auto">
						<img
							src={bell}
							class="img-fluid"
							alt="user-pic"
						/>
					</div>
					<div class="text-center pb-5 mt-2">
						<h6
							class="fs-18 fw-semibold lh-base"
						>
							Hey! You have no any
							notifications
						</h6>
					</div>
				</TabPane>
			</TabContent>
		</div>
	</Col>
</Row>
`;
</script>

<svelte:head>
	<title>Dropdowns | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Dropdowns" pageTitle="Base UI" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Single Button Dropdown" />

					<CardBody>
						<p class="text-muted">
							Use <code>btn</code> class at to create a dropdown toggle
							with &lt;button&gt; element.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-3">
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
										id="dropdownMenuButton"
									>
										Dropdown button <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="a"
										class="btn btn-secondary"
									>
										Dropdown link <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={singleButtonDropdownCode}
								id="singleButtonDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Dropdown Color Variant" />
					<CardBody>
						<p class="text-muted">
							Use <code>btn-</code> class with below mentioned variation
							to color dropdown toggle.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-3">
								<Dropdown>
									<DropdownToggle
										tag="button"
										color="primary"
									>
										Primary <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-success"
									>
										Success <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-light"
									>
										Light <i class="mdi mdi-chevron-down" />
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-info"
									>
										Info <i class="mdi mdi-chevron-down" />
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
									>
										Secondary <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-warning"
									>
										Warning <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-danger"
									>
										Danger <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-dark"
									>
										Dark <i class="mdi mdi-chevron-down" />
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={colorDropdownCode}
								id="colorDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Split Button Dropdown" />
					<CardBody>
						<p class="text-muted">
							Use <code>divider</code> attribute to DropdownItem to
							create split button dropdowns as a single button dropdown.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-3">
								<ButtonGroup>
									<Dropdown>
										<Button color="primary">Primary</Button>
										<DropdownToggle
											tag="button"
											color="primary"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>

								<ButtonGroup>
									<Dropdown>
										<Button color="success">Success</Button>
										<DropdownToggle
											tag="button"
											class="btn btn-success"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>

								<ButtonGroup>
									<Dropdown>
										<Button color="light">Light</Button>
										<DropdownToggle
											tag="button"
											class="btn btn-light"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>

								<ButtonGroup>
									<Dropdown>
										<Button color="info">Info</Button>
										<DropdownToggle
											tag="button"
											class="btn btn-info"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>

								<ButtonGroup>
									<Dropdown>
										<Button color="secondary"
											>Secondary</Button
										>
										<DropdownToggle
											tag="button"
											class="btn btn-secondary"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>

								<ButtonGroup>
									<Dropdown>
										<Button color="warning">Warning</Button>
										<DropdownToggle
											tag="button"
											class="btn btn-warning"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>

								<ButtonGroup>
									<Dropdown>
										<Button color="danger">Danger</Button>
										<DropdownToggle
											tag="button"
											class="btn btn-danger"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>

								<ButtonGroup>
									<Dropdown>
										<Button color="dark">Dark</Button>
										<DropdownToggle
											tag="button"
											class="btn btn-dark"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={splitButtonDropdownCode}
								id="splitButtonDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Dropdown Sizing" />

					<CardBody>
						<p class="text-muted">
							Use <code>btn-lg</code> class to create a large size
							dropdown button and
							<code>btn-sm</code> to create a small size dropdown button.
						</p>
						<div class="live-preview">
							<div
								class="d-flex flex-wrap gap-3 align-items-center"
							>
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn-lg"
										color="primary"
									>
										Large button <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>

								<ButtonGroup>
									<Dropdown>
										<Button color="light" class="btn-lg"
											>Large split button</Button
										>
										<DropdownToggle
											tag="button"
											class="btn btn-light btn-lg"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>

								<Dropdown>
									<DropdownToggle
										tag="button"
										color="primary"
										class="btn-sm"
									>
										Small button <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>

								<ButtonGroup>
									<Dropdown>
										<Button color="light" class="btn-sm"
											>Small split button</Button
										>
										<DropdownToggle
											tag="button"
											class="btn btn-light btn-sm"
											split
										/>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={sizingDropdownCode}
								id="sizingDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Dark Dropdowns" />

					<CardBody>
						<p class="text-muted">
							Use <code>dropdown-menu-dark</code> class onto an existing
							dropdown-menu to create dropdown items dark.
						</p>
						<div class="live-preview">
							<Dropdown>
								<DropdownToggle
									tag="button"
									class="btn btn-secondary"
									id="dropdownMenuButton2"
								>
									Dropdown button <i
										class="mdi mdi-chevron-down"
									/>
								</DropdownToggle>
								<DropdownMenu class="dropdown-menu-dark">
									<DropdownItem active>Action</DropdownItem>
									<DropdownItem>Another action</DropdownItem>
									<DropdownItem
										>Something else here</DropdownItem
									>
									<DropdownItem divider />
									<DropdownItem>Separated link</DropdownItem>
								</DropdownMenu>
							</Dropdown>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={darkDropdownCode}
								id="darkDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Alignment options" />

					<CardBody>
						<p class="text-muted">
							Dropdown demo with various <code
								>dropdown alignment</code
							> options.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-3">
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
										id="dropdownMenuButton"
									>
										Dropdown <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
									>
										Right-aligned menu <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu end={true}>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
									>
										Left-aligned, right-aligned lg <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu
										class="dropdown-menu-lg-end"
										end={true}
									>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
									>
										Right-aligned, left-aligned lg <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu
										class="dropdown-menu-lg-start"
									>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown direction="start">
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
									>
										Dropstart <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown direction="end">
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
									>
										Dropend <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown direction="up">
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
									>
										Dropup<i class="mdi mdi-chevron-down" />
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={alignDropdownCode}
								id="alignDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Dropdown Options" />

					<CardBody>
						<p class="text-muted">
							Use <code>data-bs-offset</code> or
							<code>data-bs-reference</code> to change the position
							of the dropdown.
						</p>

						<div class="live-preview">
							<div class="d-flex flex-wrap gap-3">
								<Dropdown class="me-1">
									<DropdownToggle
										tag="button"
										class="btn btn-secondary"
										id="dropdownMenuOffset"
									>
										Dropup<i class="mdi mdi-chevron-down" />
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>

								<ButtonGroup>
									<Dropdown>
										<Button color="secondary"
											>Reference</Button
										>
										<DropdownToggle
											tag="button"
											class="btn btn-secondary"
											id="dropdownMenuReference"
											split
										>
											<span class="visually-hidden"
												>Toggle Dropdown</span
											>
										</DropdownToggle>
										<DropdownMenu>
											<DropdownItem>Action</DropdownItem>
											<DropdownItem
												>Another action</DropdownItem
											>
											<DropdownItem
												>Something else here</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem
												>Separated link</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</ButtonGroup>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={optionDropdownCode}
								id="optionDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Auto Close Behavior" />

					<CardBody>
						<p class="text-muted">
							By default, the dropdown menu is closed when
							clicking inside or outside the dropdown menu. You
							can use the <code>autoClose</code> option to change this
							behavior of the dropdown.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-3">
								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-light"
									>
										Default dropdown <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-light"
									>
										Clickable outside <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-light"
										id="dropdownMenuClickableInside"
									>
										Clickable inside <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-light"
										id="dropdownMenuClickable"
									>
										Manual close <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
										<DropdownItem>Menu item</DropdownItem>
									</DropdownMenu>
								</Dropdown>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={autoCloseDropdownCode}
								id="autoCloseDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Dropdown Menu Item Color" />

					<CardBody>
						<p class="text-muted">
							Example of dropdown menu and dropdown item color.
						</p>
						<div class="live-preview">
							<Row>
								<Col xxl={3}>
									<div>
										<h6 class="font-size-13 mb-3">
											Dropdown Menu Success link example
										</h6>
										<div class="clearfix">
											<div
												class="dropdown-menu d-inline-block position-relative dropdownmenu-success"
												style="z-index: 1"
											>
												<Link
													href={null}
													class="dropdown-item"
													>Action</Link
												>
												<Link
													href={null}
													class="dropdown-item"
													>Another action</Link
												>
												<Link
													href={null}
													class="dropdown-item active"
													>Something else here</Link
												>
												<div class="dropdown-divider" />
												<Link
													href={null}
													class="dropdown-item"
													>Separated link</Link
												>
											</div>
										</div>
									</div>
								</Col>

								<Col lg={9}>
									<div class="mt-lg-0 mt-3">
										<h6 class="font-size-13 mb-0">
											Dropdown Menu link Color example
										</h6>
										<div>
											<Row>
												<Col lg={4} sm={6}>
													<div class="mt-3">
														<p
															class="font-size-13 mb-2"
														>
															Dropdown menu
															Primary link
														</p>
														<Dropdown>
															<DropdownToggle
																tag="button"
																class="btn btn-primary"
															>
																Primary <i
																	class="mdi mdi-chevron-down"
																/>
															</DropdownToggle>
															<DropdownMenu
																class="dropdownmenu-primary"
															>
																<DropdownItem
																	>Action</DropdownItem
																>
																<DropdownItem
																	>Another
																	action</DropdownItem
																>
																<DropdownItem
																	>Something
																	else here</DropdownItem
																>
																<DropdownItem
																	divider
																/>
																<DropdownItem
																	>Separated
																	link</DropdownItem
																>
															</DropdownMenu>
														</Dropdown>
													</div>
												</Col>
												<Col lg={4} sm={6}>
													<div class="mt-3">
														<p
															class="font-size-13 mb-2"
														>
															Dropdown menu
															Secondary link
														</p>
														<Dropdown>
															<DropdownToggle
																tag="button"
																class="btn btn-secondary"
															>
																Secondary <i
																	class="mdi mdi-chevron-down"
																/>
															</DropdownToggle>
															<DropdownMenu
																class="dropdownmenu-secondary"
															>
																<DropdownItem
																	>Action</DropdownItem
																>
																<DropdownItem
																	>Another
																	action</DropdownItem
																>
																<DropdownItem
																	>Something
																	else here</DropdownItem
																>
																<DropdownItem
																	divider
																/>
																<DropdownItem
																	>Separated
																	link</DropdownItem
																>
															</DropdownMenu>
														</Dropdown>
													</div>
												</Col>
												<Col lg={4} sm={6}>
													<div class="mt-3">
														<p
															class="font-size-13 mb-2"
														>
															Dropdown menu
															Success link
														</p>
														<Dropdown>
															<DropdownToggle
																tag="button"
																class="btn btn-success"
															>
																Success <i
																	class="mdi mdi-chevron-down"
																/>
															</DropdownToggle>
															<DropdownMenu
																class="dropdownmenu-success"
															>
																<DropdownItem
																	>Action</DropdownItem
																>
																<DropdownItem
																	>Another
																	action</DropdownItem
																>
																<DropdownItem
																	>Something
																	else here</DropdownItem
																>
																<DropdownItem
																	divider
																/>
																<DropdownItem
																	>Separated
																	link</DropdownItem
																>
															</DropdownMenu>
														</Dropdown>
													</div>
												</Col>
												<Col lg={4} sm={6}>
													<div class="mt-3">
														<p
															class="font-size-13 mb-2"
														>
															Dropdown menu
															Warning link
														</p>
														<Dropdown>
															<DropdownToggle
																tag="button"
																class="btn btn-warning"
															>
																Warning <i
																	class="mdi mdi-chevron-down"
																/>
															</DropdownToggle>
															<DropdownMenu
																class="dropdownmenu-warning"
															>
																<DropdownItem
																	>Action</DropdownItem
																>
																<DropdownItem
																	>Another
																	action</DropdownItem
																>
																<DropdownItem
																	>Something
																	else here</DropdownItem
																>
																<DropdownItem
																	divider
																/>
																<DropdownItem
																	>Separated
																	link</DropdownItem
																>
															</DropdownMenu>
														</Dropdown>
													</div>
												</Col>
												<Col lg={4} sm={6}>
													<div class="mt-3">
														<p
															class="font-size-13 mb-2"
														>
															Dropdown menu Info
															link
														</p>
														<Dropdown>
															<DropdownToggle
																tag="button"
																class="btn btn-info"
															>
																Info <i
																	class="mdi mdi-chevron-down"
																/>
															</DropdownToggle>
															<DropdownMenu
																class="dropdownmenu-info"
															>
																<DropdownItem
																	>Action</DropdownItem
																>
																<DropdownItem
																	>Another
																	action</DropdownItem
																>
																<DropdownItem
																	>Something
																	else here</DropdownItem
																>
																<DropdownItem
																	divider
																/>
																<DropdownItem
																	>Separated
																	link</DropdownItem
																>
															</DropdownMenu>
														</Dropdown>
													</div>
												</Col>
												<Col lg={4} sm={6}>
													<div class="mt-3">
														<p
															class="font-size-13 mb-2"
														>
															Dropdown menu Danger
															link
														</p>
														<Dropdown>
															<DropdownToggle
																tag="button"
																class="btn btn-danger"
															>
																Danger <i
																	class="mdi mdi-chevron-down"
																/>
															</DropdownToggle>
															<DropdownMenu
																class="dropdownmenu-danger"
															>
																<DropdownItem
																	>Action</DropdownItem
																>
																<DropdownItem
																	>Another
																	action</DropdownItem
																>
																<DropdownItem
																	>Something
																	else here</DropdownItem
																>
																<DropdownItem
																	divider
																/>
																<DropdownItem
																	>Separated
																	link</DropdownItem
																>
															</DropdownMenu>
														</Dropdown>
													</div>
												</Col>
											</Row>
										</div>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={menuItemDropdownCode}
								id="menuItemDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Menu Content" />

					<CardBody>
						<p class="text-muted">
							Example of dropdown menu containing <code
								>Headers, Text and Forms</code
							> content.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Dropdown>
									<DropdownToggle
										tag="button"
										color="primary"
									>
										Header <i
											class="mdi mdi-chevron-down"
										/>
									</DropdownToggle>
									<DropdownMenu>
										<div class="dropdown-header noti-title">
											<h5
												class="fs-13 text-muted text-truncate mb-0"
											>
												Welcome Jessie!
											</h5>
										</div>
										<DropdownItem>Action</DropdownItem>
										<DropdownItem
											>Another action</DropdownItem
										>
										<DropdownItem
											>Something else here</DropdownItem
										>
										<DropdownItem divider />
										<DropdownItem
											>Separated link</DropdownItem
										>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-success"
									>
										Text <i class="mdi mdi-chevron-down" />
									</DropdownToggle>
									<DropdownMenu class="dropdown-menu-md p-3">
										<p>
											Some example text that's
											free-flowing within the dropdown
											menu.
										</p>
										<p class="mb-0">
											And this is more example text.
										</p>
									</DropdownMenu>
								</Dropdown>

								<Dropdown>
									<DropdownToggle
										tag="button"
										class="btn btn-light"
									>
										Forms <i class="mdi mdi-chevron-down" />
									</DropdownToggle>
									<DropdownMenu class="dropdown-menu-md p-4">
										<form>
											<div class="mb-2">
												<Label
													class="form-label"
													for="exampleDropdownFormEmail"
													>Email address</Label
												>
												<input
													type="email"
													class="form-control"
													id="exampleDropdownFormEmail"
													placeholder="email@example.com"
												/>
											</div>
											<div class="mb-2">
												<Label
													class="form-label"
													for="exampleDropdownFormPassword"
													>Password</Label
												>
												<input
													type="password"
													class="form-control"
													id="exampleDropdownFormPassword"
													placeholder="Password"
												/>
											</div>
											<div class="mb-2">
												<div
													class="form-check custom-checkbox"
												>
													<input
														type="checkbox"
														class="form-check-input"
														id="rememberdropdownCheck"
													/>
													<Label
														class="form-check-label"
														for="rememberdropdownCheck"
														>Remember me</Label
													>
												</div>
											</div>
											<Button
												type="submit"
												class="btn btn-primary"
												>Sign in</Button
											>
										</form>
									</DropdownMenu>
								</Dropdown>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={menuContentDropdownCode}
								id="menuContentDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Notifications" />
					<CardBody>
						<p class="text-muted">
							Dropdown with notification containing multiple tabs.
						</p>
						<div class="live-preview">
							<Row class="g-3">
								<Col xxl={3} lg={5} md={6}>
									<div
										class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0 d-inline-block position-relative w-100"
										aria-labelledby="page-header-notifications-dropdown"
										style="z-index: 1"
									>
										<div
											class="dropdown-head bg-primary bg-pattern rounded-top overflow-hidden"
										>
											<div class="p-3">
												<Row class="align-items-center">
													<Col>
														<h6
															class="m-0 fs-16 fw-semibold text-white"
														>
															Notifications
														</h6>
													</Col>
													<div
														class="col-auto dropdown-tabs"
													>
														<span
															class="badge bg-light-subtle text-body fs-13"
														>
															4 New</span
														>
													</div>
												</Row>
											</div>

											<div class="px-2 pt-2">
												<Nav
													tabs
													class="dropdown-tabs nav-tabs-custom"
												>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															tabId={1}
															on:click={() =>
																(activeTab = 1)}
															active={activeTab ==
																1}
														>
															All (4)
														</NavLink>
													</NavItem>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															tabId={2}
															on:click={() =>
																(activeTab = 2)}
															active={activeTab ==
																2}
														>
															Messages
														</NavLink>
													</NavItem>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															tabId={3}
															on:click={() =>
																(activeTab = 3)}
															active={activeTab ==
																3}
														>
															Alerts
														</NavLink>
													</NavItem>
												</Nav>
											</div>
										</div>

										<TabContent
											id="notificationItemsTabContent4"
										>
											<TabPane
												tabId={1}
												class={activeTab == 1
													? "py-2 ps-2 active"
													: "py-2 ps-2"}
												id="all-noti-tab1"
											>
												<div
													data-simplebar
													style="max-height: 300px"
													class="pe-2"
												>
													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<div
																class="flex-shrink-0 avatar-xs me-3"
															>
																<span
																	class="avatar-title bg-info-subtle text-info rounded-circle fs-16"
																>
																	<i
																		class="bx bx-badge-check"
																	/>
																</span>
															</div>
															<div class="flex-1">
																<h6
																	class="mt-0 mb-2 lh-base"
																>
																	Your <b
																		>Elite</b
																	>
																	author Graphic
																	Optimization
																	<span
																		class="text-secondary"
																		>reward</span
																	> is ready!
																</h6>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> Just 30
																		sec ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar2}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Angela
																		Bernier
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Answered
																		to your
																		comment
																		on the
																		cash
																		flow
																		forecast's
																		graph
																		🔔.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 48 min
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<div
																class="flex-shrink-0 avatar-xs me-3"
															>
																<span
																	class="avatar-title bg-danger-subtle text-danger rounded-circle fs-16"
																>
																	<i
																		class="bx bx-message-square-dots"
																	/>
																</span>
															</div>
															<div class="flex-1">
																<h6
																	class="mt-0 mb-2 fs-13 lh-base"
																>
																	You have
																	received <b
																		class="text-success"
																		>20</b
																	> new messages
																	in the conversation
																</h6>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 2 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar8}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Maureen
																		Gibson
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 4 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="my-3 text-center"
													>
														<button
															type="button"
															class="btn btn-soft-success waves-effect waves-light"
															>View All
															Notifications <i
																class="ri-arrow-right-line align-middle"
															/></button
														>
													</div>
												</div>
											</TabPane>

											<TabPane
												tabId={2}
												class={activeTab == 2
													? "py-2 ps-2 active"
													: "py-2 ps-2"}
												id="messages-tab1"
											>
												<div
													data-simplebar
													style="max-height: 300px"
													class="pe-2"
												>
													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar3}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		James
																		Lemire
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 30 min
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar2}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Angela
																		Bernier
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Answered
																		to your
																		comment
																		on the
																		cash
																		flow
																		forecast's
																		graph
																		🔔.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 2 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar6}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Kenneth
																		Brown
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Mentionned
																		you in
																		his
																		comment
																		on 📃
																		invoice
																		#12501.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 10 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar8}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Maureen
																		Gibson
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 3 days
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="my-3 text-center"
													>
														<button
															type="button"
															class="btn btn-soft-success waves-effect waves-light"
															>View All Messages <i
																class="ri-arrow-right-line align-middle"
															/></button
														>
													</div>
												</div>
											</TabPane>

											<TabPane
												tabId={3}
												class={activeTab == 3
													? "p-4 active"
													: "p-4"}
												id="alerts-tab1"
											>
												<div class="w-50 pt-3 mx-auto">
													<img
														src={bell}
														class="img-fluid"
														alt="user-pic"
													/>
												</div>
												<div
													class="text-center pb-5 mt-2"
												>
													<h6
														class="fs-18 fw-semibold lh-base"
													>
														Hey! You have no any
														notifications
													</h6>
												</div>
											</TabPane>
										</TabContent>
									</div>
								</Col>

								<Col xxl={3} lg={5} md={6}>
									<div
										class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0 d-inline-block position-relative w-100"
										aria-labelledby="page-header-notifications-dropdown"
										style="z-index: 1"
									>
										<div
											class="dropdown-head bg-success bg-pattern rounded-top overflow-hidden"
										>
											<div class="p-3">
												<Row class="align-items-center">
													<Col>
														<h6
															class="m-0 fs-16 fw-semibold text-white"
														>
															Notifications
														</h6>
													</Col>
													<div
														class="col-auto dropdown-tabs"
													>
														<span
															class="badge bg-light-subtle text-body fs-13"
														>
															4 New</span
														>
													</div>
												</Row>
											</div>

											<div class="px-2 pt-2">
												<Nav
													tabs
													class="dropdown-tabs nav-tabs-custom"
												>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															on:click={() =>
																(NotificationTab = 1)}
															active={NotificationTab ==
																1}
														>
															All (4)
														</NavLink>
													</NavItem>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															on:click={() =>
																(NotificationTab = 2)}
															active={NotificationTab ==
																2}
														>
															Messages
														</NavLink>
													</NavItem>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															on:click={() =>
																(NotificationTab = 3)}
															active={NotificationTab ==
																3}
														>
															Alerts
														</NavLink>
													</NavItem>
												</Nav>
											</div>
										</div>

										<TabContent
											id="notificationItemsTabContent1"
										>
											<TabPane
												tabId={1}
												class={NotificationTab == 1
													? "active py-2 ps-2"
													: "py-2 ps-2"}
												id="all-noti-tab2"
											>
												<div
													data-simplebar
													style="max-height: 300px"
													class="pe-2"
												>
													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<div
																class="flex-shrink-0 avatar-xs me-3"
															>
																<span
																	class="avatar-title bg-info-subtle text-info rounded-circle fs-16"
																>
																	<i
																		class="bx bx-badge-check"
																	/>
																</span>
															</div>
															<div class="flex-1">
																<h6
																	class="mt-0 mb-2 lh-base"
																>
																	Your <b
																		>Elite</b
																	>
																	author Graphic
																	Optimization
																	<span
																		class="text-secondary"
																		>reward</span
																	> is ready!
																</h6>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> Just 30
																		sec ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar2}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Angela
																		Bernier
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Answered
																		to your
																		comment
																		on the
																		cash
																		flow
																		forecast's
																		graph
																		🔔.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 48 min
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<div
																class="flex-shrink-0 avatar-xs me-3"
															>
																<span
																	class="avatar-title bg-danger-subtle text-danger rounded-circle fs-16"
																>
																	<i
																		class="bx bx-message-square-dots"
																	/>
																</span>
															</div>
															<div class="flex-1">
																<h6
																	class="mt-0 mb-2 fs-13 lh-base"
																>
																	You have
																	received <b
																		class="text-success"
																		>20</b
																	> new messages
																	in the conversation
																</h6>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 2 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar8}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Maureen
																		Gibson
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 4 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="my-3 text-center"
													>
														<Button
															color="success"
															class="btn btn-soft-success"
															>View All
															Notifications <i
																class="ri-arrow-right-line align-middle"
															/></Button
														>
													</div>
												</div>
											</TabPane>

											<TabPane
												tabId={2}
												class={NotificationTab == 2
													? "active py-2 ps-2"
													: "py-2 ps-2"}
												id="messages-tab2"
											>
												<div
													data-simplebar
													style="max-height: 300px"
													class="pe-2"
												>
													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar3}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		James
																		Lemire
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 30 min
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar2}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Angela
																		Bernier
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Answered
																		to your
																		comment
																		on the
																		cash
																		flow
																		forecast's
																		graph
																		🔔.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 2 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar6}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Kenneth
																		Brown
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Mentionned
																		you in
																		his
																		comment
																		on 📃
																		invoice
																		#12501.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 10 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar8}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Maureen
																		Gibson
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 3 days
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="my-3 text-center"
													>
														<Button
															color="success"
															class="btn btn-soft-success"
															>View All Messages <i
																class="ri-arrow-right-line align-middle"
															/></Button
														>
													</div>
												</div>
											</TabPane>

											<TabPane
												tabId={1}
												class={NotificationTab == 3
													? "active p-4"
													: "p-4"}
												id="alerts-tab2"
											>
												<div class="w-50 pt-3 mx-auto">
													<img
														src={bell}
														class="img-fluid"
														alt="user-pic"
													/>
												</div>
												<div
													class="text-center pb-5 mt-2"
												>
													<h6
														class="fs-18 fw-semibold lh-base"
													>
														Hey! You have no any
														notifications
													</h6>
												</div>
											</TabPane>
										</TabContent>
									</div>
								</Col>

								<Col xxl={3} lg={5} md={6}>
									<div
										class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0 d-inline-block position-relative w-100"
										aria-labelledby="page-header-notifications-dropdown"
										style="z-index: 1"
									>
										<div
											class="dropdown-head bg-secondary bg-pattern rounded-top overflow-hidden"
										>
											<div class="p-3">
												<Row class="align-items-center">
													<Col>
														<h6
															class="m-0 fs-16 fw-semibold text-white"
														>
															Notifications
														</h6>
													</Col>
													<div
														class="col-auto dropdown-tabs"
													>
														<span
															class="badge bg-light-subtle text-body fs-13"
														>
															4 New</span
														>
													</div>
												</Row>
											</div>

											<div class="px-2 pt-2">
												<Nav
													tabs
													class="dropdown-tabs nav-tabs-custom"
												>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															on:click={() =>
																(Notification1Tab = 1)}
															active={Notification1Tab ==
																1}
														>
															All (4)
														</NavLink>
													</NavItem>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															on:click={() =>
																(Notification1Tab = 2)}
															active={Notification1Tab ==
																2}
														>
															Messages
														</NavLink>
													</NavItem>
													<NavItem>
														<NavLink
															style="cursor: pointer"
															on:click={() =>
																(Notification1Tab = 3)}
															active={Notification1Tab ==
																3}
														>
															Alerts
														</NavLink>
													</NavItem>
												</Nav>
											</div>
										</div>

										<TabContent
											id="notificationItemsTabContent3"
										>
											<TabPane
												tabId={1}
												class={Notification1Tab == 1
													? "active py-2 ps-2"
													: "py-2 ps-2"}
												id="all-noti-tab1"
											>
												<div
													data-simplebar
													style="max-height: 300px"
													class="pe-2"
												>
													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<div
																class="flex-shrink-0 avatar-xs me-3"
															>
																<span
																	class="avatar-title bg-info-subtle text-info rounded-circle fs-16"
																>
																	<i
																		class="bx bx-badge-check"
																	/>
																</span>
															</div>
															<div class="flex-1">
																<h6
																	class="mt-0 mb-2 lh-base"
																>
																	Your <b
																		>Elite</b
																	>
																	author Graphic
																	Optimization
																	<span
																		class="text-secondary"
																		>reward</span
																	> is ready!
																</h6>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> Just 30
																		sec ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar2}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Angela
																		Bernier
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Answered
																		to your
																		comment
																		on the
																		cash
																		flow
																		forecast's
																		graph
																		🔔.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 48 min
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<div
																class="flex-shrink-0 avatar-xs me-3"
															>
																<span
																	class="avatar-title bg-danger-subtle text-danger rounded-circle fs-16"
																>
																	<i
																		class="bx bx-message-square-dots"
																	/>
																</span>
															</div>
															<div class="flex-1">
																<h6
																	class="mt-0 mb-2 fs-13 lh-base"
																>
																	You have
																	received <b
																		class="text-success"
																		>20</b
																	> new messages
																	in the conversation
																</h6>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 2 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar8}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Maureen
																		Gibson
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 4 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="my-3 text-center"
													>
														<Button
															color="success"
															class="btn btn-soft-success"
															>View All
															Notifications <i
																class="ri-arrow-right-line align-middle"
															/></Button
														>
													</div>
												</div>
											</TabPane>

											<TabPane
												tabId={1}
												class={Notification1Tab == 2
													? "active py-2 ps-2"
													: "py-2 ps-2"}
												id="messages-tab3"
											>
												<div
													data-simplebar
													style="max-height: 300px"
													class="pe-2"
												>
													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar3}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		James
																		Lemire
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 30 min
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar2}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Angela
																		Bernier
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Answered
																		to your
																		comment
																		on the
																		cash
																		flow
																		forecast's
																		graph
																		🔔.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 2 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar6}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Kenneth
																		Brown
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		Mentionned
																		you in
																		his
																		comment
																		on 📃
																		invoice
																		#12501.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 10 hrs
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="text-reset notification-item d-block dropdown-item"
													>
														<div class="d-flex">
															<img
																src={avatar8}
																class="me-3 rounded-circle avatar-xs"
																alt="user-pic"
															/>
															<div class="flex-1">
																<Link href={null}
																	><h6
																		class="mt-0 mb-1 fs-13 fw-semibold"
																	>
																		Maureen
																		Gibson
																	</h6></Link
																>
																<div
																	class="fs-13 text-muted"
																>
																	<p
																		class="mb-1"
																	>
																		We
																		talked
																		about a
																		project
																		on
																		linkedin.
																	</p>
																</div>
																<p
																	class="mb-0 fs-11 fw-medium text-uppercase text-muted"
																>
																	<span
																		><i
																			class="mdi mdi-clock-outline"
																		/> 3 days
																		ago</span
																	>
																</p>
															</div>
															<div
																class="px-2 fs-16"
															>
																<input
																	class="form-check-input"
																	type="checkbox"
																/>
															</div>
														</div>
													</div>

													<div
														class="my-3 text-center"
													>
														<Button
															color="success"
															class="btn btn-soft-success"
															>View All Messages <i
																class="ri-arrow-right-line align-middle"
															/></Button
														>
													</div>
												</div>
											</TabPane>

											<TabPane
												tabId={1}
												class={Notification1Tab == 3
													? "active p-4"
													: "p-4"}
												id="alerts-tab3"
											>
												<div class="w-50 pt-3 mx-auto">
													<img
														src={bell}
														class="img-fluid"
														alt="user-pic"
													/>
												</div>
												<div
													class="text-center pb-5 mt-2"
												>
													<h6
														class="fs-18 fw-semibold lh-base"
													>
														Hey! You have no any
														notifications
													</h6>
												</div>
											</TabPane>
										</TabContent>
									</div>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={notificationDropdownCode}
								id="notificationDropdownCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
