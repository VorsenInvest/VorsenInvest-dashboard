<script>
  import {
    Card,
    CardBody,
    CardHeader,
    Col,
    Container,
    Form,
    Input,
    Nav,
    NavItem,
    Row,
    // Modal,
    ModalBody,
    Label,
    Button,
    NavLink,
  } from "sveltestrap";
  import MultiUser from "../../../assets/images/users/multi-user.jpg";
  import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
  import Flatpickr from "svelte-flatpickr";
  import DeleteModal from "../../../Components/Common/CDeleteModal.svelte";
  import jobApplication from "../../../common/data/appsJobs";
  import Select from "svelte-select";
  import { html } from "gridjs";
  import Grid from "gridjs-svelte";
  import Modal from "../../../Components/Common/Modal.svelte";

  let activeTab = 1;
  var option = [
    { label: "Status", value: "Status" },
    { label: "Approved", value: "Approved" },
    { label: "New", value: "New" },
    { label: "Pending", value: "Pending" },
    { label: "Rejected", value: "Rejected" },
  ];

  var option1 = [
    { label: "Select Options", value: "Select Options" },
    { label: "Full Time", value: "Full Time" },
    { label: "Part Time", value: "Part Time" },
  ];
  const selectCountry = "Select Options";
  let deleteModal = false;
  const setDeleteModal = (status) => {
    deleteModal = status;
  };

  var show = false;
  var handleClose = () => (show = !show);

  var data = jobApplication.jobApplication;
  const columns = [
    {
      name: "#",
      id: "appid",
      width: "140px",
      formatter: (cell) =>
        html(`<a href={null} class="fw-medium link-primary">${cell}</a>`),
    },
    {
      id: "company",
      name: "Name",
      formatter: (cell) =>
        html(
          `<div class="d-flex align-items-center">
              <div class="flex-shrink-0">
                  <img src=${cell[0]} alt="" class="avatar-xxs rounded-circle image_src object-cover">
              </div>
              <div class="flex-grow-1 ms-2">${cell[1]}</div>
          </div>`
        ),
    },
    {
      id: "designation",
      name: "Designation",
    },
    {
      id: "date",
      name: "Date",
    },
    {
      id: "contacts",
      name: "Contact",
    },
    {
      id: "type",
      name: "Type",
    },
    {
      id: "status",
      name: "Status",
      formatter: (cell) => {
        {
          if (cell == "New") {
            return html(
              `<span class="badge bg-info-subtle text-info text-uppercase">${cell}</span>`
            );
          } else if (cell == "Rejected") {
            return html(
              `<span class="badge bg-danger-subtle text-danger text-uppercase">${cell}</span>`
            );
          } else if (cell == "Pending") {
            return html(
              `<span class="badge bg-warning-subtle text-warning text-uppercase">${cell}</span>`
            );
          } else if (cell == "Approved") {
            return html(
              `<span class="badge bg-success-subtle text-success text-uppercase">${cell}</span>`
            );
          } else {
            return null;
          }
        }
      },
    },
  ];
</script>

<svelte:head>
  <title>Application | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
  <DeleteModal show={deleteModal} onCloseClick={() => setDeleteModal(false)} />
  <Container fluid>
    <BreadCrumb title="Application" pageTitle="Jobs" />
    <Row>
      <Col>
        <Card>
          <CardHeader class="border-0">
            <div class="d-md-flex align-items-center">
              <h5 class="card-title mb-3 mb-md-0 flex-grow-1">
                Job Application
              </h5>
              <div class="flex-shrink-0">
                <div class="d-flex gap-1 flex-wrap">
                  <button
                    type="button"
                    class="btn btn-primary add-btn"
                    data-bs-toggle="modal"
                    id="create-btn"
                    on:click={handleClose}
                    ><i class="ri-add-line align-bottom me-1" /> Create Application</button
                  >
                  <button type="button" class="btn btn-secondary"
                    ><i class="ri-file-download-line align-bottom me-1" />
                    Import</button
                  >
                  <button class="btn btn-soft-danger" id="remove-actions"
                    ><i class="ri-delete-bin-2-line" /></button
                  >
                </div>
              </div>
            </div>
          </CardHeader>
          <CardBody class="border border-dashed border-end-0 border-start-0">
            <Form>
              <Row class="g-3">
                <Col xxl={5} sm={6}>
                  <div class="search-box">
                    <Input
                      type="text"
                      class="form-control search"
                      placeholder="Search for application ID, company, designation status or something..."
                    />
                    <i class="ri-search-line search-icon" />
                  </div>
                </Col>
                <Col xxl={2} sm={6}>
                  <div>
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
                <Col xxl={2} sm={4}>
                  <div>
                    <Select
                      items={option}
                      name="choices-single-default"
                      id="idStatus"
                    />
                  </div>
                </Col>
                <Col xxl={2} sm={4}>
                  <div>
                    <Select
                      items={option1}
                      name="choices-single-default"
                      id="idType"
                      value={selectCountry}
                    />
                  </div>
                </Col>
                <Col xxl={1} sm={4}>
                  <div>
                    <Button type="button" color="info" class="btn w-100">
                      {" "}
                      <i class="ri-equalizer-fill me-1 align-bottom" />
                      Filters
                    </Button>
                  </div>
                </Col>
              </Row>
            </Form>
          </CardBody>
          <CardBody class="pt-0">
            <div>
              <Nav
                class="nav nav-tabs nav-tabs-custom nav-success mb-3"
                role="tablist"
              >
                <NavItem>
                  <NavLink
                    class="All py-3"
                    data-bs-toggle="tab"
                    id="All"
                    href={null}
                    role="tab"
                    aria-selected="true"
                    on:click={() => {
                      activeTab = 1;
                    }}
                    active={activeTab == 1}
                  >
                    All Application
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    class="py-3 New"
                    data-bs-toggle="tab"
                    id="New"
                    href={null}
                    role="tab"
                    aria-selected="false"
                    on:click={() => {
                      activeTab = 2;
                    }}
                    active={activeTab == 2}
                  >
                    New
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    class="py-3 Pending"
                    data-bs-toggle="tab"
                    id="Pending"
                    href={null}
                    role="tab"
                    aria-selected="false"
                    on:click={() => {
                      activeTab = 3;
                    }}
                    active={activeTab == 3}
                  >
                    Pending{" "}
                    <span class="badge bg-danger align-middle ms-1"> 2 </span>
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    class="py-3 Approved"
                    data-bs-toggle="tab"
                    id="Approved"
                    href={null}
                    role="tab"
                    aria-selected="false"
                    on:click={() => {
                      activeTab = 4;
                    }}
                    active={activeTab == 4}
                  >
                    Approved
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink
                    class="py-3 Rejected"
                    data-bs-toggle="tab"
                    id="Rejected"
                    href={null}
                    role="tab"
                    aria-selected="false"
                    on:click={() => {
                      activeTab = 5;
                    }}
                    active={activeTab == 5}
                  >
                    Rejected
                  </NavLink>
                </NavItem>
              </Nav>
              <div class="gridjs-border-none">
                <Grid
                  {data}
                  {columns}
                  sort={true}
                  pagination={{ enabled: true, limit: 10 }}
                />
              </div>
            </div>
            <Modal isOpen={show} className="modal-dialog-centered">
              <div class="modal-header p-3 bg-light">
                <h5 class="modal-title">Add Application</h5>
                <button
                  type="button"
                  class="btn-close"
                  on:click={handleClose}
                />
              </div>
              <Form action="#" autoComplete="off">
                <ModalBody class="modal-body">
                  <Input type="hidden" id="id-field" />

                  <div class="mb-3 d-none" id="modal-id">
                    <Label htmlFor="applicationId" class="form-label">ID</Label>
                    <Input
                      type="text"
                      id="applicationId"
                      class="form-control"
                      placeholder="ID"
                      readOnly
                    />
                  </div>

                  <div class="text-center">
                    <div class="position-relative d-inline-block">
                      <div class="position-absolute bottom-0 end-0">
                        <Label
                          htmlFor="companylogo-image-input"
                          class="mb-0"
                          data-bs-toggle="tooltip"
                          data-bs-placement="right"
                          title="Select Image"
                        >
                          <div class="avatar-xs cursor-pointer">
                            <div
                              class="avatar-title bg-light border rounded-circle text-muted"
                            >
                              <i class="ri-image-fill" />
                            </div>
                          </div>
                        </Label>
                        <Input
                          class="form-control d-none"
                          id="companylogo-image-input"
                          type="file"
                          accept="image/png, image/gif, image/jpeg"
                        />
                      </div>
                      <div class="avatar-lg p-1">
                        <div class="avatar-title bg-light rounded-circle">
                          <img
                            src={MultiUser}
                            id="companylogo-img"
                            class="avatar-md h-auto rounded-circle object-cover"
                            alt=""
                          />
                        </div>
                      </div>
                    </div>
                  </div>

                  <div class="mb-3">
                    <Label htmlFor="company-field" class="form-label">
                      Company
                    </Label>
                    <Input
                      type="text"
                      id="company-field"
                      class="form-control"
                      placeholder="Enter company name"
                      required
                    />
                  </div>

                  <div class="mb-3">
                    <Label htmlFor="designation-field" class="form-label">
                      Designation
                    </Label>
                    <Input
                      type="text"
                      id="designation-field"
                      class="form-control"
                      placeholder="Enter designation"
                      required
                    />
                  </div>

                  <div class="mb-3">
                    <Label htmlFor="date-field" class="form-label">
                      Apply Date
                    </Label>
                    <Input
                      type="date"
                      id="date-field"
                      class="form-control"
                      data-provider="flatpickr"
                      data-date-format="d M, Y"
                      required
                      placeholder="Select date"
                    />
                  </div>

                  <div class="mb-3">
                    <Label htmlFor="contact-field" class="form-label">
                      Contacts
                    </Label>
                    <Input
                      type="text"
                      id="contact-field"
                      class="form-control"
                      placeholder="Enter contact"
                      required
                    />
                  </div>

                  <Row class="gy-4 mb-3">
                    <div class="col-md-6">
                      <div>
                        <Label htmlFor="status-input" class="form-label">
                          Status
                        </Label>
                        <select
                          class="form-control"
                          data-trigger
                          name="status-input"
                          id="status-input"
                        >
                          <option value="">Status</option>
                          <option value="Approved">Approved</option>
                          <option value="New">New</option>
                          <option value="Pending">Pending</option>
                          <option value="Rejected">Rejected</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div>
                        <Label htmlFor="type-input" class="form-label">
                          Type
                        </Label>
                        <select
                          class="form-control"
                          data-trigger
                          name="type-input"
                          id="type-input"
                        >
                          <option value="">Select Type</option>
                          <option value="Full Time">Full Time</option>
                          <option value="Part Time">Part Time</option>
                        </select>
                      </div>
                    </div>
                  </Row>
                </ModalBody>
                <div class="modal-footer">
                  <div class="hstack gap-2 justify-content-end">
                    <Button
                      type="button"
                      class="btn btn-light"
                      on:click={handleClose}
                    >
                      Close
                    </Button>
                    <Button color="success" type="submit" id="add-btn">
                      Add
                    </Button>
                    
                  </div>
                </div>
              </Form>
            </Modal>
          </CardBody>
        </Card>
      </Col>
    </Row>
  </Container>
</div>
