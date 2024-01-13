<script>
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Container,
		Row,
	} from "sveltestrap";
	import BreadCrumb from "../../../../Components/Common/BreadCrumb.svelte";
	import BasicPolar from "./BasicPolar.svelte";
	import PolarMonochrome from "./PolarMonochrome.svelte";
</script>

<svelte:head>
	<title>Apex Polar Charts | Velzon - Svelte Admin & Dashboard Template</title
	>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Polar Charts" pageTitle="Apexcharts" />
		<Row>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Polararea Chart</h4>
					</CardHeader>
					<CardBody>
						<BasicPolar
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-warning",
								"--vz-danger",
								"--vz-info",
								"--vz-success",
								"--vz-primary",
								"--vz-dark",
								"--vz-secondary",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">PolarArea Monochrome</h4>
					</CardHeader>
					<CardBody>
						<PolarMonochrome />
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
