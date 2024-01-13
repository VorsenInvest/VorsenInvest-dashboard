<script>
	import {
		Container,
		Nav,
		NavItem,
		NavLink,
		TabContent,
		TabPane,
		Collapse,
		Row,
		Card,
		CardHeader,
		Col,
		Label,
	} from "sveltestrap";
	import { onMount } from "svelte";
	import Link from "svelte-link";
	import Select from "svelte-select";
	import { html } from "gridjs";
	import Grid from "gridjs-svelte";
	import RangeSlider from "svelte-range-slider-pips";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";

	let activeTab = 1;

	const SingleOptions = [
		{ value: "Watches", label: "Watches" },
		{ value: "Headset", label: "Headset" },
		{ value: "Sweatshirt", label: "Sweatshirt" },
		{ value: "20% off", label: "20% off" },
		{ value: "4 star", label: "4 star" },
	];

	import { getProducts } from "../../../helpers/fakebackend_helper";

	let productdata = [];
	let data = [];

	onMount(async () => {
		const res = await getProducts();
		productdata = res;
		data = productdata;
	});

	const columns = [
		{
			name: "#",
			width: "40px",
			formatter: (cell, row) =>
				html(
					`<div class="form-check"><input type="checkbox" value=${row.cells[0].data} class="form-check-input"/></div>`
				),
		},
		{
			id: "image",
			hidden: true,
		},
		{
			id: "name",
			hidden: true,
		},
		{
			id: "category",
			hidden: true,
		},
		{
			name: "Product",
			formatter: (cell, row) =>
				html(`<div class="d-flex align-items-center">
              <div class="flex-shrink-0 me-3">
                <div class="avatar-sm bg-light rounded p-1">
                  <img
                    src="${
						import.meta.env.VITE_PUBLIC_BASE_PATH
					}/images/products/${row.cells[1].data}"
                    alt=""
                    class="img-fluid d-block"
                  />
                </div>
              </div>
              <div class="flex-grow-1">
                <h5 class="fs-14 mb-1">
                  <Link
                    href="/ecommerce/apps-ecommerce-product-details"
                    class="text-dark"
                  >
                    ${row.cells[2].data}
                  </Link>
                </h5>
                <p class="text-muted mb-0">
                  Category :
                  <span class="fw-medium">
                    ${row.cells[3].data}
                  </span>
                </p>
              </div>
            </div>`),
		},
		{
			id: "stock",
			name: "Stock",
		},
		{
			id: "price",
			name: "Price",
			formatter: (product) => html(`$ ${product}.00`),
		},
		{
			id: "orders",
			name: "Orders",
		},
		{
			id: "rating",
			name: "Rating",
			formatter: (product) =>
				html(`<span>
						<span class="badge bg-light text-body fs-12 fw-medium">
						<i class="mdi mdi-star text-warning me-1"></i>${product}
						</span>
					</span>`),
		},
		{
			id: "publishedDate",
			name: "Published",
			formatter: (product) =>
				html(`<span>
					${product[0]}
					<small class="text-muted ms-1">${product[1]}</small>
				</span>`),
		},
		{
			name: "Action",
			formatter: (cell, row) =>
				html(`<ul class="list-inline hstack gap-2 mb-0">
              <li class="list-inline-item">
                <a
                  href="/ecommerce/apps-ecommerce-product-details"
                  class="text-primary d-inline-block"
                >
                  <i class="ri-eye-fill fs-16"></i>
                </a>
              </li>
              <li class="list-inline-item edit">
                <a
                  href="/#"
                  class="text-primary d-inline-block edit-item-btn"
                >
                  <i class="ri-pencil-fill fs-16"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a
                  href="/#"
                  class="text-danger d-inline-block remove-item-btn"
                >
                  <i class="ri-delete-bin-5-fill fs-16"></i>
                </a>
              </li>
            </ul>`),
		},
	];

	const toggleTab = (tab, type) => {
		if (activeTab !== tab) {
			let filteredProducts = productdata;
			if (type !== "all") {
				filteredProducts = productdata.filter(
					(product) => product.status === type
				);
			}
			data = filteredProducts;
		}
	};
</script>

<svelte:head>
	<title>Products | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Products" pageTitle="Ecommerce" />

		<Row>
			<Col xl={3} lg={4}>
				<Card>
					<CardHeader>
						<div class="d-flex mb-3">
							<div class="flex-grow-1">
								<h5 class="fs-16">Filters</h5>
							</div>
							<div class="flex-shrink-0">
								<Link
									href={null}
									class="text-decoration-underline"
									>Clear All</Link
								>
							</div>
						</div>

						<div class="filter-choices-input">
							<Select
								class="form-control"
								placeholder="Choose ..."
								title="idStatus"
								items={SingleOptions}
								isMulti={true}
							/>
						</div>
					</CardHeader>

					<div class="accordion accordion-flush">
						<div class="card-body border-bottom">
							<div>
								<p
									class="text-muted text-uppercase fs-12 fw-medium mb-2"
								>
									Products
								</p>
								<ul class="list-unstyled mb-0">
									<li>
										<Link href={null} class="d-flex py-1">
											<div class="flex-grow-1">
												<h5 class="fs-13 mb-0">
													Grocery
												</h5>
											</div>
										</Link>
									</li>
									<li>
										<Link
											class="d-flex py-1"
											data-bs-toggle="collapse"
											href="#filterlist-fashion"
											role="button"
											aria-expanded="true"
											aria-controls="filterlist-fashion"
										>
											<div class="flex-grow-1">
												<h5 class="fs-13 mb-0">
													Fashion
												</h5>
											</div>
											<div class="flex-shrink-0 ms-2">
												<span
													class="badge bg-light text-muted"
													>5</span
												>
											</div>
										</Link>

										<div
											class="collapse show"
											id="filterlist-fashion"
										>
											<ul class="ps-4">
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Men's Wear</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Women Western Wear</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Footwear</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Watches</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Kids</Link
													>
												</li>
											</ul>
										</div>
									</li>
									<li>
										<Link href={null} class="d-flex py-1">
											<div class="flex-grow-1">
												<h5 class="fs-13 mb-0">
													Mobiles
												</h5>
											</div>
										</Link>
									</li>
									<li>
										<Link
											class="d-flex py-1"
											data-bs-toggle="collapse"
											href="#filterlist-electronics"
											role="button"
											aria-expanded="false"
											aria-controls="filterlist-electronics"
										>
											<div class="flex-grow-1">
												<h5 class="fs-13 mb-0">
													Electronics
												</h5>
											</div>
											<div class="flex-shrink-0 ms-2">
												<span
													class="badge bg-light text-muted"
													>5</span
												>
											</div>
										</Link>

										<div
											class="collapse"
											id="filterlist-electronics"
										>
											<ul class="ps-4">
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Audio</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Computer</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Laptop</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Gaming</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Tablets</Link
													>
												</li>
											</ul>
										</div>
									</li>

									<li>
										<Link
											class="d-flex py-1"
											href="#filterlist-furniture"
										>
											<div class="flex-grow-1">
												<h5 class="fs-13 mb-0">
													Home & Furniture
												</h5>
											</div>
											<div class="flex-shrink-0 ms-2">
												<span
													class="badge bg-light text-muted"
													>6</span
												>
											</div>
										</Link>

										<div
											class="collapse"
											id="filterlist-furniture"
										>
											<ul class="ps-4">
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Home Furnishing</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Living rooms</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Kitchen & Dining</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Bedroom Room</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Home Decor</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Tools & Utility</Link
													>
												</li>
											</ul>
										</div>
									</li>

									<li>
										<Link
											class="d-flex py-1"
											href="#filterlist-appliances"
										>
											<div class="flex-grow-1">
												<h5 class="fs-13 mb-0">
													Appliances
												</h5>
											</div>
											<div class="flex-shrink-0 ms-2">
												<span
													class="badge bg-light text-muted"
													>7</span
												>
											</div>
										</Link>

										<div
											class="collapse"
											id="filterlist-appliances"
										>
											<ul class="ps-4">
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Televisions</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Washing Machines</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Air Conditioners</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Refrigerator</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Kitchen Appliances</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Home Appliances</Link
													>
												</li>
												<li>
													<Link
														href={null}
														class="d-block py-1 text-muted"
														>Premium Appliances</Link
													>
												</li>
											</ul>
										</div>
									</li>

									<li>
										<Link href={null} class="d-flex py-1">
											<div class="flex-grow-1">
												<h5 class="fs-13 mb-0">Kids</h5>
											</div>
										</Link>
									</li>
								</ul>
							</div>
						</div>

						<div class="card-body border-bottom">
							<p
								class="text-muted text-uppercase fs-12 fw-medium mb-2"
							>
								Price
							</p>

							<RangeSlider
								min={0}
								max={1000}
								pipstep={100}
								pips
								range
								values={[200, 800]}
								first="label"
								last="label"
								prefix="$"
								float={true}
							/>
						</div>

						<div class="accordion-item">
							<h2 class="accordion-header">
								<button
									class="accordion-button bg-transparent shadow-none"
									type="button"
									id="flush-headingBrands"
								>
									<span
										class="text-muted text-uppercase fs-12 fw-medium"
									>
										Brands
									</span>{" "}
									<span
										class="badge bg-success rounded-pill align-middle ms-1"
									>
										2
									</span>
								</button>
							</h2>
							<Collapse toggler="#flush-headingBrands">
								<div
									id="flush-collapseBrands"
									class="accordion-collapse collapse show"
									aria-labelledby="flush-headingBrands"
								>
									<div class="accordion-body text-body pt-0">
										<div class="search-box search-box-sm">
											<input
												type="text"
												class="form-control bg-light border-0"
												placeholder="Search Brands..."
											/>
											<i
												class="ri-search-line search-icon"
											/>
										</div>
										<div
											class="d-flex flex-column gap-2 mt-3"
										>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productBrandRadio5"
													defaultChecked
												/>
												<Label
													class="form-check-label"
													for="productBrandRadio5"
													>Boat</Label
												>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productBrandRadio4"
												/>
												<Label
													class="form-check-label"
													for="productBrandRadio4"
													>OnePlus</Label
												>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productBrandRadio3"
												/>
												<Label
													class="form-check-label"
													for="productBrandRadio3"
													>Realme</Label
												>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productBrandRadio2"
												/>
												<Label
													class="form-check-label"
													for="productBrandRadio2"
													>Sony</Label
												>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productBrandRadio1"
													defaultChecked
												/>
												<Label
													class="form-check-label"
													for="productBrandRadio1"
													>JBL</Label
												>
											</div>

											<div>
												<button
													type="button"
													class="btn btn-link text-decoration-none text-uppercase fw-medium p-0"
												>
													1,235 More
												</button>
											</div>
										</div>
									</div>
								</div>
							</Collapse>
						</div>

						<div class="accordion-item">
							<h2 class="accordion-header">
								<button
									class="accordion-button bg-transparent shadow-none collapsed"
									type="button"
									id="flush-headingDiscount"
								>
									<span
										class="text-muted text-uppercase fs-12 fw-medium"
									>
										Discount
									</span>{" "}
									<span
										class="badge bg-success rounded-pill align-middle ms-1"
									>
										1
									</span>
								</button>
							</h2>
							<Collapse toggler="#flush-headingDiscount">
								<div
									id="flush-collapseDiscount"
									class="accordion-collapse collapse show"
								>
									<div class="accordion-body text-body pt-1">
										<div class="d-flex flex-column gap-2">
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productdiscountRadio6"
												/>
												<Label
													class="form-check-label"
													for="productdiscountRadio6"
												>
													50% or more
												</Label>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productdiscountRadio5"
												/>
												<Label
													class="form-check-label"
													for="productdiscountRadio5"
												>
													40% or more
												</Label>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productdiscountRadio4"
												/>
												<Label
													class="form-check-label"
													for="productdiscountRadio4"
												>
													30% or more
												</Label>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productdiscountRadio3"
													defaultChecked
												/>
												<Label
													class="form-check-label"
													for="productdiscountRadio3"
												>
													20% or more
												</Label>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productdiscountRadio2"
												/>
												<Label
													class="form-check-label"
													for="productdiscountRadio2"
												>
													10% or more
												</Label>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productdiscountRadio1"
												/>
												<Label
													class="form-check-label"
													for="productdiscountRadio1"
												>
													Less than 10%
												</Label>
											</div>
										</div>
									</div>
								</div>
							</Collapse>
						</div>

						<div class="accordion-item">
							<h2 class="accordion-header">
								<button
									class="accordion-button bg-transparent shadow-none collapsed"
									type="button"
									id="flush-headingRating"
								>
									<span
										class="text-muted text-uppercase fs-12 fw-medium"
									>
										Rating
									</span>{" "}
									<span
										class="badge bg-success rounded-pill align-middle ms-1"
									>
										1
									</span>
								</button>
							</h2>

							<Collapse toggler="#flush-headingRating">
								<div
									id="flush-collapseRating"
									class="accordion-collapse collapse show"
									aria-labelledby="flush-headingRating"
								>
									<div class="accordion-body text-body">
										<div class="d-flex flex-column gap-2">
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productratingRadio4"
													defaultChecked
												/>
												<Label
													class="form-check-label"
													for="productratingRadio4"
												>
													<span class="text-muted">
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star"
														/>
													</span>{" "}
													4 & Above
												</Label>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productratingRadio3"
												/>
												<Label
													class="form-check-label"
													for="productratingRadio3"
												>
													<span class="text-muted">
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star"
														/>
														<i
															class="mdi mdi-star"
														/>
													</span>{" "}
													3 & Above
												</Label>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productratingRadio2"
												/>
												<Label
													class="form-check-label"
													for="productratingRadio2"
												>
													<span class="text-muted">
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star"
														/>
														<i
															class="mdi mdi-star"
														/>
														<i
															class="mdi mdi-star"
														/>
													</span>{" "}
													2 & Above
												</Label>
											</div>
											<div class="form-check">
												<input
													class="form-check-input"
													type="checkbox"
													id="productratingRadio1"
												/>
												<Label
													class="form-check-label"
													for="productratingRadio1"
												>
													<span class="text-muted">
														<i
															class="mdi mdi-star text-warning"
														/>
														<i
															class="mdi mdi-star"
														/>
														<i
															class="mdi mdi-star"
														/>
														<i
															class="mdi mdi-star"
														/>
														<i
															class="mdi mdi-star"
														/>
													</span>{" "}
													1
												</Label>
											</div>
										</div>
									</div>
								</div>
							</Collapse>
						</div>
					</div>
				</Card>
			</Col>

			<div class="col-xl-9 col-lg-8">
				<div>
					<div class="card">
						<div class="card-header border-0">
							<div class="row g-4">
								<div class="col-sm-auto">
									<div>
										<Link
											href="/ecommerce/apps-ecommerce-add-product"
											class="btn btn-success"
										>
											<i
												class="ri-add-line align-bottom me-1"
											/> Add Product
										</Link>
									</div>
								</div>
								<div class="col-sm">
									<div class="d-flex justify-content-sm-end">
										<div class="search-box ms-2">
											<input
												type="text"
												class="form-control"
												placeholder="Search Products..."
											/>
											<i
												class="ri-search-line search-icon"
											/>
										</div>
									</div>
								</div>
							</div>
						</div>

						<div class="card-header">
							<div class="row align-items-center">
								<div class="col">
									<Nav
										class="nav-tabs-custom card-header-tabs border-bottom-0"
										role="tablist"
									>
										<NavItem>
											<NavLink
												on:click={() => {
													activeTab = 1;
													toggleTab("1", "all");
												}}
												active={activeTab == 1}
												class="fw-semibold"
												href={null}
											>
												All{" "}
												<span
													class="badge bg-danger-subtle text-danger align-middle rounded-pill ms-1"
												>
													12
												</span>
											</NavLink>
										</NavItem>
										<NavItem>
											<NavLink
												on:click={() => {
													activeTab = 2;
													toggleTab("2", "published");
												}}
												active={activeTab == 2}
												class="fw-semibold"
												href={null}
											>
												Published{" "}
												<span
													class="badge bg-danger-subtle text-danger align-middle rounded-pill ms-1"
												>
													5
												</span>
											</NavLink>
										</NavItem>
										<NavItem>
											<NavLink
												on:click={() => {
													activeTab = 3;
													toggleTab("3", "draft");
												}}
												active={activeTab == 3}
												class="fw-semibold"
												href={null}
											>
												Draft
											</NavLink>
										</NavItem>
									</Nav>
								</div>
								<div class="col-auto">
									<div id="selection-element">
										<div
											class="my-n1 d-flex align-items-center text-muted"
										>
											Select{" "}
											<div
												id="select-content"
												class="text-body fw-semibold px-1"
											/>
											{" "}
											Result{" "}
											<button
												type="button"
												class="btn btn-link link-danger p-0 ms-3"
											>
												Remove
											</button>
										</div>
									</div>
								</div>
							</div>
						</div>

						<div class="card-body">
							<TabContent class="text-muted">
								<TabPane class="active">
									<div
										id="table-product-list-all"
										class="table-card gridjs-border-none"
									>
										{#if (data.length || []) > 0}
											<Grid
												{data}
												{columns}
												className={{ th: "text-muted" }}
												pagination={{
													enabled: true,
													limit: 10,
												}}
											/>
										{:else}
											<div class="py-4 text-center">
												<div>
													<lord-icon
														src="//cdn.lordicon.com/msoeawqm.json"
														trigger="loop"
														colors="primary:#405189,secondary:#0ab39c"
														style="width: 72px;height: 72px"
													/>
												</div>

												<div class="mt-4">
													<h5>
														Sorry! No Result Found
													</h5>
												</div>
											</div>
										{/if}
									</div>
								</TabPane>
							</TabContent>
						</div>
					</div>
				</div>
			</div>
		</Row>
	</Container>
</div>

<style global>
	@import "//cdn.jsdelivr.net/npm/gridjs/dist/theme/mermaid.min.css";
</style>
