<script>
	import { page } from "$app/stores";
	import { browser } from "$app/environment";
	// import fakeBackend from '../helpers/AuthType/fakeBackend';
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";

	let user = browser && localStorage.authUser;

	onMount(() => {
		if (!user) {
			goto("/authentication/login");
		}
	});

	const publicRoutes = [
		"/authenticationInner/login/auth-signin-basic",
		"/authenticationInner/login/auth-signin-cover",
		"/authenticationInner/register/auth-signup-basic",
		"/authenticationInner/register/auth-signup-cover",
		"/authenticationInner/passwordreset/auth-pass-reset-basic",
		"/authenticationInner/passwordreset/auth-pass-reset-cover",
		"/authenticationInner/lockscreen/auth-lockscreen-basic",
		"/authenticationInner/lockscreen/auth-lockscreen-cover",
		"/authenticationInner/passwordcreate/auth-pass-change-basic",
		"/authenticationInner/passwordcreate/auth-pass-change-cover",
		"/authenticationInner/logout/auth-logout-basic",
		"/authenticationInner/logout/auth-logout-cover",
		"/authenticationInner/successmessage/auth-success-msg-basic",
		"/authenticationInner/successmessage/auth-success-msg-cover",
		"/authenticationInner/twostepverification/auth-twostep-basic",
		"/authenticationInner/twostepverification/auth-twostep-cover",
		"/authenticationInner/errors/auth-404-basic",
		"/authenticationInner/errors/auth-404-cover",
		"/authenticationInner/errors/auth-404-alt",
		"/authenticationInner/errors/auth-500",
		"/authenticationInner/errors/auth-offline",
		"/pages/pages-maintenance",
		"/pages/pages-coming-soon",
		"/landing/OnePage",
		"/landing/Job",
		"/landing/NFTLanding",
		"/authentication/login",
	];

	$: isPublic = isPublicRoute($page.url.pathname);

	function isPublicRoute(url) {
		if (url.endsWith("/")) {
			// Remove the last character (slash)
			url = url.slice(0, -1);
		}
		return publicRoutes.includes(url);
	}

	import { addMessages, init, getLocaleFromNavigator } from "svelte-i18n";

	import Sidebar from "../Layouts/Sidebar.svelte";
	import Header from "../Layouts/Header.svelte";
	import Footer from "../Layouts/Footer.svelte";
	import Rightbar from "../Components/Common/RightSidebar.svelte";

	let open = false;
	let headerClass = "";
	let layoutType = "vertical";

	init({
		fallbackLocale: "en",
		initialLocale: getLocaleFromNavigator(),
	});
	onMount(() => {
		if (browser) {
			window.addEventListener("scroll", scrollNavigation, true);
		}
		setTimeout(() => {
			document.getElementById("preloader").style.visibility = "hidden";
			document.getElementById("preloader").style.opacity = "0";
		}, 350);
	});

	function scrollNavigation() {
		var scrollup = document.documentElement.scrollTop;
		if (scrollup > 50) {
			headerClass = "topbar-shadow";
		} else {
			headerClass = "";
		}
	}

</script>

<svelte:head>
	<script src="//cdn.jsdelivr.net/npm/apexcharts"></script>
	<script src="//cdn.lordicon.com/xdjxvujz.js"></script>
	<script src="https://cdn.jsdelivr.net/npm/jsvectormap"></script>
	<script
		src="https://cdn.jsdelivr.net/npm/jsvectormap/dist/maps/world.js"
	></script>
</svelte:head>
<div id="preloader">
	<div id="status">
		<div class="spinner-border text-primary avatar-sm" role="status">
			<span class="visually-hidden">Loading...</span>
		</div>
	</div>
</div>
{#if isPublic}
	<slot />
{:else}
	<div id="layout-wrapper">
		<Header {headerClass} />
		<Sidebar {layoutType} />
		<div class="main-content" id="maincontent">
			<slot />
			<Footer />
		</div>
		<Rightbar bind:open {layoutType} />
	</div>
{/if}

<style lang="scss">
	@import "../assets/scss/themes.scss";
</style>
