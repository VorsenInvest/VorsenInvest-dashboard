<svelte:head>
  <title>Statistics | Velzon -  Admin & Dashboard Template</title>
</svelte:head>
<script>
    import { Container, Row } from "sveltestrap";
    import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
    import UsersByDevice from "../../dashboard-analytics/UsersByDevice.svelte";
    import JobSummary from "./JobSummary.svelte";
    import NatworkSummary from "./NatworkSummary.svelte";
    import VisitorGraph from "./VisitorGraph.svelte";
    import Widgets from "./Widgets.svelte";
</script>

<div class="page-content">
  <Container fluid>
    <BreadCrumb title="STATISTICS" pageTitle="Jobs" />

    <Row class="row">
      <Widgets dataColors={["--vz-success", "--vz-danger"]} />
    </Row>

    <Row class="row">
      <VisitorGraph dataColors={["--vz-danger", "--vz-success", "--vz-warning", "--vz-info","--vz-secondary", "--vz-primary"]} />
      <UsersByDevice />
    </Row>

    <Row class="row">
      <NatworkSummary dataColors={["--vz-secondary", "--vz-info"]} />
      <JobSummary dataColors={["--vz-success","--vz-primary", "--vz-info", "--vz-danger"]} />
    </Row>
  </Container>
</div>