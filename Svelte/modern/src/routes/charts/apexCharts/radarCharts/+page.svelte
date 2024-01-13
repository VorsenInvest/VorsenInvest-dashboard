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
	import SimpleRadar from "./SimpleRadar.svelte";
	import MultipleRadar from "./MultipleRadar.svelte";
	import PolygonRadar from "./PolygonRadar.svelte";
</script>

<svelte:head>
	<title>Apex Radar Charts | Velzon - Svelte Admin & Dashboard Template</title
	>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Radar Charts" pageTitle="Apexcharts" />
		<Row>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Radar Chart</h4>
					</CardHeader>

					<CardBody>
						<SimpleRadar dataColors={["--vz-success"]} />
					</CardBody>
				</Card>
			</Col>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Radar Chart - Multiple series
						</h4>
					</CardHeader>
					<CardBody>
						<MultipleRadar
							dataColors={[
								"--vz-danger",
								"--vz-success",
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
						<h4 class="card-title mb-0">
							Radar Chart - Polygon Fill
						</h4>
					</CardHeader>
					<CardBody>
						<PolygonRadar dataColors={["--vz-info"]} />
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
