<script>
	import { Card, CardBody, CardHeader, Col, Label, Row } from "sveltestrap";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Select from "svelte-select";

	const SingleOptions = [
		{ value: "Choices 1", label: "Choices 1" },
		{ value: "Choices 2", label: "Choices 2" },
		{ value: "Choices 3", label: "Choices 3" },
		{ value: "Choices 4", label: "Choices 4" },
	];

	const GroupOptions = [
		{
			label: "UK",
			options: [
				{ label: "London", value: "London" },
				{ label: "Manchester", value: "Manchester" },
				{ label: "Liverpool", value: "Liverpool" },
			],
		},
		{
			label: "FR",
			options: [
				{ label: "Paris", value: "Paris" },
				{ label: "Lyon", value: "Lyon" },
				{ label: "Marseille", value: "Marseille" },
			],
		},
		{
			label: "DE",
			options: [
				{ label: "Hamburg", value: "Hamburg" },
				{ label: "Munich", value: "Munich" },
				{ label: "Berlin", value: "Berlin" },
			],
		},
		{
			label: "US",
			options: [
				{ label: "New York", value: "New York" },
				{ label: "Washington", value: "Washington" },
				{ label: "Michigan", value: "Michigan" },
			],
		},
		{
			label: "SP",
			options: [
				{ label: "Madrid", value: "Madrid" },
				{ label: "Barcelona", value: "Barcelona" },
				{ label: "Malaga", value: "Malaga" },
			],
		},
		{
			label: "CA",
			options: [
				{ label: "Montreal", value: "Montreal" },
				{ label: "Toronto", value: "Toronto" },
				{ label: "Vancouver", value: "Vancouver" },
			],
		},
	];

	const GroupOptions2 = [
		{ value: "Zero", label: "Zero" },
		{ value: "Two", label: "Two" },
		{ value: "Four", label: "Four" },
		{ value: "One", label: "One" },
		{ value: "Five", label: "Five" },
		{ value: "Three", label: "Three" },
		{ value: "Six", label: "Six" },
	];

	const noSortingGroup = [
		{ value: "Madrid", label: "Madrid" },
		{ value: "Toronto", label: "Toronto" },
		{ value: "Vancouver", label: "Vancouver" },
		{ value: "London", label: "London" },
		{ value: "Manchester", label: "Manchester" },
		{ value: "Liverpool", label: "Liverpool" },
		{ value: "Paris", label: "Paris" },
		{ value: "Malaga", label: "Malaga" },
		{ value: "Washington", label: "Washington" },
		{ value: "Lyon", label: "Lyon" },
		{ value: "Marseille", label: "Marseille" },
		{ value: "Hamburg", label: "Hamburg" },
		{ value: "Munich", label: "Munich" },
		{ value: "Barcelona", label: "Barcelona" },
		{ value: "Berlin", label: "Berlin" },
		{ value: "Montreal", label: "Montreal" },
		{ value: "New York", label: "New York" },
		{ value: "Michigan", label: "Michigan" },
	];

	const options = [
		{ label: "josh@joshuajohnson.co.uk", value: 1, disabled: true },
		{ label: "joe@bloggs.co.uk", value: 2, disabled: true },
	];

	const DefaultSelect = `<Row>
<Col lg={6}>
    <select class="form-select mb-3" aria-label="Default select example">
        <option selected>Select your Status </option>
        <option>Declined Payment</option>
        <option>Delivery Error</option>
        <option>Wrong Amount</option>
    </select>
</Col>
<Col lg={6}>
    <select class="form-select rounded-pill mb-3" aria-label="Default select example">
        <option selected>Search for services</option>
        <option>Information Architecture</option>
        <option>UI/UX Design</option>
        <option>Back End Development</option>
    </select>
</Col>
<Col lg={6}>
    <select class="form-select" aria-label="Disabled select example" disabled>
        <option selected>Open this select menu (Disabled)</option>
        <option>One</option>
        <option>Two</option>
        <option>Three</option>
    </select>
</Col>
</Row>
`;

	const MenuSize = `<Row>
    <Col lg={6}>
        <select class="form-select mb-3" aria-label="Default select example">
            <option selected>Select your Status </option>
            <option>Declined Payment</option>
            <option>Delivery Error</option>
            <option>Wrong Amount</option>
        </select>
    </Col>
    <Col lg={6}>
        <select class="form-select rounded-pill mb-3" aria-label="Default select example">
            <option selected>Search for services</option>
            <option>Information Architecture</option>
            <option>UI/UX Design</option>
            <option>Back End Development</option>
        </select>
    </Col>
    <Col lg={6}>
        <select class="form-select" aria-label="Disabled select example" disabled>
            <option selected>Open this select menu (Disabled)</option>
            <option>One</option>
            <option>Two</option>
            <option>Three</option>
        </select>
    </Col>
    </Row>
    `;

	const SelectSize = `<Row>
    <Col lg={6}>
        <select class="form-select mb-3" aria-label="Default select example">
            <option selected>Select your Status </option>
            <option>Declined Payment</option>
            <option>Delivery Error</option>
            <option>Wrong Amount</option>
        </select>
    </Col>
    <Col lg={6}>
        <select class="form-select rounded-pill mb-3" aria-label="Default select example">
            <option selected>Search for services</option>
            <option>Information Architecture</option>
            <option>UI/UX Design</option>
            <option>Back End Development</option>
        </select>
    </Col>
    <Col lg={6}>
        <select class="form-select" aria-label="Disabled select example" disabled>
            <option selected>Open this select menu (Disabled)</option>
            <option>One</option>
            <option>Two</option>
            <option>Three</option>
        </select>
    </Col>
    </Row>
    `;
</script>

<svelte:head>
	<title>Form Select | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<div class="container-fluid">
		<BreadCrumb title="Form Select" pageTitle="Forms" />
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Default Select" />
					<CardBody>
						<div class="live-preview">
							<Row>
								<Col lg={6}>
									<select
										class="form-select mb-3"
										aria-label="Default select example"
									>
										<option selected
											>Select your Status
										</option>
										<option value="1"
											>Declined Payment</option
										>
										<option value="2">Delivery Error</option
										>
										<option value="3">Wrong Amount</option>
									</select>
								</Col>
								<Col lg={6}>
									<select
										class="form-select rounded-pill mb-3"
										aria-label="Default select example"
									>
										<option selected
											>Search for services</option
										>
										<option value="1"
											>Information Architecture</option
										>
										<option value="2">UI/UX Design</option>
										<option value="3"
											>Back End Development</option
										>
									</select>
								</Col>
								<Col lg={6}>
									<select
										class="form-select"
										aria-label="Disabled select example"
										disabled
									>
										<option selected
											>Open this select menu (Disabled)</option
										>
										<option value="1">One</option>
										<option value="2">Two</option>
										<option value="3">Three</option>
									</select>
								</Col>
							</Row>
						</div>

						<div class="d-none code-view">
							<PrismCode code={DefaultSelect} id="defaultSelect" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Menu Size" />
					<CardBody>
						<div class="live-preview">
							<Row class="gy-4">
								<Col lg={6}>
									<select
										class="form-select"
										multiple
										aria-label="multiple select example"
									>
										<option selected
											>Open this select menu (multiple
											select option)</option
										>
										<option>One</option>
										<option>Two</option>
										<option>Three</option>
									</select>
								</Col>
								<Col lg={6}>
									<select
										class="form-select"
										size="3"
										aria-label="size 3 select example"
									>
										<option selected
											>Open this select menu (select menu
											size)</option
										>
										<option>One</option>
										<option>Two</option>
										<option>Three</option>
										<option>Four</option>
										<option>Five</option>
									</select>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={MenuSize} id="formmenuSize" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Select Size" />
					<CardBody>
						<p class="text-muted">
							Use <code>form-select-sm</code> class to set small
							select size and
							<code>form-select-lg</code> class to form-select class
							to set large select size. No such class is required for
							default select size.
						</p>
						<div class="live-preview">
							<Row class="align-items-center g-3">
								<Col lg={4}>
									<select
										class="form-select form-select-sm"
										aria-label=".form-select-sm example"
									>
										<option selected
											>Open this select menu</option
										>
										<option value="1">One</option>
										<option value="2">Two</option>
										<option value="3">Three</option>
									</select>
								</Col>
								<Col lg={4}>
									<select
										class="form-select"
										aria-label=".form-select-sm example"
									>
										<option selected
											>Open this select menu</option
										>
										<option>One</option>
										<option>Two</option>
										<option>Three</option>
									</select>
								</Col>
								<Col lg={4}>
									<select
										class="form-select form-select-lg"
										aria-label=".form-select-lg example"
									>
										<option selected
											>Open this select menu</option
										>
										<option>One</option>
										<option>Two</option>
										<option>Three</option>
									</select>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={SelectSize} id="formselectSize" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<CardHeader
						><h4 class="card-title mb-0">Choices</h4></CardHeader>
					<CardBody>
						<div>
							<div>
								<Row>
									<Col lg={4} md={6}>
										<div class="mb-3">
											<Label
												for="choices-single-default"
												class="form-label text-muted"
												>Default</Label
											>
											<div class="select-single">
												<Select items={SingleOptions} />
											</div>
										</div>
									</Col>

									<Col lg={4} md={6}>
										<div class="mb-3">
											<Label
												for="choices-single-groups"
												class="form-label text-muted"
												>Option Groups</Label
											>
											<div class="select-single">
												<Select items={GroupOptions} />
											</div>
										</div>
									</Col>

									<Col lg={4} md={6}>
										<div class="mb-3">
											<Label
												for="choices-single-no-search"
												class="form-label text-muted"
												>Options added via config with
												no search</Label
											>
											<div class="select-single">
												<Select
													isClearable={true}
													items={GroupOptions2}
												/>
											</div>
										</div>
									</Col>

									<Col lg={4} md={6}>
										<div class="mb-3">
											<Label
												for="choices-single-no-sorting"
												class="form-label text-muted"
												>Options added via config with
												no sorting</Label
											>
											<div class="select-single">
												<Select
													items={noSortingGroup}
												/>
											</div>
										</div>
									</Col>
								</Row>
							</div>

							<div class="mt-4">
								<h5 class="fs-14 mb-3">
									Multiple select input
								</h5>
								<Row>
									<Col lg={4} md={6}>
										<div class="mb-3">
											<Label
												for="choices-multiple-default"
												class="form-label text-muted"
												>Default</Label
											>
											<Select
												isMulti={true}
												multiple={true}
												items={SingleOptions}
											/>
										</div>
									</Col>

									<Col lg={4} md={6}>
										<div class="mb-3">
											<Label
												for="choices-multiple-remove-button"
												class="form-label text-muted"
												>With remove button</Label
											>
											<Select
												isMulti={true}
												isClearable={true}
												items={SingleOptions}
											/>
										</div>
									</Col>

									<Col lg={4} md={6}>
										<div class="mb-3">
											<Label
												for="choices-multiple-groups"
												class="form-label text-muted"
												>Option groups</Label
											>
											<Select
												isMulti={true}
												items={GroupOptions}
												closeMenuOnSelect={false}
											/>
										</div>
									</Col>
								</Row>
							</div>

							<div class="mt-4">
								<div>
									<Label
										for="choices-text-disabled"
										class="form-label text-muted"
										>Disabled</Label
									>
									<Select
										id={"dropdown"}
										disabled={true}
										items={options}
										isOptionDisabled={(option) =>
											option.disabled}
									/>
								</div>
							</div>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</div>
</div>
