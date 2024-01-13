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
      <VisitorGraph dataColors={["--vz-primary", "--vz-primary-rgb, 0.65", "--vz-secondary", "--vz-secondary-rgb, 0.75","--vz-primary-rgb, 0.4", "--vz-success"]} />
      <UsersByDevice />
    </Row>

    <Row class="row">
      <NatworkSummary dataColors={["--vz-primary", "--vz-secondary"]} />
      <JobSummary dataColors={["--vz-success","--vz-primary", "--vz-info", "--vz-danger"]} />
    </Row>
  </Container>
</div>