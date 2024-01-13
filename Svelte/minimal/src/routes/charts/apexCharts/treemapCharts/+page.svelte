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
	import BasicTreemap from "./BasicTreemap.svelte";
	import MultiTreemap from "./MultiTreemap.svelte";
	import DiffColorTreemap from "./DiffColorTreemap.svelte";
	import ColorRangeTreemap from "./ColorRangeTreemap.svelte";
</script>

<svelte:head>
	<title>Apex Treemap Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Treemap Charts" pageTitle="Apexcharts" />
		<Row>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Treemap Charts</h4>
					</CardHeader>

					<CardBody>
						<BasicTreemap dataColors={["--vz-primary"]} />
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Multi-Dimensional Treemap Chart
						</h4>
					</CardHeader>

					<CardBody>
						<MultiTreemap
							dataColors={["--vz-primary", "--vz-info"]}
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
							Distributed Treemap Chart (Different Color for each
							Cell)
						</h4>
					</CardHeader>

					<CardBody>
						<DiffColorTreemap
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-info",
								"--vz-light",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Treemap Chart with Color Ranges
						</h4>
					</CardHeader>
					<CardBody>
						<ColorRangeTreemap
							dataColors={["--vz-info", "--vz-primary"]}
						/>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
