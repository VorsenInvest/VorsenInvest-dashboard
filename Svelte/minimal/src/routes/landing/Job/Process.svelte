<script>
    import { Card, CardBody, Col, Container, Row } from "sveltestrap";
    import jobProcess from "../../../common/data/jobLanding";
</script>
<section class="section" id="process">
    <Container>
      <Row class="justify-content-center">
        <Col lg={8}>
          <div class="text-center mb-5">
            <h1 class="mb-3 ff-secondary fw-semibold lh-base">
              How <span class="text-primary">it's work</span> creative
              jobs & quickly features
            </h1>
            <p class="text-muted">
              A creative person has the ability to invent and develop
              original ideas, especially in the arts. Like so many creative
              people, he was never satisfied.
            </p>
          </div>
        </Col>
      </Row>
      <Row>
        {#each jobProcess.jobProcess as item,key}
          <Col lg={3} md={6}>
            <Card class={key === 0 ? "card shadow-lg" : "card shadow-none card-border-effect-none "}>
              <CardBody class="p-4">
                <h1 class="fw-bold display-5 ff-secondary mb-4 text-success position-relative">
                  <div class="job-icon-effect"></div>
                  <span>{item.id}</span>
                </h1>
                <h6 class="fs-17 mb-2">{item.lable}</h6>
                <p class="text-muted mb-0 fs-15">{item.desc}</p>
              </CardBody>
            </Card>
          </Col>
        {/each}
      </Row>
    </Container>
  </section>