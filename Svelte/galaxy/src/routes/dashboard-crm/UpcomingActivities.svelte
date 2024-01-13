<script>
    
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Row,
		Dropdown
	} from 'sveltestrap';
	import data from '../../common/data/dashboardcrm';

</script>

<Col xxl={5}>
	<Card>
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Upcoming Activities</h4>
			<div class="flex-shrink-0">
				<Dropdown class="card-header-dropdown" direction="start">
					<DropdownToggle class="text-reset dropdown-btn p-0" color="" tag="a" role="button">
						<span class="text-muted fs-18"><i class="mdi mdi-dots-vertical" /></span>
					</DropdownToggle>
					<DropdownMenu class="dropdown-menu dropdown-menu-end" end>
						<DropdownItem>Edit</DropdownItem>
						<DropdownItem>Remove</DropdownItem>
					</DropdownMenu>
				</Dropdown>
			</div>
		</CardHeader>
		<CardBody class="card-body pt-0">
			<ul class="list-group list-group-flush border-dashed">
				{#each data.activities as item}
					<li class="list-group-item ps-0">
						<Row class="align-items-center g-3">
							<div class="col-auto">
								<div class="avatar-sm p-1 py-2 h-auto bg-light rounded-3">
									<div class="text-center">
										<h5 class="mb-0">{item.date}</h5>
										<div class="text-muted">{item.weekDay}</div>
									</div>
								</div>
							</div>
							<div class="col">
								<h5 class="text-muted mt-0 mb-1 fs-13">{item.time}</h5>
								<a href="{null}" class="text-reset fs-14 mb-0">{item.caption}</a>
							</div>
							<div class="col-sm-auto">
								<div class="avatar-group">
									{#each item.subItem as subItem}
										<div class="avatar-group-item">
											<a href="{null}" class="d-inline-block">
												<img src={subItem.img} alt="" class="rounded-circle avatar-xxs" />
											</a>
										</div>
									{/each}
									<div class="avatar-group-item">
										<a href="{null}">
											<div class="avatar-xxs">
												<span class={'avatar-title rounded-circle ' + item.bgcolor + ' text-white'}>
													{item.imgNumber}
												</span>
											</div>
										</a>
									</div>
								</div>
							</div>
						</Row>
					</li>
				{/each}
			</ul>
			<div class="align-items-center mt-2 row g-3 text-center text-sm-start">
				<div class="col-sm">
					<div class="text-muted">
						Showing <span class="fw-semibold"> 4</span> of <span class="fw-semibold">125</span> Results
					</div>
				</div>
				<div class="col-sm-auto">
					<ul
						class="pagination pagination-separated pagination-sm justify-content-center justify-content-sm-start mb-0">
						<li class="page-item disabled">
							<a href="{null}" class="page-link">←</a>
						</li>
						<li class="page-item">
							<a href="{null}" class="page-link">1</a>
						</li>
						<li class="page-item active">
							<a href="{null}" class="page-link">2</a>
						</li>
						<li class="page-item">
							<a href="{null}" class="page-link">3</a>
						</li>
						<li class="page-item">
							<a href="{null}" class="page-link">→</a>
						</li>
					</ul>
				</div>
			</div>
		</CardBody>
	</Card>
</Col>
