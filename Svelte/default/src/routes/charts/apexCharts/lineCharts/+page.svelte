<script>
	import {onMount} from 'svelte';
	import {
		Card,
		CardBody,
		CardHeader,
		Col,
		Container,
		Row,
	} from "sveltestrap";

	import BreadCrumb from "../../../../Components/Common/BreadCrumb.svelte";

	import LineAllCharts from "./LineAllCharts.svelte";
	import ZoomableTimeseries from "./ZoomableTimeseries.svelte";
	import LinewithDataLabels from "./LinewithDataLabels.svelte";
	import DashedLine from "./DashedLine.svelte";
	import LinewithAnnotations from "./LinewithAnnotations.svelte";
	import BrushChart from "./BrushChart.svelte";
	import BrushChart1 from "./BrushChart1.svelte";
	import SteplineChart from "./SteplineChart.svelte";
	import GradientCharts from "./GradientCharts.svelte";
	import MissingData from "./MissingData.svelte";
	import ChartSyncingLine from './ChartSyncingLine.svelte';
	import ChartSyncingLine2 from './ChartSyncingLine2.svelte';
	import ChartSyncingArea from './ChartSyncingArea.svelte';
	import RealtimeCharts from './RealtimeCharts.svelte';
</script>

<svelte:head>
	<title>Apex Line Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Line Charts" pageTitle="Apexcharts" />
		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Line Chart</h4>
					</CardHeader>
					<CardBody>
						<div>
							<LineAllCharts dataColors={["--vz-primary"]} />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Zoomable Timeseries</h4>
					</CardHeader>
					<CardBody>
						<ZoomableTimeseries dataColors={["--vz-success"]} />
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Line with Data Labels</h4>
					</CardHeader>
					<CardBody>
						<LinewithDataLabels
							dataColors={["--vz-primary", "--vz-success"]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Dashed Line</h4>
					</CardHeader>
					<CardBody>
						<DashedLine
							dataColors={[
								"--vz-primary",
								"--vz-danger",
								"--vz-success",
							]}
						/>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Line with Annotations</h4>
					</CardHeader>
					<CardBody>
						<LinewithAnnotations dataColors={["--vz-primary"]} />
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Brush Chart</h4>
					</CardHeader>
					<CardBody>
						<div>
							<BrushChart dataColors={["--vz-danger"]} />
						</div>
						<div>
							<BrushChart1 dataColors={["--vz-info"]} />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Stepline Chart</h4>
					</CardHeader>
					<CardBody>
						<SteplineChart dataColors={["--vz-success"]} />
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Gradient Chart</h4>
					</CardHeader>
					<CardBody>
						<div>
							<GradientCharts dataColors={["--vz-success"]} />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Missing Data/ Null Value Charts
						</h4>
					</CardHeader>
					<CardBody>
						<MissingData
							dataColors={[
								"--vz-primary",
								"--vz-danger",
								"--vz-success",
							]}
						/>
					</CardBody>
				</Card>
			</Col>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Syncing Charts</h4>
					</CardHeader>
					<CardBody>
						<div>
							<ChartSyncingLine dataColors={["--vz-primary"]} class="apex-charts" dir="ltr" />
							<ChartSyncingLine2 dataColors={["--vz-warning"]} class="apex-charts" dir="ltr" />
							<ChartSyncingArea dataColors={["--vz-success"]} class="apex-charts" dir="ltr" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Realtimes Charts
						</h4>
					</CardHeader>
					<CardBody>
						<div>
							<RealtimeCharts dataColors={["--vz-success"]} />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
