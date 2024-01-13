<script>
	import {
		Card,
		CardBody,
		Col,
		Container,
		Form,
		Input,
		InputGroup,
		Label,
		Row,
	} from "sveltestrap";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";
	import Flatpickr from "svelte-flatpickr";

	//FormGrid code
	const FormGrid = `<Col md={6}>
<div class="mb-3">
    <Label for="firstNameinput" class="form-label">First Name</Label>
    <Input type="text" class="form-control" placeholder="Enter your firstname" id="firstNameinput"/>
</div>
</Col>
<Col md={6}>
    <div class="mb-3">
        <Label for="lastNameinput" class="form-label">Last Name</Label>
        <Input type="text" class="form-control" placeholder="Enter your lastname" id="lastNameinput"/>
    </div>
</Col>
<Col md={12}>
    <div class="mb-3">
        <Label for="compnayNameinput" class="form-label">Company Name</Label>
        <Input type="text" class="form-control" placeholder="Enter company name" id="compnayNameinput"/>
    </div>
</Col>
<Col md={6}>
    <div class="mb-3">
        <Label for="phonenumberInput" class="form-label">Phone Number</Label>
        <Input type="tel" class="form-control" placeholder="+(245) 451 45123" id="phonenumberInput"/>
    </div>
</Col>
<Col md={6}>
    <div class="mb-3">
        <Label for="emailidInput" class="form-label">Email Address</Label>
        <Input type="email" class="form-control" placeholder="example@gamil.com" id="emailidInput"/>
    </div>
</Col>
<Col md={12}>
    <div class="mb-3">
        <Label for="address1ControlTextarea" class="form-label">Address</Label>
        <Input type="text" class="form-control" placeholder="Address 1" id="address1ControlTextarea"/>
    </div>
</Col>
<Col md={6}>
    <div class="mb-3">
        <Label for="citynameInput" class="form-label">City</Label>
        <Input type="email" class="form-control" placeholder="Enter your city" id="citynameInput"/>
    </div>
</Col>
<Col md={6}>
    <div class="mb-3">
        <Label for="ForminputState" class="form-label">State</Label>
        <select id="ForminputState" class="form-select" data-choices data-choices-sorting="true" >
            <option>Choose...</option>
            <option>...</option>
        </select>
    </div>
</Col>
<Col md={12}>
    <div class="text-end">
        <button type="submit" class="btn btn-primary">Submit</button>
    </div>
</Col>
`;

	const Gutters = `
<Col md={12}>
<Label for="fullnameInput" class="form-label">Name</Label>
<Input type="text" class="form-control" id="fullnameInput" placeholder="Enter your name"/>
</Col>
<Col md={6}>
    <Label for="inputEmail4" class="form-label">Email</Label>
    <Input type="email" class="form-control" id="inputEmail4" placeholder="Email"/>
</Col>
<Col md={6}>
    <Label for="inputPassword4" class="form-label">Password</Label>
    <Input type="password" class="form-control" id="inputPassword4" placeholder="Password"/>
</Col>
<Col xs={12}>
    <Label for="inputAddress" class="form-label">Address</Label>
    <Input type="text" class="form-control" id="inputAddress" placeholder="1234 Main St"/>
</Col>
<Col xs={12}>
    <Label for="inputAddress2" class="form-label">Address 2</Label>
    <Input type="text" class="form-control" id="inputAddress2" placeholder="Apartment, studio, or floor"/>
</Col>
<Col md={6}>
    <Label for="inputCity" class="form-label">City</Label>
    <Input type="text" class="form-control" id="inputCity" placeholder="Enter your city"/>
</Col>
<Col md={4}>
    <Label for="inputState" class="form-label">State</Label>
    <select id="inputState" class="form-select" data-choices data-choices-sorting="true">
        <option selected>Choose...</option>
        <option>...</option>
    </select>
</Col>
<Col md={2}>
    <Label for="inputZip" class="form-label">Zip</Label>
    <Input type="text" class="form-control" id="inputZip" placeholder="Zin code"/>
</Col>
<Col xs={12}>
    <div class="form-check">
        <Input class="form-check-input" type="checkbox" id="gridCheck"/>
        <Label class="form-check-label" for="gridCheck">
            Check me out
        </Label>
    </div>
</Col>
<Col xs={12}>
    <div class="text-end">
        <button type="submit" class="btn btn-primary">Sign in</button>
    </div>
</Col>
`;

	const VerticalForm = `
<div class="mb-3">
<Label for="employeeName" class="form-label">Employee Name</Label>
    <Input type="text" class="form-control" id="employeeName" placeholder="Enter emploree name"/>
</div>
<div class="mb-3">
    <Label for="employeeUrl" class="form-label">Employee Department URL</Label>
    <Input type="url" class="form-control" id="employeeUrl" placeholder="Enter emploree url"/>
</div>
<div class="mb-3">
    <Label for="StartleaveDate" class="form-label">Start Leave Date</Label>
    <Flatpickr
        class="form-control"
        options={{
        dateFormat: "d M, Y"
        }}
    />
</div>
<div class="mb-3">
    <Label for="EndleaveDate" class="form-label">End Leave Date</Label>
    <Flatpickr
        class="form-control"
        options={{
        dateFormat: "d M, Y"
        }}
    />
</div>
<div class="mb-3">
    <Label for="VertimeassageInput" class="form-label">Message</Label>
    <textarea class="form-control" id="VertimeassageInput" rows="3" placeholder="Enter your message"></textarea>
</div>
<div class="text-end">
    <button type="submit" class="btn btn-primary">Add Leave</button>
</div>
`;

	const HorizontalForm = `<Row class="mb-3">
<Col lg={3} >
    <Label for="nameInput" class="form-label">Name</Label>
</Col>
<Col lg={9} >
    <Input type="text" class="form-control" id="nameInput" placeholder="Enter your name"/>
</Col>
</Row>
<Row class="mb-3">
<Col lg={3} >
    <Label for="websiteUrl" class="form-label">Website URL</Label>
</Col>
<Col lg={9} >
    <Input type="url" class="form-control" id="websiteUrl" placeholder="Enter your url"/>
</Col>
</Row>
<Row class="mb-3">
<Col lg={3} >
    <Label for="dateInput" class="form-label">Date</Label>
</Col>
<Col lg={9} >
    <Flatpickr
        class="form-control"
        options={{
        dateFormat: "d M, Y"
        }}
    />
</Col>
</Row>
<Row class="mb-3">
<Col lg={3} >
    <Label for="timeInput" class="form-label">Time</Label>
</Col>
<Col lg={9} >
<Flatpickr
    class="form-control"
    options={{
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
    }}
/>
</Col>
</Row>
<Row class="mb-3">
<Col lg={3} >
    <Label for="leaveemails" class="form-label">Email Id</Label>
</Col>
<Col lg={9} >
    <Input type="email" class="form-control" id="leaveemails" placeholder="Enter your email"/>
</Col>
</Row>
<Row class="mb-3">
<Col lg={3} >
    <Label for="contactNumber" class="form-label">Contact Number</Label>
</Col>
<Col lg={9} >
    <Input type="number" class="form-control" id="contactNumber" placeholder="+91 9876543210"/>
</Col>
</Row>
<Row class="mb-3">
<Col lg={3} >
    <Label for="meassageInput" class="form-label">Message</Label>
</Col>
<Col lg={9} >
    <textarea class="form-control" id="meassageInput" rows="3" placeholder="Enter your message"></textarea>
</Col>
</Row>
<div class="text-end">
<button type="submit" class="btn btn-primary">Add Leave</button>
</div>
`;

	const HorizontalFormLabelSizing = `<Col xxl={4}>
<Row>
    <Label for="colFormLabelSm" class="col-sm-2 col-form-label col-form-label-sm">Email</Label>
    <div class="col-sm-10">
        <Input type="email" class="form-control form-control-sm" id="colFormLabelSm" placeholder="col-form-label-sm"/>
    </div>
</Row>
</Col>
<Col xxl={4}>
<Row>
    <Label for="colFormLabel" class="col-sm-2 col-form-label">Email</Label>
    <div class="col-sm-10">
        <Input type="email" class="form-control" id="colFormLabel" placeholder="col-form-label"/>
    </div>
</Row>
</Col>
<Col xxl={4}>
<Row>
    <Label for="colFormLabelLg" class="col-sm-2 col-form-label col-form-label-lg">Email</Label>
    <div class="col-sm-10">
        <Input type="email" class="form-control form-control-lg" id="colFormLabelLg" placeholder="col-form-label-lg"/>
    </div>
</Row>
</Col>
`;

	const ColumnSizing = `<Col sm={6}>
<Input type="text" class="form-control" placeholder="Firstname" aria-label="First-Name"/>
</Col>
<Col sm={6}>
    <Input type="text" class="form-control" placeholder="Lastname" aria-label="Last-Name"/>
</Col>
<Col sm={4}>
    <Input type="text" class="form-control" placeholder="Email id" aria-label="Email Id"/>
</Col>
<Col sm={4}>
    <Input type="password" class="form-control" placeholder="Password" aria-label="Password"/>
</Col>
<Col sm={4}>
    <Input type="password" class="form-control" placeholder="Confirm Password" aria-label="confirm-password"/>
</Col>
<Col sm={7}>
    <Input type="text" class="form-control" placeholder="City" aria-label="City"/>
</Col>
<Col sm>
    <Input type="text" class="form-control" placeholder="State" aria-label="State"/>
</Col>
<Col sm>
    <Input type="text" class="form-control" placeholder="Zip" aria-label="Zip"/>
</Col>
    `;

	const AutoSizing = `<Form action="#">
<Row class="gy-2 gx-3 mb-3 align-items-center">
    <Col sm>
        <Label class="visually-hidden" for="autoSizingInput">Name</Label>
        <Input type="text" class="form-control" id="autoSizingInput" placeholder="Jane Doe"/>
    </Col>
    <Col sm>
        <Label class="visually-hidden" for="autoSizingInputGroup">Username</Label>
        <div class="input-group">
            <div class="input-group-text">@</div>
            <Input type="text" class="form-control" id="autoSizingInputGroup" placeholder="Username"/>
        </div>
    </Col>
    <Col sm>
        <Label class="visually-hidden" for="autoSizingSelect">Preference</Label>
        <select class="form-select" data-choices data-choices-sorting="true" id="autoSizingSelect">
            <option >Choose...</option>
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
        </select>
    </Col>
    <Col class="sm-auto">
        <div class="form-check">
            <Input class="form-check-input" type="checkbox" id="autoSizingCheck"/>
            <Label class="form-check-label" for="autoSizingCheck">
                Remember me
            </Label>
        </div>
    </Col>
    <Col class="sm-auto">
        <button type="submit" class="btn btn-primary">Submit</button>
    </Col>
</Row>
</Form>

<Form>
<Row class="gx-3 gy-2 align-items-center">
    <Col sm={3}>
        <Label class="visually-hidden" for="specificSizeInputName">Name</Label>
        <Input type="text" class="form-control" id="specificSizeInputName" placeholder="Jane Doe"/>
    </Col>
    <Col sm={3}>
        <Label class="visually-hidden" for="specificSizeInputGroupUsername">Username</Label>
        <InputGroup>
            <div class="input-group-text">@</div>
            <Input type="text" class="form-control" id="specificSizeInputGroupUsername" placeholder="Username"/>
        </InputGroup>
    </Col>
    <Col sm={3}>
        <Label class="visually-hidden" for="specificSizeSelect">Preference</Label>
        <select class="form-select" data-choices data-choices-sorting="true" id="specificSizeSelect">
            <option >Choose...</option>
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
        </select>
    </Col>
    <div class="col-auto">
        <div class="form-check">
            <Input class="form-check-input" type="checkbox" id="autoSizingCheck2"/>
            <Label class="form-check-label" for="autoSizingCheck2">
                Remember me
            </Label>
        </div>
    </div>
    <Col >
        <button type="submit" class="btn btn-primary">Submit</button>
    </Col>
</Row>
</Form>
`;

	const InlineForms = `<Row class="row-cols-lg-auto g-3 align-items-center">
<Col xs={12}>
    <Label class="visually-hidden" for="inlineFormInputGroupUsername">Username</Label>
    <div class="input-group">
        <div class="input-group-text">@</div>
        <Input type="text" class="form-control" id="inlineFormInputGroupUsername" placeholder="Username" />
    </div>
</Col>
<Col xs={12}>
    <Label class="visually-hidden" for="inlineFormSelectPref">Preference</Label>
    <select class="form-select" data-choices data-choices-sorting="true" id="inlineFormSelectPref">
        <option >Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
    </select>
</Col>
<Col xs={12}>
    <div class="form-check">
        <Input class="form-check-input" type="checkbox" id="inlineFormCheck" />
        <Label class="form-check-label" for="inlineFormCheck">
            Remember me
        </Label>
    </div>
</Col>
<Col xs={12}>
    <button type="submit" class="btn btn-primary">Submit</button>
</Col>
</Row>
`;

	const FloatingLabels = `<Form action="#">
<Row class="g-3">
    <Col lg={6}>
        <div class="form-floating">
            <Input type="text" class="form-control" id="firstnamefloatingInput" placeholder="Enter your firstname"/>
            <Label for="firstnamefloatingInput">First Name</Label>
        </div>
    </Col>
    <Col lg={6}>
        <div class="form-floating">
            <Input type="text" class="form-control" id="lastnamefloatingInput" placeholder="Enter your Lastname"/>
            <Label for="lastnamefloatingInput">Last Name</Label>
        </div>
    </Col>
    <Col lg={4}>
        <div class="form-floating">
            <Input type="email" class="form-control" id="emailfloatingInput" placeholder="Enter your email"/>
            <Label for="emailfloatingInput">Email Address</Label>
        </div>
    </Col>
    <Col lg={4}>
        <div class="form-floating">
            <Input type="password" class="form-control" id="passwordfloatingInput" placeholder="Enter your password"/>
            <Label for="passwordfloatingInput">Password</Label>
        </div>
    </Col>
    <Col lg={4}>
        <div class="form-floating">
            <Input type="password" class="form-control" id="passwordfloatingInput1" placeholder="Confirm password"/>
            <Label for="passwordfloatingInput1">Confirm Password</Label>
        </div>
    </Col>
    <Col lg={4}>
        <div class="form-floating">
            <Input type="text" class="form-control" id="cityfloatingInput" placeholder="Enter your city"/>
            <Label for="cityfloatingInput">City</Label>
        </div>
    </Col>
    <Col lg={4}>
        <div class="form-floating">
            <select class="form-select" id="floatingSelect" aria-label="Floating label select example">
              <option >Choose...</option>
              <option value="1">USA</option>
              <option value="2">Brazil</option>
              <option value="3">France</option>
              <option value="4">Germany</option>
            </select>
            <Label for="floatingSelect">Country</Label>
        </div>
    </Col>
    <Col lg={4}>
        <div class="form-floating">
            <Input type="number" class="form-control" id="zipfloatingInput" placeholder="Enter your zipcode"/>
            <Label for="zipfloatingInput">Zipcode</Label>
        </div>
    </Col>
    <Col lg={12}>
        <div class="text-end">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </Col>
</Row>
</Form>
`;
</script>

<svelte:head>
	<title>Form Layout | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Form Layout" pageTitle="Forms" />
		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Form Grid" />
					<CardBody>
						<p class="text-muted">
							More complex forms can be built using our grid
							classes. Use these for form layouts that require
							multiple columns, varied widths, and additional
							alignment options. <span class="fw-medium"
								>Requires the <code>$enable-grid-classes</code> Sass
								variable to be enabled</span> (on by default).
						</p>
						<div class="live-preview">
							<Form>
								<Row>
									<Col md={6}>
										<div class="mb-3">
											<Label
												for="firstNameinput"
												class="form-label"
												>First Name</Label
											>
											<Input
												type="text"
												class="form-control"
												placeholder="Enter your firstname"
												id="firstNameinput"
											/>
										</div>
									</Col>
									<Col md={6}>
										<div class="mb-3">
											<Label
												for="lastNameinput"
												class="form-label"
												>Last Name</Label
											>
											<Input
												type="text"
												class="form-control"
												placeholder="Enter your lastname"
												id="lastNameinput"
											/>
										</div>
									</Col>
									<Col md={12}>
										<div class="mb-3">
											<Label
												for="compnayNameinput"
												class="form-label"
												>Company Name</Label
											>
											<Input
												type="text"
												class="form-control"
												placeholder="Enter company name"
												id="compnayNameinput"
											/>
										</div>
									</Col>
									<Col md={6}>
										<div class="mb-3">
											<Label
												for="phonenumberInput"
												class="form-label"
												>Phone Number</Label
											>
											<Input
												type="tel"
												class="form-control"
												placeholder="+(245) 451 45123"
												id="phonenumberInput"
											/>
										</div>
									</Col>
									<Col md={6}>
										<div class="mb-3">
											<Label
												for="emailidInput"
												class="form-label"
												>Email Address</Label
											>
											<Input
												type="email"
												class="form-control"
												placeholder="example@gamil.com"
												id="emailidInput"
											/>
										</div>
									</Col>
									<Col md={12}>
										<div class="mb-3">
											<Label
												for="address1ControlTextarea"
												class="form-label"
												>Address</Label
											>
											<Input
												type="text"
												class="form-control"
												placeholder="Address 1"
												id="address1ControlTextarea"
											/>
										</div>
									</Col>
									<Col md={6}>
										<div class="mb-3">
											<Label
												for="citynameInput"
												class="form-label">City</Label
											>
											<Input
												type="email"
												class="form-control"
												placeholder="Enter your city"
												id="citynameInput"
											/>
										</div>
									</Col>
									<Col md={6}>
										<div class="mb-3">
											<Label
												for="ForminputState"
												class="form-label">State</Label
											>
											<select
												id="ForminputState"
												class="form-select"
												data-choices
												data-choices-sorting="true"
											>
												<option>Choose...</option>
												<option>...</option>
											</select>
										</div>
									</Col>
									<Col md={12}>
										<div class="text-end">
											<button
												type="submit"
												class="btn btn-primary"
												>Submit</button
											>
										</div>
									</Col>
								</Row>
							</Form>
						</div>
						<div class="d-none code-view">
							<PrismCode code={FormGrid} id="FormGridcode" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Gutters" />
					<div class="card-body">
						<p class="text-muted">
							By adding <Link
								href="/docs/5.1/layout/gutters/"
								class="text-decoration-underline"
								>gutter modifier classes</Link>, you can have control over the gutter width in as
							well the inline as block direction.
							<span class="fw-medium"
								>Also requires the <code
									>$enable-grid-classes</code
								> Sass variable to be enabled</span> (on by default).
						</p>
						<div class="live-preview">
							<form action="#" class="row g-3">
								<Col md={12}>
									<Label
										for="fullnameInput"
										class="form-label">Name</Label
									>
									<Input
										type="text"
										class="form-control"
										id="fullnameInput"
										placeholder="Enter your name"
									/>
								</Col>
								<Col md={6}>
									<Label for="inputEmail4" class="form-label"
										>Email</Label
									>
									<Input
										type="email"
										class="form-control"
										id="inputEmail4"
										placeholder="Email"
									/>
								</Col>
								<Col md={6}>
									<Label
										for="inputPassword4"
										class="form-label">Password</Label
									>
									<Input
										type="password"
										class="form-control"
										id="inputPassword4"
										placeholder="Password"
									/>
								</Col>
								<Col xs={12}>
									<Label for="inputAddress" class="form-label"
										>Address</Label
									>
									<Input
										type="text"
										class="form-control"
										id="inputAddress"
										placeholder="1234 Main St"
									/>
								</Col>
								<Col xs={12}>
									<Label
										for="inputAddress2"
										class="form-label">Address 2</Label
									>
									<Input
										type="text"
										class="form-control"
										id="inputAddress2"
										placeholder="Apartment, studio, or floor"
									/>
								</Col>
								<Col md={6}>
									<Label for="inputCity" class="form-label"
										>City</Label
									>
									<Input
										type="text"
										class="form-control"
										id="inputCity"
										placeholder="Enter your city"
									/>
								</Col>
								<Col md={4}>
									<Label for="inputState" class="form-label"
										>State</Label
									>
									<select
										id="inputState"
										class="form-select"
										data-choices
										data-choices-sorting="true"
									>
										<option>Choose...</option>
										<option>...</option>
									</select>
								</Col>
								<Col md={2}>
									<Label for="inputZip" class="form-label"
										>Zip</Label
									>
									<Input
										type="text"
										class="form-control"
										id="inputZip"
										placeholder="Zin code"
									/>
								</Col>
								<Col xs={12}>
									<div class="form-check">
										<input
											class="form-check-input"
											type="checkbox"
											id="gridCheck"
										/>
										<Label
											class="form-check-label"
											for="gridCheck">Check me out</Label
										>
									</div>
								</Col>
								<Col xs={12}>
									<div class="text-end">
										<button
											type="submit"
											class="btn btn-primary"
											>Sign in</button
										>
									</div>
								</Col>
							</form>
						</div>
						<div class="d-none code-view">
							<PrismCode code={Gutters} id="formGutters" />
						</div>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Vertical Form" />
					<CardBody>
						<div class="live-preview">
							<Form action="#">
								<div class="mb-3">
									<Label for="employeeName" class="form-label"
										>Employee Name</Label
									>
									<Input
										type="text"
										class="form-control"
										id="employeeName"
										placeholder="Enter emploree name"
									/>
								</div>
								<div class="mb-3">
									<Label for="employeeUrl" class="form-label"
										>Employee Department URL</Label
									>
									<Input
										type="url"
										class="form-control"
										id="employeeUrl"
										placeholder="Enter emploree url"
									/>
								</div>
								<div class="mb-3">
									<Label
										for="StartleaveDate"
										class="form-label"
										>Start Leave Date</Label
									>
									<Flatpickr
										class="form-control"
										options={{
											dateFormat: "d M, Y",
										}}
									/>
								</div>
								<div class="mb-3">
									<Label for="EndleaveDate" class="form-label"
										>End Leave Date</Label
									>
									<Flatpickr
										class="form-control"
										options={{
											dateFormat: "d M, Y",
										}}
									/>
								</div>
								<div class="mb-3">
									<Label
										for="VertimeassageInput"
										class="form-label">Message</Label
									>
									<textarea
										class="form-control"
										id="VertimeassageInput"
										rows="3"
										placeholder="Enter your message"
									/>
								</div>
								<div class="text-end">
									<button
										type="submit"
										class="btn btn-primary"
										>Add Leave</button
									>
								</div>
							</Form>
						</div>
						<div class="d-none code-view">
							<PrismCode code={VerticalForm} id="verticalForm" />
						</div>
					</CardBody>
				</Card>
			</Col>
			<Col xxl={6}>
				<Card>
					<PreviewCardHeader title="Horizontal Form" />
					<CardBody>
						<div class="live-preview">
							<form action="#">
								<Row class="mb-3">
									<Col lg={3}>
										<Label
											for="nameInput"
											class="form-label">Name</Label
										>
									</Col>
									<Col lg={9}>
										<Input
											type="text"
											class="form-control"
											id="nameInput"
											placeholder="Enter your name"
										/>
									</Col>
								</Row>
								<Row class="mb-3">
									<Col lg={3}>
										<Label
											for="websiteUrl"
											class="form-label"
											>Website URL</Label
										>
									</Col>
									<Col lg={9}>
										<Input
											type="url"
											class="form-control"
											id="websiteUrl"
											placeholder="Enter your url"
										/>
									</Col>
								</Row>
								<Row class="mb-3">
									<Col lg={3}>
										<Label
											for="dateInput"
											class="form-label">Date</Label
										>
									</Col>
									<Col lg={9}>
										<Flatpickr
											class="form-control"
											options={{
												dateFormat: "d M, Y",
											}}
										/>
									</Col>
								</Row>
								<Row class="mb-3">
									<Col lg={3}>
										<Label
											for="timeInput"
											class="form-label">Time</Label
										>
									</Col>
									<Col lg={9}>
										<Flatpickr
											class="form-control"
											options={{
												enableTime: true,
												noCalendar: true,
												dateFormat: "H:i",
											}}
										/>
									</Col>
								</Row>
								<Row class="mb-3">
									<Col lg={3}>
										<Label
											for="leaveemails"
											class="form-label">Email Id</Label
										>
									</Col>
									<Col lg={9}>
										<Input
											type="email"
											class="form-control"
											id="leaveemails"
											placeholder="Enter your email"
										/>
									</Col>
								</Row>
								<Row class="mb-3">
									<Col lg={3}>
										<Label
											for="contactNumber"
											class="form-label"
											>Contact Number</Label
										>
									</Col>
									<Col lg={9}>
										<Input
											type="number"
											class="form-control"
											id="contactNumber"
											placeholder="+91 9876543210"
										/>
									</Col>
								</Row>
								<Row class="mb-3">
									<Col lg={3}>
										<Label
											for="meassageInput"
											class="form-label">Message</Label
										>
									</Col>
									<Col lg={9}>
										<textarea
											class="form-control"
											id="meassageInput"
											rows="3"
											placeholder="Enter your message"
										/>
									</Col>
								</Row>
								<div class="text-end">
									<button
										type="submit"
										class="btn btn-primary"
										>Add Leave</button
									>
								</div>
							</form>
						</div>
						<div class="d-none code-view">
							<PrismCode code={HorizontalForm} id="horizontalForm" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Horizontal Form Label Sizing" />
					<CardBody>
						<p class="text-muted">
							Use <code>col-form-label-sm</code> class to set
							small size form label or
							<code>col-form-label-lg</code> class to set large size
							form label to &lt;label&gt;. No such class is required
							for the default size form label.
						</p>
						<div class="live-preview">
							<Row class="align-items-center g-3">
								<Col xxl={4}>
									<Row>
										<Label
											for="colFormLabelSm"
											class="col-sm-2 col-form-label col-form-label-sm"
											>Email</Label
										>
										<Col sm={10}>
											<Input
												type="email"
												class="form-control form-control-sm"
												id="colFormLabelSm"
												placeholder="col-form-label-sm"
											/>
										</Col>
									</Row>
								</Col>
								<Col xxl={4}>
									<Row>
										<Label
											for="colFormLabel"
											class="col-sm-2 col-form-label"
											>Email</Label
										>
										<Col sm={10}>
											<Input
												type="email"
												class="form-control"
												id="colFormLabel"
												placeholder="col-form-label"
											/>
										</Col>
									</Row>
								</Col>
								<Col xxl={4}>
									<Row>
										<Label
											for="colFormLabelLg"
											class="col-sm-2 col-form-label col-form-label-lg"
											>Email</Label
										>
										<Col sm={10}>
											<Input
												type="email"
												class="form-control form-control-lg"
												id="colFormLabelLg"
												placeholder="col-form-label-lg"
											/>
										</Col>
									</Row>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={HorizontalFormLabelSizing} id="horizontalFormLabelSizing" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Column Sizing" />
					<div class="card-body">
						<p class="text-muted">
							Use <code>sm={`required size`}</code> size value to set
							column size as per your requirement.
						</p>
						<div class="live-preview">
							<Row class="g-3">
								<Col sm={6}>
									<Input
										type="text"
										class="form-control"
										placeholder="Firstname"
										aria-label="First-Name"
									/>
								</Col>
								<Col sm={6}>
									<Input
										type="text"
										class="form-control"
										placeholder="Lastname"
										aria-label="Last-Name"
									/>
								</Col>
								<Col sm={4}>
									<Input
										type="text"
										class="form-control"
										placeholder="Email id"
										aria-label="Email Id"
									/>
								</Col>
								<Col sm={4}>
									<Input
										type="password"
										class="form-control"
										placeholder="Password"
										aria-label="Password"
									/>
								</Col>
								<Col sm={4}>
									<Input
										type="password"
										class="form-control"
										placeholder="Confirm Password"
										aria-label="confirm-password"
									/>
								</Col>
								<Col sm={7}>
									<Input
										type="text"
										class="form-control"
										placeholder="City"
										aria-label="City"
									/>
								</Col>
								<Col sm>
									<Input
										type="text"
										class="form-control"
										placeholder="State"
										aria-label="State"
									/>
								</Col>
								<Col sm>
									<Input
										type="text"
										class="form-control"
										placeholder="Zip"
										aria-label="Zip"
									/>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={ColumnSizing} id="columnSizing" />
						</div>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Auto Sizing" />
					<CardBody>
						<div class="live-preview">
							<Form action="#">
								<Row class="gy-2 gx-3 mb-3 align-items-center">
									<Col sm>
										<Label
											class="visually-hidden"
											for="autoSizingInput">Name</Label
										>
										<Input
											type="text"
											class="form-control"
											id="autoSizingInput"
											placeholder="Jane Doe"
										/>
									</Col>
									<Col sm>
										<Label
											class="visually-hidden"
											for="autoSizingInputGroup"
											>Username</Label
										>
										<div class="input-group">
											<div class="input-group-text">
												@
											</div>
											<Input
												type="text"
												class="form-control"
												id="autoSizingInputGroup"
												placeholder="Username"
											/>
										</div>
									</Col>
									<Col sm>
										<Label
											class="visually-hidden"
											for="autoSizingSelect"
											>Preference</Label
										>
										<select
											class="form-select"
											data-choices
											data-choices-sorting="true"
											id="autoSizingSelect"
										>
											<option>Choose...</option>
											<option value="1">One</option>
											<option value="2">Two</option>
											<option value="3">Three</option>
										</select>
									</Col>
									<Col class="sm-auto">
										<div class="form-check">
											<input
												class="form-check-input"
												type="checkbox"
												id="autoSizingCheck"
											/>
											<Label
												class="form-check-label"
												for="autoSizingCheck"
												>Remember me</Label
											>
										</div>
									</Col>
									<Col class="sm-auto">
										<button
											type="submit"
											class="btn btn-primary"
											>Submit</button
										>
									</Col>
								</Row>
							</Form>

							<Form>
								<Row class="gx-3 gy-2 align-items-center">
									<Col sm={3}>
										<Label
											class="visually-hidden"
											for="specificSizeInputName"
											>Name</Label
										>
										<Input
											type="text"
											class="form-control"
											id="specificSizeInputName"
											placeholder="Jane Doe"
										/>
									</Col>
									<Col sm={3}>
										<Label
											class="visually-hidden"
											for="specificSizeInputGroupUsername"
											>Username</Label
										>
										<InputGroup>
											<div class="input-group-text">
												@
											</div>
											<Input
												type="text"
												class="form-control"
												id="specificSizeInputGroupUsername"
												placeholder="Username"
											/>
										</InputGroup>
									</Col>
									<Col sm={3}>
										<Label
											class="visually-hidden"
											for="specificSizeSelect"
											>Preference</Label
										>
										<select
											class="form-select"
											data-choices
											data-choices-sorting="true"
											id="specificSizeSelect"
										>
											<option>Choose...</option>
											<option value="1">One</option>
											<option value="2">Two</option>
											<option value="3">Three</option>
										</select>
									</Col>
									<div class="col-auto">
										<div class="form-check">
											<input
												class="form-check-input"
												type="checkbox"
												id="autoSizingCheck2"
											/>
											<Label
												class="form-check-label"
												for="autoSizingCheck2"
												>Remember me</Label
											>
										</div>
									</div>
									<Col>
										<button
											type="submit"
											class="btn btn-primary"
											>Submit</button
										>
									</Col>
								</Row>
							</Form>
						</div>
						<div class="d-none code-view">
							<PrismCode code={AutoSizing} id="autoSizing" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Inline Forms" />
					<CardBody>
						<p class="text-muted">
							Use <code>row-cols-*</code> class to set form inline.
						</p>
						<div class="live-preview">
							<Form action="#">
								<Row
									class="row-cols-lg-auto g-3 align-items-center"
								>
									<Col xs={12}>
										<Label
											class="visually-hidden"
											for="inlineFormInputGroupUsername"
											>Username</Label
										>
										<div class="input-group">
											<div class="input-group-text">
												@
											</div>
											<Input
												type="text"
												class="form-control"
												id="inlineFormInputGroupUsername"
												placeholder="Username"
											/>
										</div>
									</Col>
									<Col xs={12}>
										<Label
											class="visually-hidden"
											for="inlineFormSelectPref"
											>Preference</Label
										>
										<select
											class="form-select"
											data-choices
											data-choices-sorting="true"
											id="inlineFormSelectPref"
										>
											<option>Choose...</option>
											<option value="1">One</option>
											<option value="2">Two</option>
											<option value="3">Three</option>
										</select>
									</Col>
									<Col xs={12}>
										<div class="form-check">
											<input
												class="form-check-input"
												type="checkbox"
												id="inlineFormCheck"
											/>
											<Label
												class="form-check-label"
												for="inlineFormCheck"
												>Remember me</Label
											>
										</div>
									</Col>
									<Col xs={12}>
										<button
											type="submit"
											class="btn btn-primary"
											>Submit</button
										>
									</Col>
								</Row>
							</Form>
						</div>
						<div class="d-none code-view">
							<PrismCode code={InlineForms} id="inlineForms" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Floating Labels" />
					<CardBody>
						<p class="text-muted">
							Use <code>form-floating</code> class to enable floating
							labels with Bootstrap’s textual form fields.
						</p>
						<div class="live-preview">
							<Form action="#">
								<Row class="g-3">
									<Col lg={6}>
										<div class="form-floating">
											<Input
												type="text"
												class="form-control"
												id="firstnamefloatingInput"
												placeholder="Enter your firstname"
											/>
											<Label for="firstnamefloatingInput"
												>First Name</Label
											>
										</div>
									</Col>
									<Col lg={6}>
										<div class="form-floating">
											<Input
												type="text"
												class="form-control"
												id="lastnamefloatingInput"
												placeholder="Enter your Lastname"
											/>
											<Label for="lastnamefloatingInput"
												>Last Name</Label
											>
										</div>
									</Col>
									<Col lg={4}>
										<div class="form-floating">
											<Input
												type="email"
												class="form-control"
												id="emailfloatingInput"
												placeholder="Enter your email"
											/>
											<Label for="emailfloatingInput"
												>Email Address</Label
											>
										</div>
									</Col>
									<Col lg={4}>
										<div class="form-floating">
											<Input
												type="password"
												class="form-control"
												id="passwordfloatingInput"
												placeholder="Enter your password"
											/>
											<Label for="passwordfloatingInput"
												>Password</Label
											>
										</div>
									</Col>
									<Col lg={4}>
										<div class="form-floating">
											<Input
												type="password"
												class="form-control"
												id="passwordfloatingInput1"
												placeholder="Confirm password"
											/>
											<Label for="passwordfloatingInput1"
												>Confirm Password</Label
											>
										</div>
									</Col>
									<Col lg={4}>
										<div class="form-floating">
											<Input
												type="text"
												class="form-control"
												id="cityfloatingInput"
												placeholder="Enter your city"
											/>
											<Label for="cityfloatingInput"
												>City</Label
											>
										</div>
									</Col>
									<Col lg={4}>
										<div class="form-floating">
											<select
												class="form-select"
												id="floatingSelect"
												aria-label="Floating label select example"
											>
												<option>Choose...</option>
												<option value="1">USA</option>
												<option value="2">Brazil</option
												>
												<option value="3">France</option
												>
												<option value="4"
													>Germany</option
												>
											</select>
											<Label for="floatingSelect"
												>Country</Label
											>
										</div>
									</Col>
									<Col lg={4}>
										<div class="form-floating">
											<Input
												type="number"
												class="form-control"
												id="zipfloatingInput"
												placeholder="Enter your zipcode"
											/>
											<Label for="zipfloatingInput"
												>Zipcode</Label
											>
										</div>
									</Col>
									<Col lg={12}>
										<div class="text-end">
											<button
												type="submit"
												class="btn btn-primary"
												>Submit</button
											>
										</div>
									</Col>
								</Row>
							</Form>
						</div>
						<div class="d-none code-view">
							<PrismCode code={FloatingLabels} id="floatingLabels" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
