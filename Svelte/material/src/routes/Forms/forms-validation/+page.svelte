<script>
  import {
    Row,
    Col,
    Card,
    CardBody,
    Button,
    Label,
    Input,
    Container,
    InputGroup,
    FormGroup
  } from "sveltestrap";
  import { createForm } from "svelte-forms-lib";
  import * as yup from "yup";
  import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
  import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
  import PrismCode from "../../../Components/Common/Prism.svelte";
  import Tooltipform from '../tooltipform.svelte'
  import UiContent from "../../../Components/Common/UiContent.svelte";
  const { form, errors, state, handleChange, handleSubmit } = createForm({
      initialValues: {
        firstname: "Mark",
        lastname: "Otto",
        city: "",
        state: "",
        zip: "",
      },
      validationSchema: yup.object().shape({
        firstname: yup.string().required("Please Enter Your First Name"),
        lastname: yup.string().required("Please Enter Your Last Name"),
        city: yup.string().required("Please Enter Your City"),
        state: yup.string().required("Please Enter Your State"),
        zip: yup.string().required("Please Enter Your Zip"),
      }),
      onSubmit: values => {
        alert(JSON.stringify(values));
      }
    });

    const BrowserDefaults = `<form class="row g-3">
<Col md={4}>
  <Label for="validationDefault01" class="form-label"
    >First name</Label
  >
  <Input
    type="text"
    class="form-control"
    id="validationDefault01"
    value="Mark"
    required
  />
</Col>
<Col md={4}>
  <Label for="validationDefault02" class="form-label"
    >Last name</Label
  >
  <Input
    type="text"
    class="form-control"
    id="validationDefault02"
    value="Otto"
    required
  />
</Col>
<Col md={4}>
  <Label for="validationDefaultUsername" class="form-label"
    >Username</Label
  >
  <InputGroup>
    <span class="input-group-text" id="inputGroupPrepend2"
      >@</span
    >
    <Input
      type="text"
      class="form-control"
      id="validationDefaultUsername"
      aria-describedby="inputGroupPrepend2"
      required
    />
  </InputGroup>
</Col>
<Col md={6}>
  <Label for="validationDefault03" class="form-label"
    >City</Label
  >
  <Input
    type="text"
    class="form-control"
    id="validationDefault03"
    required
  />
</Col>
<Col md={3}>
  <Label for="validationDefault04" class="form-label"
    >State</Label
  >
  <select class="form-select" id="validationDefault04" required>
    <option disabled value="">Choose...</option>
    <option>...</option>
  </select>
</Col>
<Col md={3}>
  <Label for="validationDefault05" class="form-label">Zip</Label
  >
  <Input
    type="text"
    class="form-control"
    id="validationDefault05"
    required
  />
</Col>
<Col xs={12}>
  <div class="form-check">
    <input
      class="form-check-input"
      type="checkbox"
      value=""
      id="invalidCheck2"
      required
    />
    <Label class="form-check-label" for="invalidCheck2">
      Agree to terms and conditions
    </Label>
  </div>
</Col>
<Col xs={12}>
  <button class="btn btn-primary" type="submit"
    >Submit form</button
  >
</Col>
</form>`;

    const Customstyle= `<form on:submit={handleSubmit} class="needs-validation was-validated">
<Row>
  <Col md="6">
    <FormGroup class="mb-3">
      <Label htmlfor="validationCustom01">First name</Label>
      <input
        name="firstname"
        placeholder="Mark"
        type="text"
        class="form-control"
        id="validationCustom01"
        on:change={handleChange}
        on:blur={handleChange}
        bind:value={$form.firstname}
        required
      />
      {#if $errors.firstname}
        <div class="invalid-feedback" style="display: block">{$errors.firstname}</div>
      {/if}
    </FormGroup>
  </Col>
  <Col md="6">
    <FormGroup class="mb-3">
      <Label htmlfor="validationCustom02">Last name</Label>
      <input
        name="lastname"
        placeholder="Otto"
        type="text"
        class="form-control"
        id="validationCustom02"
        on:change={handleChange}
        on:blur={handleChange}
        bind:value={$form.lastname}
        required
      />
        {#if $errors.lastname}
        <div class="invalid-feedback" style="display: block">{$errors.lastname}</div>
        {/if}
    </FormGroup>
  </Col>
</Row>
<Row>
  <Col md="4">
    <FormGroup class="mb-3">
      <Label htmlfor="validationCustom03">City</Label>
      <input
        name="city"
        placeholder="City"
        type="text"
        class="form-control"
        on:change={handleChange}
        on:blur={handleChange}
        bind:value={$form.city}
        required
      />
      {#if $errors.city}
      <div class="invalid-feedback" style="display: block">{$errors.city}</div>
      {/if}
    </FormGroup>
  </Col>
  <Col md="4">
    <FormGroup class="mb-3">
      <Label htmlfor="validationCustom04">State</Label>
      <input
        name="state"
        placeholder="State"
        type="text"
        class="form-control"
        id="validationCustom04"
        on:change={handleChange}
        on:blur={handleChange}
        bind:value={$form.state}
        required
      />
      {#if $errors.state}
      <div class="invalid-feedback" style="display: block">{$errors.state}</div>
      {/if}
    </FormGroup>
  </Col>
  <Col md="4">
    <FormGroup class="mb-3">
      <Label htmlfor="validationCustom05">Zip</Label>
      <input
        name="zip"
        placeholder="Zip"
        type="text"
        class="form-control"
        id="validationCustom05"
        on:change={handleChange}
        on:blur={handleChange}
        bind:value={$form.zip}
        required
      />
      {#if $errors.zip}
      <div class="invalid-feedback" style="display: block">{$errors.zip}</div>
      {/if}
    </FormGroup>
  </Col>
</Row>
<Row>
  <Col lg="12">
    <FormGroup class="mb-3">
      <div class="form-check">
        <input
          type="checkbox"
          class="form-check-input"
          id="invalidCheck"
          required  
        />
        <Label class="form-check-label" htmlfor="invalidCheck">
          {" "}
          Agree to terms and conditions
        </Label>
      </div>
    </FormGroup>
  </Col>
</Row>
<button class="btn btn-primary" type="submit">
  Submit form
</button>
</form>`
</script>

<svelte:head>
  <title>Form Validation | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<UiContent />
<div class="page-content">
  <Container fluid={true}>
    <BreadCrumb title="Form Validation" pageTitle="Forms" />
    <Row>
      <Col lg={12}>
        <Card>
          <PreviewCardHeader title="Browser defaults" />
          <CardBody>
            <p class="text-muted">
              Not interested in custom validation feedback messages or writing
              JavaScript to change form behaviors? All good, you can use the
              browser defaults. Try submitting the form below. Depending on your
              browser and OS, you will see a slightly different style of
              feedback.While these feedback styles cannot be styled with CSS,
              you can still customize the feedback text through JavaScript.
            </p>

            <div class="live-preview">
              <form class="row g-3">
                <Col md={4}>
                  <Label for="validationDefault01" class="form-label"
                    >First name</Label
                  >
                  <Input
                    type="text"
                    class="form-control"
                    id="validationDefault01"
                    value="Mark"
                    required
                  />
                </Col>
                <Col md={4}>
                  <Label for="validationDefault02" class="form-label"
                    >Last name</Label
                  >
                  <Input
                    type="text"
                    class="form-control"
                    id="validationDefault02"
                    value="Otto"
                    required
                  />
                </Col>
                <Col md={4}>
                  <Label for="validationDefaultUsername" class="form-label"
                    >Username</Label
                  >
                  <InputGroup>
                    <span class="input-group-text" id="inputGroupPrepend2"
                      >@</span
                    >
                    <Input
                      type="text"
                      class="form-control"
                      id="validationDefaultUsername"
                      aria-describedby="inputGroupPrepend2"
                      required
                    />
                  </InputGroup>
                </Col>
                <Col md={6}>
                  <Label for="validationDefault03" class="form-label"
                    >City</Label
                  >
                  <Input
                    type="text"
                    class="form-control"
                    id="validationDefault03"
                    required
                  />
                </Col>
                <Col md={3}>
                  <Label for="validationDefault04" class="form-label"
                    >State</Label
                  >
                  <select class="form-select" id="validationDefault04" required>
                    <option disabled value="">Choose...</option>
                    <option>...</option>
                  </select>
                </Col>
                <Col md={3}>
                  <Label for="validationDefault05" class="form-label">Zip</Label
                  >
                  <Input
                    type="text"
                    class="form-control"
                    id="validationDefault05"
                    required
                  />
                </Col>
                <Col xs={12}>
                  <div class="form-check">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      value=""
                      id="invalidCheck2"
                      required
                    />
                    <Label class="form-check-label" for="invalidCheck2">
                      Agree to terms and conditions
                    </Label>
                  </div>
                </Col>
                <Col xs={12}>
                  <button class="btn btn-primary" type="submit"
                    >Submit form</button
                  >
                </Col>
              </form>
            </div>
            <div class="d-none code-view">
              <PrismCode code={BrowserDefaults} id="browserdefaults" />
            </div>
          </CardBody>
        </Card>
      </Col>
    </Row>

    <Row>
      <Col lg={12}>
        <Card>
          <PreviewCardHeader title="Custom Styles" />
          <CardBody>
            <p class="text-muted">
              For custom Bootstrap form validation messages, you will need to add the <code>novalidate</code> boolean attribute to your <code>&lt;form&gt;</code>. This disables the browser default feedback tooltips, but still provides access to the form validation APIs in JavaScript. Try to submit the form below; our JavaScript will intercept the submit button and relay feedback to you. When attempting to submit, you will see the <code>:invalid</code> and <code>:valid</code> styles applied to your form controls.
            </p>
            <div class="live-preview">
              <form on:submit={handleSubmit} class="needs-validation was-validated">
                <Row>
                  <Col md="6">
                    <FormGroup class="mb-3">
                      <Label htmlfor="validationCustom01">First name</Label>
                      <input
                        name="firstname"
                        placeholder="Mark"
                        type="text"
                        class="form-control"
                        id="validationCustom01"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.firstname}
                        required
                      />
                      {#if $errors.firstname}
                        <div class="invalid-feedback" style="display: block">{$errors.firstname}</div>
                      {/if}
                    </FormGroup>
                  </Col>
                  <Col md="6">
                    <FormGroup class="mb-3">
                      <Label htmlfor="validationCustom02">Last name</Label>
                      <input
                        name="lastname"
                        placeholder="Otto"
                        type="text"
                        class="form-control"
                        id="validationCustom02"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.lastname}
                        required
                      />
                        {#if $errors.lastname}
                        <div class="invalid-feedback" style="display: block">{$errors.lastname}</div>
                        {/if}
                    </FormGroup>
                  </Col>
                </Row>
                <Row>
                  <Col md="4">
                    <FormGroup class="mb-3">
                      <Label htmlfor="validationCustom03">City</Label>
                      <input
                        name="city"
                        placeholder="City"
                        type="text"
                        class="form-control"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.city}
                        required
                      />
                      {#if $errors.city}
                      <div class="invalid-feedback" style="display: block">{$errors.city}</div>
                      {/if}
                    </FormGroup>
                  </Col>
                  <Col md="4">
                    <FormGroup class="mb-3">
                      <Label htmlfor="validationCustom04">State</Label>
                      <input
                        name="state"
                        placeholder="State"
                        type="text"
                        class="form-control"
                        id="validationCustom04"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.state}
                        required
                      />
                      {#if $errors.state}
                      <div class="invalid-feedback" style="display: block">{$errors.state}</div>
                      {/if}
                    </FormGroup>
                  </Col>
                  <Col md="4">
                    <FormGroup class="mb-3">
                      <Label htmlfor="validationCustom05">Zip</Label>
                      <input
                        name="zip"
                        placeholder="Zip"
                        type="text"
                        class="form-control"
                        id="validationCustom05"
                        on:change={handleChange}
                        on:blur={handleChange}
                        bind:value={$form.zip}
                        required
                      />
                      {#if $errors.zip}
                      <div class="invalid-feedback" style="display: block">{$errors.zip}</div>
                      {/if}
                    </FormGroup>
                  </Col>
                </Row>
                <Row>
                  <Col lg="12">
                    <FormGroup class="mb-3">
                      <div class="form-check">
                        <input
                          type="checkbox"
                          class="form-check-input"
                          id="invalidCheck"
                          required  
                        />
                        <Label class="form-check-label" htmlfor="invalidCheck">
                          {" "}
                          Agree to terms and conditions
                        </Label>
                      </div>
                    </FormGroup>
                  </Col>
                </Row>
                <button class="btn btn-primary" type="submit">
                  Submit form
                </button>
            </form>
            </div>
            <div class="d-none code-view">
              <PrismCode code={Customstyle} id="customstyle"/>
            </div>
          </CardBody>
        </Card>
      </Col>
      </Row>

      <Tooltipform />
  </Container>
</div>
