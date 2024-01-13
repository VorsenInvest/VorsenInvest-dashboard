<script>
    import { Card, CardBody, Col, Row } from "sveltestrap";
    import { Navigation, Autoplay } from "swiper";
    import { Swiper, SwiperSlide } from "swiper/svelte";
    import Link from "svelte-link";
    import "swiper/css";
    import "swiper/css/pagination";
    import "swiper/css/navigation";
    import "swiper/css/scrollbar";
    import "swiper/css/effect-fade";
    import "swiper/css/effect-flip";
    import "swiper/css/autoplay";
    import data from "../../common/data/dashboardNFT";
    import TopArtworkChart from "./TopArtworkChart.svelte";
</script>
<Row>
    <Col xxl={8}>
    <div class="d-flex pt-2 pb-4">
                <h5 class="card-title fs-18 mb-0">Featured NFTs Artworks</h5>
            </div>
    <Swiper modules={[Navigation, Autoplay]} slidesPerView={1} spaceBetween={10} 
    
     breakpoints={{ 640: { slidesPerView: 2, spaceBetween: 20, }, 768: { slidesPerView: 2, spaceBetween: 24, },
        1024: { slidesPerView: 3, spaceBetween: 24, }, }} loop={true} autoplay={{ delay: 2500, disableOnInteraction:
        false }} class="mySwiper marketplace-swiper rounded gallery-light">
       
        {#each data.featuredNFTData as item}
        <SwiperSlide>
            <div class="card explore-box card-animate rounded">
                <div class="bookmark-icon position-absolute top-0 end-0 p-2">
                    <button type="button" class="btn btn-icon active" data-bs-toggle="button" aria-pressed="true"><i
                            class="mdi mdi-cards-heart fs-16" /></button>
                </div>
                <div class="explore-place-bid-img">
                    <img src={item.img} alt="" class="img-fluid card-img-top explore-img" />
                    <div class="bg-overlay" />
                    <div class="place-bid-btn">
                        <Link href={null} class="btn btn-success"><i class="ri-auction-fill align-bottom me-1" /> Place
                        Bid</Link>
                    </div>
                </div>
                <CardBody>
                    <p class="fw-medium mb-0 float-end">
                        <i class="mdi mdi-heart text-danger align-middle" />
                        {item.price}
                    </p>
                    <h5 class="mb-1">
                        <Link href="/NFTmarketplace/Itemdetails/apps-nft-item-details" class="link-dark">{item.title}
                        </Link>
                    </h5>
                    <p class="text-muted mb-0">{item.category}</p>
                </CardBody>
                <div class="card-footer border-top border-top-dashed">
                    <div class="d-flex align-items-center">
                        <div class="flex-grow-1 fs-14">
                            <i class="ri-price-tag-3-fill text-warning align-bottom me-1" />
                            Highest:
                            <span class="fw-medium">{item.highest}</span>
                        </div>
                        <h5 class="flex-shrink-0 fs-14 text-primary mb-0">
                            {item.price}
                        </h5>
                    </div>
                </div>
            </div>
        </SwiperSlide>
        {/each}
    </Swiper>
    </Col>
    <Col xxl={4}>
    <Card>
        <div class="card-header align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">Top Artworks</h4>
            <div class="flex-shrink-0">
                <div>
                    <button type="button" class="btn btn-soft-primary btn-sm material-shadow-none">
                        See All
                    </button>
                </div>
            </div>
        </div>
        <CardBody>
            <div class="table-responsive table-card">
                <div data-simplebar style="max-height: 410px">
                    <table class="table table-borderless align-middle">
                        <tbody>
                            {#each data.topartWork as item}
                            <tr>
                                <td>
                                    <div class="d-flex align-items-center">
                                        <img src={item.img} alt="" class="avatar-sm rounded-circle" />
                                        <div class="ms-3">
                                            <Link href={null}>
                                            <h6 class="fs-15 mb-1">
                                                {item.title}
                                            </h6>
                                            </Link>
                                            <p class="mb-0 text-muted">
                                                {item.sales} Sales
                                            </p>
                                        </div>
                                    </div>
                                </td>
                                <td>
                                    <TopArtworkChart seriesData={item.series} chartsColor={item.chartsColor}
                                        id={item.id} />
                                </td>
                                <td class="text-end">
                                    <Link href={null}>
                                    <h6 class="fs-15 mb-1">
                                        ${item.collection}+
                                    </h6>
                                    </Link>
                                    <p class="mb-0 text-muted">
                                        Total USD
                                    </p>
                                </td>
                            </tr>
                            {/each}
                        </tbody>
                    </table>
                </div>
            </div>
        </CardBody>
    </Card>
    </Col>
</Row>