<svelte:head>
  <title>Ticket Details | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import { Container, Row } from 'sveltestrap';

	import Section from './Section.svelte';
	import TicketDescription from './TicketDescription.svelte';
	import TicketDetails from './TicketDetails.svelte';
</script>

<div class="page-content">
	<Container fluid>
		<Row>
			<Section />
		</Row>
		<Row>
            <TicketDescription />
            <TicketDetails />
		</Row>
	</Container>
</div>
