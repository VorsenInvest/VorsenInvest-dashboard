<script>
	import {
		Button,
		Card,
		CardBody,
		Col,
		Container,
		Row,
		Toast,
		ToastBody,
		ToastHeader,
		Form
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import { toasts, ToastContainer, BootstrapToast } from "svelte-toasts";
	import Link from "svelte-link";

	import logosm from '../../../assets/images/logo-sm.png'
	
	let toast1 = true;
	let toast2 = true;
	let toast3 = true;
	let toast4 = true;
	let toast5 = true;
	let toast6 = true;
	let toast7 = false;
	let toast8 = false;
	let toast9 = false;
	let toast10 = false;
	let toast11 = true;

	let position = "";
	const setPosition = (newpos) =>{
		position = newpos
	}

	// Bootstrap Toasts

	const bootstrapToastsCode = `<!-- Default Toast --> 
	let toast1 = true;

<Toast isOpen={toast1}>
    <ToastHeader toggle={() => (toast1 = !toast1)}>
        <img src={logosm} class="rounded me-2" alt="..." height="20" />
        <span class="fw-semibold me-auto">Velzon</span>
        <small style="margin-left:140px">06 mins ago</small>
    </ToastHeader>
    <ToastBody>
        Hello, world! This is a toast message.
    </ToastBody>
</Toast>

<!-- Translucent Toast --> 
let toast2 = true;

<Toast isOpen={toast2}>
    <ToastHeader toggle={() => (toast2 = !toast2)}>
        <img src={logosm} class="rounded me-2" alt="..." height="20" />
    <span class="fw-semibold me-auto">Velzon</span>
    <small style="margin-left:"150px">11 mins ago</small>
    </ToastHeader>
    <ToastBody>
        Hello, world! This is a toast message.
    </ToastBody>
</Toast>

<!-- Stacking Toast --> 
let toast3 = true;

<Toast isOpen={toast3}>
    <ToastHeader toggle={() => (toast3 = !toast3)}>
        <img src={logosm} class="rounded me-2" alt="..." height="20" />
        <span class="fw-semibold me-auto">Velzon</span>
        <small style="margin-left:165px">Just now</small>
    </ToastHeader>
    <ToastBody>
        See? Just like this.
    </ToastBody>
</Toast>

<!-- Placement Toast --> 
let toast5 = true;

<div class="bg-light" style="position: 'relative'; min-height: '200px'">
    <Toast isOpen={toast5} style="position: 'absolute'; top: '16px'; right: '16px'">
        <ToastHeader toggle={() => (toast5 = !toast5)}>
            <img src={logosm} class="rounded me-2" alt="..." height="20" />
            <span class="fw-semibold me-auto">Velzon</span>
            <small style="margin-left:140px">06 mins ago</small>
        </ToastHeader>
        <ToastBody>
            Hello, world! This is a toast message.
        </ToastBody>
    </Toast>
</div>

 <!-- Flexbox container for aligning the toasts -->
 let toast6 = true;

<div class="bg-light d-flex justify-content-center align-items-center" style="height: 200px">
    <Toast isOpen={toast6}>
        <ToastHeader toggle={() => (toast6 = !toast6)}>
             <img src={logosm} class="rounded me-2" alt="..." height="20" />
             <span class="fw-semibold me-auto">Velzon</span>
             <small style="margin-left:"150px">11 mins ago</small>
        </ToastHeader>
        <ToastBody>
             Hello, world! This is a toast message.
        </ToastBody>
    </Toast>
</div>
`;

	// Toast Placement
	const toastPlacementCode = `let toast11 = true;

let position = "";
const setPosition = (newpos) =>{
	position = newpos
}

<Form>
	<div class="mb-3">
		<select class="form-select mt-2" on:change={(e) => setPosition(e.currentTarget.value)}>
			<option value="" defaultValue>Select a position...</option>
			<option value="top-0 start-0">Top left</option>
			<option value="top-0 start-50 translate-middle-x">Top center</option>
			<option value="top-0 end-0">Top right</option>
			<option value="top-50 start-0 translate-middle-y">Middle left</option>
			<option value="top-50 start-50 translate-middle">Middle center</option>
			<option value="top-50 end-0 translate-middle-y">Middle right</option>
			<option value="bottom-0 start-0">Bottom left</option>
			<option value="bottom-0 start-50 translate-middle-x">Bottom center</option>
			<option value="bottom-0 end-0">Bottom right</option>
		</select>
	</div>
</Form>
<div aria-live="polite" aria-atomic="true" class="bd-example bg-light position-relative" style="min-height: 300px">
	<div class={"toast-container position-absolute p-3 " + position} id="toastPlacement">
		<Toast isOpen={toast11}>
			<ToastHeader toggle={() =>
				(toast11 = !toast11)}>
				<img src={logosm} class="rounded me-2"
					alt="..." height="20" />
				<strong class="me-auto">Velzon</strong>
				<small style="margin-left: 150px">11 mins ago</small>
			</ToastHeader>
			<ToastBody>
				Hello, world! This is a toast message.
			</ToastBody>
		</Toast>
	</div>
</div>

`;

	// Bordered with Icon Toast
	const borderIconCode = `
<!-- Bordered With Icon Toast -->
<div class="hstack flex-wrap gap-2">
    <Button class="btn btn-primary" id="borderedToast1Btn" on:click={() => (toast7 = !toast7)} >Primary Toast</Button>
    <Button class="btn btn-success" id="borderedToast2Btn" on:click={() => (toast8 = !toast8)} >Success Toast</Button>
    <Button class="btn btn-info" id="borderedTost3Btn" on:click={() => (toast9 = !toast9)} >info Toast</Button>
    <Button class="btn btn-danger" id="borderedToast4Btn" on:click={() => (toast10 = !toast10)} >Danger Toast</Button>
</div>
    
<div style="z-index: 11">
    <Toast isOpen={toast7} id="borderedToast1" class="toast-border-primary overflow-hidden mt-3">
        <ToastBody>
            <div class="d-flex align-items-center">
                <div class="flex-shrink-0 me-2">
                    <i class="ri-user-smile-line align-middle"></i>
                </div>
                <div class="flex-grow-1">
                    <h6 class="mb-0">Your application was successfully sent.</h6>
                </div>
            </div>
        </ToastBody>
    </Toast>
</div>
    
<div style="z-index: 11">
    <Toast isOpen={toast8} id="borderedToast2" class="toast-border-success overflow-hidden mt-3">
        <ToastBody>
            <div class="d-flex align-items-center">
                <div class="flex-shrink-0 me-2">
                        <i class="ri-checkbox-circle-fill align-middle"></i>
                </div>
                <div class="flex-grow-1">
                        <h6 class="mb-0">Yey! Everything worked!</h6>
                </div>
            </div>
        </ToastBody>
    </Toast>
</div>
    
<div style="z-index: 11">
    <Toast isOpen={toast9} id="borderedToast3" class="toast-border-wainforning overflow-hidden mt-3">
        <ToastBody>
            <div class="d-flex align-items-center">
                <div class="flex-shrink-0 me-2">
                    <i class="ri-notification-off-line align-middle"></i>
                </div>
                <div class="flex-grow-1">
                    <h6 class="mb-0">Something went wrong, try again.</h6>
                </div>
            </div>
        </ToastBody>
    </Toast>
</div>
    
<div style="z-index: 11">
    <Toast isOpen={toast10} id="borderedToast4" class="toast-border-danger overflow-hidden mt-3">
        <ToastBody>
            <div class="d-flex align-items-center">
                <div class="flex-shrink-0 me-2">
                    <i class="ri-alert-line align-middle"></i>
                </div>
                <div class="flex-grow-1">
                    <h6 class="mb-0">Something is very wrong!  <Link href={null} class="text-decoration-underline">See detailed report.</Link></h6>
                </div>
            </div>
        </ToastBody>
    </Toast>
</div>
`;

	// Toastify JS
	const toastifyCode = `<!-- Toast -->
const defaultnotify = () => toast("Welcome Back! This is a Toast Notification", { position: "top-right", hideProgressBar: true, class: 'bg-primary text-white' });
const successnotify = () => toast("Your application was successfully sent", { position: "top-center", hideProgressBar: true, closeOn:click: false, class: 'bg-success text-white' });
const warningnotify = () => toast("Warning ! Something went wrong try again", { position: "top-center", hideProgressBar: true, closeOn:click: false, class: 'bg-warning text-white' });
const errornotify = () => toast("Error ! An error occurred.", { position: "top-center", hideProgressBar: true, closeOn:click: false, class: 'bg-danger text-white' });

<Button color="light" class="w-xs" on:click={defaultnotify}>Default</Button>
<Button color="light" class="w-xs" on:click={successnotify}>Success</Button>
<Button color="light" class="w-xs" on:click={warningnotify}>Warning</Button>
<Button color="light" class="w-xs" on:click={errornotify}>Error</Button>
<ToastContainer />

<!-- Display Position -->
const topleftnotify = () => toast("Welcome Back ! This is a Toast Notification", { position: "top-left", hideProgressBar: true, class: 'bg-success text-white' });
const topcenternotify = () => toast("Welcome Back ! This is a Toast Notification", { position: "top-center", hideProgressBar: true, class: 'bg-success text-white' });
const toprightnotify = () => toast("Welcome Back ! This is a Toast Notification", { position: "top-right", hideProgressBar: true, class: 'bg-success text-white' });
const bottomleftnotify = () => toast("Welcome Back ! This is a Toast Notification", { position: "bottom-left", hideProgressBar: true, class: 'bg-success text-white' });
const bottomcenternotify = () => toast("Welcome Back ! This is a Toast Notification", { position: "bottom-center", hideProgressBar: true, class: 'bg-success text-white' });
const bottomrightnotify = () => toast("Welcome Back ! This is a Toast Notification", { position: "bottom-right", hideProgressBar: true, class: 'bg-success text-white' });

<Button color="light" class="w-xs" on:click={topleftnotify}>Top Left</Button>
<Button color="light" class="w-xs" on:click={topcenternotify}>Top Center</Button>
<Button color="light" class="w-xs" on:click={toprightnotify}>Top Right</Button>
<Button color="light" class="w-xs" on:click={bottomleftnotify}>Bottom Left</Button>
<Button color="light" class="w-xs" on:click={bottomcenternotify}>Bottom Center</Button>
<Button color="light" class="w-xs" on:click={bottomrightnotify}>Bottom Right</Button>

<!-- Offset Position -->
const offsetnotify = () => toast("Welcome Back ! This is a Toast Notification", { position: "top-right", hideProgressBar: true, class: 'bg-success text-white m-5' });
<Button color="light" class="w-xs" on:click={offsetnotify} >Click Me</Button>

<!-- Close icon Display -->
const closeiconnotify = () => toast("Welcome Back ! This is a Toast Notification", { position: "top-right", hideProgressBar: true, class: 'bg-success text-white' });
<Button color="light" class="w-xs" on:click={closeiconnotify} >Click Me</Button>

<!-- Duration -->
const durationnotify = () => toast("Toast Duration 5s", { position: "top-right", hideProgressBar: false, class: 'bg-success text-white' });
<Button color="light" class="w-xs" on:click={durationnotify} >Click Me</Button>
`;

	const defaultnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-center",
			class: "bg-success text-white",
			type: "success",
			theme: "dark",
		});
	};
	const successnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Your application was successfully sent",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-center",
			class: "bg-success text-white",
			type: "success",
			theme: "dark",
		});
	};

	const warningnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Warning ! Something went wrong try again",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-center",
			class: "bg-success text-white",
			type: "warning",
			theme: "dark",
		});
	};

	const errornotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Error ! An error occurred.",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-center",
			class: "bg-success text-white",
			type: "error",
			theme: "dark",
		});
	};

	const topleftnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back ! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-left",
			class: "bg-success text-white",
			type: "success",
			theme: "dark",
		});
	};

	const topcenternotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back ! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-center",
			class: "bg-success text-white",
			type: "success",
			theme: "dark",
		});
	};

	const toprightnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back ! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-right",
			class: "bg-success text-white",
			type: "success",
			theme: "dark",
		});
	};

	const bottomleftnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back ! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "bottom-left",
			class: "bg-success text-white",
			type: "success",
			theme: "dark",
		});
	};

	const bottomcenternotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back ! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "bottom-center",
			class: "bg-success text-white",
			type: "success",
			theme: "dark",
		});
	};

	const bottomrightnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back ! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "bottom-right",
			class: "bg-success text-white",
			type: "success",
			theme: "dark",
		});
	};

	const offsetnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back ! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-right",
			class: "bg-success text-white m-5",
			type: "success",
			theme: "dark",
		});
	};

	const closeiconnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Welcome Back ! This is a Toast Notification",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-right",
			class: "bg-success text-white m-5",
			type: "success",
			theme: "dark",
		});
	};
	const durationnotify = () => {
		const toast = toasts.add({
			title: "",
			description: "Toast Duration 5s",
			duration: 10000, // 0 or negative to avoid auto-remove
			placement: "top-right",
			class: "bg-success text-white m-5",
			type: "success",
			theme: "dark",
		});
	};
</script>

<svelte:head>
	<title>Notifications | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Notifications" pageTitle="Base UI" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Bootstrap Toasts" />
					<CardBody>
						<div class="live-preview">
							<Row class="g-3">
								<Col xxl={6}>
									<h5 class="fs-14 mb-3">Default Toast</h5>
									<div class="p-3 my-2 rounded">
										<Toast isOpen={toast1}>
											<ToastHeader
												toggle={() =>
													(toast1 = !toast1)}
											>
												<img
													src={logosm}
													class="rounded me-2"
													alt="..."
													height="20"
												/>
												<span
													class="fw-semibold me-auto"
													>Velzon</span
												>
												<small
													style="margin-left: 140px"
													>06 mins ago</small
												>
											</ToastHeader>
											<ToastBody
												>Hello, world! This is a toast
												message.</ToastBody
											>
										</Toast>
									</div>
									<div class="mt-4">
										<h5 class="fs-14">Translucent</h5>
										<p class="text-muted">
											Toasts are slightly translucent,
											too, so they blend over whatever
											they might appear over.
										</p>

										<div class="p-3 bg-light">
											<Toast isOpen={toast2}>
												<ToastHeader
													toggle={() =>
														(toast2 = !toast2)}
												>
													<img
														src={logosm}
														class="rounded me-2"
														alt="..."
														height="20"
													/>
													<span
														class="fw-semibold me-auto"
														>Velzon</span
													>
													<small
														style="margin-left: 150px"
														>11 mins ago</small
													>
												</ToastHeader>
												<ToastBody
													>Hello, world! This is a
													toast message.</ToastBody
												>
											</Toast>
										</div>
									</div>
								</Col>
								<Col xxl={6}>
									<div>
										<h5 class="fs-14">Stacking</h5>
										<p class="text-muted">
											When you have multiple toasts, we
											default to vertically stacking them
											in a readable manner.
										</p>

										<div class="p-3 bg-light">
											<Toast isOpen={toast3}>
												<ToastHeader
													toggle={() =>
														(toast3 = !toast3)}
												>
													<img
														src={logosm}
														class="rounded me-2"
														alt="..."
														height="20"
													/>
													<span
														class="fw-semibold me-auto"
														>Velzon</span
													>
													<small
														style="margin-left: 165px"
														>Just now</small
													>
												</ToastHeader>
												<ToastBody
													>See? Just like this.</ToastBody
												>
											</Toast>

											<Toast isOpen={toast4}>
												<ToastHeader
													toggle={() =>
														(toast4 = !toast4)}
												>
													<img
														src={logosm}
														class="rounded me-2"
														alt="..."
														height="20"
													/>
													<span
														class="fw-semibold me-auto"
														>Velzon</span
													>
													<small
														style="margin-left: 130px"
														>2 seconds ago</small
													>
												</ToastHeader>
												<ToastBody
													>Heads up, toasts will stack
													automatically</ToastBody
												>
											</Toast>
										</div>
									</div>
								</Col>
							</Row>

							<div class="mt-5">
								<h5 class="fs-14">Placement</h5>
								<Row class="g-3">
									<Col xxl={6}>
										<div>
											<p class="text-muted">
												Place toasts with custom CSS as
												you need them. The top right is
												often used for notifications, as
												is the top middle. If you’re
												only ever going to show one
												toast at a time, put the
												positioning styles right on the <code
													>.toast</code
												>.
											</p>
											<div class="bg-light"
												style="position: relative; min-height: 200px"
											>
												<Toast
													isOpen={toast5}
													style="position: absolute; top: 16px; right: 16px"
												>
													<ToastHeader
														toggle={() =>
															(toast5 = !toast5)}
													>
														<img
															src={logosm}
															class="rounded me-2"
															alt="..."
															height="20"
														/>
														<span
															class="fw-semibold me-auto"
															>Velzon</span
														>
														<small
															style="margin-left: 140px"
															>06 mins ago</small
														>
													</ToastHeader>
													<ToastBody
														>Hello, world! This is a
														toast message.</ToastBody
													>
												</Toast>
											</div>
										</div>
									</Col>

									<Col xxl={6}>
										<div>
											<p class="text-muted">
												You can also get fancy with
												flexbox utilities to align
												toasts horizontally and/or
												vertically.
											</p>
											<div class="bg-light d-flex justify-content-center align-items-center"
												style="height: 200px"
											>
												<Toast isOpen={toast6}>
													<ToastHeader
														toggle={() =>
															(toast6 = !toast6)}
													>
														<img
															src={logosm}
															class="rounded me-2"
															alt="..."
															height="20"
														/>
														<span
															class="fw-semibold me-auto"
															>Velzon</span
														>
														<small
															style="margin-left: 150px"
															>11 mins ago</small
														>
													</ToastHeader>
													<ToastBody
														>Hello, world! This is a
														toast message.</ToastBody
													>
												</Toast>
											</div>
										</div>
									</Col>
								</Row>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={bootstrapToastsCode}
								id="bootstrapToastsCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Toast Placement" />
					<CardBody>
						<p class="text-muted">Various example of <code>toast placement</code>.</p>
						<div class="live-preview">
							<Form>
								<div class="mb-3">
									<select class="form-select mt-2" on:change={(e) => setPosition(e.currentTarget.value)}>
										<option value="" defaultValue>Select a position...</option>
										<option value="top-0 start-0">Top left</option>
										<option value="top-0 start-50 translate-middle-x">Top center</option>
										<option value="top-0 end-0">Top right</option>
										<option value="top-50 start-0 translate-middle-y">Middle left</option>
										<option value="top-50 start-50 translate-middle">Middle center</option>
										<option value="top-50 end-0 translate-middle-y">Middle right</option>
										<option value="bottom-0 start-0">Bottom left</option>
										<option value="bottom-0 start-50 translate-middle-x">Bottom center</option>
										<option value="bottom-0 end-0">Bottom right</option>
									</select>
								</div>
							</Form>
							<div aria-live="polite" aria-atomic="true" class="bd-example bg-light position-relative" style="min-height: 300px">
								<div class={"toast-container position-absolute p-3 " + position} id="toastPlacement">
									<Toast isOpen={toast11}>
										<ToastHeader toggle={() =>
											(toast11 = !toast11)}>
											<img src={logosm} class="rounded me-2"
												alt="..." height="20" />
											<strong class="me-auto">Velzon</strong>
											<small style="margin-left: 150px">11 mins ago</small>
										</ToastHeader>
										<ToastBody>
											Hello, world! This is a toast message.
										</ToastBody>
									</Toast>
								</div>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={toastPlacementCode}
								id="toastPlacementCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Bordered with Icon Toast" />
					<CardBody>
						<p class="text-muted">
							Use <code>toast-border-</code> with below-mentioned color
							variation to set a toast with border and icon.
						</p>
						<div class="live-preview">
							<div class="position-relative">
								<div class="hstack flex-wrap gap-2">
									<Button
										class="btn btn-primary"
										id="borderedToast1Btn"
										on:click={() => (toast7 = !toast7)}
										>Primary Toast</Button
									>
									<Button
										class="btn btn-success"
										id="borderedToast2Btn"
										on:click={() => (toast8 = !toast8)}
										>Success Toast</Button
									>
									<Button
										class="btn btn-warning"
										id="borderedTost3Btn"
										on:click={() => (toast9 = !toast9)}
										>Warning Toast</Button
									>
									<Button
										class="btn btn-danger"
										id="borderedToast4Btn"
										on:click={() => (toast10 = !toast10)}
										>Danger Toast</Button
									>
								</div>

								<div style="z-index: 11">
									<Toast
										isOpen={toast7}
										id="borderedToast1"
										class="toast-border-primary overflow-hidden mt-3"
									>
										<ToastBody>
											<div class="d-flex align-items-center"
											>
												<div class="flex-shrink-0 me-2">
													<i
														class="ri-user-smile-line align-middle"
													/>
												</div>
												<div class="flex-grow-1">
													<h6 class="mb-0">
														Your application was
														successfully sent.
													</h6>
												</div>
											</div>
										</ToastBody>
									</Toast>
								</div>

								<div style="z-index: 11">
									<Toast
										isOpen={toast8}
										id="borderedToast2"
										class="toast-border-success overflow-hidden mt-3"
									>
										<ToastBody>
											<div class="d-flex align-items-center"
											>
												<div class="flex-shrink-0 me-2">
													<i
														class="ri-checkbox-circle-fill align-middle"
													/>
												</div>
												<div class="flex-grow-1">
													<h6 class="mb-0">
														Yey! Everything worked!
													</h6>
												</div>
											</div>
										</ToastBody>
									</Toast>
								</div>

								<div style="z-index: 11">
									<Toast
										isOpen={toast9}
										id="borderedToast3"
										class="toast-border-info overflow-hidden mt-3"
									>
										<ToastBody>
											<div class="d-flex align-items-center"
											>
												<div class="flex-shrink-0 me-2">
													<i
														class="ri-notification-off-line align-middle"
													/>
												</div>
												<div class="flex-grow-1">
													<h6 class="mb-0">
														Something went wrong,
														try again.
													</h6>
												</div>
											</div>
										</ToastBody>
									</Toast>
								</div>
								<div style="z-index: 11">
									<Toast
										isOpen={toast10}
										id="borderedToast4"
										class="toast-border-danger overflow-hidden mt-3"
									>
										<ToastBody>
											<div class="d-flex align-items-center"
											>
												<div class="flex-shrink-0 me-2">
													<i
														class="ri-alert-line align-middle"
													/>
												</div>
												<div class="flex-grow-1">
													<h6 class="mb-0">
														Something is very wrong! <Link
															href={null}
															class="text-decoration-underline"
															>See detailed
															report.</Link
														>
													</h6>
												</div>
											</div>
										</ToastBody>
									</Toast>
								</div>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={borderIconCode}
								id="borderIconCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Toastify JS" />
					<CardBody>
						<div class="live-preview">
							<div class="hstack flex-wrap gap-2">
								<Button
									color="light"
									class="w-xs"
									on:click={defaultnotify}>Default</Button
								>
								<Button
									color="light"
									class="w-xs"
									on:click={successnotify}>Success</Button
								>
								<Button
									color="light"
									class="w-xs"
									on:click={warningnotify}>Warning</Button
								>
								<Button
									color="light"
									class="w-xs"
									on:click={errornotify}>Error</Button
								>
								<ToastContainer let:data>
									<BootstrapToast {data} />
								</ToastContainer>
							</div>
							<div class="mt-4 pt-2">
								<h5 class="fs-14 mb-3">Display Position</h5>
								<div class="hstack flex-wrap gap-2">
									<Button
										color="light"
										class="w-xs"
										on:click={topleftnotify}
										>Top Left</Button
									>
									<Button
										color="light"
										class="w-xs"
										on:click={topcenternotify}
										>Top Center</Button
									>
									<Button
										color="light"
										class="w-xs"
										on:click={toprightnotify}
										>Top Right</Button
									>
									<Button
										color="light"
										class="w-xs"
										on:click={bottomleftnotify}
										>Bottom Left</Button
									>
									<Button
										color="light"
										class="w-xs"
										on:click={bottomcenternotify}
										>Bottom Center</Button
									>
									<Button
										color="light"
										class="w-xs"
										on:click={bottomrightnotify}
										>Bottom Right</Button
									>
								</div>
							</div>

							<Row class="mt-3">
								<Col lg={4}>
									<div class="mt-4">
										<h5 class="fs-14 mb-3">
											Offset Position
										</h5>
										<div class="d-flex align-items-center flex-wrap gap-2"
										>
											<Button
												color="light"
												class="w-xs"
												on:click={offsetnotify}
												>Click Me</Button
											>
										</div>
									</div>
								</Col>
								<Col lg={4}>
									<div class="mt-4">
										<h5 class="fs-14 mb-3">
											Close icon Display
										</h5>
										<div class="d-flex align-items-center flex-wrap gap-2"
										>
											<Button
												color="light"
												class="w-xs"
												on:click={closeiconnotify}
												>Click Me</Button
											>
										</div>
									</div>
								</Col>
								<Col lg={4}>
									<div class="mt-4">
										<h5 class="fs-14 mb-3">Duration</h5>
										<div class="d-flex align-items-center flex-wrap gap-2"
										>
											<Button
												color="light"
												class="w-xs"
												on:click={durationnotify}
												>Click Me</Button
											>
										</div>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={toastifyCode}
								id="toastifyCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
