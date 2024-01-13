<script>
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import { Container, Row } from "sveltestrap";
	import Widgets from "./Widgets.svelte";
	import AllTransactions from "./AllTransactions.svelte";
</script>

<svelte:head>
	<script src="//cdn.lordicon.com/xdjxvujz.js"></script>
	<title>Transaction | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Transactions" pageTitle="Crypto" />
		<Row>
			<Widgets />
		</Row>
		<AllTransactions />
	</Container>
</div>
