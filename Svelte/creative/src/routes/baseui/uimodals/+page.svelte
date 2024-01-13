<script>
	import {
		Button,
		Card,
		CardBody,
		Col,
		Container,
		Input,
		// Modal,
		ModalBody,
		ModalHeader,
		Row,
		Popover,
		Tooltip,
		Label,
		Alert
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";
	import Modal from "../../../Components/Common/Modal.svelte";

	// Import Images
	import loginImg from "../../../assets/images/modals/login.png";
	import signupImg from "../../../assets/images/modals/signup.png";
	import subscribeImg from "../../../assets/images/modals/subscribe.png";
	import paymentImg from "../../../assets/images/modals/success-payment.png";
	import authbg from "../../../assets/images/auth-one-bg.jpg";

	let modal_standard = false;
	const tog_standard = () => (modal_standard = !modal_standard);

	let modal_center = false;
	const tog_center = () => (modal_center = !modal_center);

	let modal_grid = false;
	const tog_grid = () => (modal_grid = !modal_grid);

	let modal_tooltip = false;
	const tog_tooltip = () => (modal_tooltip = !modal_tooltip);

	let modal_fullscreen = false;
	const tog_fullscreen = () => (modal_fullscreen = !modal_fullscreen);

	let modal_xlarge = false;
	const tog_xlarge = () => (modal_xlarge = !modal_xlarge);

	let modal_large = false;
	const tog_large = () => (modal_large = !modal_large);

	let modal_small = false;
	const tog_small = () => (modal_small = !modal_small);

	let modal_fullscreen1 = false;
	const tog_fullscreen1 = () => (modal_fullscreen1 = !modal_fullscreen1);

	let modal_fullscreen_sm = false;
	const tog_fullscreen_sm = () =>
		(modal_fullscreen_sm = !modal_fullscreen_sm);

	let modal_fullscreen_md = false;
	const tog_fullscreen_md = () =>
		(modal_fullscreen_md = !modal_fullscreen_md);

	let modal_fullscreen_lg = false;
	const tog_fullscreen_lg = () =>
		(modal_fullscreen_lg = !modal_fullscreen_lg);

	let modal_fullscreen_xl = false;
	const tog_fullscreen_xl = () =>
		(modal_fullscreen_xl = !modal_fullscreen_xl);

	let modal_fullscreen_xxl = false;
	const tog_fullscreen_xxl = () =>
		(modal_fullscreen_xxl = !modal_fullscreen_xxl);

	let modal_scroll = false;
	const tog_scroll = () => (modal_scroll = !modal_scroll);

	let modal_backdrop = false;
	const tog_backdrop = () => (modal_backdrop = !modal_backdrop);

	let modal_varying1 = false;
	const tog_varying1 = () => (modal_varying1 = !modal_varying1);

	let modal_varying2 = false;
	const tog_varying2 = () => (modal_varying2 = !modal_varying2);

	let modal_varying3 = false;
	const tog_varying3 = () => (modal_varying3 = !modal_varying3);

	let modal_togFirst = false;
	const tog_togFirst = () => (modal_togFirst = !modal_togFirst);

	let modal_togSecond = false;
	const tog_togSecond = () => (modal_togSecond = !modal_togSecond);

	let modal_animationRight = false;
	const tog_animationRight = () =>
		(modal_animationRight = !modal_animationRight);

	let modal_animationLeft = false;
	const tog_animationLeft = () =>
		(modal_animationLeft = !modal_animationLeft);

	let modal_animationUp = false;
	const tog_animationUp = () => (modal_animationUp = !modal_animationUp);

	let modal_animationFlip = false;
	const tog_animationFlip = () =>
		(modal_animationFlip = !modal_animationFlip);

	let modal_animationZoom = false;
	const tog_animationZoom = () =>
		(modal_animationZoom = !modal_animationZoom);

	let modal_positionTop = false;
	const tog_positionTop = () => (modal_positionTop = !modal_positionTop);

	let modal_positionTopRight = false;
	const tog_positionTopRight = () =>
		(modal_positionTopRight = !modal_positionTopRight);

	let modal_positionBottom = false;
	const tog_positionBottom = () =>
		(modal_positionBottom = !modal_positionBottom);

	let modal_positionBottomRight = false;
	const tog_positionBottomRight = () =>
		(modal_positionBottomRight = !modal_positionBottomRight);
	
	let modal_loginModals = false;
	const tog_loginModals = () => (modal_loginModals = !modal_loginModals);

	let subscribeModals = false;
	const tog_subscribeModals = () => (subscribeModals = !subscribeModals);
	
	let modal_signUpModals = false;
	const tog_signUpModals = () => (modal_signUpModals = !modal_signUpModals);	

	let modal_successMessage = false;
	const tog_successMessage = () => (modal_successMessage = !modal_successMessage);	
	
	const defaultModalCode = `
<!-- Default Modals -->
let modal_standard = false;
	const tog_standard = () => (modal_standard = !modal_standard);
	<Modal
	id="myModal"
	isOpen={modal_standard}
	toggle={() => {
		tog_standard();
	}}
>
	<ModalHeader
		class="modal-title"
		id="myModalLabel"
		toggle={() => {
			tog_standard();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody>
		<h5 class="fs-15">Overflowing text to show scroll behavior</h5>
		<p class="text-muted">
			One morning, when Gregor Samsa woke from troubled dreams, he found
			himself transformed in his bed into a horrible vermin. He lay on his
			armour-like back, and if he lifted his head a little he could see
			his brown belly, slightly domed and divided by arches into stiff
			sections.
		</p>
		<p class="text-muted">
			The bedding was hardly able to cover it and seemed ready to slide
			off any moment. His many legs, pitifully thin compared with the size
			of the rest of him, waved about helplessly as he looked. "What's
			happened to me?" he thought.
		</p>
		<p class="text-muted">
			It wasn't a dream. His room, a proper human room although a little
			too small, lay peacefully between its four familiar walls.
		</p>
	</ModalBody>
	<div class="modal-footer">
		<Button
			color="light"
			on:click={() => {
				tog_standard();
			}}
		>
			Close
		</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>
	<Button color="primary" on:click={tog_standard}>Standard Modal</Button>
`;

	// Vertically Centered Modal
	const centeredModalCode = `
<!-- Vertically Centered -->
let modal_center = false;
	const tog_center = () => (modal_center = !modal_center);
	<Modal
	isOpen={modal_center}
	toggle={() => {
		tog_center();
	}}
	centered
>
	<ModalHeader class="modal-title" />

	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/hrqwmuhr.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width:120px;height:120px"
		/>
		<div class="mt-4">
			<h3 class="mb-3">Oops something went wrong!</h3>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Button color="light" on:click={tog_center}>Close</Button>
				<Link href={null} class="btn btn-danger">Try Again</Link>
			</div>
		</div>
	</ModalBody>
</Modal>
<Button color="primary" on:click={tog_center}>Center Modal</Button>
`;

	// Grids in Modals
	const gridsModalCode = `
<!-- Grids in modals -->
let modal_grid = false;
const tog_grid = () => (modal_grid = !modal_grid);
<Modal
	isOpen={modal_grid}
	toggle={() => {
		tog_grid();
	}}
>
	<ModalHeader
		class="modal-title fw-bold"
		toggle={() => {
			tog_grid();
		}}
	>
		Grid Modals
	</ModalHeader>
	<ModalBody>
		<form action="#">
			<div class="row g-3">
				<Col xxl={6}>
					<div>
						<Label for="firstName" class="form-label">First Name</Label
						>
						<Input
							type="text"
							class="form-control"
							id="firstName"
							placeholder="Enter firstname"
						/>
					</div>
				</Col>
				<Col xxl={6}>
					<div>
						<Label for="lastName" class="form-label">Last Name</Label
						>
						<Input
							type="text"
							class="form-control"
							id="lastName"
							placeholder="Enter lastname"
						/>
					</div>
				</Col>
				<Col lg={12}>
					<Label class="form-label">Gender</Label>
					<div>
						<div class="form-check form-check-inline">
							<input
								class="form-check-input"
								type="radio"
								name="inlineRadioOptions"
								id="inlineRadio1"
								value="option1"
							/>
							<Label class="form-check-label" for="inlineRadio1"
								>Male</Label>
						</div>
						<div class="form-check form-check-inline">
							<input
								class="form-check-input"
								type="radio"
								name="inlineRadioOptions"
								id="inlineRadio2"
								value="option2"
							/>
							<Label class="form-check-label" for="inlineRadio2"
								>Female</Label>
						</div>
						<div class="form-check form-check-inline">
							<input
								class="form-check-input"
								type="radio"
								name="inlineRadioOptions"
								id="inlineRadio3"
								value="option3"
							/>
							<Label class="form-check-label" for="inlineRadio3"
								>Others</Label>
						</div>
					</div>
				</Col>
				<Col xxl={6}>
					<Label for="emailInput" class="form-label">Email</Label>
					<Input
						type="email"
						class="form-control"
						id="emailInput"
						placeholder="Enter your email"
					/>
				</Col>
				<Col xxl={6}>
					<Label for="passwordInput" class="form-label"
						>Password</Label>
					<Input
						type="password"
						class="form-control"
						id="passwordInput"
						value="451326546"
						readOnly
					/>
				</Col>
				<Col lg={12}>
					<div class="hstack gap-2 justify-content-end">
						<Button color="light" on:click={tog_grid}>Close</Button>
						<Button color="primary">Submit</Button>
					</div>
				</Col>
			</div>
		</form>
	</ModalBody>
</Modal>
<Button color="primary" on:click={tog_grid}>Launch Demo Modal</Button>
`;

	// Static Backdrop Modal
	const staticBackdropModalCode = `
<!-- Static Backdrop -->
<Modal
	isOpen={modal_backdrop}
	toggle={() => {
		tog_backdrop();
	}}
	backdrop={"static"}
	id="staticBackdrop"
	centered
>
	<ModalHeader
		class="modal-title"
		id="staticBackdropLabel"
		toggle={() => {
			tog_backdrop();
		}}
	>
		Modal title
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/lupuorrc.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>

		<div class="mt-4">
			<h3 class="mb-3">You've made it!</h3>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-secondary fw-medium"
					on:click={tog_backdrop}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success" on:click={tog_backdrop}>Completed</Link
				>
			</div>
		</div>
	</ModalBody>
</Modal>
<Button color="primary" on:click={tog_backdrop}>Static Backdrop Modal</Button>

`;

	// Toggle Between Modal
	const togglebetweenCode = `
<!-- Default List -->
let modal_togFirst = false;
	const tog_togFirst = () => (modal_togFirst = !modal_togFirst);
	<Modal
	isOpen={modal_togFirst}
	toggle={() => {
		tog_togFirst();
	}}
	id="firstmodal"
	centered
>
	<ModalHeader
		class="modal-title"
		id="exampleModalToggleLabel"
		toggle={() => {
			tog_togFirst();
		}}
	>
		Modal 1
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/tdrtiskw.json"
			trigger="loop"
			colors="primary:#f7b84b,secondary:#405189"
			style="width: 130px; height: 130px"
		/>
		<div class="mt-4 pt-4">
			<h3>Uh oh, something went wrong!</h3>
			<p class="text-muted">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>

			<Button
				color="warning"
				on:click={() => {
					tog_togSecond();
					tog_togFirst(false);
				}}
			>
				Continue
			</Button>
		</div>
	</ModalBody>
</Modal>
<Button color="primary" on:click={tog_togFirst}>Open First Modal</Button>
`;

	// Tooltips and Popovers
	const tooltipModalCode = `
<!-- Tooltips and Popovers -->
let modal_tooltip = false;
	const tog_tooltip = () => (modal_tooltip = !modal_tooltip);
<Modal
	isOpen={modal_togSecond}
	toggle={() => {
		tog_togSecond();
	}}
	id="secondmodal"
	centered
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalToggleLabel2"
		toggle={() => {
			tog_togSecond();
		}}
	>
		Modal 2
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<h5 class="fs-17">Popover in a Modal</h5>
		<p class="text-muted">
			You only need to know a little to make a big
			{" "}<Link
				href={null}
				class="popover-test fw-medium text-decoration-underline link-success"
				id="Popover"
			>
				Popover on Click
			</Link>{" "}
			you do every day. So let's get started. First, some common types of fonts
			and what you need to know about them triggers a popover on click.
		</p>
		<Popover
			placement="bottom"
			target="Popover"
			title="Common Types of Fonts"
		>
			They're a good choice for more traditional projects.
		</Popover>

		<h5 class="fs-17">Tooltips in a Modal</h5>
		<p class="text-muted">
			Opposites attract, and that’s a fact. It’s in our
			{" "}<Link
				href={null}
				class="tooltip-test text-decoration-underline fw-medium"
				id="Tooltip1"
			>
				graphic design
			</Link>{" "} to be interested in the unusual, and that’s why using
			{" "}<Link
				href={null}
				class="tooltip-test text-decoration-underline"
				id="Tooltip2">design</Link
			>
			contrasting colors in Graphic Design is a must.
		</p>
		<Tooltip placement="top" target="Tooltip1">Morton Bayer</Tooltip>
		<Tooltip placement="top" target="Tooltip2">Web Developers</Tooltip>
	</ModalBody>
</Modal>
<Button color="primary" on:click={tog_tooltip}>Launch Demo Modal</Button>
`;

	// Scrollable Modal
	const scrollableModalCode = `
<!-- Scrollable Modal -->
let modal_scroll = false;
	const tog_scroll = () => (modal_scroll = !modal_scroll);
	<Modal
	isOpen={modal_scroll}
	toggle={() => {
		tog_scroll();
	}}
	scrollable={true}
	id="exampleModalScrollable"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalScrollableTitle"
		toggle={() => {
			tog_scroll();
		}}
	>
		Scrollable modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					You've probably heard that opposites attract. The same is
					true for fonts. Don't be afraid to combine font styles that
					are different but complementary, like sans serif with serif,
					short with tall, or decorative with simple. Qui photo booth
					letterpress, commodo enim craft beer mlkshk aliquip jean
					shorts ullamco ad vinyl cillum PBR.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-17 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Just like in the image where we talked about using multiple
					fonts, you can see that the background in this graphic
					design is blurred. Whenever you put text on top of an image,
					it’s important that your viewers can understand.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Keytar raw denim keffiyeh etsy art party before they sold
					out master cleanse gluten-free squid scenester freegan cosby
					sweater.
				</p>
			</div>
		</div>
	</ModalBody>

	<div class="modal-footer">
		<Button color="light" on:click={tog_scroll}>Close</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>
<Button color="primary" on:click={tog_scroll}>Scrollable Modal</Button>
`;

	// Varying Modal Content
	const varyingModalCode = `
<!-- Varying Modal Content -->
let modal_varying1 = false;
const tog_varying1 = () => (modal_varying1 = !modal_varying1);

let modal_varying2 = false;
const tog_varying2 = () => (modal_varying2 = !modal_varying2);

let modal_varying3 = false;
const tog_varying3 = () => (modal_varying3 = !modal_varying3);

<Button
	color="primary"
	on:click={tog_varying1}
	>Open Modal for Mary</Button
>
<Button
	color="primary"
	on:click={tog_varying2}
	>Open Modal for Jennifer</Button
>
<Button
	color="primary"
	on:click={tog_varying3}
	>Open Modal for Roderick</Button
>
`;

	// Optional Sizes
	const optionalModalCode = `
<!-- Optional Modal Sizes -->
let modal_fullscreen = false;
const tog_fullscreen = () => (modal_fullscreen = !modal_fullscreen);

let modal_xlarge = false;
const tog_xlarge = () => (modal_xlarge = !modal_xlarge);

let modal_large = false;
const tog_large = () => (modal_large = !modal_large);

let modal_small = false;
const tog_small = () => (modal_small = !modal_small);

<Modal
	size="xl"
	isOpen={modal_fullscreen}
	toggle={() => {
		tog_fullscreen();
	}}
	class="modal-fullscreen"
	id="exampleModalFullscreen"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalFullscreenLabel"
		toggle={() => {
			tog_fullscreen();
		}}
	>
		Fullscreen Modal Heading
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					You've probably heard that opposites attract. The same is
					true for fonts. Don't be afraid to combine font styles that
					are different but complementary, like sans serif with serif,
					short with tall, or decorative with simple. Qui photo booth
					letterpress, commodo enim craft beer mlkshk aliquip jean
					shorts ullamco ad vinyl cillum PBR.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-16 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Just like in the image where we talked about using multiple
					fonts, you can see that the background in this graphic
					design is blurred. Whenever you put text on top of an image,
					it’s important that your viewers can understand.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Keytar raw denim keffiyeh etsy art party before they sold
					out master cleanse gluten-free squid scenester freegan cosby
					sweater.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			color="light"
			on:click={() => {
				tog_fullscreen();
			}}
			class="btn btn-link link-success fw-medium"
			><i class="ri-close-line me-1 align-middle" />
			Close
		</Link>
		<Button color="primary" class="btn btn-primary ">Save changes</Button>
	</div>
</Modal>

<Modal
	size="xl"
	isOpen={modal_xlarge}
	toggle={() => {
		tog_xlarge();
	}}
>
	<ModalHeader
		class="modal-title"
		id="myExtraLargeModalLabel"
		toggle={() => {
			tog_xlarge();
		}}
	>
		Extra large modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					You've probably heard that opposites attract. The same is
					true for fonts. Don't be afraid to combine font styles that
					are different but complementary, like sans serif with serif,
					short with tall, or decorative with simple. Qui photo booth
					letterpress, commodo enim craft beer mlkshk aliquip jean
					shorts ullamco ad vinyl cillum PBR.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-16 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Just like in the image where we talked about using multiple
					fonts, you can see that the background in this graphic
					design is blurred. Whenever you put text on top of an image,
					it’s important that your viewers can understand.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Keytar raw denim keffiyeh etsy art party before they sold
					out master cleanse gluten-free squid scenester freegan cosby
					sweater.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={tog_xlarge}
			><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	size="lg"
	isOpen={modal_large}
	toggle={() => {
		tog_large();
	}}
>
	<ModalHeader
		class="modal-title"
		id="myLargeModalLabel"
		toggle={() => {
			tog_large();
		}}
	>
		Large Modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					You've probably heard that opposites attract. The same is
					true for fonts. Don't be afraid to combine font styles that
					are different but complementary, like sans serif with serif,
					short with tall, or decorative with simple. Qui photo booth
					letterpress, commodo enim craft beer mlkshk aliquip jean
					shorts ullamco ad vinyl cillum PBR.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-16 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Just like in the image where we talked about using multiple
					fonts, you can see that the background in this graphic
					design is blurred. Whenever you put text on top of an image,
					it’s important that your viewers can understand.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Keytar raw denim keffiyeh etsy art party before they sold
					out master cleanse gluten-free squid scenester freegan cosby
					sweater.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={tog_large}
			><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	size="sm"
	isOpen={modal_small}
	toggle={() => {
		tog_small();
	}}
>
	<ModalHeader
		class="modal-title"
		id="mySmallModalLabel"
		toggle={() => {
			tog_small();
		}}
	>
		Small Modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={tog_small}
			><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Button
	color="primary"
	on:click={tog_fullscreen}
	>Fullscreen Modal</Button
>

<Button color="info" on:click={tog_xlarge}
	>Extra large Modal</Button
>

<Button color="success" on:click={tog_large}
	>Large Modal</Button
>

<Button color="danger" on:click={tog_small}
	>Small Modal</Button
>
`;

	// Fullscreen Responsive Modals
	const fullscreenResponsiveCode = `
<!-- Fullscreen Modals -->
let modal_fullscreen1 = false;
const tog_fullscreen1 = () => (modal_fullscreen1 = !modal_fullscreen1);

let modal_fullscreen_sm = false;
const tog_fullscreen_sm = () =>
	(modal_fullscreen_sm = !modal_fullscreen_sm);

let modal_fullscreen_md = false;
const tog_fullscreen_md = () =>
	(modal_fullscreen_md = !modal_fullscreen_md);

let modal_fullscreen_lg = false;
const tog_fullscreen_lg = () =>
	(modal_fullscreen_lg = !modal_fullscreen_lg);

let modal_fullscreen_xl = false;
const tog_fullscreen_xl = () =>
	(modal_fullscreen_xl = !modal_fullscreen_xl);

let modal_fullscreen_xxl = false;
const tog_fullscreen_xxl = () =>
	(modal_fullscreen_xxl = !modal_fullscreen_xxl);

	<Modal
	size="xl"
	isOpen={modal_fullscreen1}
	toggle={() => {
		tog_fullscreen1();
	}}
	class="modal-fullscreen"
	id="fullscreeexampleModal"
>
	<ModalHeader
		class="modal-title"
		id="fullscreeexampleModalLabel"
		toggle={() => {
			tog_fullscreen1();
		}}
	>
		Full screen modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-16 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			type="button"
			on:click={() => {
				tog_fullscreen1();
			}}
			class="btn btn-link link-success fw-medium"
			><i class="ri-close-line me-1 align-middle" />
			Close
		</Link>
		<Button color="primary" class="btn btn-primary ">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenSm"
	isOpen={modal_fullscreen_sm}
	toggle={() => {
		tog_fullscreen_sm();
	}}
>
	<ModalHeader
		class="modal-title"
		id="exampleModalFullscreenSmLabel"
		toggle={() => {
			tog_fullscreen_sm();
		}}
	>
		Full screen below sm
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_sm();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenMd"
	isOpen={modal_fullscreen_md}
	toggle={() => {
		tog_fullscreen_md();
	}}
>
	<ModalHeader
		class="modal-title"
		id="exampleModalFullscreenMdLabel"
		toggle={() => {
			tog_fullscreen_md();
		}}
	>
		Full screen below md
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_md();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenLg"
	isOpen={modal_fullscreen_lg}
	toggle={() => {
		tog_fullscreen_lg();
	}}
>
	<ModalHeader
		class="modal-title"
		id="exampleModalFullscreenLgLabel"
		toggle={() => {
			tog_fullscreen_lg();
		}}
	>
		Full screen below lg
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_lg();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenXl"
	isOpen={modal_fullscreen_xl}
	toggle={() => {
		tog_fullscreen_xl();
	}}
>
	<ModalHeader
		class="modal-title"
		id="exampleModalFullscreenXlLabel"
		toggle={() => {
			tog_fullscreen_xl();
		}}
	>
		Full screen below xl
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_xl();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenXxl"
	isOpen={modal_fullscreen_xxl}
	toggle={() => {
		tog_fullscreen_xxl();
	}}
>
	<ModalHeader
		class="modal-title"
		id="exampleModalFullscreenXxlLabel"
		toggle={() => {
			tog_fullscreen_xxl();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_xxl();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Button
	color="primary"
	on:click={tog_fullscreen1}
	>Fullscreen modal</Button
>
<Button
	color="primary"
	on:click={tog_fullscreen_sm}
	>Full Screen Below sm</Button
>
<Button
	color="primary"
	on:click={tog_fullscreen_md}
	>Full Screen Below md</Button
>
<Button
	color="primary"
	on:click={tog_fullscreen_lg}
	>Full Screen Below lg</Button
>
<Button
	color="primary"
	on:click={tog_fullscreen_xl}
	>Full Screen Below xl</Button
>
<Button
	color="primary"
	on:click={tog_fullscreen_xxl}
	>Full Screen Below xxl</Button
>
`;

	// Animation Modals
	const animationModalCode = `
<!-- Animation Modals -->
let modal_animationRight = false;
const tog_animationRight = () =>
	(modal_animationRight = !modal_animationRight);

let modal_animationLeft = false;
const tog_animationLeft = () =>
	(modal_animationLeft = !modal_animationLeft);

let modal_animationUp = false;
const tog_animationUp = () => (modal_animationUp = !modal_animationUp);

let modal_animationFlip = false;
const tog_animationFlip = () =>
	(modal_animationFlip = !modal_animationFlip);

let modal_animationZoom = false;
const tog_animationZoom = () =>
	(modal_animationZoom = !modal_animationZoom);

	<Modal
	id="fadeInRightModal"
	isOpen={modal_animationRight}
	toggle={() => {
		tog_animationRight();
	}}
	modalClass="fadeInRight"
	centered
>
	<ModalHeader
		class="modal-title"
		id="fadeInRightModalLabel"
		toggle={() => {
			tog_animationRight();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody>
		<h5 class="fs-16">Overflowing text to show scroll behavior</h5>
		<p class="text-muted">
			One morning, when Gregor Samsa woke from troubled dreams, he found
			himself transformed in his bed into a horrible vermin. He lay on his
			armour-like back, and if he lifted his head a little he could see
			his brown belly, slightly domed and divided by arches into stiff
			sections.
		</p>
		<p class="text-muted">
			The bedding was hardly able to cover it and seemed ready to slide
			off any moment. His many legs, pitifully thin compared with the size
			of the rest of him, waved about helplessly as he looked. "What's
			happened to me?" he thought.
		</p>
	</ModalBody>
	<div class="modal-footer">
		<Button
			color="light"
			on:click={() => {
				tog_animationRight();
			}}
		>
			Close
		</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="fadeInleftModal"
	isOpen={modal_animationLeft}
	toggle={() => {
		tog_animationLeft();
	}}
	modalClass="fadeInLeft"
	centered
>
	<ModalHeader
		class="modal-title"
		id="fadeInleftModalLabel"
		toggle={() => {
			tog_animationLeft();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody>
		<h5 class="fs-16">Overflowing text to show scroll behavior</h5>
		<p class="text-muted">
			One morning, when Gregor Samsa woke from troubled dreams, he found
			himself transformed in his bed into a horrible vermin. He lay on his
			armour-like back, and if he lifted his head a little he could see
			his brown belly, slightly domed and divided by arches into stiff
			sections.
		</p>
		<p class="text-muted">
			The bedding was hardly able to cover it and seemed ready to slide
			off any moment. His many legs, pitifully thin compared with the size
			of the rest of him, waved about helplessly as he looked. "What's
			happened to me?" he thought.
		</p>
	</ModalBody>
	<div class="modal-footer">
		<Button
			color="light"
			on:click={() => {
				tog_animationLeft();
			}}
		>
			Close
		</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="fadeInUpModal"
	isOpen={modal_animationUp}
	toggle={() => {
		tog_animationUp();
	}}
	modalClass="fadeInUp"
	centered
>
	<ModalHeader
		class="modal-title"
		id="fadeInUpModalLabel"
		toggle={() => {
			tog_animationUp();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody>
		<h5 class="fs-16">Overflowing text to show scroll behavior</h5>
		<p class="text-muted">
			One morning, when Gregor Samsa woke from troubled dreams, he found
			himself transformed in his bed into a horrible vermin. He lay on his
			armour-like back, and if he lifted his head a little he could see
			his brown belly, slightly domed and divided by arches into stiff
			sections.
		</p>
		<p class="text-muted">
			The bedding was hardly able to cover it and seemed ready to slide
			off any moment. His many legs, pitifully thin compared with the size
			of the rest of him, waved about helplessly as he looked. "What's
			happened to me?" he thought.
		</p>
	</ModalBody>
	<div class="modal-footer">
		<Button
			color="light"
			on:click={() => {
				tog_animationUp();
			}}
		>
			Close
		</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="flipModal"
	isOpen={modal_animationFlip}
	toggle={() => {
		tog_animationFlip();
	}}
	modalClass="flip"
	centered
>
	<ModalHeader
		class="modal-title"
		id="flipModalLabel"
		toggle={() => {
			tog_animationFlip();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody>
		<h5 class="fs-16">Overflowing text to show scroll behavior</h5>
		<p class="text-muted">
			One morning, when Gregor Samsa woke from troubled dreams, he found
			himself transformed in his bed into a horrible vermin. He lay on his
			armour-like back, and if he lifted his head a little he could see
			his brown belly, slightly domed and divided by arches into stiff
			sections.
		</p>
		<p class="text-muted">
			The bedding was hardly able to cover it and seemed ready to slide
			off any moment. His many legs, pitifully thin compared with the size
			of the rest of him, waved about helplessly as he looked. "What's
			happened to me?" he thought.
		</p>
	</ModalBody>
	<div class="modal-footer">
		<Button
			color="light"
			on:click={() => {
				tog_animationFlip();
			}}
		>
			Close
		</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="flipModal"
	isOpen={modal_animationZoom}
	toggle={() => {
		tog_animationZoom();
	}}
	modalClass="zoomIn"
	centered
>
	<ModalHeader
		class="modal-title"
		id="flipModalLabel"
		toggle={() => {
			tog_animationZoom();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody>
		<h5 class="fs-16">Overflowing text to show scroll behavior</h5>
		<p class="text-muted">
			One morning, when Gregor Samsa woke from troubled dreams, he found
			himself transformed in his bed into a horrible vermin. He lay on his
			armour-like back, and if he lifted his head a little he could see
			his brown belly, slightly domed and divided by arches into stiff
			sections.
		</p>
		<p class="text-muted">
			The bedding was hardly able to cover it and seemed ready to slide
			off any moment. His many legs, pitifully thin compared with the size
			of the rest of him, waved about helplessly as he looked. "What's
			happened to me?" he thought.
		</p>
	</ModalBody>
	<div class="modal-footer">
		<Button
			color="light"
			on:click={() => {
				tog_animationZoom();
			}}
		>
			Close
		</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Button
	color="primary"
	on:click={tog_animationRight}
	>Fade In Right Modal</Button
>
<Button
	color="primary"
	on:click={tog_animationLeft}
	>Fade In Left Modal</Button
>
<Button
	color="primary"
	on:click={tog_animationUp}
	>Fade In Up Modal</Button
>
<Button
	color="primary"
	on:click={tog_animationFlip}
	>Flip Modal</Button
>
<Button
	color="primary"
	on:click={tog_animationZoom}
	>Zoom In Modal</Button
>
`;

	// Modal Positions
	const positionModalCode = `
<!-- Positions Modals -->
let modal_positionTop = false;
const tog_positionTop = () => (modal_positionTop = !modal_positionTop);

let modal_positionTopRight = false;
const tog_positionTopRight = () =>
	(modal_positionTopRight = !modal_positionTopRight);

let modal_positionBottom = false;
const tog_positionBottom = () =>
	(modal_positionBottom = !modal_positionBottom);

let modal_positionBottomRight = false;
const tog_positionBottomRight = () =>
	(modal_positionBottomRight = !modal_positionBottomRight);

	<Modal
	id="topmodal"
	isOpen={modal_positionTop}
	toggle={() => {
		tog_positionTop();
	}}
>
	<ModalHeader
		class="modal-title"
		id="myModalLabel"
		toggle={() => {
			tog_positionTop();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/pithnlch.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>
		<div class="mt-4">
			<h4 class="mb-3">Your event has been created.</h4>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-success fw-medium"
					on:click={() => {
						tog_positionTop();
					}}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success">Completed</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	id="top-rightmodal"
	isOpen={modal_positionTopRight}
	toggle={() => {
		tog_positionTopRight();
	}}
	class="modal-dialog-right"
>
	<ModalHeader
		class="modal-title"
		id="myModalLabel"
		toggle={() => {
			tog_positionTopRight();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/pithnlch.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>
		<div class="mt-4">
			<h4 class="mb-3">Your event has been created.</h4>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-success fw-medium"
					on:click={() => {
						tog_positionTopRight();
					}}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success">Completed</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	id="bottomModal"
	isOpen={modal_positionBottom}
	toggle={() => {
		tog_positionBottom();
	}}
	class="modal-dialog-bottom"
>
	<ModalHeader
		class="modal-title"
		id="myModalLabel"
		toggle={() => {
			tog_positionBottom();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/pithnlch.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>
		<div class="mt-4">
			<h4 class="mb-3">Your event has been created.</h4>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-success fw-medium"
					on:click={tog_positionBottom}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success">Completed</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	id="bottom-rightModal"
	isOpen={modal_positionBottomRight}
	toggle={() => {
		tog_positionBottomRight();
	}}
	class="modal-dialog-bottom-right"
>
	<ModalHeader
		class="modal-title"
		id="myModalLabel"
		toggle={() => {
			tog_positionBottomRight();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/pithnlch.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>
		<div class="mt-4">
			<h4 class="mb-3">Your event has been created.</h4>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-success fw-medium"
					on:click={tog_positionBottomRight}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success">Completed</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Button
	color="primary"
	on:click={tog_positionTop}
	>Top Modal</Button
>
<Button
	color="secondary"
	on:click={tog_positionTopRight}
	>Top Right Modal</Button
>
<Button
	color="success"
	on:click={tog_positionBottom}
	>Bottom Modal</Button
>
<Button
	color="danger"
	on:click={tog_positionBottomRight}
	>Bottom Right Modal</Button
>
`;
</script>

<svelte:head>
	<title>Modals | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	 <Container fluid>
		<BreadCrumb title="Modals" pageTitle="Base UI" />
		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Default Modal" />

					<CardBody>
						<p class="text-muted text-muted">
							A default modal Example.
						</p>
						<div class="live-preview">
							<div>
								<Button color="primary" on:click={tog_standard}
									>Standard Modal</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={defaultModalCode}
								id="defaultModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Vertically Centered Modal" />

					<CardBody>
						<p class="text-muted">
							Use <code>modal-dialog-centered</code> class to show
							vertically center the modal.
						</p>
						<div class="live-preview">
							<div>
								<Button color="primary" on:click={tog_center}
									>Center Modal</Button
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={centeredModalCode}
								id="centeredModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Grids in Modals" />
					<CardBody>
						<div class="live-preview">
							<Button color="primary" on:click={tog_grid}
								>Launch Demo Modal</Button>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={gridsModalCode}
								id="gridsModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Static Backdrop Modal" />
					<CardBody>
						<div class="live-preview">
							<div>
								<Button color="primary" on:click={tog_backdrop}
									>Static Backdrop Modal</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={staticBackdropModalCode}
								id="staticBackdropModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Toggle Between Modal" />
					<CardBody>
						<div class="live-preview">
							<div>
								<Button color="primary" on:click={tog_togFirst}
									>Open First Modal</Button
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={togglebetweenCode}
								id="togglebetweenCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Tooltips and Popovers" />
					<CardBody>
						<div class="live-preview">
							<Button color="primary" on:click={tog_tooltip}
								>Launch Demo Modal</Button>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={tooltipModalCode}
								id="tooltipModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Scrollable Modal" />
					<CardBody>
						<div class="live-preview">
							<div>
								<Button color="primary" on:click={tog_scroll}
									>Scrollable Modal</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={scrollableModalCode}
								id="scrollableModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Varying Modal Content" />
					<CardBody>
						<div class="live-preview">
							<div>
								<div class="hstack gap-2 flex-wrap">
									<Button
										color="primary"
										on:click={tog_varying1}
										>Open Modal for Mary</Button
									>
									<Button
										color="primary"
										on:click={tog_varying2}
										>Open Modal for Jennifer</Button
									>
									<Button
										color="primary"
										on:click={tog_varying3}
										>Open Modal for Roderick</Button
									>
								</div>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={varyingModalCode}
								id="varyingModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Optional Sizes" />
					<CardBody>
						<p class="text-muted">
							Use <code>modal-fullscreen</code>,
							<code>modal-xl</code>, <code>modal-lg</code>, or
							<code>modal-sm</code> class to modal-dialog class to
							set different size modal respectively.
						</p>
						<div class="live-preview">
							<div>
								<div class="hstack flex-wrap gap-2">
									<Button
										color="primary"
										on:click={tog_fullscreen}
										>Fullscreen Modal</Button
									>

									<Button color="info" on:click={tog_xlarge}
										>Extra large Modal</Button
									>

									<Button color="success" on:click={tog_large}
										>Large Modal</Button
									>

									<Button color="danger" on:click={tog_small}
										>Small Modal</Button
									>
								</div>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={optionalModalCode}
								id="optionalModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Fullscreen Responsive Modals" />
					<CardBody>
						<p class="text-muted text-muted">
							Below mentioned modifier classes are used to show
							fullscreen modal as per minimum screen requirement.
						</p>
						<div class="live-preview">
							<div>
								<div class="hstack gap-2 flex-wrap">
									<Button
										color="primary"
										on:click={tog_fullscreen1}
										>Fullscreen modal</Button
									>
									<Button
										color="primary"
										on:click={tog_fullscreen_sm}
										>Full Screen Below sm</Button
									>
									<Button
										color="primary"
										on:click={tog_fullscreen_md}
										>Full Screen Below md</Button
									>
									<Button
										color="primary"
										on:click={tog_fullscreen_lg}
										>Full Screen Below lg</Button
									>
									<Button
										color="primary"
										on:click={tog_fullscreen_xl}
										>Full Screen Below xl</Button
									>
									<Button
										color="primary"
										on:click={tog_fullscreen_xxl}
										>Full Screen Below xxl</Button
									>
								</div>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={fullscreenResponsiveCode}
								id="fullscreenResponsiveCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<!-- <Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Animation Modals" />
					<CardBody>
						<p class="text-muted">
							Use <code>fadeInRight</code>,
							<code>fadeInLeft</code>, <code>fadeInUp</code>,
							<code>flip</code>, or <code>zoomIn</code> class to modal
							class to set different modal with animation effect respectively.
						</p>
						<div class="live-preview">
							<div>
								<div class="hstack gap-2 flex-wrap">
									<Button
										color="primary"
										on:click={tog_animationRight}
										>Fade In Right Modal</Button
									>
									<Button
										color="primary"
										on:click={tog_animationLeft}
										>Fade In Left Modal</Button
									>
									<Button
										color="primary"
										on:click={tog_animationUp}
										>Fade In Up Modal</Button
									>
									<Button
										color="primary"
										on:click={tog_animationFlip}
										>Flip Modal</Button
									>
									<Button
										color="primary"
										on:click={tog_animationZoom}
										>Zoom In Modal</Button
									>
								</div>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={animationModalCode}
								id="animationModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row> -->

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Modal Positions" />
					<CardBody>
						<p class="text-muted text-muted">
							Use <code>modal-dialog-right</code>,
							<code>modal-dialog-bottom</code>, or
							<code>modal-dialog-bottom-right</code> class to modal-dialog
							class to set modal at different positions respectively.
						</p>
						<div class="live-preview">
							<div>
								<div class="hstack gap-2 flex-wrap">
									<Button
										color="primary"
										on:click={tog_positionTop}
										>Top Modal</Button
									>
									<Button
										color="secondary"
										on:click={tog_positionTopRight}
										>Top Right Modal</Button
									>
									<Button
										color="success"
										on:click={tog_positionBottom}
										>Bottom Modal</Button
									>
									<Button
										color="danger"
										on:click={tog_positionBottomRight}
										>Bottom Right Modal</Button
									>
								</div>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={positionModalCode}
								id="positionModalCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row class="mt-2">
			<Col lg={12}>
				<div class="justify-content-between d-flex align-items-center mb-3">
					<h5 class="mb-0 pb-1 text-decoration-underline">Custom Modals Example</h5>
				</div>
				<Row>
					<Col xl={4} md={6}>
						<Card class="text-center border">
							<CardBody class="p-4 pb-0">
								<h5 class="mb-4">Success Message</h5>
								<p class="text-muted">Here is an example of a sweet alert with a success message.</p>
								<div>
									<Button color="primary" data-bs-toggle="modal" data-bs-target="#success-Payment" on:click={() => tog_successMessage()} >Click me</Button>
								</div>

								<Row class="justify-content-center mt-2">
									<Col lg={10}>
										<div>
											<img src={paymentImg} alt="Mac" class="img-fluid" />
										</div>
									</Col>
								</Row>
							</CardBody>
						</Card>
					</Col>

					<Col xl={4} md={6}>
						<Card class="text-center border">
							<CardBody class="p-4 pb-0">
								<h5 class="mb-4">Login Modals</h5>
								<p class="text-muted">Here is an example of a sweet alert with a error message.</p>
								<div>
									<Button color="primary" on:click={() => tog_loginModals()} data-bs-toggle="modal" data-bs-target="#loginModals">Click me</Button>
								</div>

								<Row class="justify-content-center mt-2">
									<Col lg={10}>
										<div>
											<img src={loginImg} alt="Mac" class="img-fluid" />
										</div>
									</Col>
								</Row>
							</CardBody>
						</Card>
					</Col>

					<Col xl={4} md={6}>
						<Card class="text-center border">
							<CardBody class="p-4 pb-0">
								<h5 class="mb-4">Subscribe Modals</h5>
								<p class="text-muted">Here is an example of a sweet alert with a warning message.</p>
								<div>
									<Button color="primary" on:click={() => tog_subscribeModals()} data-bs-toggle="modal" data-bs-target="#subscribeModals">Click me</Button>
								</div>

								<Row class="justify-content-center mt-2">
									<Col lg={10}>
										<div>
											<img src={subscribeImg} alt="Mac" class="img-fluid" />
										</div>
									</Col>
								</Row>
							</CardBody>
						</Card>
					</Col>

					<Col xl={4} md={6}>
						<Card class="text-center border">
							<CardBody class="p-4 pb-0">
								<h5 class="mb-4">Sign Up Modals</h5>
								<p class="text-muted">Here is an example of a sweet alert with a community registration field. </p>

								<div>
									<Button color="primary" on:click={() => tog_signUpModals()} data-bs-toggle="modal" data-bs-target="#signupModals">Click me</Button>
								</div>

								<Row class="justify-content-center mt-2">
									<Col lg={10}>
										<div>
											<img src={signupImg} alt="Mac" class="img-fluid" />
										</div>
									</Col>
								</Row>
							</CardBody>
						</Card>
					</Col>
				</Row>
			</Col>
		</Row>
	</Container>
</div>


<Modal
	id="myModal"
	isOpen={modal_standard}
>

	<div class="modal-header">
		<h5 class="modal-title fw-bold" id="myModalLabel">Modal Heading</h5>
		<button type="button" class="btn-close" on:click={() => {
			tog_standard();
		}}></button>
	</div>
	<ModalBody>
		<h5 class="fs-16">Overflowing text to show scroll behavior</h5>
		<p class="text-muted">
			One morning, when Gregor Samsa woke from troubled dreams, he found
			himself transformed in his bed into a horrible vermin. He lay on his
			armour-like back, and if he lifted his head a little he could see
			his brown belly, slightly domed and divided by arches into stiff
			sections.
		</p>
		<p class="text-muted">
			The bedding was hardly able to cover it and seemed ready to slide
			off any moment. His many legs, pitifully thin compared with the size
			of the rest of him, waved about helplessly as he looked. "What's
			happened to me?" he thought.
		</p>
		<p class="text-muted">
			It wasn't a dream. His room, a proper human room although a little
			too small, lay peacefully between its four familiar walls.
		</p>
	</ModalBody>
	<div class="modal-footer">
		<Button
			color="light"
			on:click={() => {
				tog_standard();
			}}
		>
			Close
		</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	isOpen={modal_center}
	toggle={() => {
		tog_center();
	}} className="modal-dialog-centered">
	<ModalHeader class="modal-title" />

	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/hrqwmuhr.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width:120px;height:120px"
		/>
		<div class="mt-4">
			<h3 class="mb-3">Oops something went wrong!</h3>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Button color="light" on:click={tog_center}>Close</Button>
				<Link href={null} class="btn btn-danger">Try Again</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	isOpen={modal_grid}
	toggle={() => {
		tog_grid();
	}}
>
	<ModalHeader
		class="modal-title fw-bold"
		toggle={() => {
			tog_grid();
		}}
	>
		Grid Modals
	</ModalHeader>
	<ModalBody>
		<form action="#">
			<div class="row g-3">
				<Col xxl={6}>
					<div>
						<Label for="firstName" class="form-label">First Name</Label
						>
						<Input
							type="text"
							class="form-control"
							id="firstName"
							placeholder="Enter firstname"
						/>
					</div>
				</Col>
				<Col xxl={6}>
					<div>
						<Label for="lastName" class="form-label">Last Name</Label
						>
						<Input
							type="text"
							class="form-control"
							id="lastName"
							placeholder="Enter lastname"
						/>
					</div>
				</Col>
				<Col lg={12}>
					<Label class="form-label">Gender</Label>
					<div>
						<div class="form-check form-check-inline">
							<input
								class="form-check-input"
								type="radio"
								name="inlineRadioOptions"
								id="inlineRadio1"
								value="option1"
							/>
							<Label class="form-check-label" for="inlineRadio1"
								>Male</Label>
						</div>
						<div class="form-check form-check-inline">
							<input
								class="form-check-input"
								type="radio"
								name="inlineRadioOptions"
								id="inlineRadio2"
								value="option2"
							/>
							<Label class="form-check-label" for="inlineRadio2"
								>Female</Label>
						</div>
						<div class="form-check form-check-inline">
							<input
								class="form-check-input"
								type="radio"
								name="inlineRadioOptions"
								id="inlineRadio3"
								value="option3"
							/>
							<Label class="form-check-label" for="inlineRadio3"
								>Others</Label>
						</div>
					</div>
				</Col>
				<Col xxl={6}>
					<Label for="emailInput" class="form-label">Email</Label>
					<Input
						type="email"
						class="form-control"
						id="emailInput"
						placeholder="Enter your email"
					/>
				</Col>
				<Col xxl={6}>
					<Label for="passwordInput" class="form-label">Password</Label>
					<Input
						type="password"
						class="form-control"
						id="passwordInput"
						value="451326546"
						placeholder="Enter password"
					/>
				</Col>
				<Col lg={12}>
					<div class="hstack gap-2 justify-content-end">
						<Button color="light" on:click={tog_grid}>Close</Button>
						<Button color="primary">Submit</Button>
					</div>
				</Col>
			</div>
		</form>
	</ModalBody>
</Modal>

<Modal
	isOpen={modal_backdrop}
	toggle={() => {
		tog_backdrop();
	}}
	backdrop={"static"}
	id="staticBackdrop"
	className="modal-dialog-centered"
>
	<ModalHeader
		class="modal-title"
		id="staticBackdropLabel"
		toggle={() => {
			tog_backdrop();
		}}
	>
		Modal title
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/lupuorrc.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>

		<div class="mt-4">
			<h3 class="mb-3">You've made it!</h3>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-secondary fw-medium"
					on:click={tog_backdrop}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success" on:click={tog_backdrop}>Completed</Link
				>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	isOpen={modal_togFirst}
	toggle={() => {
		tog_togFirst();
	}}
	id="firstmodal"
	className="modal-dialog-centered"
>
	<ModalHeader
		class="modal-title"
		id="exampleModalToggleLabel"
		toggle={() => {
			tog_togFirst();
		}}
	>
		Modal 1
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/tdrtiskw.json"
			trigger="loop"
			colors="primary:#f7b84b,secondary:#405189"
			style="width: 130px; height: 130px"
		/>
		<div class="mt-4 pt-4">
			<h3>Uh oh, something went wrong!</h3>
			<p class="text-muted">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>

			<Button
				color="warning"
				on:click={() => {
					tog_togSecond();
					tog_togFirst(false);
				}}
			>
				Continue
			</Button>
		</div>
	</ModalBody>
</Modal>

<Modal
	isOpen={modal_togSecond}
	toggle={() => {
		tog_togSecond();
	}}
	id="secondmodal"
	className="modal-dialog-centered"
>
	<ModalHeader
		class="modal-title"
		id="exampleModalToggleLabel2"
		toggle={() => {
			tog_togSecond();
		}}
	>
		Modal 2
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/zpxybbhl.json"
			trigger="loop"
			colors="primary:#405189,secondary:#0ab39c"
			style="width: 150px; height: 150px"
		/>
		<div class="mt-4 pt-3">
			<h3 class="mb-3">Follow-Up Email</h3>
			<p class="text-muted mb-4">
				Hide this modal and show the first with the button below
				Automatically Send your invitees a follow -Up email.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Button
					color="danger"
					on:click={() => {
						tog_togFirst();
						tog_togSecond(false);
					}}
				>
					Back to First
				</Button>
				<Button color="light" on:click={tog_togSecond}>Close</Button>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	isOpen={modal_tooltip}
	toggle={() => {
		tog_tooltip();
	}}
>
	<ModalHeader
		class="modal-title fw-bold"
		toggle={() => {
			tog_tooltip();
		}}
	>
		Tooltips and Popovers Modal
	</ModalHeader>
	<ModalBody>
		<h5 class="fs-17">Popover in a Modal</h5>
		<p class="text-muted">
			You only need to know a little to make a big
			{" "}<Link
				href={null}
				class="popover-test fw-medium text-decoration-underline link-success"
				id="Popover"
			>
				Popover on Click
			</Link>{" "}
			you do every day. So let's get started. First, some common types of fonts
			and what you need to know about them triggers a popover on click.
		</p>
		<Popover
			placement="bottom"
			target="Popover"
			title="Common Types of Fonts"
		>
			They're a good choice for more traditional projects.
		</Popover>

		<h5 class="fs-17">Tooltips in a Modal</h5>
		<p class="text-muted">
			Opposites attract, and that’s a fact. It’s in our
			{" "}<Link
				href={null}
				class="tooltip-test text-decoration-underline fw-medium"
				id="Tooltip1"
			>
				graphic design
			</Link>{" "} to be interested in the unusual, and that’s why using
			{" "}<Link
				href={null}
				class="tooltip-test text-decoration-underline"
				id="Tooltip2">design</Link
			>
			contrasting colors in Graphic Design is a must.
		</p>
		<Tooltip placement="top" target="Tooltip1">Morton Bayer</Tooltip>
		<Tooltip placement="top" target="Tooltip2">Web Developers</Tooltip>
	</ModalBody>
	<div class="modal-footer">
		<div class="mx-auto">
			<Link href={null} class="btn btn-link fw-semibold"
				>Read More <i
					class="ri-arrow-right-line ms-1 align-middle"
				/></Link
			>
		</div>
	</div>
</Modal>

<Modal
	isOpen={modal_scroll}
	toggle={() => {
		tog_scroll();
	}}
	className="modal-dialog-scrollable"
	id="exampleModalScrollable"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalScrollableTitle"
		toggle={() => {
			tog_scroll();
		}}
	>
		Scrollable modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					You've probably heard that opposites attract. The same is
					true for fonts. Don't be afraid to combine font styles that
					are different but complementary, like sans serif with serif,
					short with tall, or decorative with simple. Qui photo booth
					letterpress, commodo enim craft beer mlkshk aliquip jean
					shorts ullamco ad vinyl cillum PBR.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-17 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Just like in the image where we talked about using multiple
					fonts, you can see that the background in this graphic
					design is blurred. Whenever you put text on top of an image,
					it’s important that your viewers can understand.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Keytar raw denim keffiyeh etsy art party before they sold
					out master cleanse gluten-free squid scenester freegan cosby
					sweater.
				</p>
			</div>
		</div>
	</ModalBody>

	<div class="modal-footer">
		<Button color="light" on:click={tog_scroll}>Close</Button>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	size="xl"
	isOpen={modal_fullscreen}
	toggle={() => {
		tog_fullscreen();
	}}
	className="modal-fullscreen"
	id="exampleModalFullscreen"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalFullscreenLabel"
		toggle={() => {
			tog_fullscreen();
		}}
	>
		Fullscreen Modal Heading
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					You've probably heard that opposites attract. The same is
					true for fonts. Don't be afraid to combine font styles that
					are different but complementary, like sans serif with serif,
					short with tall, or decorative with simple. Qui photo booth
					letterpress, commodo enim craft beer mlkshk aliquip jean
					shorts ullamco ad vinyl cillum PBR.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-16 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Just like in the image where we talked about using multiple
					fonts, you can see that the background in this graphic
					design is blurred. Whenever you put text on top of an image,
					it’s important that your viewers can understand.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Keytar raw denim keffiyeh etsy art party before they sold
					out master cleanse gluten-free squid scenester freegan cosby
					sweater.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			color="light"
			on:click={() => {
				tog_fullscreen();
			}}
			class="btn btn-link link-success fw-medium"
			><i class="ri-close-line me-1 align-middle" />
			Close
		</Link>
		<Button color="primary" class="btn btn-primary ">Save changes</Button>
	</div>
</Modal>

<Modal
	size="xl"
	isOpen={modal_xlarge}
	toggle={() => {
		tog_xlarge();
	}}
	className="modal-xl"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="myExtraLargeModalLabel"
		toggle={() => {
			tog_xlarge();
		}}
	>
		Extra large modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					You've probably heard that opposites attract. The same is
					true for fonts. Don't be afraid to combine font styles that
					are different but complementary, like sans serif with serif,
					short with tall, or decorative with simple. Qui photo booth
					letterpress, commodo enim craft beer mlkshk aliquip jean
					shorts ullamco ad vinyl cillum PBR.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-16 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Just like in the image where we talked about using multiple
					fonts, you can see that the background in this graphic
					design is blurred. Whenever you put text on top of an image,
					it’s important that your viewers can understand.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Keytar raw denim keffiyeh etsy art party before they sold
					out master cleanse gluten-free squid scenester freegan cosby
					sweater.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={tog_xlarge}
			><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	size="lg"
	isOpen={modal_large}
	toggle={() => {
		tog_large();
	}}
	className="modal-lg"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="myLargeModalLabel"
		toggle={() => {
			tog_large();
		}}
	>
		Large Modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					You've probably heard that opposites attract. The same is
					true for fonts. Don't be afraid to combine font styles that
					are different but complementary, like sans serif with serif,
					short with tall, or decorative with simple. Qui photo booth
					letterpress, commodo enim craft beer mlkshk aliquip jean
					shorts ullamco ad vinyl cillum PBR.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-16 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Just like in the image where we talked about using multiple
					fonts, you can see that the background in this graphic
					design is blurred. Whenever you put text on top of an image,
					it’s important that your viewers can understand.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Keytar raw denim keffiyeh etsy art party before they sold
					out master cleanse gluten-free squid scenester freegan cosby
					sweater.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={tog_large}
			><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	size="sm"
	isOpen={modal_small}
	toggle={() => {
		tog_small();
	}}
	className="modal-sm"
>
	<ModalHeader
		class="modal-title"
		id="mySmallModalLabel"
		toggle={() => {
			tog_small();
		}}
	>
		Small Modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={tog_small}
			><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	size="xl"
	isOpen={modal_fullscreen1}
	toggle={() => {
		tog_fullscreen1();
	}}
	className="modal-fullscreen"
	id="fullscreeexampleModal"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="fullscreeexampleModalLabel"
		toggle={() => {
			tog_fullscreen1();
		}}
	>
		Full screen modal
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					For that very reason, I went on a quest and spoke to many
					different professional graphic designers and asked them what
					graphic design tips they live.
				</p>
			</div>
		</div>
		<h6 class="fs-16 my-3">Graphic Design</h6>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Opposites attract, and that’s a fact. It’s in our nature to
					be interested in the unusual, and that’s why using
					contrasting colors in Graphic Design is a must. It’s
					eye-catching, it makes a statement, it’s impressive graphic
					design. Increase or decrease the letter spacing depending.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Trust fund seitan letterpress, keytar raw denim keffiyeh
					etsy art party before they sold out master cleanse
					gluten-free squid scenester freegan cosby sweater.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			type="button"
			on:click={() => {
				tog_fullscreen1();
			}}
			class="btn btn-link link-success fw-medium"
			><i class="ri-close-line me-1 align-middle" />
			Close
		</Link>
		<Button color="primary" class="btn btn-primary ">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenSm"
	isOpen={modal_fullscreen_sm}
	toggle={() => {
		tog_fullscreen_sm();
	}}
	className="modal-fullscreen-sm-down"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalFullscreenSmLabel"
		toggle={() => {
			tog_fullscreen_sm();
		}}
	>
		Full screen below sm
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_sm();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenMd"
	isOpen={modal_fullscreen_md}
	toggle={() => {
		tog_fullscreen_md();
	}}
	className="modal-fullscreen-md-down"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalFullscreenMdLabel"
		toggle={() => {
			tog_fullscreen_md();
		}}
	>
		Full screen below md
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_md();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenLg"
	isOpen={modal_fullscreen_lg}
	toggle={() => {
		tog_fullscreen_lg();
	}}
	className="modal-fullscreen-lg-down"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalFullscreenLgLabel"
		toggle={() => {
			tog_fullscreen_lg();
		}}
	>
		Full screen below lg
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_lg();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenXl"
	isOpen={modal_fullscreen_xl}
	toggle={() => {
		tog_fullscreen_xl();
	}}
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalFullscreenXlLabel"
		toggle={() => {
			tog_fullscreen_xl();
		}}
		className="modal-fullscreen-sm-down"
	>
		Full screen below xl
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_xl();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	id="exampleModalFullscreenXxl"
	isOpen={modal_fullscreen_xxl}
	toggle={() => {
		tog_fullscreen_xxl();
	}}
	className="modal-fullscreen-xxl-down"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="exampleModalFullscreenXxlLabel"
		toggle={() => {
			tog_fullscreen_xxl();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody>
		<h6 class="fs-16">Give your text a good structure</h6>
		<div class="d-flex">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2">
				<p class="text-muted mb-0">
					Raw denim you probably haven't heard of them jean shorts
					Austin. Nesciunt tofu stumptown aliqua, retro synth master
					cleanse.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					Too much or too little spacing, as in the example below, can
					make things unpleasant for the reader. The goal is to make
					your text as comfortable to read as possible.
				</p>
			</div>
		</div>
		<div class="d-flex mt-2">
			<div class="flex-shrink-0">
				<i class="ri-checkbox-circle-fill text-success" />
			</div>
			<div class="flex-grow-1 ms-2 ">
				<p class="text-muted mb-0">
					In some designs, you might adjust your tracking to create a
					certain artistic effect. It can also help you fix fonts that
					are poorly spaced to begin with.
				</p>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer">
		<Link
			href={null}
			class="btn btn-link link-success fw-medium"
			on:click={() => {
				tog_fullscreen_xxl();
			}}><i class="ri-close-line me-1 align-middle" /> Close</Link
		>
		<Button color="primary">Save changes</Button>
	</div>
</Modal>

<Modal
	isOpen={modal_varying1}
	toggle={() => {
		tog_varying1();
	}}
	id="exampleModal"
>
	<ModalHeader
		toggle={() => {
			tog_varying1();
		}}
	>
		New message to Mary
	</ModalHeader>
	<ModalBody>
		<form>
			<div class="mb-3">
				<Label for="customer-name" class="col-form-label">Customer Name:</Label
				>
				<Input
					type="text"
					class="form-control"
					id="customer-name"
					value="Mary"
					readOnly
				/>
			</div>
			<div class="mb-3">
				<Label for="message-text" class="col-form-label">Message:</Label
				>
				<textarea class="form-control" id="message-text" rows="4" />
			</div>
		</form>
	</ModalBody>
	<div class="modal-footer">
		<Button color="light" on:click={tog_varying1}>Back</Button>
		<Button color="primary">Send message</Button>
	</div>
</Modal>

<Modal
	isOpen={modal_varying2}
	toggle={() => {
		tog_varying2();
	}}
>
	<ModalHeader
		class="modal-title fw-bold"
		toggle={() => {
			tog_varying2();
		}}
	>
		New message to Jennifer
	</ModalHeader>
	<ModalBody>
		<form>
			<div class="mb-3">
				<Label for="customer-name" class="col-form-label">Customer Name:</Label
				>
				<Input
					type="text"
					class="form-control"
					id="customer-name"
					value="Jennifer"
					readOnly
				/>
			</div>
			<div class="mb-3">
				<Label for="message-text" class="col-form-label">Message:</Label
				>
				<textarea class="form-control" id="message-text" rows="4" />
			</div>
		</form>
	</ModalBody>
	<div class="modal-footer">
		<Button color="light" on:click={tog_varying2}>Back</Button>
		<Button color="primary">Send message</Button>
	</div>
</Modal>;

<Modal
	isOpen={modal_varying3}
	toggle={() => {
		tog_varying3();
	}}
>
	<ModalHeader
		class="modal-title fw-bold"
		toggle={() => {
			tog_varying3();
		}}
	>
		New message to Roderick
	</ModalHeader>
	<ModalBody>
		<form>
			<div class="mb-3">
				<Label for="customer-name" class="col-form-label">Customer Name:</Label
				>
				<Input
					type="text"
					class="form-control"
					id="customer-name"
					value="Roderick"
					readOnly
				/>
			</div>
			<div class="mb-3">
				<Label for="message-text" class="col-form-label">Message:</Label
				>
				<textarea class="form-control" id="message-text" rows="4" />
			</div>
		</form>
	</ModalBody>
	<div class="modal-footer">
		<Button color="light" on:click={tog_varying3}>Back</Button>
		<Button color="primary">Send message</Button>
	</div>
</Modal>;

<Modal
	id="topmodal"
	isOpen={modal_positionTop}
	toggle={() => {
		tog_positionTop();
	}}
	
>
	<ModalHeader
		class="modal-title fw-bold"
		id="myModalLabel"
		toggle={() => {
			tog_positionTop();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/pithnlch.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>
		<div class="mt-4">
			<h4 class="mb-3">Your event has been created.</h4>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-success fw-medium"
					on:click={() => {
						tog_positionTop();
					}}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success">Completed</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	id="top-rightmodal"
	isOpen={modal_positionTopRight}
	toggle={() => {
		tog_positionTopRight();
	}}
	className="modal-dialog-right"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="myModalLabel"
		toggle={() => {
			tog_positionTopRight();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/pithnlch.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>
		<div class="mt-4">
			<h4 class="mb-3">Your event has been created.</h4>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-success fw-medium"
					on:click={() => {
						tog_positionTopRight();
					}}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success">Completed</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	id="bottomModal"
	isOpen={modal_positionBottom}
	toggle={() => {
		tog_positionBottom();
	}}
	className="modal-dialog-bottom"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="myModalLabel"
		toggle={() => {
			tog_positionBottom();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/pithnlch.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>
		<div class="mt-4">
			<h4 class="mb-3">Your event has been created.</h4>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-success fw-medium"
					on:click={tog_positionBottom}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success">Completed</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal
	id="bottom-rightModal"
	isOpen={modal_positionBottomRight}
	toggle={() => {
		tog_positionBottomRight();
	}}
	className="modal-dialog-bottom-right"
>
	<ModalHeader
		class="modal-title fw-bold"
		id="myModalLabel"
		toggle={() => {
			tog_positionBottomRight();
		}}
	>
		Modal Heading
	</ModalHeader>
	<ModalBody class="text-center p-5">
		<lord-icon
			src="//cdn.lordicon.com/pithnlch.json"
			trigger="loop"
			colors="primary:#121331,secondary:#08a88a"
			style="width: 120px; height: 120px"
		/>
		<div class="mt-4">
			<h4 class="mb-3">Your event has been created.</h4>
			<p class="text-muted mb-4">
				The transfer was not successfully received by us. the email of
				the recipient wasn't correct.
			</p>
			<div class="hstack gap-2 justify-content-center">
				<Link
					href={null}
					class="btn btn-link link-success fw-medium"
					on:click={tog_positionBottomRight}><i class="ri-close-line me-1 align-middle" /> Close</Link
				>
				<Link href={null} class="btn btn-success">Completed</Link>
			</div>
		</div>
	</ModalBody>
</Modal>

<Modal id="success-Payment" tabIndex="-1" isOpen={modal_successMessage} toggle={() => { tog_successMessage(); }} className="modal-dialog-centered">
	<ModalBody class='text-center p-5'>
		<div class="text-end">
			<button type="button" on:click={() => { tog_successMessage(); }} class="btn-close text-end" data-bs-dismiss="modal" aria-label="Close"></button>
		</div>
		<div class="mt-2">
			<lord-icon src="https://cdn.lordicon.com/tqywkdcz.json" trigger="hover"
				style="width: 150px; height: 150px">
			</lord-icon>
			<h4 class="mb-3 mt-4 fw-bold">Your Transaction is Successfull !</h4>
			<p class="text-muted fs-15 mb-4">Successful transaction is the status of operation whose result is the payment of the amount paid by the customer in favor of the merchant.</p>
			<div class="hstack gap-2 justify-content-center">
				<button class="btn btn-primary">New transaction</button>
				<button class="btn btn-soft-success"><i class="ri-links-line align-bottom"></i> Copy tracking link</button>
			</div>
		</div>
	</ModalBody>
	<div class="modal-footer bg-light p-3 justify-content-center" >
		<p class="mb-0 text-muted">You like our service? <Link href={null} class="link-secondary fw-semibold">Invite Friends</Link></p>
	</div>
</Modal>


<Modal id="loginModals" tabIndex="-1" isOpen={modal_loginModals} toggle={() => { tog_loginModals(); }} className="modal-dialog-centered">
	<div class="modal-content border-0 overflow-hidden">
		<ModalBody class='login-modal p-5'>
			<h5 class="text-white fs-20 fw-bold">Login</h5>
			<p class="text-white-50 mb-4">Don't have an account? <Link href="/#" class="text-white">Sign Up.</Link></p>
			<div class="vstack gap-2 justify-content-center">
				<button class="btn btn-light"><i class="ri-google-fill align-bottom text-danger"></i> Google</button>
				<button class="btn btn-info"><i class="ri-facebook-fill align-bottom"></i> Facebook</button>
			</div>
		</ModalBody>
		<ModalBody class="p-5">
			<h5 class="mb-3 fw-bold">Login with Email</h5>
			<form>
				<div class="mb-2">
					<input type="email" class="form-control" id="exampleInputEmail1" placeholder="Enter your email/username" />
				</div>
				<div class="mb-3">
					<input type="password" class="form-control" id="exampleInputPassword1" placeholder="Enter your password" />
					<div class="mt-1 text-end">
						<Link href="/authenticationInner/passwordreset/auth-pass-reset-basic">Forgot password ?</Link>
					</div>
				</div>
				<button type="submit" class="btn btn-primary w-100" on:click={() => { tog_loginModals(); }}>Submit</button>
			</form>
		</ModalBody>
	</div>
</Modal>


<Modal id="subscribeModals" tabIndex="-1" isOpen={subscribeModals} toggle={() => { tog_subscribeModals(); }} className="modal-dialog-centered modal-lg">
	<Row class="g-0">
		<Col lg={7}>
			<div class="modal-body p-5">
				<h2 class="lh-base fw-bold">Subscribe now today to get <span class="text-danger">20% off</span> experiences!</h2>
				<p class="text-muted mb-4">A free bet is a bet which is provided by a betting
					site for a customer to place and then benefit from the winnings. Free bets are commonly used as welcome offers.</p>
				<div class="input-group mb-3">

					<input type="text" class="form-control" placeholder="Enter your email" aria-label="Example text with button addon" aria-describedby="button-addon1" />
					<button class="btn btn-primary" type="button" id="button-addon1">Subscript Now</button>
				</div>

				<div class="form-check">
					<input type="checkbox" class="form-check-input" id="exampleCheck1" />
					<Label class="form-check-label" htmlfor="exampleCheck1">By subscribing to a particular channel or user on YouTube, you can receive instant updates.</Label>
				</div>
			</div>
		</Col>
		<Col lg={5}>
			<div class="subscribe-modals-cover h-100">
				<img src={authbg} alt="" class="h-100 w-100 object-cover" style="clipPath: polygon(100% 0%, 100% 100%, 100% 100%, 0% 100%, 25% 50%, 0% 0%)" />
			</div>
		</Col>
	</Row>
</Modal>

<Modal id="signupModals" tabIndex="-1" isOpen={modal_signUpModals} toggle={() => { tog_signUpModals(); }} className="modal-dialog-centered">
	<ModalHeader class="p-3" toggle={() => { tog_signUpModals(); }}>
		Sign Up
	</ModalHeader>
	<Alert color="success" class="rounded-0 mb-0">
		<p class="mb-0">Up to <span class="fw-semibold">50% OFF</span>, Hurry up before the stock ends</p>
	</Alert>
	<ModalBody>
		<form>
			<div class="mb-3">
				<Label htmlfor="fullName" class="form-label">Full Name</Label>
				<input type="email" class="form-control" id="fullName" placeholder="Enter your name" />
			</div>
			<div class="mb-3">
				<Label htmlfor="emailInput" class="form-label">Email address</Label>
				<input type="email" class="form-control" id="emailInput" placeholder="Enter your email" />
			</div>
			<div class="mb-3">
				<Label htmlfor="exampleInputPassword1" class="form-label">Password</Label>
				<input type="password" class="form-control" id="exampleInputPassword1" placeholder="Enter your password" />
			</div>
			<div class="mb-3 form-check">
				<input type="checkbox" class="form-check-input" id="checkTerms" />
				<Label class="form-check-label" htmlfor="checkTerms">I agree to the <span class="fw-semibold">Terms of Service</span> and Privacy Policy</Label>
			</div>
			<div class="text-end">
				<button type="submit" class="btn btn-primary" on:click={() => { tog_signUpModals(); }}>Sign Up Now</button>
			</div>
		</form>
	</ModalBody>
</Modal>