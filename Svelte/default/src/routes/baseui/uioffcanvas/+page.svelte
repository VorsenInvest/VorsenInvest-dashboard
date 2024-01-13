<script>
	import {
		Button,
		Card,
		CardBody,
		Col,
		Container,
		Offcanvas,
		OffcanvasBody,
		Row,
		Tooltip,
	} from "sveltestrap";

	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";

	import avatar1 from "../../../assets/images/users/avatar-1.jpg";
	import avatar2 from "../../../assets/images/users/avatar-2.jpg";
	import avatar3 from "../../../assets/images/users/avatar-3.jpg";
	import avatar4 from "../../../assets/images/users/avatar-4.jpg";
	import avatar6 from "../../../assets/images/users/avatar-6.jpg";
	import avatar7 from "../../../assets/images/users/avatar-7.jpg";
	import avatar8 from "../../../assets/images/users/avatar-8.jpg";
	import img2 from "../../../assets/images/small/img-2.jpg";
	import img3 from "../../../assets/images/small/img-3.jpg";
	import img4 from "../../../assets/images/small/img-4.jpg";
	import img9 from "../../../assets/images/small/img-9.jpg";
	import img10 from "../../../assets/images/small/img-10.jpg";
	import img11 from "../../../assets/images/small/img-11.jpg";
	import img12 from "../../../assets/images/small/img-12.jpg";

	let open = false;
	const toggleDefultCanvas = () => (open = !open);

	let isTop = false;
	const toggleTopCanvas = () => (isTop = !isTop);

	let isRight = false;
	const toggleRightCanvas = () => (isRight = !isRight);

	let isBottom = false;
	const toggleBottomCanvas = () => (isBottom = !isBottom);

	let isLeft = false;
	const toggleLeftCanvas = () => (isLeft = !isLeft);

	let isEnableScroll = false;
	const toggleEnableScroll = () => (isEnableScroll = !isEnableScroll);

	let isBackdrop = false;
	const toggleBackdrop = () => (isBackdrop = !isBackdrop);

	let isScrollBackDrop = false;
	const toggleScrollBackDrop = () => (isScrollBackDrop = !isScrollBackDrop);

	// Default Offcanvas

	const defaultOffcanvasCode = `
<!-- Base Examples -->
<Offcanvas
	isOpen={open}
	toggle={toggleDefultCanvas}
	class="offcanvas-p-0"
	id="offcanvasExample"
	header="Recent Acitivity"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div data-simplebar style="height: calc(100vh - 112px);">
			<div class="acitivity-timeline p-4">
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar1}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Oliver Phillips <span
								class="badge bg-primary-subtle text-primary align-middle"
								>New</span>
						</h6>
						<p class="text-muted mb-2">
							We talked about a project on linkedin.
						</p>
						<small class="mb-0 text-muted">Today</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0 avatar-xs acitivity-avatar">
						<div class="avatar-title bg-success-subtle text-success rounded-circle"
						>
							N
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Nancy Martino <span
								class="badge bg-secondary-subtle text-secondary align-middle"
								>In Progress</span>
						</h6>
						<p class="text-muted mb-2">
							<i class="ri-file-text-line align-middle ms-2" /> Create
							new project Buildng product
						</p>
						<div class="avatar-group mb-2">
							<Link
								href=""
								class="avatar-group-item"
								id="Christi">
								<img
									src={avatar4}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Christi"
								>Christi</Tooltip>
							<Tooltip placement="top" target="Frank"
								>Frank Hook Ruby</Tooltip>
							<Tooltip placement="top" target="more">more</Tooltip
							>

							<Link href="" class="avatar-group-item" id="Frank">
								<img
									src={avatar3}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Frank"
								>Frank Hook</Tooltip>

							<Link href="" class="avatar-group-item" id="Ruby">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle bg-light text-primary"
									>
										R
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="Ruby">Ruby</Tooltip>

							<Link href="" class="avatar-group-item" id="more">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle">
										2+
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="more">more</Tooltip>
						</div>
						<small class="mb-0 text-muted">Yesterday</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Natasha Carey <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span>
						</h6>
						<p class="text-muted mb-2">
							Adding a new event with attachments
						</p>
						<Row class="border border-dashed gx-2 p-2 mb-2">
							<Col class="col-4">
								<img
									src={img2}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img3}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img4}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
						</Row>
						<small class="mb-0 text-muted">25 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Bethany Johnson</h6>
						<p class="text-muted mb-2">
							added a new member to velzon dashboard
						</p>
						<small class="mb-0 text-muted">19 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div class="avatar-title rounded-circle bg-danger-subtle text-danger">
								<i class="ri-shopping-bag-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Your order is placed <span
								class="badge bg-danger-subtle text-danger align-middle ms-1"
								>Out of Delivery</span>
						</h6>
						<p class="text-muted mb-2">
							These customers can rest assured their order has
							been placed.
						</p>
						<small class="mb-0 text-muted">16 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar7}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Lewis Pratt</h6>
						<p class="text-muted mb-2">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic.
						</p>
						<small class="mb-0 text-muted">22 Oct</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div class="avatar-title rounded-circle bg-info-subtle text-info">
								<i class="ri-line-chart-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Monthly sales report</h6>
						<p class="text-muted mb-2">
							<span class="text-danger">2 days left</span>
							notification to submit the monthly sales report. <Link
								href=""
								class="link-warning text-decoration-underline"
								>Reports Builder</Link>
						</p>
						<small class="mb-0 text-muted">15 Oct</small>
					</div>
				</div>
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							New ticket received <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span>
						</h6>
						<p class="text-muted mb-2">
							User <span class="text-secondary">Erica245</span> submitted
							a ticket.
						</p>
						<small class="mb-0 text-muted">26 Aug</small>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>
<Link
	href=""
	class="btn btn-secondary"
	on:click={toggleDefultCanvas}
>
	Link with href
</Link>
<Button
	color="secondary"
	on:click={toggleDefultCanvas}
	>Button with target</Button
>
`;

	// Placement Offcanvas
	const placementOffcanvasCode = `
<!-- Placement Offcanvas -->
<Offcanvas
	isOpen={isTop}
	placement="top"
	toggle={toggleTopCanvas}
	id="offcanvasTop"
	header="Gallery"
	class="offcanvas-p-0"
	style="min-height: 46vh"
>
	<OffcanvasBody class="p-4">
		<Row class="gallery-light">
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box light mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img12}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									A mix of friends and strangers heading off
									to find an adventure.
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Erica Kernan</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 3.4K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 1.3K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box light mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img9}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Dramatic clouds at the Golden Gate Bridge
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Ron Mackie</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 5.1K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 4.7K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img11}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Cycling in the countryside
								</h5>
							</div>
						</Link>
					</div>

					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Nancy Martino</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 3.2K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 1.1K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6} class="d-md-none d-xl-block">
				<Card class="gallery-box mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img10}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Fun day at the Hill Station
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Henry Baird</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 632
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 95
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
		</Row>
	</OffcanvasBody>
</Offcanvas>
<Offcanvas
	isOpen={isRight}
	placement="end"
	toggle={toggleRightCanvas}
	id="offcanvasRight"
	header="Recent Acitivity"
	class="offcanvas-p-0"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div data-simplebar style="height: calc(100vh - 112px);">
			<div class="acitivity-timeline p-4">
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar1}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Oliver Phillips <span
								class="badge bg-primary-subtle text-primary align-middle"
								>New</span>
						</h6>
						<p class="text-muted mb-2">
							We talked about a project on linkedin.
						</p>
						<small class="mb-0 text-muted">Today</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0 avatar-xs acitivity-avatar">
						<div class="avatar-title bg-success-subtle text-success rounded-circle"
						>
							N
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Nancy Martino <span
								class="badge bg-secondary-subtle text-secondary align-middle"
								>In Progress</span>
						</h6>
						<p class="text-muted mb-2">
							<i class="ri-file-text-line align-middle ms-2" /> Create
							new project Buildng product
						</p>
						<div class="avatar-group mb-2">
							<Link
								href=""
								class="avatar-group-item"
								id="Christi">
								<img
									src={avatar4}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Christi"
								>Christi</Tooltip>
							<Tooltip placement="top" target="Frank"
								>Frank Hook Ruby</Tooltip>
							<Tooltip placement="top" target="more">more</Tooltip
							>
							<Link href="" class="avatar-group-item" id="Frank">
								<img
									src={avatar3}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Frank"
								>Frank Hook</Tooltip>

							<Link href="" class="avatar-group-item" id="Ruby">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle bg-light text-primary"
									>
										R
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="Ruby">Ruby</Tooltip>

							<Link href="" class="avatar-group-item" id="more">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle">
										2+
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="more">more</Tooltip>
						</div>
						<small class="mb-0 text-muted">Yesterday</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Natasha Carey <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span>
						</h6>
						<p class="text-muted mb-2">
							Adding a new event with attachments
						</p>
						<div class="row border border-dashed gx-2 p-2 mb-2">
							<Col class="col-4">
								<img
									src={img2}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img3}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img4}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
						</div>
						<small class="mb-0 text-muted">25 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Bethany Johnson</h6>
						<p class="text-muted mb-2">
							added a new member to velzon dashboard
						</p>
						<small class="mb-0 text-muted">19 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div class="avatar-title rounded-circle bg-danger-subtle text-danger">
								<i class="ri-shopping-bag-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Your order is placed <span
								class="badge bg-danger-subtle text-danger align-middle ms-1"
								>Out of Delivery</span>
						</h6>
						<p class="text-muted mb-2">
							These customers can rest assured their order has
							been placed.
						</p>
						<small class="mb-0 text-muted">16 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar7}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Lewis Pratt</h6>
						<p class="text-muted mb-2">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic.
						</p>
						<small class="mb-0 text-muted">22 Oct</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div class="avatar-title rounded-circle bg-info-subtle text-info">
								<i class="ri-line-chart-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Monthly sales report</h6>
						<p class="text-muted mb-2">
							<span class="text-danger">2 days left</span>
							notification to submit the monthly sales report. <Link
								href=""
								class="link-warning text-decoration-underline"
								>Reports Builder</Link>
						</p>
						<small class="mb-0 text-muted">15 Oct</small>
					</div>
				</div>
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							New ticket received <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span>
						</h6>
						<p class="text-muted mb-2">
							User <span class="text-secondary">Erica245</span> submitted
							a ticket.
						</p>
						<small class="mb-0 text-muted">26 Aug</small>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>

<Offcanvas
	isOpen={isBottom}
	placement="bottom"
	toggle={toggleBottomCanvas}
	id="offcanvasBottom"
	header="Gallery"
	class="offcanvas-p-0"
	style="min-height: 46vh"
>
	<OffcanvasBody class="p-4">
		<Row class="gallery-light">
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box light mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img12}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									A mix of friends and strangers heading off
									to find an adventure.
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Erica Kernan</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 3.4K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 1.3K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box light mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img9}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Dramatic clouds at the Golden Gate Bridge
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Ron Mackie</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 5.1K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 4.7K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img11}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Cycling in the countryside
								</h5>
							</div>
						</Link>
					</div>

					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Nancy Martino</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 5.1K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 4.7K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6} class="d-md-none d-xl-block">
				<Card class="gallery-box mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img10}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Fun day at the Hill Station
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Henry Baird</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 632
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 95
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
		</Row>
	</OffcanvasBody>
</Offcanvas>

<Offcanvas
	isOpen={isLeft}
	placement="start"
	header="Recent Acitivity"
	class="offcanvas-p-0"
	toggle={toggleLeftCanvas}
	id="offcanvasLeft"
>
	<OffcanvasBody>
		<div data-simplebar style="height: calc(100vh - 112px);">
			<div class="acitivity-timeline p-4">
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar1}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Oliver Phillips <span
								class="badge bg-primary-subtle text-primary align-middle"
								>New</span>
						</h6>
						<p class="text-muted mb-2">
							We talked about a project on linkedin.
						</p>
						<small class="mb-0 text-muted">Today</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0 avatar-xs acitivity-avatar">
						<div class="avatar-title bg-success-subtle text-success rounded-circle"
						>
							N
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Nancy Martino <span
								class="badge bg-secondary-subtle text-secondary align-middle"
								>In Progress</span>
						</h6>
						<p class="text-muted mb-2">
							<i class="ri-file-text-line align-middle ms-2" /> Create
							new project Buildng product
						</p>
						<div class="avatar-group mb-2">
							<Link
								href=""
								class="avatar-group-item"
								id="Christi">
								<img
									src={avatar4}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Christi"
								>Christi</Tooltip>

							<Link href="" class="avatar-group-item" id="Frank">
								<img
									src={avatar3}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Frank"
								>Frank Hook</Tooltip>

							<Link href="" class="avatar-group-item" id="Ruby">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle bg-light text-primary"
									>
										R
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="Ruby">Ruby</Tooltip>

							<Link href="" class="avatar-group-item" id="more">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle">
										2+
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="more">more</Tooltip>
						</div>
						<small class="mb-0 text-muted">Yesterday</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Natasha Carey <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span>
						</h6>
						<p class="text-muted mb-2">
							Adding a new event with attachments
						</p>
						<div class="row border border-dashed gx-2 p-2 mb-2">
							<Col class="col-4">
								<img
									src={img2}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img3}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img4}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
						</div>
						<small class="mb-0 text-muted">25 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Bethany Johnson</h6>
						<p class="text-muted mb-2">
							added a new member to velzon dashboard
						</p>
						<small class="mb-0 text-muted">19 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div class="avatar-title rounded-circle bg-danger-subtle text-danger">
								<i class="ri-shopping-bag-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Your order is placed <span
								class="badge bg-danger-subtle text-danger align-middle ms-1"
								>Out of Delivery</span>
						</h6>
						<p class="text-muted mb-2">
							These customers can rest assured their order has
							been placed.
						</p>
						<small class="mb-0 text-muted">16 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar7}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Lewis Pratt</h6>
						<p class="text-muted mb-2">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic.
						</p>
						<small class="mb-0 text-muted">22 Oct</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div class="avatar-title rounded-circle bg-info-subtle text-info">
								<i class="ri-line-chart-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Monthly sales report</h6>
						<p class="text-muted mb-2">
							<span class="text-danger">2 days left</span>
							notification to submit the monthly sales report. <Link
								href=""
								class="link-warning text-decoration-underline"
								>Reports Builder</Link>
						</p>
						<small class="mb-0 text-muted">15 Oct</small>
					</div>
				</div>
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							New ticket received <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span>
						</h6>
						<p class="text-muted mb-2">
							User <span class="text-secondary">Erica245</span> submitted
							a ticket.
						</p>
						<small class="mb-0 text-muted">26 Aug</small>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>
<Button
	color="primary"
	on:click={toggleTopCanvas}
	>Toggle Top Offcanvas</Button
>
<Button
	color="secondary"
	on:click={toggleRightCanvas}
	>Toggle Right Offcanvas</Button
>
<Button
	color="success"
	on:click={toggleBottomCanvas}
	>Toggle Bottom Offcanvas</Button
>
<Button
	color="danger"
	on:click={toggleLeftCanvas}
	>Toggle Left Offcanvas</Button
>
`;

	// Backdrop Offcanvas

	const backdropOffcanvasCode = `
<!-- Backdrop Offcanvas -->
<Offcanvas
	isOpen={isEnableScroll}
	scrollable
	backdrop={false}
	header="Customer Acitivity"
	class="offcanvas-p-0"
	toggle={toggleEnableScroll}
	id="offcanvasScrolling"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div>
			<div data-simplebar style="height: calc(100vh - 112px);">
				<div class="acitivity-timeline p-4">
					<div class="acitivity-item d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar1}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Oliver Phillips <span
									class="badge bg-primary-subtle text-primary align-middle"
									>New</span
								>
							</h6>
							<p class="text-muted mb-2">
								We talked about a project on linkedin.
							</p>
							<small class="mb-0 text-muted">Today</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0 avatar-xs acitivity-avatar">
							<div class="avatar-title bg-success-subtle text-success rounded-circle">
								N
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Nancy Martino <span
									class="badge bg-secondary-subtle text-secondary align-middle"
									>In Progress</span
								>
							</h6>
							<p class="text-muted mb-2">
								<i
									class="ri-file-text-line align-middle ms-2"
								/> Create new project Buildng product
							</p>
							<div class="avatar-group mb-2">
								<Link
									href=""
									class="avatar-group-item"
									id="Christi"
								>
									<img
										src={avatar4}
										alt=""
										class="rounded-circle avatar-xs"
									/>
								</Link>
								<Tooltip placement="top" target="Christi"
									>Christi</Tooltip
								>
								<Link
									href=""
									class="avatar-group-item"
									id="Frank"
								>
									<img
										src={avatar3}
										alt=""
										class="rounded-circle avatar-xs"
									/>
								</Link>
								<Tooltip placement="top" target="Frank"
									>Frank Hook</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									id="Ruby"
								>
									<div class="avatar-xs">
										<div class="avatar-title rounded-circle bg-light text-primary"
										>
											R
										</div>
									</div>
								</Link>
								<Tooltip placement="top" target="Ruby"
									>Ruby</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									id="more"
								>
									<div class="avatar-xs">
										<div class="avatar-title rounded-circle"
										>
											2+
										</div>
									</div>
								</Link>
								<Tooltip placement="top" target="more"
									>more</Tooltip
								>
							</div>
							<small class="mb-0 text-muted">Yesterday</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar2}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Natasha Carey <span
									class="badge bg-success-subtle text-success align-middle"
									>Completed</span
								>
							</h6>
							<p class="text-muted mb-2">
								Adding a new event with attachments
							</p>
							<div class="row border border-dashed gx-2 p-2 mb-2">
								<Col class="col-4">
									<img
										src={img2}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
								<Col class="col-4">
									<img
										src={img3}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
								<Col class="col-4">
									<img
										src={img4}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
							</div>
							<small class="mb-0 text-muted">25 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar6}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Bethany Johnson</h6>
							<p class="text-muted mb-2">
								added a new member to velzon dashboard
							</p>
							<small class="mb-0 text-muted">19 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<div class="avatar-xs acitivity-avatar">
								<div class="avatar-title rounded-circle bg-danger-subtle text-danger"
								>
									<i class="ri-shopping-bag-line" />
								</div>
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Your order is placed <span
									class="badge bg-danger-subtle text-danger align-middle ms-1"
									>Out of Delivery</span
								>
							</h6>
							<p class="text-muted mb-2">
								These customers can rest assured their order has
								been placed.
							</p>
							<small class="mb-0 text-muted">16 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar7}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Lewis Pratt</h6>
							<p class="text-muted mb-2">
								They all have something to say beyond the words
								on the page. They can come across as casual or
								neutral, exotic or graphic.
							</p>
							<small class="mb-0 text-muted">22 Oct</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<div class="avatar-xs acitivity-avatar">
								<div class="avatar-title rounded-circle bg-info-subtle text-info"
								>
									<i class="ri-line-chart-line" />
								</div>
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Monthly sales report</h6>
							<p class="text-muted mb-2">
								<span class="text-danger">2 days left</span>
								notification to submit the monthly sales report. <Link
									href=""
									class="link-warning text-decoration-underline"
									>Reports Builder</Link
								>
							</p>
							<small class="mb-0 text-muted">15 Oct</small>
						</div>
					</div>
					<div class="acitivity-item d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar8}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								New ticket received <span
									class="badge bg-success-subtle text-success align-middle"
									>Completed</span
								>
							</h6>
							<p class="text-muted mb-2">
								User <span class="text-secondary">Erica245</span
								> submitted a ticket.
							</p>
							<small class="mb-0 text-muted">26 Aug</small>
						</div>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>
<Button
	class="btn btn-light"
	on:click={toggleEnableScroll}
	>Enable Body Scrolling</Button
>

<Offcanvas
	isOpen={isBackdrop}
	toggle={toggleBackdrop}
	id="offcanvasWithBackdrop"
	header="Customer Acitivity"
	class="offcanvas-p-0"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div>
			<div data-simplebar style="height: calc(100vh - 112px);">
				<div class="acitivity-timeline p-4">
					<div class="acitivity-item d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar1}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Oliver Phillips <span
									class="badge bg-primary-subtle text-primary align-middle"
									>New</span
								>
							</h6>
							<p class="text-muted mb-2">
								We talked about a project on linkedin.
							</p>
							<small class="mb-0 text-muted">Today</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0 avatar-xs acitivity-avatar">
							<div class="avatar-title bg-success-subtle text-success rounded-circle">
								N
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Nancy Martino <span
									class="badge bg-secondary-subtle text-secondary align-middle"
									>In Progress</span
								>
							</h6>
							<p class="text-muted mb-2">
								<i
									class="ri-file-text-line align-middle ms-2"
								/> Create new project Buildng product
							</p>
							<div class="avatar-group mb-2">
								<Link
									href=""
									class="avatar-group-item"
									title=""
									id="Christi"
								>
									<img
										src={avatar4}
										alt=""
										class="rounded-circle avatar-xs"
									/>
								</Link>
								<Tooltip placement="top" target="Christi"
									>Christi</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									title=""
									id="Frank"
								>
									<img
										src={avatar3}
										alt=""
										class="rounded-circle avatar-xs"
									/>
								</Link>
								<Tooltip placement="top" target="Frank"
									>Frank Hook</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									title=""
									id="Ruby"
								>
									<div class="avatar-xs">
										<div class="avatar-title rounded-circle bg-light text-primary"
										>
											R
										</div>
									</div>
								</Link>
								<Tooltip placement="top" target="Ruby"
									>Ruby</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									title=""
									id="more"
								>
									<div class="avatar-xs">
										<div class="avatar-title rounded-circle"
										>
											2+
										</div>
									</div>
								</Link>
								<Tooltip placement="top" target="more"
									>more</Tooltip
								>
							</div>
							<small class="mb-0 text-muted">Yesterday</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar2}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Natasha Carey <span
									class="badge bg-success-subtle text-success align-middle"
									>Completed</span
								>
							</h6>
							<p class="text-muted mb-2">
								Adding a new event with attachments
							</p>
							<div class="row border border-dashed gx-2 p-2 mb-2">
								<Col class="col-4">
									<img
										src={img2}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
								<Col class="col-4">
									<img
										src={img3}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
								<Col class="col-4">
									<img
										src={img4}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
							</div>
							<small class="mb-0 text-muted">25 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar6}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Bethany Johnson</h6>
							<p class="text-muted mb-2">
								added a new member to velzon dashboard
							</p>
							<small class="mb-0 text-muted">19 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<div class="avatar-xs acitivity-avatar">
								<div class="avatar-title rounded-circle bg-danger-subtle text-danger"
								>
									<i class="ri-shopping-bag-line" />
								</div>
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Your order is placed <span
									class="badge bg-danger-subtle text-danger align-middle ms-1"
									>Out of Delivery</span
								>
							</h6>
							<p class="text-muted mb-2">
								These customers can rest assured their order has
								been placed.
							</p>
							<small class="mb-0 text-muted">16 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar7}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Lewis Pratt</h6>
							<p class="text-muted mb-2">
								They all have something to say beyond the words
								on the page. They can come across as casual or
								neutral, exotic or graphic.
							</p>
							<small class="mb-0 text-muted">22 Oct</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<div class="avatar-xs acitivity-avatar">
								<div class="avatar-title rounded-circle bg-info-subtle text-info"
								>
									<i class="ri-line-chart-line" />
								</div>
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Monthly sales report</h6>
							<p class="text-muted mb-2">
								<span class="text-danger">2 days left</span>
								notification to submit the monthly sales report. <Link
									href=""
									class="link-warning text-decoration-underline"
									>Reports Builder</Link
								>
							</p>
							<small class="mb-0 text-muted">15 Oct</small>
						</div>
					</div>
					<div class="acitivity-item d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar8}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								New ticket received <span
									class="badge bg-success-subtle text-success align-middle"
									>Completed</span
								>
							</h6>
							<p class="text-muted mb-2">
								User <span class="text-secondary">Erica245</span
								> submitted a ticket.
							</p>
							<small class="mb-0 text-muted">26 Aug</small>
						</div>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>

<Button
	class="btn btn-light"
	on:click={toggleBackdrop}
	>Enable Backdrop (Default)</Button
>

<Offcanvas
	isOpen={isScrollBackDrop}
	scrollable
	toggle={toggleScrollBackDrop}
	header="Customer Acitivity"
	class="offcanvas-p-0"
	id="offcanvasWithBothOptions"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div data-simplebar style="height: calc(100vh - 112px);">
			<div class="acitivity-timeline p-4">
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar1}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Oliver Phillips <span
								class="badge bg-primary-subtle text-primary align-middle"
								>New</span>
						</h6>
						<p class="text-muted mb-2">
							We talked about a project on linkedin.
						</p>
						<small class="mb-0 text-muted">Today</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0 avatar-xs acitivity-avatar">
						<div class="avatar-title bg-success-subtle text-success rounded-circle"
						>
							N
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Nancy Martino <span
								class="badge bg-secondary-subtle text-secondary align-middle"
								>In Progress</span>
						</h6>
						<p class="text-muted mb-2">
							<i class="ri-file-text-line align-middle ms-2" /> Create
							new project Buildng product
						</p>
						<div class="avatar-group mb-2">
							<Link
								href=""
								class="avatar-group-item"
								id="Christi">
								<img
									src={avatar4}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Christi"
								>Christi</Tooltip>
							<Link href="" class="avatar-group-item" id="Frank">
								<img
									src={avatar3}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Frank"
								>Frank Hook</Tooltip>

							<Link href="" class="avatar-group-item" id="Ruby">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle bg-light text-primary"
									>
										R
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="Ruby">Ruby</Tooltip>

							<Link href="" class="avatar-group-item" id="more">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle">
										2+
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="more">more</Tooltip>
						</div>
						<small class="mb-0 text-muted">Yesterday</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Natasha Carey <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span>
						</h6>
						<p class="text-muted mb-2">
							Adding a new event with attachments
						</p>
						<div class="row border border-dashed gx-2 p-2 mb-2">
							<Col class="col-4">
								<img
									src={img2}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img3}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img4}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
						</div>
						<small class="mb-0 text-muted">25 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Bethany Johnson</h6>
						<p class="text-muted mb-2">
							added a new member to velzon dashboard
						</p>
						<small class="mb-0 text-muted">19 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div class="avatar-title rounded-circle bg-danger-subtle text-danger">
								<i class="ri-shopping-bag-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Your order is placed <span
								class="badge bg-danger-subtle text-danger align-middle ms-1"
								>Out of Delivery</span>
						</h6>
						<p class="text-muted mb-2">
							These customers can rest assured their order has
							been placed.
						</p>
						<small class="mb-0 text-muted">16 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar7}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Lewis Pratt</h6>
						<p class="text-muted mb-2">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic.
						</p>
						<small class="mb-0 text-muted">22 Oct</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div class="avatar-title rounded-circle bg-info-subtle text-info">
								<i class="ri-line-chart-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Monthly sales report</h6>
						<p class="text-muted mb-2">
							<span class="text-danger">2 days left</span>
							notification to submit the monthly sales report. <Link
								href=""
								class="link-warning text-decoration-underline"
								>Reports Builder</Link>
						</p>
						<small class="mb-0 text-muted">15 Oct</small>
					</div>
				</div>
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							New ticket received <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span>
						</h6>
						<p class="text-muted mb-2">
							User <span class="text-secondary">Erica245</span> submitted
							a ticket.
						</p>
						<small class="mb-0 text-muted">26 Aug</small>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>

<Button
	class="btn btn-light"
	on:click={toggleScrollBackDrop}
	>Enable Both Scrolling & Backdrop</Button
>
`;
</script>

<svelte:head>
	<title>Offcanvas | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Offcanvas" pageTitle="Base UI" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Default Offcanvas" />

					<CardBody>
						<p class="text-muted">
							Use the <code>offcanvas</code> class to set a default
							offcanvas.
						</p>
						<div class="live-preview">
							<div class="hstack flex-wrap gap-2">
								<Link
									href=""
									class="btn btn-secondary"
									on:click={toggleDefultCanvas}
								>
									Link with href
								</Link>
								<Button
									color="secondary"
									on:click={toggleDefultCanvas}
									>Button with target</Button
								>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={defaultOffcanvasCode}
								id="defaultOffcanvasCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Placement Offcanvas" />
					<CardBody>
						<p class="text-muted">
							Use <code>placement="start"</code> ,
							<code>placement="top"</code>,
							<code>placement="bottom"</code>, or
							<code>placement="end"</code>, to offcanvas attribute
							to set different Offcanvas Placement.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button
									color="primary"
									on:click={toggleTopCanvas}
									>Toggle Top Offcanvas</Button
								>
								<Button
									color="secondary"
									on:click={toggleRightCanvas}
									>Toggle Right Offcanvas</Button
								>
								<Button
									color="success"
									on:click={toggleBottomCanvas}
									>Toggle Bottom Offcanvas</Button
								>
								<Button
									color="danger"
									on:click={toggleLeftCanvas}
									>Toggle Left Offcanvas</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={placementOffcanvasCode}
								id="placementOffcanvasCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Backdrop Offcanvas" />
					<CardBody>
						<p class="text-muted">
							Here are the example of offcanvas with scrolling
							active and backdrop visible.
						</p>
						<div class="live-preview">
							<div class="d-flex flex-wrap gap-2">
								<Button
									class="btn btn-light"
									on:click={toggleEnableScroll}
									>Enable Body Scrolling</Button
								>
								<Button
									class="btn btn-light"
									on:click={toggleBackdrop}
									>Enable Backdrop (Default)</Button
								>
								<Button
									class="btn btn-light"
									on:click={toggleScrollBackDrop}
									>Enable Both Scrolling & Backdrop</Button
								>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={backdropOffcanvasCode}
								id="backdropOffcanvasCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>

<Offcanvas
	isOpen={open}
	toggle={toggleDefultCanvas}
	class="offcanvas-p-0"
	id="offcanvasExample"
	header="Recent Acitivity"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div data-simplebar style="height: calc(100vh - 112px);">
			<div class="acitivity-timeline p-4">
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar1}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Oliver Phillips <span
								class="badge bg-primary-subtle text-primary align-middle"
								>New</span
							>
						</h6>
						<p class="text-muted mb-2">
							We talked about a project on linkedin.
						</p>
						<small class="mb-0 text-muted">Today</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0 avatar-xs acitivity-avatar">
						<div
							class="avatar-title bg-success-subtle text-success rounded-circle"
						>
							N
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Nancy Martino <span
								class="badge bg-secondary-subtle text-secondary align-middle"
								>In Progress</span
							>
						</h6>
						<p class="text-muted mb-2">
							<i class="ri-file-text-line align-middle ms-2" /> Create
							new project Buildng product
						</p>
						<div class="avatar-group mb-2">
							<Link
								href=""
								class="avatar-group-item"
								id="Christi"
							>
								<img
									src={avatar4}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Christi"
								>Christi</Tooltip
							>
							<Tooltip placement="top" target="Frank"
								>Frank Hook Ruby</Tooltip
							>
							<Tooltip placement="top" target="more">more</Tooltip
							>

							<Link href="" class="avatar-group-item" id="Frank">
								<img
									src={avatar3}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Frank"
								>Frank Hook</Tooltip
							>

							<Link href="" class="avatar-group-item" id="Ruby">
								<div class="avatar-xs">
									<div
										class="avatar-title rounded-circle bg-light text-primary"
									>
										R
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="Ruby">Ruby</Tooltip
							>

							<Link href="" class="avatar-group-item" id="more">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle">
										2+
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="more">more</Tooltip
							>
						</div>
						<small class="mb-0 text-muted">Yesterday</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Natasha Carey <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span
							>
						</h6>
						<p class="text-muted mb-2">
							Adding a new event with attachments
						</p>
						<Row class="border border-dashed gx-2 p-2 mb-2">
							<Col class="col-4">
								<img
									src={img2}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img3}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img4}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
						</Row>
						<small class="mb-0 text-muted">25 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Bethany Johnson</h6>
						<p class="text-muted mb-2">
							added a new member to velzon dashboard
						</p>
						<small class="mb-0 text-muted">19 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div
								class="avatar-title rounded-circle bg-danger-subtle text-danger"
							>
								<i class="ri-shopping-bag-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Your order is placed <span
								class="badge bg-danger-subtle text-danger align-middle ms-1"
								>Out of Delivery</span
							>
						</h6>
						<p class="text-muted mb-2">
							These customers can rest assured their order has
							been placed.
						</p>
						<small class="mb-0 text-muted">16 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar7}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Lewis Pratt</h6>
						<p class="text-muted mb-2">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic.
						</p>
						<small class="mb-0 text-muted">22 Oct</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div
								class="avatar-title rounded-circle bg-info-subtle text-info"
							>
								<i class="ri-line-chart-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Monthly sales report</h6>
						<p class="text-muted mb-2">
							<span class="text-danger">2 days left</span>
							notification to submit the monthly sales report. <Link
								href=""
								class="link-warning text-decoration-underline"
								>Reports Builder</Link
							>
						</p>
						<small class="mb-0 text-muted">15 Oct</small>
					</div>
				</div>
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							New ticket received <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span
							>
						</h6>
						<p class="text-muted mb-2">
							User <span class="text-secondary">Erica245</span> submitted
							a ticket.
						</p>
						<small class="mb-0 text-muted">26 Aug</small>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>

<Offcanvas
	isOpen={isTop}
	placement="top"
	toggle={toggleTopCanvas}
	id="offcanvasTop"
	header="Gallery"
	class="offcanvas-p-0"
	style="min-height: 46vh"
>
	<OffcanvasBody class="p-4">
		<Row class="gallery-light">
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box light mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img12}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									A mix of friends and strangers heading off
									to find an adventure.
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Erica Kernan</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 3.4K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 1.3K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box light mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img9}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Dramatic clouds at the Golden Gate Bridge
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Ron Mackie</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 5.1K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 4.7K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img11}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Cycling in the countryside
								</h5>
							</div>
						</Link>
					</div>

					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Nancy Martino</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 3.2K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 1.1K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6} class="d-md-none d-xl-block">
				<Card class="gallery-box mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img10}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Fun day at the Hill Station
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Henry Baird</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 632
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 95
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
		</Row>
	</OffcanvasBody>
</Offcanvas>

<Offcanvas
	isOpen={isRight}
	placement="end"
	toggle={toggleRightCanvas}
	id="offcanvasRight"
	header="Recent Acitivity"
	class="offcanvas-p-0"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div data-simplebar style="height: calc(100vh - 112px);">
			<div class="acitivity-timeline p-4">
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar1}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Oliver Phillips <span
								class="badge bg-primary-subtle text-primary align-middle"
								>New</span
							>
						</h6>
						<p class="text-muted mb-2">
							We talked about a project on linkedin.
						</p>
						<small class="mb-0 text-muted">Today</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0 avatar-xs acitivity-avatar">
						<div
							class="avatar-title bg-success-subtle text-success rounded-circle"
						>
							N
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Nancy Martino <span
								class="badge bg-secondary-subtle text-secondary align-middle"
								>In Progress</span
							>
						</h6>
						<p class="text-muted mb-2">
							<i class="ri-file-text-line align-middle ms-2" /> Create
							new project Buildng product
						</p>
						<div class="avatar-group mb-2">
							<Link
								href=""
								class="avatar-group-item"
								id="Christi"
							>
								<img
									src={avatar4}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Christi"
								>Christi</Tooltip
							>
							<Tooltip placement="top" target="Frank"
								>Frank Hook Ruby</Tooltip
							>
							<Tooltip placement="top" target="more">more</Tooltip
							>
							<Link href="" class="avatar-group-item" id="Frank">
								<img
									src={avatar3}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Frank"
								>Frank Hook</Tooltip
							>

							<Link href="" class="avatar-group-item" id="Ruby">
								<div class="avatar-xs">
									<div
										class="avatar-title rounded-circle bg-light text-primary"
									>
										R
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="Ruby">Ruby</Tooltip
							>

							<Link href="" class="avatar-group-item" id="more">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle">
										2+
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="more">more</Tooltip
							>
						</div>
						<small class="mb-0 text-muted">Yesterday</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Natasha Carey <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span
							>
						</h6>
						<p class="text-muted mb-2">
							Adding a new event with attachments
						</p>
						<div class="row border border-dashed gx-2 p-2 mb-2">
							<Col class="col-4">
								<img
									src={img2}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img3}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img4}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
						</div>
						<small class="mb-0 text-muted">25 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Bethany Johnson</h6>
						<p class="text-muted mb-2">
							added a new member to velzon dashboard
						</p>
						<small class="mb-0 text-muted">19 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div
								class="avatar-title rounded-circle bg-danger-subtle text-danger"
							>
								<i class="ri-shopping-bag-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Your order is placed <span
								class="badge bg-danger-subtle text-danger align-middle ms-1"
								>Out of Delivery</span
							>
						</h6>
						<p class="text-muted mb-2">
							These customers can rest assured their order has
							been placed.
						</p>
						<small class="mb-0 text-muted">16 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar7}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Lewis Pratt</h6>
						<p class="text-muted mb-2">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic.
						</p>
						<small class="mb-0 text-muted">22 Oct</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div
								class="avatar-title rounded-circle bg-info-subtle text-info"
							>
								<i class="ri-line-chart-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Monthly sales report</h6>
						<p class="text-muted mb-2">
							<span class="text-danger">2 days left</span>
							notification to submit the monthly sales report. <Link
								href=""
								class="link-warning text-decoration-underline"
								>Reports Builder</Link
							>
						</p>
						<small class="mb-0 text-muted">15 Oct</small>
					</div>
				</div>
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							New ticket received <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span
							>
						</h6>
						<p class="text-muted mb-2">
							User <span class="text-secondary">Erica245</span> submitted
							a ticket.
						</p>
						<small class="mb-0 text-muted">26 Aug</small>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>

<Offcanvas
	isOpen={isBottom}
	placement="bottom"
	toggle={toggleBottomCanvas}
	id="offcanvasBottom"
	header="Gallery"
	class="offcanvas-p-0"
	style="min-height: 46vh"
>
	<OffcanvasBody class="p-4">
		<Row class="gallery-light">
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box light mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img12}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									A mix of friends and strangers heading off
									to find an adventure.
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Erica Kernan</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 3.4K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 1.3K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box light mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img9}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Dramatic clouds at the Golden Gate Bridge
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Ron Mackie</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 5.1K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 4.7K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6}>
				<Card class="gallery-box mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img11}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Cycling in the countryside
								</h5>
							</div>
						</Link>
					</div>

					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Nancy Martino</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 5.1K
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 4.7K
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
			<Col xl={3} lg={4} sm={6} class="d-md-none d-xl-block">
				<Card class="gallery-box mb-0">
					<div class="gallery-container">
						<Link href="" title="">
							<img
								class="gallery-img img-fluid mx-auto"
								src={img10}
								alt=""
							/>
							<div class="gallery-overlay">
								<h5 class="overlay-caption">
									Fun day at the Hill Station
								</h5>
							</div>
						</Link>
					</div>
					<div class="box-content">
						<div class="d-flex align-items-center mt-1">
							<div class="flex-grow-1 text-muted">
								by <Link href="" class="text-body text-truncate"
									>Henry Baird</Link
								>
							</div>
							<div class="flex-shrink-0">
								<div class="d-flex gap-3">
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-thumb-up-fill text-muted align-bottom me-1"
										/> 632
									</button>
									<button
										type="button"
										class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
									>
										<i
											class="ri-question-answer-fill text-muted align-bottom me-1"
										/> 95
									</button>
								</div>
							</div>
						</div>
					</div>
				</Card>
			</Col>
		</Row>
	</OffcanvasBody>
</Offcanvas>

<Offcanvas
	isOpen={isLeft}
	placement="start"
	header="Recent Acitivity"
	class="offcanvas-p-0"
	toggle={toggleLeftCanvas}
	id="offcanvasLeft"
>
	<OffcanvasBody>
		<div data-simplebar style="height: calc(100vh - 112px);">
			<div class="acitivity-timeline p-4">
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar1}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Oliver Phillips <span
								class="badge bg-primary-subtle text-primary align-middle"
								>New</span
							>
						</h6>
						<p class="text-muted mb-2">
							We talked about a project on linkedin.
						</p>
						<small class="mb-0 text-muted">Today</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0 avatar-xs acitivity-avatar">
						<div
							class="avatar-title bg-success-subtle text-success rounded-circle"
						>
							N
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Nancy Martino <span
								class="badge bg-secondary-subtle text-secondary align-middle"
								>In Progress</span
							>
						</h6>
						<p class="text-muted mb-2">
							<i class="ri-file-text-line align-middle ms-2" /> Create
							new project Buildng product
						</p>
						<div class="avatar-group mb-2">
							<Link
								href=""
								class="avatar-group-item"
								id="Christi"
							>
								<img
									src={avatar4}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Christi"
								>Christi</Tooltip
							>

							<Link href="" class="avatar-group-item" id="Frank">
								<img
									src={avatar3}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Frank"
								>Frank Hook</Tooltip
							>

							<Link href="" class="avatar-group-item" id="Ruby">
								<div class="avatar-xs">
									<div
										class="avatar-title rounded-circle bg-light text-primary"
									>
										R
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="Ruby">Ruby</Tooltip
							>

							<Link href="" class="avatar-group-item" id="more">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle">
										2+
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="more">more</Tooltip
							>
						</div>
						<small class="mb-0 text-muted">Yesterday</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Natasha Carey <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span
							>
						</h6>
						<p class="text-muted mb-2">
							Adding a new event with attachments
						</p>
						<div class="row border border-dashed gx-2 p-2 mb-2">
							<Col class="col-4">
								<img
									src={img2}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img3}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img4}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
						</div>
						<small class="mb-0 text-muted">25 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Bethany Johnson</h6>
						<p class="text-muted mb-2">
							added a new member to velzon dashboard
						</p>
						<small class="mb-0 text-muted">19 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div
								class="avatar-title rounded-circle bg-danger-subtle text-danger"
							>
								<i class="ri-shopping-bag-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Your order is placed <span
								class="badge bg-danger-subtle text-danger align-middle ms-1"
								>Out of Delivery</span
							>
						</h6>
						<p class="text-muted mb-2">
							These customers can rest assured their order has
							been placed.
						</p>
						<small class="mb-0 text-muted">16 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar7}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Lewis Pratt</h6>
						<p class="text-muted mb-2">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic.
						</p>
						<small class="mb-0 text-muted">22 Oct</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div
								class="avatar-title rounded-circle bg-info-subtle text-info"
							>
								<i class="ri-line-chart-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Monthly sales report</h6>
						<p class="text-muted mb-2">
							<span class="text-danger">2 days left</span>
							notification to submit the monthly sales report. <Link
								href=""
								class="link-warning text-decoration-underline"
								>Reports Builder</Link
							>
						</p>
						<small class="mb-0 text-muted">15 Oct</small>
					</div>
				</div>
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							New ticket received <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span
							>
						</h6>
						<p class="text-muted mb-2">
							User <span class="text-secondary">Erica245</span> submitted
							a ticket.
						</p>
						<small class="mb-0 text-muted">26 Aug</small>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>

<Offcanvas
	isOpen={isEnableScroll}
	scrollable
	backdrop={false}
	header="Customer Acitivity"
	class="offcanvas-p-0"
	toggle={toggleEnableScroll}
	id="offcanvasScrolling"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div>
			<div data-simplebar style="height: calc(100vh - 112px);">
				<div class="acitivity-timeline p-4">
					<div class="acitivity-item d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar1}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Oliver Phillips <span
									class="badge bg-primary-subtle text-primary align-middle"
									>New</span
								>
							</h6>
							<p class="text-muted mb-2">
								We talked about a project on linkedin.
							</p>
							<small class="mb-0 text-muted">Today</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0 avatar-xs acitivity-avatar">
							<div
								class="avatar-title bg-success-subtle text-success rounded-circle"
							>
								N
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Nancy Martino <span
									class="badge bg-secondary-subtle text-secondary align-middle"
									>In Progress</span
								>
							</h6>
							<p class="text-muted mb-2">
								<i
									class="ri-file-text-line align-middle ms-2"
								/> Create new project Buildng product
							</p>
							<div class="avatar-group mb-2">
								<Link
									href=""
									class="avatar-group-item"
									id="Christi"
								>
									<img
										src={avatar4}
										alt=""
										class="rounded-circle avatar-xs"
									/>
								</Link>
								<Tooltip placement="top" target="Christi"
									>Christi</Tooltip
								>
								<Link
									href=""
									class="avatar-group-item"
									id="Frank"
								>
									<img
										src={avatar3}
										alt=""
										class="rounded-circle avatar-xs"
									/>
								</Link>
								<Tooltip placement="top" target="Frank"
									>Frank Hook</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									id="Ruby"
								>
									<div class="avatar-xs">
										<div
											class="avatar-title rounded-circle bg-light text-primary"
										>
											R
										</div>
									</div>
								</Link>
								<Tooltip placement="top" target="Ruby"
									>Ruby</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									id="more"
								>
									<div class="avatar-xs">
										<div
											class="avatar-title rounded-circle"
										>
											2+
										</div>
									</div>
								</Link>
								<Tooltip placement="top" target="more"
									>more</Tooltip
								>
							</div>
							<small class="mb-0 text-muted">Yesterday</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar2}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Natasha Carey <span
									class="badge bg-success-subtle text-success align-middle"
									>Completed</span
								>
							</h6>
							<p class="text-muted mb-2">
								Adding a new event with attachments
							</p>
							<div class="row border border-dashed gx-2 p-2 mb-2">
								<Col class="col-4">
									<img
										src={img2}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
								<Col class="col-4">
									<img
										src={img3}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
								<Col class="col-4">
									<img
										src={img4}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
							</div>
							<small class="mb-0 text-muted">25 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar6}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Bethany Johnson</h6>
							<p class="text-muted mb-2">
								added a new member to velzon dashboard
							</p>
							<small class="mb-0 text-muted">19 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<div class="avatar-xs acitivity-avatar">
								<div
									class="avatar-title rounded-circle bg-danger-subtle text-danger"
								>
									<i class="ri-shopping-bag-line" />
								</div>
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Your order is placed <span
									class="badge bg-danger-subtle text-danger align-middle ms-1"
									>Out of Delivery</span
								>
							</h6>
							<p class="text-muted mb-2">
								These customers can rest assured their order has
								been placed.
							</p>
							<small class="mb-0 text-muted">16 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar7}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Lewis Pratt</h6>
							<p class="text-muted mb-2">
								They all have something to say beyond the words
								on the page. They can come across as casual or
								neutral, exotic or graphic.
							</p>
							<small class="mb-0 text-muted">22 Oct</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<div class="avatar-xs acitivity-avatar">
								<div
									class="avatar-title rounded-circle bg-info-subtle text-info"
								>
									<i class="ri-line-chart-line" />
								</div>
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Monthly sales report</h6>
							<p class="text-muted mb-2">
								<span class="text-danger">2 days left</span>
								notification to submit the monthly sales report.
								<Link
									href=""
									class="link-warning text-decoration-underline"
									>Reports Builder</Link
								>
							</p>
							<small class="mb-0 text-muted">15 Oct</small>
						</div>
					</div>
					<div class="acitivity-item d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar8}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								New ticket received <span
									class="badge bg-success-subtle text-success align-middle"
									>Completed</span
								>
							</h6>
							<p class="text-muted mb-2">
								User <span class="text-secondary">Erica245</span
								> submitted a ticket.
							</p>
							<small class="mb-0 text-muted">26 Aug</small>
						</div>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>

<Offcanvas
	isOpen={isBackdrop}
	toggle={toggleBackdrop}
	id="offcanvasWithBackdrop"
	header="Customer Acitivity"
	class="offcanvas-p-0"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div>
			<div data-simplebar style="height: calc(100vh - 112px);">
				<div class="acitivity-timeline p-4">
					<div class="acitivity-item d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar1}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Oliver Phillips <span
									class="badge bg-primary-subtle text-primary align-middle"
									>New</span
								>
							</h6>
							<p class="text-muted mb-2">
								We talked about a project on linkedin.
							</p>
							<small class="mb-0 text-muted">Today</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0 avatar-xs acitivity-avatar">
							<div
								class="avatar-title bg-success-subtle text-success rounded-circle"
							>
								N
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Nancy Martino <span
									class="badge bg-secondary-subtle text-secondary align-middle"
									>In Progress</span
								>
							</h6>
							<p class="text-muted mb-2">
								<i
									class="ri-file-text-line align-middle ms-2"
								/> Create new project Buildng product
							</p>
							<div class="avatar-group mb-2">
								<Link
									href=""
									class="avatar-group-item"
									title=""
									id="Christi"
								>
									<img
										src={avatar4}
										alt=""
										class="rounded-circle avatar-xs"
									/>
								</Link>
								<Tooltip placement="top" target="Christi"
									>Christi</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									title=""
									id="Frank"
								>
									<img
										src={avatar3}
										alt=""
										class="rounded-circle avatar-xs"
									/>
								</Link>
								<Tooltip placement="top" target="Frank"
									>Frank Hook</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									title=""
									id="Ruby"
								>
									<div class="avatar-xs">
										<div
											class="avatar-title rounded-circle bg-light text-primary"
										>
											R
										</div>
									</div>
								</Link>
								<Tooltip placement="top" target="Ruby"
									>Ruby</Tooltip
								>

								<Link
									href=""
									class="avatar-group-item"
									title=""
									id="more"
								>
									<div class="avatar-xs">
										<div
											class="avatar-title rounded-circle"
										>
											2+
										</div>
									</div>
								</Link>
								<Tooltip placement="top" target="more"
									>more</Tooltip
								>
							</div>
							<small class="mb-0 text-muted">Yesterday</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar2}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Natasha Carey <span
									class="badge bg-success-subtle text-success align-middle"
									>Completed</span
								>
							</h6>
							<p class="text-muted mb-2">
								Adding a new event with attachments
							</p>
							<div class="row border border-dashed gx-2 p-2 mb-2">
								<Col class="col-4">
									<img
										src={img2}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
								<Col class="col-4">
									<img
										src={img3}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
								<Col class="col-4">
									<img
										src={img4}
										alt=""
										class="img-fluid rounded"
									/>
								</Col>
							</div>
							<small class="mb-0 text-muted">25 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar6}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Bethany Johnson</h6>
							<p class="text-muted mb-2">
								added a new member to velzon dashboard
							</p>
							<small class="mb-0 text-muted">19 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<div class="avatar-xs acitivity-avatar">
								<div
									class="avatar-title rounded-circle bg-danger-subtle text-danger"
								>
									<i class="ri-shopping-bag-line" />
								</div>
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								Your order is placed <span
									class="badge bg-danger-subtle text-danger align-middle ms-1"
									>Out of Delivery</span
								>
							</h6>
							<p class="text-muted mb-2">
								These customers can rest assured their order has
								been placed.
							</p>
							<small class="mb-0 text-muted">16 Nov</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar7}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Lewis Pratt</h6>
							<p class="text-muted mb-2">
								They all have something to say beyond the words
								on the page. They can come across as casual or
								neutral, exotic or graphic.
							</p>
							<small class="mb-0 text-muted">22 Oct</small>
						</div>
					</div>
					<div class="acitivity-item py-3 d-flex">
						<div class="flex-shrink-0">
							<div class="avatar-xs acitivity-avatar">
								<div
									class="avatar-title rounded-circle bg-info-subtle text-info"
								>
									<i class="ri-line-chart-line" />
								</div>
							</div>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">Monthly sales report</h6>
							<p class="text-muted mb-2">
								<span class="text-danger">2 days left</span>
								notification to submit the monthly sales report.
								<Link
									href=""
									class="link-warning text-decoration-underline"
									>Reports Builder</Link
								>
							</p>
							<small class="mb-0 text-muted">15 Oct</small>
						</div>
					</div>
					<div class="acitivity-item d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar8}
								alt=""
								class="avatar-xs rounded-circle acitivity-avatar"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h6 class="mb-1">
								New ticket received <span
									class="badge bg-success-subtle text-success align-middle"
									>Completed</span
								>
							</h6>
							<p class="text-muted mb-2">
								User <span class="text-secondary">Erica245</span
								> submitted a ticket.
							</p>
							<small class="mb-0 text-muted">26 Aug</small>
						</div>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>

<Offcanvas
	isOpen={isScrollBackDrop}
	scrollable
	toggle={toggleScrollBackDrop}
	header="Customer Acitivity"
	class="offcanvas-p-0"
	id="offcanvasWithBothOptions"
>
	<OffcanvasBody class="p-0 overflow-hidden">
		<div data-simplebar style="height: calc(100vh - 112px);">
			<div class="acitivity-timeline p-4">
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar1}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Oliver Phillips <span
								class="badge bg-primary-subtle text-primary align-middle"
								>New</span
							>
						</h6>
						<p class="text-muted mb-2">
							We talked about a project on linkedin.
						</p>
						<small class="mb-0 text-muted">Today</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0 avatar-xs acitivity-avatar">
						<div
							class="avatar-title bg-success-subtle text-success rounded-circle"
						>
							N
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Nancy Martino <span
								class="badge bg-secondary-subtle text-secondary align-middle"
								>In Progress</span
							>
						</h6>
						<p class="text-muted mb-2">
							<i class="ri-file-text-line align-middle ms-2" /> Create
							new project Buildng product
						</p>
						<div class="avatar-group mb-2">
							<Link
								href=""
								class="avatar-group-item"
								id="Christi"
							>
								<img
									src={avatar4}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Christi"
								>Christi</Tooltip
							>
							<Link href="" class="avatar-group-item" id="Frank">
								<img
									src={avatar3}
									alt=""
									class="rounded-circle avatar-xs"
								/>
							</Link>
							<Tooltip placement="top" target="Frank"
								>Frank Hook</Tooltip
							>

							<Link href="" class="avatar-group-item" id="Ruby">
								<div class="avatar-xs">
									<div
										class="avatar-title rounded-circle bg-light text-primary"
									>
										R
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="Ruby">Ruby</Tooltip
							>

							<Link href="" class="avatar-group-item" id="more">
								<div class="avatar-xs">
									<div class="avatar-title rounded-circle">
										2+
									</div>
								</div>
							</Link>
							<Tooltip placement="top" target="more">more</Tooltip
							>
						</div>
						<small class="mb-0 text-muted">Yesterday</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Natasha Carey <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span
							>
						</h6>
						<p class="text-muted mb-2">
							Adding a new event with attachments
						</p>
						<div class="row border border-dashed gx-2 p-2 mb-2">
							<Col class="col-4">
								<img
									src={img2}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img3}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
							<Col class="col-4">
								<img
									src={img4}
									alt=""
									class="img-fluid rounded"
								/>
							</Col>
						</div>
						<small class="mb-0 text-muted">25 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar6}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Bethany Johnson</h6>
						<p class="text-muted mb-2">
							added a new member to velzon dashboard
						</p>
						<small class="mb-0 text-muted">19 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div
								class="avatar-title rounded-circle bg-danger-subtle text-danger"
							>
								<i class="ri-shopping-bag-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							Your order is placed <span
								class="badge bg-danger-subtle text-danger align-middle ms-1"
								>Out of Delivery</span
							>
						</h6>
						<p class="text-muted mb-2">
							These customers can rest assured their order has
							been placed.
						</p>
						<small class="mb-0 text-muted">16 Nov</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar7}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Lewis Pratt</h6>
						<p class="text-muted mb-2">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic.
						</p>
						<small class="mb-0 text-muted">22 Oct</small>
					</div>
				</div>
				<div class="acitivity-item py-3 d-flex">
					<div class="flex-shrink-0">
						<div class="avatar-xs acitivity-avatar">
							<div
								class="avatar-title rounded-circle bg-info-subtle text-info"
							>
								<i class="ri-line-chart-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">Monthly sales report</h6>
						<p class="text-muted mb-2">
							<span class="text-danger">2 days left</span>
							notification to submit the monthly sales report. <Link
								href=""
								class="link-warning text-decoration-underline"
								>Reports Builder</Link
							>
						</p>
						<small class="mb-0 text-muted">15 Oct</small>
					</div>
				</div>
				<div class="acitivity-item d-flex">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle acitivity-avatar"
						/>
					</div>
					<div class="flex-grow-1 ms-3">
						<h6 class="mb-1">
							New ticket received <span
								class="badge bg-success-subtle text-success align-middle"
								>Completed</span
							>
						</h6>
						<p class="text-muted mb-2">
							User <span class="text-secondary">Erica245</span> submitted
							a ticket.
						</p>
						<small class="mb-0 text-muted">26 Aug</small>
					</div>
				</div>
			</div>
		</div>
	</OffcanvasBody>
	<div class="offcanvas-foorter border-top p-3 text-center">
		<Link href="" class="link-success"
			>View All Acitivity <i
				class="ri-arrow-right-s-line align-middle ms-1"
			/></Link
		>
	</div>
</Offcanvas>
