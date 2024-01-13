<script>
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import { Col, Container, Row } from "sveltestrap";
	import Watchlist from "./Watchlist.svelte";
	import PortfolioStatistics from "./PortfolioStatistics.svelte";
	import MarketStatus from "./MarketStatus.svelte";
	import Widgets from "./Widgets.svelte";
	import RecentTransaction from "./RecentTransaction.svelte";
</script>

<svelte:head>
	<title>My Wallet | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="My Wallet" pageTitle="Crypto" />
		<Row>
			<Col xxl={9}>
				<PortfolioStatistics dataColors={["--vz-primary"]} />
				<Watchlist />
				<MarketStatus />
			</Col>
			<Col xxl={3}>
				<Widgets />
				<RecentTransaction />
			</Col>
		</Row>
	</Container>
</div>
