<svelte:head>
  <title>Task List | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import { Container, Row } from 'sveltestrap';
	import AllTasks from '../AllTasks.svelte';
	import Widgets from '../Widgets.svelte';
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Tasks List" pageTitle="Tasks" />
		<Row>
			<Widgets />
		</Row>
		<AllTasks />
	</Container>
</div>
