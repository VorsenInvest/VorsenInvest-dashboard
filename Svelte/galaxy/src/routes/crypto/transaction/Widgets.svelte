<script>
    import { Card, CardBody, Col } from "sveltestrap";
    import Link from "svelte-link";

    import { Swiper, SwiperSlide } from "swiper/svelte";
    import "swiper/css";
    import "swiper/css/pagination";
    import { Autoplay, Mousewheel } from "swiper";
    import Counter from "./../../../Components/Common/CounterPage.svelte";
</script>

<Counter />
<Col xxl={3} md={6}>
    <Card class="card-animate">
        <CardBody>
            <div class="d-flex mb-3">
                <div class="flex-grow-1">
                    <lord-icon
                        src="//cdn.lordicon.com/fhtaantg.json"
                        trigger="loop"
                        colors="primary:#8c68cd,secondary:#4788ff"
                        style="width:55px;height:55px"
                    />
                </div>
                <div class="flex-shrink-0">
                    <Link
                        href={null}
                        class="badge bg-warning-subtle text-warning badge-border"
                        >BTC</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-info-subtle text-info badge-border"
                        >ETH</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-primary-subtle text-primary badge-border"
                        >USD</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-danger-subtle text-danger badge-border"
                        >EUR</Link
                    >
                </div>
            </div>

            <h3 class="mb-2">
                $<span class="counter-value" data-target="74858">0</span><small
                    class="text-muted fs-13">.68k</small
                >
            </h3>
            <h6 class="text-muted mb-0">Available Balance (USD)</h6>
        </CardBody>
    </Card>
</Col>
<Col xxl={3} md={6}>
    <Card class="card-animate">
        <CardBody>
            <div class="d-flex mb-3">
                <div class="flex-grow-1">
                    <lord-icon
                        src="//cdn.lordicon.com/qhviklyi.json"
                        trigger="loop"
                        colors="primary:#8c68cd,secondary:#4788ff"
                        style="width:55px;height:55px"
                    />
                </div>
                <div class="flex-shrink-0">
                    <Link
                        href={null}
                        class="badge bg-warning-subtle text-warning badge-border"
                        >BTC</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-info-subtle text-info badge-border"
                        >ETH</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-primary-subtle text-primary badge-border"
                        >USD</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-danger-subtle text-danger badge-border"
                        >EUR</Link
                    >
                </div>
            </div>

            <h3 class="mb-2">
                $<span class="counter-value" data-target="74361">0</span><small
                    class="text-muted fs-13">.34k</small
                >
            </h3>
            <h6 class="text-muted mb-0">Send (Previous Month)</h6>
        </CardBody>
    </Card>
</Col>
<Col xxl={3} md={6}>
    <Card class="card-animate">
        <CardBody>
            <div class="d-flex mb-3">
                <div class="flex-grow-1">
                    <lord-icon
                        src="//cdn.lordicon.com/yeallgsa.json"
                        trigger="loop"
                        colors="primary:#8c68cd,secondary:#4788ff"
                        style="width:55px;height:55px"
                    />
                </div>
                <div class="flex-shrink-0">
                    <Link
                        href={null}
                        class="badge bg-warning-subtle text-warning badge-border"
                        >BTC</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-info-subtle text-info badge-border"
                        >ETH</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-primary-subtle text-primary badge-border"
                        >USD</Link
                    >
                    <Link
                        href={null}
                        class="badge bg-danger-subtle text-danger badge-border"
                        >EUR</Link
                    >
                </div>
            </div>

            <h3 class="mb-2">
                $<span class="counter-value" data-target="97685">0</span><small
                    class="text-muted fs-13">.22k</small
                >
            </h3>
            <h6 class="text-muted mb-0">Receive (Previous Month)</h6>
        </CardBody>
    </Card>
</Col>
<Col xxl={3} md={6}>
    <Swiper
        slidesPerView={1}
        spaceBetween={24}
        mousewheel={true}
        loop={true}
        autoplay={{
            delay: 2000,
            disableOnInteraction: false,
        }}
        modules={[Autoplay, Mousewheel]}
        class="default-swiper rounded"
    >
        <SwiperSlide>
            <Card class="card-animate">
                <CardBody class="bg-primary-subtle">
                    <div class="d-flex mb-3">
                        <div class="flex-grow-1">
                            <lord-icon
                                src="//cdn.lordicon.com/yeallgsa.json"
                                trigger="loop"
                                colors="primary:#8c68cd,secondary:#4788ff"
                                style="width:55px;height:55px"
                            />
                        </div>
                        <div class="flex-shrink-0">
                            <Link href={null} class="fw-medium"
                                >Bitcoin (BTC)</Link
                            >
                        </div>
                    </div>
                    <h3 class="mb-2">
                        $245<small class="text-muted fs-13">.65k</small>
                    </h3>
                    <h6 class="text-muted mb-0">
                        Send - Receive (Previous Month)
                    </h6>
                </CardBody>
            </Card>
        </SwiperSlide>
        <SwiperSlide>
            <Card class="card-animate">
                <CardBody class="bg-primary-subtle">
                    <div class="d-flex mb-3">
                        <div class="flex-grow-1">
                            <lord-icon
                                src="//cdn.lordicon.com/vaeagfzc.json"
                                trigger="loop"
                                colors="primary:#8c68cd,secondary:#4788ff"
                                style="width:55px;height:55px"
                            />
                        </div>
                        <div class="flex-shrink-0">
                            <Link href={null} class="fw-medium"
                                >Ethereum (ETH)</Link
                            >
                        </div>
                    </div>
                    <h3 class="mb-2">
                        $24<small class="text-muted fs-13">.74k</small>
                    </h3>
                    <h6 class="text-muted mb-0">
                        Send - Receive (Previous Month)
                    </h6>
                </CardBody>
            </Card>
        </SwiperSlide>
        <SwiperSlide>
            <Card class="card-animate">
                <CardBody class="bg-primary-subtle">
                    <div class="d-flex mb-3">
                        <div class="flex-grow-1">
                            <lord-icon
                                src="//cdn.lordicon.com/vaeagfzc.json"
                                trigger="loop"
                                colors="primary:#8c68cd,secondary:#4788ff"
                                style="width:55px;height:55px"
                            />
                        </div>
                        <div class="flex-shrink-0">
                            <Link href={null} class="fw-medium">Monero (XMR)</Link
                            >
                        </div>
                    </div>
                    <h3 class="mb-2">
                        $124<small class="text-muted fs-13">.36k</small>
                    </h3>
                    <h6 class="text-muted mb-0">
                        Send - Receive (Previous Month)
                    </h6>
                </CardBody>
            </Card>
        </SwiperSlide>
    </Swiper>
</Col>
<svelte:head>
    <script src="//cdn.lordicon.com/xdjxvujz.js"></script>
</svelte:head>
