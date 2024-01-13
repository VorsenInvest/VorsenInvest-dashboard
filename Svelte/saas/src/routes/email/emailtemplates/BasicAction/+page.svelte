<script>
	import BreadCrumb from '../../../../Components/Common/BreadCrumb.svelte';
    import { Container } from 'sveltestrap';
    import Basic from './basic.svelte';
    import SubscribeAction from './SubscribeAction.svelte';
    import EmailVerifyAction from "./EmailVerifyAction.svelte";
    import PasswordChangeAction from "./PasswordChangeAction.svelte";
</script>
<svelte:head>
	<title>Basic Action | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Basic Action" pageTitle="Basic Action" />
        <Basic />
        <SubscribeAction />
        <EmailVerifyAction />
        <PasswordChangeAction />
    </Container>
</div>