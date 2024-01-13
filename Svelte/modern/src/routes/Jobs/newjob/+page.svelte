<svelte:head>
  <title>New Job | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import {
        Card,
        CardBody,
        CardHeader,
        Col,
        Container,
        Form,
        Input,
        Label,
        Row,
    } from "sveltestrap";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import Flatpickr from "svelte-flatpickr";
</script>

<div class="page-content">
    <Container fluid class="container-fluid">
        <BreadCrumb title="New Job" pageTitle="Jobs" />

        <Row class="row">
            <Col class="col-lg-12">
                <Card class="card">
                    <Form action="#">
                        <CardHeader class="card-header">
                            <h5 class="card-title mb-0">Create Job</h5>
                        </CardHeader>
                        <CardBody class="card-body">
                            <Row class="row g-4">
                                <Col class="col-lg-6">
                                    <div>
                                        <Label
                                            htmlFor="job-title-Input"
                                            class="form-label"
                                        >
                                            Job Title <span class="text-danger"
                                                >*</span
                                            >
                                        </Label>
                                        <Input
                                            type="text"
                                            class="form-control"
                                            id="job-title-Input"
                                            placeholder="Enter job title"
                                            required
                                        />
                                    </div>
                                </Col>
                                <Col class="col-lg-6">
                                    <div>
                                        <Label
                                            htmlFor="job-position-Input"
                                            class="form-label"
                                        >
                                            Job Position <span
                                                class="text-danger">*</span
                                            >
                                        </Label>
                                        <Input
                                            type="text"
                                            class="form-control"
                                            id="job-position-Input"
                                            placeholder="Enter job position"
                                            required
                                        />
                                    </div>
                                </Col>
                                <Col class="col-lg-6">
                                    <div>
                                        <Label
                                            htmlFor="job-category-Input"
                                            class="form-label"
                                        >
                                            Job Category <span
                                                class="text-danger">*</span
                                            >
                                        </Label>
                                        <select
                                            class="form-control"
                                            data-choices
                                            name="job-category-Input"
                                            required
                                        >
                                            <option value=""
                                                >Select Category</option
                                            >
                                            <option
                                                value="Accounting & Finance"
                                            >
                                                Accounting & Finance
                                            </option>
                                            <option value="Purchasing Manager">
                                                Purchasing Manager
                                            </option>
                                            <option
                                                value="Education & training"
                                            >
                                                Education & training
                                            </option>
                                            <option
                                                value="Marketing & Advertising"
                                            >
                                                Marketing & Advertising
                                            </option>
                                            <option value="It / Software Jobs">
                                                It / Software Jobs
                                            </option>
                                            <option value="Digital Marketing">
                                                Digital Marketing
                                            </option>
                                            <option
                                                value="Administrative Officer"
                                            >
                                                Administrative Officer
                                            </option>
                                            <option value="Government Jobs">
                                                Government Jobs
                                            </option>
                                        </select>
                                    </div>
                                </Col>
                                <Col class="col-lg-6">
                                    <div>
                                        <Label
                                            htmlFor="job-type-Input"
                                            class="form-label"
                                        >
                                            Job Type <span class="text-danger"
                                                >*</span
                                            >
                                        </Label>
                                        <select
                                            class="form-control"
                                            data-choices
                                            name="job-type-Input"
                                            required
                                        >
                                            <option value=""
                                                >Select job type</option
                                            >
                                            <option value="Full Time"
                                                >Full Time</option
                                            >
                                            <option value="Part Time"
                                                >Part Time</option
                                            >
                                            <option value="Freelance"
                                                >Freelance</option
                                            >
                                            <option value="Intership"
                                                >Intership</option
                                            >
                                        </select>
                                    </div>
                                </Col>

                                <Col class="col-lg-12">
                                    <div>
                                        <Label
                                            htmlFor="description-field"
                                            class="form-label"
                                        >
                                            Description <span
                                                class="text-danger">*</span
                                            >
                                        </Label>
                                        <textarea
                                            class="form-control"
                                            id="description-field"
                                            rows="3"
                                            placeholder="Enter description"
                                            required
                                        />
                                    </div>
                                </Col>

                                <Col class="col-md-6">
                                    <div>
                                        <Label
                                            htmlFor="vancancy-Input"
                                            class="form-label"
                                        >
                                            No. of Vancancy{" "}
                                            <span class="text-danger">*</span>
                                        </Label>
                                        <Input
                                            type="number"
                                            class="form-control"
                                            id="vancancy-Input"
                                            placeholder="No. of vancancy"
                                            required
                                        />
                                    </div>
                                </Col>
                                <Col class="col-md-6">
                                    <div>
                                        <Label
                                            htmlFor="experience-Input"
                                            class="form-label"
                                        >
                                            Experience <span class="text-danger"
                                                >*</span
                                            >
                                        </Label>
                                        <select
                                            class="form-control"
                                            data-choices
                                            name="experience-Input"
                                        >
                                            <option value=""
                                                >Select Experience</option
                                            >
                                            <option value="0 Year"
                                                >0 Year</option
                                            >
                                            <option value="2 Yeasr"
                                                >2 Years</option
                                            >
                                            <option value="3 Years"
                                                >3 Years</option
                                            >
                                            <option value="4 Years"
                                                >4 Years</option
                                            >
                                            <option value="5 Years"
                                                >5 Years</option
                                            >
                                        </select>
                                    </div>
                                </Col>

                                <Col class="col-lg-6">
                                    <div>
                                        <Label
                                            htmlFor="last-apply-date-Input"
                                            class="form-label"
                                        >
                                            Last Date of Apply{" "}
                                            <span class="text-danger">*</span>
                                        </Label>
                                        <Flatpickr
                                            class="form-control"
                                            id="datepicker-publish-input"
                                            placeholder="Select date"
                                            options={{
                                                altInput: true,
                                                altFormat: "F j, Y",
                                                mode: "multiple",
                                                dateFormat: "d.m.y",
                                            }}
                                        />
                                    </div>
                                </Col>

                                <Col class="col-lg-6">
                                    <div>
                                        <Label
                                            htmlFor="close-date-Input"
                                            class="form-label"
                                        >
                                            Close Date <span class="text-danger"
                                                >*</span
                                            >
                                        </Label>
                                        <Flatpickr
                                            class="form-control"
                                            id="datepicker-publish-input"
                                            placeholder="Select date"
                                            options={{
                                                altInput: true,
                                                altFormat: "F j, Y",
                                                mode: "multiple",
                                                dateFormat: "d.m.y",
                                            }}
                                        />
                                    </div>
                                </Col>

                                <Col class="col-md-6">
                                    <div>
                                        <Label
                                            htmlFor="start-salary-Input"
                                            class="form-label"
                                        >
                                            Start Salary
                                        </Label>
                                        <Input
                                            type="number"
                                            class="form-control"
                                            id="start-salary-Input"
                                            placeholder="Enter start salary"
                                            required
                                        />
                                    </div>
                                </Col>

                                <Col class="col-md-6">
                                    <div>
                                        <Label
                                            htmlFor="last-salary-Input"
                                            class="form-label"
                                        >
                                            Last Salary
                                        </Label>
                                        <Input
                                            type="number"
                                            class="form-control"
                                            id="last-salary-Input"
                                            placeholder="Enter end salary"
                                            required
                                        />
                                    </div>
                                </Col>

                                <Col class="col-md-6">
                                    <div>
                                        <Label
                                            htmlFor="country-Input"
                                            class="form-label"
                                        >
                                            Country <span class="text-danger"
                                                >*</span
                                            >
                                        </Label>
                                        <Input
                                            type="text"
                                            class="form-control"
                                            id="country-Input"
                                            placeholder="Enter country"
                                            required
                                        />
                                    </div>
                                </Col>

                                <Col class="col-md-6">
                                    <div>
                                        <Label
                                            htmlFor="city-Input"
                                            class="form-label"
                                        >
                                            State <span class="text-danger"
                                                >*</span
                                            >
                                        </Label>
                                        <Input
                                            type="text"
                                            class="form-control"
                                            id="city-Input"
                                            placeholder="Enter city"
                                            required
                                        />
                                    </div>
                                </Col>

                                <Col class="col-lg-12">
                                    <div>
                                        <Label
                                            htmlFor="website-field"
                                            class="form-label"
                                        >
                                            Tags
                                        </Label>
                                        <Input
                                            class="form-control"
                                            id="choices-text-unique-values"
                                            data-choices
                                            data-choices-text-unique-true
                                            type="text"
                                            defaultValue="Design, Remote"
                                            required
                                        />
                                    </div>
                                </Col>

                                <Col class="col-lg-12">
                                    <div
                                        class="hstack justify-content-end gap-2"
                                    >
                                        <button
                                            type="button"
                                            class="btn btn-ghost-danger"
                                        >
                                            <i
                                                class="ri-close-line align-bottom"
                                            />{" "}
                                            Cancel
                                        </button>
                                        <button
                                            type="submit"
                                            class="btn btn-primary"
                                        >
                                            Add Job
                                        </button>
                                    </div>
                                </Col>
                            </Row>
                        </CardBody>
                    </Form>
                </Card>
            </Col>
        </Row>
    </Container>
</div>
