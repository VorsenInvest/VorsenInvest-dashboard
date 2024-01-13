<script>
	import {
		Card,
		CardBody,
		Col,
		Container,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Input,
		Label,
		Row,
		Dropdown
	} from "sveltestrap";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";

	//InputExample code
	const InputExample = `<!-- Basic Input -->
<Col xxl={3} md={6}>
    <div>
        <Label for="basiInput" class="form-label">Basic Input</Label>
        <Input type="password" class="form-control" id="basiInput" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="labelInput" class="form-label">Input with Label</Label>
        <Input type="password" class="form-control" id="labelInput" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="placeholderInput" class="form-label">Input with Placeholder</Label>
        <Input type="password" class="form-control" id="placeholderInput" placeholder="Placeholder" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="valueInput" class="form-label">Input with Value</Label>
        <Input type="text" class="form-control" id="valueInput" value="Input value" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="readonlyPlaintext" class="form-label">Readonly Plain Text Input</Label>
        <Input type="text" class="form-control-plaintext" id="readonlyPlaintext" value="Readonly input" readonly />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="readonlyInput" class="form-label">Readonly Input</Label>
        <Input type="text" class="form-control" id="readonlyInput" value="Readonly input" readonly />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="disabledInput" class="form-label">Disabled Input</Label>
        <Input type="text" class="form-control" id="disabledInput" value="Disabled input" disabled />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="iconInput" class="form-label">Input with Icon</Label>
        <div class="form-icon">
            <Input type="email" class="form-control form-control-icon" id="iconInput" placeholder="example@gmail.com" />
            <i class="ri-mail-unread-line"></i>
        </div>
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="iconrightInput" class="form-label">Input with Icon Right</Label>
        <div class="form-icon right">
            <Input type="email" class="form-control form-control-icon" id="iconrightInput" placeholder="example@gmail.com" />
            <i class="ri-mail-unread-line"></i>
        </div>
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="exampleInputdate" class="form-label">Input Date</Label>
        <Input type="date" class="form-control" id="exampleInputdate" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="exampleInputtime" class="form-label">Input Time</Label>
        <Input type="time" class="form-control" id="exampleInputtime" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="exampleInputpassword" class="form-label">Input Password</Label>
        <Input type="password" class="form-control" id="exampleInputpassword" value="44512465" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="exampleFormControlTextarea5" class="form-label">Example Textarea</Label>
        <textarea class="form-control" id="exampleFormControlTextarea5" rows="3"></textarea>
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="formtextInput" class="form-label">Form Text</Label>
        <Input type="password" class="form-control" id="formtextInput" />
        <div id="passwordHelpBlock" class="form-text">
            Must be 8-20 characters long.
        </div>
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="colorPicker" class="form-label">Color Picker</Label>
        <Input type="color" class="form-control form-control-color w-100" id="colorPicker" value="#25a0e2" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="borderInput" class="form-label">Input Border Style</Label>
        <Input type="text" class="form-control border-dashed" id="borderInput" placeholder="Enter your name" />
    </div>
</Col>

<Col xxl={3} md={6}>
    <Label for="exampleDataList" class="form-label">Datalist example</Label>
    <Input class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Search your country..." />
    <datalist id="datalistOptions">
        <option value="Switzerland"> </option>
        <option value="New York"> </option>
        <option value="France"> </option>
        <option value="Spain"> </option>
        <option value="Chicago"> </option>
        <option value="Bulgaria"> </option>
        <option value="Hong Kong"> </option>
    </datalist>
</Col>

<Col xxl={3} md={6}>
    <div>
        <Label for="exampleInputrounded" class="form-label">Rounded Input</Label>
        <Input type="text" class="form-control rounded-pill" id="exampleInputrounded" placeholder="Enter your name" />
    </div>
</Col>
`;

	const InputSizing = `<Col lg={4}>
<Input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" />
</Col>

<Col lg={4}>
<Input class="form-control" type="text" placeholder=".form-control" />
</Col>

<Col lg={4}>
<Input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" />
</Col>
`;

	const FileInput = `<!-- Default File Input Example -->
<Row class="align-items-center g-3">
<Col lg={4}>
    <div>
        <Label for="formFile" class="form-label">Default File Input Example</Label>
        <p class="text-muted">Use <code>input</code> attribute with <code>type="file"</code> tag for default file input.</p>
        <Input class="form-control" type="file" id="formFile" />
    </div>
</Col>

<Col lg={4}>
    <div>
        <Label for="formFileMultiple" class="form-label">Multiple Files Input Example</Label>
        <p class="text-muted">Use <code>multiple</code> attribute within the input attribute to select multiple files.</p>
        <Input class="form-control" type="file" id="formFileMultiple" multiple />
    </div>
</Col>

<Col lg={4}>
    <div>
        <Label for="formFileDisabled" class="form-label">Disabled File Input Example</Label>
        <p class="text-muted">Use <code>disabled</code> attribute within the input attribute to disable the file input.</p>
        <Input class="form-control" type="file" id="formFileDisabled" disabled />
    </div>
</Col>
</Row>

<Row class="mt-4 align-items-center g-3">
<h5 class="fs-14">File Input Sizing</h5>
<Col lg={4}>
    <div>
        <Label for="formSizeSmall" class="form-label">Small Size File Input Example</Label>
        <p class="text-muted">Use <code>form-control-sm</code> class within the form-control class to set a small size file input.</p>
        <Input class="form-control form-control-sm" id="formSizeSmall" type="file" />
    </div>
</Col>
<Col lg={4}>
    <div>
        <Label for="formSizeDefault" class="form-label">Default Size File Input Example</Label>
        <p class="text-muted">Use <code>form-control </code>class and <code>type="file"</code> attribute within the input attribute to set a default size file input.</p>
        <Input class="form-control" id="formSizeDefault" type="file" />
    </div>
</Col>
<Col lg={4}>
    <div>
        <Label for="formSizeLarge" class="form-label">Large Size File Input Example</Label>
        <p class="text-muted">Use <code>form-control-lg</code> class within the form-control class to set a large size file input.</p>

        <Input class="form-control form-control-lg" id="formSizeLarge" type="file" />
    </div>
</Col>

</Row>
`;

	const InputGroup = `<div>
<h5 class="fs-15">Basic example</h5>
<p class="text-muted">Use <code>input-group</code> class to div element which contains input attribute to wrap a default input in the group.</p>
<Row class="g-3">
    <Col lg={6}>
        <div class="input-group">
            <span class="input-group-text" id="basic-addon1">@</span>
            <Input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" />
        </div>
    </Col>
    <Col lg={6}>
        <div class="input-group">
            <Input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="basic-addon2" />
            <span class="input-group-text" id="basic-addon2">@example.com</span>
        </div>
    </Col>
    <Col lg={12}>
        <div class="input-group">
            <span class="input-group-text">$</span>
            <Input type="text" class="form-control" aria-label="Amount (to the nearest dollar)" />
            <span class="input-group-text">.00</span>
        </div>
    </Col>
    <Col lg={12}>
        <div class="input-group">
            <Input type="text" class="form-control" placeholder="Username" aria-label="Username" />
            <span class="input-group-text">@</span>
            <Input type="text" class="form-control" placeholder="Server" aria-label="Server" />
        </div>
    </Col>
    <Col lg={6}>
        <div class="input-group">
            <span class="input-group-text">With textarea</span>
            <textarea class="form-control" aria-label="With textarea" rows="2"></textarea>
        </div>
    </Col>
    <Col lg={6}>
        <Label for="basic-url" class="form-label">Your vanity URL</Label>
        <div class="input-group">
            <span class="input-group-text" id="basic-addon3">https://example.com/users/</span>
            <Input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3" />
        </div>
    </Col>
</Row>
</div>

<div class="mt-4">
<h5 class="fs-15">Wrapping</h5>
<p class="text-muted">
    Input groups wrap by default via <code>flex-wrap: wrap</code> in order to accommodate custom form field validation within an input group. You may disable this with <code>flex-nowrap</code> class.
</p>
<div class="input-group flex-nowrap">
    <span class="input-group-text" id="addon-wrapping">@</span>
    <Input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping" />
</div>
</div>
`;

	const InputGroupSizing = `<!-- Input Group Sizing -->
<Row class="align-items-center g-3">
    <Col lg={4} >
        <div class="input-group input-group-sm">
            <span class="input-group-text" id="inputGroup-sizing-sm">Small</span>
            <Input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm" />
        </div>
    </Col>
    <Col lg={4} >
        <div class="input-group">
            <span class="input-group-text" id="inputGroup-sizing-default">Default</span>
            <Input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" />
        </div>
    </Col>
    <Col lg={4} >
        <div class="input-group input-group-lg">
            <span class="input-group-text" id="inputGroup-sizing-lg">Large</span>
            <Input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg" />
        </div>
    </Col>
</Row>
`;

	const MultipleInputs = `<!-- Multiple Inputs -->
<div class="input-group mb-3">
<span class="input-group-text">First and last name</span>
<Input type="text" aria-label="First name" class="form-control" />
<Input type="text" aria-label="Last name" class="form-control" />
</div>

<div class="input-group mb-3">
    <span class="input-group-text">$</span>
    <span class="input-group-text">0.00</span>
    <Input type="text" class="form-control" aria-label="Dollar amount (with dot and two decimal places)" />
</div>

<div class="input-group">
    <Input type="text" class="form-control" aria-label="Dollar amount (with dot and two decimal places)" />
    <span class="input-group-text">$</span>
    <span class="input-group-text">0.00</span>
</div>
`;

	const ButtonsCheckboxesRadiosGroup = `<!-- Checkbox Input -->
<div class="input-group">
    <div class="input-group-text">
        <input class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input">
    </div>
    <input type="text" class="form-control" aria-label="Text input with checkbox">
</div>

<!-- Radio Input -->
<div class="input-group">
    <div class="input-group-text">
        <input class="form-check-input mt-0" type="radio" value="" aria-label="Radio button for following text input">
    </div>
    <input type="text" class="form-control" aria-label="Text input with radio button">
</div>

<!-- Buttons Input -->
<div class="input-group">
    <button class="btn btn-outline-primary" type="button" id="button-addon1">Button</button>
    <input type="text" class="form-control" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1">
</div>
<div class="input-group">
    <input type="text" class="form-control" aria-label="Recipient's username" aria-describedby="button-addon2">
    <button class="btn btn-outline-success" type="button" id="button-addon2">Button</button>
</div>
<div class="input-group">
    <button class="btn btn-primary" type="button">Button</button>
    <button class="btn btn-success" type="button">Button</button>
    <input type="text" class="form-control" placeholder="" aria-label="Example text with two button addons">
</div>
<div class="input-group">
    <input type="text" class="form-control" aria-label="Recipient's username with two button addons">
    <button class="btn btn-primary" type="button">Button</button>
    <button class="btn btn-success" type="button">Button</button>
</div>
`;

	const ButtonsWithDropdowns = ` 
<!-- Buttons with dropdowns -->
<div class="input-group">
    <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href={null}>Action</a></li>
        <li><a class="dropdown-item" href={null}>Another action</a></li>
        <li><a class="dropdown-item" href={null}>Something else here</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href={null}>Separated link</a></li>
    </ul>
    <input type="text" class="form-control" aria-label="Text input with dropdown button">
</div>

<div class="input-group">
    <input type="text" class="form-control" aria-label="Text input with dropdown button">
    <button class="btn btn-success dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
    <ul class="dropdown-menu dropdown-menu-end">
      <li><a class="dropdown-item" href={null}>Action</a></li>
        <li><a class="dropdown-item" href={null}>Another action</a></li>
        <li><a class="dropdown-item" href={null}>Something else here</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href={null}>Separated link</a></li>
    </ul>
</div>

<div class="input-group">
    <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
    <ul class="dropdown-menu">
        <li><a class="dropdown-item" href={null}>Action before</a></li>
        <li><a class="dropdown-item" href={null}>Another action before</a></li>
        <li><a class="dropdown-item" href={null}>Something else here</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href={null}>Separated link</a></li>
    </ul>
    <input type="text" class="form-control" aria-label="Text input with 2 dropdown buttons">
    <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
    <ul class="dropdown-menu dropdown-menu-end">
        <li><a class="dropdown-item" href={null}>Action</a></li>
        <li><a class="dropdown-item" href={null}>Another action</a></li>
        <li><a class="dropdown-item" href={null}>Something else here</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href={null}>Separated link</a></li>
    </ul>
</div>
`;

	const CustomForms = `<!-- Select -->
<div class="input-group">
    <Label class="input-group-text" for="inputGroupSelect01">Options</Label>
    <select class="form-select" id="inputGroupSelect01">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
    </select>
</div>
<div class="input-group">
    <select class="form-select" id="inputGroupSelect02">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
        </select>
    <Label class="input-group-text" for="inputGroupSelect02">Options</Label>
</div>
<div class="input-group">
    <button class="btn btn-outline-primary" type="button">Button</button>
    <select class="form-select" id="inputGroupSelect03" aria-label="Example select with button addon">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
    </select>
</div>
<div class="input-group">
    <select class="form-select" id="inputGroupSelect04" aria-label="Example select with button addon">
        <option selected>Choose...</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
    </select>
    <button class="btn btn-outline-secondary" type="button">Button</button>
</div>

<!-- File Input -->
<div class="input-group">
    <Label class="input-group-text" for="inputGroupFile01">Upload</Label>
    <input type="file" class="form-control" id="inputGroupFile01">
</div>
<div class="input-group">
    <input type="file" class="form-control" id="inputGroupFile02">
    <Label class="input-group-text" for="inputGroupFile02">Upload</Label>
</div>
<div class="input-group">
    <button class="btn btn-outline-primary" type="button" id="inputGroupFileAddon03">Button</button>
    <input type="file" class="form-control" id="inputGroupFile03" aria-describedby="inputGroupFileAddon03" aria-label="Upload">
</div>
<div class="input-group">
    <input type="file" class="form-control" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04" aria-label="Upload">
    <button class="btn btn-outline-success" type="button" id="inputGroupFileAddon04">Button</button>
</div>
`;
</script>

<svelte:head>
	<title>basic Elements | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Basic Elements" pageTitle="Forms" />

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Input Example" />

					<CardBody class="card-body">
						<div class="live-preview">
							<Row class="gy-4">
								<Col xxl={3} md={6}>
									<div>
										<Label
											for="basiInput"
											class="form-label"
											>Basic Input</Label
										>
										<Input
											type="password"
											class="form-control"
											id="basiInput"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="labelInput"
											class="form-label"
											>Input with Label</Label
										>
										<Input
											type="password"
											class="form-control"
											id="labelInput"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="placeholderInput"
											class="form-label"
											>Input with Placeholder</Label
										>
										<Input
											type="password"
											class="form-control"
											id="placeholderInput"
											placeholder="Placeholder"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="valueInput"
											class="form-label"
											>Input with Value</Label
										>
										<Input
											type="text"
											class="form-control"
											id="valueInput"
											value="Input value"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="readonlyPlaintext"
											class="form-label"
											>Readonly Plain Text Input</Label
										>
										<Input
											type="text"
											class="form-control plaintext"
											id="readonlyPlaintext"
											value="Readonly input"
											readonly
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="readonlyInput"
											class="form-label"
											>Readonly Input</Label
										>
										<Input
											type="text"
											class="form-control plaintext"
											id="readonlyInput"
											value="Readonly input"
											readonly
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="disabledInput"
											class="form-label"
											>Disabled Input</Label
										>
										<Input
											type="text"
											class="form-control"
											id="disabledInput"
											value="Disabled input"
											disabled
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="iconInput"
											class="form-label"
											>Input with Icon</Label
										>
										<div class="form-icon">
											<Input
												type="email"
												class="form-control form-control-icon"
												id="iconInput"
												placeholder="example@gmail.com"
											/>
											<i class="ri-mail-unread-line" />
										</div>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="iconrightInput"
											class="form-label"
											>Input with Icon Right</Label
										>
										<div class="form-icon right">
											<Input
												type="email"
												class="form-control form-control-icon"
												id="iconrightInput"
												placeholder="example@gmail.com"
											/>
											<i class="ri-mail-unread-line" />
										</div>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="exampleInputdate"
											class="form-label">Input Date</Label
										>
										<Input
											type="date"
											class="form-control"
											id="exampleInputdate"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="exampleInputtime"
											class="form-label">Input Time</Label
										>
										<Input
											type="time"
											class="form-control"
											id="exampleInputtime"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="exampleInputpassword"
											class="form-label"
											>Input Password</Label
										>
										<Input
											type="password"
											class="form-control"
											id="exampleInputpassword"
											value="44512465"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="exampleFormControlTextarea5"
											class="form-label"
											>Example Textarea</Label
										>
										<textarea
											class="form-control"
											id="exampleFormControlTextarea5"
											rows="3"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="formtextInput"
											class="form-label">Form Text</Label
										>
										<Input
											type="password"
											class="form-control"
											id="formtextInput"
										/>
										<div 	id="passwordHelpBlock"
											class="form-text"
										>
											Must be 8-20 characters long.
										</div>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="colorPicker"
											class="form-label"
											>Color Picker</Label
										>
										<Input
											type="color"
											class="form-control form-control-color w-100"
											id="colorPicker"
											value="#25a0e2"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="borderInput"
											class="form-label"
											>Input Border Style</Label
										>
										<Input
											type="text"
											class="form-control border-dashed"
											id="borderInput"
											placeholder="Enter your name"
										/>
									</div>
								</Col>

								<Col xxl={3} md={6}>
									<Label
										for="exampleDataList"
										class="form-label"
										>Datalist example</Label
									>
									<Input
										class="form-control"
										list="datalistOptions"
										id="exampleDataList"
										placeholder="Search your country..."
									/>
									<datalist id="datalistOptions">
										<option value="Switzerland" />
										<option value="New York" />
										<option value="France" />
										<option value="Spain" />
										<option value="Chicago" />
										<option value="Bulgaria" />
										<option value="Hong Kong" />
									</datalist>
								</Col>

								<Col xxl={3} md={6}>
									<div>
										<Label
											for="exampleInputrounded"
											class="form-label"
											>Rounded Input</Label
										>
										<Input
											type="text"
											class="form-control rounded-pill"
											id="exampleInputrounded"
											placeholder="Enter your name"
										/>
									</div>
								</Col>
								<Col xxl={3} md={6}>
									<div class="form-floating">
										<Input
											type="text"
											class="form-control"
											id="firstnamefloatingInput"
											placeholder="Enter your firstname"
										/>
										<Label for="firstnamefloatingInput"
											>Floating Input</Label
										>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={InputExample} id="InputExample" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Input Sizing" />

					<CardBody>
						<p class="text-muted">
							Use <code>form-control-lg</code> class to set large
							size input and Use
							<code>form-control-sm</code> class to set small size
							input. No class is needed for default size input.
						</p>
						<div class="live-preview">
							<Row class="align-items-center g-3">
								<Col lg={4}>
									<Input
										class="form-control form-control-sm"
										type="text"
										placeholder=".form-control-sm"
									/>
								</Col>

								<Col lg={4}>
									<Input
										class="form-control"
										type="text"
										placeholder=".form-control"
									/>
								</Col>

								<Col lg={4}>
									<Input
										class="form-control form-control-lg"
										type="text"
										placeholder=".form-control-lg"
									/>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={InputSizing} id="InputSizing" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="File Input" />

					<CardBody>
						<div class="live-preview">
							<Row class="align-items-center g-3">
								<Col lg={4}>
									<div>
										<Label for="formFile" class="form-label"
											>Default File Input Example</Label
										>
										<p class="text-muted">
											Use <code>input</code> attribute
											with <code>type="file"</code> tag for
											default file input.
										</p>
										<Input
											class="form-control"
											type="file"
											id="formFile"
										/>
									</div>
								</Col>

								<Col lg={4}>
									<div>
										<Label
											for="formFileMultiple"
											class="form-label"
											>Multiple Files Input Example</Label
										>
										<p class="text-muted">
											Use <code>multiple</code> attribute within
											the input attribute to select multiple
											files.
										</p>
										<Input
											class="form-control"
											type="file"
											id="formFileMultiple"
											multiple
										/>
									</div>
								</Col>

								<Col lg={4}>
									<div>
										<Label
											for="formFileDisabled"
											class="form-label"
											>Disabled File Input Example</Label
										>
										<p class="text-muted">
											Use <code>disabled</code> attribute within
											the input attribute to disable the file
											input.
										</p>
										<Input
											class="form-control"
											type="file"
											id="formFileDisabled"
											disabled
										/>
									</div>
								</Col>
							</Row>

							<Row class="mt-4 align-items-center g-3">
								<h5 class="fs-14">File Input Sizing</h5>
								<Col lg={4}>
									<div>
										<Label
											for="formSizeSmall"
											class="form-label"
											>Small Size File Input Example</Label
										>
										<p class="text-muted">
											Use <code>form-control-sm</code> class
											within the form-control class to set
											a small size file input.
										</p>
										<Input
											class="form-control form-control-sm"
											id="formSizeSmall"
											type="file"
										/>
									</div>
								</Col>
								<Col lg={4}>
									<div>
										<Label
											for="formSizeDefault"
											class="form-label"
											>Default Size File Input Example</Label
										>
										<p class="text-muted">
											Use <code>form-control </code>class
											and <code>type="file"</code> attribute
											within the input attribute to set a default
											size file input.
										</p>
										<Input
											class="form-control"
											id="formSizeDefault"
											type="file"
										/>
									</div>
								</Col>
								<Col lg={4}>
									<div>
										<Label
											for="formSizeLarge"
											class="form-label"
											>Large Size File Input Example</Label
										>
										<p class="text-muted">
											Use <code>form-control-lg</code> class
											within the form-control class to set
											a large size file input.
										</p>

										<Input
											class="form-control form-control-lg"
											id="formSizeLarge"
											type="file"
										/>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={FileInput} id="formFileInput" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Input Group" />

					<CardBody>
						<div class="live-preview">
							<div>
								<h5 class="fs-15">Basic example</h5>
								<p class="text-muted">
									Use <code>input-group</code> class to div element
									which contains input attribute to wrap a default
									input in the group.
								</p>
								<Row class="g-3">
									<Col lg={6}>
										<div class="input-group">
											<span
												class="input-group-text"
												id="basic-addon1">@</span
											>
											<Input
												type="text"
												class="form-control"
												placeholder="Username"
												aria-label="Username"
												aria-describedby="basic-addon1"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<Input
												type="text"
												class="form-control"
												placeholder="Recipient's username"
												aria-label="Recipient's username"
												aria-describedby="basic-addon2"
											/>
											<span
												class="input-group-text"
												id="basic-addon2"
												>@example.com</span
											>
										</div>
									</Col>
									<Col lg={12}>
										<div class="input-group">
											<span class="input-group-text"
												>$</span
											>
											<Input
												type="text"
												class="form-control"
												aria-label="Amount (to the nearest dollar)"
											/>
											<span class="input-group-text"
												>.00</span
											>
										</div>
									</Col>
									<Col lg={12}>
										<div class="input-group">
											<Input
												type="text"
												class="form-control"
												placeholder="Username"
												aria-label="Username"
											/>
											<span class="input-group-text"
												>@</span
											>
											<Input
												type="text"
												class="form-control"
												placeholder="Server"
												aria-label="Server"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<span class="input-group-text"
												>With textarea</span
											>
											<textarea
												class="form-control"
												aria-label="With textarea"
												rows="2"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<Label
											for="basic-url"
											class="form-label"
											>Your vanity URL</Label
										>
										<div class="input-group">
											<span
												class="input-group-text"
												id="basic-addon3"
												>https://example.com/users/</span
											>
											<Input
												type="text"
												class="form-control"
												id="basic-url"
												aria-describedby="basic-addon3"
											/>
										</div>
									</Col>
								</Row>
							</div>

							<div class="mt-4">
								<h5 class="fs-15">Wrapping</h5>
								<p class="text-muted">
									Input groups wrap by default via <code
										>flex-wrap: wrap</code
									>
									in order to accommodate custom form field
									validation within an input group. You may
									disable this with <code>flex-nowrap</code> class.
								</p>
								<div class="input-group flex-nowrap">
									<span
										class="input-group-text"
										id="addon-wrapping">@</span
									>
									<Input
										type="text"
										class="form-control"
										placeholder="Username"
										aria-label="Username"
										aria-describedby="addon-wrapping"
									/>
								</div>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode code={InputGroup} id="formInputGroup" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Input Group Sizing" />

					<CardBody>
						<p class="text-muted">
							Use <code>input-group-sm</code> class to set a small
							size input group and
							<code>input-group-lg</code> class to input-group class
							to set a large size input group respectively. no such
							class is required for a default size input group.
						</p>
						<div class="live-preview">
							<Row class="align-items-center g-3">
								<Col lg={4}>
									<div class="input-group input-group-sm">
										<span
											class="input-group-text"
											id="inputGroup-sizing-sm"
											>Small</span
										>
										<Input
											type="text"
											class="form-control"
											aria-label="Sizing example input"
											aria-describedby="inputGroup-sizing-sm"
										/>
									</div>
								</Col>
								<Col lg={4}>
									<div class="input-group">
										<span
											class="input-group-text"
											id="inputGroup-sizing-default"
											>Default</span
										>
										<Input
											type="text"
											class="form-control"
											aria-label="Sizing example input"
											aria-describedby="inputGroup-sizing-default"
										/>
									</div>
								</Col>
								<Col lg={4}>
									<div class="input-group input-group-lg">
										<span
											class="input-group-text"
											id="inputGroup-sizing-lg"
											>Large</span
										>
										<Input
											type="text"
											class="form-control"
											aria-label="Sizing example input"
											aria-describedby="inputGroup-sizing-lg"
										/>
									</div>
								</Col>
							</Row>
						</div>
						<div class="d-none code-view">
							<PrismCode code={InputGroupSizing} id="formInputGroupSizing" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Multiple Inputs" />

					<CardBody>
						<p class="text-muted">
							While multiple <code>&lt;input&gt;</code>s are
							supported visually, validation styles are only
							available for input groups with a single
							<code>&lt;input&gt;</code>.
						</p>
						<div class="live-preview">
							<div class="input-group mb-3">
								<span class="input-group-text"
									>First and last name</span
								>
								<Input
									type="text"
									aria-label="First name"
									class="form-control"
								/>
								<Input
									type="text"
									aria-label="Last name"
									class="form-control"
								/>
							</div>

							<div class="input-group mb-3">
								<span class="input-group-text">$</span>
								<span class="input-group-text">0.00</span>
								<Input
									type="text"
									class="form-control"
									aria-label="Dollar amount (with dot and two decimal places)"
								/>
							</div>

							<div class="input-group">
								<Input
									type="text"
									class="form-control"
									aria-label="Dollar amount (with dot and two decimal places)"
								/>
								<span class="input-group-text">$</span>
								<span class="input-group-text">0.00</span>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode code={MultipleInputs} id="multipleInputs" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader
						title="Buttons, Checkboxs and Radios Group"
					/>

					<CardBody>
						<div class="live-preview">
							<div>
								<p class="text-muted">
									Use any checkbox, radio, or button option
									within an input group’s addon instead of
									text. We recommend adding <code>mt-0</code>
									class to the
									<code>form-check-input</code> when there’s no
									visible text next to the input.
								</p>
								<Row class="g-3">
									<Col lg={6}>
										<div class="input-group">
											<div class="input-group-text">
												<input
													class="form-check-input mt-0"
													type="checkbox"
													value=""
													aria-label="Checkbox for following text input"
												/>
											</div>
											<Input
												type="text"
												class="form-control"
												aria-label="Text input with checkbox"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<div class="input-group-text">
												<input
													class="form-check-input mt-0"
													type="radio"
													value=""
													aria-label="Radio button for following text input"
												/>
											</div>
											<Input
												type="text"
												class="form-control"
												aria-label="Text input with radio button"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<button
												class="btn btn-outline-primary"
												type="button"
												id="button-addon1"
												>Button</button
											>
											<Input
												type="text"
												class="form-control"
												placeholder=""
												aria-label="Example text with button addon"
												aria-describedby="button-addon1"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<Input
												type="text"
												class="form-control"
												aria-label="Recipient's username"
												aria-describedby="button-addon2"
											/>
											<button
												class="btn btn-outline-success"
												type="button"
												id="button-addon2"
												>Button</button
											>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<button
												class="btn btn-primary"
												type="button">Button</button
											>
											<button
												class="btn btn-success"
												type="button">Button</button
											>
											<Input
												type="text"
												class="form-control"
												placeholder=""
												aria-label="Example text with two button addons"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<Input
												type="text"
												class="form-control"
												aria-label="Recipient's username with two button addons"
											/>
											<button
												class="btn btn-primary"
												type="button">Button</button
											>
											<button
												class="btn btn-success"
												type="button">Button</button
											>
										</div>
									</Col>
								</Row>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode code={ButtonsCheckboxesRadiosGroup} id="ButtonsCheckboxesRadiosGroup" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Buttons with dropdowns" />

					<CardBody>
						<div class="live-preview">
							<div>
								<p class="text-muted">
									You can use a button with the dropdown
									toggle to set the file input group.
								</p>
								<Row class="g-3">
									<Col lg={6}>
										<Dropdown class="input-group">
											<DropdownToggle
												tag="button"
												class="btn btn-primary dropdown-toggle"
												color=""
												type="button"
												>Dropdown</DropdownToggle
											>
											<DropdownMenu>
												<DropdownItem
													>Action</DropdownItem
												>
												<DropdownItem
													>Another action</DropdownItem
												>
												<DropdownItem
													>Something else here</DropdownItem
												>
												<DropdownItem divider />
												<DropdownItem
													>Separated link</DropdownItem
												>
											</DropdownMenu>
											<Input
												type="text"
												class="form-control"
												aria-label="Text input with dropdown button"
											/>
										</Dropdown>
									</Col>
									<Col lg={6}>
										<Dropdown class="input-group">
											<Input
												type="text"
												class="form-control"
												aria-label="Text input with dropdown button"
											/>
											<DropdownToggle
												tag="button"
												class="btn btn-success dropdown-toggle"
												type="button"
												color=""
												data-bs-toggle="dropdown"
												aria-expanded="false"
												>Dropdown</DropdownToggle
											>
											<DropdownMenu
												class="dropdown-menu-end"
											>
												<DropdownItem
													>Action</DropdownItem
												>
												<DropdownItem
													>Another action</DropdownItem
												>
												<DropdownItem
													>Something else here</DropdownItem
												>
												<DropdownItem divider />
												<DropdownItem
													>Separated link</DropdownItem
												>
											</DropdownMenu>
										</Dropdown>
									</Col>
									<Col lg={12}>
										<div class="input-group">
											<Dropdown>
												<DropdownToggle
													tag="button"
													class="btn btn-outline-secondary dropdown-toggle"
													type="button"
													color=""
													data-bs-toggle="dropdown"
													aria-expanded="false"
													>Dropdown</DropdownToggle
												>
												<DropdownMenu>
													<DropdownItem
														>Action before</DropdownItem
													>
													<DropdownItem
														>Another action before</DropdownItem
													>
													<DropdownItem
														>Something else here</DropdownItem
													>
													<DropdownItem divider />
													<DropdownItem
														>Separated link</DropdownItem
													>
												</DropdownMenu>
											</Dropdown>
											<Input
												type="text"
												class="form-control"
												aria-label="Text input with 2 dropdown buttons"
											/>
											<Dropdown>
												<DropdownToggle
													tag="button"
													class="btn btn-outline-secondary dropdown-toggle"
													type="button"
													color=""
													data-bs-toggle="dropdown"
													aria-expanded="false"
													>Dropdown</DropdownToggle
												>
												<DropdownMenu
													class="dropdown-menu-end"
												>
													<DropdownItem
														>Action</DropdownItem
													>
													<DropdownItem
														>Another action</DropdownItem
													>
													<DropdownItem
														>Something else here</DropdownItem
													>
													<DropdownItem divider />
													<DropdownItem
														>Separated link</DropdownItem
													>
												</DropdownMenu>
											</Dropdown>
										</div>
									</Col>
								</Row>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode code={ButtonsWithDropdowns} id="ButtonsWithDropdowns" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col lg={12}>
				<Card>
					<PreviewCardHeader title="Custom Forms" />

					<CardBody>
						<p class="text-muted">
							Input groups include support for custom selects and
							custom file inputs. Browser default versions of
							these are not supported.
						</p>
						<div class="live-preview">
							<div>
								<h5 class="fs-15 mb-3">Select</h5>
								<Row class="g-3">
									<Col lg={6}>
										<div class="input-group">
											<Label
												class="input-group-text"
												for="inputGroupSelect01"
												>Options</Label
											>
											<select
												class="form-select"
												id="inputGroupSelect01"
											>
												<option>Choose...</option>
												<option value="1">One</option>
												<option value="2">Two</option>
												<option value="3">Three</option>
											</select>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<select
												class="form-select"
												id="inputGroupSelect02"
											>
												<option>Choose...</option>
												<option value="1">One</option>
												<option value="2">Two</option>
												<option value="3">Three</option>
											</select>
											<Label
												class="input-group-text"
												for="inputGroupSelect02"
												>Options</Label
											>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<button
												class="btn btn-outline-primary"
												type="button">Button</button
											>
											<select
												class="form-select"
												id="inputGroupSelect03"
												aria-label="Example select with button addon"
											>
												<option>Choose...</option>
												<option value="1">One</option>
												<option value="2">Two</option>
												<option value="3">Three</option>
											</select>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<select
												class="form-select"
												id="inputGroupSelect04"
												aria-label="Example select with button addon"
											>
												<option>Choose...</option>
												<option value="1">One</option>
												<option value="2">Two</option>
												<option value="3">Three</option>
											</select>
											<button
												class="btn btn-outline-secondary"
												type="button">Button</button
											>
										</div>
									</Col>
								</Row>
							</div>

							<div class="mt-4">
								<h5 class="fs-15 mb-3">File Input</h5>
								<Row class="g-3">
									<Col lg={6}>
										<div class="input-group">
											<Label
												class="input-group-text"
												for="inputGroupFile01"
												>Upload</Label
											>
											<Input
												type="file"
												class="form-control"
												id="inputGroupFile01"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<Input
												type="file"
												class="form-control"
												id="inputGroupFile02"
											/>
											<Label
												class="input-group-text"
												for="inputGroupFile02"
												>Upload</Label
											>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<button
												class="btn btn-outline-primary"
												type="button"
												id="inputGroupFileAddon03"
												>Button</button
											>
											<Input
												type="file"
												class="form-control"
												id="inputGroupFile03"
												aria-describedby="inputGroupFileAddon03"
												aria-label="Upload"
											/>
										</div>
									</Col>
									<Col lg={6}>
										<div class="input-group">
											<Input
												type="file"
												class="form-control"
												id="inputGroupFile04"
												aria-describedby="inputGroupFileAddon04"
												aria-label="Upload"
											/>
											<button
												class="btn btn-outline-success"
												type="button"
												id="inputGroupFileAddon04"
												>Button</button
											>
										</div>
									</Col>
								</Row>
							</div>
						</div>
						<div class="d-none code-view">
							<PrismCode code={CustomForms} id="CustomForms" />
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
