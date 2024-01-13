<svelte:head>
  <title>CRM | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import { Container, Row } from 'sveltestrap';
	import BreadCrumb from '../../Components/Common/BreadCrumb.svelte';

	import BalanceOverview from './BalanceOverview.svelte';
	import ClosingDeals from './ClosingDeals.svelte';
	import DealsStatus from './DealsStatus.svelte';
	import DealType from './DealType.svelte';
	import MyTasks from './MyTasks.svelte';
	import SalesForecast from './SalesForecast.svelte';
	import UpcomingActivities from './UpcomingActivities.svelte';
	import Widgets from './Widgets.svelte';
	import Counter from '../../Components/Common/CounterPage.svelte'
</script>
<Counter />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="CRM" pageTitle="Dashboards" />
		<Row>
			<Widgets />
		</Row>
		<Row>
			<SalesForecast />
			<DealType />
			<BalanceOverview />
		</Row>
		<Row>
			<DealsStatus />
			<MyTasks />
		</Row>
		<Row>
			<UpcomingActivities />
			<ClosingDeals />
		</Row>
	</Container>
</div>
