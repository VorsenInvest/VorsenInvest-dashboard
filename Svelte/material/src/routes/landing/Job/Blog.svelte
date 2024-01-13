<script>
    import { Button, Card, CardBody, Col, Container, Row , NavLink} from "sveltestrap";
    import img8 from "../../../assets/images/small/img-8.jpg";
    import img6 from "../../../assets/images/small/img-6.jpg";
    import img9 from "../../../assets/images/small/img-9.jpg";
</script>
<section class="section" id="blog">
    <Container>
      <Row class="justify-content-center">
        <Col class="col-lg-8">
          <div class="text-center mb-5">
            <h1 class="mb-3 ff-secondary fw-semibold text-capitalize lh-base">
              Our Latest <span class="text-primary">News</span>
            </h1>
            <p class="text-muted mb-4">
              We thrive when coming up with innovative ideas but also
              understand that NavLink smart concept should be supported with
              faucibus sapien odio measurable results.
            </p>
          </div>
        </Col>
      </Row>

      <Row>
        <Col class="col-lg-4 col-md-6">
          <Card>
            <CardBody>
              <img src={img8} alt="" class="img-fluid rounded" />
            </CardBody>
            <CardBody>
              <ul class="list-inline fs-14 text-muted">
                <li class="list-inline-item">
                  <i class="ri-calendar-line align-bottom me-1"></i> 30
                  Oct, 2021
                </li>
                <li class="list-inline-item">
                  <i class="ri-message-2-line align-bottom me-1"></i>{" "}
                  364 Comment
                </li>
              </ul>
              <NavLink href={null}>
                <h5>Design your apps in your own way ?</h5>
              </NavLink>
              <p class="text-muted fs-14">
                One disadvantage of Lorum Ipsum is that in Latin layouts
                certain letters appear more frequently than others.
              </p>

              <div>
                <NavLink href={null} class="link-success">
                  Learn More{" "}
                  <i class="ri-arrow-right-line align-bottom ms-1"></i>
                </NavLink>
              </div>
            </CardBody>
          </Card>
        </Col>
        <Col class="col-lg-4 col-md-6">
          <Card>
            <CardBody>
              <img src={img6} alt="" class="img-fluid rounded" />
            </CardBody>
            <CardBody>
              <ul class="list-inline fs-14 text-muted">
                <li class="list-inline-item">
                  <i class="ri-calendar-line align-bottom me-1"></i> 02
                  Oct, 2021
                </li>
                <li class="list-inline-item">
                  <i class="ri-message-2-line align-bottom me-1"></i>{" "}
                  245 Comment
                </li>
              </ul>
              <NavLink href={null}>
                <h5>Smartest applications for business ?</h5>
              </NavLink>
              <p class="text-muted fs-14">
                Due to its widespread use as filler text for layouts,
                non-readability is of great importance: human perception.
              </p>

              <div>
                <NavLink href={null} class="link-success">
                  Learn More{" "}
                  <i class="ri-arrow-right-line align-bottom ms-1"></i>
                </NavLink>
              </div>
            </CardBody>
          </Card>
        </Col>
        <Col class="col-lg-4 col-md-6">
          <Card>
            <CardBody>
              <img src={img9} alt="" class="img-fluid rounded" />
            </CardBody>
            <CardBody>
              <ul class="list-inline fs-14 text-muted">
                <li class="list-inline-item">
                  <i class="ri-calendar-line align-bottom me-1"></i> 23
                  Sept, 2021
                </li>
                <li class="list-inline-item">
                  <i class="ri-message-2-line align-bottom me-1"></i>{" "}
                  354 Comment
                </li>
              </ul>
              <NavLink href={null}>
                <h5>How apps is changing the IT world</h5>
              </NavLink>
              <p class="text-muted fs-14">
                Intrinsically incubate intuitive opportunities and real-time
                potentialities Appropriately communicate one-to-one
                technology.
              </p>

              <div>
                <NavLink href={null} class="link-success">
                  Learn More{" "}
                  <i class="ri-arrow-right-line align-bottom ms-1"></i>
                </NavLink>
              </div>
            </CardBody>
          </Card>
        </Col>
      </Row>
    </Container>
  </section>
  <section class="py-5 bg-info position-relative">
    <div class="bg-overlay bg-overlay-pattern opacity-50"></div>
    <Container>
      <Row class="align-items-center gy-4">
        <Col class="col-sm">
          <div>
            <h4 class="text-white fw-semibold">
              Get New Jobs Notification!
            </h4>
            <p class="text-white text-opacity-75 mb-0">
              Subscribe & get all related jobs notification.
            </p>
          </div>
        </Col>
        <Col class="col-sm-auto">
          <Button class="btn btn-danger" type="button">
            Subscribe Now{" "}
            <i class="ri-arrow-right-line align-bottom"></i>
          </Button>
        </Col>
      </Row>
    </Container>
  </section>