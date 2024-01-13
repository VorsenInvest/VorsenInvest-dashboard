<script>
	import {
		Card,
		CardBody,
		CardHeader,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Nav,
		NavItem,
		NavLink,
		TabContent,
		TabPane,
		Dropdown,
		Label,
	} from "sveltestrap";
	import Link from "svelte-link";
	let activeTab = 1;

	import avatar6 from "../../assets/images/users/avatar-6.jpg";
	import avatar7 from "../../assets/images/users/avatar-7.jpg";
	import avatar8 from "../../assets/images/users/avatar-8.jpg";
	import avatar10 from "../../assets/images/users/avatar-10.jpg";
	import img4 from "../../assets/images/small/img-4.jpg";
	import img5 from "../../assets/images/small/img-5.jpg";
</script>

<Card>
	<CardHeader>
		<div>
			<Nav
				class="nav-tabs-custom rounded card-header-tabs border-bottom-0"
			>
				<NavItem>
					<NavLink
						on:click={() => (activeTab = 1)}
						active={activeTab == 1}>Comments (5)</NavLink
					>
				</NavItem>
				<NavItem>
					<NavLink
						on:click={() => (activeTab = 2)}
						active={activeTab == 2}
					>
						Attachments File (4)
					</NavLink>
				</NavItem>
				<NavItem>
					<NavLink
						on:click={() => (activeTab = 3)}
						active={activeTab == 3}
					>
						Time Entries (9 hrs 13 min)
					</NavLink>
				</NavItem>
			</Nav><!--end nav-->
		</div>
	</CardHeader>
	<CardBody>
		<TabContent>
			<TabPane tabId={1} class={activeTab == 1 ? "active" : ""}>
				<h5 class="card-title mb-4">Comments</h5>
				<div
					data-simplebar
					style="height: 508px;"
					class="px-3 mx-n3 mb-2"
				>
					<div class="d-flex mb-4">
						<div class="flex-shrink-0">
							<img
								src={avatar7}
								alt=""
								class="avatar-xs rounded-circle"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h5 class="fs-15">
								<Link href="/pages/profile/simple"
									>Joseph Parker</Link
								>
								<small class="text-muted"
									>20 Dec 2021 - 05:47AM</small
								>
							</h5>
							<p class="text-muted">
								I am getting message from customers that when
								they place order always get error message .
							</p>
							<Link href={null} class="badge text-muted bg-light"
								><i class="mdi mdi-reply" /> Reply</Link
							>
							<div class="d-flex mt-4">
								<div class="flex-shrink-0">
									<img
										src={avatar10}
										alt=""
										class="avatar-xs rounded-circle"
									/>
								</div>
								<div class="flex-grow-1 ms-3">
									<h5 class="fs-15">
										<Link href="/pages/profile/simple"
											>Tonya Noble</Link
										>
										<small class="text-muted"
											>22 Dec 2021 - 02:32PM</small
										>
									</h5>
									<p class="text-muted">
										Please be sure to check your Spam
										mailbox to see if your email filters
										have identified the email from Dell as
										spam.
									</p>
									<Link
										href={null}
										class="badge text-muted bg-light"
										><i class="mdi mdi-reply" /> Reply</Link
									>
								</div>
							</div>
						</div>
					</div>
					<div class="d-flex mb-4">
						<div class="flex-shrink-0">
							<img
								src={avatar8}
								alt=""
								class="avatar-xs rounded-circle"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h5 class="fs-15">
								<Link href="/pages/profile/simple"
									>Thomas Taylor</Link
								>
								<small class="text-muted"
									>24 Dec 2021 - 05:20PM</small
								>
							</h5>
							<p class="text-muted">
								If you have further questions, please contact
								Customer Support from the “Action Menu” on your <Link
									href={null}
									class="text-decoration-underline"
									>Online Order Support</Link
								>.
							</p>
							<Link href={null} class="badge text-muted bg-light"
								><i class="mdi mdi-reply" /> Reply</Link
							>
						</div>
					</div>
					<div class="d-flex">
						<div class="flex-shrink-0">
							<img
								src={avatar10}
								alt=""
								class="avatar-xs rounded-circle"
							/>
						</div>
						<div class="flex-grow-1 ms-3">
							<h5 class="fs-15">
								<Link href="/pages/profile/simple"
									>Tonya Noble</Link
								>
								<small class="text-muted">26 min ago</small>
							</h5>
							<p class="text-muted">
								Your <Link
									href={null}
									class="text-decoration-underline"
									>Online Order Support</Link
								> provides you with the most current status of your
								order. To help manage your order refer to the “Action
								Menu” to initiate return, contact Customer Support
								and more.
							</p>
							<div class="row g-2 mb-3">
								<div class="col-lg-1 col-sm-2 col-6">
									<img
										src={img4}
										alt=""
										class="img-fluid rounded"
									/>
								</div>
								<div class="col-lg-1 col-sm-2 col-6">
									<img
										src={img5}
										alt=""
										class="img-fluid rounded"
									/>
								</div>
							</div>
							<Link href={null} class="badge text-muted bg-light"
								><i class="mdi mdi-reply" /> Reply</Link
							>
							<div class="d-flex mt-4">
								<div class="flex-shrink-0">
									<img
										src={avatar6}
										alt=""
										class="avatar-xs rounded-circle"
									/>
								</div>
								<div class="flex-grow-1 ms-3">
									<h5 class="fs-13">
										<Link
											href="/pages/profile/settings/pages-profile-settings"
											>Nancy Martino</Link
										>
										<small class="text-muted"
											>8 sec ago</small
										>
									</h5>
									<p class="text-muted">
										Other shipping methods are available at
										checkout if you want your purchase
										delivered faster.
									</p>
									<Link
										href={null}
										class="badge text-muted bg-light"
										><i class="mdi mdi-reply" /> Reply</Link
									>
								</div>
							</div>
						</div>
					</div>
				</div>
				<form class="mt-4">
					<div class="row g-3">
						<div class="col-lg-12">
							<Label
								for="exampleFormControlTextarea1"
								class="form-label">Leave a Comments</Label
							>
							<textarea
								class="form-control bg-light border-light"
								id="exampleFormControlTextarea1"
								rows="3"
								placeholder="Enter comments"
							/>
						</div>
						<!--end col-->
						<div class="col-12 text-end">
							<button
								type="button"
								class="btn btn-ghost-secondary btn-icon waves-effect me-1"
								><i class="ri-attachment-line fs-16" /></button
							>
							<Link href={null} class="btn btn-success"
								>Post Comments</Link
							>
						</div>
					</div>
					<!--end row-->
				</form>
			</TabPane><!--end tab-pane-->
			<TabPane tabId={2} class={activeTab == 2 ? "active" : ""}>
				<div class="table-responsive table-card">
					<table class="table table-borderless align-middle mb-0">
						<thead class="table-light text-muted">
							<tr>
								<th scope="col">File Name</th>
								<th scope="col">Type</th>
								<th scope="col">Size</th>
								<th scope="col">Upload Date</th>
								<th scope="col">Action</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>
									<div class="d-flex align-items-center">
										<div class="avatar-sm">
											<div
												class="avatar-title bg-primary-subtle text-primary rounded fs-20"
											>
												<i class="ri-file-zip-fill" />
											</div>
										</div>
										<div class="ms-3 flex-grow-1">
											<h6 class="fs-15 mb-0">
												<Link href={null} class="link-secondary"
													>App pages.zip</Link
												>
											</h6>
										</div>
									</div>
								</td>
								<td>Zip File</td>
								<td>2.22 MB</td>
								<td>21 Dec, 2021</td>
								<td>
									<Dropdown>
										<DropdownToggle
											href={null}
											class="btn btn-light btn-icon"
											id="dropdownMenuLink1"
										>
											<i class="ri-equalizer-fill" />
										</DropdownToggle>
										<DropdownMenu
											class="dropdown-menu-end"
											style="position: absolute; inset: 0px 0px auto auto; margin: 0px; transform: translate(0px, 23px);"
										>
											<DropdownItem href={null}>
												<i
													class="ri-eye-fill me-2 align-middle text-muted"
												/>View</DropdownItem
											>

											<DropdownItem href={null}>
												<i
													class="ri-download-2-fill me-2 align-middle text-muted"
												/>Download</DropdownItem
											>
											<DropdownItem divider />
											<DropdownItem href={null}>
												<i
													class="ri-delete-bin-5-line me-2 align-middle text-muted"
												/>Delete</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</td>
							</tr>
							<tr>
								<td>
									<div class="d-flex align-items-center">
										<div class="avatar-sm">
											<div
												class="avatar-title bg-danger-subtle text-danger rounded fs-20"
											>
												<i class="ri-file-pdf-fill" />
											</div>
										</div>
										<div class="ms-3 flex-grow-1">
											<h6 class="fs-15 mb-0">
												<Link href={null} class="link-secondary"
													>Velzon admin.ppt</Link
												>
											</h6>
										</div>
									</div>
								</td>
								<td>PPT File</td>
								<td>2.24 MB</td>
								<td>25 Dec, 2021</td>
								<td>
									<Dropdown>
										<DropdownToggle
											href={null}
											class="btn btn-light btn-icon"
											id="dropdownMenuLink2"
										>
											<i class="ri-equalizer-fill" />
										</DropdownToggle>
										<DropdownMenu
											class="dropdown-menu-end"
											aria-labelledby="dropdownMenuLink2"
											data-popper-placement="bottom-end"
											style="position: absolute; inset: 0px 0px auto auto; margin: 0px; transform: translate(0px, 23px);"
										>
											<DropdownItem href={null}>
												<i
													class="ri-eye-fill me-2 align-middle text-muted"
												/>View</DropdownItem
											>

											<DropdownItem href={null}>
												<i
													class="ri-download-2-fill me-2 align-middle text-muted"
												/>Download</DropdownItem
											>

											<DropdownItem divider />

											<DropdownItem href={null}>
												<i
													class="ri-delete-bin-5-line me-2 align-middle text-muted"
												/>Delete</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</td>
							</tr>
							<tr>
								<td>
									<div class="d-flex align-items-center">
										<div class="avatar-sm">
											<div
												class="avatar-title bg-info-subtle text-info rounded fs-20"
											>
												<i class="ri-folder-line" />
											</div>
										</div>
										<div class="ms-3 flex-grow-1">
											<h6 class="fs-15 mb-0">
												<Link href={null} class="link-secondary"
													>Images.zip</Link
												>
											</h6>
										</div>
									</div>
								</td>
								<td>ZIP File</td>
								<td>1.02 MB</td>
								<td>28 Dec, 2021</td>
								<td>
									<Dropdown>
										<DropdownToggle
											href={null}
											class="btn btn-light btn-icon"
											id="dropdownMenuLink3"
										>
											<i class="ri-equalizer-fill" />
										</DropdownToggle>
										<DropdownMenu
											class="dropdown-menu-end"
											aria-labelledby="dropdownMenuLink3"
											data-popper-placement="bottom-end"
											style="position: absolute; inset: 0px 0px auto auto; margin: 0px; transform: translate(0px, 23px);"
										>
											<DropdownItem href={null}>
												<i
													class="ri-eye-fill me-2 align-middle"
												/>View</DropdownItem
											>

											<DropdownItem href={null}>
												<i
													class="ri-download-2-fill me-2 align-middle"
												/>Download</DropdownItem
											>

											<DropdownItem href={null}>
												<i
													class="ri-delete-bin-5-line me-2 align-middle"
												/>Delete</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</td>
							</tr>
							<tr>
								<td>
									<div class="d-flex align-items-center">
										<div class="avatar-sm">
											<div
												class="avatar-title bg-danger-subtle text-danger rounded fs-20"
											>
												<i class="ri-image-2-fill" />
											</div>
										</div>
										<div class="ms-3 flex-grow-1">
											<h6 class="fs-15 mb-0">
												<Link href={null} class="link-secondary"
													>Bg-pattern.png</Link
												>
											</h6>
										</div>
									</div>
								</td>
								<td>PNG File</td>
								<td>879 KB</td>
								<td>02 Nov 2021</td>
								<td>
									<Dropdown>
										<DropdownToggle
											href={null}
											class="btn btn-light btn-icon"
											id="dropdownMenuLink4"
										>
											<i class="ri-equalizer-fill" />
										</DropdownToggle>
										<DropdownMenu
											class="dropdown-menu-end"
											aria-labelledby="dropdownMenuLink4"
											data-popper-placement="bottom-end"
											style="position: absolute; inset: 0px 0px auto auto; margin: 0px; transform: translate(0px, 23px);"
										>
											<DropdownItem href={null}>
												<i
													class="ri-eye-fill me-2 align-middle"
												/>View</DropdownItem
											>

											<DropdownItem href={null}>
												<i
													class="ri-download-2-fill me-2 align-middle"
												/>Download</DropdownItem
											>

											<DropdownItem href={null}>
												<i
													class="ri-delete-bin-5-line me-2 align-middle"
												/>Delete</DropdownItem
											>
										</DropdownMenu>
									</Dropdown>
								</td>
							</tr>
						</tbody>
					</table>
					<!--end table-->
				</div>
			</TabPane><!--end tab-pane-->
			<TabPane tabId={3} class={activeTab == 3 ? "active" : ""}>
				<h6 class="card-title mb-4 pb-2">Time Entries</h6>
				<div class="table-responsive table-card">
					<table class="table align-middle mb-0">
						<thead class="table-light text-muted">
							<tr>
								<th scope="col">Member</th>
								<th scope="col">Date</th>
								<th scope="col">Duration</th>
								<th scope="col">Timer Idle</th>
								<th scope="col">Tasks Title</th>
							</tr>
						</thead>
						<tbody>
							<tr>
								<th scope="row">
									<div class="d-flex align-items-center">
										<img
											src={avatar8}
											alt=""
											class="rounded-circle avatar-xxs"
										/>
										<div class="flex-grow-1 ms-2">
											<Link
												href="/pages/profile/simple"
												class="fw-medium link-secondary"
												>Thomas Taylor</Link
											>
										</div>
									</div>
								</th>
								<td>02 Jan, 2022</td>
								<td>3 hrs 12 min</td>
								<td>05 min</td>
								<td>Apps Pages</td>
							</tr>
							<tr>
								<td>
									<div class="d-flex align-items-center">
										<img
											src={avatar10}
											alt=""
											class="rounded-circle avatar-xxs"
										/>
										<div class="flex-grow-1 ms-2">
											<Link
												href="/pages/profile/simple"
												class="fw-medium link-secondary"
												>Tonya Noble</Link
											>
										</div>
									</div>
								</td>
								<td>28 Dec, 2021</td>
								<td>1 hrs 35 min</td>
								<td>-</td>
								<td>Profile Page Design</td>
							</tr>
							<tr>
								<th scope="row">
									<div class="d-flex align-items-center">
										<img
											src={avatar10}
											alt=""
											class="rounded-circle avatar-xxs"
										/>
										<div class="flex-grow-1 ms-2">
											<Link
												href="/pages/profile/simple"
												class="fw-medium link-secondary"
												>Tonya Noble</Link
											>
										</div>
									</div>
								</th>
								<td>27 Dec, 2021</td>
								<td>4 hrs 26 min</td>
								<td>03 min</td>
								<td>Ecommerce Dashboard</td>
							</tr>
						</tbody>
					</table>
					<!--end table-->
				</div>
			</TabPane><!--edn tab-pane-->
		</TabContent><!--end tab-content-->
	</CardBody>
</Card>
