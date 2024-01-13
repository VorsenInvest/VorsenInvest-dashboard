<svelte:head>
  <title>Product Details | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import {
		Card,
		CardBody,
		Col,
		Container,
		Nav,
		NavItem,
		NavLink,
		Row,
		TabContent,
		TabPane,
		Button,
		Progress,
		Label,
		Input,
		Tooltip
	} from 'sveltestrap';

	let activeTab = 1;

	import data from '../../../common/data/ecommerce';
	import PricingWidgetList from '../PricingWidgetList.svelte';
	import img1 from '../../../assets/images/products/img-1.png';
	import img6 from '../../../assets/images/products/img-6.png';
	import img8 from '../../../assets/images/products/img-8.png';
	import img10 from '../../../assets/images/small/img-10.jpg';
	import img11 from '../../../assets/images/small/img-11.jpg';
	import img12 from '../../../assets/images/small/img-12.jpg';

	import { Swiper, SwiperSlide } from 'swiper/svelte';

	// Import Swiper styles
	import 'swiper/css';

	import 'swiper/css/free-mode';
	import 'swiper/css/navigation';
	import 'swiper/css/thumbs';

	// import required modules
	import { FreeMode, Navigation, Thumbs } from 'swiper';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';

	let thumbsSwiper = null;

	const setThumbsSwiper = (e) => {
		const [swiper] = e.detail;
		// set Thumbs swiper instance
		setTimeout(() => {
			thumbsSwiper = swiper;
		});
	};
	
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Product Details" pageTitle="Ecommerce" />

		<Row>
			<Col lg={12}>
				<Card>
					<CardBody>
						<Row class="gx-lg-5">
							<Col xl={4} md={8} class="mx-auto">
								<div class="product-img-slider sticky-side-div">
									<Swiper
										style="--swiper-navigation-color: #fff;--swiper-pagination-color: #fff"
										loop={true}
										spaceBetween={10}
										navigation={true}
										thumbs={{ swiper: thumbsSwiper }}
										modules={[FreeMode, Navigation, Thumbs]}
										class="mySwiper2 swiper product-thumbnail-slider p-2 rounded bg-light"
									>
										<SwiperSlide>
											<img
												src={img8}
												alt=""
												class="img-fluid d-block"
											/>
										</SwiperSlide>
										<SwiperSlide>
											<img
												src={img6}
												alt=""
												class="img-fluid d-block"
											/>
										</SwiperSlide>
										<SwiperSlide>
											<img
												src={img1}
												alt=""
												class="img-fluid d-block"
											/>
										</SwiperSlide>
										<SwiperSlide>
											<img
												src={img8}
												alt=""
												class="img-fluid d-block"
											/>
										</SwiperSlide>
									</Swiper>

									<div class="product-nav-slider mt-2">
										<Swiper
											on:swiper={setThumbsSwiper}
											spaceBetween={10}
											slidesPerView={4}
											freeMode={true}
											watchSlidesProgress={true}
											modules={[FreeMode, Navigation, Thumbs]}
											class="mySwiper swiper product-nav-slider mt-2 overflow-hidden"
										>
											<SwiperSlide class="rounded">
												<div class="nav-slide-item">
													<img
														src={img8}
														alt=""
														class="img-fluid d-block rounded"
													/>
												</div>
											</SwiperSlide>
											<SwiperSlide>
												<div class="nav-slide-item">
													<img
														src={img6}
														alt=""
														class="img-fluid d-block rounded"
													/>
												</div>
											</SwiperSlide>
											<SwiperSlide>
												<div class="nav-slide-item">
													<img
														src={img1}
														alt=""
														class="img-fluid d-block rounded"
													/>
												</div>
											</SwiperSlide>
											<SwiperSlide>
												<div class="nav-slide-item">
													<img
														src={img8}
														alt=""
														class="img-fluid d-block rounded"
													/>
												</div>
											</SwiperSlide>
										</Swiper>
									</div>
								</div>
								</Col>

							<Col xl={8}>
								<div class="mt-xl-0 mt-5">
									<div class="d-flex">
										<div class="flex-grow-1">
											<h5>Full Sleeve Sweatshirt for Men (Pink)</h5>
											<div class="hstack gap-3 flex-wrap">
												<div><a href="{null}" class="text-primary d-block">Tommy Hilfiger</a></div>
												<div class="vr" />
												<div class="text-muted">
													Seller : <span class="text-body fw-medium">Zoetic Fashion</span>
												</div>
												<div class="vr" />
												<div class="text-muted">
													Published : <span class="text-body fw-medium">26 Mar, 2021</span>
												</div>
											</div>
										</div>
										<div class="flex-shrink-0">
											<div>
												<a href="/ecommerce/apps-ecommerce-add-product" class="btn btn-light" id="edit-product"
													><i class="ri-pencil-fill align-bottom" /></a
												>
												<Tooltip target="edit-product" placement="top">Edit</Tooltip>
											</div>
										</div>
									</div>

									<div class="d-flex flex-wrap gap-2 align-items-center mt-3">
										<div class="text-muted fs-16">
											<span class="mdi mdi-star text-warning" />
											<span class="mdi mdi-star text-warning" />
											<span class="mdi mdi-star text-warning" />
											<span class="mdi mdi-star text-warning" />
											<span class="mdi mdi-star text-warning" />
										</div>
										<div class="text-muted">( 5.50k Customer Review )</div>
									</div>

									<Row class="mt-4">
										{#each data.productDetailsWidgets as pricingDetails}
											<PricingWidgetList {pricingDetails} />
										{/each}
									</Row>

									<Row>
										<Col xl={6}>
											<div class="mt-4">
												<h5 class="fs-14">Sizes :</h5>
												<div class="d-flex flex-wrap gap-2 btn-checkbox">
													<div data-bs-toggle="tooltip"
														data-bs-trigger="hover"
														data-bs-placement="top"
														title="Out of Stock">
														<Input
															type="radio"
															class="btn-check"
															name="productsize-radio"
															id="productsize-radio1"
															disabled />
														<Label
															class="btn btn-soft-primary avatar-xs rounded-circle p-0 d-flex justify-content-center align-items-center"
															for="productsize-radio1">S</Label>
													</div>

													<div data-bs-toggle="tooltip"
														data-bs-trigger="hover"
														data-bs-placement="top"
														title="04 Items Available"
													>
														<Input
															type="radio"
															class="btn-check"
															name="productsize-radio"
															id="productsize-radio2"
														/>
														<Label
															class="btn btn-soft-primary avatar-xs rounded-circle p-0 d-flex justify-content-center align-items-center"
															for="productsize-radio2">M</Label
														>
													</div>
													<div data-bs-toggle="tooltip"
														data-bs-trigger="hover"
														data-bs-placement="top"
														title="06 Items Available"
													>
														<Input
															type="radio"
															class="btn-check"
															name="productsize-radio"
															id="productsize-radio3"
														/>
														<Label
															class="btn btn-soft-primary avatar-xs rounded-circle p-0 d-flex justify-content-center align-items-center"
															for="productsize-radio3">L</Label
														>
													</div>

													<div data-bs-toggle="tooltip"
														data-bs-trigger="hover"
														data-bs-placement="top"
														title="Out of Stock"
													>
														<Input
															type="radio"
															class="btn-check"
															name="productsize-radio"
															id="productsize-radio4"
															disabled
														/>
														<Label
															class="btn btn-soft-primary avatar-xs rounded-circle p-0 d-flex justify-content-center align-items-center"
															for="productsize-radio4">XL</Label
														>
													</div>
												</div>
											</div>
										</Col>
										<!-- end col -->

										<Col xl={6}>
											<div class=" mt-4">
												<h5 class="fs-14">Colors :</h5>
												<div class="d-flex flex-wrap gap-2">
													<Tooltip target="color-1" placement="top">Out of Stock</Tooltip>
													<Button
														type="button"
														id="color-1"
														color=""
														class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-primary"
														disabled
													>
														<i class="ri-checkbox-blank-circle-fill" />
													</Button>

													<Tooltip target="color-2" placement="top">03 Items Available</Tooltip>

													<Button
														type="button"
														id="color-2"
														color=""
														class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-secondary"
													>
														<i class="ri-checkbox-blank-circle-fill" />
													</Button>

													<Tooltip target="color-3" placement="top">03 Items Available</Tooltip>

													<Button
														id="color-3"
														type="button"
														color=""
														class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-success"
													>
														<i class="ri-checkbox-blank-circle-fill" />
													</Button>

													<Tooltip target="color-4" placement="top">02 Items Available</Tooltip>
													<Button
														id="color-4"
														type="button"
														color=""
														class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-info"
													>
														<i class="ri-checkbox-blank-circle-fill" />
													</Button>

													<Tooltip target="color-5">01 Items Available</Tooltip>
													<Button
														id="color-5"
														type="button"
														color=""
														class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-warning"
													>
														<i class="ri-checkbox-blank-circle-fill" />
													</Button>

													<Tooltip target="color-6">04 Items Available</Tooltip>

													<Button
														id="color-6"
														type="button"
														color=""
														class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-danger"
													>
														<i class="ri-checkbox-blank-circle-fill" />
													</Button>

													<Tooltip target="color-7">03 Items Available</Tooltip>

													<Button
														id="color-7"
														type="button"
														color=""
														class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-light"
													>
														<i class="ri-checkbox-blank-circle-fill" />
													</Button>

													<Tooltip target="color-8">04 Items Available</Tooltip>

													<Button
														id="color-8"
														type="button"
														color=""
														class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-20 text-dark"
													>
														<i class="ri-checkbox-blank-circle-fill" />
													</Button>
												</div>
											</div>
										</Col>
										<!-- end col -->
									</Row>
									<!-- end row -->

									<div class="mt-4 text-muted">
										<h5 class="fs-14">Description :</h5>
										<p>
											Tommy Hilfiger men striped pink sweatshirt. Crafted with cotton. Material
											composition is 100% organic cotton. This is one of the world’s leading
											designer lifestyle brands and is internationally recognized for celebrating
											the essence of classic American cool style, featuring preppy with a twist
											designs.
										</p>
									</div>

									<Row>
										<div class="col-sm-6">
											<div class="mt-3">
												<h5 class="fs-14">Features :</h5>
												<ul class="list-unstyled">
													<li class="py-1">
														<i class="mdi mdi-circle-medium me-1 text-muted align-middle" />
														Full Sleeve
													</li>
													<li class="py-1">
														<i class="mdi mdi-circle-medium me-1 text-muted align-middle" />
														Cotton
													</li>
													<li class="py-1">
														<i class="mdi mdi-circle-medium me-1 text-muted align-middle" />
														All Sizes available
													</li>
													<li class="py-1">
														<i class="mdi mdi-circle-medium me-1 text-muted align-middle" />
														4 Different Color
													</li>
												</ul>
											</div>
										</div>
										<div class="col-sm-6">
											<div class="mt-3">
												<h5 class="fs-14">Services :</h5>
												<ul class="list-unstyled product-desc-list">
													<li class="py-1">10 Days Replacement</li>
													<li class="py-1">Cash on Delivery available</li>
												</ul>
											</div>
										</div>
									</Row>

									<div class="product-content mt-5">
										<h5 class="fs-14 mb-3">Product Description :</h5>

										<Nav tabs class="nav-tabs-custom nav-success">
											<NavItem>
												<NavLink
													style="cursor: pointer"
													class={activeTab == 1 ? 'active' : ''}
													on:click={() => (activeTab = 1)}
												>
													Specification
												</NavLink>
											</NavItem>
											<NavItem>
												<NavLink
													style="cursor: pointer"
													class={activeTab == 2 ? 'active' : ''}
													on:click={() => (activeTab = 2)}
												>
													Details
												</NavLink>
											</NavItem>
										</Nav>
										<TabContent id="nav-tabContent" class="border border-top-0 p-4">
											<TabPane id="nav-speci" tabId={1} class={activeTab == 1 ? 'active' : ''}>
												<div class="table-responsive">
													<table class="table mb-0">
														<tbody>
															<tr>
																<th scope="row" style="width: 200px;"> Category</th>
																<td>T-Shirt</td>
															</tr>
															<tr>
																<th scope="row">Brand</th>
																<td>Tommy Hilfiger</td>
															</tr>
															<tr>
																<th scope="row">Color</th>
																<td>Blue</td>
															</tr>
															<tr>
																<th scope="row">Material</th>
																<td>Cotton</td>
															</tr>
															<tr>
																<th scope="row">Weight</th>
																<td>140 Gram</td>
															</tr>
														</tbody>
													</table>
												</div>
											</TabPane>
											<TabPane tabId={2} class={activeTab == 2 ? 'active' : ''}>
												<div>
													<h5 class="font-size-16 mb-3">
														Tommy Hilfiger Sweatshirt for Men (Pink)
													</h5>
													<p>
														Tommy Hilfiger men striped pink sweatshirt. Crafted with cotton.
														Material composition is 100% organic cotton. This is one of the world’s
														leading designer lifestyle brands and is internationally recognized for
														celebrating the essence of classic American cool style, featuring preppy
														with a twist designs.
													</p>
													<div>
														<p class="mb-2">
															<i class="mdi mdi-circle-medium me-1 text-muted align-middle" />
															Machine Wash
														</p>
														<p class="mb-2">
															<i class="mdi mdi-circle-medium me-1 text-muted align-middle" />
															Fit Type: Regular
														</p>
														<p class="mb-2">
															<i class="mdi mdi-circle-medium me-1 text-muted align-middle" />
															100% Cotton
														</p>
														<p class="mb-0">
															<i class="mdi mdi-circle-medium me-1 text-muted align-middle" />
															Long sleeve
														</p>
													</div>
												</div>
											</TabPane>
										</TabContent>
									</div>
									<!-- product-content -->

									<div class="mt-5">
										<div>
											<h5 class="fs-14 mb-3">Ratings & Reviews</h5>
										</div>
										<Row class="gy-4 gx-0">
											<Col lg={4}>
												<div>
													<div class="pb-3">
														<div class="bg-light px-3 py-2 rounded-2 mb-2">
															<div class="d-flex align-items-center">
																<div class="flex-grow-1">
																	<div class="fs-16 align-middle text-warning">
																		<i class="ri-star-fill" />
																		<i class="ri-star-fill" />
																		<i class="ri-star-fill" />
																		<i class="ri-star-fill" />
																		<i class="ri-star-half-fill" />
																	</div>
																</div>
																<div class="flex-shrink-0">
																	<h6 class="mb-0">4.5 out of 5</h6>
																</div>
															</div>
														</div>
														<div class="text-center">
															<div class="text-muted">
																Total <span class="fw-medium">5.50k</span> reviews
															</div>
														</div>
													</div>

													<div class="mt-3">
														<Row class="align-items-center g-2">
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0">5 star</h6>
																</div>
															</div>
															<div class="col">
																<div class="p-2">
																	<div class="progress animated-progess progress-sm">
																		<Progress bar color="success" value={50.16} />
																	</div>
																</div>
															</div>
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0 text-muted">2758</h6>
																</div>
															</div>
														</Row>
														<!-- end row -->

														<Row class="align-items-center g-2">
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0">4 star</h6>
																</div>
															</div>
															<div class="col">
																<div class="p-2">
																	<div class="progress animated-progess progress-sm">
																		<Progress bar color="primary" value={19.32} />
																	</div>
																</div>
															</div>
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0 text-muted">1063</h6>
																</div>
															</div>
														</Row>
														<!-- end row -->

														<Row class="align-items-center g-2">
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0">3 star</h6>
																</div>
															</div>
															<div class="col">
																<div class="p-2">
																	<div class="progress animated-progess progress-sm">
																		<Progress bar color="success" value={18.12} />
																	</div>
																</div>
															</div>
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0 text-muted">997</h6>
																</div>
															</div>
														</Row>
														<!-- end row -->

														<Row class="align-items-center g-2">
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0">2 star</h6>
																</div>
															</div>
															<div class="col">
																<div class="p-2">
																	<div class="progress animated-progess progress-sm">
																		<Progress bar color="warning" value={7.42} />
																	</div>
																</div>
															</div>

															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0 text-muted">408</h6>
																</div>
															</div>
														</Row>
														<!-- end row -->

														<Row class="align-items-center g-2">
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0">1 star</h6>
																</div>
															</div>
															<div class="col">
																<div class="p-2">
																	<div class="progress animated-progess progress-sm">
																		<Progress bar color="danger" value={4.98} />
																	</div>
																</div>
															</div>
															<div class="col-auto">
																<div class="p-2">
																	<h6 class="mb-0 text-muted">274</h6>
																</div>
															</div>
														</Row>
														<!-- end row -->
													</div>
												</div>
											</Col>
											<!-- end col -->

											<Col lg={8}>
												<div class="ps-lg-4">
													<div class="d-flex flex-wrap align-items-start gap-3">
														<h5 class="fs-14">Reviews:</h5>
													</div>

													<div class="me-lg-n3 pe-lg-4" data-simplebar style="max-height: 225px">
														<ul class="list-unstyled mb-0">
															<li class="py-2">
																<div class="border border-dashed rounded p-3">
																	<div class="d-flex align-items-start mb-3">
																		<div class="hstack gap-3">
																			<div class="badge rounded-pill bg-success mb-0">
																				<i class="mdi mdi-star" />
																				4.2
																			</div>
																			<div class="vr" />
																			<div class="flex-grow-1">
																				<p class="text-muted mb-0">
																					Superb sweatshirt. I loved it. It is for winter.
																				</p>
																			</div>
																		</div>
																	</div>

																	<div class="d-flex flex-grow-1 gap-2 mb-3">
																		<a href="{null}" class="d-block">
																			<img
																				src={img12}
																				alt=""
																				class="avatar-sm rounded object-cover"
																			/>
																		</a>
																		<a href="{null}" class="d-block">
																			<img
																				src={img11}
																				alt=""
																				class="avatar-sm rounded object-cover"
																			/>
																		</a>
																		<a href="{null}" class="d-block">
																			<img
																				src={img10}
																				alt=""
																				class="avatar-sm rounded object-cover"
																			/>
																		</a>
																	</div>

																	<div class="d-flex align-items-end">
																		<div class="flex-grow-1">
																			<h5 class="fs-14 mb-0">Henry</h5>
																		</div>

																		<div class="flex-shrink-0">
																			<p class="text-muted fs-13 mb-0">12 Jul, 21</p>
																		</div>
																	</div>
																</div>
															</li>
															<li class="py-2">
																<div class="border border-dashed rounded p-3">
																	<div class="d-flex align-items-start mb-3">
																		<div class="hstack gap-3">
																			<div class="badge rounded-pill bg-success mb-0">
																				<i class="mdi mdi-star" />
																				4.0
																			</div>
																			<div class="vr" />
																			<div class="flex-grow-1">
																				<p class="text-muted mb-0">
																					Great at this price, Product quality and look is awesome.
																				</p>
																			</div>
																		</div>
																	</div>
																	<div class="d-flex align-items-end">
																		<div class="flex-grow-1">
																			<h5 class="fs-14 mb-0">Nancy</h5>
																		</div>

																		<div class="flex-shrink-0">
																			<p class="text-muted fs-13 mb-0">06 Jul, 21</p>
																		</div>
																	</div>
																</div>
															</li>

															<li class="py-2">
																<div class="border border-dashed rounded p-3">
																	<div class="d-flex align-items-start mb-3">
																		<div class="hstack gap-3">
																			<div class="badge rounded-pill bg-success mb-0">
																				<i class="mdi mdi-star" />
																				4.2
																			</div>
																			<div class="vr" />
																			<div class="flex-grow-1">
																				<p class="text-muted mb-0">Good product. I am so happy.</p>
																			</div>
																		</div>
																	</div>
																	<div class="d-flex align-items-end">
																		<div class="flex-grow-1">
																			<h5 class="fs-14 mb-0">Joseph</h5>
																		</div>

																		<div class="flex-shrink-0">
																			<p class="text-muted fs-13 mb-0">06 Jul, 21</p>
																		</div>
																	</div>
																</div>
															</li>

															<li class="py-2">
																<div class="border border-dashed rounded p-3">
																	<div class="d-flex align-items-start mb-3">
																		<div class="hstack gap-3">
																			<div class="badge rounded-pill bg-success mb-0">
																				<i class="mdi mdi-star" />
																				4.1
																			</div>
																			<div class="vr" />
																			<div class="flex-grow-1">
																				<p class="text-muted mb-0">Nice Product, Good Quality.</p>
																			</div>
																		</div>
																	</div>
																	<div class="d-flex align-items-end">
																		<div class="flex-grow-1">
																			<h5 class="fs-14 mb-0">Jimmy</h5>
																		</div>

																		<div class="flex-shrink-0">
																			<p class="text-muted fs-13 mb-0">24 Jun, 21</p>
																		</div>
																	</div>
																</div>
															</li>
														</ul>
													</div>
												</div>
											</Col>
											<!-- end col -->
										</Row>
										<!-- end Ratings & Reviews -->
									</div>
									<!-- end card body -->
								</div>
							</Col>
							<!-- end col -->
						</Row>
						<!-- end row -->
					</CardBody>
					<!-- end card body -->
				</Card>
				<!-- end card -->
			</Col>
			<!-- end col -->
		</Row>
	</Container>
</div>
