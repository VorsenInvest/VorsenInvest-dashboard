<script>
	import { Container, Row } from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import MarketGraph from "./MarketGraph.svelte";
	import Widgets from "./Widgets.svelte";
	import BuySellCoin from "./BuySellCoin.svelte";
	import Market from "./Market.svelte";
</script>

<svelte:head>
	<title>Buy & Sell | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Buy & Sell" pageTitle="Crypto" />
		<Row>
			<Widgets />
		</Row>
		<Row>
			<MarketGraph dataColors={["--vz-primary", "--vz-success"]}/>
			<BuySellCoin />
		</Row>
		<Market />
	</Container>
</div>
