<script>
    import { browser } from "$app/environment"
    import { onMount } from "svelte";
    import Navbar from './navbar.svelte';
    import Home from './home.svelte';
    import Connect from './Connect.svelte';
    import Products from "./Products.svelte";
    import Features from './Features.svelte';
    import Trending from "./Trending.svelte";
    import DiscoverItems from "./DiscoverItems.svelte";
    import TopCreator from "./TopCreator.svelte";
    import CTA from './CTA.svelte';
    import Footer from "./footer.svelte";

    onMount(() => {
        if (browser) {
            window.onscroll = function () {
                scrollFunction();
            };
        }
    });

    const scrollFunction = () => {
        const element = document.getElementById("back-to-top");
        if (element) {
            if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
                element.style.display = "block";
            } else {
                element.style.display = "none";
            }
        }
    };

    const toTop = () => {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    };
</script>
<svelte:head>
	<title>Landing | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="layout-wrapper landing">
    <Navbar />
    <Home />
    <Connect />
    <Products />
    <Features />
    <Trending />
    <DiscoverItems />
    <TopCreator />
    <CTA />
    <Footer />
    <button on:click={() => toTop()} class="btn btn-danger btn-icon landing-back-top" id="back-to-top">
        <i class="ri-arrow-up-line"></i>
    </button>
</div>