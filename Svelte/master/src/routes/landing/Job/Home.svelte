<script>
    import {
  Card,
  Col,
  Container,
  Form,
  Input,
  Row,
  Tooltip,
} from "sveltestrap";
import Link from 'svelte-link'

import Avatar3 from "../../../assets/images/users/avatar-3.jpg";
import Avatar9 from "../../../assets/images/users/avatar-9.jpg";
import Avatar10 from "../../../assets/images/users/avatar-10.jpg";
import JobProfile2 from "../../../assets/images/job-profile2.png";

</script>
<section class="section job-hero-section bg-light pb-0" id="hero">
    <Container>
      <Row class="justify-content-between align-items-center">
        <Col lg={6}>
          <div>
            <h1 class="display-6 fw-semibold text-capitalize mb-3 lh-base">
              Find your next job and build your dream here
            </h1>
            <p class="lead text-muted lh-base mb-4">
              Find jobs, create trackable resumes and enrich your
              applications. Carefully crafted after analyzing the needs of
              different industries.
            </p>
            <Form action="#" class="job-panel-filter">
              <Row class="g-md-0 g-2">
                <Col class="col-md-4">
                  <div>
                    <Input
                      type="search"
                      id="job-title"
                      class="form-control filter-input-box"
                      placeholder="Job, Company name..."
                    />
                  </div>
                </Col>
                <Col class="col-md-4">
                  <div>
                    <select class="form-control" data-choices>
                      <option value="">Select job type</option>
                      <option value="Full Time">Full Time</option>
                      <option value="Part Time">Part Time</option>
                      <option value="Freelance">Freelance</option>
                      <option value="Intership">Intership</option>
                    </select>
                  </div>
                </Col>
                <Col class="col-md-4">
                  <div class="h-100">
                    <button
                      class="btn btn-primary submit-btn w-100 h-100"
                      type="submit"
                    >
                      <i class="ri-search-2-line align-bottom me-1"></i>{" "}
                      Find Job
                    </button>
                  </div>
                </Col>
              </Row>
            </Form>

            <ul class="treding-keywords list-inline mb-0 mt-3 fs-13">
              <li class="list-inline-item text-danger fw-semibold">
                <i class="mdi mdi-tag-multiple-outline align-middle"></i>{" "}
                Trending Keywords:
              </li>
              <li class="list-inline-item">
                <Link href={null}>
                  Design,
                </Link>
              </li>
              <li class="list-inline-item">
                <Link href={null}>
                  Development,
                </Link>
              </li>
              <li class="list-inline-item">
                <Link href={null}>
                  Manager,
                </Link>
              </li>
              <li class="list-inline-item">
                <Link href={null}>
                  Senior
                </Link>
              </li>
            </ul>
          </div>
        </Col>
        <Col lg={4}>
          <div class="position-relative home-img text-center mt-5 mt-lg-0">
            <Card class="card-bg-fill p-3 rounded shadow-lg inquiry-box">
              <div class="d-flex align-items-center">
                <div class="avatar-sm flex-shrink-0 me-3">
                  <div class="avatar-title bg-warning-subtle text-warning rounded fs-18">
                    <i class="ri-mail-send-line"></i>
                  </div>
                </div>
                <h5 class="fs-15 lh-base mb-0">
                  Work Inquiry from velzon
                </h5>
              </div>
            </Card>

            <Card class="card-bg-fill p-3 rounded shadow-lg application-box">
              <h5 class="fs-15 lh-base mb-3">Applications</h5>
              <div class="avatar-group">
                <Link href={null} class="avatar-group-item" id="brent">
                  <Tooltip placement="top" target="brent">
                    Brent Gonzalez
                  </Tooltip>
                  <div class="avatar-xs">
                    <img
                      src={Avatar3}
                      alt=""
                      class="rounded-circle img-fluid"
                    />
                  </div>
                </Link>
                <Link href={null} class="avatar-group-item " id="ellen">
                  <Tooltip placement="top" target="ellen">
                    Ellen Smith
                  </Tooltip>
                  <div class="avatar-xs">
                    <div class="avatar-title rounded-circle bg-danger">
                      S
                    </div>
                  </div>
                </Link>
                <Link href={null} class="avatar-group-item" id="smith">
                  <Tooltip placement="top" target="smith">
                    Ellen Smith
                  </Tooltip>
                  <div class="avatar-xs">
                    <img
                      src={Avatar10}
                      alt=""
                      class="rounded-circle img-fluid"
                    />
                  </div>
                </Link>
                <Link
                  href={null}
                  class="avatar-group-item"
                  data-bs-toggle="tooltip"
                  data-bs-trigger="hover"
                  data-bs-placement="top"
                >
                  <div class="avatar-xs">
                    <div class="avatar-title rounded-circle bg-success">
                      Z
                    </div>
                  </div>
                </Link>
                <Link
                  href={null}
                  class="avatar-group-item"
                  id="gonzalez"
                >
                  <Tooltip placement="top" target="gonzalez">
                    Brent Gonzalez
                  </Tooltip>
                  <div class="avatar-xs">
                    <img
                      src={Avatar9}
                      alt=""
                      class="rounded-circle img-fluid"
                    />
                  </div>
                </Link>
                <Link href={null} class="avatar-group-item" id="more">
                  <Tooltip placement="top" target="more">
                    More Appliances
                  </Tooltip>
                  <div class="avatar-xs">
                    <div class="avatar-title fs-13 rounded-circle bg-light border-dashed border text-primary">
                      2k+
                    </div>
                  </div>
                </Link>
              </div>
            </Card>
            <img src={JobProfile2} alt="" class="user-img" />

            <div class="circle-effect">
              <div class="circle"></div>
              <div class="circle2"></div>
              <div class="circle3"></div>
              <div class="circle4"></div>
            </div>
          </div>
        </Col>
      </Row>
    </Container>
  </section>