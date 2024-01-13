<script>
	export let code,id;
	import { onMount } from "svelte";

	import { browser } from "$app/environment";
	onMount(async () => {
		if (browser) {
}			document.getElementById(id).insertAdjacentText('beforeend',code);
	});
</script>

<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
<pre class="language-markup" style="max-height: 352px;" tabindex="0"><code class="language-markup" id={id}></code></pre>