<script>
	import {
		Card,
		CardBody,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Row,
		Dropdown,
	} from "sveltestrap";
	import WatchListChart from "./watchListChart.svelte";
	import { Swiper, SwiperSlide } from "swiper/svelte";
	import cryptoData from "../../../common/data/cryptoPage";

	// Import Swiper styles
	import "swiper/css";
	import "swiper/css/free-mode";
	import "swiper/css/navigation";
	import "swiper/css/thumbs";
	import { Autoplay, Mousewheel } from "swiper";
</script>

<div class="d-flex align-items-center mb-3">
	<div class="flex-grow-1">
		<h5 class="mb-0">Watchlist</h5>
	</div>
	<div class="flexshrink-0">
		<button class="btn btn-primary btn-sm"
			><i class="ri-star-line align-bottom" /> Add Watchlist</button
		>
	</div>
</div>
<Swiper
	slidesPerView={4}
	spaceBetween={24}
	mousewheel={true}
	autoplay={{
		delay: 2000,
		disableOnInteraction: false,
	}}
	modules={[Autoplay, Mousewheel]}
	class="cryptoSlider"
>
	{#each cryptoData.watchlist as item}
		<SwiperSlide>
			<Card>
				<CardBody>
					<div class="float-end">
						<Dropdown>
							<DropdownToggle color="" class="text-reset p-0">
								<span class="text-muted fs-18">
									<i class="mdi mdi-dots-horizontal" />
								</span>
							</DropdownToggle>
							<DropdownMenu class="dropdown-menu-end" end>
								<DropdownItem>View Details</DropdownItem>
								<DropdownItem>Remove Watchlist</DropdownItem>
							</DropdownMenu>
						</Dropdown>
					</div>
					<div class="d-flex align-items-center">
						<img
							src={item.img}
							class="bg-light rounded-circle p-1 avatar-xs img-fluid"
							alt=""
						/>
						<h6 class="ms-2 mb-0 fs-14">{item.coinName}</h6>
					</div>
					<Row class="align-items-end g-0">
						<Col xs={6}>
							<h5 class="mb-1 mt-4">{item.price}</h5>
							<p
								class={"fs-13 fw-medium mb-0 text-" +
									item.percentageClass}>
								{item.percentage}
								<span class="text-muted ms-2 fs-10"
									>({item.coinNameAbbr})</span
								>
							</p>
						</Col>
						<Col xs={6}>
							<div
								class="apex-charts crypto-widget"
								id="bitcoin_sparkline_charts"
								dir="ltr">
								<WatchListChart
									id={item.id}
									seriesData={item.series}
									chartsColor={item.chartsColor}
								/>
							</div>
						</Col>
					</Row>
				</CardBody>
			</Card>
		</SwiperSlide>
	{/each}
</Swiper>
