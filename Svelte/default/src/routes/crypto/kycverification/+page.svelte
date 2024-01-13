<script>
	import { Container, Row } from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import KYC from "./KYCVerification.svelte";
</script>

<svelte:head>
	<title>KYC Application | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="KYC Application" pageTitle="Crypto" />
		<Row>
			<KYC />
		</Row>
	</Container>
</div>
