<script>
    import { Card, CardBody, Col, Row,Label } from 'sveltestrap';
    import Link from 'svelte-link';
    //swiper
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import "swiper/css";
    import "swiper/css/pagination";
    import 'swiper/scss/navigation';
    import 'swiper/css/autoplay';
    import { Autoplay, Mousewheel } from "swiper";

    //import images
    import img3 from "../../assets/images/products/img-3.png";
    import img4 from "../../assets/images/products/img-4.png";
    import img5 from "../../assets/images/products/img-5.png";
    import img6 from "../../assets/images/products/img-6.png";
    import img8 from "../../assets/images/products/img-8.png";

    import avatar1 from "../../assets/images/users/avatar-1.jpg";
    import avatar2 from "../../assets/images/users/avatar-2.jpg";
    import avatar3 from "../../assets/images/users/avatar-3.jpg";
    import avatar4 from "../../assets/images/users/avatar-4.jpg";
    import avatar5 from "../../assets/images/users/avatar-5.jpg";

    const confirnPayment = () => {
        if (document.querySelector('input[name=listGroupRadioGrid]:checked')) {
            document.getElementById("notification-overlay").style.visibility = "visible";
            document.getElementById("notification-overlay").style.opacity = "1";
    
            var checkedElem = document.querySelector('input[name=listGroupRadioGrid]:checked').parentElement;
            var payamount = checkedElem.querySelector(".pay-amount").innerHTML
            document.querySelector("#notification-overlay .success-pay").innerHTML = payamount
        } else {
            document.getElementById("notification-warn").classList.remove("d-none");
            setTimeout(() => document.getElementById("notification-warn").classList.add("d-none"), 2000);
        }
    }

    const backToHome = () => {
        document.getElementById("notification-overlay").style.visibility = "hidden";
        document.getElementById("notification-overlay").style.opacity = "0";
    }

    let setCount = 2;

    const updatecount = (newval) => {
        setCount = newval;
    }
    
</script>

<Row>
    <Col xs={12}>
        <h5 class="text-decoration-underline mb-3 mt-2 pb-3">Ecommerce Widgets</h5>
    </Col>
</Row>

<Row>
    <Col xl={3} md={6}>
        <Card class="card-height-100">
            <div class="card-header align-items-center d-flex">
                <h4 class="card-title mb-0 flex-grow-1">Hot Products</h4>
                <div class="flex-shrink-0">
                    <Link class="text-muted" href="!#">
                        View All
                    </Link>
                </div>
            </div>
            <CardBody>
            <Swiper
                direction={"horizontal"}
                slidesPerView={1.5}
                spaceBetween={10}
                mousewheel={true}
                loop={false}
                autoplay={{
                    delay: 2000,
                    disableOnInteraction: false,
                }}
                modules={[Autoplay, Mousewheel]}
                class="mySwiper vertical-swiper"
                >
                    <SwiperSlide style="max-width: 200px">
                        <div>
                            <div class="bg-info-subtle rounded">
                                <img src={img3} alt="" style="max-height: 210px;max-width: auto" />
                            </div>
                            <div class="pt-3">
                                <h5 class="text-secondary">$99.94</h5>
                                <a href={null}>
                                    <h6 class="fs-15 lh-base text-truncate mb-0">350 ml Glass Grocery Container</h6>
                                </a>
                            </div>
                        </div>
                    </SwiperSlide>
                    <SwiperSlide style="max-width: 200px">
                        <div>
                            <div class="bg-success-subtle rounded">
                                <img src={img4} alt="" style="max-height: 210px;max-width: auto" />
                            </div>
                            <div class="pt-3">
                                <h5 class="text-secondary">$99.94</h5>
                                <a href={null}>
                                    <h6 class="fs-15 lh-base text-truncate mb-0">Fabric Dual Tone Living Room Chair</h6>
                                </a>
                            </div>
                        </div>
                    </SwiperSlide>
                    <SwiperSlide style="max-width: 200px">
                        <div>
                            <div class="bg-warning-subtle rounded">
                                <img src={img5} alt="" style="max-height: 210px;max-width: auto" />
                            </div>
                            <div class="pt-3">
                                <h5 class="text-secondary">$99.94</h5>
                                <a href={null}>
                                    <h6 class="fs-15 lh-base text-truncate mb-0">Crux Motorsports Helmet</h6>
                                </a>
                            </div>
                        </div>
                    </SwiperSlide>
                    <SwiperSlide style="max-width: 200px">
                        <div>
                            <div class="bg-secondary-subtle rounded">
                                <img src={img6} alt="" style="max-height: 210px;max-width: auto" />
                            </div>
                            <div class="pt-3">
                                <h5 class="text-secondary">$99.94</h5>
                                <a href={null}>
                                    <h6 class="fs-15 lh-base text-truncate mb-0">Half Sleeve T-Shirts (Blue)</h6>
                                </a>
                            </div>
                        </div>
                    </SwiperSlide>
                </Swiper>
            </CardBody>
        </Card>
    </Col>

    <Col xl={3} ms={6}>
        <Card class="card-height-100">
            <CardBody>
                <div class="d-flex align-items-center mb-3">
                    <div class="avatar-sm me-3 flex-shrink-0">
                        <div class="avatar-title bg-info-subtle rounded">
                            <img src={img6} alt="" class="avatar-xs" />
                        </div>
                    </div>
                    <div class="flex-grow-1">
                        <p class="text-muted mb-2">Adidas</p>
                        <h5 class="fs-15 fw-bold mb-0">Half Sleeve T-Shirts (Blue)</h5>
                    </div>
                </div>
                <p class="text-muted pb-1">If you couldn't relate to the information in the previous point, you might be looking for the singlet T-shirt, which is also known as the half T-shirt.</p>

                <Row class="mb-4">
                    <Col xl={6}>
                        <h6 class="fs-14 mb-2">Sizes</h6>
                        <ul class="clothes-size list-unstyled hstack gap-2 mb-0">
                            <li>
                                <input type="radio" name="sizes" id="color-1" disabled />
                                <Label class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle" html-for="color-1">S</Label>
                            </li>
                            <li>
                                <input type="radio" name="sizes" id="color-2" />
                                <Label class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle" html-for="color-2">M</Label>
                            </li>
                            <li>
                                <input type="radio" name="sizes" id="color-3" />
                                <Label class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle" html-for="color-3">L</Label>
                            </li>
                            <li>
                                <input type="radio" name="sizes" id="color-4" />
                                <Label class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle" html-for="color-4">XL</Label>
                            </li>
                        </ul>
                    </Col>
                    <Col xl={6}>
                        <div>
                            <h6 class="fs-14 mb-2">Colors</h6>
                            <div class="d-flex flex-wrap gap-2 select-color">
                                <div data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="Out of Stock">
                                    <button type="button" class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-primary" disabled>
                                        <i class="ri-checkbox-blank-circle-fill"></i>
                                    </button>
                                </div>
                                <div data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="03 Items Available">
                                    <button type="button" class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-secondary">
                                        <i class="ri-checkbox-blank-circle-fill"></i>
                                    </button>
                                </div>
                                <div data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="03 Items Available">
                                    <button type="button" class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-success">
                                        <i class="ri-checkbox-blank-circle-fill"></i>
                                    </button>
                                </div>
                                <div data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="02 Items Available">
                                    <button type="button" class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-info">
                                        <i class="ri-checkbox-blank-circle-fill"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </Col>
                </Row>

                <div class="d-flex mb-4 align-items-center">
                    <div class="flex-grow-1">
                        <h5 class="text-primary fs-18 mb-0"><span>$22.45</span> <small class="text-decoration-line-through text-muted fs-13">$37.45</small></h5>
                    </div>
                    
                    <div class="input-step flex-shrink-0">
                        <button type="button" class="minus" on:click={ updatecount(setCount - 1) }>–</button>
                        <input type="number" class="product-quantity" value={setCount} min="0" max="100" />
                        <button type="button" class="plus" on:click={ updatecount(setCount + 1) }>+</button>
                    </div>
                </div>

                <Link href={null} class="btn btn-soft-danger d-block">Add to Cart</Link>

            </CardBody>
        </Card>
    </Col>

    <Col xl={3} md={6}>
        <Card>
            <CardBody class="position-relative">
                <h5 class="mb-3 fw-semibold">Select Bank</h5>
                <div class="vstack gap-2">
                    <div class="form-check card-radio">
                        <input id="listGroupRadioGrid1" name="listGroupRadioGrid" type="radio" class="form-check-input" /> 
                        <Label class="form-check-label" html-for="listGroupRadioGrid1">
                            <div class="d-flex align-items-center">
                                <div class="flex-shrink-0">
                                    <div class="avatar-xs">
                                        <div class="avatar-title bg-success-subtle text-success fs-18 rounded">
                                            <i class="ri-visa-fill"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex-grow-1 ms-3">
                                    <h6 class="mb-1">Visa Card</h6>
                                    <b class="pay-amount">$8,500</b>
                                </div>
                            </div>
                        </Label>
                    </div>
                    <div class="form-check card-radio">
                        <input id="listGroupRadioGrid2" name="listGroupRadioGrid" type="radio" class="form-check-input" />
                        <Label class="form-check-label" html-for="listGroupRadioGrid2">
                            <div class="d-flex align-items-center">
                                <div class="flex-shrink-0">
                                    <div class="avatar-xs">
                                        <div class="avatar-title bg-info-subtle text-info fs-18 rounded">
                                            <i class="ri-bank-card-2-line"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex-grow-1 ms-3">
                                    <h6 class="mb-1">Credit Card</h6>
                                    <b class="pay-amount">$8,326</b>
                                </div>
                            </div>
                        </Label>
                    </div>
                    <div class="form-check card-radio">
                        <input id="listGroupRadioGrid3" name="listGroupRadioGrid" type="radio" class="form-check-input" />
                        <Label class="form-check-label" html-for="listGroupRadioGrid3">
                            <div class="d-flex align-items-center">
                                <div class="flex-shrink-0">
                                    <div class="avatar-xs">
                                        <div class="avatar-title bg-danger-subtle text-danger fs-18 rounded">
                                            <i class="ri-mastercard-line"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex-grow-1 ms-3">
                                    <h6 class="mb-1">Mastercard Card</h6>
                                    <b class="pay-amount">$8,400</b>
                                </div>
                            </div>
                        </Label>
                    </div>
                </div>
    
                <button type="button" class="btn btn-success w-100 mt-3" id="confirm-btn" on:click={confirnPayment}>Confirm</button>
    
                <div id="notification-warn" class="position-absolute top-0 start-0 end-0 d-none">
                    <div class="alert alert-warning" role="alert">
                        Select at list one item
                    </div>
                </div>
    
                <div class="notification-elem" id="notification-overlay">
                    <div class="text-center">
                        <lord-icon src="https://cdn.lordicon.com/lupuorrc.json" trigger="loop" colors="primary:#0ab39c,secondary:#405189" style="width:10px;height:20px"></lord-icon>
                        <div class="mt-4 pt-2">
                            <h5 class="mb-1 success-pay">$6,201 Payment Successfully</h5>
                            <p class="text-muted mx-4">Aww yeah, you successfully read this important message.</p>
    
                            <div>
                                <button type="button" class="btn btn-danger btn-sm w-sm" id="back-btn" on:click={backToHome}>Back to Home</button>
                            </div>
                        </div>
                    </div>
                </div>
            </CardBody>
        </Card>
    </Col>

    <Col xl={3} ms={6}>
        <Card class="card-height-100">
            <CardBody>
                <div class="d-flex align-items-center mb-3">
                    <div class="avatar-sm me-3 flex-shrink-0">
                        <div class="avatar-title bg-info-subtle rounded">
                            <img src={img8} alt="" class="avatar-xs" />
                        </div>
                    </div>
                    <div class="flex-grow-1">
                        <p class="text-muted mb-2">Adidas</p>
                        <h5 class="fs-15 fw-bold mb-0">Half Sleeve T-Shirts (Blue)</h5>
                    </div>
                </div>
                <p class="text-muted pb-1">If you couldn't relate to the information in the previous point, you might be looking for the singlet T-shirt, which is also known as the half T-shirt.</p>

                <Row class="mb-4">
                    <Col xl={6}>
                        <h6 class="fs-14 mb-2">Sizes</h6>
                        <ul class="clothes-size list-unstyled hstack gap-2 mb-0">
                            <li>
                                <input type="radio" name="sizes" id="color-1" disabled />
                                <Label class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle" html-for="color-1">S</Label>
                            </li>
                            <li>
                                <input type="radio" name="sizes" id="color-2" />
                                <Label class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle" html-for="color-2">M</Label>
                            </li>
                            <li>
                                <input type="radio" name="sizes" id="color-3" />
                                <Label class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle" html-for="color-3">L</Label>
                            </li>
                            <li>
                                <input type="radio" name="sizes" id="color-4" />
                                <Label class="avatar-xs btn btn-soft-primary p-0 d-flex align-items-center justify-content-center rounded-circle" html-for="color-4">XL</Label>
                            </li>
                        </ul>
                    </Col>
                    <Col xl={6}>
                        <div>
                            <h6 class="fs-14 mb-2">Colors</h6>
                            <div class="d-flex flex-wrap gap-2 select-color">
                                <div data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="Out of Stock">
                                    <button type="button" class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-primary" disabled>
                                        <i class="ri-checkbox-blank-circle-fill"></i>
                                    </button>
                                </div>
                                <div data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="03 Items Available">
                                    <button type="button" class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-secondary">
                                        <i class="ri-checkbox-blank-circle-fill"></i>
                                    </button>
                                </div>
                                <div data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="03 Items Available">
                                    <button type="button" class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-success">
                                        <i class="ri-checkbox-blank-circle-fill"></i>
                                    </button>
                                </div>
                                <div data-bs-toggle="tooltip" data-bs-trigger="hover" data-bs-placement="top" title="02 Items Available">
                                    <button type="button" class="btn avatar-xs p-0 d-flex align-items-center justify-content-center border rounded-circle fs-22 text-info">
                                        <i class="ri-checkbox-blank-circle-fill"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </Col>
                </Row>

                <div class="d-flex mb-4 align-items-center">
                    <div class="flex-grow-1">
                        <h5 class="text-primary fs-18 mb-0"><span>$22.45</span> <small class="text-decoration-line-through text-muted fs-13">$37.45</small></h5>
                    </div>
                    
                    <div class="input-step flex-shrink-0">
                        <button type="button" class="minus" on:click={() => setCount(setCount - 1)}>–</button>
                        <input type="number" class="product-quantity" defaultValue={setCount} min="0" max="100" />
                        <button type="button" class="plus" on:click={() => setCount(setCount + 1)}>+</button>
                    </div>
                </div>

                <Link href={null} class="btn btn-soft-danger d-block">Add to Cart</Link>

            </CardBody>
        </Card>
    </Col>
</Row>

<Row>
    <Col class="col-xxl-5">
        <Card>
            <Row class="g-0">
                <Col lg={6}>
                    <CardBody class="border-end">
                        <div class="search-box">
                            <input type="text" class="form-control bg-light border-light" autoComplete="off" id="searchList" placeholder="Search candidate..." />
                            <i class="ri-search-line search-icon"></i>
                        </div>
                        <div data-simplebar style="max-height: 190px;" class="px-3 mx-n3">
                            <ul class="list-unstyled mb-0 pt-2" id="candidate-list">
                                <li>
                                    <Link href="!#" class="d-flex align-items-center py-2">
                                        <div class="flex-shrink-0 me-2">
                                            <div class="avatar-xs">
                                                <img src={avatar1} alt="" class="img-fluid rounded-circle candidate-img" />
                                            </div>
                                        </div>
                                        <div class="flex-grow-1">
                                            <h5 class="fs-13 mb-1 text-truncate"><span class="candidate-name">Anna Adame</span> <span class="text-muted fw-normal">@Anna</span></h5>
                                            <div class="d-none candidate-position">Web Developer</div>
                                        </div>
                                    </Link>
                                </li>

                                <li>
                                    <Link href="!#" class="d-flex align-items-center py-2">
                                        <div class="flex-shrink-0 me-2">
                                            <div class="avatar-xs">
                                                <img src={avatar2} alt="" class="img-fluid rounded-circle candidate-img" />
                                            </div>
                                        </div>
                                        <div class="flex-grow-1">
                                            <h5 class="fs-13 mb-1 text-truncate"><span class="candidate-name">Patricia Cavin</span> <span class="text-muted fw-normal">@Patricia</span></h5>
                                            <div class="d-none candidate-position">Web Developer</div>
                                        </div>
                                    </Link>
                                </li>
                                <li>
                                    <Link href="!#" class="d-flex align-items-center py-2">
                                        <div class="flex-shrink-0 me-2">
                                            <div class="avatar-xs">
                                                <img src={avatar3} alt="" class="img-fluid rounded-circle candidate-img" />
                                            </div>
                                        </div>
                                        <div class="flex-grow-1">
                                            <h5 class="fs-13 mb-1 text-truncate"><span class="candidate-name">Jason Tran</span> <span class="text-muted fw-normal">@Jason</span></h5>
                                            <div class="d-none candidate-position">Magento Developer</div>
                                        </div>
                                    </Link>
                                </li>
                                <li>
                                    <Link href="!#" class="d-flex align-items-center py-2">
                                        <div class="flex-shrink-0 me-2">
                                            <div class="avatar-xs">
                                                <img src={avatar4} alt="" class="img-fluid rounded-circle candidate-img" />
                                            </div>
                                        </div>
                                        <div class="flex-grow-1">
                                            <h5 class="fs-13 mb-1 text-truncate"><span class="candidate-name">Cheryl Moore</span> <span class="text-muted fw-normal">@Cheryl</span></h5>
                                            <div class="d-none candidate-position">Product Designer</div>
                                        </div>
                                    </Link>
                                </li>
                                <li>
                                    <Link href="!#" class="d-flex align-items-center py-2">
                                        <div class="flex-shrink-0 me-2">
                                            <div class="avatar-xs">
                                                <img src={avatar5} alt="" class="img-fluid rounded-circle candidate-img" />
                                            </div>
                                        </div>
                                        <div class="flex-grow-1">
                                            <h5 class="fs-13 mb-1 text-truncate"><span class="candidate-name">Jennifer Bailey</span> <span class="text-muted fw-normal">@Jennifer</span></h5>
                                            <div class="d-none candidate-position">Marketing Director</div>
                                        </div>
                                    </Link>
                                </li>
                            </ul>
                        </div>
                    </CardBody>
                </Col>
                <div class="col-lg-6">
                    <div class="card-body text-center">
                        <div class="avatar-md mb-3 mx-auto">
                            <img src={avatar1} alt="" id="candidate-img" class="img-thumbnail rounded-circle shadow-none" />
                        </div>

                        <h5 id="candidate-name" class="mb-0">Anna Adame</h5>
                        <p id="candidate-position" class="text-muted">Web Developer</p>

                        <div class="d-flex gap-2 justify-content-center mb-3">
                            <button type="button" class="btn avatar-xs p-0" data-bs-toggle="tooltip" data-bs-placement="top" title="Google">
                                <span class="avatar-title rounded-circle bg-light text-body">
                                    <i class="ri-google-line"></i>
                                </span>
                            </button>

                            <button type="button" class="btn avatar-xs p-0" data-bs-toggle="tooltip" data-bs-placement="top" title="Linkedin">
                                <span class="avatar-title rounded-circle bg-light text-body">
                                    <i class="ri-linkedin-line"></i>
                                </span>
                            </button>
                            <button type="button" class="btn avatar-xs p-0" data-bs-toggle="tooltip" data-bs-placement="top" title="Dribbble">
                                <span class="avatar-title rounded-circle bg-light text-body">
                                    <i class="ri-dribbble-fill"></i>
                                </span>
                            </button>
                        </div>

                        <div>
                            <button type="button" class="btn btn-success rounded-pill w-sm"><i class="ri-add-fill me-1 align-bottom"></i> Follow</button>
                        </div>
                    </div>
                </div>
            </Row>
        </Card>
    </Col>
</Row>