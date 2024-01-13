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
	import BasicHeatmap from "./BasicHeatmap.svelte";
	import MultipleHeatmap from "./MultipleHeatmap.svelte";
	import ColorRange from "./ColorRange.svelte";
	import RangeWithoutShades from "./RangeWithoutShades.svelte";
</script>

<svelte:head>
	<title
		>Apex heatmap Charts | Velzon - Svelte Admin & Dashboard Template</title
	>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Heatmap Charts" pageTitle="Apexcharts" />
		<Row>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Heatmap Chart</h4>
					</CardHeader>
					<CardBody>
						<div class="live-preview">
							<BasicHeatmap dataColors={["--vz-success"]} />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Heatmap - Multiple Series
						</h4>
					</CardHeader>

					<CardBody>
						<MultipleHeatmap
							dataColors={[
								"--vz-primary",
								"--vz-secondary",
								"--vz-success",
								"--vz-info",
								"--vz-warning",
								"--vz-danger",
								"--vz-dark",
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
					<div class="card-header">
						<h4 class="card-title mb-0">Heatmap Color Range</h4>
					</div>

					<div class="card-body">
						<ColorRange
							dataColors={[
								"--vz-info",
								"--vz-success",
								"--vz-primary",
								"--vz-warning",
							]}
						/>
					</div>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<div class="card-header">
						<h4 class="card-title mb-0">
							Heatmap - Range Without Shades
						</h4>
					</div>

					<div class="card-body">
						<RangeWithoutShades
							dataColors={["--vz-info", "--vz-primary"]}
						/>
					</div>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
