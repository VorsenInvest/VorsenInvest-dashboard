<script>
  import { Container, Row } from "sveltestrap";
  import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
  import UsersByDevice from "../../dashboard-analytics/UsersByDevice.svelte";
  import JobSummary from "./JobSummary.svelte";
  import NatworkSummary from "./NatworkSummary.svelte";
  import VisitorGraph from "./VisitorGraph.svelte";
  import Widgets from "./Widgets.svelte";
</script>

<svelte:head>
  <title>Statistics | Velzon - Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
  <Container fluid>
    <BreadCrumb title="STATISTICS" pageTitle="Jobs" />

    <Row class="row">
      <Widgets dataColors={["--vz-success", "--vz-danger"]} />
    </Row>

    <Row class="row">
      <VisitorGraph
        dataColors={[
          "--vz-primary",
          "--vz-danger",
          "--vz-secondary",
          "--vz-success",
          "--vz-warning",
          "--vz-success",
        ]}
      />
      <UsersByDevice />
    </Row>

    <Row class="row">
      <NatworkSummary dataColors={["--vz-primary", "--vz-secondary"]} />
      <JobSummary
        dataColors={[
          "--vz-info",
          "--vz-secondary",
          "--vz-primary",
          "--vz-danger",
        ]}
      />
    </Row>
  </Container>
</div>
