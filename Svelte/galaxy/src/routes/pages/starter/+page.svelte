<svelte:head>
  <title>Starter | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import { Col, Container, Row } from 'sveltestrap';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Starter" pageTitle="Pages" />
		<Row>
			<Col xs={12} />
		</Row>
	</Container>
</div>
