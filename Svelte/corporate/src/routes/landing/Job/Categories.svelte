<script>
    import { Card, CardBody, Col, Container, Row } from "sveltestrap";
    import categories from "../../../common/data/jobLanding";
    import Link from 'svelte-link';
</script>
<section class="section bg-light" id="categories">
    <Container>
      <Row class="justify-content-center">
        <Col lg={7} >
          <div class="text-center mb-5">
            <h1 class="mb-3 ff-secondary fw-semibold text-capitalize lh-base">
              High demand jobs{" "}
              <span class="text-primary">Categories</span> Featured
            </h1>
            <p class="text-muted">
              Post a job to tell us about your project. We'll quickly match
              you with the right freelancers.
            </p>
          </div>
        </Col>
      </Row>

      <Row class="justify-content-center">
        {#each categories.categories as item}
          <Col lg={3} md={6}>
            <Card class="shadow-none text-center py-3">
              <CardBody class="py-4">
                <div class="avatar-sm position-relative mb-4 mx-auto">
                  <div class="job-icon-effect"></div>
                  <div class="avatar-title bg-transparent text-success rounded-circle">
                    <i class={item.icon}></i>
                  </div>
                </div>
                <Link href={null} class="to-link">
                  <h5 class="fs-17 pt-1">{item.lable}</h5>
                </Link>
                <p class="mb-0 text-muted">{item.jobs}</p>
              </CardBody>
            </Card>
          </Col>
        {/each}
      </Row>
    </Container>
</section>
<section class="py-5 bg-primary position-relative">
    <div class="bg-overlay bg-overlay-pattern opacity-50"></div>
    <Container>
        <Row class="align-items-center gy-4">
        <Col class="col-sm">
            <div>
            <h4 class="text-white mb-2">Ready to Started?</h4>
            <p class="text-white-50 mb-0">
                Create new account and refer your friend
            </p>
            </div>
        </Col>
        <Col class="col-sm-auto">
            <div>
            <Link href={null} class="btn bg-gradient btn-secondary">
                Create Free Account
            </Link>
            </div>
        </Col>
        </Row>
    </Container>
</section>