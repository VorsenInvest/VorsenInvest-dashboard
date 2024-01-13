<svelte:head>
  <title>Search Results | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Dropdown,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Input,
		Nav,
		NavItem,
		NavLink,
		Offcanvas,
		OffcanvasBody,
		Pagination,
		PaginationItem,
		PaginationLink,
		Row,
		TabContent,
		TabPane
	} from 'sveltestrap';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import Link from 'svelte-link';
	let isOpen = false;
	let activeTab = 1;
	import { Lightbox } from 'svelte-lightbox';

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
	
	import { Swiper, SwiperSlide } from 'swiper/svelte';

	// Import Swiper styles
	import 'swiper/css';
	import 'swiper/css/pagination';
	const toggleOffCanvas = () => (isOpen = !isOpen);
	const swiper = [
		{
			id: 1,
			img: img12,
			title: 'Bootstrap'
		},
		{
			id: 2,
			img: img11,
			title: 'Website'
		},
		{
			id: 3,
			img: img10,
			title: 'Responsive'
		},
		{
			id: 4,
			img: img9,
			title: 'Design'
		},
		{
			id: 5,
			img: img8,
			title: 'eCommerce'
		},
		{
			id: 6,
			img: img7,
			title: 'Templates'
		},
		{
			id: 7,
			img: img6,
			title: 'Admin Panel'
		},
		{
			id: 8,
			img: img5,
			title: 'Simple'
		},
		{
			id: 9,
			img: img3,
			title: 'Dark'
		}
	];

	const gallery = [
		{
			id: 1,
			img: img1,
			title: 'Glasses and laptop from above',
			auther: 'Ron Mackie',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 2,
			img: img2,
			title: 'Working at a coffee shop',
			auther: 'Nancy Martino',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 3,
			img: img3,
			title: 'Photo was taken in Beach',
			auther: 'Elwood Arter',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 4,
			img: img4,
			title: 'Drawing a sketch',
			auther: 'Jason McQuaid',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 5,
			img: img5,
			title: 'Working from home little spot',
			auther: 'Henry Baird',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 6,
			img: img6,
			title: 'Glasses and laptop from above',
			auther: 'Erica Kernan',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 7,
			img: img7,
			title: 'Sunrise above a beach',
			auther: 'James Ballard',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 8,
			img: img8,
			title: 'Project discussion with team',
			auther: 'Ruby Griffin',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 9,
			img: img9,
			title: 'Dramatic clouds at the Golden Gate Bridge',
			auther: 'Ron Mackie',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 10,
			img: img10,
			title: 'Fun day at the Hill Station',
			auther: 'Henry Baird',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 11,
			img: img11,
			title: 'Cycling in the countryside',
			auther: 'Nancy Martino',
			likes: '2.2K',
			comments: '1.3K'
		},
		{
			id: 12,
			img: img12,
			title: 'A mix of friends and strangers heading off to find an adventure.',
			auther: 'Erica Kernan',
			likes: '2.2K',
			comments: '1.3K'
		}
	];

	const news = [
		{
			id: 1,
			img: img1,
			badgeClass: 'success',
			badgeText: 'Business',
			title: 'A mix of friends and strangers heading off to find an adventure',
			auther: 'James Ballard',
			date: '23 Nov, 2021'
		},
		{
			id: 2,
			img: img2,
			badgeClass: 'warning',
			badgeText: 'Development',
			title: 'How to get creative in your work ?',
			auther: 'Ruby Griffin',
			date: '23 Nov, 2021'
		},
		{
			id: 3,
			img: img3,
			badgeClass: 'info',
			badgeText: 'Fashion',
			title: 'How to become a best sale marketer in a year!',
			auther: 'Elwood Arter',
			date: '23 Nov, 2021'
		},
		{
			id: 4,
			img: img4,
			badgeClass: 'primary',
			badgeText: 'Product',
			title: 'Manage white space in responsive layouts ?',
			auther: 'Nancy Martino',
			date: '23 Nov, 2021'
		},
		{
			id: 5,
			img: img5,
			badgeClass: 'success',
			badgeText: 'Business',
			title: 'Stack designer Olivia Murphy offers freelancing advice',
			auther: 'Erica Kernan',
			date: '11 Nov, 2021'
		},
		{
			id: 6,
			img: img6,
			badgeClass: 'danger',
			badgeText: 'Design',
			title: 'A day in the of a professional fashion designer',
			auther: 'Jason McQuaid',
			date: '14 Nov, 2021'
		},
		{
			id: 7,
			img: img7,
			badgeClass: 'danger',
			badgeText: 'Design',
			title: 'Design your apps in your own way',
			auther: 'Henry Baird',
			date: '19 Nov, 2021'
		},
		{
			id: 8,
			img: img8,
			badgeClass: 'warning',
			badgeText: 'Development',
			title: 'How apps is changing the IT world',
			auther: 'Elwood Arter',
			date: '10 Aug, 2021'
		}
	];

	const video = [
		{
			id: 1,
			title: 'Admin dashboard templates - Material Design for Velzon',
			siteLink: 'https://themesbrand.com/velzon/index.html',
			videoLink: '//www.youtube.com/embed/GfSZtaoc5bw',
			description:
				'Velzon admin is super flexible, powerful, clean, modern & responsive admin template based on bootstrap 5 stable with unlimited possibilities. You can simply change to any layout or mode by changing a couple of lines of code. You can start small and large projects or update design in your existing project using Velzon it is very quick and easy as it is beautiful, adroit, and delivers the ultimate user experience.',
			likes: 335,
			comments: 102,
			auther: 'Themesbrand'
		},
		{
			id: 2,
			title: 'Create Responsive Admin Dashboard using Html CSS',
			siteLink: 'https://themesbrand.com/velzon/index.html',
			videoLink: '//www.youtube.com/embed/Z-fV2lGKnnU',
			description:
				'Velzon admin is super flexible, powerful, clean, modern & responsive admin template based on bootstrap 5 stable with unlimited possibilities. You can simply change to any layout or mode by changing a couple of lines of code. You can start small and large projects or update design in your existing project using Velzon it is very quick and easy as it is beautiful, adroit, and delivers the ultimate user experience.',
			likes: 485,
			comments: 167,
			auther: 'Themesbrand'
		},
		{
			id: 3,
			title: 'Velzon - The Most Popular Bootstrap 5 HTML, Angular & React Js Admin',
			siteLink: 'https://themesbrand.com/velzon/index.html',
			videoLink: '//www.youtube.com/embed/1y_kfWUCFDQ',
			description:
				'Velzon admin is super flexible, powerful, clean, modern & responsive admin template based on bootstrap 5 stable with unlimited possibilities. You can simply change to any layout or mode by changing a couple of lines of code. You can start small and large projects or update design in your existing project using Velzon it is very quick and easy as it is beautiful, adroit, and delivers the ultimate user experience.',
			likes: 122,
			comments: 51,
			auther: 'Themesbrand'
		}
	];
</script>

<div class="page-content">
	<div class="container-fluid">
		<BreadCrumb title="Search Results" pageTitle="Pages" />

		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader class="border-0">
						<Row class="justify-content-center mb-4">
							<Col lg={6}>
								<Row class="g-2">
									<Col>
										<div class="position-relative mb-3">
											<Input
												type="text"
												class="form-control form-control-lg bg-light border-light"
												placeholder="Search here.."
												defaultValue="Admin Dashboard"
											/>
											<Link
												href={null}
												class="btn btn-link link-success btn-lg position-absolute end-0 top-0"
												onClick={toggleOffCanvas}><i class="ri-mic-fill" /></Link
											>
										</div>
									</Col>
									<div class="col-auto">
										<button type="submit" class="btn btn-primary btn-lg waves-effect waves-light"
											><i class="mdi mdi-magnify me-1" /> Search</button
										>
									</div>
								</Row>
							</Col>
							<Col lg={12}>
								<h5 class="fs-16 fw-semibold text-center mb-0">
									Showing results for "<span class="text-primary fw-medium fst-italic"
										>Admin Dashboard</span
									> "
								</h5>
							</Col>
						</Row>

						<Offcanvas {isOpen} placement="top" {toggleOffCanvas} tabIndex="-1">
							<OffcanvasBody>
								<button
									type="button"
									class="btn-close text-reset float-end"
									data-bs-dismiss="offcanvas"
									aria-label="Close"
								/>
								<div class="d-flex flex-column h-100 justify-content-center align-items-center">
									<div class="search-voice">
										<i class="ri-mic-fill align-middle" />
										<span class="voice-wave" />
										<span class="voice-wave" />
										<span class="voice-wave" />
									</div>
									<h4>Talk to me, what can I do for you?</h4>
								</div>
							</OffcanvasBody>
						</Offcanvas>
					</CardHeader>
					<div>
						<Nav class="nav-tabs nav-tabs-custom" role="tablist">
							<NavItem>
								<NavLink href={null} on:click={() => (activeTab = 1)} active={activeTab == 1}>
									<i class="ri-search-2-line text-muted align-bottom me-1" /> All Results
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink href={null} on:click={() => (activeTab = 2)} active={activeTab == 2}>
									<i class="ri-image-fill text-muted align-bottom me-1" /> Images
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink href={null} on:click={() => (activeTab = 3)} active={activeTab == 3}>
									<i class="ri-list-unordered text-muted align-bottom me-1" /> News
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink href={null} on:click={() => (activeTab = 4)} active={activeTab == 4}>
									<i class="ri-video-line text-muted align-bottom me-1" /> Videos
								</NavLink>
							</NavItem>
							<li class="nav-item ms-auto">
								<Dropdown>
									<DropdownToggle class="nav-link fw-medium text-reset mb-n1" role="button">
										<i class="ri-settings-4-line align-middle me-1" /> Settings
									</DropdownToggle>
									<DropdownMenu>
										<DropdownItem>Search Settings</DropdownItem>
										<DropdownItem>Advanced Search</DropdownItem>
										<DropdownItem>Search History</DropdownItem>
										<DropdownItem>Search Help</DropdownItem>
										<DropdownItem divider />
										<DropdownItem>Dark Mode:Off</DropdownItem>
									</DropdownMenu>
								</Dropdown>
							</li>
						</Nav>
					</div>
					<CardBody class="p-4">
						<TabContent {activeTab} class="text-muted">
							<TabPane tabId={1} class={activeTab == 1 ? 'active' : ''}>
								<div class="pb-3">
									<h5 class="mb-1">
										<Link href={null}>Velzon - Responsive Bootstrap 5 Admin Dashboard</Link>
									</h5>
									<p class="text-success mb-2">https://themesbrand.com/velzon/index.html</p>
									<p class="text-muted mb-2">
										Velzon admin is super flexible, powerful, clean, modern & responsive admin
										template based on <span class="fw-semibold">bootstrap 5</span> stable with unlimited
										possibilities. You can simply change to any layout or mode by changing a couple of
										lines of code. You can start small and large projects or update design in your existing
										project using Velzon it is very quick and easy as it is beautiful, adroit, and delivers
										the ultimate user experience.
									</p>
									<ul class="list-inline d-flex align-items-center g-3 text-muted fs-14 mb-0">
										<li class="list-inline-item me-3">
											<i class="ri-thumb-up-line align-middle me-1" />10
										</li>
										<li class="list-inline-item me-3">
											<i class="ri-question-answer-line align-middle me-1" />8
										</li>
										<li class="list-inline-item">
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0">
													<i class="ri-user-line" />
												</div>
												<div class="flex-grow-1 fs-13 ms-1">
													<span class="fw-medium">Themesbrand</span>
												</div>
											</div>
										</li>
									</ul>
								</div>

								<div class="border border-dashed" />

								<div class="py-3">
									<h5 class="fs-13 mb-3 text-muted fst-italic">Showing results Images</h5>
									<Row>
										<Col xl={4} lg={10}>
											<Row class="g-2">
												<Col md={3} sm={6}>
													<div>
														<Lightbox class="image-popup d-block">
															<img
																src={img1}
																alt=""
																class="img-fluid d-block rounded"
															/>
														</Lightbox>
													</div>
												</Col>
												<Col md={3} sm={6}>
													<div>
														<Lightbox class="image-popup d-block">
															<img
																src={img3}
																alt=""
																class="img-fluid d-block rounded"
															/>
														</Lightbox>
													</div>
												</Col>
												<Col md={3} sm={6}>
													<div>
														<Lightbox class="image-popup d-block">
															<img
																src={img4}
																alt=""
																class="img-fluid d-block rounded"
															/>
														</Lightbox>
													</div>
												</Col>
												<Col md={3} sm={6}>
													<div class="search-more-results rounded">
														<Lightbox class="d-block">
															<img
																src={img5}
																alt=""
																class="img-fluid d-block rounded"
															/>
															<div class="bg-overlay" />
															<div class="nav-icon">
																<i class="ri-image-fill align-middle me-1" /> 99+
															</div>
														</Lightbox>
													</div>
												</Col>
											</Row>
										</Col>
									</Row>
								</div>

								<div class="border border-dashed" />

								<div class="py-3">
									<h5 class="mb-1">
										<Link href={null}>Skote - Admin & Dashboard Template by Themesbrand</Link>
									</h5>
									<p class="text-success mb-2">https://themesbrand.com/skote/</p>
									<p class="text-muted mb-2">
										Skote is an admin dashboard template that is a beautifully crafted, clean &
										minimal designed admin template with Dark, Light Layouts with RTL options. You
										can build any type of web application like Saas based interface, eCommerce,
										Crypto, CRM, CMS, Project management apps, Admin Panels, etc.
									</p>
									<ul class="list-inline d-flex align-items-center g-3 text-muted fs-14 mb-0">
										<li class="list-inline-item me-3">
											<i class="ri-thumb-up-line align-middle me-1" />485
										</li>
										<li class="list-inline-item me-3">
											<i class="ri-question-answer-line align-middle me-1" />167
										</li>
										<li class="list-inline-item">
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0">
													<i class="ri-user-line" />
												</div>
												<div class="flex-grow-1 fs-13 ms-1">
													<span class="fw-medium">Themesbrand</span>
												</div>
											</div>
										</li>
									</ul>
								</div>

								<div class="border border-dashed" />

								<div class="py-3">
									<h5 class="mb-1">
										<Link href={null}>Minia - React Js Admin & Dashboard Template</Link>
									</h5>
									<p class="text-success mb-2">https://themesbrand.com/minia/react/</p>
									<p class="text-muted mb-2">
										Minia react is a simple and beautiful admin template built with Bootstrap
										^5.1.3. It has <span class="fw-semibold">5+ different layouts and 3 modes</span>
										( Dark, Light & RTL ) which are managed by SCSS only. You can simply change to any
										layouts or mode by changing a couple of lines code.
									</p>
									<ul class="list-inline d-flex align-items-center g-3 text-muted fs-14 mb-0">
										<li class="list-inline-item me-3">
											<i class="ri-thumb-up-line align-middle me-1" />69
										</li>
										<li class="list-inline-item me-3">
											<i class="ri-question-answer-line align-middle me-1" />43
										</li>
										<li class="list-inline-item">
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0">
													<i class="ri-user-line" />
												</div>
												<div class="flex-grow-1 fs-13 ms-1">
													<span class="fw-medium">Themesbrand</span>
												</div>
											</div>
										</li>
									</ul>
								</div>

								<div class="border border-dashed" />

								<div class="py-3">
									<h5 class="mb-1">
										<Link href={null}>Doson - Angular Admin & Dashboard Template by Themesbrand</Link>
									</h5>
									<p class="text-success mb-2">https://themesbrand.com/dason/angular/</p>
									<p class="text-muted mb-2">
										Dason is a simple and beautiful admin template built with Bootstrap ^5.1.3. It
										has 5+ different layouts and 3 modes ( Dark, Light & RTL ) which are managed by
										SCSS only. You can simply change to any layouts or mode by changing a couple of
										lines code.
									</p>
									<ul class="list-inline d-flex align-items-center g-3 text-muted fs-14 mb-0">
										<li class="list-inline-item me-3">
											<i class="ri-thumb-up-line align-middle me-1" />102
										</li>
										<li class="list-inline-item me-3">
											<i class="ri-question-answer-line align-middle me-1" />36
										</li>
										<li class="list-inline-item">
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0">
													<i class="ri-user-line" />
												</div>
												<div class="flex-grow-1 fs-13 ms-1">
													<span class="fw-medium">Themesbrand</span>
												</div>
											</div>
										</li>
									</ul>
								</div>
								<Pagination listClassName="justify-content-center" class="pagination-separated mb-0 ">
									<PaginationItem disabled>
										<PaginationLink href={null}><i class="mdi mdi-chevron-left" /></PaginationLink>
									</PaginationItem>
									<PaginationItem active><PaginationLink href={null}>1</PaginationLink></PaginationItem>
									<PaginationItem><PaginationLink href={null}>2</PaginationLink></PaginationItem>
									<PaginationItem><PaginationLink href={null}>3</PaginationLink></PaginationItem>
									<PaginationItem><PaginationLink href={null}>4</PaginationLink></PaginationItem>
									<PaginationItem><PaginationLink href={null}>5</PaginationLink></PaginationItem>
									<PaginationItem>
										<PaginationLink href={null}><i class="mdi mdi-chevron-right" /></PaginationLink>
									</PaginationItem>
								</Pagination>
							</TabPane>
							<TabPane tabId={2} class={activeTab == 2 ? 'active' : ''}>
								<Row>
									<Col lg={12}>
										<Swiper
											loop={true}
											slidesPerView={9}
											spaceBetween={20}
											autoplay={{ delay: 3000 }}
											pagination={{ clickable: true }}
											class="images-menu mb-3 swiper-initialized swiper-horizontal swiper-pointer-events"
										>
											<div class="swiper-wrapper">
												{#each swiper as item}
													<SwiperSlide>
														<div class="d-flex align-items-center border border-dashed rounded p-2">
															<div class="flex-shrink-0">
																<img src={item.img} alt="" width="65" class="rounded" />
															</div>
															<div class="flex-grow-1 ms-2">
																<Link href={null} class="stretched-link fw-medium">{item.title}</Link>
															</div>
														</div>
													</SwiperSlide>
												{/each}
											</div>
										</Swiper>
									</Col>
								</Row>
								<div class="gallery-light">
									<Row>
										{#each gallery as item}
											<Col xl={3} lg={4} sm={6}>
												<Card class="gallery-box">
													<div class="gallery-container">
														<Link class="image-popup" href="" title="">
															<img class="gallery-img img-fluid mx-auto" src={item.img} alt="" />
															<div class="gallery-overlay">
																<h5 class="overlay-caption">{item.title}</h5>
															</div>
														</Link>
													</div>
													<div class="box-content">
														<div class="d-flex align-items-center mt-2">
															<div class="flex-grow-1 text-muted">
																by <Link href="" class="text-body text-truncate">{item.auther}</Link
																>
															</div>
															<div class="flex-shrink-0">
																<div class="d-flex gap-3">
																	<button
																		type="button"
																		class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
																	>
																		<i class="ri-thumb-up-fill text-muted align-bottom me-1" />
																		{item.likes}
																	</button>
																	<button
																		type="button"
																		class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
																	>
																		<i
																			class="ri-question-answer-fill text-muted align-bottom me-1"
																		/>
																		{item.comments}
																	</button>
																</div>
															</div>
														</div>
													</div>
												</Card>
											</Col>
										{/each}
									</Row>

									<div class="mt-4">
										<Pagination
										listClassName="justify-content-center"
											class="pagination-separated mb-0"
										>
											<PaginationItem disabled>
												<PaginationLink href={null}><i class="mdi mdi-chevron-left" /></PaginationLink>
											</PaginationItem>
											<PaginationItem active>
												<PaginationLink href={null}>1</PaginationLink>
											</PaginationItem>
											<PaginationItem><PaginationLink href={null}>2</PaginationLink></PaginationItem>
											<PaginationItem><PaginationLink href={null}>3</PaginationLink></PaginationItem>
											<PaginationItem><PaginationLink href={null}>4</PaginationLink></PaginationItem>
											<PaginationItem><PaginationLink href={null}>5</PaginationLink></PaginationItem>
											<PaginationItem>
												<PaginationLink href={null}><i class="mdi mdi-chevron-right" /></PaginationLink>
											</PaginationItem>
										</Pagination>
									</div>
								</div>
							</TabPane>
							<TabPane tabId={3} class={activeTab == 3 ? 'active' : ''}>
								<Row>
									{#each news as item}
										<Col lg={6}>
											<Card class="border">
												<CardBody>
													<div class="d-sm-flex">
														<div class="flex-shrink-0">
															<img src={item.img} alt="" width="115" class="rounded-1" />
														</div>
														<div class="flex-grow-1 ms-sm-4 mt-3 mt-sm-0">
															<ul class="list-inline mb-2">
																<li class="list-inline-item">
																	<span class={`badge bg-${item.badgeClass}-subtle text-${item.badgeClass} fs-11`}
																		>{item.badgeText}</span
																	>
																</li>
															</ul>
															<h5><Link href={null}>{item.title}</Link></h5>
															<ul class="list-inline mb-0">
																<li class="list-inline-item">
																	<i class="ri-user-3-fill text-success align-middle me-1" />
																	{item.auther}
																</li>
																<li class="list-inline-item">
																	<i class="ri-calendar-2-fill text-success align-middle me-1" />
																	{item.date}
																</li>
															</ul>
														</div>
													</div>
												</CardBody>
											</Card>
										</Col>
									{/each}
								</Row>

								<Pagination
									listClassName="justify-content-center"
									class="pagination-separated mb-0 mt-4 "
								>
									<PaginationItem disabled>
										<PaginationLink href={null}><i class="mdi mdi-chevron-left" /></PaginationLink>
									</PaginationItem>
									<PaginationItem active><PaginationLink href={null}>1</PaginationLink></PaginationItem>
									<PaginationItem><PaginationLink href={null}>2</PaginationLink></PaginationItem>
									<PaginationItem><PaginationLink href={null}>3</PaginationLink></PaginationItem>
									<PaginationItem><PaginationLink href={null}>4</PaginationLink></PaginationItem>
									<PaginationItem><PaginationLink href={null}>5</PaginationLink></PaginationItem>
									<PaginationItem>
										<PaginationLink href={null}><i class="mdi mdi-chevron-right" /></PaginationLink>
									</PaginationItem>
								</Pagination>
							</TabPane>
							<TabPane tabId={4} class={activeTab == 4 ? 'active' : ''}>
								<Row>
									{#each video as item}
										<Col lg={12} class="video-list">
											<div class="list-element mt-4">
												<h5 class="mb-1"><Link href={null}>{item.title}</Link></h5>
												<p class="text-success">{item.siteLink}</p>
												<div class="d-flex flex-column flex-sm-row">
													<div class="flex-shrink-0">
														<iframe
															src={item.videoLink}
															title="YouTube video"
															allowFullScreen
															class="rounded"
														/>
													</div>
													<div class="flex-grow-1 ms-sm-3 mt-2 mt-sm-0">
														<p class="text-muted mb-0">{item.description}</p>
														<div class="border border-dashed mb-1 mt-3" />
														<ul
															class="list-inline d-flex align-items-center g-3 text-muted fs-14 mb-0"
														>
															<li class="list-inline-item me-3">
																<i class="ri-thumb-up-line align-middle me-1" />{item.likes}
															</li>
															<li class="list-inline-item me-3">
																<i
																	class="ri-question-answer-line align-middle me-1"
																/>{item.comments}
															</li>
															<li class="list-inline-item">
																<div class="d-flex align-items-center">
																	<div class="flex-shrink-0">
																		<i class="ri-user-line" />
																	</div>
																	<div class="flex-grow-1 fs-13 ms-1">
																		<span class="fw-medium">{item.auther}</span>
																	</div>
																</div>
															</li>
														</ul>
													</div>
												</div>
											</div>
										</Col>
									{/each}
									<div class="text-center">
										<button id="loadmore" class="btn btn-link text-success mt-2"
											><i class="mdi mdi-loading mdi-spin fs-20 align-middle me-2" /> Load more
										</button>
									</div>
								</Row>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</div>
</div>
