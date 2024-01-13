<svelte:head>
  <title>Task Details | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
import { Container, Col, Row } from 'sveltestrap';
import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
import Comments from '../Comments.svelte';
import Summary from '../Summary.svelte';
import TimeTracking from "../TimeTracking.svelte";
</script>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Tasks Details" pageTitle="Tasks" />

        <Row>
            <Col xxl={3}>
                <TimeTracking />
            </Col>
            <Col xxl={9}>
                <Summary />
                <Comments />
            </Col>
        </Row>

    </Container>
</div>