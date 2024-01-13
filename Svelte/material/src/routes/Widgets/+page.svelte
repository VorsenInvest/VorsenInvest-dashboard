<svelte:head>
  <title>Widget | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import { Container } from 'sveltestrap';
	import BreadCrumb from '../../Components/Common/BreadCrumb.svelte';
	import TileBoxs from './TileBoxs.svelte';
	import OtherWidgets from './OtherWidgets.svelte';
	import UpcomingActivity from './UpcomingActivities.svelte';
	import ChartMapWidgets from './Chart&MapWidgets.svelte';
	import EcommerceWidgets from './EcommerceWidgets.svelte';
	import CreditCard from './CreditCard.svelte';
	import WidgetData from '../../common/data/widgets';
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Widgets" pageTitle="Velzon" />
		<TileBoxs {WidgetData} />

		<OtherWidgets otherWidgets2={WidgetData.otherWidgets2} />

		 <UpcomingActivity
			widgetsActivities={WidgetData.widgetsActivities}
			widgetsTasks={WidgetData.widgetsTasks}
		/>

		 <ChartMapWidgets
			widgetsAudiences={WidgetData.widgetsAudiences}
			widgetsPortfolio={WidgetData.widgetsPortfolio}
		/>

		<EcommerceWidgets /> 
		<CreditCard />
	</Container>
</div>
