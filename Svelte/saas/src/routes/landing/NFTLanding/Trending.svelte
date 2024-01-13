<script>
    import { Container, Row, Col, Card, CardBody } from 'sveltestrap';
    import Link from 'svelte-link';

    //swiper
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import "swiper/css";
    import "swiper/css/pagination";
    import 'swiper/scss/navigation';
    import 'swiper/css/autoplay';
    import { Pagination, Autoplay, Navigation } from "swiper";

    //import Images
    import Img01 from "../../../assets/images/nft/img-01.jpg";
    import Img02 from "../../../assets/images/nft/img-02.jpg";
    import Img03 from "../../../assets/images/nft/img-03.jpg";
    import Img04 from "../../../assets/images/nft/img-04.jpg";
    import Img05 from "../../../assets/images/nft/img-05.jpg";
    import Img06 from "../../../assets/images/nft/img-06.jpg";
    
</script>
<section class="section bg-light" id="categories">
    <Container fluid>
        <Row class="justify-content-center">
            <Col lg={5}>
                <div class="text-center mb-5">
                    <h2 class="mb-3 fw-bold lh-base">Trending All Categories</h2>
                    <p class="text-muted">The process of creating an NFT may cost less than a dollar, but the process of selling it can cost up to a thousand dollars. For example, Allen Gannett, a software developer.</p>
                </div>
            </Col>
        </Row>
        <Row>
            <Col lg={12}>
                <Swiper modules={[Navigation, Autoplay, Pagination]}
                    slidesPerView={4}
                    spaceBetween={30}
                    navigation={{
                        nextEl: ".swiper-button-next",
                        prevEl: ".swiper-button-prev",
                    }}
                    pagination={{
                        el: ".swiper-pagination",
                        clickable: true,
                    }}
                    breakpoints={{
                        640: {
                            slidesPerView: 2,
                            spaceBetween: 20,
                        },
                        768: {
                            slidesPerView: 3,
                            spaceBetween: 24,
                        },
                        1024: {
                            slidesPerView: 4,
                            spaceBetween: 30,
                        },
                    }}
                    loop={true}
                    autoplay={{ delay: 2500, disableOnInteraction: false }}
                    class="mySwiper swiper mySwiper pb-4">
                        <SwiperSlide>
                            <Card>
                                <CardBody>
                                    <Row class="g-1 mb-3">
                                        <Col lg={6}>
                                            <img src={Img06} alt="" class="img-fluid rounded" />
                                            <img src="https://img.themesbrand.com/velzon/images/img-2.gif" alt="" class="img-fluid rounded mt-1" />
                                        </Col>
                                        <Col lg={6}>
                                            <img src="https://img.themesbrand.com/velzon/images/img-5.gif" alt="" class="img-fluid rounded mb-1" />
                                            <img src={Img03} alt="" class="img-fluid rounded" />
                                        </Col>
                                    </Row>
                                    <Link href={null} class="float-end"> View All <i class="ri-arrow-right-line align-bottom"></i></Link>
                                    <h5 class="mb-0 fs-16"><Link href={null} class="text-body">Artwork <span class="badge badge-soft-success">206</span></Link></h5>
                                </CardBody>
                            </Card>
                        </SwiperSlide>
                        <SwiperSlide>
                            <Card>
                                <CardBody>
                                    <Row class="g-1 mb-3">
                                        <Col lg={6}>
                                            <img src={Img05} alt="" class="img-fluid rounded" />
                                            <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt="" class="img-fluid rounded mt-1" />
                                        </Col>
                                        <Col lg={6}>
                                            <img src="https://img.themesbrand.com/velzon/images/img-4.gif" alt="" class="img-fluid rounded mb-1" />
                                            <img src={Img04} alt="" class="img-fluid rounded" />
                                        </Col>
                                    </Row>
                                    <Link href={null} class="float-end"> View All <i class="ri-arrow-right-line align-bottom"></i></Link>
                                    <h5 class="mb-0 fs-16"><Link href={null} class="text-body">Crypto Card <span class="badge badge-soft-success">743</span></Link></h5>
                                </CardBody>
                            </Card>
                        </SwiperSlide>
                        <SwiperSlide>
                            <Card>
                                <CardBody>
                                    <Row class="g-1 mb-3">
                                        <Col lg={6}>
                                            <img src={Img02} alt="" class="img-fluid rounded" />
                                            <img src="https://img.themesbrand.com/velzon/images/img-3.gif" alt="" class="img-fluid rounded mt-1" />
                                        </Col>
                                        <Col lg={6}>
                                            <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt="" class="img-fluid rounded mb-1" />
                                            <img src={Img01} alt="" class="img-fluid rounded" />
                                        </Col>
                                    </Row>
                                    <Link href={null} class="float-end"> View All <i class="ri-arrow-right-line align-bottom"></i></Link>
                                    <h5 class="mb-0 fs-16"><Link href={null} class="text-body">Music <span class="badge badge-soft-success">679</span></Link></h5>
                                </CardBody>
                            </Card>
                        </SwiperSlide>
                        <SwiperSlide>
                            <Card>
                                <CardBody>
                                    <Row class="g-1 mb-3">
                                        <Col lg={6}>
                                            <img src={Img03} alt="" class="img-fluid rounded" />
                                            <img src="https://img.themesbrand.com/velzon/images/img-5.gif" alt="" class="img-fluid rounded mt-1" />
                                        </Col>
                                        <Col lg={6}>
                                            <img src="https://img.themesbrand.com/velzon/images/img-2.gif" alt="" class="img-fluid rounded mb-1" />
                                            <img src={Img05} alt="" class="img-fluid rounded" />
                                        </Col>
                                    </Row>
                                    <Link href={null} class="float-end"> View All <i class="ri-arrow-right-line align-bottom"></i></Link>
                                    <h5 class="mb-0 fs-16"><Link href={null} class="text-body">Games <span class="badge badge-soft-success">341</span></Link></h5>
                                </CardBody>
                            </Card>
                        </SwiperSlide>
                        <SwiperSlide>
                            <Card>
                                <CardBody>
                                    <Row class="g-1 mb-3">
                                        <Col lg={6}>
                                            <img src={Img02} alt="" class="img-fluid rounded" />
                                            <img src="https://img.themesbrand.com/velzon/images/img-3.gif" alt="" class="img-fluid rounded mt-1" />
                                        </Col>
                                        <Col lg={6}>
                                            <img src="https://img.themesbrand.com/velzon/images/img-1.gif" alt="" class="img-fluid rounded mb-1" />
                                            <img src={Img01} alt="" class="img-fluid rounded" />
                                        </Col>
                                    </Row>
                                    <Link href={null} class="float-end"> View All <i class="ri-arrow-right-line align-bottom"></i></Link>
                                    <h5 class="mb-0 fs-16"><Link href={null} class="text-body">Photography <span class="badge badge-soft-success">1452</span></Link></h5>
                                </CardBody>
                            </Card>
                        </SwiperSlide>
                    <div class="swiper-pagination swiper-pagination-dark"></div>
                </Swiper>
            </Col>
        </Row>
    </Container>
</section>