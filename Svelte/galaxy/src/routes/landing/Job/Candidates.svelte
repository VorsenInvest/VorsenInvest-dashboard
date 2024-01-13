<script>
    import { Col, Container, Row } from "sveltestrap";
    import avatar2 from "../../../assets/images/users/avatar-2.jpg";
    import avatar3 from "../../../assets/images/users/avatar-3.jpg";
    import avatar10 from "../../../assets/images/users/avatar-10.jpg";
    import avatar8 from "../../../assets/images/users/avatar-8.jpg";
    import avatar5 from "../../../assets/images/users/avatar-5.jpg";
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import { Autoplay, Mousewheel } from "swiper";
    import "swiper/css";

    import 'swiper/scss/navigation';
    import 'swiper/scss/pagination';

</script>

<section class="section bg-light" id="candidates">
    <div class="bg-overlay bg-overlay-pattern" />
    <Container>
        <Row class="justify-content-center">
            <Col class="col-lg-8">
                <div class="text-center mb-5">
                    <h1 class="mb-3 ff-secondary fw-semibold text-capitalize lh-base">
                        Hire Experts <span class="text-primary">Team</span>
                    </h1>
                    <p class="text-muted mb-4">
                        Hiring experts costs more per hour than hiring entry- or
                        mid-level freelancers, but they can usually get the work
                        done faster—and better.
                    </p>
                </div>
            </Col>
        </Row>
        <Row>
            <Col class="col-lg-12">
                <Swiper
                    autoplay={{
                        delay: 2000,
                        disableOnInteraction: false,
                    }}
                    modules={[Autoplay, Mousewheel]}
                    slidesPerView={4}
                    spaceBetween={24}
                    Autoplay={true}
                    class="swiper candidate-swiper py-3"
                >
                    
                        <SwiperSlide class="swiper-slide">
                            <div class="card text-center">
                                <div class="card-body p-4">
                                    <img
                                        src={avatar2}
                                        alt=""
                                        class="rounded-circle avatar-md mx-auto d-block"
                                    />
                                    <h5 class="fs-17 mt-3 mb-2">
                                        Nancy Martino
                                    </h5>
                                    <p class="text-muted fs-13 mb-3">
                                        Creative Designer
                                    </p>

                                    <p class="text-muted mb-4 fs-14">
                                        <i
                                            class="ri-map-pin-2-line text-primary me-1 align-bottom"
                                        />{" "}
                                        Escondido, California
                                    </p>

                                    <a href={null} class="btn btn-primary w-100">
                                        View Profile
                                    </a>
                                </div>
                            </div>
                        </SwiperSlide>
                        <SwiperSlide class="swiper-slide">
                            <div class="card text-center">
                                <div class="card-body p-4">
                                    <img
                                        src={avatar3}
                                        alt=""
                                        class="rounded-circle avatar-md mx-auto d-block"
                                    />
                                    <h5 class="fs-17 mt-3 mb-2">Glen Matney</h5>
                                    <p class="text-muted fs-13 mb-3">
                                        Marketing Director
                                    </p>

                                    <p class="text-muted mb-4 fs-14">
                                        <i
                                            class="ri-map-pin-2-line text-primary me-1 align-bottom"
                                        />{" "}
                                        Escondido, California
                                    </p>

                                    <a href={null} class="btn btn-primary w-100">
                                        View Profile
                                    </a>
                                </div>
                            </div>
                        </SwiperSlide>
                        <SwiperSlide class="swiper-slide">
                            <div class="card text-center">
                                <div class="card-body p-4">
                                    <img
                                        src={avatar10}
                                        alt=""
                                        class="rounded-circle avatar-md mx-auto d-block"
                                    />
                                    <h5 class="fs-17 mt-3 mb-2">
                                        Alexis Clarke
                                    </h5>
                                    <p class="text-muted fs-13 mb-3">
                                        Product Manager
                                    </p>

                                    <p class="text-muted mb-4 fs-14">
                                        <i
                                            class="ri-map-pin-2-line text-primary me-1 align-bottom"
                                        />{" "}
                                        Escondido, California
                                    </p>

                                    <a href={null} class="btn btn-primary w-100">
                                        View Profile
                                    </a>
                                </div>
                            </div>
                        </SwiperSlide>
                        <SwiperSlide class="swiper-slide">
                            <div class="card text-center">
                                <div class="card-body p-4">
                                    <img
                                        src={avatar8}
                                        alt=""
                                        class="rounded-circle avatar-md mx-auto d-block"
                                    />
                                    <h5 class="fs-17 mt-3 mb-2">James Price</h5>
                                    <p class="text-muted fs-13 mb-3">
                                        Product Designer
                                    </p>

                                    <p class="text-muted mb-4 fs-14">
                                        <i
                                            class="ri-map-pin-2-line text-primary me-1 align-bottom"
                                        />{" "}
                                        Escondido, California
                                    </p>

                                    <a href={null} class="btn btn-primary w-100">
                                        View Profile
                                    </a>
                                </div>
                            </div>
                        </SwiperSlide>
                        <SwiperSlide class="swiper-slide">
                            <div class="card text-center">
                                <div class="card-body p-4">
                                    <img
                                        src={avatar5}
                                        alt=""
                                        class="rounded-circle avatar-md mx-auto d-block"
                                    />
                                    <h5 class="fs-17 mt-3 mb-2">
                                        Michael Morris
                                    </h5>
                                    <p class="text-muted fs-13 mb-3">
                                        Full Stack Developer
                                    </p>

                                    <p class="text-muted mb-4 fs-14">
                                        <i
                                            class="ri-map-pin-2-line text-primary me-1 align-bottom"
                                        />{" "}
                                        Escondido, California
                                    </p>

                                    <a href={null} class="btn btn-primary w-100">
                                        View Profile
                                    </a>
                                </div>
                            </div>
                        </SwiperSlide>
                    
                </Swiper>
            </Col>
        </Row>
    </Container>
</section>
