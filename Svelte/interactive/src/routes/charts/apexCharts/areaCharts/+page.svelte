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
	import BasicAreaCharts from "./BasicAreaCharts.svelte";
	import SplineAreaChart from "./SplineAreaChart.svelte";
	import AxisChart from "./AxisChart.svelte";
	import NegativeAreaChart from "./NegativeAreaChart.svelte";
	import GithubStyleCharts from "./GithubStyleCharts.svelte";
	import GithubStyleCharts1 from "./GithubStyleCharts1.svelte";
	import StackedAreaChart from "./StackedAreaChart.svelte";
	import IrregularAreaCharts from "./IrregularAreaCharts.svelte";
	import AreaNullValueChart from "./AreaNullValueChart.svelte";
	import Link from "svelte-link";

	import avatar2 from "../../../../assets/images/users/avatar-2.jpg";
</script>

<svelte:head>
	<title>Apex Area Charts | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Area Charts" pageTitle="Apexcharts" />
		<Row>
			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Basic Area Chart</h4>
					</CardHeader>
					<CardBody>
						<BasicAreaCharts dataColors={["--vz-info"]} />
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Spline Area Chart</h4>
					</CardHeader>
					<CardBody>
						<SplineAreaChart
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
						<h4 class="card-title mb-0">
							Area Chart - Datetime X - Axis Chart
						</h4>
					</CardHeader>
					<CardBody>
						<div>
							<div
								class="toolbar d-flex align-items-start justify-content-center flex-wrap gap-2"
							>
								<button
									type="button"
									class="btn btn-soft-info timeline-btn btn-sm"
									id="one_month"
								>
									1M
								</button>
								<button
									type="button"
									class="btn btn-soft-info timeline-btn btn-sm"
									id="six_months"
								>
									6M
								</button>
								<button
									type="button"
									class="btn btn-soft-info timeline-btn btn-sm active"
									id="one_year"
								>
									1Y
								</button>
								<button
									type="button"
									class="btn btn-soft-primary timeline-btn btn-sm"
									id="all"
								>
									ALL
								</button>
							</div>
							<AxisChart dataColors={["--vz-info"]} />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Area with Negative Values Chart
						</h4>
					</CardHeader>
					<CardBody>
						<NegativeAreaChart
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
						<h4 class="card-title mb-0">
							Area Chart - Github Style
						</h4>
					</CardHeader>
					<CardBody>
						<div>
							<div class="bg-light">
								<GithubStyleCharts dataColors={["--vz-info"]} />
							</div>

							<div
								class="github-style d-flex align-items-center my-2"
							>
								<div class="flex-shrink-0 me-2">
									<img
										class="avatar-sm rounded"
										src={avatar2}
										data-hovercard-user-id="634573"
										alt=""
									/>
								</div>
								<div class="flex-grow-1">
									<Link
										href={null}
										class="font-size-14 text-dark fw-medium"
										>coder</Link
									>
									<div class="cmeta text-muted font-size-11">
										<span
											class="commits text-dark fw-medium"
										/> commits
									</div>
								</div>
							</div>

							<div class="bg-light">
								<GithubStyleCharts1
									dataColors={["--vz-primary"]}
								/>
							</div>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Stacked Area Chart</h4>
					</CardHeader>
					<CardBody>
						<StackedAreaChart
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
						<h4 class="card-title mb-0">
							Irregular Timeseries Chart
						</h4>
					</CardHeader>
					<CardBody>
						<IrregularAreaCharts
							dataColors={[
								"--vz-primary",
								"--vz-info",
								"--vz-gray-300",
							]}
						/>
					</CardBody>
				</Card>
			</Col>

			<Col lg={6}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">
							Area Chart With Null Values Chart
						</h4>
					</CardHeader>
					<CardBody>
						<AreaNullValueChart dataColors={["--vz-primary"]} />
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
