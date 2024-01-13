<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Collapse,
		Container,
		Row,
	} from "sveltestrap";
	import MasonryLayout from "svelte-masonry-layout";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import Link from "svelte-link";
	import { browser } from "$app/environment"

	const breakpointColumnsObj = {
		default: 3,
		1100: 3,
		700: 2,
		500: 1,
	};

	// Card Spinner
	function spinner(id) {
		if (browser) {
			document.getElementById(id).classList.remove("d-none");
			document.getElementById(id).classList.add("d-block");
			setTimeout(function () {
				document.getElementById(id).classList.remove("d-block");
				document.getElementById(id).classList.add("d-none");
			}, 3000);
		}
	}

	function delthis(id) {
		if (browser) {
			document.getElementById(id).remove();
		}
	}

	import img1 from '../../../assets/images/small/img-1.jpg';
	import img2 from '../../../assets/images/small/img-2.jpg';
	import img3 from '../../../assets/images/small/img-3.jpg';
	import img4 from '../../../assets/images/small/img-4.jpg';
	import img5 from '../../../assets/images/small/img-5.jpg';
	import img6 from '../../../assets/images/small/img-6.jpg';
	import img7 from '../../../assets/images/small/img-7.jpg';
	import img8 from '../../../assets/images/small/img-8.jpg';
	import img9 from '../../../assets/images/small/img-9.jpg';
	import img10 from '../../../assets/images/small/img-10.jpg';
	import img11 from '../../../assets/images/small/img-11.jpg';
	import img12 from '../../../assets/images/small/img-12.jpg';
	import avatar1 from '../../../assets/images/users/avatar-1.jpg';
	import avatar2 from '../../../assets/images/users/avatar-2.jpg';
	import avatar3 from '../../../assets/images/users/avatar-3.jpg';
	import avatar4 from '../../../assets/images/users/avatar-4.jpg';
	import avatar5 from '../../../assets/images/users/avatar-5.jpg';
	import avatar6 from '../../../assets/images/users/avatar-6.jpg';
	import avatar7 from '../../../assets/images/users/avatar-7.jpg';
	import avatar8 from '../../../assets/images/users/avatar-8.jpg';
	import logosm from '../../../assets/images/logo-sm.png';

</script>

<svelte:head>
	<title>Cards | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Cards" pageTitle="Base UI" />
		<Row>
			<Col sm={6} xl={3}>
				<Card>
					<img
						class="card-img-top img-fluid"
						src={img1}
						alt="Card cap"
					/>
					<CardBody>
						<h4 class="card-title mb-2">Web Developer</h4>
						<p class="card-text">
							At missed advice my it no sister. Miss told ham dull
							knew see she spot near can. Spirit her entire her
							called.
						</p>
						<div class="text-end">
							<Link href={null} class="btn btn-primary">Submit</Link>
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col sm={6} xl={3}>
				<Card>
					<img
						class="card-img-top img-fluid"
						src={img2}
						alt="Card cap"
					/>
					<CardBody>
						<h4 class="card-title mb-2">
							How apps is changing the IT world
						</h4>
						<p class="card-text mb-0">
							Whether article spirits new her covered hastily
							sitting her. Money witty books nor son add. Chicken
							age had evening believe but proceed pretend mrs.
						</p>
					</CardBody>
					<div class="card-footer">
						<Link href={null} class="card-link link-secondary">Read More <i
								class="ri-arrow-right-s-line ms-1 align-middle lh-1"
							/></Link
						>
						<Link href={null} class="card-link link-success">Bookmark <i
								class="ri-bookmark-line align-middle ms-1 lh-1"
							/></Link
						>
					</div>
				</Card>
			</Col>
			<Col sm={6} xl={3}>
				<Card>
					<img
						class="card-img-top img-fluid"
						src={img3}
						alt="Card cap"
					/>
					<CardBody>
						<p class="card-text">
							We quickly learn to fear and thus automatically
							avoid potentially stressful situations of all kinds,
							including the most common of all making mistakes.
						</p>
					</CardBody>
					<ul class="list-group list-group-flush">
						<li class="list-group-item">An item</li>
						<li class="list-group-item">A second item</li>
						<li class="list-group-item">A third item</li>
					</ul>
				</Card>
			</Col>
			<Col sm={6} xl={3}>
				<Card>
					<CardBody>
						<h4 class="card-title mb-2">
							What planning process needs ?
						</h4>
						<h6 class="card-subtitle font-14 text-muted">
							Development
						</h6>
					</CardBody>
					<img
						class="img-fluid"
						src={img4}
						alt="Card cap"
					/>
					<CardBody>
						<p class="card-text">
							Objectively pursue diverse catalysts for change for
							interoperable meta-services. Distinctively
							re-engineer revolutionary meta-services.
						</p>
					</CardBody>
					<div class="card-footer">
						<Link href={null} class="card-link link-secondary">Read More <i
								class="ri-arrow-right-s-line ms-1 align-middle lh-1"
							/></Link
						>
						<Link href={null} class="card-link link-success">Bookmark <i
								class="ri-bookmark-line align-middle ms-1 lh-1"
							/></Link
						>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Using Grid Markup
					</h5>
				</div>
				<Row class="row-cols-xxl-5 row-cols-lg-3 row-cols-1">
					<Col>
						<Card class="card-body">
							<div class="d-flex mb-4 align-items-center">
								<div class="flex-shrink-0">
									<img
										src={avatar1}
										alt=""
										class="avatar-sm rounded-circle"
									/>
								</div>
								<div class="flex-grow-1 ms-2">
									<h5 class="card-title mb-1">
										Oliver Phillips
									</h5>
									<p class="text-muted mb-0">
										Digital Marketing
									</p>
								</div>
							</div>
							<h6 class="mb-1">$15,548</h6>
							<p class="card-text text-muted">Expense Account</p>
							<Link href={null} class="btn btn-primary btn-sm"
								>See Details</Link>
						</Card>
					</Col>
					<Col>
						<Card class="card-body">
							<div class="d-flex mb-4 align-items-center">
								<div class="flex-shrink-0">
									<img
										src={avatar4}
										alt=""
										class="avatar-sm rounded-circle"
									/>
								</div>
								<div class="flex-grow-1 ms-2">
									<h5 class="card-title mb-1">
										Natasha Carey
									</h5>
									<p class="text-muted mb-0">Manager</p>
								</div>
							</div>
							<h6 class="mb-1">$8,785</h6>
							<p class="card-text text-muted">Expense Account</p>
							<Link href={null} class="btn btn-primary btn-sm"
								>See Details</Link>
						</Card>
					</Col>
					<Col>
						<Card class="card-body">
							<div class="d-flex mb-4 align-items-center">
								<div class="flex-shrink-0">
									<img
										src={avatar3}
										alt=""
										class="avatar-sm rounded-circle"
									/>
								</div>
								<div class="flex-grow-1 ms-2">
									<h5 class="card-title mb-1">
										Bethany Johnson
									</h5>
									<p class="text-muted mb-0">Development</p>
								</div>
							</div>
							<h6 class="mb-1">$1,542</h6>
							<p class="card-text text-muted">Expense Account</p>
							<Link href={null} class="btn btn-primary btn-sm"
								>See Details</Link>
						</Card>
					</Col>
					<Col>
						<Card class="card-body">
							<div class="d-flex mb-4 align-items-center">
								<div class="flex-shrink-0">
									<img
										src={avatar5}
										alt=""
										class="avatar-sm rounded-circle"
									/>
								</div>
								<div class="flex-grow-1 ms-2">
									<h5 class="card-title mb-1">
										Erica Kernan
									</h5>
									<p class="text-muted mb-0">
										Fashion Designer
									</p>
								</div>
							</div>
							<h6 class="mb-1">$798</h6>
							<p class="card-text text-muted">Expense Account</p>
							<Link href={null} class="btn btn-primary btn-sm"
								>See Details</Link>
						</Card>
					</Col>
					<Col>
						<Card class="card-body">
							<div class="d-flex mb-4 align-items-center">
								<div class="flex-shrink-0">
									<img
										src={avatar6}
										alt=""
										class="avatar-sm rounded-circle"
									/>
								</div>
								<div class="flex-grow-1 ms-2">
									<h5 class="card-title mb-1">Lewis Pratt</h5>
									<p class="text-muted mb-0">Design</p>
								</div>
							</div>
							<h6 class="mb-1">$2,856</h6>
							<p class="card-text text-muted">Expense Account</p>
							<Link href={null} class="btn btn-primary btn-sm"
								>See Details</Link>
						</Card>
					</Col>
				</Row>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Card Text Alignment
					</h5>
				</div>
				<Row>
					<Col lg={6} xxl={4}>
						<Card class="card-body">
							<div class="avatar-sm mb-3">
								<div class="avatar-title bg-success-subtle text-success fs-17 rounded"
								>
									<i class="ri-smartphone-line" />
								</div>
							</div>
							<h4 class="card-title">Text Application</h4>
							<p class="card-text text-muted">
								Send a link to apply on mobile device.
								Appropriately communicate one-to-one technology.
							</p>
							<Link href={null} class="btn btn-success"
								>Apply Now</Link>
						</Card>
					</Col>
					<Col lg={6} xxl={4}>
						<div class="card card-body text-center">
							<div class="avatar-sm mx-auto mb-3">
								<div class="avatar-title bg-success-subtle text-success fs-17 rounded"
								>
									<i class="ri-add-line" />
								</div>
							</div>
							<h4 class="card-title">Add New Application</h4>
							<p class="card-text text-muted">
								Send a link to apply on mobile device.
								Appropriately communicate one-to-one technology.
							</p>
							<Link href={null} class="btn btn-success">Add New</Link>
						</div>
					</Col>
					<Col lg={6} xxl={4}>
						<div class="card card-body text-end">
							<div class="avatar-sm ms-auto mb-3">
								<div class="avatar-title bg-success-subtle text-success fs-17 rounded"
								>
									<i class="ri-gift-fill" />
								</div>
							</div>
							<h4 class="card-title">Text Application</h4>
							<p class="card-text text-muted">
								Send a link to apply on mobile device.
								Appropriately communicate one-to-one technology.
							</p>
							<Link href={null} class="btn btn-success">Add New</Link>
						</div>
					</Col>
				</Row>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Card Header and Footer
					</h5>
				</div>
				<Row>
					<Col lg={6} xxl={4}>
						<Card>
							<CardHeader>
								<button
									type="button"
									class="btn-close float-end fs-11"
									aria-label="Close"
								/>
								<h6 class="card-title mb-0">
									Hi, Erica Kernan
								</h6>
							</CardHeader>
							<CardBody>
								<h6 class="card-title">
									How to get creative in your work ?
								</h6>
								<p class="card-text text-muted mb-0">
									A business consulting agency is involved in
									the planning, implementation, and education
									of businesses. Miss told ham dull knew see
									she spot near can. Spirit her entire her
									called.
								</p>
							</CardBody>
							<div class="card-footer">
								<Link href={null} class="link-success float-end"
									>Read More <i
										class="ri-arrow-right-s-line align-middle ms-1 lh-1"
									/></Link
								>
								<p class="text-muted mb-0">1 days Ago</p>
							</div>
						</Card>
					</Col>
					<Col lg={6} xxl={4}>
						<Card>
							<CardHeader>
								<button
									type="button"
									class="btn-close float-end fs-11"
									aria-label="Close"
								/>
								<h6 class="card-title mb-0">
									Invoice<span class="text-secondary"
										>#45155468</span
									>
								</h6>
							</CardHeader>
							<CardBody>
								<h6 class="card-title">
									What planning process needs ?
								</h6>
								<p class="card-text text-muted mb-0">
									Intrinsically incubate intuitive
									opportunities and real-time potentialities
									for change for interoperable meta-services
									itself or distract the viewer's attention
									from the layout.
								</p>
							</CardBody>
							<div class="card-footer">
								<Link href={null} class="link-success float-end"
									>Payment Now <i
										class="ri-arrow-right-s-line align-middle ms-1 lh-1"
									/></Link
								>
								<p class="text-muted mb-0">5 days Left</p>
							</div>
						</Card>
					</Col>
					<Col lg={6} xxl={4}>
						<Card>
							<CardHeader>
								<h6 class="card-title mb-0">
									Creative Agency Quote
								</h6>
							</CardHeader>
							<CardBody>
								<blockquote class="card-blockquote mb-0">
									<p class="text-muted mb-2">
										There are many variations of passages of
										Lorem Ipsum available.
									</p>
									<figure class="mb-0">
										<blockquote class="blockquote">
											<p class="lead">
												"A business consulting agency is
												involved in the planning,
												implementation, and education of
												businesses."
											</p>
										</blockquote>
										<figcaption
											class="blockquote-footer fs-13 text-end mb-0"
										>
											Creative Agency<cite
												title="Source Title"
												class="text-primary fw-semibold"
											>
												Alice Mellor</cite
											>
										</figcaption>
									</figure>
								</blockquote>
							</CardBody>
						</Card>
					</Col>
				</Row>
			</Col>
		</Row>

		<Row>
			<Col xl={4}>
				<Card>
					<CardBody>
						<h4 class="card-title mb-3">
							<i
								class="ri-user-3-fill align-middle me-1 text-muted"
							/> Natasha Carey
						</h4>
						<p class="text-muted">
							Too much or too little spacing, as in the example
							below, can make things unpleasant for the reader.
							The goal is to make your text as comfortable to read
							as possible.
						</p>
						<p class="text-muted mb-0">
							This response is important for our ability to learn
							from mistakes, but it alsogives rise to
							self-criticism.
						</p>
					</CardBody>
					<div class="card-footer text-center">
						<Link href={null} class="link-secondary">View All Notification (2) <i
								class="ri-arrow-right-s-line align-middle ms-1 lh-1"
							/></Link
						>
					</div>
				</Card>
			</Col>
			<Col xl={4}>
				<Card>
					<CardHeader>
						<span class="float-end text-secondary">Overview</span>
						<h6 class="card-title">
							Give your text a good structure
						</h6>
						<p class="card-subtitle text-muted mb-0">
							Fantastic Design
						</p>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Contrary to popular belief, you don’t have to work
							endless nights and hours to create a <Link
								href={null}
								class="text-decoration-underline"
								><b>Fantastic Design</b></Link> by using complicated 3D elements. Flat design is your
							friend. Remember that. And the great thing about flat
							design is that it has become more and more popular over
							the years.
						</p>
						<p class="text-muted mb-0">
							In some designs, you might adjust your tracking to
							create a certain artistic effect.
						</p>
					</CardBody>
				</Card>
			</Col>
			<Col xl={4}>
				<Card>
					<CardHeader>
						<h6 class="card-title mb-0">
							<i class="ri-gift-line align-middle me-1 lh-1" /> You've
							made it!
						</h6>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							After gathering lots of different opinions and
							graphic design basics, I came up with a list of 30
							graphic design tips that you can start implementing.
							Each design is a new, unique piece of art birthed
							into this world.
						</p>
						<p class="text-muted mb-0">
							Art party locavore wolf cliche high life echo park
							Austin.
						</p>
					</CardBody>
					<div class="card-footer">
						<div class="hstack gap-2 justify-content-end">
							<Link
								href={null}
								class="btn btn-link btn-sm link-success"
								><i class="ri-close-line align-middle lh-1" /> Close</Link>
							<Link href={null} class="btn btn-primary btn-sm"
								>Read More</Link>
						</div>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xl={4}>
				<Card>
					<CardHeader>
						<button
							type="button"
							class="btn-close float-end fs-11"
							aria-label="Close"
						/>
						<h6 class="card-title mb-0">Employee Card</h6>
					</CardHeader>
					<CardBody class="p-4 text-center">
						<div class="mx-auto avatar-md mb-3">
							<img
								src={avatar8}
								alt=""
								class="img-fluid rounded-circle"
							/>
						</div>
						<h5 class="card-title mb-1">Gabriel Palmer</h5>
						<p class="text-muted mb-0">Graphic Designer</p>
					</CardBody>
					<div class="card-footer text-center">
						<ul class="list-inline mb-0">
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-secondary"><i class="ri-facebook-fill"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-success"><i class="ri-whatsapp-line"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-primary"><i class="ri-linkedin-fill"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-danger"><i class="ri-slack-fill"></i></Link>
							</li>
						</ul>
					</div>
				</Card>
			</Col>
			<Col xl={4}>
				<Card>
					<CardHeader>
						<button
							type="button"
							class="btn-close float-end fs-11"
							aria-label="Close"
						/>
						<h6 class="card-title mb-0">Employee Card</h6>
					</CardHeader>
					<CardBody class="p-4 text-center">
						<div class="mx-auto avatar-md mb-3">
							<img
								src={avatar5}
								alt=""
								class="img-fluid rounded-circle"
							/>
						</div>
						<h5 class="card-title mb-1">Amelie Townsend</h5>
						<p class="text-muted mb-0">Project Manager</p>
					</CardBody>
					<div class="card-footer text-center">
						<ul class="list-inline mb-0">
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-secondary"><i class="ri-facebook-fill"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-success"><i class="ri-whatsapp-line"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-primary"><i class="ri-linkedin-fill"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-danger"><i class="ri-slack-fill"></i></Link>
							</li>
						</ul>
					</div>
				</Card>
			</Col>
			<Col xl={4}>
				<Card>
					<CardHeader>
						<button
							type="button"
							class="btn-close float-end fs-11"
							aria-label="Close"
						/>
						<h6 class="card-title mb-0">Employee Card</h6>
					</CardHeader>
					<CardBody class="p-4 text-center">
						<div class="mx-auto avatar-md mb-3">
							<img
								src={avatar3}
								alt=""
								class="img-fluid rounded-circle"
							/>
						</div>
						<h5 class="card-title mb-1">Jeffrey Montgomery</h5>
						<p class="text-muted mb-0">UI/UX Designer</p>
					</CardBody>
					<div class="card-footer text-center">
						<ul class="list-inline mb-0">
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-secondary"><i class="ri-facebook-fill"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-success"><i class="ri-whatsapp-line"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-primary"><i class="ri-linkedin-fill"></i></Link>
							</li>
							<li class="list-inline-item">
								<Link href={null} class="lh-1 align-middle link-danger"><i class="ri-slack-fill"></i></Link>
							</li>
						</ul>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xl={4} id="card-none1">
				<Card>
					<CardHeader>
						<div class="d-flex align-items-center">
							<div class="flex-grow-1">
								<h6 class="card-title mb-0">
									Card with Spinner Loader
								</h6>
							</div>
							<div class="flex-shrink-0">
								<ul
									class="list-inline card-toolbar-menu d-flex align-items-center mb-0"
								>
									<li class="list-inline-item">
										<Link
											href=""
											class="align-middle"
											role="button"
											on:click={() => spinner("spinner1")}
										>
											<i
												class="mdi mdi-refresh align-middle"
											/>
										</Link>
									</li>
									<li class="list-inline-item">
										<Link
											href=""
											id="collapseexample1"
											class="align-middle minimize-card"
											role="button"
										>
											<i
												class="mdi mdi-plus align-middle plus"
											/>
											<i
												class="mdi mdi-minus align-middle minus"
											/>
										</Link>
									</li>
									<li class="list-inline-item">
										<button
											type="button"
											on:click={() =>
												delthis("card-none1")}
											class="btn-close fs-10 align-middle"
										/>
									</li>
								</ul>
							</div>
						</div>
						<div class="card-preloader d-none" id="spinner1">
							<div class="card-status">
								<div class="spinner-border text-success">
									<span class="visually-hidden"
										>Loading...</span
									>
								</div>
							</div>
						</div>
					</CardHeader>

					<Collapse
						toggler="#collapseexample1"
						class="card-body"
						isOpen>
						<div class="d-flex">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								Some placeholder content for the collapse
								component. This panel is hidden by default but
								revealed when the user activates.
							</div>
						</div>
						<div class="d-flex mt-2">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								Too much or too little spacing, as in the
								example below, can make things unpleasant for
								the reader. The goal is to make your text as
								comfortable to read as possible.
							</div>
						</div>
						<div class="d-flex mt-2">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								This may be the most commonly encountered tip I
								received from the designers I spoke with. They
								highly encourage that you use different fonts in
								one design, but do not over-exaggerate and go
								overboard.
							</div>
						</div>

						<div class="card-status visually-hidden">
							<div class="spinner-border text-success">
								<span class="visually-hidden">Loading...</span>
							</div>
						</div>
					</Collapse>
				</Card>
			</Col>
			<Col xl={4} id="card-none2">
				<Card>
					<CardHeader>
						<div class="d-flex align-items-center">
							<div class="flex-grow-1">
								<h6 class="card-title mb-0">
									Card with Growing Spinner Loader
								</h6>
							</div>
							<div class="flex-shrink-0">
								<ul
									class="list-inline card-toolbar-menu d-flex align-items-center mb-0"
								>
									<li class="list-inline-item">
										<Link
											href=""
											class="align-middle"
											role="button"
											on:click={() => spinner("spinner2")}
										>
											<i
												class="mdi mdi-refresh align-middle"
											/>
										</Link>
									</li>
									<li class="list-inline-item">
										<Link
											href=""
											class="align-middle minimize-card"
											role="button"
											id="collapseExample2"
										>
											<i
												class="mdi mdi-plus align-middle plus"
											/>
											<i
												class="mdi mdi-minus align-middle minus"
											/>
										</Link>
									</li>
									<li class="list-inline-item">
										<button
											type="button"
											on:click={() =>
												delthis("card-none2")}
											class="btn-close fs-10 align-middle"
										/>
									</li>
								</ul>
							</div>
						</div>
						<div class="card-preloader d-none" id="spinner2">
							<div class="card-status">
								<div class="spinner-grow text-danger">
									<span class="visually-hidden"
										>Loading...</span
									>
								</div>
							</div>
						</div>
					</CardHeader>

					<Collapse
						class="card-body"
						toggler="#collapseExample2"
						isOpen>
						<div class="d-flex">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								Some placeholder content for the collapse
								component. This panel is hidden by default but
								revealed when the user activates.
							</div>
						</div>
						<div class="d-flex mt-2">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								Too much or too little spacing, as in the
								example below, can make things unpleasant for
								the reader. The goal is to make your text as
								comfortable to read as possible.
							</div>
						</div>
						<div class="d-flex mt-2">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								This may be the most commonly encountered tip I
								received from the designers I spoke with. They
								highly encourage that you use different fonts in
								one design, but do not over-exaggerate and go
								overboard.
							</div>
						</div>
					</Collapse>
				</Card>
			</Col>
			<Col xl={4} id="card-none3">
				<Card>
					<CardHeader>
						<div class="d-flex align-items-center">
							<div class="flex-grow-1">
								<h6 class="card-title mb-0">
									Card with Custom Loader
								</h6>
							</div>
							<div class="flex-shrink-0">
								<ul
									class="list-inline card-toolbar-menu d-flex align-items-center mb-0"
								>
									<li class="list-inline-item">
										<Link
											href=""
											class="align-middle"
											role="button"
											on:click={() => spinner("spinner3")}
										>
											<i
												class="mdi mdi-refresh align-middle"
											/>
										</Link>
									</li>
									<li class="list-inline-item">
										<Link
											href=""
											class="align-middle minimize-card"
											role="button"
											id="collapseExample3"
										>
											<i
												class="mdi mdi-plus align-middle plus"
											/>
											<i
												class="mdi mdi-minus align-middle minus"
											/>
										</Link>
									</li>
									<li class="list-inline-item">
										<button
											type="button"
											on:click={() =>
												delthis("card-none3")}
											class="btn-close fs-10 align-middle"
										/>
									</li>
								</ul>
							</div>
						</div>
						<div class="card-preloader d-none" id="spinner3">
							<div class="card-status">
								<img
									src={logosm}
									alt=""
									class="img-fluid custom-loader"
								/>
							</div>
						</div>
					</CardHeader>

					<Collapse
						class="card-body"
						toggler="#collapseExample3"
						isOpen>
						<div class="d-flex">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								Some placeholder content for the collapse
								component. This panel is hidden by default but
								revealed when the user activates.
							</div>
						</div>
						<div class="d-flex mt-2">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								Too much or too little spacing, as in the
								example below, can make things unpleasant for
								the reader. The goal is to make your text as
								comfortable to read as possible.
							</div>
						</div>
						<div class="d-flex mt-2">
							<div class="flex-shrink-0">
								<i
									class="ri-checkbox-circle-fill text-success"
								/>
							</div>
							<div class="flex-grow-1 ms-2 text-muted">
								This may be the most commonly encountered tip I
								received from the designers I spoke with. They
								highly encourage that you use different fonts in
								one design, but do not over-exaggerate and go
								overboard.
							</div>
						</div>
					</Collapse>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 text-decoration-underline">
						Card Caps & Overlays
					</h5>
				</div>
				<Row>
					<Col lg={6} xxl={4}>
						<Card class="card-overlay">
							<img
								class="card-img img-fluid"
								src={img12}
								alt="Card"
							/>
							<div class="card-img-overlay p-0 d-flex flex-column">
								<CardHeader class="bg-transparent">
									<h4 class="card-title text-white mb-0">
										Design your apps in your own way
									</h4>
								</CardHeader>
								<CardBody>
									<p class="card-text text-white mb-2">
										Each design is a new, unique piece of
										art birthed into this world, and while
										you have the opportunity to be creative
										and make your unpleasant for the reader.
									</p>
									<p class="card-text">
										<small class="text-white"
											>Last updated 3 mins ago</small
										>
									</p>
								</CardBody>
								<div class="card-footer bg-transparent text-center"
								>
									<Link href={null} class="link-light"
										>Read More <i
											class="ri-arrow-right-s-line align-middle ms-1 lh-1"
										/></Link
									>
								</div>
							</div>
						</Card>
					</Col>
					<Col lg={6} xxl={4}>
						<Card class="card-overlay">
							<img
								class="card-img img-fluid"
								src={img1}
								alt="Card"
							/>
							<div class="card-img-overlay p-0">
								<CardHeader class="bg-transparent">
									<h4 class="card-title text-white mb-0">
										Design your apps in your own way
									</h4>
								</CardHeader>
								<CardBody>
									<p class="card-text text-white mb-2">
										Each design is a new, unique piece of
										art birthed into this world, and while
										you have the opportunity to be creative
										and make your unpleasant for the reader.
									</p>
									<p class="card-text">
										<small class="text-white"
											>Last updated 3 mins ago</small
										>
									</p>
								</CardBody>
							</div>
						</Card>
					</Col>
					<Col lg={6} xxl={4}>
						<Card class="card-overlay">
							<img
								class="card-img img-fluid"
								src={img5}
								alt="Card"
							/>
							<div class="card-img-overlay p-0" style="top: auto">
								<CardBody>
									<p class="card-text text-white mb-2">
										Each design is a new, unique piece of
										art birthed into this world, and while
										you have the opportunity to be creative
										and make your unpleasant for the reader.
									</p>
									<p class="card-text">
										<small class="text-white"
											>Last updated 3 mins ago</small
										>
									</p>
								</CardBody>
								<div class="card-footer bg-transparent">
									<h4 class="card-title text-white mb-0">
										Design your apps in your own way
									</h4>
								</div>
							</div>
						</Card>
					</Col>
				</Row>

				<Row>
					<Col lg={6} xxl={4}>
						<Card>
							<img
								class="card-img-top img-fluid"
								src={img6}
								alt="Card cap"
							/>
							<CardBody>
								<h4 class="card-title mb-2">
									A day in the of a professional fashion
									designer
								</h4>
								<p class="card-text text-muted">
									Exercitation +1 labore velit, blog sartorial
									PBR leggings next level wes anderson artisan
									four loko farm-to-table craft beer twee.
									commodo enim craft beer mlkshk aliquip jean
									shorts ullamco.
								</p>
								<p class="card-text">Last updated 3 mins ago</p>
							</CardBody>
						</Card>
					</Col>
					<Col lg={6} xxl={4}>
						<Card>
							<CardBody>
								<h4 class="card-title mb-2">
									A day in the of a professional fashion
									designer
								</h4>
								<p class="card-text text-muted">
									Exercitation +1 labore velit, blog sartorial
									PBR leggings next level wes anderson artisan
									four loko farm-to-table craft beer twee.
									commodo enim craft beer mlkshk aliquip jean
									shorts ullamco.
								</p>
								<p class="card-text">Last updated 3 mins ago</p>
							</CardBody>
							<img
								class="card-img-bottom img-fluid"
								src={img7}
								alt="Card cap"
							/>
						</Card>
					</Col>

					<Col lg={6} xxl={4}>
						<Card>
							<CardBody>
								<h4 class="card-title mb-2">
									A day in the of a professional fashion
									designer
								</h4>
								<p class="card-text text-muted">
									Exercitation +1 labore velit, blog sartorial
									PBR leggings next level wes anderson artisan
									four loko farm-to-table craft beer twee.
								</p>
							</CardBody>
							<img
								class="card-img rounded-0 img-fluid"
								src={img8}
								alt="Card cap"
							/>
							<div class="card-footer">
								<p class="card-text mb-0">
									Last updated 3 mins ago
								</p>
							</div>
						</Card>
					</Col>

					<Col lg={6} xxl={4}>
						<Card>
							<CardHeader>
								<h4 class="card-title mb-0">
									A day in the of a professional fashion
									designer
								</h4>
							</CardHeader>
							<CardBody>
								<p class="card-text text-muted">
									Exercitation +1 labore velit, blog sartorial
									PBR leggings next level wes anderson artisan
									four loko farm-to-table craft beer twee.
								</p>
							</CardBody>
							<img
								class="card-img rounded-0 img-fluid"
								src={img10}
								alt="Card cap"
							/>
							<div class="card-footer">
								<p class="card-text mb-0">
									Last updated 3 mins ago
								</p>
							</div>
						</Card>
					</Col>

					<Col lg={6} xxl={4}>
						<Card>
							<img
								class="card-img-top img-fluid"
								src={img11}
								alt="Card cap"
							/>
							<CardHeader>
								<h4 class="card-title mb-0">
									A day in the of a professional fashion
									designer
								</h4>
							</CardHeader>
							<CardBody>
								<p class="card-text text-muted">
									Exercitation +1 labore velit, blog sartorial
									PBR leggings next level wes anderson artisan
									four loko farm-to-table craft beer twee.
								</p>
							</CardBody>
							<div class="card-footer">
								<p class="card-text mb-0">
									Last updated 3 mins ago
								</p>
							</div>
						</Card>
					</Col>

					<Col lg={6} xxl={4}>
						<Card>
							<CardHeader>
								<h4 class="card-title mb-0">
									A day in the of a professional fashion
									designer
								</h4>
							</CardHeader>
							<CardBody>
								<p class="card-text text-muted">
									Exercitation +1 labore velit, blog sartorial
									PBR leggings next level wes anderson artisan
									four loko farm-to-table craft beer twee.
									ommodo enim craft beer mlkshk aliquip jean
									shorts ullamco.
								</p>
								<p class="card-text mb-0">
									Last updated 3 mins ago
								</p>
							</CardBody>
							<img
								class="card-img-bottom img-fluid"
								src={img11}
								alt="Card cap"
							/>
						</Card>
					</Col>
				</Row>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Horizontal Card
					</h5>
				</div>
				<Row>
					<Col xxl={6}>
						<Card>
							<Row class="g-0">
								<Col md={4}>
									<img
										class="rounded-start img-fluid h-100 object-cover"
										src={img12}
										alt="Card"
									/>
								</Col>
								<Col md={8}>
									<CardHeader>
										<h5 class="card-title mb-0">
											Give your text a good structure
										</h5>
									</CardHeader>
									<CardBody>
										<p class="card-text mb-2">
											For that very reason, I went on a
											quest and spoke to many different
											professional graphic designers and
											asked them what graphic design tips
											they live.
										</p>
										<p class="card-text">
											<small class="text-muted"
												>Last updated 3 mins ago</small
											>
										</p>
									</CardBody>
								</Col>
							</Row>
						</Card>
					</Col>
					<Col xxl={6}>
						<Card>
							<Row class="g-0">
								<Col md={8}>
									<CardHeader>
										<h5 class="card-title mb-0">
											Manage white space in responsive
											layouts ?
										</h5>
									</CardHeader>
									<CardBody>
										<p class="card-text mb-2">
											For that very reason, I went on a
											quest and spoke to many different
											professional graphic designers and
											asked them what graphic design tips
											they live.
										</p>
										<p class="card-text">
											<small class="text-muted"
												>Last updated 3 mins ago</small
											>
										</p>
									</CardBody>
								</Col>
								<div class="col-md-4">
									<img
										class="rounded-end img-fluid h-100 object-cover"
										src={img4}
										alt="Card"
									/>
								</div>
							</Row>
						</Card>
					</Col>

					<Col xxl={6}>
						<Card>
							<Row class="g-0">
								<Col md={4}>
									<img
										class="rounded-start img-fluid h-100 object-cover"
										src={img9}
										alt="Card"
									/>
								</Col>
								<Col md={8}>
									<CardBody>
										<h5 class="card-title mb-2">
											Give your text a good structure
										</h5>
										<p class="card-text text-muted mb-0">
											For that very reason, I went on a
											quest and spoke to many different
											professional graphic designers and
											asked them what graphic design tips
											they live.
										</p>
									</CardBody>
									<div class="card-footer">
										<p class="card-text">
											<small class="text-muted"
												>Last updated 3 mins ago</small
											>
										</p>
									</div>
								</Col>
							</Row>
						</Card>
					</Col>

					<Col xxl={6}>
						<Card>
							<Row class="g-0">
								<Col md={8}>
									<CardBody>
										<h5 class="card-title mb-2">
											Manage white space in responsive
											layouts ?
										</h5>
										<p class="card-text text-muted mb-0">
											For that very reason, I went on a
											quest and spoke to many different
											professional graphic designers and
											asked them what graphic design tips
											they live.
										</p>
									</CardBody>
									<div class="card-footer">
										<p class="card-text">
											<small class="text-muted"
												>Last updated 3 mins ago</small
											>
										</p>
									</div>
								</Col>
								<Col md={4}>
									<img
										class="rounded-end img-fluid h-100 object-cover"
										src={img2}
										alt="Card"
									/>
								</Col>
							</Row>
						</Card>
					</Col>
				</Row>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Card Background Color
					</h5>
				</div>
				<Row>
					<Col xxl={4}>
						<Card class="card-primary">
							<CardBody>
								<div class="d-flex align-items-center">
									<div class="flex-shrink-0">
										<img
											src={avatar1}
											alt=""
											class="avatar-sm rounded-circle"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										<p class="card-text">
											<span class="fw-medium"
												>Jeffrey Montgomery</span
											> (Graphic Designer) started a new conversation.
										</p>
									</div>
								</div>
							</CardBody>
							<div class="card-footer">
								<div class="text-center">
									<Link href={null} class="link-light"
										>Connect Now <i
											class="ri-arrow-right-s-line align-middle lh-1"
										/></Link
									>
								</div>
							</div>
						</Card>
					</Col>
					<Col xxl={4}>
						<Card class="card-success">
							<CardBody>
								<div class="d-flex align-items-center">
									<div class="flex-shrink-0">
										<img
											src={avatar2}
											alt=""
											class="avatar-sm rounded-circle"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										<p class="card-text">
											<span class="fw-medium"
												>Charles Dickens</span
											> (Financial Analyst) started a new conversation.
										</p>
									</div>
								</div>
							</CardBody>
							<div class="card-footer">
								<div class="text-center">
									<Link href={null} class="link-light"
										>Connect Now <i
											class="ri-arrow-right-s-line align-middle lh-1"
										/></Link
									>
								</div>
							</div>
						</Card>
					</Col>
					<Col xxl={4}>
						<Card class="card-info">
							<CardBody>
								<div class="d-flex align-items-center">
									<div class="flex-shrink-0">
										<img
											src={avatar3}
											alt=""
											class="avatar-sm rounded-circle"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										<p class="card-text">
											<span class="fw-medium"
												>Oliver Phillips</span
											> (UI/UX Designer) started a new conversation.
										</p>
									</div>
								</div>
							</CardBody>
							<div class="card-footer">
								<div class="text-center">
									<Link href={null} class="link-light"
										>Connect Now <i
											class="ri-arrow-right-s-line align-middle lh-1"
										/></Link
									>
								</div>
							</div>
						</Card>
					</Col>
				</Row>
			</Col>
		</Row>

		<Row>
			<Col xxl={4}>
				<Card class="card-warning">
					<CardBody>
						<div class="d-flex align-items-center">
							<div class="flex-shrink-0">
								<img
									src={avatar4}
									alt=""
									class="avatar-sm rounded-circle"
								/>
							</div>
							<div class="flex-grow-1 ms-3">
								<p class="card-text">
									<span class="fw-medium">Rebecca Swartz</span
									> (Graphic Designer) started a new conversation.
								</p>
							</div>
						</div>
					</CardBody>
					<div class="card-footer">
						<div class="text-center">
							<Link href={null} class="link-light"
								>Connect Now <i
									class="ri-arrow-right-s-line align-middle lh-1"
								/></Link>
						</div>
					</div>
				</Card>
			</Col>
			<Col xxl={4}>
				<Card class="card-danger">
					<CardBody>
						<div class="d-flex align-items-center">
							<div class="flex-shrink-0">
								<img
									src={avatar6}
									alt=""
									class="avatar-sm rounded-circle"
								/>
							</div>
							<div class="flex-grow-1 ms-3">
								<p class="card-text">
									<span class="fw-medium">Betty Richards</span
									> (Back End Developer) started a new conversation.
								</p>
							</div>
						</div>
					</CardBody>
					<div class="card-footer">
						<div class="text-center">
							<Link href={null} class="link-light"
								>Connect Now <i
									class="ri-arrow-right-s-line align-middle lh-1"
								/></Link>
						</div>
					</div>
				</Card>
			</Col>
			<Col xxl={4}>
				<Card class="card-dark">
					<CardBody>
						<div class="d-flex align-items-center">
							<div class="flex-shrink-0">
								<img
									src={avatar5}
									alt=""
									class="avatar-sm rounded-circle"
								/>
							</div>
							<div class="flex-grow-1 ms-3">
								<p class="card-text">
									<span class="fw-medium">Brooke Hayes</span> (Founder
									& CEO) started a new conversation.
								</p>
							</div>
						</div>
					</CardBody>
					<div class="card-footer">
						<div class="text-center">
							<Link href={null} class="link-light"
								>Connect Now <i
									class="ri-arrow-right-s-line align-middle lh-1"
								/></Link>
						</div>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={4}>
				<Card class="card-secondary">
					<CardBody>
						<div class="d-flex align-items-center">
							<div class="flex-shrink-0">
								<img
									src={avatar7}
									alt=""
									class="avatar-sm rounded-circle"
								/>
							</div>
							<div class="flex-grow-1 ms-3">
								<p class="card-text">
									<span class="fw-medium"
										>Bethany Johnson</span
									> (Team Leader) started a new conversation.
								</p>
							</div>
						</div>
					</CardBody>
					<div class="card-footer">
						<div class="text-center">
							<Link href={null} class="link-light"
								>Connect Now <i
									class="ri-arrow-right-s-line align-middle lh-1"
								/></Link>
						</div>
					</div>
				</Card>
			</Col>
			<Col xxl={4}>
				<Card class="card-light">
					<CardBody>
						<div class="d-flex align-items-center">
							<div class="flex-shrink-0">
								<img
									src={avatar8}
									alt=""
									class="avatar-sm rounded-circle"
								/>
							</div>
							<div class="flex-grow-1 ms-3">
								<p class="card-text">
									<span class="fw-medium"
										>Amelie Townsend</span
									> (UI/UX Designer) started a new conversation.
								</p>
							</div>
						</div>
					</CardBody>
					<div class="card-footer">
						<div class="text-center">
							<Link href={null} class="link-dark"
								>Connect Now <i
									class="ri-arrow-right-s-line align-middle lh-1"
								/></Link>
						</div>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Card Border Color
					</h5>
				</div>

				<Row>
					<Col xxl={4}>
						<Card class="border card-border-primary">
							<CardHeader>
								<span class="float-end">75%</span>
								<h6 class="card-title mb-0">
									Handle to Forcast <span
										class="badge bg-danger align-middle fs-10"
										>Poor</span
									>
								</h6>
							</CardHeader>
							<CardBody>
								<p class="card-text">
									Whether article spirits new her covered
									hastily sitting her. Money witty books nor
									son add build on the card Chicken age had
									evening believe but proceed pretend mrs.
								</p>
								<div class="text-end">
									<Link
										href={null}
										class="link-primary fw-medium"
										>Read More <i
											class="ri-arrow-right-line align-middle"
										/></Link
									>
								</div>
							</CardBody>
						</Card>
					</Col>
					<Col xxl={4}>
						<Card class="border card-border-success">
							<CardHeader>
								<span class="float-end">100%</span>
								<h6 class="card-title mb-0">
									Quality Forcast <span
										class="badge bg-success align-middle fs-10"
										>Excellent</span
									>
								</h6>
							</CardHeader>
							<CardBody>
								<p class="card-text">
									They all have something to say beyond the
									words on the page. They can come across as
									casual or neutral, exotic or graphic. Cosby
									sweater eu banh mi, qui irure terry
									richardson ex squid.
								</p>
								<div class="text-end">
									<Link
										href={null}
										class="link-success fw-medium"
										>Read More <i
											class="ri-arrow-right-line align-middle"
										/></Link
									>
								</div>
							</CardBody>
						</Card>
					</Col>
					<Col xxl={4}>
						<Card class="border card-border-info">
							<CardHeader>
								<h6 class="card-title mb-0">
									Check your E-mails <span
										class="badge bg-info align-middle fs-10"
										>In Process</span
									>
								</h6>
							</CardHeader>
							<CardBody>
								<p class="card-text">
									They all have something to say beyond the
									words on the page. They can come across as
									casual or neutral, exotic or graphic. Cosby
									sweater eu banh mi, qui irure terry
									richardson ex squid.
								</p>
								<div class="text-end">
									<Link href={null} class="link-info fw-medium"
										>Read More <i
											class="ri-arrow-right-line align-middle"
										/></Link
									>
								</div>
							</CardBody>
						</Card>
					</Col>
				</Row>
			</Col>
		</Row>

		<Row>
			<Col xxl={4}>
				<Card class="border card-border-warning">
					<CardHeader>
						<h6 class="card-title mb-0">
							Check your Payment <span
								class="badge bg-warning align-middle fs-10"
								>Pending</span>
						</h6>
					</CardHeader>
					<CardBody>
						<p class="card-text">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic. Cosby sweater eu banh mi, qui
							irure terry richardson ex squid.
						</p>
						<div class="text-end">
							<Link href={null} class="link-warning fw-medium"
								>Read More <i
									class="ri-arrow-right-line align-middle"
								/></Link>
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col xxl={4}>
				<Card class="border card-border-danger">
					<CardHeader>
						<h6 class="card-title mb-0">
							Your Ordered Cancel <span
								class="badge bg-danger align-middle fs-10"
								>Cancel</span>
						</h6>
					</CardHeader>
					<CardBody>
						<p class="card-text">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic. Cosby sweater eu banh mi, qui
							irure terry richardson ex squid.
						</p>
						<div class="text-end">
							<Link href={null} class="link-danger fw-medium"
								>Read More <i
									class="ri-arrow-right-line align-middle"
								/></Link>
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col xxl={4}>
				<Card class="border card-border-dark">
					<CardHeader>
						<h6 class="card-title mb-0">Handle to Forcast</h6>
					</CardHeader>
					<CardBody>
						<p class="card-text">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic. Cosby sweater eu banh mi, qui
							irure terry richardson ex squid.
						</p>
						<div class="text-end">
							<Link href={null} class="link-body fw-medium"
								>Read More <i
									class="ri-arrow-right-line align-middle"
								/></Link>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={4}>
				<Card class="border card-border-secondary">
					<CardHeader>
						<h6 class="card-title mb-0">Quality Forcast</h6>
					</CardHeader>
					<CardBody>
						<p class="card-text">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic. Cosby sweater eu banh mi, qui
							irure terry richardson ex squid.
						</p>
						<div class="text-end">
							<Link href={null} class="link-secondary fw-medium"
								>Read More <i
									class="ri-arrow-right-line align-middle"
								/></Link>
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col xxl={4}>
				<Card class="border card-border-light">
					<CardHeader>
						<h6 class="card-title mb-0">Check your E-mails</h6>
					</CardHeader>
					<CardBody>
						<p class="card-text">
							They all have something to say beyond the words on
							the page. They can come across as casual or neutral,
							exotic or graphic. Cosby sweater eu banh mi, qui
							irure terry richardson ex squid.
						</p>
						<div class="text-end">
							<Link href={null} class="link-dark fw-medium"
								>Read More <i
									class="ri-arrow-right-line align-middle"
								/></Link>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Card Groups
					</h5>
				</div>
				<div class="card-group">
					<Card class="mb-4">
						<img
							class="card-img-top img-fluid"
							src={img4}
							alt="Card cap"
						/>
						<CardBody>
							<h4 class="card-title">
								A day in the of a professional fashion designer
							</h4>
							<p class="card-text">
								This is a longer card with supporting text below
								as a natural lead-in to additional content. This
								content is a little bit longer.
							</p>
						</CardBody>
						<div class="card-footer">
							<p class="card-text">
								<small class="text-muted"
									>Last updated 3 mins ago</small
								>
							</p>
						</div>
					</Card>
					<Card class="mb-4">
						<img
							class="card-img-top img-fluid"
							src={img5}
							alt="Card cap"
						/>
						<CardBody>
							<h4 class="card-title">
								Manage white space in responsive layouts ?
							</h4>
							<p class="card-text">
								This card has supporting text below as a natural
								lead-in to additional content.
							</p>
						</CardBody>
						<div class="card-footer">
							<p class="card-text">
								<small class="text-muted"
									>Last updated 3 mins ago</small
								>
							</p>
						</div>
					</Card>
					<Card class="mb-4">
						<img
							class="card-img-top img-fluid"
							src={img6}
							alt="Card cap"
						/>
						<CardBody>
							<h4 class="card-title">
								Give your text a good structure?
							</h4>
							<p class="card-text">
								This is a wider card with supporting text below
								as a natural lead-in to additional content. This
								card has even longer content than the first to
								show that equal height action.
							</p>
						</CardBody>
						<div class="card-footer">
							<p class="card-text">
								<small class="text-muted"
									>Last updated 3 mins ago</small
								>
							</p>
						</div>
					</Card>
				</div>
			</Col>
		</Row>

		<Row class="g-3">
			<div
				class="justify-content-between d-flex align-items-center mt-3 mb-4"
			>
				<h5 class="mb-0 pb-1 text-decoration-underline">
					Grid Card Groups
				</h5>
			</div>
			<Col class="col-xxl col-6">
				<Card class="h-100">
					<CardHeader>
						<h4 class="card-title mb-0">
							A day in the of a professional fashion designer
						</h4>
					</CardHeader>
					<img
						class="img-fluid"
						src={img11}
						alt="Card cap"
					/>
					<CardBody>
						<p class="card-text">
							This may be the most commonly encountered tip I
							received from the designers I spoke with. They
							highly encourage that you use different fonts in one
							design, but do not over-exaggerate and go overboard.
						</p>
					</CardBody>
					<div class="card-footer">
						<p class="card-text">
							<small class="text-muted"
								>Last updated 3 mins ago</small>
						</p>
					</div>
				</Card>
			</Col>
			<Col class="col-xxl col-6">
				<Card class="h-100">
					<img
						class="card-img-top img-fluid"
						src={img10}
						alt="Card cap"
					/>
					<CardBody>
						<h4 class="card-title">
							Give your text a good structure?
						</h4>
						<p class="card-text">
							This is a wider card with supporting text below as a
							natural lead-in to additional content. This card has
							even longer content than the first to show that
							equal height action.
						</p>
					</CardBody>
					<div class="card-footer">
						<p class="card-text">
							<small class="text-muted"
								>Last updated 3 mins ago</small>
						</p>
					</div>
				</Card>
			</Col>
			<Col class="col-xxl col-6">
				<Card class="h-100">
					<img
						class="card-img-top img-fluid"
						src={img5}
						alt="Card cap"
					/>
					<CardBody>
						<h4 class="card-title">
							Manage white space in responsive layouts ?
						</h4>
						<p class="card-text">
							Exercitation +1 labore velit, blog sartorial PBR
							leggings next level wes anderson artisan four loko
							farm-to-table craft beer twee. ommodo enim craft
							beer mlkshk aliquip jean shorts ullamco.
						</p>
					</CardBody>
					<div class="card-footer">
						<p class="card-text">
							<small class="text-muted"
								>Last updated 3 mins ago</small>
						</p>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col sm={12}>
				<div
					class="justify-content-between d-flex align-items-center mt-5 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Cards Masonry
					</h5>
				</div>

				<Row>
					<MasonryLayout
						breakpointCols={breakpointColumnsObj}
						gap="15px"
						class="my-masonry-grid">
						<Col>
							<Card>
								<img
									src={img3}
									class="card-img-top"
									alt="..."
								/>
								<CardBody>
									<h5 class="card-title mb-1">
										Card title that wraps to a new line
									</h5>
									<p class="card-text">
										This is a longer card with supporting
										text below as a natural lead-in to
										additional content. This content is a
										little bit longer.
									</p>
								</CardBody>
							</Card>
						</Col>
						<Col>
							<Card>
								<CardBody>
									<h4 class="card-title mb-2">
										A day in the of a professional fashion
										designer
									</h4>
									<p class="card-text text-muted">
										Exercitation +1 labore velit, blog
										sartorial PBR leggings next level wes
										anderson artisan four loko farm-to-table
										craft beer twee.
									</p>
								</CardBody>
								<img
									class="card-img rounded-0 img-fluid"
									src={img8}
									alt="Card cap"
								/>
								<div class="card-footer">
									<p class="card-text mb-0">
										Last updated 3 mins ago
									</p>
								</div>
							</Card>
						</Col>
						<Col>
							<Card>
								<img
									src={img7}
									class="card-img"
									alt="..."
								/>
							</Card>
						</Col>
						<Card>
							<CardHeader>
								<button
									type="button"
									class="btn-close float-end fs-11"
									aria-label="Close"
								/>
								<h6 class="fs-15 mb-0">Hi, Erica Kernan</h6>
							</CardHeader>
							<CardBody>
								<h6 class="card-title">
									How to get creative in your work ?
								</h6>
								<p class="card-text text-muted mb-0">
									A business consulting agency is involved in
									the planning, implementation, and education
									of businesses. Miss told ham dull knew see
									she spot near can. Spirit her entire her
									called.
								</p>
							</CardBody>
							<div class="card-footer">
								<Link href={null} class="link-success float-end"
									>Read More <i
										class="ri-arrow-right-s-line align-middle ms-1 lh-1"
									/></Link
								>
								<p class="text-muted mb-0">1 days Ago</p>
							</div>
						</Card>
						<Card class="bg-primary text-white text-center p-3">
							<blockquote class="card-blockquote m-0">
								<p>
									Lorem ipsum dolor sit amet, consectetur
									adipiscing elit. Integer posuere erat.
								</p>
								<footer
									class="blockquote-footer text-white font-size-12 mt-0 mb-0"
								>
									Someone famous in <cite title="Source Title"
										>Source Title</cite
									>
								</footer>
							</blockquote>
						</Card>
						<Card class="p-3">
							<figure class="mb-0">
								<blockquote class="blockquote">
									<p class="lead">
										"A business consulting agency is
										involved in the planning,
										implementation, and education of
										businesses."
									</p>
								</blockquote>
								<figcaption
									class="blockquote-footer fs-13 text-end mb-0"
								>
									Creative Agency <cite
										title="Source Title"
										class="text-primary fw-semibold"
									> 
										Alice Mellor</cite
									>
								</figcaption>
							</figure>
						</Card>
						<div />
						<div>
							<Card>
								<CardBody>
									<h5 class="card-title mb-1">Card title</h5>
									<p class="card-text">
										This is another card with title and
										supporting text below. This card has
										some additional content to make it
										slightly taller overall.
									</p>
									<p class="card-text">
										<small class="text-muted"
											>Last updated 3 mins ago</small
										>
									</p>
								</CardBody>
							</Card>
						</div>
						<div>
							<Card class="card-success">
								<CardBody>
									<div class="d-flex align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar2}
												alt=""
												class="avatar-sm rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-3">
											<p class="card-text">
												<span class="fw-medium"
													>Charles Dickens</span
												> (Financial Analyst) started a new
												conversation.
											</p>
										</div>
									</div>
								</CardBody>
								<div class="card-footer">
									<div class="text-center">
										<Link href={null} class="link-light"
											>Connect Now <i
												class="ri-arrow-right-s-line align-middle lh-1"
											/></Link
										>
									</div>
								</div>
							</Card>
						</div>
						<div />
						<div />
						<div>
							<Card class="text-center">
								<CardBody>
									<h5 class="card-title mb-1">Card title</h5>
									<p class="card-text">
										This card has a regular title and short
										paragraphy of text below it.
									</p>
									<p class="card-text">
										<small class="text-muted"
											>Last updated 3 mins ago</small
										>
									</p>
								</CardBody>
							</Card>
						</div>
					</MasonryLayout>
				</Row>
			</Col>
		</Row>

		<Row>
			<Col class="col-12">
				<div
					class="justify-content-between d-flex align-items-center mt-3 mb-4"
				>
					<h5 class="mb-0 pb-1 text-decoration-underline">
						Stretched Link
					</h5>
				</div>
				<Row>
					<Col xl={4}>
						<Card>
							<img
								src={img3}
								class="card-img-top"
								alt="..."
							/>
							<CardBody>
								<h5 class="card-title">
									Card with stretched link
								</h5>
								<p class="card-text">
									Some quick example text to build on the card
									title and make up the bulk of the card's
									content.
								</p>
								<Link
									href={null}
									class="btn btn-primary stretched-link"
									>Go somewhere</Link
								>
							</CardBody>
						</Card>
					</Col>
					<Col xl={8}>
						<Card>
							<CardBody>
								<div class="d-flex position-relative">
									<img
										src={avatar3}
										class="flex-shrink-0 me-3 avatar-xl rounded"
										alt="..."
									/>
									<div>
										<h5 class="mt-0">
											Custom component with stretched link
										</h5>
										<p>
											This is some placeholder content for
											the custom component. It is intended
											to mimic what some real-world
											content would look like, and we're
											using it here to give the component
											a bit of body and size.
										</p>
										<Link href={null} class="stretched-link"
											>Go somewhere</Link
										>
									</div>
								</div>
							</CardBody>
						</Card>
						<Card>
							<CardBody>
								<Row class="g-0 bg-light position-relative">
									<Col md={5}>
										<img
											src={img4}
											class="rounded-start img-fluid"
											alt="..."
										/>
									</Col>
									<Col md={7} class="p-4">
										<h5 class="mt-0">
											Columns with stretched link
										</h5>
										<p>
											Another instance of placeholder
											content for this other custom
											component. It is intended to mimic
											what some real-world content would
											look like, and we're using it here
											to give the component a bit of body
											and size.
										</p>
										<Link href={null} class="stretched-link"
											>Go somewhere</Link
										>
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
