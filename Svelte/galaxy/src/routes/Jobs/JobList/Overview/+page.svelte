<svelte:head>
  <title>Job Overview | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import { Col, Container, Row } from "sveltestrap";
    import Header from "./Header.svelte";
    import JobDescription from "./JobDescription.svelte";
    import RelatedJobs from "./RelatedJobs.svelte";
    import RightSection from "./RightSection.svelte";
</script>
<div class="page-content">
    <Container fluid>

      <Row>
        <Header />
      </Row>

      <Row>
        <Col xxl={9}>
          <JobDescription />

          <RelatedJobs />
        </Col>
        <Col xxl={3}>
          <RightSection />
        </Col>
      </Row>
    </Container>
  </div>