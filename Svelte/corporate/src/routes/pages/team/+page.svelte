<svelte:head>
  <title>Team | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import {
		Button,
		Card,
		CardBody,
		Col,
		Container,
		Dropdown,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Form,
		Input,
		Label,
		Modal,
		ModalBody,
		Offcanvas,
		OffcanvasBody,
		Row,
		ModalHeader
	} from 'sveltestrap';
	import Link from 'svelte-link';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';

	let open = false;
	const toggle = () => {
		open = !open;
	};

	let openModal = false;
	const toggleOffCanvas = () => (openModal = !openModal);

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
	import avatar2 from '../../../assets/images/users/avatar-2.jpg';
	import avatar3 from '../../../assets/images/users/avatar-3.jpg';
	import avatar4 from '../../../assets/images/users/avatar-4.jpg';
	import avatar5 from '../../../assets/images/users/avatar-5.jpg';
	import avatar6 from '../../../assets/images/users/avatar-6.jpg';
	import avatar7 from '../../../assets/images/users/avatar-7.jpg';
	import avatar8 from '../../../assets/images/users/avatar-8.jpg';

	const team = [
		{
			id: 1,
			backgroundImg: img9,
			userImage: avatar2,
			name: 'Nancy Martino',
			jobPosition: 'Team Leader & HR',
			projectCount: 225,
			taskCount: 197
		},
		{
			id: 2,
			backgroundImg: img12,
			userImage: null,
			userShortName: 'HB',
			name: 'Henry Baird',
			jobPosition: 'Full Stack Developer',
			projectCount: 352,
			taskCount: 376,
			bgColor: 'light',
			textColor: 'primary'
		},
		{
			id: 3,
			backgroundImg: img11,
			userImage: avatar3,
			name: 'Frank Hook',
			jobPosition: 'Project Manager',
			projectCount: 162,
			taskCount: 192
		},
		{
			id: 4,
			backgroundImg: img1,
			userImage: avatar8,
			name: 'Jennifer Carter',
			jobPosition: 'UI/UX Designer',
			projectCount: 241,
			taskCount: 205
		},
		{
			id: 5,
			backgroundImg: img10,
			userImage: null,
			userShortName: 'ME',
			name: 'Megan Elmore',
			jobPosition: 'Team Leader & Web Developer',
			projectCount: 201,
			taskCount: 263,
			bgColor: 'light',
			textColor: 'primary'
		},
		{
			id: 6,
			backgroundImg: img2,
			userImage: avatar4,
			name: 'Alexis Clarke',
			jobPosition: 'Backend Developer',
			projectCount: 132,
			taskCount: 147
		},
		{
			id: 7,
			backgroundImg: img4,
			userImage: null,
			userShortName: 'NC',
			name: 'Nathan Cole',
			jobPosition: 'Front-End Developer',
			projectCount: 352,
			taskCount: 376,
			bgColor: 'light',
			textColor: 'primary'
		},
		{
			id: 8,
			backgroundImg: img7,
			userImage: avatar6,
			name: 'Joseph Parker',
			jobPosition: 'Full Stack Developer',
			projectCount: 64,
			taskCount: 93
		},
		{
			id: 9,
			backgroundImg: img3,
			userImage: avatar5,
			name: 'Erica Kernan',
			jobPosition: 'Web Designer',
			projectCount: 345,
			taskCount: 298
		},
		{
			id: 10,
			backgroundImg: img5,
			userImage: null,
			userShortName: 'DP',
			name: 'Donald Palmer',
			jobPosition: 'Wed Developer',
			projectCount: 95,
			taskCount: 135,
			bgColor: 'light',
			textColor: 'primary'
		},
		{
			id: 11,
			backgroundImg: img8,
			userImage: avatar7,
			name: 'Jack Gough',
			jobPosition: 'React Js Developer',
			projectCount: 87,
			taskCount: 121
		},
		{
			id: 12,
			backgroundImg: img6,
			userImage: null,
			userShortName: 'MW',
			name: 'Marie Ward',
			jobPosition: 'Backend Developer',
			projectCount: 145,
			taskCount: 210,
			bgColor: 'light',
			textColor: 'primary'
		}
	];
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Team" pageTitle="Pages" />
		<Card>
			<CardBody>
				<Row class="g-2">
					<Col sm={4}>
						<div class="search-box">
							<Input
								type="text"
								class="form-control"
								placeholder="Search for name, tasks, projects or something..."
							/>
							<i class="ri-search-line search-icon" />
						</div>
					</Col>
					<Col class="col-sm-auto ms-auto">
						<div class="list-grid-nav hstack gap-1">
							<Button
								color="info"
								id="grid-view-button"
								class="btn btn-soft-info nav-link btn-icon fs-14 active filter-button"
								><i class="ri-grid-fill" /></Button>
							<Button
								color="info"
								id="list-view-button"
								class="btn btn-soft-info nav-link  btn-icon fs-14 filter-button"
								><i class="ri-list-unordered" /></Button>
							<Dropdown>
								<DropdownToggle type="button" class="btn btn-soft-info btn-icon fs-14">
									<i class="ri-more-2-fill" />
								</DropdownToggle>
								<DropdownMenu>
									<li><Link class="dropdown-item" href={null}>All</Link></li>
									<li><Link class="dropdown-item" href={null}>Last Week</Link></li>
									<li><Link class="dropdown-item" href={null}>Last Month</Link></li>
									<li><Link class="dropdown-item" href={null}>Last Year</Link></li>
								</DropdownMenu>
							</Dropdown>
							<Button color="secondary" on:click={openModal}>
								<i class="ri-add-fill me-1 align-bottom" /> Add Members</Button>
						</div>
					</Col>
				</Row>
			</CardBody>
		</Card>

		<Row>
			<Col lg={12}>
				<div>
					<Row class="team-list grid-view-filter">
						{#each team as item}
							<Col>
								<Card class="team-box">
									<div class="team-cover">
										<img src={item.backgroundImg} alt="" class="img-fluid" />
									</div>
									<CardBody class="p-4">
										<Row class="align-items-center team-row">
											<Col class="team-settings">
												<Row>
													<Col>
															<div class="flex-shrink-0 me-2">
																<button type="button" class="btn btn-light btn-icon rounded-circle btn-sm favourite-btn">
																	<i class="ri-star-fill fs-14"></i>
																</button>
															</div>
													</Col>
													<Dropdown direction="start" class="col text-end">
														<DropdownToggle
															tag="a"
															color=""
															class="p-0 text-white"
															id="dropdownMenuLink2"
															role="button"
														>
															<i class="ri-more-fill fs-17" />
														</DropdownToggle>
														<DropdownMenu>
															<DropdownItem
																><i class="ri-eye-line me-2 align-middle" />View</DropdownItem
															>
															<DropdownItem
																><i class="ri-star-line me-2 align-middle" />Favorites</DropdownItem
															>
															<DropdownItem
																><i
																	class="ri-delete-bin-5-line me-2 align-middle"
																/>Delete</DropdownItem
															>
														</DropdownMenu>
													</Dropdown>
												</Row>
											</Col>
											<Col lg={4} class="col">
												<div class="team-profile-img">
													<div class="avatar-lg img-thumbnail rounded-circle flex-shrink-0">
														{#if item.userImage != null}
															<img
																src={item.userImage}
																alt=""
																class="img-fluid d-block rounded-circle"
															/>
														{:else}
															<div 						class={'avatar-title rounded-circle bg-' +
																	item.bgColor +
																	' text-' +
																	item.textColor}
															>
																{item.userShortName}
															</div>
														{/if}
													</div>
													<div class="team-content">
														<Link href={null} on:click={toggleOffCanvas}
															><h5 class="fs-16 mb-1">{item.name}</h5></Link
														>
														<p class="text-muted mb-0">{item.jobPosition}</p>
													</div>
												</div>
											</Col>
											<Col lg={4} class="col">
												<Row class="text-muted text-center">
													<Col xs={6} class="border-end border-end-dashed">
														<h5 class="mb-1">{item.projectCount}</h5>
														<p class="text-muted mb-0">Projects</p>
													</Col>
													<Col xs={6}>
														<h5 class="mb-1">{item.taskCount}</h5>
														<p class="text-muted mb-0">Tasks</p>
													</Col>
												</Row>
											</Col>
											<Col lg={2} class="col">
												<div class="text-end">
													<Link href="/pages/profile/simple" class="btn btn-light view-btn"
														>View Profile</Link
													>
												</div>
											</Col>
										</Row>
									</CardBody>
								</Card>
							</Col>
						{/each}

						<Col lg={12}>
							<div class="text-center mb-3">
								<Link href={null} class="text-success"
									><i class="mdi mdi-loading mdi-spin fs-20 align-middle me-2" /> Load More
								</Link>
							</div>
						</Col>
					</Row>

					<Modal isOpen={open} {toggle} centered>
						<div class="modal-content">
							<ModalHeader {toggle}>
								<h5 class="modal-title" id="myModalLabel">Add New Members</h5>
							</ModalHeader>
							<ModalBody>
								<Form>
									<Row>
										<Col lg={12}>
											<div class="mb-3">
												<Label for="teammembersName" class="form-label">Name</Label>
												<Input
													type="text"
													class="form-control"
													id="teammembersName"
													placeholder="Enter name"
												/>
											</div>
										</Col>
										<Col lg={12}>
											<div class="mb-3">
												<Label for="designation" class="form-label">Designation</Label>
												<Input
													type="text"
													class="form-control"
													id="designation"
													placeholder="Enter designation"
												/>
											</div>
										</Col>
										<Col lg={6}>
											<div class="mb-3">
												<Label for="totalProjects" class="form-label">Projects</Label>
												<Input
													type="number"
													class="form-control"
													id="totalProjects"
													placeholder="Total projects"
												/>
											</div>
										</Col>
										<Col lg={6}>
											<div class="mb-3">
												<Label for="totalTasks" class="form-label">Tasks</Label>
												<Input
													type="number"
													class="form-control"
													id="totalTasks"
													placeholder="Total tasks"
												/>
											</div>
										</Col>
										<Col lg={12}>
											<div class="mb-4">
												<Label for="formFile" class="form-label">Profile Images</Label>
												<Input class="form-control" type="file" id="formFile" />
											</div>
										</Col>
										<Col lg={12}>
											<div class="hstack gap-2 justify-content-end">
												<button type="button" class="btn btn-light" data-bs-dismiss="modal"
													>Close</button
												>
												<button type="submit" class="btn btn-success" on:click={toggle}
													>Add Member</button
												>
											</div>
										</Col>
									</Row>
								</Form>
							</ModalBody>
						</div>
					</Modal>

					<Offcanvas
						isOpen={openModal}
						placement="end"
						toggle={toggleOffCanvas}
						class="offcanvas-end border-0">
						<OffcanvasBody class="profile-offcanvas p-0">
							<div class="team-cover">
								<img src={img9} alt="" class="img-fluid" />
							</div>
							<div class="p-3">
								<div class="team-settings">
									<Row>
										<Col>
											<div class="flex-shrink-0 me-2">  
												<button type="button" class="btn btn-light btn-icon rounded-circle btn-sm favourite-btn ">  
													<i class="ri-star-fill fs-14"></i>   
												</button>              
											</div>
										</Col>
										<Dropdown direction="start" class="col text-end">
											<DropdownToggle
												tag="a"
												color=""
												class="p-0 text-white"
												id="dropdownMenuLink14"
											>
												<i class="ri-more-fill fs-17" />
											</DropdownToggle>
											<DropdownMenu>
												<DropdownItem><i class="ri-eye-line me-2 align-middle" />View</DropdownItem>
												<DropdownItem
													><i class="ri-star-line me-2 align-middle" />Favorites</DropdownItem
												>
												<DropdownItem
													><i class="ri-delete-bin-5-line me-2 align-middle" />Delete</DropdownItem
												>
											</DropdownMenu>
										</Dropdown>
									</Row>
								</div>
							</div>
							<div class="p-3 text-center">
								<img
									src={avatar2}
									alt=""
									class="avatar-lg img-thumbnail rounded-circle mx-auto"
								/>
								<div class="mt-3">
									<h5 class="fs-15"><Link href={null} class="link-primary">Nancy Martino</Link></h5>
									<p class="text-muted">Team Leader & HR</p>
								</div>
								<div class="hstack gap-2 justify-content-center mt-4">
									<div class="avatar-xs">
										<Link
											href={null}
											class="avatar-title bg-soft-secondary text-secondary rounded fs-16"
										>
											<i class="ri-facebook-fill" />
										</Link>
									</div>
									<div class="avatar-xs">
										<Link href={null} class="avatar-title bg-soft-success text-success rounded fs-16">
											<i class="ri-slack-fill" />
										</Link>
									</div>
									<div class="avatar-xs">
										<Link href={null} class="avatar-title bg-soft-info text-info rounded fs-16">
											<i class="ri-linkedin-fill" />
										</Link>
									</div>
									<div class="avatar-xs">
										<Link href={null} class="avatar-title bg-soft-danger text-danger rounded fs-16">
											<i class="ri-dribbble-fill" />
										</Link>
									</div>
								</div>
							</div>
							<Row class="g-0 text-center">
								<Col xs={6}>
									<div class="p-3 border border-dashed border-start-0">
										<h5 class="mb-1">124</h5>
										<p class="text-muted mb-0">Projects</p>
									</div>
								</Col>
								<Col xs={6}>
									<div class="p-3 border border-dashed border-start-0">
										<h5 class="mb-1">81</h5>
										<p class="text-muted mb-0">Tasks</p>
									</div>
								</Col>
							</Row>
							<div class="p-3">
								<h5 class="fs-15 mb-3">Personal Details</h5>
								<div class="mb-3">
									<p class="text-muted text-uppercase fw-semibold fs-12 mb-2">Number</p>
									<h6>+(256) 2451 8974</h6>
								</div>
								<div class="mb-3">
									<p class="text-muted text-uppercase fw-semibold fs-12 mb-2">Email</p>
									<h6>nancymartino@email.com</h6>
								</div>
								<div>
									<p class="text-muted text-uppercase fw-semibold fs-12 mb-2">Location</p>
									<h6 class="mb-0">Carson City - USA</h6>
								</div>
							</div>
							<div class="p-3 border-top">
								<h5 class="fs-15 mb-4">File Manager</h5>
								<div class="d-flex mb-3">
									<div class="flex-shrink-0 avatar-xs">
										<div class="avatar-title bg-soft-danger text-danger rounded fs-16">
											<i class="ri-image-2-line" />
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1"><Link href={null}>Images</Link></h6>
										<p class="text-muted mb-0">4469 Files</p>
									</div>
									<div class="text-muted">12 GB</div>
								</div>
								<div class="d-flex mb-3">
									<div class="flex-shrink-0 avatar-xs">
										<div class="avatar-title bg-soft-secondary text-secondary rounded fs-16">
											<i class="ri-file-zip-line" />
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1"><Link href={null}>Documents</Link></h6>
										<p class="text-muted mb-0">46 Files</p>
									</div>
									<div class="text-muted">3.46 GB</div>
								</div>
								<div class="d-flex mb-3">
									<div class="flex-shrink-0 avatar-xs">
										<div class="avatar-title bg-soft-success text-success rounded fs-16">
											<i class="ri-live-line" />
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1"><Link href={null}>Media</Link></h6>
										<p class="text-muted mb-0">124 Files</p>
									</div>
									<div class="text-muted">4.3 GB</div>
								</div>
								<div class="d-flex">
									<div class="flex-shrink-0 avatar-xs">
										<div class="avatar-title bg-soft-primary text-primary rounded fs-16">
											<i class="ri-error-warning-line" />
										</div>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="mb-1"><Link href={null}>Others</Link></h6>
										<p class="text-muted mb-0">18 Files</p>
									</div>
									<div class="text-muted">846 MB</div>
								</div>
							</div>
						</OffcanvasBody>
						<div class="offcanvas-foorter border p-3 hstack gap-3 text-center position-relative">
							<button class="btn btn-light w-100"
								><i class="ri-question-answer-fill align-bottom ms-1" /> Send Message</button>
							<Link href="/pages/profile/simple" class="btn btn-primary w-100"
								><i class="ri-user-3-fill align-bottom ms-1" /> View Profile</Link>
						</div>
					</Offcanvas>
				</div>
			</Col>
		</Row>

		<!-- <svg class="bookmark-hide">
			<symbol viewBox="0 0 24 24" stroke="currentColor" fill="var(--color-svg)" id="icon-star"
				><path
					strokeWidth=".4"
					d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
				/></symbol
			>
		</svg> -->
	</Container>
</div>
