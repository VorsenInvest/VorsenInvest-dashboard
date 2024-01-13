<script>
	import { Card, CardBody, Row, Progress } from "sveltestrap";
	import data from "../../common/data/dashboardEcommerce";
	import ReviewSlider from "../../Components/Common/ReviewSlider.svelte";
	import img1 from '../../assets/images/products/img-1.png';
	import img2 from '../../assets/images/products/img-2.png';
	import img8 from '../../assets/images/products/img-8.png';
	import avatar2 from '../../assets/images/users/avatar-2.jpg';
	import avatar3 from '../../assets/images/users/avatar-3.jpg';
	import giftbox from '../../assets/images/giftbox.png';
</script>

<div class="col-auto layout-rightside-col d-none" id="layout-rightside-coll">
	<div class="overlay" />
	<div class="layout-rightside">
		<Card class="h-100 rounded-0">
			<CardBody class="p-0">
				<div class="p-3">
					<h6 class="text-muted mb-0 text-uppercase fw-semibold">
						Recent Activity
					</h6>
				</div>
				<div data-simplebar style="max-height: 410px;" class="p-3 pt-0">
					<div class="acitivity-timeline acitivity-main">
						<div class="acitivity-item d-flex">
							<div class="flex-shrink-0 avatar-xs acitivity-avatar">
								<div class="avatar-title bg-success-subtle text-success rounded-circle">
									<i class="ri-shopping-cart-2-line" />
								</div>
							</div>
							<div class="flex-grow-1 ms-3">
								<h6 class="mb-1 lh-base">
									Purchase by James Price
								</h6>
								<p class="text-muted mb-1">
									Product noise evolve smartwatch{" "}
								</p>
								<small class="mb-0 text-muted">02:14 PM Today</small>
							</div>
						</div>
						<div class="acitivity-item py-3 d-flex">
							<div class="flex-shrink-0 avatar-xs acitivity-avatar">
								<div class="avatar-title bg-danger-subtle text-danger rounded-circle">
									<i class="ri-stack-fill" />
								</div>
							</div>
							<div class="flex-grow-1 ms-3">
								<h6 class="mb-1 lh-base">
									Added new{" "}
									<span class="fw-semibold">style collection</span>
								</h6>
								<p class="text-muted mb-1">
									By Nesta Technologies
								</p>
								<div class="d-inline-flex gap-2 border border-dashed p-2 mb-2">
									<a href="/ecommerce/apps-ecommerce-product-details" class="bg-light rounded p-1">
										<img src={img8} alt="" class="img-fluid d-block" />
									</a>
									<a href="/ecommerce/apps-ecommerce-product-details" class="bg-light rounded p-1">
										<img src={img2} alt="" class="img-fluid d-block" />
									</a>
									<a href="/ecommerce/apps-ecommerce-product-details" class="bg-light rounded p-1">
										<img src={img1} alt="" class="img-fluid d-block" />
									</a>
								</div>
								<p class="mb-0 text-muted">
									<small>9:47 PM Yesterday</small>
								</p>
							</div>
						</div>
						<div class="acitivity-item py-3 d-flex">
							<div class="flex-shrink-0">
								<img src={avatar2} alt="" class="avatar-xs rounded-circle acitivity-avatar" />
							</div>
							<div class="flex-grow-1 ms-3">
								<h6 class="mb-1 lh-base">
									Natasha Carey have liked the products
								</h6>
								<p class="text-muted mb-1">
									Allow users to like products in your
									WooCommerce store.
								</p>
								<small class="mb-0 text-muted">25 Dec, 2021</small>
							</div>
						</div>
						<div class="acitivity-item py-3 d-flex">
							<div class="flex-shrink-0">
								<div class="avatar-xs acitivity-avatar">
									<div class="avatar-title rounded-circle bg-secondary">
										<i class="mdi mdi-sale fs-14" />
									</div>
								</div>
							</div>
							<div class="flex-grow-1 ms-3">
								<h6 class="mb-1 lh-base">
									Today offers by{" "}
									<a href="/ecommerce/apps-ecommerce-seller-details" class="link-secondary">
										Digitech Galaxy
									</a>
								</h6>
								<p class="text-muted mb-2">
									Offer is valid on orders of Rs.500 Or above
									for selected products only.
								</p>
								<small class="mb-0 text-muted">12 Dec, 2021</small>
							</div>
						</div>
						<div class="acitivity-item py-3 d-flex">
							<div class="flex-shrink-0">
								<div class="avatar-xs acitivity-avatar">
									<div class="avatar-title rounded-circle bg-danger-subtle text-danger">
										<i class="ri-bookmark-fill" />
									</div>
								</div>
							</div>
							<div class="flex-grow-1 ms-3">
								<h6 class="mb-1 lh-base">Favoried Product</h6>
								<p class="text-muted mb-2">
									Esther James have favorited product.
								</p>
								<small class="mb-0 text-muted">25 Nov, 2021</small>
							</div>
						</div>
						<div class="acitivity-item py-3 d-flex">
							<div class="flex-shrink-0">
								<div class="avatar-xs acitivity-avatar">
									<div class="avatar-title rounded-circle bg-secondary">
										<i class="mdi mdi-sale fs-14" />
									</div>
								</div>
							</div>
							<div class="flex-grow-1 ms-3">
								<h6 class="mb-1 lh-base">
									Flash sale starting{" "}
									<span class="text-primary">Tomorrow.</span>
								</h6>
								<p class="text-muted mb-0">
									Flash sale by{" "}
									<a href="{null}" class="link-secondary fw-medium">
										Zoetic Fashion
									</a>
								</p>
								<small class="mb-0 text-muted">22 Oct, 2021</small>
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
								<h6 class="mb-1 lh-base">
									Monthly sales report
								</h6>
								<p class="text-muted mb-2">
									<span class="text-danger">2 days left</span>{" "}
									notification to submit the monthly sales report.{" "}
									<a href="{null}" class="link-warning text-decoration-underline">
										Reports Builder
									</a>
								</p>
								<small class="mb-0 text-muted">15 Oct</small>
							</div>
						</div>
						<div class="acitivity-item d-flex">
							<div class="flex-shrink-0">
								<img src={avatar3} alt="" class="avatar-xs rounded-circle acitivity-avatar" />
							</div>
							<div class="flex-grow-1 ms-3">
								<h6 class="mb-1 lh-base">
									Frank Hook Commented
								</h6>
								<p class="text-muted mb-2 fst-italic">
									" A product that has reviews is more likable
									to be sold than a product. "
								</p>
								<small class="mb-0 text-muted">26 Aug, 2021</small>
							</div>
						</div>
					</div>
				</div>

				<div class="p-3 mt-2">
					<h6 class="text-muted mb-3 text-uppercase fw-semibold">
						Top 10 Categories
					</h6>

					<ol class="ps-3 text-muted">
						{#each data.topCategories as item}
						<li class="py-1">
							<a href="{null}" class="text-muted">
								{item.category}{" "}
								<span class="float-end">({item.total})</span>
							</a>
						</li>
						{/each}
					</ol>
					<div class="mt-3 text-center">
						<a href="{null}" class="text-muted text-decoration-underline">
							View all Categories
						</a>
					</div>
				</div>
				<div class="p-3">
					<h6 class="text-muted mb-3 text-uppercase fw-semibold">
						Products Reviews
					</h6>
					<ReviewSlider />
				</div>

				<div class="p-3">
					<h6 class="text-muted mb-3 text-uppercase fw-semibold">
						Customer Reviews
					</h6>
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

					<div class="mt-3">
						<Row class="align-items-center g-2">
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0">5 star</h6>
								</div>
							</div>
							<div class="col">
								<div class="p-1">
									<Progress bar class="animated-progess progress-sm" color="success" value="50.16" />
								</div>
							</div>
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0 text-muted">2758</h6>
								</div>
							</div>
						</Row>

						<Row class="align-items-center g-2">
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0">4 star</h6>
								</div>
							</div>
							<div class="col">
								<div class="p-1">
									<Progress bar class="animated-progess progress-sm" color="success" value="29.32" />
								</div>
							</div>
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0 text-muted">1063</h6>
								</div>
							</div>
						</Row>

						<Row class="align-items-center g-2">
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0">3 star</h6>
								</div>
							</div>
							<div class="col">
								<div class="p-1">
									<Progress bar class="animated-progess progress-sm" color="warning" value="18.12" />
								</div>
							</div>
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0 text-muted">997</h6>
								</div>
							</div>
						</Row>

						<Row class="align-items-center g-2">
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0">2 star</h6>
								</div>
							</div>
							<div class="col">
								<div class="p-1">
									<Progress bar class="animated-progess progress-sm" color="success" value="4.98" />
								</div>
							</div>

							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0 text-muted">227</h6>
								</div>
							</div>
						</Row>

						<Row class="align-items-center g-2">
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0">1 star</h6>
								</div>
							</div>
							<div class="col">
								<div class="p-1">
									<Progress bar class="animated-progess progress-sm" color="danger" value="7.42" />
								</div>
							</div>
							<div class="col-auto">
								<div class="p-1">
									<h6 class="mb-0 text-muted">408</h6>
								</div>
							</div>
						</Row>
					</div>
				</div>

				<Card class="sidebar-alert bg-light border-0 text-center mx-4 mb-0 mt-3">
					<CardBody>
						<img src={giftbox} alt="" />
						<div class="mt-4">
							<h5>Invite New Seller</h5>
							<p class="text-muted lh-base">
								Refer a new seller to us and earn $100 per
								refer.
							</p>
							<button type="button" class="btn btn-primary btn-label rounded-pill">
								<i class="ri-mail-fill label-icon align-middle rounded-pill fs-16 me-2" />{" "}
								Invite Now
							</button>
						</div>
					</CardBody>
				</Card>
			</CardBody>
		</Card>
	</div>
</div>