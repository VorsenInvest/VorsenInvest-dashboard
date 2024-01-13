<script>
	import { Container, Row, Card, CardBody, Col } from "sveltestrap";
	import Widgets from "./widgets.svelte";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import ICO from "./ico.svelte";
</script>

<svelte:head>
	<title>ICO List | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="ICO List" pageTitle="Crypto" />

		<Row class="row-cols-xxl-5 row-cols-lg-3 row-cols-sm-2 row-cols-1">
			<Widgets />
		</Row>
		<!--end row-->

		<ICO />
	</Container>
</div>
