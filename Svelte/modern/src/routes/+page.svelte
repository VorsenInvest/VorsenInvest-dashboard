<script>
	import { goto } from '$app/navigation';
	import {onMount} from 'svelte';

	onMount(async () => {
        await goto("/dashboard");
    });
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>

</section>