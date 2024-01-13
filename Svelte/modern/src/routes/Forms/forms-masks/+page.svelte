<svelte:head>
  <title>Input Mask | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
	import { cleave } from 'svelte-cleavejs';
	import { Card, CardBody, CardHeader, Col, Container, Row, Label } from 'sveltestrap';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
</script>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Input Masks" pageTitle="Forms" />
		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader>
						<h4 class="card-title mb-0">Examples</h4>
					</CardHeader>

					<CardBody>
						<form action="#">
							<div>
								<h5 class="fs-14 mb-3 text-muted">Date Formatting</h5>
								<Row>
									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-date" class="form-label">Date</Label>
											<input
												placeholder="DD-MM-YYYY"
												use:cleave={{
													date: true,
													delimiter: '-',
													datePattern: ['d', 'm', 'Y']
												}}
												class="form-control"
											/>
										</div>
									</Col>

									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-date-format" class="form-label">Date Formatting</Label>
											<input
												placeholder="MM/YY"
												use:cleave={{
													date: true,
													datePattern: ['m', 'y']
												}}
												class="form-control"
											/>
										</div>
									</Col>
								</Row>
							</div>

							<div class="border mt-3 border-dashed" />

							<div class="mt-4">
								<h6 class="mb-3 fs-14 text-muted">Time Formatting</h6>
								<Row>
									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-time" class="form-label">Time</Label>
											<input
												placeholder="hh:mm:ss"
												use:cleave={{
													time: true,
													timePattern: ['h', 'm', 's']
												}}
												class="form-control"
											/>
										</div>
									</Col>

									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-time-format" class="form-label">Time Formatting</Label>
											<input
												placeholder="hh:mm"
												use:cleave={{
													time: true,
													timePattern: ['h', 'm']
												}}
												class="form-control"
											/>
										</div>
									</Col>
								</Row>
							</div>

							<div class="border mt-3 border-dashed" />

							<div class="mt-4">
								<h5 class="fs-14 mb-3 text-muted">Custom Options</h5>
								<Row>
									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-ccard" class="form-label">Credit Card</Label>
											<input
												placeholder="xxxx xxxx xxxx xxxx"
												use:cleave={{
													creditCard: true
												}}
												class="form-control"
											/>
										</div>
									</Col>

									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-delimiter" class="form-label">Delimiter</Label>
											<input
												placeholder="xxx·xxx·xxx"
												use:cleave={{
													delimiter: '·',
													blocks: [3, 3, 3],
													uppercase: true
												}}
												class="form-control"
											/>
										</div>
									</Col>
								</Row>

								<Row>
									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-delimiters" class="form-label">Delimiters</Label>
											<input
												placeholder="xxx.xxx.xxx-xx"
												use:cleave={{
													delimiters: ['.', '.', '-'],
													blocks: [3, 3, 3, 2],
													uppercase: true
												}}
												class="form-control"
											/>
										</div>
									</Col>

									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-prefix" class="form-label">Prefix</Label>
											<input
												use:cleave={{
													prefix: 'PREFIX',
													delimiter: '-',
													blocks: [6, 4, 4, 4],
													uppercase: true
												}}
												class="form-control"
											/>
										</div>
									</Col>
								</Row>
								<Row>
									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-Phone" class="form-label">Phone</Label>
											<input
												placeholder="(xxx)xxx-xxxx"
												use:cleave={{
													delimiters: ['(', ')', '-'],
        											blocks: [0, 3, 3, 4],
												}}
												class="form-control"
											/>
										</div>
									</Col>

									<Col xl={6}>
										<div class="mb-3">
											<Label for="cleave-numeral" class="form-label">Numeral Formatting</Label>
											<input
											placeholder="Enter numeral"
												use:cleave={{
													numeral: true,
    												numeralThousandsGroupStyle: 'thousand'
												}}
												class="form-control"
											/>
										</div>
									</Col>
								</Row>

								
							</div>
						</form>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
	<!-- container-fluid -->
</div>
