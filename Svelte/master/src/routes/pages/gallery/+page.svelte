<script>
	import Masonry from 'svelte-bricks'
	import { Card, CardBody, Col, Container, Row } from "sveltestrap";
	import Link from "svelte-link";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";

	import img1 from "../../../assets/images/small/img-1.jpg";
	import img2 from "../../../assets/images/small/img-2.jpg";
	import img3 from "../../../assets/images/small/img-3.jpg";
	import img4 from "../../../assets/images/small/img-4.jpg";
	import img5 from "../../../assets/images/small/img-5.jpg";
	import img6 from "../../../assets/images/small/img-6.jpg";
	import img7 from "../../../assets/images/small/img-7.jpg";
	import img8 from "../../../assets/images/small/img-8.jpg";
	import img9 from "../../../assets/images/small/img-9.jpg";
	import img10 from "../../../assets/images/small/img-10.jpg";
	import img11 from "../../../assets/images/small/img-11.jpg";
	import img12 from "../../../assets/images/small/img-12.jpg";

	var gallery = [
		{
			id: 1,
			img: img1,
			title: "Glasses and laptop from above",
			auther: "Ron Mackie",
			likes: "2.2K",
			comments: "1.3K",
			category: "Project",
		},
		{
			id: 2,
			img: img2,
			title: "Working at a coffee shop",
			auther: "Nancy Martino",
			likes: "2.2K",
			comments: "1.3K",
			category: "Project",
		},
		{
			id: 3,
			img: img3,
			title: "Photo was taken in Beach",
			auther: "Elwood Arter",
			likes: "2.2K",
			comments: "1.3K",
			category: "Project",
		},
		{
			id: 4,
			img: img4,
			title: "Drawing a sketch",
			auther: "Jason McQuaid",
			likes: "2.2K",
			comments: "1.3K",
			category: "Project",
		},
		{
			id: 5,
			img: img5,
			title: "Working from home little spot",
			auther: "Henry Baird",
			likes: "2.2K",
			comments: "1.3K",
			category: "Project",
		},
		{
			id: 6,
			img: img6,
			title: "Glasses and laptop from above",
			auther: "Erica Kernan",
			likes: "2.2K",
			comments: "1.3K",
			category: "Designing",
		},
		{
			id: 7,
			img: img7,
			title: "Sunrise above a beach",
			auther: "James Ballard",
			likes: "2.2K",
			comments: "1.3K",
			category: "Development",
		},
		{
			id: 8,
			img: img8,
			title: "Project discussion with team",
			auther: "Ruby Griffin",
			likes: "2.2K",
			comments: "1.3K",
			category: "Designing",
		},
		{
			id: 9,
			img: img9,
			title: "Dramatic clouds at the Golden Gate Bridge",
			auther: "Ron Mackie",
			likes: "2.2K",
			comments: "1.3K",
			category: "Photography",
		},
		{
			id: 10,
			img: img10,
			title: "Fun day at the Hill Station",
			auther: "Henry Baird",
			likes: "2.2K",
			comments: "1.3K",
			category: "Development",
		},
		{
			id: 11,
			img: img11,
			title: "Cycling in the countryside",
			auther: "Nancy Martino",
			likes: "2.2K",
			comments: "1.3K",
			category: "Designing",
		},
		{
			id: 12,
			img: img12,
			title: "A mix of friends and strangers heading off to find an adventure.",
			auther: "Erica Kernan",
			likes: "2.2K",
			comments: "1.3K",
			category: "Designing",
		},
		{
			id: 13,
			img: img8,
			title: "Project discussion with team",
			auther: "Ruby Griffin",
			likes: "2.2K",
			comments: "1.3K",
			category: "Photography",
		},
	];
	let displayCategory = "All";
	let originalGallery = [...gallery]; // Create a copy of the original gallery data

	function setCategory(category) {
		displayCategory = category;

		if (displayCategory === "All") {
			// If category is "All", reset the gallery data to the original data
			gallery = [...originalGallery];
		} else {
			// Filter the gallery based on the selected category
			gallery = originalGallery.filter(item => item.category === displayCategory);
		}
	}

	let [minColWidth, maxColWidth, gap] = [320, 430, 5]
  	let width, height
</script>

<svelte:head>
	<title>Gallery | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Gallery" pageTitle="Pages" />
		<Row>
			<Col lg={12}>
				<div class="">
					<CardBody class="px-1">
						<Row>
							<Col lg={12}>
								<div class="text-center">
									<ul
										class="list-inline categories-filter animation-nav"
										id="filter"
									>
										<li class="list-inline-item">
											<a
												href={null}
												on:click={() =>
													setCategory("All")}
												class={displayCategory === "All"
													? "categories active"
													: "categories"}
												data-filter="*">All</a
											>
										</li>
										<li class="list-inline-item">
											<a
												href={null}
												on:click={() =>
													setCategory("Project")}
												class={displayCategory ===
												"Project"
													? "categories active"
													: "categories"}
												data-filter=".project"
												>Project</a
											>
										</li>
										<li class="list-inline-item">
											<a
												href={null}
												on:click={() =>
													setCategory("Designing")}
												class={displayCategory ===
												"Designing"
													? "categories active"
													: "categories"}
												data-filter=".designing"
												>Designing</a
											>
										</li>
										<li class="list-inline-item">
											<a
												href={null}
												on:click={() =>
													setCategory("Photography")}
												class={displayCategory ===
												"Photography"
													? "categories active"
													: "categories"}
												data-filter=".photography"
												>Photography</a
											>
										</li>
										<li class="list-inline-item">
											<a
												href={null}
												on:click={() =>
													setCategory("Development")}
												class={displayCategory ===
												"Development"
													? "categories active"
													: "categories"}
												data-filter=".development"
												>Development</a
											>
										</li>
									</ul>
								</div>
								<Masonry
								items={gallery}
									{minColWidth}
									{maxColWidth}
									{gap}
									let:item
									bind:width
									bind:height
									animate={true}
								>
									 
										<div
											class="col element-item project designing development"
										>
											<Card class="gallery-box">
												<div class="gallery-container">
													<Link
														class="image-popup"
														href={null}
														title=""
													>
														<img
														class="gallery-img img-fluid mx-auto"
														src={item.img}
														alt=""
														/>
													
											
														<div
															class="gallery-overlay"
														>
															<h5
																class="overlay-caption"
															>
																{item.title}
															</h5>
														</div>
													</Link>
												</div>

												<div class="box-content">
													<div
														class="d-flex align-items-center mt-1"
													>
														<div
															class="flex-grow-1 text-muted"
														>
															by <Link
																href={null}
																class="text-body text-truncate"
																>{item.auther}</Link
															>
														</div>
														<div
															class="flex-shrink-0"
														>
															<div
																class="d-flex gap-3"
															>
																<button
																	type="button"
																	class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0 material-shadow-none"
																>
																	<i
																		class="ri-thumb-up-fill text-muted align-bottom me-1"
																	/>
																	{item.likes}
																</button>
																<button
																	type="button"
																	class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0 material-shadow-none"
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
										</div>
									
								</Masonry>
								<div class="text-center mt-2 mb-4">
									<Link href={null} class="text-success material-shadow-none"
										><i
											class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"
										/> Load More
									</Link>
								</div>
							</Col>
						</Row>
					</CardBody>
				</div>
			</Col>
		</Row>
	</Container>
</div>
