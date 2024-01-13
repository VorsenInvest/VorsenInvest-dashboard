<script>
	import { Swiper, SwiperSlide } from 'swiper/svelte';

	// Import Swiper styles
	import 'swiper/css';
	import 'swiper/css/pagination';

	import { Autoplay, Mousewheel } from 'swiper';
	import {
		Card,
		CardBody,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Row,
		Dropdown
	} from 'sveltestrap';

	import data from '../../common/data/crypto';
    import DashboardCryptoCharts from './DashboardCryptoCharts.svelte';
	
</script>

<Col lg={12}>
	<Swiper
		slidesPerView={5}
		spaceBetween={24}
		mousewheel={true}
		autoplay={{
			delay: 2000,
			disableOnInteraction: false
		}}
		modules={[Autoplay, Mousewheel]}
		class="cryptoSlider"
	>
		{#each data.cryptoSlider as item}
			<SwiperSlide>
				<Card>
					<CardBody>
						<div class="float-end">
							<Dropdown>
								<DropdownToggle class="text-reset p-0" color="" tag="a" role="button">
									<span class="text-muted fs-18"><i class="mdi mdi-dots-horizontal" /></span>
								</DropdownToggle>
								<DropdownMenu class="dropdown-menu dropdown-menu-end" end>
									<DropdownItem href={null}>Details</DropdownItem>
									<DropdownItem href={null}>Cancel</DropdownItem>
								</DropdownMenu>
							</Dropdown>
						</div>
						<div class="d-flex align-items-center">
							<img src={item.img} class="bg-light rounded-circle p-1 avatar-xs img-fluid" alt="" />
							<h6 class="ms-2 mb-0">{item.label}</h6>
						</div>
						<Row class="align-items-end g-0">
							<Col xs={6}>
								<h5 class="mb-1 mt-4">{item.price}</h5>
								<p class={'fw-medium mb-0 text-' + item.changeClass}>
									{item.change}<span class="text-muted ms-2 text-uppercase"
										>({item.coinName})</span
									>
								</p>
							</Col>
							<Col xs={6}>
								<div class="apex-charts crypto-widget" dir="ltr">
									<DashboardCryptoCharts seriesData={item.series} id={item.id} chartsColor={item.chartsColor} />
								</div>
							</Col>
						</Row>
					</CardBody>
				</Card>
			</SwiperSlide>
		{/each}
	</Swiper>
</Col>