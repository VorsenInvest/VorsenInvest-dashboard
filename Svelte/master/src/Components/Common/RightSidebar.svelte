<script>
	import { onMount } from "svelte";
	import { Label, Collapse } from "sveltestrap";
	import { browser } from "$app/environment";
	import 'overlayscrollbars/overlayscrollbars.css';
	import { theme, setTheme } from "$lib/theme";
	import { themeChangeEvent, triggerThemeChange } from "$lib/eventBus";
	export let open = false;

	export let layoutType;

	//import Images
	import img01 from "../../assets/images/sidebar/img-1.jpg";
	import img02 from "../../assets/images/sidebar/img-2.jpg";
	import img03 from "../../assets/images/sidebar/img-3.jpg";
	import img04 from "../../assets/images/sidebar/img-4.jpg";

	let leftSidebarType = "dark";
	let layoutModeType = "light";
	let layoutWidthType = "fluid";
	let layoutPositionType = "fixed";
	let topbarThemeType = "light";
	let leftsidbarSizeType = "lg";
	let leftSidebarViewType = "default";
	let leftSidebarTypes = "gradient";
	let leftSidebarImageTypes = "none";
	let themeType = "saas";
	let themeColorType = "default";
	let bodyImageType="none";

	let isOpen = false;

	function topFunction() {
		if (browser) {
			document.body.scrollTop = 0;
			document.documentElement.scrollTop = 0;
		}
	}

	// When the user scrolls down 20px from the top of the document, show the button

	onMount(async () => {
		if (browser) {
			changeLayout(layoutType);
			changeLayoutMode(layoutModeType);
			changeLayoutWidth(layoutWidthType);
			changeLeftsidebarSizeType(leftsidbarSizeType);
			changeLayoutPosition(layoutPositionType);
			changeTopbarTheme(topbarThemeType);
			changeLeftsidebarViewType(leftSidebarViewType);
			changeSidebarTheme(leftSidebarType);
			changeTheme(themeType);
			changeSidebarUserProfile(false);
			changeThemeColors(themeColorType);
			changeBodyImage(bodyImageType);

			window.onscroll = function () {
				scrollFunction();
			};

		}
	});

	function changeLayout(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-layout", value);
	}

	function changeLayoutMode(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-bs-theme", value);
	}

	function changeLayoutWidth(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-layout-width", value);
	}

	function changeLeftsidebarSizeType(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-sidebar-size", value);
	}
	function changeLayoutPosition(value) {
		if (document.documentElement)
			document.documentElement.setAttribute(
				"data-layout-position",
				value
			);
	}
	function changeTopbarTheme(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-topbar", value);
	}
	function changeLeftsidebarViewType(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-layout-style", value);
	}
	function changeSidebarTheme(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-sidebar", value);
	}
	function changeTheme(value) { 
		if (document.documentElement)
			document.documentElement.setAttribute("data-theme", value);
		if(browser){
			setTheme(value);
			// Trigger the theme change event
			triggerThemeChange(value);
		}
			
		if(value == "galaxy"){
			document.getElementById("body-img").style.display = "block";
		}else{
			document.getElementById("body-img").style.display = "none";
		}
	}
	function changeThemeColors(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-theme-colors", value);
	}
	function changeBodyImage(value) {
		if (document.documentElement)
			document.documentElement.setAttribute("data-body-image", value);
	}

	function changeBodyAttribute(attribute, value) {
		if (document.documentElement)
			document.documentElement.setAttribute(attribute, value);

			if(attribute == "data-theme"){
				if(value == "galaxy"){
					document.getElementById("body-img").style.display = "block";
				}else{
					document.getElementById("body-img").style.display = "none";
				}
			}
	}

	function changeSidebarUserProfile(checked){
		if(checked){
			document.documentElement.setAttribute("data-sidebar-user-show","");
		}else{
			document.documentElement.removeAttribute("data-sidebar-user-show");
		}
	}

	function scrollFunction() {
		if (browser) {
			var mybutton = document.getElementById("back-to-top");
			if(mybutton != null){
				if (document.body.scrollTop > 100 ||
					document.documentElement.scrollTop > 100
				) {
					mybutton.style.display = "block";
				} else {
					mybutton.style.display = "none";
				}
			}
		}
	}
</script>

<div>
	<button on:click={topFunction} class="btn btn-danger btn-icon" id="back-to-top">
		<i class="ri-arrow-up-line" />
	</button>
	<div class="customizer-setting d-none d-md-block">
		<a href="{null}" class="btn-info rounded-pill shadow-lg btn btn-icon btn-lg p-2" on:click={()=> (open = !open)}
			>
			<i class="mdi mdi-spin mdi-cog-outline fs-22" />
		</a>
	</div>
	<div class="offcanvas offcanvas-end border-0 {open === true ? 'show' : ''}" id="theme-settings-offcanvas"
		style="visibility: visible;" aria-modal="true" role="dialog">
		<div class="d-flex align-items-center bg-primary bg-gradient p-3 offcanvas-header">
			<h5 class="m-0 me-2 text-white">Theme Customizer</h5>

			<button type="button" class="btn-close btn-close-white ms-auto" on:click={()=> (open = false)}
				/>
		</div>
		<div class="offcanvas-body p-0">
			<div data-overlayscrollbars-initialize class="h-100">
				<div class="p-4">

					<div class="form-check form-switch form-switch-md mb-3 mt-4">
						<input type="checkbox" class="form-check-input" id="sidebarUserProfile" on:change={(e) =>changeSidebarUserProfile(e.target.checked) }>
						<label class="form-check-label" for="sidebarUserProfile">Sidebar User Profile Avatar</label>
					</div>
	
					<h6 class="mt-4 mb-0 fw-semibold text-uppercase">Theme</h6>
					<p class="text-muted">Choose your suitable Theme.</p>
	
					<div class="row">
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme01" name="data-theme" type="radio" value="default" class="form-check-input"
								on:change={()=>changeTheme("default")} checked={themeType == "default"}>
								<label class="form-check-label p-0" for="customizer-theme01">
									<img src="https://themesbrand.com/velzon/assets/images/demo/default.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Default</h5>
						</div>
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme02" name="data-theme" type="radio" value="saas" class="form-check-input"
								on:change={()=>changeTheme("saas")} checked={themeType == "saas"}>
								<label class="form-check-label p-0" for="customizer-theme02">
									<img src="https://themesbrand.com/velzon/assets/images/demo//saas.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Sass</h5>
						</div>
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme03" name="data-theme" type="radio" value="corporate" class="form-check-input"
								on:change={()=>changeTheme("corporate")} checked={themeType == "corporate"}>
								<label class="form-check-label p-0" for="customizer-theme03">
									<img src="https://themesbrand.com/velzon/assets/images/demo//corporate.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Corporate</h5>
						</div>
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme04" name="data-theme" type="radio" value="galaxy" class="form-check-input"
								on:change={()=>changeTheme("galaxy")} checked={themeType == "galaxy"}>
								<label class="form-check-label p-0" for="customizer-theme04">
									<img src="https://themesbrand.com/velzon/assets/images/demo//galaxy.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Galaxy</h5>
						</div>
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme05" name="data-theme" type="radio" value="material" class="form-check-input"
								on:change={()=>changeTheme("material")} checked={themeType == "material"}>
								<label class="form-check-label p-0" for="customizer-theme05">
									<img src="https://themesbrand.com/velzon/assets/images/demo//material.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Material</h5>
						</div>
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme06" name="data-theme" type="radio" value="creative" class="form-check-input"
								on:change={()=> changeTheme("creative")} checked={themeType == "creative"}>
								<label class="form-check-label p-0" for="customizer-theme06">
									<img src="https://themesbrand.com/velzon/assets/images/demo/creative.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Creative</h5>
						</div>
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme07" name="data-theme" type="radio" value="minimal" class="form-check-input"
								on:change={()=>changeTheme("minimal")} checked={themeType == "minimal"}>
								<label class="form-check-label p-0" for="customizer-theme07">
									<img src="https://themesbrand.com/velzon/assets/images/demo/minimal.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Minimal</h5>
						</div>
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme08" name="data-theme" type="radio" value="modern" class="form-check-input"
								on:change={()=>changeTheme("modern")} checked={themeType == "modern"}>
								<label class="form-check-label p-0" for="customizer-theme08">
									<img src="https://themesbrand.com/velzon/assets/images/demo/modern.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Modern</h5>
						</div>
						<!-- end col -->
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme09" name="data-theme" type="radio" value="interactive" class="form-check-input"
								on:change={()=>changeTheme("interactive")} checked={themeType == "interactive"}>
								<label class="form-check-label p-0" for="customizer-theme09">
									<img src="https://themesbrand.com/velzon/assets/images/demo/interactive.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Interactive</h5>
						</div><!-- end col -->
	
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme10" name="data-theme" type="radio" value="classic" class="form-check-input"
								on:change={()=>changeTheme("classic")} checked={themeType == "classic"}>
								<label class="form-check-label p-0" for="customizer-theme10">
									<img src="https://themesbrand.com/velzon/assets/images/demo/classic.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Classic</h5>
						</div><!-- end col -->
	
						<div class="col-6">
							<div class="form-check card-radio">
								<input id="customizer-theme11" name="data-theme" type="radio" value="vintage" class="form-check-input"
								on:change={()=>changeTheme("vintage")} checked={themeType == "vintage"}>
								<label class="form-check-label p-0" for="customizer-theme11">
									<img src="https://themesbrand.com/velzon/assets/images/demo/vintage.png" alt="" class="img-fluid">
								</label>
							</div>
							<h5 class="fs-13 text-center fw-medium mt-2">Vintage</h5>
						</div><!-- end col -->
					</div>

					<h6 class="mt-4 mb-0 fw-semibold text-uppercase">
						Color Scheme
					</h6>
					<p class="text-muted">Choose Light or Dark Scheme.</p>

					<div class="colorscheme-cardradio">
						<div class="row">
							<div class="col-4">
								<div class="form-check card-radio">
									<input class="form-check-input" type="radio" name="data-bs-theme"
										id="layout-mode-light" value="light" on:change={()=>
									changeBodyAttribute(
									"data-bs-theme",
									"light"
									)}
									checked={layoutModeType == "light"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="layout-mode-light">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">Light</h5>
							</div>

							<div class="col-4">
								<div class="form-check card-radio dark">
									<input class="form-check-input" type="radio" name="data-bs-theme"
										id="layout-mode-dark" value="dark" on:change={()=>
									changeBodyAttribute(
									"data-bs-theme",
									"dark"
									)}
									checked={layoutModeType == "dark"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 bg-dark material-shadow" for="layout-mode-dark">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-white bg-opacity-10 d-flex h-100 flex-column gap-1 p-1">
													<span
														class="d-block p-1 px-2 bg-white bg-opacity-10 rounded mb-2" />
													<span class="d-block p-1 px-2 pb-0 bg-white bg-opacity-10" />
													<span class="d-block p-1 px-2 pb-0 bg-white bg-opacity-10" />
													<span class="d-block p-1 px-2 pb-0 bg-white bg-opacity-10" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-white bg-opacity-10 d-block p-1" />
													<span class="bg-white bg-opacity-10 d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">Dark</h5>
							</div>
						</div>
					</div>
					{#if layoutType !== "twocolumn"}
					<div id="layout-width">
						<h6 class="mt-4 mb-0 fw-semibold text-uppercase">
							Layout Width
						</h6>
						<p class="text-muted">
							Choose Fluid or Boxed layout.
						</p>

						<div class="row">
							<div class="col-4">
								<div class="form-check card-radio">
									<input class="form-check-input" type="radio" name="data-layout-width"
										id="layout-width-fluid" value="lg" on:change={()=>
									changeBodyAttribute(
									"data-layout-width",
									"lg"
									)}
									checked={layoutWidthType == "lg"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100" for="layout-width-fluid">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Fluid
								</h5>
							</div>
							<div class="col-4">
								<div class="form-check card-radio">
									<input class="form-check-input" type="radio" name="data-layout-width"
										id="layout-width-boxed" value="boxed" on:change={()=>
									changeBodyAttribute(
									"data-layout-width",
									"boxed"
									)}
									checked={layoutWidthType == "boxed"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 px-2 material-shadow" for="layout-width-boxed">
										<span class="d-flex gap-1 h-100 border-start border-end">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Boxed
								</h5>
							</div>
						</div>
					</div>

					<div id="layout-position">
						<h6 class="mt-4 mb-0 fw-semibold text-uppercase">
							Layout Position
						</h6>
						<p class="text-muted">
							Choose Fixed or Scrollable Layout Position.
						</p>

						<div class="btn-group radio" role="group">
							<input type="radio" class="btn-check" name="data-layout-position" id="layout-position-fixed"
								value="fixed" on:change={()=>
							changeBodyAttribute(
							"data-layout-position",
							"fixed"
							)}
							checked={layoutPositionType == "fixed"}
							/>
							<Label class="btn btn-light w-sm" for="layout-position-fixed">Fixed</Label>

							<input type="radio" class="btn-check" name="data-layout-position"
								id="layout-position-scrollable" value="scrollable" on:change={()=>
							changeBodyAttribute(
							"data-layout-position",
							"scrollable"
							)}
							checked={layoutPositionType == "scrollable"}
							/>
							<Label class="btn btn-light w-sm ms-0" for="layout-position-scrollable">Scrollable</Label>
						</div>
					</div>
					{/if}

					<h6 class="mt-4 mb-0 fw-semibold text-uppercase">
						Topbar Color
					</h6>
					<p class="text-muted">Choose Light or Dark Topbar Color.</p>

					<div class="row">
						<div class="col-4">
							<div class="form-check card-radio h-auto">
								<input class="form-check-input" type="radio" name="data-topbar" id="topbar-color-light"
									value="light" on:change={()=>
								changeBodyAttribute(
								"data-topbar",
								"light"
								)}
								checked={topbarThemeType == "light"}
								/>
								<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="topbar-color-light">
									<span class="d-flex gap-1 h-100">
										<span class="flex-shrink-0">
											<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
												<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2" />
												<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
											</span>
										</span>
										<span class="flex-grow-1">
											<span class="d-flex h-100 flex-column">
												<span class="bg-light d-block p-1" />
												<span class="bg-light d-block p-1 mt-auto" />
											</span>
										</span>
									</span>
								</Label>
							</div>
							<h5 class="fs-13 text-center mt-2">Light</h5>
						</div>
						<div class="col-4">
							<div class="form-check card-radio">
								<input class="form-check-input" type="radio" name="data-topbar" id="topbar-color-dark"
									value="dark" on:change={()=>
								changeBodyAttribute(
								"data-topbar",
								"dark"
								)}
								checked={topbarThemeType == "dark"}
								/>
								<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="topbar-color-dark">
									<span class="d-flex gap-1 h-100">
										<span class="flex-shrink-0">
											<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
												<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2" />
												<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
											</span>
										</span>
										<span class="flex-grow-1">
											<span class="d-flex h-100 flex-column">
												<span class="bg-primary d-block p-1" />
												<span class="bg-light d-block p-1 mt-auto" />
											</span>
										</span>
									</span>
								</Label>
							</div>
							<h5 class="fs-13 text-center mt-2">Dark</h5>
						</div>
					</div>
					{#if layoutType === "vertical"}
					<div id="sidebar-size">
						<h6 class="mt-4 mb-0 fw-semibold text-uppercase">
							Sidebar Size
						</h6>
						<p class="text-muted">Choose a size of Sidebar.</p>

						<div class="row">
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar-size"
										id="sidebar-size-default" value="lg" on:change={()=>
									changeBodyAttribute(
									"data-sidebar-size",
									"lg"
									)}
									checked={leftsidbarSizeType == "lg"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="sidebar-size-default">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Default
								</h5>
							</div>

							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar-size"
										id="sidebar-size-compact" value="md" on:change={()=>
									changeBodyAttribute(
									"data-sidebar-size",
									"md"
									)}
									checked={leftsidbarSizeType == "md"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="sidebar-size-compact">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 bg-primary-subtle rounded mb-2" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Compact
								</h5>
							</div>

							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar-size"
										id="sidebar-size-small" value="sm" on:change={()=>
									changeBodyAttribute(
									"data-sidebar-size",
									"sm"
									)}
									checked={leftsidbarSizeType == "sm"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="sidebar-size-small">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1">
													<span class="d-block p-1 bg-primary-subtle mb-2" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Small (Icon View)
								</h5>
							</div>

							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar-size"
										id="sidebar-size-small-hover" value="sm-hover" on:change={()=>
									changeBodyAttribute(
									"data-sidebar-size",
									"sm-hover"
									)}
									checked={leftsidbarSizeType ==
									"sm-hover"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="sidebar-size-small-hover">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1">
													<span class="d-block p-1 bg-primary-subtle mb-2" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Small Hover View
								</h5>
							</div>
						</div>
					</div>

					<div id="sidebar-view">
						<h6 class="mt-4 mb-0 fw-semibold text-uppercase">
							Sidebar View
						</h6>
						<p class="text-muted">
							Choose Default or Detached Sidebar view.
						</p>

						<div class="row">
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-layout-style"
										id="sidebar-view-default" value="default" on:change={()=>
									changeBodyAttribute(
									"data-layout-style",
									"default"
									)}
									checked={leftSidebarViewType ==
									"default"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="sidebar-view-default">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Default
								</h5>
							</div>
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-layout-style"
										id="sidebar-view-detached" value="detached" on:change={()=>
									changeBodyAttribute(
									"data-layout-style",
									"detached"
									)}
									checked={leftSidebarViewType ==
									"detached"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="sidebar-view-detached">
										<span class="d-flex h-100 flex-column">
											<span class="bg-light d-flex p-1 gap-1 align-items-center px-2">
												<span class="d-block p-1 bg-primary-subtle rounded me-1" />
												<span class="d-block p-1 pb-0 px-2 bg-primary-subtle ms-auto" />
												<span class="d-block p-1 pb-0 px-2 bg-primary-subtle" />
											</span>
											<span class="d-flex gap-1 h-100 p-1 px-2">
												<span class="flex-shrink-0">
													<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
														<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
														<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
														<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													</span>
												</span>
											</span>
											<span class="bg-light d-block p-1 mt-auto px-2" />
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Detached
								</h5>
							</div>
						</div>
					</div>
					{/if}

					{#if layoutType !== "horizontal"}
					<div id="sidebar-color">
						<h6 class="mt-4 mb-0 fw-semibold text-uppercase">
							Sidebar Color
						</h6>
						<p class="text-muted">
							Choose a color of Sidebar.
						</p>

						<div class="row">
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar"
										id="sidebar-color-light" value="light" on:change={()=> {
									changeBodyAttribute(
									"data-sidebar",
									"light"
									)
									isOpen = false
									}}
									checked={leftSidebarType == "light"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="sidebar-color-light">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-white border-end d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">
									Light
								</h5>
							</div>
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar"
										id="sidebar-color-dark" value="dark" on:change={()=>{
									changeBodyAttribute(
									"data-sidebar",
									"dark"
									);
									isOpen = false
									}}
									checked={leftSidebarType == "dark"}
									/>
									<Label class="form-check-label p-0 avatar-md w-100 material-shadow" for="sidebar-color-dark">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-primary d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 px-2 bg-white rounded mb-2" />
													<span class="d-block p-1 px-2 pb-0 bg-white" />
													<span class="d-block p-1 px-2 pb-0 bg-white" />
													<span class="d-block p-1 px-2 pb-0 bg-white" />
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1" />
													<span class="bg-light d-block p-1 mt-auto" />
												</span>
											</span>
										</span>
									</Label>
								</div>
								<h5 class="fs-13 text-center mt-2">Dark</h5>
							</div>
							<div class="col-4">
								<button on:click={()=> {
									(isOpen = !isOpen)
									changeBodyAttribute(
									"data-sidebar",
									"gradient"
									)
									}}
									class={"btn btn-link avatar-md w-100 p-0 overflow-hidden border" + (isOpen ?
									'active': '')}
									type="button"
									data-bs-target="#collapseBgGradient"
									>
									<span class="d-flex gap-1 h-100">
										<span class="flex-shrink-0">
											<span class="bg-vertical-gradient d-flex h-100 flex-column gap-1 p-1">
												<span class="d-block p-1 px-2 bg-white rounded mb-2"></span>
												<span class="d-block p-1 px-2 pb-0 bg-white"></span>
												<span class="d-block p-1 px-2 pb-0 bg-white"></span>
												<span class="d-block p-1 px-2 pb-0 bg-white"></span>
											</span>
										</span>
										<span class="flex-grow-1">
											<span class="d-flex h-100 flex-column">
												<span class="bg-light d-block p-1"></span>
												<span class="bg-light d-block p-1 mt-auto"></span>
											</span>
										</span>
									</span>
								</button>
								<h5 class="fs-13 text-center mt-2">Gradient</h5>
							</div>
						</div>
						<Collapse {isOpen} class="collapse" id="collapseBgGradient">
							<div class="d-flex gap-2 flex-wrap img-switch p-2 px-3 bg-light rounded">

								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar"
										id="sidebar-color-gradient" value="gradient" on:change={()=>
									changeBodyAttribute(
									"data-sidebar",
									"gradient"
									)}
									checked={leftSidebarTypes == "gradient"}
									>
									<Label class="form-check-label p-0 avatar-xs rounded-circle"
										for="sidebar-color-gradient">
										<span class="avatar-title rounded-circle bg-vertical-gradient"></span>
									</Label>
								</div>
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar"
										id="sidebar-color-gradient-2" value="gradient-2" on:change={()=>
									changeBodyAttribute(
									"data-sidebar",
									"gradient-2"
									)}
									checked={leftSidebarTypes == "gradient-2"}
									>
									<Label class="form-check-label p-0 avatar-xs rounded-circle"
										for="sidebar-color-gradient-2">
										<span class="avatar-title rounded-circle bg-vertical-gradient-2"></span>
									</Label>
								</div>
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar"
										id="sidebar-color-gradient-3" value="gradient-3" on:change={()=>
									changeBodyAttribute(
									"data-sidebar",
									"gradient-3"
									)}
									checked={leftSidebarTypes == "gradient-3"}
									>
									<Label class="form-check-label p-0 avatar-xs rounded-circle"
										for="sidebar-color-gradient-3">
										<span class="avatar-title rounded-circle bg-vertical-gradient-3"></span>
									</Label>
								</div>
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-sidebar"
										id="sidebar-color-gradient-4" value="gradient-4" on:change={()=>
									changeBodyAttribute(
									"data-sidebar",
									"gradient-4"
									)}
									checked={leftSidebarTypes == "gradient-4"}
									>
									<Label class="form-check-label p-0 avatar-xs rounded-circle"
										for="sidebar-color-gradient-4">
										<span class="avatar-title rounded-circle bg-vertical-gradient-4"></span>
									</Label>
								</div>
							</div>
						</Collapse>
					</div>
					<div id="sidebar-img">
						<h6 class="mt-4 mb-0 fw-semibold text-uppercase">Sidebar Images</h6>
						<p class="text-muted">Choose a image of Sidebar.</p>

						<div class="d-flex gap-2 flex-wrap img-switch">
							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-sidebar-image"
									id="sidebarimg-none" value="none" on:change={()=>
								changeBodyAttribute(
								"data-sidebar-image",
								"none"
								)}
								checked={leftSidebarImageTypes == "none"}
								>
								<Label class="form-check-label p-0 avatar-sm h-auto" for="sidebarimg-none">
									<span
										class="avatar-md w-auto bg-light d-flex align-items-center justify-content-center">
										<i class="ri-close-fill fs-20"></i>
									</span>
								</Label>
							</div>

							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-sidebar-image"
									id="sidebarimg-01" value="img-1" on:change={()=>
								changeBodyAttribute(
								"data-sidebar-image",
								"img-1"
								)}
								checked={leftSidebarImageTypes == "img-1"}
								>
								<Label class="form-check-label p-0 avatar-sm h-auto" for="sidebarimg-01">
									<img src={img01} alt="" class="avatar-md w-auto object-cover">
								</Label>
							</div>

							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-sidebar-image"
									id="sidebarimg-02" value="img-2" on:change={()=>
								changeBodyAttribute(
								"data-sidebar-image",
								"img-2"
								)}
								checked={leftSidebarImageTypes == "img-2"}
								>
								<Label class="form-check-label p-0 avatar-sm h-auto" for="sidebarimg-02">
									<img src={img02} alt="" class="avatar-md w-auto object-cover">
								</Label>
							</div>
							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-sidebar-image"
									id="sidebarimg-03" value="img-3" on:change={()=>
								changeBodyAttribute(
								"data-sidebar-image",
								"img-3"
								)}
								checked={leftSidebarImageTypes == "img-3"}
								>
								<Label class="form-check-label p-0 avatar-sm h-auto" for="sidebarimg-03">
									<img src={img03} alt="" class="avatar-md w-auto object-cover">
								</Label>
							</div>
							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-sidebar-image"
									id="sidebarimg-04" value="img-4" on:change={()=>
								changeBodyAttribute(
								"data-sidebar-image",
								"img-4"
								)}
								checked={leftSidebarImageTypes == "img-4"}
								>
								<Label class="form-check-label p-0 avatar-sm h-auto" for="sidebarimg-04">
									<img src={img04} alt="" class="avatar-md w-auto object-cover">
								</Label>
							</div>
						</div>
					</div>
					{/if}

					<div id="theme-color">
						<h6 class="mt-4 mb-0 fw-semibold text-uppercase">Primary Color</h6>
						<p class="text-muted">Choose a color of Primary.</p>
	
						<div class="d-flex flex-wrap gap-2">
							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-theme-colors" id="themeColor-01" value="default"
								on:change={() => changeThemeColors("default")} checked={themeColorType == "default"}>
								<label class="form-check-label avatar-xs p-0" for="themeColor-01"></label>
							</div>
							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-theme-colors" id="themeColor-02" value="green"
								on:change={() => changeThemeColors("green")} checked={themeColorType == "green"}>
								<label class="form-check-label avatar-xs p-0" for="themeColor-02"></label>
							</div>
							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-theme-colors" id="themeColor-03" value="purple"
								on:change={() => changeThemeColors("purple")} checked={themeColorType == "purple"}>
								<label class="form-check-label avatar-xs p-0" for="themeColor-03"></label>
							</div>
							<div class="form-check sidebar-setting card-radio">
								<input class="form-check-input" type="radio" name="data-theme-colors" id="themeColor-04" value="blue"
								on:change={() => changeThemeColors("blue")} checked={themeColorType == "blue"}>
								<label class="form-check-label avatar-xs p-0" for="themeColor-04"></label>
							</div>
						</div>
					</div>

					<div id="body-img" style="display: none;">
						<h6 class="mt-4 mb-0 fw-semibold text-uppercase">Background Image</h6>
						<p class="text-muted">Choose a body background image.</p>
					
						<div class="row">
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-body-image" id="body-img-none" value="none"
									on:change={() => changeBodyAttribute("data-body-image","none")} checked={bodyImageType == "none"}>
									<label class="form-check-label p-0 avatar-md w-100" data-body-image="none" for="body-img-none">
										<span class="d-flex gap-1 h-100">
											<span class="flex-shrink-0">
												<span class="bg-light d-flex h-100 flex-column gap-1 p-1">
													<span class="d-block p-1 px-2 bg-primary-subtle rounded mb-2"></span>
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle"></span>
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle"></span>
													<span class="d-block p-1 px-2 pb-0 bg-primary-subtle"></span>
												</span>
											</span>
											<span class="flex-grow-1">
												<span class="d-flex h-100 flex-column">
													<span class="bg-light d-block p-1"></span>
													<span class="bg-light d-block p-1 mt-auto"></span>
												</span>
											</span>
										</span>
									</label>
								</div>
								<h5 class="fs-13 text-center mt-2">None</h5>
							</div>
							<!-- end col -->
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-body-image" id="body-img-one" value="img-1"
									on:change={() => changeBodyAttribute("data-body-image","img-1")} checked={bodyImageType == "img-1"}>
									<label class="form-check-label p-0 avatar-md w-100" data-body-image="img-1" for="body-img-one">
									</label>
								</div>
								<h5 class="fs-13 text-center mt-2">One</h5>
							</div>
							<!-- end col -->
					
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-body-image" id="body-img-two" value="img-2"
									on:change={() => changeBodyAttribute("data-body-image","img-2")} checked={bodyImageType == "img-2"}>
									<label class="form-check-label p-0 avatar-md w-100" data-body-image="img-2" for="body-img-two">
									</label>
								</div>
								<h5 class="fs-13 text-center mt-2">Two</h5>
							</div>
							<!-- end col -->
					
							<div class="col-4">
								<div class="form-check sidebar-setting card-radio">
									<input class="form-check-input" type="radio" name="data-body-image" id="body-img-three" value="img-3"
									on:change={() => changeBodyAttribute("data-body-image","img-3")} checked={bodyImageType == "img-3"}>
									<label class="form-check-label p-0 avatar-md w-100" data-body-image="img-3" for="body-img-three">
									</label>
								</div>
								<h5 class="fs-13 text-center mt-2">Three</h5>
							</div>
							<!-- end col -->
						</div>
						<!-- end row -->
					</div>
				</div>
			</div>
		</div>
		<div class="offcanvas-footer border-top p-3 text-center">
			<div class="row">
				<div class="col-12">
					<a href="https://1.envato.market/velzon-admin" target="_blank" type="button"
						class="btn btn-primary w-100">Preview</a>
				</div>
			</div>
		</div>
	</div>
</div>
{#if open}
<script>
	document.documentElement.style.overflow = "hidden";
	document.body.style.paddingRight="17px";
</script>
<div class="offcanvas-backdrop fade show" on:click={()=> open = !open }></div>
{:else}
<script>
	document.documentElement.removeAttribute("style");
	document.body.removeAttribute("style");
</script>
{/if}