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
	import SimplePie from "./SimplePie.svelte";
	import SimpleDonut from "./SimpleDonut.svelte";
	import UpdateDonut from "./UpdateDonut.svelte";
	import MonochromePie from "./MonochromePie.svelte";
	import GradientDonut from "./GradientDonut.svelte";
	import PatternedDonut from "./PatternedDonut.svelte";
	import ImagePieChart from "./ImagePieChart.svelte";
</script>

<svelte:head>
	<title>Apex Pie Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Pie Charts" pageTitle="Apexcharts" />
		<Row>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Simple Pie Chart</h4>
					</CardHeader>

					<CardBody>
						<SimplePie
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-warning",
								"--vz-danger",
								"--vz-info",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Simple Donut Chart</h4>
					</CardHeader>
					<CardBody>
						<SimpleDonut
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-warning",
								"--vz-danger",
								"--vz-info",
							]}
						/>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row class="row">
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Updating Donut Chart</h4>
					</CardHeader>
					<CardBody>
						<div>
							<UpdateDonut
								dataColors={[
									"--vz-primary",
									"--vz-success",
									"--vz-warning",
									"--vz-danger",
									"--vz-info",
								]}
							/>
							<div class="d-flex align-items-start flex-wrap gap-2 justify-content-center mt-4">
								<button id="add" class="btn btn-light btn-sm">
									+ ADD
								</button>

								<button
									id="remove"
									class="btn btn-light btn-sm"
								>
									- REMOVE
								</button>

								<button
									id="randomize"
									class="btn btn-light btn-sm"
								>
									RANDOMIZE
								</button>

								<button id="reset" class="btn btn-light btn-sm">
									RESET
								</button>
							</div>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Monochrome Pie Chart</h4>
					</CardHeader>

					<CardBody>
						<MonochromePie dataColors={["--vz-primary"]} />
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Gradient Donut Chart</h4>
					</CardHeader>

					<CardBody>
						<GradientDonut
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-warning",
								"--vz-danger",
								"--vz-info",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col xl={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Patterned Donut Chart</h4>
					</CardHeader>
					<CardBody>
						<PatternedDonut
							dataColors={[
								"--vz-primary",
								"--vz-success",
								"--vz-warning",
								"--vz-danger",
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
						<h4 class="card-title mb-0">
							Pie Chart with Image Fill
						</h4>
					</CardHeader>

					<CardBody>
						<ImagePieChart
							dataColors={['#93C3EE', '#E5C6A0', '#669DB5', '#94A74A']
							}
						/>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
