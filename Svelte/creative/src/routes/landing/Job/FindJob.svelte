<script>
import {
    Card,
    CardBody,
    Col,
    Container,
    Row,
    Tooltip,
} from "sveltestrap";
import findJob from "../../../common/data/jobLanding";
import img1 from "../../../assets/images/companies/img-1.png";
import img5 from "../../../assets/images/companies/img-5.png";
import img2 from "../../../assets/images/companies/img-2.png";
import img7 from "../../../assets/images/companies/img-7.png";
import img8 from "../../../assets/images/companies/img-8.png";
import Link from 'svelte-link'

</script>
<section class="section" id="findJob">
    <Container>
      <Row class="justify-content-center">
        <Col class="col-lg-7">
          <div class="text-center mb-5">
            <h1 class="mb-3 ff-secondary fw-bold text-capitalize lh-base">
              Find Your <span class="text-primary">Career</span> You
              Deserve it
            </h1>
            <p class="text-muted">
              Post a job to tell us about your project. We'll quickly match you with the right freelancers.
            </p>
          </div>
        </Col>
      </Row>

      <Row>
        {#each findJob.findJob as item}
          <Col class="col-lg-6">
            <Card class="shadow-lg">
              <CardBody>
                <div class="d-flex">
                  <div class="avatar-sm">
                    <div class={"avatar-title bg-"+ item.iconColor +"-subtle rounded"}>
                      <img
                        src={item.company}
                        alt=""
                        class="avatar-xxs"
                      />
                    </div>
                  </div>
                  <div class="ms-3 flex-grow-1">
                    <Link href={null}>
                      <h5>{item.lable}</h5>
                    </Link>
                    <ul class="list-inline text-muted mb-3">
                      <li class="list-inline-item">
                        <i class="ri-building-line align-bottom me-1"></i>{" "}
                        {item.name}
                      </li>
                      <li class="list-inline-item">
                        <i class="ri-map-pin-2-line align-bottom me-1"></i>{" "}
                        {item.location}
                      </li>
                      <li class="list-inline-item">
                        <i class="ri-money-dollar-circle-line align-bottom me-1"></i>{" "}
                        {item.salary}
                      </li>
                    </ul>
                    <div class="hstack gap-2">
                      <span class={"badge bg-" + item.s1[1]+"-subtle text-" + item.s1[1]}>
                        {item.s1[0]}
                      </span>
                      <span class={"badge bg-" + item.s2[1]+"-subtle text-" + item.s2[1]}>
                        {item.s2[0]}
                      </span>
                      {#if item.s3}
                        <span class={"badge bg-" + item.s3[1]+"-subtle text-" + item.s3[1]}>
                            {item.s3[0]}
                        </span>
                      {/if}
                    </div>
                  </div>
                  <div>
                    <button
                      type="button"
                      class="btn btn-ghost-primary btn-icon custom-toggle"
                      data-bs-toggle="button"
                    >
                      <span class="icon-on">
                        <i class="ri-bookmark-line"></i>
                      </span>
                      <span class="icon-off">
                        <i class="ri-bookmark-fill"></i>
                      </span>
                    </button>
                  </div>
                </div>
              </CardBody>
            </Card>
          </Col>
          {/each}

        <div class="col-lg-12">
          <div class="text-center mt-4">
            <Link href={null} class="btn btn-ghost-primary">
              View More Jobs{" "}
              <i class="ri-arrow-right-line align-bottom"></i>
            </Link>
          </div>
        </div>
      </Row>
    </Container>
  </section>
  <section class="section">
    <Container>
      <Row class="align-items-center gy-4">
        <Col class="col-lg-6 order-2 order-lg-1">
          <div class="text-muted mt-5 mt-lg-0">
            <h5 class="fs-12 text-uppercase text-danger fw-semibold">
              Hot Featured Company
            </h5>
            <h1 class="mb-3 ff-secondary fw-bold text-capitalize lh-base">
              Get <span class="text-primary">10,000+</span> Featured
              Companies
            </h1>
            <p class="ff-secondary mb-2">
              The demand for content writing services is growing. This is
              because content is required in almost every industry.{" "}
              <b>
                Many companies have discovered how effective content
                marketing is.
              </b>{" "}
              This is Link major reason for this increase in demand.
            </p>
            <p class="mb-4 ff-secondary">
              A Content Writer is Link professional who writes
              informative and engaging articles to help brands showcase
              their products.
            </p>

            <div class="mt-4">
              <Link href="/dashboard" class="btn btn-primary">
                View More Companies{" "}
                <i class="ri-arrow-right-line align-middle ms-1"></i>
              </Link>
            </div>
          </div>
        </Col>
        <Col class="col-lg-4 col-sm-7 col-10 ms-lg-auto mx-auto order-1 order-lg-2">
          <div>
            <Card class="shadow-lg">
              <CardBody>
                <button
                  type="button"
                  class="btn btn-icon btn-soft-primary float-end"
                  data-bs-toggle="button"
                  aria-pressed="true"
                >
                  <i class="mdi mdi-cards-heart fs-16"></i>
                </button>
                <div class="avatar-sm mb-4">
                  <div class="avatar-title bg-secondary-subtle rounded">
                    <img src={img1} alt="" class="avatar-xxs" />
                  </div>
                </div>
                <Link href={null}>
                  <h5>New Web designer</h5>
                </Link>
                <p class="text-muted">Themesbrand</p>

                <div class="d-flex gap-4 mb-3">
                  <div>
                    <i class="ri-map-pin-2-line text-primary me-1 align-bottom"></i>{" "}
                    Escondido,California
                  </div>

                  <div>
                    <i class="ri-time-line text-primary me-1 align-bottom"></i>{" "}
                    3 min ago
                  </div>
                </div>

                <p class="text-muted">
                  As NavLink Product Designer, you will work within NavLink
                  Product Delivery Team fused with UX, engineering, product
                  and data talent.
                </p>

                <div class="hstack gap-2">
                  <span class="badge badge-soft-success">
                    Full Time
                  </span>
                  <span class="badge badge-soft-primary">
                    Freelance
                  </span>
                  <span class="badge badge-soft-danger">Urgent</span>
                </div>

                <div class="mt-4 hstack gap-2">
                  <Link href={null} class="btn btn-soft-primary w-100">
                    Apply Job
                  </Link>
                  <Link href={null} class="btn btn-soft-success w-100">
                    Overview
                  </Link>
                </div>
              </CardBody>
            </Card>
            <Card class="shadow-lg mb-0 features-company-widgets bg-secondary rounded-3 card-bg-fill">
              <CardBody>
                <h5 class="text-white fs-16 mb-4">
                  10,000+ Featured Companies
                </h5>

                <div class="d-flex gap-1">
                  <Link href={null} id="abc">
                    <Tooltip placement="top" target="abc">
                      Brent Gonzalez
                    </Tooltip>
                    <div class="avatar-xs">
                      <div class="avatar-title bg-light bg-opacity-25 rounded-circle">
                        <img src={img5} alt="" height="15" />
                      </div>
                    </div>
                  </Link>
                  <Link href={null} id="abs">
                    <Tooltip placement="top" target="abs">
                      Brent Gonzalez
                    </Tooltip>
                    <div class="avatar-xs">
                      <div class="avatar-title bg-light bg-opacity-25 rounded-circle">
                        <img src={img2} alt="" height="15" />
                      </div>
                    </div>
                  </Link>
                  <Link href={null} id="brent">
                    <Tooltip placement="top" target="brent">
                      Brent Gonzalez
                    </Tooltip>
                    <div class="avatar-xs">
                      <div class="avatar-title bg-light bg-opacity-25 rounded-circle">
                        <img src={img8} alt="" height="15" />
                      </div>
                    </div>
                  </Link>
                  <Link href={null} id="ellen">
                    <Tooltip placement="top" target="ellen">
                      Ellen Smith
                    </Tooltip>
                    <div class="avatar-xs">
                      <div class="avatar-title bg-light bg-opacity-25 rounded-circle">
                        <img src={img7} alt="" height="15" />
                      </div>
                    </div>
                  </Link>
                  <Link href={null} id="more">
                    <Tooltip placement="top" target="more">
                      More Companies
                    </Tooltip>
                    <div class="avatar-xs">
                      <div class="avatar-title fs-11 rounded-circle bg-light bg-opacity-25 text-white">
                        1k+
                      </div>
                    </div>
                  </Link>
                </div>
              </CardBody>
            </Card>
          </div>
        </Col>
      </Row>
    </Container>
  </section>