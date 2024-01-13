<svelte:head>
  <title>Seller Details | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';

	import {
		CardBody,
		Container,
		CardHeader,
		Col,
		Card,
		Row,
		Input,
		Progress,
		Table,
		Button
	} from 'sveltestrap';

	import Link from 'svelte-link';

	import ecommerceData from '../../../common/data/ecommerce';

	import ReviewSlider from '../../../Components/Common/ReviewSlider.svelte';

	import Counter from '../../../Components/Common/CounterPage.svelte';
	import RevenueCharts from "../../dashboard/DashboardEcommerceCharts.svelte";
	import img2 from '../../../assets/images/companies/img-2.png'

	const data = ecommerceData.productsData;

	import { html } from 'gridjs';
	import Grid from 'gridjs-svelte';

	const columns = [
		{
			name: '#',
			width: '40px',
			formatter: (cell) => html(`<div class="form-check"><input type="checkbox" class="form-check-input"/></div>`)
		},
		{
			id: 'image',
			hidden: true
		},
		{
			id: 'name',
			hidden: true
		},
		{
			id: 'category',
			hidden: true
		},
		{
			name: 'Product',
			formatter: (cell, row) =>
				html(`<div class="d-flex align-items-center">
              <div class="flex-shrink-0 me-3">
                <div class="avatar-sm bg-light rounded p-1">
                  <img
                    src=${row.cells[1].data}
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
            </div>`)
		},
		{
			id: 'stock',
			name: 'Stock'
		},
		{
			id: 'price',
			name: 'Price',
			formatter: (product) => html(`$ ${product}.00`)
		},
		{
			id: 'orders',
			name: 'Orders'
		},
		{
			id: 'rating',
			name: 'Rating',
			formatter: (product) =>
				html(`<span>
        <span class="badge bg-light text-body fs-12 fw-medium">
          <i class="mdi mdi-star text-warning me-1"></i>${product}
        </span>
      </span>`)
		},
		{
			id: 'publishedDate',
			name: 'Published',
			formatter: (product) =>
				html(`<span>
        ${product[0]}
        <small class="text-muted ms-1">${product[1]}</small>
      </span>`)
		},
		{
            name: 'Action',
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
                  href="#"
                  class="text-primary d-inline-block edit-item-btn"
                >
                  <i class="ri-pencil-fill fs-16"></i>
                </a>
              </li>
              <li class="list-inline-item">
                <a
                  href="#"
                  class="text-danger d-inline-block remove-item-btn"
                >
                  <i class="ri-delete-bin-5-fill fs-16"></i>
                </a>
              </li>
            </ul>`)
        }
        
	];
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Seller Details" pageTitle="Ecommerce" />
		<Counter />

		<Row>
			<div class="col-xxl-3">
				<Card>
					<CardBody class="p-4">
						<div>
							<div class="flex-shrink-0 avatar-md mx-auto">
								<div class="avatar-title bg-light rounded">
									<img src={img2} alt="" height="50" />
								</div>
							</div>
							<div class="mt-4 text-center">
								<h5 class="mb-1">Force Medicines</h5>
								<p class="text-muted">Since 1987</p>
							</div>
							<div class="table-responsive">
								<Table class="table mb-0 table-borderless">
									<tbody>
										<tr>
											<th><span class="fw-medium">Owner Name</span></th>
											<td>David Marshall</td>
										</tr>
										<tr>
											<th><span class="fw-medium">Company Type</span></th>
											<td>Partnership</td>
										</tr>
										<tr>
											<th><span class="fw-medium">Email</span></th>
											<td>forcemedicines@gamil.com</td>
										</tr>
										<tr>
											<th><span class="fw-medium">Website</span></th>
											<td><Link href="{null}" class="link-primary">www.forcemedicines.com</Link></td>
										</tr>
										<tr>
											<th><span class="fw-medium">Contact No.</span></th>
											<td>+(123) 9876 654 321</td>
										</tr>
										<tr>
											<th><span class="fw-medium">Fax</span></th>
											<td>+1 999 876 5432</td>
										</tr>
										<tr>
											<th><span class="fw-medium">Location</span></th>
											<td>United Kingdom</td>
										</tr>
									</tbody>
								</Table>
							</div>
						</div>
					</CardBody>
					<!--end card-body-->
					<CardBody class="border-top border-top-dashed p-4">
						<div>
							<h6 class="text-muted text-uppercase fw-semibold mb-4">Customer Reviews</h6>
							<div>
								<div>
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
											Total <span class="fw-medium">5.50k</span>
											reviews
										</div>
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
												<div class="progress animated-progess progress-sm">
													<Progress bar color="success" value={50.16} />
												</div>
											</div>
										</div>
										<div class="col-auto">
											<div class="p-1">
												<h6 class="mb-0 text-muted">2758</h6>
											</div>
										</div>
									</Row>
									<!-- end row -->

									<Row class="align-items-center g-2">
										<div class="col-auto">
											<div class="p-1">
												<h6 class="mb-0">4 star</h6>
											</div>
										</div>
										<div class="col">
											<div class="p-1">
												<div class="progress animated-progess progress-sm">
													<Progress bar color="success" value={29.32} />
												</div>
											</div>
										</div>
										<div class="col-auto">
											<div class="p-1">
												<h6 class="mb-0 text-muted">1063</h6>
											</div>
										</div>
									</Row>
									<!-- end row -->

									<Row class="align-items-center g-2">
										<div class="col-auto">
											<div class="p-1">
												<h6 class="mb-0">3 star</h6>
											</div>
										</div>
										<div class="col">
											<div class="p-1">
												<div class="progress animated-progess progress-sm">
													<Progress bar color="warning" value={18.12} />
												</div>
											</div>
										</div>
										<div class="col-auto">
											<div class="p-1">
												<h6 class="mb-0 text-muted">997</h6>
											</div>
										</div>
									</Row>
									<!-- end row -->

									<Row class="align-items-center g-2">
										<div class="col-auto">
											<div class="p-1">
												<h6 class="mb-0">2 star</h6>
											</div>
										</div>
										<div class="col">
											<div class="p-1">
												<div class="progress animated-progess progress-sm">
													<Progress bar color="success" value={4.98} />
												</div>
											</div>
										</div>

										<div class="col-auto">
											<div class="p-1">
												<h6 class="mb-0 text-muted">227</h6>
											</div>
										</div>
									</Row>
									<!-- end row -->

									<Row class="align-items-center g-2">
										<div class="col-auto">
											<div class="p-1">
												<h6 class="mb-0">1 star</h6>
											</div>
										</div>
										<div class="col">
											<div class="p-1">
												<div class="progress animated-progess progress-sm">
													<Progress bar color="danger" value={7.42} />
												</div>
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
						</div>
					</CardBody>
					<!--end card-body-->
					<CardBody class="p-4 border-top border-top-dashed">
						<h6 class="text-muted text-uppercase fw-semibold mb-4">Products Reviews</h6>
						<!-- Swiper -->
						<ReviewSlider />
						<div class="text-center mt-3">
							<Link href="{null}" class="link-primary"
								>View All Reviews <i class="ri-arrow-right-line align-bottom ms-1" /></Link>
						</div>
					</CardBody>
					<CardBody class="p-4 border-top border-top-dashed">
						<h6 class="text-muted text-uppercase fw-semibold mb-4">Contact Support</h6>
						<form action="#">
							<div class="mb-3">
								<Input
									type="textarea"
									class="form-control"
									id="exampleFormControlTextarea1"
									rows="4"
									placeholder="Enter your messages..."
								/>
							</div>
							<div class="text-end">
								<Button color="primary"
									><i class="ri-mail-send-line align-bottom me-1" /> Send Messages</Button
								>
							</div>
						</form>
					</CardBody>
					<!--end card-body-->
				</Card>
				<!--end card-->
			</div>
			<!--end col-->

			<div class="col-xxl-9">
				<!-- <Revenue /> -->
				<Card>
					<CardHeader class="border-0 align-items-center d-flex">
						<h4 class="card-title mb-0 flex-grow-1">Revenue</h4>
						<div>
							<button type="button" class="btn btn-soft-info btn-sm">
								ALL
							</button>
							<button type="button" class="btn btn-soft-info btn-sm"> 1M </button>
							<button type="button" class="btn btn-soft-info btn-sm"> 6M </button>
							<button type="button" class="btn btn-soft-primary btn-sm">
								1Y
							</button>
						</div>
					</CardHeader>
					<CardHeader class="p-0 border-0 bg-light-subtle">
						<Row class="g-0 text-center">
							<Col xs={6} sm={3}>
								<div class="p-3 border border-dashed border-start-0">
									<h5 class="mb-1">
										<span class="counter-value" data-target="7585">0</span>
									</h5>
									<p class="text-muted mb-0">Orders</p>
								</div>
							</Col>
							<Col xs={6} sm={3}>
								<div class="p-3 border border-dashed border-start-0">
									<h5 class="mb-1">
										$<span class="counter-value" data-target="22.89">0</span
										>k
									</h5>
									<p class="text-muted mb-0">Earnings</p>
								</div>
							</Col>
							<Col xs={6} sm={3}>
								<div class="p-3 border border-dashed border-start-0">
									<h5 class="mb-1">
										<span class="counter-value" data-target="367">0</span>
									</h5>
									<p class="text-muted mb-0">Refunds</p>
								</div>
							</Col>
							<Col xs={6} sm={3}>
								<div
									class="p-3 border border-dashed border-start-0 border-end-0"
								>
									<h5 class="mb-1 text-success">
										<span class="counter-value" data-target="18.92">0</span
										>%
									</h5>
									<p class="text-muted mb-0">Conversation Ratio</p>
								</div>
							</Col>
						</Row>
					</CardHeader>
					<CardBody class="p-0 pb-2">
						<div class="w-100">
							<div dir="ltr">
								<RevenueCharts
									dataColors={["--vz-info", "--vz-primary", "--vz-danger"]}
								/>
							</div>
						</div>
					</CardBody>
				</Card>

				<Row class=" g-4 mb-3">
					<div class="col-sm-auto">
						<div>
							<Link href="/ecommerce/apps-ecommerce-add-product" class="btn btn-success"
								><i class="ri-add-line align-bottom me-1" /> Add New</Link>
						</div>
					</div>
					<div class="col-sm">
						<div class="d-flex justify-content-sm-end">
							<div class="search-box ms-2">
								<Input type="text" class="form-control" placeholder="Search Products..." />
								<i class="ri-search-line search-icon" />
							</div>
						</div>
					</div>
				</Row>
				<Card>
					<CardBody>
						{#if (ecommerceData.productsData.length || []) > 0}
							<div class="table-card gridjs-border-none">
								<Grid {data} {columns} className={{th: 'text-muted'}} pagination={{ enabled: true, limit: 10 }} />
							</div>
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
									<h5>Sorry! No Result Found</h5>
								</div>
							</div>
						{/if}
					</CardBody>
				</Card>
			</div>
			<!--end col-->
		</Row>
	</Container>
</div>