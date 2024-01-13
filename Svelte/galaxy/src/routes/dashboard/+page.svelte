<script>
	import { Container, Row, Col } from "sveltestrap";
	import Section from "./Section.svelte";
	import Widget from "./Widgets.svelte";
	import Revenue from "./Revenue.svelte";
	import SalesByLocations from "./SalesByLocations.svelte";
	import BestSellingProducts from "./BestSellingProducts.svelte";
	import TopSellers from "./TopSellers.svelte";
	import StoreVisits from "./StoreVisits.svelte";
	import RecentOrders from "./RecentOrders.svelte";
	import RecentActivity from "./RecentActivity.svelte";
	import Counter from "../../Components/Common/CounterPage.svelte";
</script>

<svelte:head>
	<title>Dashboard | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<Counter />
<div class="page-content">
	<Container fluid>
	
		<Row>
			<Col>
				<div class="h-100">
					<Section />
					<Row>
						<Widget />
					</Row>
					<Row>
						<Col xl={8}>
							<Revenue />
						</Col>
						<SalesByLocations />
					</Row>
					<Row>
						<BestSellingProducts />
						<TopSellers />
					</Row>
					<Row>
						<StoreVisits dataColors={["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.70", "--vz-primary-rgb, 0.60", "--vz-primary-rgb, 0.45"]} />
						<RecentOrders />
					</Row>
				</div>
			</Col>
			<RecentActivity />
		</Row>
	</Container>
</div>
