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
	import Simple from "./Simple.svelte";
	import ThreeDBubble from "./ThreeDBubble.svelte";
</script>

<svelte:head>
	<title
		>Apex Bubble Charts | Velzon - Svelte Admin & Dashboard Template</title
	>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Bubble Charts" pageTitle="Apexcharts" />
		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Bubble Chart</h4>
					</CardHeader>
					<CardBody>
						<Simple
							dataColors={[
								"--vz-primary",
								"--vz-info",
								"--vz-secondary",
								"--vz-success",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">3D Bubble Chart</h4>
					</CardHeader>
					<CardBody>
						<ThreeDBubble
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-info",
								"--vz-secondary",
							]}
						/>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
