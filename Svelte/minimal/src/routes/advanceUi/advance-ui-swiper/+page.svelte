<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Container,
		Row,
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";

	import {
		Pagination,
		Navigation,
		Scrollbar,
		EffectFade,
		EffectCreative,
		Mousewheel,
		EffectFlip,
		EffectCoverflow,
		Autoplay,
	} from "swiper";
	import { Swiper, SwiperSlide } from "swiper/svelte";
	import Link from "svelte-link";
	import "swiper/css";
	import "swiper/css/pagination";
	import "swiper/css/navigation";
	import "swiper/css/scrollbar";
	import "swiper/css/effect-fade";
	import "swiper/css/effect-flip";
	import "swiper/css/autoplay";

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

	const pagination = {
		clickable: true,
		renderBullet: function (index, className) {
			return '<span class="' + className + '">' + (index + 1) + "</span>";
		},
	};
</script>

<svelte:head>
	<title>Swiper Slider | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Swiper Slider" pageTitle="Advance UI" />
		<Row>
			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Default Swiper</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>default-swiper</code> class to set a default
							swiper.
						</p>

						<Swiper
							modules={[Autoplay]}
							spaceBetween={50}
							slidesPerView={1}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							paceBetween={30}
							centeredSlides={true}
							class="mySwiper"
						>
							<!--  -->
							<SwiperSlide
								><img
									src={img1}
									alt=""
									class="img-fluid"
								/></SwiperSlide
							>
							<SwiperSlide
								><img
									src={img2}
									alt=""
									class="img-fluid"
								/></SwiperSlide
							>
							<SwiperSlide
								><img
									src={img3}
									alt=""
									class="img-fluid"
								/></SwiperSlide
							>
							<!-- </div> -->
						</Swiper>
					</CardBody>
				</Card>
			</Col>

			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Navigation & Pagination Swiper
						</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>navigation-swiper</code> class to set a swiper
							with navigation and pagination.
						</p>

						<Swiper
							modules={[Navigation, Pagination, Autoplay]}
							spaceBetween={50}
							slidesPerView={1}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							navigation={true}
							paceBetween={30}
							centeredSlides={true}
							class="mySwiper swiper navigation-swiper rounded"
						>
							
								<SwiperSlide
									><img
										src={img4}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img5}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img6}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>

			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Pagination Dynamic Swiper
						</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>pagination-dynamic-swiper</code> class to set
							a dynamic swiper with pagination.
						</p>

						<Swiper
							pagination={{
								clickable: true,
								dynamicBullets: true,
							}}
							modules={[Pagination, Autoplay]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper swiper pagination-dynamic-swiper rounded dynamic-pagination"
						>
							
								<SwiperSlide
									><img
										src={img7}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img8}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img9}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>
			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Pagination Fraction Swiper
						</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>pagination-fraction-swiper</code> class to
							set a fraction swiper with pagination.
						</p>

						<Swiper
							pagination={{ type: "fraction", clickable: true }}
							navigation={true}
							modules={[Pagination, Navigation, Autoplay]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper swiper pagination-fraction-swiper rounded dynamic-pagination"
						>
							
								<SwiperSlide
									><img
										src={img10}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img11}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img12}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>
			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Pagination Custom Swiper
						</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>pagination-custom-swiper</code> class to set
							a swiper with custom pagination.
						</p>

						<Swiper
							modules={[Autoplay, Pagination, Navigation]}
							pagination={true}
							navigation={true}
							loop={true}
							autoplay={{ delay: 2500, disableOnInteraction: false }} class="mySwiper swiper pagination-custom-swiper rounded dynamic-pagination"
						>
								<SwiperSlide
									><img
										src={img2}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img3}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img4}
										alt=""
										class="img-fluid"
									/></SwiperSlide>
							<div class="swiper-pagination pagination-custom" />
						</Swiper>
					</CardBody>
				</Card>
			</Col>
			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Pagination Progress Swiper
						</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>pagination-progress-swiper</code> class to
							set a swiper with progress pagination.
						</p>

						<Swiper
							pagination={{ type: "progressbar" }}
							navigation={true}
							modules={[Pagination, Navigation, Autoplay]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper swiper pagination-progress-swiper rounded dynamic-pagination"
						>
							
								<SwiperSlide
									><img
										src={img5}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img6}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img7}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>
			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Scrollbar Swiper</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>pagination-scrollbar-swiper</code> class to
							set a swiper with scrollbar pagination.
						</p>

						<Swiper
							scrollbar={{ hide: true }}
							modules={[Scrollbar, Autoplay]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper swiper pagination-scrollbar-swiper rounded"
						>
							
								<SwiperSlide
									><img
										src={img8}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img9}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img10}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>

			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Vertical Swiper</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>vertical-swiper</code> class to set a vertical
							swiper.
						</p>

						<Swiper
							direction={"vertical"}
							pagination={{ clickable: true }}
							modules={[Pagination, Autoplay]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper swiper vertical-swiper rounded dynamic-pagination"
							style="height: 324px"
						>
							
								<SwiperSlide
									><img
										src={img11}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img12}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img1}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>

			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Mousewheel Control Swiper
						</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>mousewheel-control-swiper</code> class to set
							a swiper with mousewheel scroll.
						</p>

						<Swiper
							direction={"vertical"}
							slidesPerView={1}
							spaceBetween={30}
							mousewheel={true}
							pagination={{
								clickable: true,
							}}
							modules={[Mousewheel, Pagination, Autoplay]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper mousewheel-control-swiper rounded dynamic-pagination"
							style="height: 324px"
						>
							
								<SwiperSlide
									><img
										src={img3}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img4}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
								<SwiperSlide
									><img
										src={img5}
										alt=""
										class="img-fluid"
									/></SwiperSlide
								>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>

			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Effect Fade Swiper</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>effect-fade-swiper</code> class to set a swiper
							with fade effect.
						</p>

						<Swiper
							spaceBetween={30}
							effect={"fade"}
							pagination={{ clickable: true }}
							modules={[EffectFade, Pagination, Autoplay]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper swiper effect-fade-swiper rounded dynamic-pagination"
						>
							<SwiperSlide>
								<img
									src={img6}
									alt=""
									class="img-fluid"
								/>
							</SwiperSlide>
							<SwiperSlide>
								<img
									src={img7}
									alt=""
									class="img-fluid"
								/>
							</SwiperSlide>
							<SwiperSlide>
								<img
									src={img8}
									alt=""
									class="img-fluid"
								/>
							</SwiperSlide>
						</Swiper>
					</CardBody>
				</Card>
			</Col>
			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Effect Creative Swiper</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>effect-creative-swiper</code> class to set
							a swiper with creative custom effect.
						</p>

						<Swiper
							grabCursor={true}
							effect={"creative"}
							pagination={{ clickable: true }}
							creativeEffect={{
								prev: { shadow: true, translate: [0, 0, -400] },
								next: { translate: ["100%", 0, 0] },
							}}
							modules={[EffectCreative, Pagination, Autoplay]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper swiper effect-creative-swiper rounded dynamic-pagination"
						>
							<SwiperSlide
								><img
									src={img9}
									alt=""
									class="img-fluid"
								/></SwiperSlide
							>
							<SwiperSlide
								><img
									src={img10}
									alt=""
									class="img-fluid"
								/></SwiperSlide
							>
							<SwiperSlide
								><img
									src={img11}
									alt=""
									class="img-fluid"
								/></SwiperSlide
							>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>
			<Col xl={4} lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Effect Flip Swiper</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>effect-flip-swiper</code> class to set a swiper
							with flip effect.
						</p>

						<Swiper
							grabCursor={true}
							pagination={{ clickable: true }}
							modules={[
								EffectFlip,
								Pagination,
								Navigation,
								Autoplay,
							]}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							class="mySwiper effect-flip-swiper rounded dynamic-pagination"
						>
							
								<SwiperSlide>
									<img
										src={img12}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
								<SwiperSlide>
									<img
										src={img1}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
								<SwiperSlide>
									<img
										src={img2}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
							
						</Swiper>
					</CardBody>
				</Card>
			</Col>
			<Col lg={12}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Effect Coverflow Swiper</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>effect-coverflow-swiper</code> class to set
							a swiper with coverflow effect.
						</p>

						<Swiper
							effect={"coverflow"}
							grabCursor={true}
							centeredSlides={true}
							slidesPerView={"4"}
							loop={true}
							autoplay={{
								delay: 2500,
								disableOnInteraction: false,
							}}
							coverflowEffect={{
								rotate: 50,
								stretch: 0,
								depth: 100,
								modifier: 1,
								slideShadows: true,
							}}
							pagination={{
								clickable: true,
								dynamicBullets: true,
							}}
							modules={[EffectCoverflow, Pagination, Autoplay]}
							class="mySwiper swiper effect-coverflow-swiper rounded pb-5"
						>
							
								<SwiperSlide>
									<img
										src={img4}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
								<SwiperSlide>
									<img
										src={img5}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
								<SwiperSlide>
									<img
										src={img6}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
								<SwiperSlide>
									<img
										src={img7}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
								<SwiperSlide>
									<img
										src={img8}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
								<SwiperSlide>
									<img
										src={img9}
										alt=""
										class="img-fluid"
									/>
								</SwiperSlide>
							<div
								class="swiper-pagination swiper-pagination-dark"
							/>
						</Swiper>
					</CardBody>
				</Card>
			</Col>

			<Col lg={12}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Responsive Breakpoints Swiper
						</h4>
					</CardHeader>
					<CardBody>
						<p class="text-muted">
							Use <code>responsive-swiper</code> class to set a responsive
							swiper.
						</p>

						<Swiper
							slidesPerView={1}
							spaceBetween={10}
							pagination={{ clickable: true }}
							breakpoints={{
								640: {
									slidesPerView: 2,
									spaceBetween: 20,
								},
								768: {
									slidesPerView: 3,
									spaceBetween: 40,
								},
								1024: {
									slidesPerView: 4,
									spaceBetween: 50,
								},
							}}
							loop={true}
							modules={[Pagination]}
							class="mySwiper swiper responsive-swiper rounded gallery-light pb-4"
						>
							
								<SwiperSlide>
									<div class="gallery-box card">
										<div class="gallery-container">
											<Link
												class="image-popup"
												href={img1}
												title=""
											>
												<img
													class="gallery-img img-fluid mx-auto"
													src={img1}
													alt=""
												/>
												<div class="gallery-overlay">
													<h5 class="overlay-caption">
														Glasses and laptop from
														above
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
														href=""
														class="text-body text-truncate"
														>Ron Mackie</Link
													>
												</div>
												<div class="flex-shrink-0">
													<div class="d-flex gap-3">
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-thumb-up-fill text-muted align-bottom me-1"
															/> 2.2K
														</button>
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-question-answer-fill text-muted align-bottom me-1"
															/> 1.3K
														</button>
													</div>
												</div>
											</div>
										</div>
									</div>
								</SwiperSlide>
								<SwiperSlide
									><div class="gallery-box card">
										<div class="gallery-container">
											<Link
												class="image-popup"
												href={img2}
												title=""
											>
												<img
													class="gallery-img img-fluid mx-auto"
													src={img2}
													alt=""
												/>
												<div class="gallery-overlay">
													<h5 class="overlay-caption">
														Working at a coffee shop
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
														href=""
														class="text-body text-truncate"
														>Nancy Martino</Link
													>
												</div>
												<div class="flex-shrink-0">
													<div class="d-flex gap-3">
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-thumb-up-fill text-muted align-bottom me-1"
															/> 3.2K
														</button>
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-question-answer-fill text-muted align-bottom me-1"
															/> 1.1K
														</button>
													</div>
												</div>
											</div>
										</div>
									</div>
								</SwiperSlide>
								<SwiperSlide
									><div class="gallery-box card mb-0">
										<div class="gallery-container">
											<Link
												class="image-popup"
												href={img10}
												title=""
											>
												<img
													class="gallery-img img-fluid mx-auto"
													src={img10}
													alt=""
												/>
												<div class="gallery-overlay">
													<h5 class="overlay-caption">
														Fun day at the Hill
														Station
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
														href=""
														class="text-body text-truncate"
														>Henry Baird</Link
													>
												</div>
												<div class="flex-shrink-0">
													<div class="d-flex gap-3">
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-thumb-up-fill text-muted align-bottom me-1"
															/> 632
														</button>
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-question-answer-fill text-muted align-bottom me-1"
															/> 95
														</button>
													</div>
												</div>
											</div>
										</div>
									</div>
								</SwiperSlide>
								<SwiperSlide
									><div class="gallery-box card">
										<div class="gallery-container">
											<Link
												class="image-popup"
												href={img4}
												title=""
											>
												<img
													class="gallery-img img-fluid mx-auto"
													src={img4}
													alt=""
												/>
												<div class="gallery-overlay">
													<h5 class="overlay-caption">
														Drawing a sketch
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
														href=""
														class="text-body text-truncate"
														>Jason McQuaid</Link
													>
												</div>
												<div class="flex-shrink-0">
													<div class="d-flex gap-3">
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-thumb-up-fill text-muted align-bottom me-1"
															/> 825
														</button>
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-question-answer-fill text-muted align-bottom me-1"
															/> 101
														</button>
													</div>
												</div>
											</div>
										</div>
									</div>
								</SwiperSlide>
								<SwiperSlide
									><div class="gallery-box card">
										<div class="gallery-container">
											<Link
												class="image-popup"
												href={img6}
												title=""
											>
												<img
													class="gallery-img img-fluid mx-auto"
													src={img6}
													alt=""
												/>
												<div class="gallery-overlay">
													<h5 class="overlay-caption">
														Project discussion with
														team
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
														href=""
														class="text-body text-truncate"
														>Erica Kernan</Link
													>
												</div>
												<div class="flex-shrink-0">
													<div class="d-flex gap-3">
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-thumb-up-fill text-muted align-bottom me-1"
															/> 3.4K
														</button>
														<button
															type="button"
															class="btn btn-sm fs-12 btn-link text-body text-decoration-none px-0"
														>
															<i
																class="ri-question-answer-fill text-muted align-bottom me-1"
															/> 1.3k
														</button>
													</div>
												</div>
											</div>
										</div>
									</div>
								</SwiperSlide>
						</Swiper>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
