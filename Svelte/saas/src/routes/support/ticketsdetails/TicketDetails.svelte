<script>
	import { Card, CardBody, CardHeader, Col } from "sveltestrap";
	import Select from "svelte-select";
	import Link from "svelte-link";

	import avatar3 from "../../../assets/images/users/avatar-3.jpg";
	import avatar4 from "../../../assets/images/users/avatar-4.jpg";
	import avatar10 from "../../../assets/images/users/avatar-10.jpg";

	const allStatus = [
		{ label: "Stauts", value: "Stauts" },
		{ label: "New", value: "New" },
		{ label: "Open", value: "Open" },
		{ label: "Inprogress", value: "Inprogress" },
		{ label: "Closed", value: "Closed" },
	];
</script>

<Col xxl={3}>
	<Card>
		<CardHeader>
			<h5 class="card-title mb-0">Ticket Details</h5>
		</CardHeader>
		<CardBody>
			<div class="table-responsive table-card">
				<table class="table table-borderless align-middle mb-0">
					<tbody>
						<tr>
							<td class="fw-medium">Ticket</td>
							<td>#VLZ<span id="t-no">135</span> </td>
						</tr>
						<tr>
							<td class="fw-medium">Client</td>
							<td id="t-client">Themesbrand</td>
						</tr>
						<tr>
							<td class="fw-medium">Project</td>
							<td>Velzon - Admin Dashboard</td>
						</tr>
						<tr>
							<td class="fw-medium">Assigned To:</td>
							<td>
								<div class="avatar-group">
									<Link
										href={null}
										class="avatar-group-item"
										data-bs-original-title="Erica Kernan"
									>
										<img
											src={avatar4}
											alt=""
											class="rounded-circle avatar-xs"
										/>
									</Link>
									<Link href={null} class="avatar-group-item">
										<img
											src={avatar10}
											alt=""
											class="rounded-circle avatar-xs"
										/>
									</Link>
									<Link href={null} class="avatar-group-item">
										<img
											src={avatar3}
											alt=""
											class="rounded-circle avatar-xs"
										/>
									</Link>
									<Link href={null} class="avatar-group-item">
										<div class="avatar-xs">
											<div
												class="avatar-title fs-16 rounded-circle bg-light border-dashed border text-primary"
											>
												+
											</div>
										</div>
									</Link>
								</div>
							</td>
						</tr>
						<tr>
							<td class="fw-medium">Status:</td>
							<td class="select-single">
								<Select
									class="form-select"
									id="t-status"
									items={allStatus}
								/>
							</td>
						</tr>
						<tr>
							<td class="fw-medium">Priority</td>
							<td>
								<span class="badge bg-danger" id="t-priority"
									>High</span
								>
							</td>
						</tr>
						<tr>
							<td class="fw-medium">Create Date</td>
							<td id="c-date">20 Dec, 2021</td>
						</tr>
						<tr>
							<td class="fw-medium">Due Date</td>
							<td id="d-date">29 Dec, 2021</td>
						</tr>
						<tr>
							<td class="fw-medium">Last Activity</td>
							<td>14 min ago</td>
						</tr>
						<tr>
							<td class="fw-medium">Labels</td>
							<td class="hstack text-wrap gap-1">
								<span
									class="badge bg-primary-subtle text-primary"
									>Admin</span
								>
								<span
									class="badge bg-primary-subtle text-primary"
									>UI</span
								>
								<span
									class="badge bg-primary-subtle text-primary"
									>Dashboard</span
								>
								<span
									class="badge bg-primary-subtle text-primary"
									>Design</span
								>
							</td>
						</tr>
					</tbody>
				</table>
			</div>
		</CardBody>
		<!--end card-body-->
	</Card>
	<!--end card-->
	<Card>
		<CardHeader>
			<h6 class="card-title fw-semibold mb-0">Files Attachment</h6>
		</CardHeader>
		<CardBody>
			<div
				class="d-flex align-items-center border border-dashed p-2 rounded"
			>
				<div class="flex-shrink-0 avatar-sm">
					<div class="avatar-title bg-light rounded">
						<i class="ri-file-zip-line fs-20 text-primary" />
					</div>
				</div>
				<div class="flex-grow-1 ms-3">
					<h6 class="mb-1">
						<Link href={null} class="text-body">Velzon-admin.zip</Link>
					</h6>
					<small class="text-muted">3.2 MB</small>
				</div>
				<div class="hstack gap-3 fs-16">
					<Link href={null} class="text-muted"
						><i class="ri-download-2-line" /></Link
					>
					<Link href={null} class="text-muted"
						><i class="ri-delete-bin-line" /></Link
					>
				</div>
			</div>
			<div
				class="d-flex align-items-center border border-dashed p-2 rounded mt-2"
			>
				<div class="flex-shrink-0 avatar-sm">
					<div class="avatar-title bg-light rounded">
						<i class="ri-file-ppt-2-line fs-20 text-danger" />
					</div>
				</div>
				<div class="flex-grow-1 ms-3">
					<h6 class="mb-1">
						<Link href={null} class="text-body">Velzon-admin.ppt</Link>
					</h6>
					<small class="text-muted">4.5 MB</small>
				</div>
				<div class="hstack gap-3 fs-16">
					<Link href={null} class="text-muted"
						><i class="ri-download-2-line" /></Link
					>
					<Link href={null} class="text-muted"
						><i class="ri-delete-bin-line" /></Link
					>
				</div>
			</div>
		</CardBody>
	</Card>
</Col>
