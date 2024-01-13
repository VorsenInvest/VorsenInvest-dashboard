<script>
    import { browser } from "$app/environment"
    import { onMount } from "svelte";
    import { Collapse, Container, NavbarToggler, NavLink } from "sveltestrap";
    import LogoDark from "../../../assets/images/logo-dark.png";
    import LogoLight from "../../../assets/images/logo-light.png";
    import Link from 'svelte-link';
    var navClass = '';
    let isOpen = true
    const toggle = () => isOpen = !isOpen;

    onMount(() => {
        if (browser) {
            window.addEventListener("scroll", scrollNavigation, true);
        }
    });
    
    const scrollNavigation = () => {
    var scrollup = document.documentElement.scrollTop;
    if (scrollup > 50) {
      navClass = " is-sticky";
    } else {
        navClass = '';
    }
  };
</script>

<nav
    class={"navbar navbar-expand-lg navbar-landing fixed-top job-navbar" +
        navClass}
    id="navbar"
>
    <Container fluid class="custom-container">
        <Link class="navbar-brand" href="/dashboard">
            <img
                src={LogoDark}
                class="card-logo card-logo-dark"
                alt="logo dark"
                height="17"
            />
            <img
                src={LogoLight}
                class="card-logo card-logo-light"
                alt="logo light"
                height="17"
            />
        </Link>
        <NavbarToggler
            on:click={toggle}
            class="navbar-toggler py-0 fs-20 text-body"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
        >
            <i class="mdi mdi-menu" />
        </NavbarToggler>

        <Collapse class="navbar-collapse" id="navbarSupportedContent" {isOpen}>
            <nav
                class="navbar-nav mx-auto mt-2 mt-lg-0"
                id="navbar-example"
            >
                <li class="nav-item">
                    <NavLink class="fs-16" href="#hero">Home</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-16" href="#process">Process</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-16" href="#categories">
                        Categories
                    </NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-16" href="#findJob">Find Jobs</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-16" href="#candidates">
                        Candidates
                    </NavLink>
                </li>
                <li class="nav-item">
                    <NavLink class="fs-16" href="#blog">Blog</NavLink>
                </li>
            </nav>

            <div>
                <Link href="/authenticationInner/login/auth-signin-basic" class="btn btn-soft-danger">
                    <i class="ri-user-3-line align-bottom me-1" /> Login & Register
                </Link>
            </div>
        </Collapse>
    </Container>
</nav>