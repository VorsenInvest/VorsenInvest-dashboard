<script>
  import { Card, CardBody, Col, Container, Row } from "sveltestrap";

  import Avatar10 from "../../../assets/images/users/avatar-10.jpg";
  import About from "../../../assets/images/about.jpg";
  import Link from "svelte-link";
</script>

<section class="section">
  <Container>
    <Row
      class="align-items-center justify-content-lg-between justify-content-center gy-4"
    >
      <Col lg={5} sm={7}>
        <div class="about-img-section mb-5 mb-lg-0 text-center">
          <Card
            class="card-bg-fill rounded shadow-lg inquiry-box d-none d-lg-block"
          >
            <CardBody class="d-flex align-items-center">
              <div class="avatar-sm flex-shrink-0 me-3">
                <div
                  class="avatar-title bg-secondary-subtle text-secondary rounded-circle fs-18"
                >
                  <i class="ri-briefcase-2-line" />
                </div>
              </div>
              <h5 class="fs-15 lh-base mb-0">
                Search Over{" "}
                <span class="text-secondary fw-semibold">1,00,000+</span>{" "}
                Jobs
              </h5>
            </CardBody>
          </Card>

          <Card class="feedback-box">
            <CardBody class="d-flex shadow-lg">
              <div class="flex-shrink-0 me-3">
                <img src={Avatar10} alt="" class="avatar-sm rounded-circle" />
              </div>
              <div class="flex-grow-1">
                <h5 class="fs-14 lh-base mb-0">Tonya Noble</h5>
                <p class="text-muted fs-11 mb-1">UI/UX Designer</p>

                <div class="text-warning">
                  <i class="ri-star-s-fill" />
                  <i class="ri-star-s-fill" />
                  <i class="ri-star-s-fill" />
                  <i class="ri-star-s-fill" />
                  <i class="ri-star-s-line" />
                </div>
              </div>
            </CardBody>
          </Card>
          <img src={About} alt="" class="img-fluid mx-auto rounded-3" />
        </div>
      </Col>
      <Col lg={6}>
        <div class="text-muted">
          <h1 class="mb-3 lh-base">
            Find Your <span class="text-primary">Dream Job</span> in One Place
          </h1>
          <p class="ff-secondary fs-16 mb-2">
            The first step in finding your <b>dream job </b> is deciding where to
            look for first-hand insight. Contact professionals who are already working
            in industries or positions that interest you.
          </p>
          <p class="ff-secondary fs-16">
            Schedule informational interviews and phone calls or ask for the
            opportunity to shadow them on the job.
          </p>

          <div class="vstack gap-2 mb-4 pb-1">
            <div class="d-flex align-items-center">
              <div class="flex-shrink-0 me-2">
                <div class="avatar-xs icon-effect">
                  <div
                    class="avatar-title bg-transparent text-success rounded-circle h2"
                  >
                    <i class="ri-check-fill" />
                  </div>
                </div>
              </div>
              <div class="flex-grow-1">
                <p class="mb-0">Dynamic Conetnt</p>
              </div>
            </div>
            <div class="d-flex align-items-center">
              <div class="flex-shrink-0 me-2">
                <div class="avatar-xs icon-effect">
                  <div
                    class="avatar-title bg-transparent text-success rounded-circle h2"
                  >
                    <i class="ri-check-fill" />
                  </div>
                </div>
              </div>
              <div class="flex-grow-1">
                <p class="mb-0">Setup plugin's information.</p>
              </div>
            </div>
            <div class="d-flex align-items-center">
              <div class="flex-shrink-0 me-2">
                <div class="avatar-xs icon-effect">
                  <div
                    class="avatar-title bg-transparent text-success rounded-circle h2"
                  >
                    <i class="ri-check-fill" />
                  </div>
                </div>
              </div>
              <div class="flex-grow-1">
                <p class="mb-0">Themes customization information</p>
              </div>
            </div>
          </div>

          <div>
            <Link href={null} class="btn btn-primary">
              Find Your Jobs{" "}
              <i class="ri-arrow-right-line align-bottom ms-1" />
            </Link>
          </div>
        </div>
      </Col>
    </Row>
  </Container>
</section>
