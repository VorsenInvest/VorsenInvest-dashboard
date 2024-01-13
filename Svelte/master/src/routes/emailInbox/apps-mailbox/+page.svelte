<script>
	import { Container } from "sveltestrap";
	import EmailSidebar from "../EmailSidebar.svelte";
	import EmailToolbar from "../EmailToolbar.svelte";
</script>

<svelte:head>
	<title>Mailbox | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<div class="email-wrapper d-lg-flex gap-1 mx-n4 mt-n4 p-1">
			<EmailSidebar />
			<EmailToolbar />
		</div>
	</Container>
</div>
