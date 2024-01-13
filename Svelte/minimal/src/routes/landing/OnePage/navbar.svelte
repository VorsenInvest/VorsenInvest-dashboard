<script>
    import {onMount} from "svelte";
import { Collapse, Container, NavbarToggler, NavLink } from "sveltestrap";
import Link from "svelte-link";

// Import Images
import logodark from "../../../assets/images/logo-dark.png";
import logolight from "../../../assets/images/logo-light.png";
let navClass = "";
let isOpen = true;

onMount(() => {
    window.addEventListener("scroll", scrollNavigation, true);
})

const scrollNavigation = () => {
        var scrollup = document.documentElement.scrollTop;
        if (scrollup > 50) {
            navClass = "is-sticky";
        } else {
            navClass = '';
        }
    }
</script>
<nav class={"navbar navbar-expand-lg navbar-landing fixed-top " + navClass} id="navbar">
    <Container>
        <Link class="navbar-brand" href="/dashboard">
            <img src={logodark} class="card-logo card-logo-dark" alt="logo dark" height="17" />
            <img src={logolight} class="card-logo card-logo-light" alt="logo light" height="17" />
        </Link>

        <NavbarToggler class="navbar-toggler py-0 fs-20 text-body" on:click={() => (isOpen = !isOpen)} type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
            aria-expanded="false" aria-label="Toggle navigation">
            <i class="mdi mdi-menu"></i>
        </NavbarToggler>

        <Collapse
            {isOpen}
            class="navbar-collapse"
            id="navbarSupportedContent"
        >
            <div
                class="navbar-nav mx-auto mt-2 mt-lg-0"
                id="navbar-example"
            >
                <li class="nav-item">
                    <NavLink href="#hero" class="fs-15">Home</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink href="#services" class="fs-15">Services</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink href="#features" class="fs-15">Features</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink href="#plans" class="fs-15">Plans</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink href="#reviews" class="fs-15">Reviews</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink href="#team" class="fs-15">Team</NavLink>
                </li>
                <li class="nav-item">
                    <NavLink href="#contact" class="fs-15">Contact</NavLink>
                </li>
            </div>

            <div class="">
                <Link href="/authenticationInner/login/auth-signin-basic" class="btn btn-link fw-medium text-decoration-none text-dark">Sign
                    in</Link>
                <Link href="/authenticationInner/register/auth-signup-basic" class="btn btn-primary">Sign Up</Link>
            </div>
        </Collapse>
    </Container>
</nav>