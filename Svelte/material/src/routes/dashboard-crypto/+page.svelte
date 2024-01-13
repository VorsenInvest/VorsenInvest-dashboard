<svelte:head>
  <title>Crypto Dashboard | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import { Container, Row, Col } from 'sveltestrap';
	import BreadCrumb from '../../Components/Common/BreadCrumb.svelte';
	import MarketGraph from './MarketGraph.svelte';
	import MyCurrencies from './MyCurrencies.svelte';
	import MyPortfolio from './MyPortfolio.svelte';
	import NewsFeed from './NewsFeed.svelte';
	import RecentActivity from './RecentActivity.svelte';
	import TopPerformers from './TopPerformers.svelte';
	import Trading from './Trading.svelte';
	import Widgets from './Widgets.svelte';
	import Widgets1 from './Widgets1.svelte';
	import Counter from '../../Components/Common/CounterPage.svelte'
</script>
<Counter />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Crypto" pageTitle="Dashboards" />
		<Row>
			<MyPortfolio />
			<Col class="col-xxl-9 order-xxl-0 order-first">
				<Row>
					<Widgets />
				</Row>
				<MarketGraph />
			</Col>
		</Row>
		<Row>
			<Widgets1 />
		</Row>
		<Row>
			<MyCurrencies />
			<Trading />
		</Row>
		<Row>
			<RecentActivity />
			<TopPerformers />
			<NewsFeed />
		</Row>
	</Container>
</div>
