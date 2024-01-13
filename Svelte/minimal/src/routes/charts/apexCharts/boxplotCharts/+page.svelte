<script>
	import BreadCrumb from "../../../../Components/Common/BreadCrumb.svelte";
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Container,
		Row,
	} from "sveltestrap";

	import Basic from "./Basic.svelte";
	import Scatter from "./Scatter.svelte";
	import Horizontal from "./Horizontal.svelte";
</script>

<svelte:head>
	<title
		>Apex Boxplot Charts | Velzon - Svelte Admin & Dashboard Template</title
	>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Boxplot Charts" pageTitle="Apexcharts" />
		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Box Chart</h4>
					</CardHeader>
					<CardBody>
						<Basic dataColors={["--vz-primary", "--vz-info"]} />
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Boxplot with Scatter Chart
						</h4>
					</CardHeader>
					<CardBody>
						<Scatter
							dataColors={[
								"--vz-succcess",
								"--vz-info",
								"--vz-light",
								"--vz-primary",
							]}
						/>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Horizontal BoxPlot</h4>
					</CardHeader>
					<CardBody>
						<Horizontal dataColors={["--vz-light", "--vz-card-custom"]} />
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
