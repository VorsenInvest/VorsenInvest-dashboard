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

	import BasicColumn from "./BasicColumn.svelte";
	import ColumnWithLable from "./ColumnWithLable.svelte";
	import StackedColumn from "./StackedColumn.svelte";
	import StackedColumn2 from "./StackedColumn2.svelte";
	import ColumnMarker from "./ColumnMarker.svelte";
	import RotateLable from "./RotateLable.svelte";
	import NagetiveLable from "./NagetiveLable.svelte";
	import RangeColumn from "./RangeColumn.svelte";
	import DynamicColumn from "./DynamicColumn.svelte";
	import Quarter from "./Quarter.svelte";
	import DistributedColumn from "./DistributedColumn.svelte";
	import ColumnGroupLabels from "./ColumnGroupLabels.svelte";
	import GroupStackedColumn from "./GroupStackedColumn.svelte";
	import Dumbbell from "./Dumbbell.svelte";
</script>

<svelte:head>
	<title
		>Apex Column Charts | Velzon - Svelte Admin & Dashboard Template</title
	>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Column Charts" pageTitle="Apexcharts" />
		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Column Chart</h4>
					</CardHeader>
					<CardBody>
						<BasicColumn
							dataColors={[
								"--vz-gray-300",
								"--vz-primary",
								"--vz-info",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Column with Data Labels</h4>
					</CardHeader>
					<CardBody>
						<ColumnWithLable dataColors={["--vz-info"]} />
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Stacked Column Charts</h4>
					</CardHeader>
					<CardBody>
						<StackedColumn
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-warning",
								"--vz-danger",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Stacked Column 100</h4>
					</CardHeader>
					<CardBody>
						<StackedColumn2
							dataColors={[
								"--vz-primary",
								"--vz-info",
								"--vz-gray-300",
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
						<h4 class="card-title mb-0">Grouped Stacked Columns</h4>
					</CardHeader>
					<CardBody>
						<GroupStackedColumn
							dataColors={[
								"--vz-success",
								"--vz-primary",
								"--vz-secondary",
								"--vz-danger",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Dumbbell Chart</h4>
					</CardHeader>
					<CardBody>
						<Dumbbell
							dataColors={["--vz-success", "--vz-primary"]}
						/>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Column with Markers</h4>
					</CardHeader>
					<CardBody>
						<ColumnMarker
							dataColors={["--vz-success", "--vz-primary"]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Column with Rotated Labels
						</h4>
					</CardHeader>
					<CardBody>
						<RotateLable dataColors={["--vz-primary"]} />
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Column with Nagetive Values
						</h4>
					</CardHeader>
					<CardBody>
						<NagetiveLable
							dataColors={[
								"--vz-info",
								"--vz-primary",
								"--vz-gray-300",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Range Column Chart</h4>
					</CardHeader>
					<CardBody>
						<RangeColumn
							dataColors={["--vz-primary", "--vz-info"]}
						/>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Dynamic Loaded Chart</h4>
					</CardHeader>
					<CardBody>
						<div id="dynamicloadedchart-wrap">
							<div id="chart-year" class="apex-charts">
								<DynamicColumn
									dataColors={[
										"--vz-primary",
										"--vz-success",
										"--vz-warning",
										"--vz-danger",
										"--vz-dark",
										"--vz-info",
									]}
								/>
							</div>
							<div id="chart-quarter" class="apex-charts">
								<Quarter dataColors={["--vz-primary"]} />
							</div>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Distributed Columns Chart
						</h4>
					</CardHeader>
					<CardBody>
						<DistributedColumn
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-warning",
								"--vz-danger",
								"--vz-dark",
								"--vz-info",
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
						<h4 class="card-title mb-0">Column with Group Label</h4>
					</CardHeader>
					<CardBody>
						<ColumnGroupLabels dataColors={["--vz-info"]} />
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
