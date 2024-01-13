<script>
    import BreadCrumb from '../../../../Components/Common/BreadCrumb.svelte';
    import { Container } from 'sveltestrap';
    import InvoiceAction from "./InvoiceAction.svelte";
    import FeedbackAction from "./FeedbackAction.svelte";
    import RatingTemplate from "./RatingTemplate.svelte";
</script>
<svelte:head>
	<title>Ecommerce Action | Velzon - Svelte Admin & Dashboard Template</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Ecommerce Action" pageTitle="Email" />
        <InvoiceAction />
        <FeedbackAction />
        <RatingTemplate />
    </Container>
</div>