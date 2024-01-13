<svelte:head>
  <title>Tickets List | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import Counter from '../../../Components/Common/CounterPage.svelte';
	import tickitData from '../../../common/data/supportTickets';
	import Widgets from './Widgets.svelte';
	import TicketsData from './TicketsData.svelte';

	import { Row, Container } from 'sveltestrap';
</script>

<Counter />

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Tickets List" pageTitle="Invoices" />

		<Row>
			<Widgets ticketsWidgets={tickitData.ticketsWidgets} />
		</Row>

		<TicketsData />
	</Container>
</div>
