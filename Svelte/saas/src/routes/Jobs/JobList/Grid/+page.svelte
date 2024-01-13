<script>
  import {
    Card,
    CardBody,
    Col,
    DropdownItem,
    DropdownMenu,
    DropdownToggle,
    Form,
    Input,
    Row,
    Dropdown,
  } from "sveltestrap";
  import Flatpickr from "svelte-flatpickr";
  import jobGrid from "../../../../common/data/appsJobs";
  import Link from "svelte-link";
  import BreadCrumb from "../../../../Components/Common/BreadCrumb.svelte";
</script>

<svelte:head>
  <title>Job Grid | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
  <div class="container-fluid">
    <BreadCrumb title="Job Grid Lists" pageTitle="Jobs" />

    <Row>
      <Col lg={12}>
        <Card>
          <CardBody class="bg-light-subtle">
            <Form>
              <Row class="g-3">
                <Col xxl={4} sm={12}>
                  <div class="search-box">
                    <Input
                      type="text"
                      class="form-control search bg-light border-light"
                      id="searchJob"
                      autoComplete="off"
                      placeholder="Search for jobs or companies..."
                    />
                    <i class="ri-search-line search-icon" />
                  </div>
                </Col>

                <Col xxl={3} sm={4}>
                  <Flatpickr
                    class="form-control"
                    id="datepicker-publish-input"
                    placeholder="Select a date"
                    options={{
                      altInput: true,
                      altFormat: "F j, Y",
                      mode: "multiple",
                      dateFormat: "d.m.y",
                    }}
                  />
                </Col>

                <Col xxl={2} sm={4}>
                  <div class="input-light">
                    <select
                      class="form-control"
                      data-choices
                      data-choices-search-false
                      name="choices-idType"
                      id="idType"
                    >
                      <option value="all" defaultValue> All </option>
                      <option value="Full Time">Full Time</option>
                      <option value="Part Time">Part Time</option>
                      <option value="Intership">Intership</option>
                      <option value="Freelance">Freelance</option>
                    </select>
                  </div>
                </Col>

                <Col xxl={2} sm={4}>
                  <div class="input-light">
                    <select
                      class="form-control"
                      data-choices
                      data-choices-search-false
                      name="choices-single-default"
                      id="idStatus"
                    >
                      <option value="all" defaultValue> All </option>
                      <option value="Active">Active</option>
                      <option value="New">New</option>
                      <option value="Close">Close</option>
                    </select>
                  </div>
                </Col>

                <Col xxl={1} sm={4}>
                  <button type="button" class="btn btn-primary w-100">
                    <i class="ri-equalizer-fill me-1 align-bottom" />{" "}
                    Filters
                  </button>
                </Col>
              </Row>
            </Form>
          </CardBody>
        </Card>
      </Col>
    </Row>

    <Row>
      <Col lg={12}>
        <div class="d-flex align-items-center mb-4">
          <div class="flex-grow-1">
            <p class="text-muted fs-14 mb-0">
              Result: <span id="total-result">7</span>
            </p>
          </div>
          <div class="flex-shrink-0">
            <Dropdown class="dropdown">
              <DropdownToggle
                class="btn text-muted fs-14 dropdown-toggle p-0"
                href={null}
                role="button"
                tag="button"
                type="button"
                color=""
              >
                All View
              </DropdownToggle>
              <DropdownMenu
                class="dropdown-menu"
                aria-labelledby="dropdownMenuLink"
              >
                <li>
                  <DropdownItem class="dropdown-item" href={null}>
                    Action
                  </DropdownItem>
                </li>
                <li>
                  <DropdownItem class="dropdown-item" href={null}>
                    Another action
                  </DropdownItem>
                </li>
                <li>
                  <DropdownItem class="dropdown-item" href={null}>
                    Something else here
                  </DropdownItem>
                </li>
              </DropdownMenu>
            </Dropdown>
          </div>
        </div>
      </Col>
    </Row>

    <Row id="job-list">
      <Col lg={3} md={6} id="job-widget">
        <Card class="card-height-100 bg-info bg-job">
          <CardBody class="p-5">
            <h2 class="lh-base text-white">
              Velzon invites young professionals for an intership!
            </h2>
            <p class="text-white text-opacity-75 mb-0 fs-14">
              Don't miss your opportunity to improve your skills!
            </p>
            <div class="mt-5 pt-2">
              <button type="button" class="btn btn-light w-100">
                View More{" "}
                <i class="ri-arrow-right-line align-bottom" />
              </button>
            </div>
          </CardBody>
        </Card>
      </Col>

      {#each jobGrid.jobGrid as item}
        <Col lg={3} md={6}>
          <Card>
            <CardBody>
              <button
                type="button"
                class="btn btn-icon btn-soft-primary float-end"
                data-bs-toggle="button"
                aria-pressed="true"
              >
                <i class="mdi mdi-cards-heart fs-16" />
              </button>
              <div class="avatar-sm mb-4">
                <div class="avatar-title bg-light rounded">
                  <img src={item.companyLogo} alt="" class="avatar-xxs" />
                </div>
              </div>
              <Link href={null}>
                <h5>{item.jobTitle}</h5>
              </Link>
              <p class="text-muted">{item.companyName}</p>
              <div class="d-flex gap-4 mb-3">
                <div>
                  <i
                    class="ri-map-pin-2-line text-primary me-1 align-bottom"
                  />{" "}
                  {item.location}
                </div>
                <div>
                  <i class="ri-time-line text-primary me-1 align-bottom" />{" "}
                  {item.postDate}
                </div>
              </div>
              <p class="text-muted">{item.description}</p>
              <div class="hstack gap-2">
                {#each item.requirement as subItem}
                  {#if subItem === "Full Time"}
                    <span class="badge bg-success-subtle text-success"
                      >{subItem}</span
                    >
                  {:else if subItem === "Freelance"}
                    <span class="badge bg-primary-subtle text-primary"
                      >{subItem}</span
                    >
                  {:else if subItem === "Urgent"}
                    <span class="badge bg-danger-subtle text-danger"
                      >{subItem}</span
                    >
                  {:else}
                    <span class="badge bg-warning-subtle text-warning"
                      >{subItem}</span
                    >
                  {/if}
                {/each}
              </div>
              <div class="mt-4 hstack gap-2">
                <Link href={null} class="btn btn-soft-primary w-100">
                  Apply Job
                </Link>
                <Link
                  href="/apps-job-details"
                  class="btn btn-soft-success w-100"
                >
                  Overview
                </Link>
              </div>
            </CardBody>
          </Card>
        </Col>
      {/each}
    </Row>

    <Row class="g-0 justify-content-end mb-4" id="pagination-element">
      <Col sm={6}>
        <div
          class="pagination-block pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0"
        >
          <div class="page-item">
            <Link href="" class="page-link" id="page-prev">Previous</Link>
          </div>
          <span id="page-num" class="pagination" />
          <div class="page-item">
            <Link href="" class="page-link" id="page-next">Next</Link>
          </div>
        </div>
      </Col>
    </Row>
  </div>
</div>
