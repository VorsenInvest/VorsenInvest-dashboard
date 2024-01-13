<script>
  import {
    Card,
    CardBody,
    Col,
    Container,
    Form,
    Input,
    Row,
    Table,
    NavLink,
  } from "sveltestrap";
  import Flatpickr from "svelte-flatpickr";
  import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
  import img6 from "../../../assets/images/companies/img-6.png";
  import jobCompanies from "../../../common/data/appsJobs";
</script>

<svelte:head>
  <title>Companies List | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
  <Container fluid class="container-fluid">
    <BreadCrumb title="Companies" pageTitle="Job" />
    <Row>
      <Col xxl={9}>
        <Card>
          <CardBody>
            <Form>
              <Row class="g-3">
                <Col xxl={5} sm={6}>
                  <div class="search-box">
                    <Input
                      type="text"
                      class="form-control search bg-light border-light"
                      id="searchCompany"
                      placeholder="Search for company, industry type..."
                    />
                    <i class="ri-search-line search-icon" />
                  </div>
                </Col>

                <Col xxl={3} sm={6}>
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
                      name="choices-single-default"
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
                  <button type="button" class="btn btn-danger w-100">
                    <i class="ri-equalizer-fill me-1 align-bottom" />{" "}
                    Filters
                  </button>
                </Col>
              </Row>
            </Form>
          </CardBody>
        </Card>

        <Row class="job-list-row" id="companies-list">
          {#each jobCompanies.jobCompanies as item}
            <Col xxl={3} md={6}>
              <Card class="card companiesList-card">
                <CardBody>
                  <div class="avatar-sm mx-auto">
                    <div class="avatar-title bg-light rounded">
                      <img
                        src={item.image_src}
                        alt=""
                        class="avatar-xxs companyLogo-img"
                      />
                    </div>
                  </div>
                  <div class="text-center">
                    <a href={null}>
                      <h5 class="mt-3 company-name">{item.lable}</h5>
                    </a>
                    <div class="d-none company-desc">
                      {item.company_info}
                    </div>
                    <p class="text-muted industry-type">
                      {item.industry_type}
                    </p>
                    <div class="d-none">
                      <span class="employee">{item.employee}</span>
                      <span class="location">{item.location}</span>
                      <span class="rating">{item.rating}</span>
                      <span class="website">{item.website}</span>
                      <span class="email">{item.email}</span>
                      <span class="since">{item.since}</span>
                    </div>
                  </div>
                  <div>
                    <button
                      type="button"
                      class="btn btn-soft-primary w-100 viewcompany-list"
                    >
                      <span class="vacancy">{item.vacancy}</span> Jobs Available
                    </button>
                  </div>
                </CardBody>
              </Card>
            </Col>
          {/each}
        </Row>

        <Row class="g-0 justify-content-end mb-4" id="pagination-element">
          <Col sm="6">
            <div
              class="pagination-block pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0"
            >
              <div class="page-item">
                <NavLink href="" class="page-link" id="page-prev">
                  Previous
                </NavLink>
              </div>
              <span id="page-num" class="pagination" />
              <div class="page-item">
                <NavLink href="" class="page-link" id="page-next">Next</NavLink>
              </div>
            </div>
          </Col>
        </Row>
      </Col>
      <Col xxl={3}>
        <Card id="company-overview">
          <CardBody>
            <div class="avatar-lg mx-auto mb-3">
              <div class="avatar-title bg-light rounded">
                <img src={img6} alt="" class="avatar-sm company-logo" />
              </div>
            </div>

            <div class="text-center">
              <NavLink href={null}>
                <h5 class="overview-companyname fw-semibold fs-17">Syntyce Solutions</h5>
              </NavLink>
              <p class="text-muted overview-industryType">IT Department</p>

              <ul class="list-inline mb-0">
                <li class="list-inline-item avatar-xs">
                  <NavLink
                    href=""
                    class="avatar-title bg-success-subtle text-success fs-15 rounded"
                  >
                    <i class="ri-global-line" />
                  </NavLink>
                </li>
                <li class="list-inline-item avatar-xs">
                  <NavLink
                    href=""
                    class="avatar-title bg-danger-subtle text-danger fs-15 rounded"
                  >
                    <i class="ri-mail-line" />
                  </NavLink>
                </li>
                <li class="list-inline-item avatar-xs">
                  <NavLink
                    href=""
                    class="avatar-title bg-warning-subtle text-warning fs-15 rounded"
                  >
                    <i class="ri-question-answer-line" />
                  </NavLink>
                </li>
              </ul>
            </div>
          </CardBody>

          <CardBody>
            <h6 class="text-muted text-uppercase fw-semibold mb-3">
              Information
            </h6>
            <p class="text-muted mb-4 overview-companydesc">
              The IT department of NavLink company ensures that the network of
              computers within the organisation are well-connected and
              functioning properly. All the other departments within the company
              rely on them to ensure that their respective functions can go on
              seamlessly.
            </p>

            <div class="table-responsive table-card">
              <Table class="table table-borderless mb-4">
                <tbody>
                  <tr>
                    <td class="fw-medium">Industry Type</td>
                    <td class="overview-industryType"> Chemical Industries </td>
                  </tr>
                  <tr>
                    <td class="fw-medium">Location</td>
                    <td class="overview-company_location"> Damascus, Syria </td>
                  </tr>
                  <tr>
                    <td class="fw-medium">Employee</td>
                    <td class="overview-employee">10-50</td>
                  </tr>
                  <tr>
                    <td class="fw-medium">Vacancy</td>
                    <td class="overview-vacancy">23</td>
                  </tr>
                  <tr>
                    <td class="fw-medium">Rating</td>
                    <td>
                      <span class="overview-rating">4.8</span>{" "}
                      <i class="ri-star-fill text-warning align-bottom" />
                    </td>
                  </tr>
                  <tr>
                    <td class="fw-medium">Website</td>
                    <td>
                      <NavLink
                        href=""
                        class="link-primary text-decoration-underline overview-website"
                      >
                        www.syntycesolution.com
                      </NavLink>
                    </td>
                  </tr>
                  <tr>
                    <td class="fw-medium">Contact Email</td>
                    <td class="overview-email"> info@syntycesolution.com </td>
                  </tr>
                  <tr>
                    <td class="fw-medium">Since</td>
                    <td class="overview-since">1995</td>
                  </tr>
                </tbody>
              </Table>
            </div>

            <div class="hstack gap-3">
              <button
                type="button"
                class="btn btn-soft-success custom-toggle w-100 shadow-none"
                data-bs-toggle="button"
              >
                <span class="icon-on">
                  <i class="ri-add-line align-bottom me-1" /> Follow
                </span>
                <span class="icon-off">
                  <i class="ri-user-unfollow-line align-bottom me-1" />{" "}
                  Unfollow
                </span>
              </button>
              <a href={null} class="btn btn-info w-100">
                More View{" "}
                <i class="ri-arrow-right-line align-bottom" />
              </a>
            </div>
          </CardBody>
        </Card>

        <Card class="overflow-hidden shadow-none">
          <CardBody class="bg-danger-subtle">
            <div class="d-flex align-items-center">
              <div class="flex-shrink-0">
                <div class="avatar-sm">
                  <div
                    class="avatar-title bg-danger-subtle text-danger rounded-circle fs-17"
                  >
                    <i class="ri-gift-line" />
                  </div>
                </div>
              </div>
              <div class="flex-grow-1 ms-2">
                <h6 class="fs-16">Free trial</h6>
                <p class="text-muted mb-0">28 days left</p>
              </div>
              <div>
                <a href="/pages/pricing/pages-pricing" class="btn btn-danger">
                  Upgrade
                </a>
              </div>
            </div>
          </CardBody>
          <CardBody
            class="bg-danger-subtle border-top border-danger border-opacity-25 border-top-dashed"
          >
            <NavLink
              href={null}
              class="d-flex justify-content-between align-items-center text-body"
            >
              <span>See benefits</span>
              <i class="ri-arrow-right-s-line fs-18" />
            </NavLink>
          </CardBody>
        </Card>
      </Col>
    </Row>
  </Container>
</div>
