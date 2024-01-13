<script>
    import { Collapse, Container, NavbarToggler, NavLink } from "sveltestrap";
    import Link from "svelte-link";
    import { browser } from "$app/environment"

    // Import Images
    import logodark from "../../../assets/images/logo-dark.png";
    import logolight from "../../../assets/images/logo-light.png";
    import { onMount } from "svelte";
    
    let navClass = '';
    let isOpen = true
    onMount(() => {
        if (browser) {
            window.addEventListener("scroll", scrollNavigation, true);
        }
    });
    const toggle = () => {isOpen = !isOpen};

const scrollNavigation = () => {
    var scrollup = document.documentElement.scrollTop;
    if (scrollup > 50) {
        navClass = "is-sticky";
    } else {
        navClass = '';
    }
}
</script>
<nav class={"navbar navbar-expand-lg navbar-landing navbar-light fixed-top " + navClass} id="navbar">
    <Container>
        <Link class="navbar-brand" href="/dashboard">
            <img src={logodark} class="card-logo card-logo-dark" alt="logo dark" height="17" />
            <img src={logolight} class="card-logo card-logo-light" alt="logo light" height="17" />
        </Link>

        <NavbarToggler class="navbar-toggler py-0 fs-20 text-body" on:click={toggle} type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
            aria-expanded="false" aria-label="Toggle navigation">
            <i class="mdi mdi-menu"></i>
        </NavbarToggler>

        <Collapse
            class="navbar-collapse"
            id="navbarSupportedContent"
            {isOpen}
        >
            <div
                class="navbar-nav mx-auto mt-2 mt-lg-0 active"
                id="navbar-example"
            >
                <li class="nav-item">
                    <NavLink class="fs-15" href="#hero">Home</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-15" href="#wallet">Wallet</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-15" href="#marketplace">Marketplace</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-15" href="#categories">Categories</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-15" href="#creators">Creators</NavLink>
                </li>
            </div>

            <div class="">
                <Link href="//crypto/mywallet" class="btn btn-success">Wallet Connect </Link>
            </div>
        </Collapse>
    </Container>
</nav>
<div class="bg-overlay bg-overlay-pattern"></div>