<script>
	import {
		Card,
		CardBody,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Dropdown,
		Button,
		Table,
	} from "sveltestrap";
	import Link from "svelte-link";
	import Select from "svelte-select";

	import avatar2 from "../../assets/images/users/avatar-2.jpg";
	import avatar8 from "../../assets/images/users/avatar-8.jpg";
	import avatar10 from "../../assets/images/users/avatar-10.jpg";

	const timeTraking = [
		{
			value: "Select Task board",
			label: "Select Task board",
		},
		{
			value: "Unassigned",
			label: "Unassigned",
		},
		{
			value: "To Do",
			label: "To Do",
		},
		{
			value: "Inprogress",
			label: "Inprogress",
		},
		{
			value: "In Reviews",
			label: "In Reviews",
		},
		{
			value: "Completed",
			label: "Completed",
		},
	];
</script>

<Card>
	<CardBody class="text-center">
		<h6 class="card-title mb-3 flex-grow-1 text-start">Time Tracking</h6>
		<div class="mb-2">
			<lord-icon
				src="//cdn.lordicon.com/kbtmbyzy.json"
				trigger="loop"
				colors="primary:#405189,secondary:#02a8b5"
				style="width:90px;height:90px"
			/>
		</div>
		<h3 class="mb-1">9 hrs 13 min</h3>
		<h5 class="fs-14 mb-4">Profile Page Structure</h5>
		<div class="hstack gap-2 justify-content-center">
			<Button color="danger" class="btn-sm"
				><i class="ri-stop-circle-line align-bottom me-1" /> Stop</Button
			>
			<Button color="success" class="btn-sm"
				><i class="ri-play-circle-line align-bottom me-1" /> Start</Button
			>
		</div>
	</CardBody>
</Card>
<Card class="mb-3">
	<CardBody>
		<div class="mb-4 select-single">
			<Select
				class="form-control"
				name="choices-single-default"
				items={timeTraking}
			/>
		</div>
		<div class="table-card">
			<Table class="mb-0">
				<tbody>
					<tr>
						<td class="fw-medium">Tasks No</td>
						<td>#VLZ456</td>
					</tr>
					<tr>
						<td class="fw-medium">Tasks Title</td>
						<td>Profile Page Structure</td>
					</tr>
					<tr>
						<td class="fw-medium">Project Name</td>
						<td>Velzon - Admin Dashboard</td>
					</tr>
					<tr>
						<td class="fw-medium">Priority</td>
						<td
							><span class="badge bg-danger-subtle text-danger"
								>High</span
							></td
						>
					</tr>
					<tr>
						<td class="fw-medium">Status</td>
						<td
							><span
								class="badge bg-secondary-subtle text-secondary"
								>Inprogress</span
							></td
						>
					</tr>
					<tr>
						<td class="fw-medium">Due Date</td>
						<td>05 Jan, 2022</td>
					</tr>
				</tbody>
			</Table>
		</div>
	</CardBody>
</Card>
<Card class="mb-3">
	<CardBody>
		<div class="d-flex mb-3">
			<h6 class="card-title mb-0 flex-grow-1">Assigned To</h6>
			<div class="flex-shrink-0">
				<Button color="soft-danger" class="material-shadow-none" size="sm"
					><i class="ri-share-line me-1 align-bottom" /> Assigned Member</Button
				>
			</div>
		</div>
		<ul class="list-unstyled vstack gap-3 mb-0">
			<li>
				<div class="d-flex align-items-center">
					<div class="flex-shrink-0">
						<img
							src={avatar10}
							alt=""
							class="avatar-xs rounded-circle material-shadow"
						/>
					</div>
					<div class="flex-grow-1 ms-2">
						<h6 class="mb-1">
							<Link href="/pages/profile/simple">Tonya Noble</Link
							>
						</h6>
						<p class="text-muted mb-0">Full Stack Developer</p>
					</div>
					<div class="flex-shrink-0">
						<Dropdown>
							<DropdownToggle
								class="btn btn-icon btn-sm fs-16 text-muted dropdown material-shadow-none"
								color=""
							>
								<i class="ri-more-fill" />
							</DropdownToggle>
							<DropdownMenu>
								<div>
									<DropdownItem
										><i
											class="ri-eye-fill text-muted me-2 align-bottom"
										/>View</DropdownItem
									>
								</div>
								<div>
									<DropdownItem
										><i
											class="ri-star-fill text-muted me-2 align-bottom"
										/>Favourite</DropdownItem
									>
								</div>
								<div>
									<DropdownItem
										><i
											class="ri-delete-bin-5-fill text-muted me-2 align-bottom"
										/>Delete</DropdownItem
									>
								</div>
							</DropdownMenu>
						</Dropdown>
					</div>
				</div>
			</li>
			<li>
				<div class="d-flex align-items-center">
					<div class="flex-shrink-0">
						<img
							src={avatar8}
							alt=""
							class="avatar-xs rounded-circle material-shadow"
						/>
					</div>
					<div class="flex-grow-1 ms-2">
						<h6 class="mb-1">
							<Link href="/pages/profile/simple"
								>Thomas Taylor</Link
							>
						</h6>
						<p class="text-muted mb-0">UI/UX Designer</p>
					</div>
					<div class="flex-shrink-0">
						<Dropdown>
							<DropdownToggle
								class="btn btn-icon btn-sm fs-16 text-muted dropdown material-shadow-none"
								color=""
							>
								<i class="ri-more-fill" />
							</DropdownToggle>
							<DropdownMenu>
								<div>
									<DropdownItem
										><i
											class="ri-eye-fill text-muted me-2 align-bottom"
										/>View</DropdownItem
									>
								</div>
								<div>
									<DropdownItem
										><i
											class="ri-star-fill text-muted me-2 align-bottom"
										/>Favourite</DropdownItem
									>
								</div>
								<div>
									<DropdownItem
										><i
											class="ri-delete-bin-5-fill text-muted me-2 align-bottom"
										/>Delete</DropdownItem
									>
								</div>
							</DropdownMenu>
						</Dropdown>
					</div>
				</div>
			</li>
			<li>
				<div class="d-flex align-items-center">
					<div class="flex-shrink-0">
						<img
							src={avatar2}
							alt=""
							class="avatar-xs rounded-circle material-shadow"
						/>
					</div>
					<div class="flex-grow-1 ms-2">
						<h6 class="mb-1">
							<Link href="/pages/profile/simple"
								>Nancy Martino</Link
							>
						</h6>
						<p class="text-muted mb-0">Web Designer</p>
					</div>
					<div class="flex-shrink-0">
						<Dropdown>
							<DropdownToggle
								class="btn btn-icon btn-sm fs-16 text-muted dropdown material-shadow-none"
								color=""
							>
								<i class="ri-more-fill" />
							</DropdownToggle>
							<DropdownMenu>
								<div>
									<DropdownItem
										><i
											class="ri-eye-fill text-muted me-2 align-bottom"
										/>View</DropdownItem
									>
								</div>
								<div>
									<DropdownItem
										><i
											class="ri-star-fill text-muted me-2 align-bottom"
										/>Favourite</DropdownItem
									>
								</div>
								<div>
									<DropdownItem
										><i
											class="ri-delete-bin-5-fill text-muted me-2 align-bottom"
										/>Delete</DropdownItem
									>
								</div>
							</DropdownMenu>
						</Dropdown>
					</div>
				</div>
			</li>
		</ul>
	</CardBody>
</Card>
<Card>
	<CardBody>
		<h5 class="card-title mb-3">Attachments</h5>
		<div class="vstack gap-2">
			<div class="border rounded border-dashed p-2">
				<div class="d-flex align-items-center">
					<div class="flex-shrink-0 me-3">
						<div class="avatar-sm">
							<div
								class="avatar-title bg-light text-secondary rounded fs-24"
							>
								<i class="ri-folder-zip-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 overflow-hidden">
						<h5 class="fs-13 mb-1">
							<Link
								href={null}
								class="text-body text-truncate d-block"
								>App pages.zip</Link
							>
						</h5>
						<div>2.2MB</div>
					</div>
					<div class="flex-shrink-0 ms-2">
						<div class="d-flex gap-1">
							<Button
								color=""
								class="btn btn-icon text-muted btn-sm fs-18 material-shadow-none"
								><i class="ri-download-2-line" /></Button
							>
							<Dropdown>
								<DropdownToggle
									class="btn btn-icon text-muted btn-sm fs-18 dropdown material-shadow-none"
									color=""
								>
									<i class="ri-more-fill" />
								</DropdownToggle>
								<DropdownMenu>
									<li>
										<DropdownItem
											><i
												class="ri-pencil-fill align-bottom me-2 text-muted"
											/> Rename</DropdownItem
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
						</div>
					</div>
				</div>
			</div>

			<div class="border rounded border-dashed p-2">
				<div class="d-flex align-items-center">
					<div class="flex-shrink-0 me-3">
						<div class="avatar-sm">
							<div
								class="avatar-title bg-light text-secondary rounded fs-24"
							>
								<i class="ri-file-ppt-2-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 overflow-hidden">
						<h5 class="fs-13 mb-1">
							<Link
								href={null}
								class="text-body text-truncate d-block"
								>Velzon admin.ppt</Link
							>
						</h5>
						<div>2.4MB</div>
					</div>
					<div class="flex-shrink-0 ms-2">
						<div class="d-flex gap-1">
							<Button
								color=""
								class="btn btn-icon text-muted btn-sm fs-18 material-shadow-none"
								><i class="ri-download-2-line" /></Button
							>
							<Dropdown>
								<DropdownToggle
									class="btn btn-icon text-muted btn-sm fs-18 dropdown material-shadow-none"
									color=""
								>
									<i class="ri-more-fill" />
								</DropdownToggle>
								<DropdownMenu>
									<li>
										<DropdownItem
											><i
												class="ri-pencil-fill align-bottom me-2 text-muted"
											/> Rename</DropdownItem
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
						</div>
					</div>
				</div>
			</div>

			<div class="border rounded border-dashed p-2">
				<div class="d-flex align-items-center">
					<div class="flex-shrink-0 me-3">
						<div class="avatar-sm">
							<div
								class="avatar-title bg-light text-secondary rounded fs-24"
							>
								<i class="ri-folder-zip-line" />
							</div>
						</div>
					</div>
					<div class="flex-grow-1 overflow-hidden">
						<h5 class="fs-13 mb-1">
							<Link
								href={null}
								class="text-body text-truncate d-block"
								>Images.zip</Link
							>
						</h5>
						<div>1.2MB</div>
					</div>
					<div class="flex-shrink-0 ms-2">
						<div class="d-flex gap-1">
							<Button
								color=""
								class="btn btn-icon text-muted btn-sm fs-18 material-shadow-none"
								><i class="ri-download-2-line" /></Button
							>
							<Dropdown>
								<DropdownToggle
									class="btn btn-icon text-muted btn-sm fs-18 dropdown material-shadow-none"
									color=""
								>
									<i class="ri-more-fill" />
								</DropdownToggle>
								<DropdownMenu>
									<li>
										<DropdownItem
											><i
												class="ri-pencil-fill align-bottom me-2 text-muted"
											/> Rename</DropdownItem
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
						</div>
					</div>
				</div>
			</div>
			<div class="mt-2 text-center">
				<Button color="success">View more</Button>
			</div>
		</div>
	</CardBody>
</Card>
