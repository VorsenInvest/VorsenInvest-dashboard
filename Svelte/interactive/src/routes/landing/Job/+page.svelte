<svelte:head>
  <title>Job Landing | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import { browser } from "$app/environment"
    import { onMount } from "svelte";
    import Blog from "./Blog.svelte";
    import Candidates from "./Candidates.svelte";
    import Categories from "./Categories.svelte";
    import Features from "./Features.svelte";
    import FindJob from "./FindJob.svelte";
    import Footer from "./Footer.svelte";
    import Home from "./Home.svelte";
    import Navbar from "./Navbar.svelte";
    import Process from "./Process.svelte";

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
        if (
            document.body.scrollTop > 100 ||
            document.documentElement.scrollTop > 100
        ) {
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
<div class="layout-wrapper landing">
    <Navbar />
    <Home />
    <Process />
    <Features />
    <Categories />
    <FindJob />
    <Candidates />
    <Blog />
    <Footer />
    <button
      on:click={() => toTop()}
      class="btn btn-danger btn-icon landing-back-top"
      id="back-to-top"
    >
      <i class="ri-arrow-up-line"></i>
    </button>
  </div>