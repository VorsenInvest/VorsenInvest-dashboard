<script>
	//Import Components
	import { Container,Dropdown,
        DropdownToggle,
        DropdownMenu,
        DropdownItem, } from "sveltestrap";
	import VerticalLayout from "./VerticalLayout.svelte";
	import HorizontalLayout from "./HorizontalLayout.svelte";
	import TwoColumnLayout from "./TwoColumnLayout.svelte";
	import avatar1 from '../assets/images/users/avatar-1.jpg';
	import { goto,invalidateAll } from '$app/navigation';

	const logout = async  function () {
		await invalidateAll();
		localStorage.removeItem('authUser');
		goto('/authentication/login');
	}

	function removesidebar() {
		document.body.classList.remove("vertical-sidebar-enable");
	}
	
	export let layoutType;
	import logosm from '../assets/images/logo-sm.png'
	import logodark from '../assets/images/logo-dark.png'
	import logolight from '../assets/images/logo-light.png'

	const verticalSidebarClass = () =>{
        if (document.documentElement.getAttribute('data-sidebar-size') === 'sm-hover') {
            document.documentElement.setAttribute('data-sidebar-size', 'sm-hover-active');
            } else if (document.documentElement.getAttribute('data-sidebar-size') === 'sm-hover-active') {
            document.documentElement.setAttribute('data-sidebar-size', 'sm-hover');
            } else {
            document.documentElement.setAttribute('data-sidebar-size', 'sm-hover');
        }
     }
</script>
<svelte:head>
	<script src="//unpkg.com/simplebar@latest/dist/simplebar.min.js"></script>
	<script src="//cdn.jsdelivr.net/npm/simplebar@latest/dist/simplebar.min.js"></script>
</svelte:head>
<div class="app-menu navbar-menu">
	<!-- LOGO -->
	<div class="navbar-brand-box">
		<!-- Dark Logo-->
		<a href="/#" class="logo logo-dark">
			<span class="logo-sm">
				<img src={logosm} alt="" height="22" />
			</span>
			<span class="logo-lg">
				<img
					src={logodark}
					alt=""
					height="17"
				/>
			</span>
		</a>
		<!-- Light Logo-->
		<a href="/#" class="logo logo-light">
			<span class="logo-sm">
				<img src={logosm} alt="" height="22" />
			</span>
			<span class="logo-lg">
				<img
					src={logolight}
					alt=""
					height="17"
				/>
			</span>
		</a>
		<button
		type="button"
		class="btn btn-sm p-0 fs-20 header-item float-end btn-vertical-sm-hover"
		id="vertical-hover"
		on:click="{verticalSidebarClass}"
	>
		<i class="ri-record-circle-line" />
	</button>
	</div>

	{#if layoutType === "horizontal"}
		<div id="scrollbar">
			<div class="container-fluid">
				<div id="two-column-menu" />
				<ul class="navbar-nav" id="navbar-nav">
					<HorizontalLayout />
				</ul>
			</div>
			<!-- Sidebar -->
		</div>
	{:else if layoutType === "twocolumn"}
		<TwoColumnLayout {layoutType} />
	{:else}
			
		<Dropdown class="sidebar-user m-1 rounded">
			<DropdownToggle type="button" color="" class="btn material-shadow-none" id="page-header-user-dropdown">
				<span class="d-flex align-items-center gap-2">
					<img class="rounded header-profile-user" src={avatar1} alt="Header Avatar">
					<span class="text-start">
						<span class="d-block fw-medium sidebar-user-name-text">Anna Adame</span>
						<span class="d-block fs-14 sidebar-user-name-sub-text"><i class="ri ri-circle-fill fs-10 text-success align-baseline"></i> <span class="align-middle">Online</span></span>
					</span>
				</span>
			</DropdownToggle>
			<DropdownMenu end>
				<h6 class="dropdown-header">Welcome Anna!</h6>
				<DropdownItem href="/pages/profile/simple"><i
						class="mdi mdi-account-circle text-muted fs-16 align-middle me-1" /> <span
						class="align-middle">Profile</span></DropdownItem>
				<DropdownItem href="/apps-chat"><i class="mdi mdi-message-text-outline text-muted fs-16 align-middle me-1" />
					<span class="align-middle">Messages</span>
				</DropdownItem>
				<DropdownItem href="/tasks/apps-tasks-kanban"><i
						class="mdi mdi-calendar-check-outline text-muted fs-16 align-middle me-1" />
					<span class="align-middle">Taskboard</span>
				</DropdownItem>
				<DropdownItem href="/pages/faqs"><i class="mdi mdi-lifebuoy text-muted fs-16 align-middle me-1" />
					<span class="align-middle">Help</span>
				</DropdownItem>
				<div class="dropdown-divider" />
				<DropdownItem href="/pages/profile/simple"><i class="mdi mdi-wallet text-muted fs-16 align-middle me-1" />
					<span class="align-middle">Balance : <b>$5971.67</b></span>
				</DropdownItem>
				<DropdownItem href="/pages/profile/simple"><span
						class="badge bg-success-subtle text-success mt-1 float-end">New</span><i
						class="mdi mdi-cog-outline text-muted fs-16 align-middle me-1" /> <span
						class="align-middle">Settings</span></DropdownItem>
				<DropdownItem href="/authenticationInner/lockscreen/auth-lockscreen-basic"><i
						class="mdi mdi-lock text-muted fs-16 align-middle me-1" />
					<span class="align-middle">Lock screen</span>
				</DropdownItem>
				<DropdownItem href={null} on:click={logout}><i
						class="mdi mdi-logout text-muted fs-16 align-middle me-1" />
					<span class="align-middle" data-key="t-logout">Logout</span>
				</DropdownItem>
			</DropdownMenu>
		</Dropdown>
		<div id="scrollbar" data-simplebar class="h-100">
			<Container fluid>
				<div id="two-column-menu" />
				<ul class="navbar-nav" id="navbar-nav">
					<VerticalLayout />
				</ul>
			</Container>
		</div>
	{/if}

	<div class="sidebar-background"></div>
</div>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="vertical-overlay" on:click|self={removesidebar} />