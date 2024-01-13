<script>
	import {
		Card,
		CardBody,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Row,
		Dropdown,
	} from "sveltestrap";
	import img4 from "../../../assets/images/companies/img-4.png";
</script>

<Col lg={12}>
	<Card class="mt-n4 mx-n4 mb-n5">
		<div class="bg-warning-subtle">
			<CardBody class="pb-4 mb-5">
				<Row>
					<div class="col-md">
						<Row class="align-items-center">
							<div class="col-md-auto">
								<div class="avatar-md mb-md-0 mb-4">
									<div
										class="avatar-title bg-white rounded-circle"
									>
										<img
											src={img4}
											alt=""
											class="avatar-sm"
										/>
									</div>
								</div>
							</div>
							<!--end col-->
							<div class="col-md">
								<h4 class="fw-semibold" id="ticket-title">
									#VLZ135 - Create an Excellent UI for a
									Dashboard
								</h4>
								<div class="hstack gap-3 flex-wrap">
									<div class="text-muted">
										<i
											class="ri-building-line align-bottom me-1"
										/><span id="ticket-client"
											>Themesbrand</span
										>
									</div>
									<div class="vr" />
									<div class="text-muted">
										Create Date : <span
											class="fw-medium"
											id="create-date">20 Dec, 2021</span
										>
									</div>
									<div class="vr" />
									<div class="text-muted">
										Due Date : <span
											class="fw-medium"
											id="due-date">29 Dec, 2021</span
										>
									</div>
									<div class="vr" />
									<div
										class="badge rounded-pill bg-info fs-12"
										id="ticket-status"
									>
										New
									</div>
									<div
										class="badge rounded-pill bg-danger fs-12"
										id="ticket-priority"
									>
										High
									</div>
								</div>
							</div>
							<!--end col-->
						</Row>
						<!--end row-->
					</div>
					<!--end col-->
					<div class="col-md-auto mt-md-0 mt-4">
						<div class="hstack gap-1 flex-wrap">
							<button
								type="button"
								class="btn avatar-xs mt-n1 p-0 favourite-btn active"
							>
								<span class="avatar-title bg-transparent fs-15">
									<i class="ri-star-fill" />
								</span>
							</button>
							<Dropdown>
								<DropdownToggle
									tag="button"
									color=""
									type="button"
									class="btn py-0 fs-16 text-body"
								>
									<i class="ri-share-line" />
								</DropdownToggle>

								<DropdownMenu>
									<li>
										<DropdownItem
											><i
												class="ri-eye-fill align-bottom me-2 text-muted"
											/> View</DropdownItem
										>
									</li>
									<li>
										<DropdownItem
											><i
												class="ri-share-forward-fill align-bottom me-2 text-muted"
											/> Share with</DropdownItem
										>
									</li>
									<li>
										<DropdownItem
											><i
												class="ri-delete-bin-fill align-bottom me-2 text-muted"
											/> Delete</DropdownItem
										>
									</li>
								</DropdownMenu>
							</Dropdown>
							<button
								type="button"
								class="btn py-0 fs-16 text-body"
							>
								<i class="ri-flag-line" />
							</button>
						</div>
					</div>
					<!--end col-->
				</Row>
				<!--end row-->
			</CardBody>
			<!-- end card body -->
		</div>
	</Card>
	<!-- end card -->
</Col>
<!-- end col -->
