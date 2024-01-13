<script>
	import {
		Card,
		CardBody,
		Col,
		Container,
		Nav,
		NavItem,
		NavLink,
		Row,
		TabContent,
		TabPane,
		Tooltip,
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import Link from "svelte-link";

	import img3 from '../../../assets/images/small/img-3.jpg';
	import img4 from '../../../assets/images/small/img-4.jpg';
	import img5 from '../../../assets/images/small/img-5.jpg';
	import img6 from '../../../assets/images/small/img-6.jpg';
	import img7 from '../../../assets/images/small/img-7.jpg';
	import img8 from '../../../assets/images/small/img-8.jpg';
	import avatar1 from '../../../assets/images/users/avatar-1.jpg';
	import avatar2 from '../../../assets/images/users/avatar-2.jpg';
	import avatar3 from '../../../assets/images/users/avatar-3.jpg';
	import avatar4 from '../../../assets/images/users/avatar-4.jpg';
	import avatar5 from '../../../assets/images/users/avatar-5.jpg';
	import avatar6 from '../../../assets/images/users/avatar-6.jpg';
	import avatar7 from '../../../assets/images/users/avatar-7.jpg';
	import avatar8 from '../../../assets/images/users/avatar-8.jpg';

	let activeTab = 1;
	let justifyTab = 1;
	let pillsTab = 1;
	let justifyPillsTab = 1;
	let verticalTab = 1;
	let cardHeaderTab = 1;
	let customActiveTab = 1;
	let arrowNavTab = 1;
	let headerJustifyTab = 1;
	let bottomCardTab = 1;
	let customHoverTab = 1;
	let customverticalTab = 1;
	let animationNavTab = 1;
	let navBadgeTab = 1;
	let topBorderjustifyTab = 1;
	let topBorderTab = 1;
	let colorNavTab = 1;
	let lightNavTab = 1;
	let outlineborderTab = 1;
	let customNav = 1;
</script>

<svelte:head>
	<title>Tabs | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Tabs" pageTitle="Base UI" />
		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Default Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">A default tabbed interface.</p>

						<Nav tabs class="nav-tabs mb-3">
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (activeTab = 1)}
									active={activeTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (activeTab = 2)}
									active={activeTab == 2}
								>
									Product
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (activeTab = 3)}
									active={activeTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (activeTab = 4)}
									active={activeTab == 4}
								>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={activeTab == 1 ? "active" : ""}
								id="home">
								<h6>Graphic Design</h6>
								<p class="mb-0">
									They all have something to say beyond the
									words on the page. They can come across as
									casual or neutral, exotic or graphic. That's
									why it's important to think about your
									message, then choose a font that fits. Cosby
									sweater eu banh mi, qui irure terry
									richardson ex squid.
								</p>
							</TabPane>

							<TabPane
								class={activeTab == 2 ? "active" : ""}
								id="product">
								<h6>Product</h6>
								<p class="mb-0">
									You've probably heard that opposites
									attract. The same is true for fonts. Don't
									be afraid to combine font styles that are
									different but complementary, like sans serif
									with serif, short with tall, or decorative
									with simple. Qui photo booth letterpress,
									commodo enim craft beer mlkshk aliquip jean
									shorts ullamco ad vinyl cillum PBR.
								</p>
							</TabPane>

							<TabPane
								class={activeTab == 3 ? "active" : ""}
								id="messages">
								<h6>Messages</h6>
								<p class="mb-0">
									Etsy mixtape wayfarers, ethical wes anderson
									tofu before they sold out mcsweeney's
									organic lomo retro fanny pack lo-fi
									farm-to-table readymade. Messenger bag
									gentrify pitchfork tattooed craft beer,
									iphone skateboard locavore carles etsy
									salvia banksy hoodie helvetica. DIY synth
									PBR banksy irony.
								</p>
							</TabPane>

							<TabPane
								class={activeTab == 4 ? "active" : ""}
								id="settings">
								<h6>Settings</h6>
								<p class="mb-0">
									Trust fund seitan letterpress, keytar raw
									denim keffiyeh etsy art party before they
									sold out master cleanse gluten-free squid
									scenester freegan cosby sweater. Fanny pack
									portland seitan DIY, art party locavore wolf
									cliche high life echo park Austin. Cred
									vinyl keffiyeh DIY salvia PBR, banh mi
									before they sold out farm-to-table VHS.
								</p>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Justify Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>nav-justified</code> class to generate equal-width
							elements with all horizontal space will be occupied by
							nav links.
						</p>

						<Nav tabs class="nav-tabs nav-justified mb-3">
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (justifyTab = 1)}
									active={justifyTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (justifyTab = 2)}
									active={justifyTab == 2}
								>
									Product
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (justifyTab = 3)}
									active={justifyTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (justifyTab = 4)}
									active={justifyTab == 4}
								>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={justifyTab == 1 ? "active" : ""}
								id="base-justified-home">
								<h6>Graphic Design</h6>
								<p class="mb-0">
									They all have something to say beyond the
									words on the page. They can come across as
									casual or neutral, exotic or graphic. That's
									why it's important to think about your
									message, then choose a font that fits. Cosby
									sweater eu banh mi, qui irure terry
									richardson ex squid.
								</p>
							</TabPane>

							<TabPane
								class={justifyTab == 2 ? "active" : ""}
								id="product">
								<h6>Product</h6>
								<p class="mb-0">
									You've probably heard that opposites
									attract. The same is true for fonts. Don't
									be afraid to combine font styles that are
									different but complementary, like sans serif
									with serif, short with tall, or decorative
									with simple. Qui photo booth letterpress,
									commodo enim craft beer mlkshk aliquip jean
									shorts ullamco ad vinyl cillum PBR.
								</p>
							</TabPane>

							<TabPane
								class={justifyTab == 3 ? "active" : ""}
								id="base-justified-messages">
								<h6>Messages</h6>
								<p class="mb-0">
									Etsy mixtape wayfarers, ethical wes anderson
									tofu before they sold out mcsweeney's
									organic lomo retro fanny pack lo-fi
									farm-to-table readymade. Messenger bag
									gentrify pitchfork tattooed craft beer,
									iphone skateboard locavore carles etsy
									salvia banksy hoodie helvetica. DIY synth
									PBR banksy irony.
								</p>
							</TabPane>

							<TabPane
								class={justifyTab == 4 ? "active" : ""}
								id="base-justified-settings">
								<h6>Settings</h6>
								<p class="mb-0">
									Trust fund seitan letterpress, keytar raw
									denim keffiyeh etsy art party before they
									sold out master cleanse gluten-free squid
									scenester freegan cosby sweater. Fanny pack
									portland seitan DIY, art party locavore wolf
									cliche high life echo park Austin. Cred
									vinyl keffiyeh DIY salvia PBR, banh mi
									before they sold out farm-to-table VHS.
								</p>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Pills Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>nav-pills</code> class to generate particular
							selected nav links without borders.
						</p>

						<Nav pills class="nav-success mb-3">
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (pillsTab = 1)}
									active={pillsTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (pillsTab = 2)}
									active={pillsTab == 2}
								>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (pillsTab = 3)}
									active={pillsTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (pillsTab = 4)}
									active={pillsTab == 4}
								>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={pillsTab == 1 ? "active" : ""}
								id="home-1">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Raw denim you probably haven't heard of
										them jean shorts Austin. Nesciunt tofu
										stumptown aliqua, retro synth master
										cleanse.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Too much or too little spacing, as in
										the example below, can make things
										unpleasant for the reader. The goal is
										to make your text as comfortable to read
										as possible.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={pillsTab == 2 ? "active" : ""}
								id="profile-1">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										In some designs, you might adjust your
										tracking to create a certain artistic
										effect. It can also help you fix fonts
										that are poorly spaced to begin with.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										A wonderful serenity has taken
										possession of my entire soul, like these
										sweet mornings of spring which I enjoy
										with my whole heart.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={pillsTab == 3 ? "active" : ""}
								id="messages-1">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Each design is a new, unique piece of
										art birthed into this world, and while
										you have the opportunity to be creative
										and make your own style choices.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={pillsTab == 4 ? "active" : ""}
								id="settings-1">
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										After gathering lots of different
										opinions and graphic design basics, I
										came up with a list of 30 graphic design
										tips that you can start implementing.
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Pills Justified Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>nav-pills nav-justified</code> class to generate
							equal-width elements without borders, all horizontal
							space will be occupied by nav links.
						</p>

						<Nav pills class="nav-justified mb-3">
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (justifyPillsTab = 1)}
									active={justifyPillsTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (justifyPillsTab = 2)}
									active={justifyPillsTab == 2}
								>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (justifyPillsTab = 3)}
									active={justifyPillsTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (justifyPillsTab = 4)}
									active={justifyPillsTab == 4}
								>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={justifyPillsTab == 1 ? "active" : ""}
								id="pill-justified-home-1">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Raw denim you probably haven't heard of
										them jean shorts Austin. Nesciunt tofu
										stumptown aliqua, retro synth master
										cleanse.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Too much or too little spacing, as in
										the example below, can make things
										unpleasant for the reader. The goal is
										to make your text as comfortable to read
										as possible.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={justifyPillsTab == 2 ? "active" : ""}
								id="pill-justified-profile-1">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										In some designs, you might adjust your
										tracking to create a certain artistic
										effect. It can also help you fix fonts
										that are poorly spaced to begin with.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										A wonderful serenity has taken
										possession of my entire soul, like these
										sweet mornings of spring which I enjoy
										with my whole heart.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={justifyPillsTab == 3 ? "active" : ""}
								id="pill-justified-messages-1">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Each design is a new, unique piece of
										art birthed into this world, and while
										you have the opportunity to be creative
										and make your own style choices.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={justifyPillsTab == 4 ? "active" : ""}
								id="pill-justified-settings-1">
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										After gathering lots of different
										opinions and graphic design basics, I
										came up with a list of 30 graphic design
										tips that you can start implementing.
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Vertical Nav Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>flex-column</code> class to create Vertical
							nav tabs.
						</p>
						<Row>
							<Col md={3}>
								<Nav pills class="flex-column text-center" id="v-pills-tab">
									<NavItem>
										<NavLink
											style="cursor: pointer"
											on:click={() => (verticalTab = 1)}
											active={verticalTab == 1}
											class="mb-2"
											id="v-pills-home-tab"
										>
											Home
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											style="cursor: pointer"
											on:click={() => (verticalTab = 2)}
											active={verticalTab == 2}
											class="mb-2"
											id="v-pills-profile-tab"
										>
											Profile
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											style="cursor: pointer"
											on:click={() => (verticalTab = 3)}
											active={verticalTab == 3}
											class="mb-2"
											id="v-pills-messages-tab"
										>
											Messages
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											style="cursor: pointer"
											on:click={() => (verticalTab = 4)}
											active={verticalTab == 4}
											id="v-pills-settings-tab"
										>
											Settings
										</NavLink>
									</NavItem>
								</Nav>
							</Col>
							<Col md={9}>
								<TabContent
									class="text-muted mt-4 mt-md-0"
									id="v-pills-tabContent"
								>
									<TabPane
										class={verticalTab == 1 ? "active" : ""}
										id="v-pills-home"
									>
										<div class="d-flex mb-2">
											<div class="flex-shrink-0">
												<img
													src={img4}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<p class="mb-0">
													You always want to make sure
													that your fonts work well
													together and try to limit
													the number of fonts you use
													to three or less. Experiment
													and play around with the
													fonts that you already have
													in the software you’re
													working with reputable font
													websites.
												</p>
											</div>
										</div>
										<p class="mb-0">
											This may be the most commonly
											encountered tip I received from the
											designers I spoke with. They highly
											encourage that you use different
											fonts in one design, but do not
											over-exaggerate and go overboard.
										</p>
									</TabPane>
									<TabPane
										class={verticalTab == 2 ? "active" : ""}
										id="v-pills-profile"
									>
										<div class="d-flex mb-2">
											<div class="flex-shrink-0">
												<img
													src={img5}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<p class="mb-0">
													I also decreased the
													transparency in the text so
													that the mountains come
													through the text, bringing
													the quote truly to life.
													Make sure that the placement
													of your text is pleasing to
													look at, and you try to
													achieve symmetry for this
													effect.
												</p>
											</div>
										</div>
										<p class="mb-0">
											You've probably heard that opposites
											attract. The same is true for fonts.
											Don't be afraid to combine font
											styles that are different but
											complementary. You can always play
											around with the text that is
											overlaid on an image.
										</p>
									</TabPane>
									<TabPane
										class={verticalTab == 3 ? "active" : ""}
										id="v-pills-messages"
									>
										<div class="d-flex mb-2">
											<div class="flex-shrink-0">
												<img
													src={img6}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<p class="mb-0">
													In this image, you can see
													that the line height has
													been reduced significantly,
													and the size was brought up
													exponentially. Experiment
													and play around with the
													fonts that you already have
													in the software you’re
													working with reputable font
													websites.
												</p>
											</div>
										</div>
										<p class="mb-0">
											They highly encourage that you use
											different fonts in one design, but
											do not over-exaggerate and go
											overboard This may be the most
											commonly encountered tip I received
											from the designers I spoke with.
										</p>
									</TabPane>

									<TabPane
										class={verticalTab == 4 ? "active" : ""}
										id="v-pills-settings"
									>
										<div class="d-flex mb-2">
											<div class="flex-shrink-0">
												<img
													src={img7}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<p class="mb-0">
													When designing, the goal is
													to draw someone’s attention
													and portray to them what
													you’re trying to say. You
													can make a big statement by
													using little tricks, like
													this one. Use contrasting
													fonts. you can use a bold
													sanserif font with a
													cursive.
												</p>
											</div>
										</div>
										<p class="mb-0">
											If you’re using multiple elements,
											make sure that your principal object
											is larger than the others, as the
											eye of your viewer will
											automatically be drawn to the larger
											of the two objects.
										</p>
									</TabPane>
								</TabContent>
							</Col>
						</Row>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Card Header Tabs</h5>
				<Card>
					<div class="card-header align-items-center d-flex">
						<div class="flex-grow-1 oveflow-hidden">
							<p class="text-muted text-truncates mb-0">
								Use <code>card-header-tabs</code> class to create
								card header tabs.
							</p>
						</div>
						<div class="flex-shrink-0 ms-2">
							<Nav
								tabs
								class="nav justify-content-end nav-tabs-custom rounded card-header-tabs border-bottom-0">
								<NavItem>
									<NavLink
										style="cursor: pointer"
										on:click={() => (cardHeaderTab = 1)}
										active={cardHeaderTab == 1}
									>
										Home
									</NavLink>
								</NavItem>
								<NavItem>
									<NavLink
										style="cursor: pointer"
										on:click={() => (cardHeaderTab = 2)}
										active={cardHeaderTab == 2}
									>
										Profile
									</NavLink>
								</NavItem>
								<NavItem>
									<NavLink
										style="cursor: pointer"
										on:click={() => (cardHeaderTab = 3)}
										active={cardHeaderTab == 3}
									>
										Messages
									</NavLink>
								</NavItem>
							</Nav>
						</div>
					</div>
					<CardBody>
						<TabContent class="text-muted">
							<TabPane
								class={cardHeaderTab == 1 ? "active" : ""}
								id="home2">
								<p class="flex-grow-1 mb-0">
									<img
										src={avatar2}
										alt=""
										class="avatar-lg rounded float-start me-3"
									/>
									Food truck fixie locavore, accusamus mcsweeney's
									marfa nulla single-origin coffee squid. Exercitation
									+1 labore velit, blog sartorial PBR leggings
									next level wes anderson artisan four loko farm-to-table
									craft beer twee. commodo enim craft beer mlkshk
									aliquip jean shorts ullamco ad vinyl cillum PBR.
									Homo nostrud organic, assumenda labore aesthetic
									magna delectus.commodo enim craft beer mlkshk
									aliquip jean shorts ullamco ad vinyl cillum PBR.
									Homo nostrud organic, assumenda labore aesthetic
									magna delectus. If you’re using multiple elements,
									make sure that your principal object is larger
									than assumenda.
								</p>
							</TabPane>

							<TabPane
								class={cardHeaderTab == 2 ? "active" : ""}
								id="profile2">
								<p class="me-3 mb-0">
									<img
										src={avatar3}
										alt=""
										class="avatar-lg rounded float-end ms-3"
									/> Experiment and play around with the fonts
									that you already have in the software you’re
									working with reputable font websites. commodo
									enim craft beer mlkshk aliquip jean shorts ullamco
									ad vinyl cillum PBR. Homo nostrud organic, assumenda
									labore aesthetic magna delectus.commodo enim
									craft beer mlkshk aliquip jean shorts ullamco
									ad vinyl cillum PBR. Homo nostrud organic, assumenda
									labore aesthetic magna delectus Scale all elements
									of your design: text, elements, buttons, everything.
									Increase or decrease the letter spacing depending
									on the situation and try, try again until it
									looks right, and each /.
								</p>
							</TabPane>

							<TabPane
								class={cardHeaderTab == 3 ? "active" : ""}
								id="messages2">
								<p class="ms-3 mb-0">
									<img
										src={avatar5}
										alt=""
										class="avatar-lg rounded float-start me-3"
									/>Trust fund seitan letterpress, keytar raw
									denim keffiyeh etsy art party before they
									sold out master cleanse gluten-free squid
									scenester freegan cosby sweater. Fanny pack
									portland seitan DIY, art party locavore wolf
									cliche high life echo park Austin. Cred
									vinyl keffiyeh DIY salvia PBR, beer mlkshk
									aliquip jean shorts ullamco ad vinyl cillum
									PBR. Homo nostrud organic, assumenda labore
									aes Homo nostrud organic, assumenda labore
									aesthetic magna delectus Scale all elements
									of your design: text, elements, buttons,
									everything.Increase or decrease the letter
									spacing depending on the situation and try,
									try again until it looks right, and each.
								</p>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Custom Tabs Bordered</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>nav-tabs-custom</code> class to create custom
							tabs with borders.
						</p>
						<Nav
							tabs
							class="nav nav-tabs nav-tabs-custom nav-success nav-justified mb-3"
						>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (customActiveTab = 1)}
									active={customActiveTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (customActiveTab = 2)}
									active={customActiveTab == 2}
								>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (customActiveTab = 3)}
									active={customActiveTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (customActiveTab = 4)}
									active={customActiveTab == 4}
								>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={customActiveTab == 1 ? "active" : ""}
								id="home1">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-multiple-blank-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Trust fund seitan letterpress, keytar
										raw denim keffiyeh etsy art party before
										they sold out master cleanse gluten-free
										squid scenester freegan cosby sweater.
										Fanny pack portland seitan DIY, art
										party locavore wolf cliche high life
										echo park Austin. Cred vinyl keffiyeh
										DIY salvia PBR.
										<div class="mt-2">
											<Link
												href={null}
												class="btn btn-sm btn-soft-primary"
												>Read More <i
													class="ri-arrow-right-line ms-1 align-middle"
												/></Link
											>
										</div>
									</div>
								</div>
							</TabPane>
							<TabPane
								class={customActiveTab == 2 ? "active" : ""}>
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-multiple-blank-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										When, while the lovely valley teems with
										vapour around me, and the meridian sun
										strikes the upper surface of the
										impenetrable foliage of my trees, and
										but a few stray gleams steal into the
										inner sanctuary, I throw myself down
										among the tall grass by the trickling
										stream; and, as I lie close to the
										earth, a thousand unknown.
										<div class="mt-2">
											<Link
												href={null}
												class="btn btn-sm btn-soft-primary"
												>Read More <i
													class="ri-arrow-right-line ms-1 align-middle"
												/></Link
											>
										</div>
									</div>
								</div>
							</TabPane>
							<TabPane
								class={customActiveTab == 3 ? "active" : ""}>
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-multiple-blank-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Etsy mixtape wayfarers, ethical wes
										anderson tofu before they sold out
										mcsweeney's organic lomo retro fanny
										pack lo-fi farm-to-table readymade.
										Messenger bag gentrify pitchfork
										tattooed craft beer, iphone skateboard
										locavore carles etsy salvia banksy
										hoodie helvetica. DIY synth PBR banksy
										irony.
										<div class="mt-2">
											<Link
												href={null}
												class="btn btn-sm btn-soft-primary"
												>Read More <i
													class="ri-arrow-right-line ms-1 align-middle"
												/></Link
											>
										</div>
									</div>
								</div>
							</TabPane>
							<TabPane
								class={customActiveTab == 4 ? "active" : ""}>
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-multiple-blank-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										when darkness overspreads my eyes, and
										heaven and earth seem to dwell in my
										soul and absorb its power, like the form
										of a beloved mistress, then I often
										think with longing, Oh, would I could
										describe these conceptions, could
										impress upon paper all that is living so
										full and warm within me, that it might
										be the.
										<div class="mt-2">
											<Link
												href={null}
												class="btn btn-sm btn-soft-primary"
												>Read More <i
													class="ri-arrow-right-line ms-1 align-middle"
												/></Link
											>
										</div>
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Arrow Nav tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>arrow-navtabs </code>class to create arrow
							nav tabs.
						</p>
						<Nav
							pills
							class="nav nav-pills arrow-navtabs nav-success bg-light mb-3"
						>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (arrowNavTab = 1)}
									active={arrowNavTab == 1}
								>
									Overview
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (arrowNavTab = 2)}
									active={arrowNavTab == 2}
								>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (arrowNavTab = 3)}
									active={arrowNavTab == 3}
								>
									Contact
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={arrowNavTab == 1 ? "active" : ""}
								id="arrow-overview">
								<h6>Give your text a good structure</h6>
								<p class="mb-0">
									Contrary to popular belief, you don’t have
									to work endless nights and hours to create a <Link
										href={null}
										class="text-decoration-underline"
										><b>Fantastic Design</b></Link
									> by using complicated 3D elements. Flat design
									is your friend. Remember that. And the great
									thing about flat design is that it has become
									more and more popular over the years, which is
									excellent news to the beginner and advanced designer.
								</p>
							</TabPane>
							<TabPane
								class={arrowNavTab == 2 ? "active" : ""}
								id="arrow-profile">
								<h6>Use a color palette</h6>
								<p class="mb-0">
									Opposites attract, and that’s a fact. It’s
									in our nature to be interested in the
									unusual, and that’s why using contrasting
									colors in <Link
										href={null}
										class="text-decoration-underline"
										><b>Graphic Design</b></Link
									> is a must. It’s eye-catching, it makes a statement,
									it’s impressive graphic design. Increase or decrease
									the letter spacing depending on the situation
									and try, try again until it looks right, and
									each letter has the perfect spot of its own.
								</p>
							</TabPane>
							<TabPane
								class={arrowNavTab == 3 ? "active" : ""}
								id="arrow-contact">
								<h6>Contact</h6>
								<p class="mb-0">
									Consistency is the one thing that can take
									all of the different elements in your
									design, and tie them all together and make
									them work. In an awareness campaign, it is
									vital for people to begin put 2 and 2
									together and begin to recognize your cause.
									Consistency piques people’s interest is that
									it has become more and more popular over the
									years, which is excellent news to the
									beginner and advanced <Link
										href={null}
										class="text-decoration-underline"
										><b>Contact Designer</b></Link
									>.
								</p>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Header Justify Tabs</h5>
				<Card>
					<div class="card-header align-items-xl-center d-xl-flex">
						<p class="text-muted flex-grow-1 mb-xl-0">
							Use <code>card-header-pills</code> class to create header
							justify tab.
						</p>
						<div class="flex-shrink-0">
							<Nav pills class="card-header-pills">
								<NavItem>
									<NavLink
										style="cursor: pointer"
										on:click={() => (headerJustifyTab = 1)}
										active={headerJustifyTab == 1}
									>
										Developers
									</NavLink>
								</NavItem>
								<NavItem>
									<NavLink
										style="cursor: pointer"
										on:click={() => (headerJustifyTab = 2)}
										active={headerJustifyTab == 2}
									>
										Designers
									</NavLink>
								</NavItem>
								<NavItem>
									<NavLink
										style="cursor: pointer"
										on:click={() => (headerJustifyTab = 3)}
										active={headerJustifyTab == 3}
									>
										Managers
									</NavLink>
								</NavItem>
							</Nav>
						</div>
					</div>
					<CardBody>
						<TabContent class="text-muted">
							<TabPane
								class={headerJustifyTab == 1 ? "active" : ""}
								id="developers">
								<Row>
									<Col sm={6}>
										<div class="d-flex">
											<div class="flex-shrink-0">
												<img
													src={avatar8}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Dominic Charlton
												</h6>
												<p class="mb-0">
													520 Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar7}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Charlie Pritchard
												</h6>
												<p class="mb-0">
													45.2K Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar6}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Harvey Wells
												</h6>
												<p class="mb-0">
													1025 Followers
												</p>
											</div>
										</div>
									</Col>
									<Col sm={6}>
										<div class="d-flex mt-3 mt-sm-0">
											<div class="flex-shrink-0">
												<img
													src={avatar5}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Amelie Townsend
												</h6>
												<p class="mb-0">
													6584 Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar4}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Emily Slater
												</h6>
												<p class="mb-0">
													24.8K Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar3}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Declan Long
												</h6>
												<p class="mb-0">
													1.5K Followers
												</p>
											</div>
										</div>
									</Col>
								</Row>
							</TabPane>

							<TabPane
								class={headerJustifyTab == 2 ? "active" : ""}
								id="designers">
								<Row>
									<Col sm={6}>
										<div class="d-flex">
											<div class="flex-shrink-0">
												<img
													src={avatar1}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Luke Brown
												</h6>
												<p class="mb-0">
													654 Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar2}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Matilda Walker
												</h6>
												<p class="mb-0">
													270 Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar3}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Leo Stokes
												</h6>
												<p class="mb-0">
													4120 Followers
												</p>
											</div>
										</div>
									</Col>
									<Col sm={6}>
										<div class="d-flex mt-3 mt-sm-0">
											<div class="flex-shrink-0">
												<img
													src={avatar4}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Chelsea Preston
												</h6>
												<p class="mb-0">
													9854 Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar5}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Jennifer Barker
												</h6>
												<p class="mb-0">
													15.8K Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar6}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Callum Murray
												</h6>
												<p class="mb-0">2K Followers</p>
											</div>
										</div>
									</Col>
								</Row>
							</TabPane>

							<TabPane
								class={headerJustifyTab == 3 ? "active" : ""}
								id="managers">
								<Row>
									<Col sm={6}>
										<div class="d-flex">
											<div class="flex-shrink-0">
												<img
													src={avatar7}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Dominic Charlton
												</h6>
												<p class="mb-0">
													784 Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar8}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Matilda Walker
												</h6>
												<p class="mb-0">
													6549 Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar4}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Jennifer Barker
												</h6>
												<p class="mb-0">
													2100 Followers
												</p>
											</div>
										</div>
									</Col>
									<Col sm={6}>
										<div class="d-flex mt-3 mt-sm-0">
											<div class="flex-shrink-0">
												<img
													src={avatar5}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Amelie Townsend
												</h6>
												<p class="mb-0">
													4565 Followers
												</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar1}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Emily Slater
												</h6>
												<p class="mb-0">8K Followers</p>
											</div>
										</div>
										<div class="d-flex mt-3">
											<div class="flex-shrink-0">
												<img
													src={avatar2}
													alt=""
													class="avatar-sm rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<h6 class="mb-1 fs-14">
													Declan Long
												</h6>
												<p class="mb-0">
													9800 Followers
												</p>
											</div>
										</div>
									</Col>
								</Row>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Bottom Card Nav Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>card-footer-tabs</code> class to create the
							bottom card nav justify tab.
						</p>
						<TabContent class="text-muted">
							<TabPane
								class={bottomCardTab == 1 ? "active" : ""}
								id="bottomtabs-home">
								<h5>
									<i
										class="ri-home-3-line align-bottom me-1"
									/> Home
								</h5>
								<p class="mb-2">
									On the note of consistency, color
									consistency is a MUST. If you’re not trying
									to create crazy contrast in your design,
									then a great idea would be for you to use a
									color palette throughout your entire design.
									It will subconsciously interest viewers and
									also is very pleasing to look at.
								</p>
								<p class="mb-0">
									Any bypasser will stop to see what you have
									to see, even if your design has nothing to
									do with them, for the simple fact that it is
									beautiful to look at.
								</p>
							</TabPane>

							<TabPane
								class={bottomCardTab == 2 ? "active" : ""}
								id="bottomtabs-profile">
								<h5>
									<i
										class="ri-user-2-line align-bottom me-1"
									/> Profile
								</h5>
								<p class="mb-2">
									Just like in the image where we talked about
									using multiple fonts, you can see that the
									background in this graphic design is
									blurred. Whenever you put text on top of an
									image, it’s important that your viewers can
									understand the text, and sometimes that
									means applying a gaussian readable.
								</p>
								<p class="mb-0">
									A very bad quack might jinx zippy fowls. Few
									quips galvanized the mock jury box. Quick
									brown dogs jump over the lazy fox. The jay,
									pig, fox, zebra, and my wolves.
								</p>
							</TabPane>

							<TabPane
								class={bottomCardTab == 3 ? "active" : ""}
								id="bottomtabs-messages">
								<h5>
									<i class="ri-mail-line align-bottom me-1" />
									Messages
								</h5>
								<p class="mb-2">
									Blowzy red vixens fight for a quick jump.
									Joaquin Phoenix was gazed by MTV for luck. A
									wizard’s job is to vex chumps quickly in
									fog. Watch "Jeopardy! ", Alex Trebek's fun
									TV quiz game. Woven silk pyjamas exchanged
									for blue quartz. Brawny gods just flocked up
									to quiz and vex him.
								</p>
								<p class="mb-0">
									Big July earthquakes confound zany
									experimental vow. My girl wove six dozen
									plaid jackets before she quit. Six big
									devils from Japan quickly forgot how to
									waltz.
								</p>
							</TabPane>
						</TabContent>
					</CardBody>
					<div class="card-footer bg-transparent border-top">
						<Nav pills class="nav-justified card-footer-tabs fs-17">
							<NavItem id="home">
								<NavLink
									style="cursor: pointer"
									on:click={() => (bottomCardTab = 1)}
									active={bottomCardTab == 1}
								>
									<i class="ri-home-3-line" />
								</NavLink>
								<Tooltip placement="top" target="home"
									>Home</Tooltip
								>
							</NavItem>
							<NavItem id="profile">
								<NavLink
									style="cursor: pointer"
									on:click={() => (bottomCardTab = 2)}
									active={bottomCardTab == 2}
								>
									<i class="ri-user-2-line" />
								</NavLink>
								<Tooltip placement="top" target="profile"
									>Profile</Tooltip
								>
							</NavItem>
							<NavItem id="messages">
								<NavLink
									style="cursor: pointer"
									on:click={() => (bottomCardTab = 3)}
									active={bottomCardTab == 3}
								>
									<i class="ri-mail-line" />
								</NavLink>
								<Tooltip placement="top" target="messages"
									>Messages</Tooltip
								>
							</NavItem>
						</Nav>
					</div>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Custom Hover Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>custom-hover-nav-tabs</code> class to create
							custom hover tabs.
						</p>
					</CardBody>
					<div class="border">
						<Nav pills class="nav nav-pills custom-hover-nav-tabs">
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (customHoverTab = 1)}
									active={customHoverTab == 1}
								>
									<i
										class="ri-user-fill nav-icon nav-tab-position"
									/>
									<h5 class="nav-titl nav-tab-position m-0">
										Customer
									</h5>
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (customHoverTab = 2)}
									active={customHoverTab == 2}
								>
									<i
										class="ri-file-text-line nav-icon nav-tab-position"
									/>
									<h5 class="nav-titl nav-tab-position m-0">
										Description
									</h5>
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (customHoverTab = 3)}
									active={customHoverTab == 3}
								>
									<i
										class="ri-star-half-line nav-icon nav-tab-position"
									/>
									<h5 class="nav-titl nav-tab-position m-0">
										Reviews
									</h5>
								</NavLink>
							</NavItem>
						</Nav>
					</div>
					<CardBody>
						<TabContent class="text-muted">
							<TabPane
								class={customHoverTab == 1 ? "active" : ""}
								id="custom-hover-customere">
								<h6>Customer Details</h6>
								<div class="table-responsive">
									<table class="table mb-0">
										<thead>
											<tr>
												<th scope="col">#</th>
												<th scope="col">Name</th>
												<th scope="col">Address</th>
												<th scope="col">Country</th>
												<th scope="col">Pincode</th>
											</tr>
										</thead>
										<tbody>
											<tr>
												<th scope="row">1</th>
												<td>Ruby Butcher</td>
												<td>412 Rosewood Lane</td>
												<td>New York</td>
												<td>10019</td>
											</tr>
											<tr>
												<th scope="row">2</th>
												<td>Martha T Goldberg</td>
												<td
													>2760 Clarksburg Park Road</td
												>
												<td>Arizona</td>
												<td>86038</td>
											</tr>
										</tbody>
									</table>
								</div>
							</TabPane>

							<TabPane
								class={customHoverTab == 2 ? "active" : ""}
								id="custom-hover-customere">
								<h6>Description</h6>
								<div class="table-responsive">
									<table class="table mb-0">
										<thead>
											<tr>
												<th scope="col">Title</th>
												<th scope="col">Categories</th>
												<th scope="col">Author</th>
											</tr>
										</thead>
										<tbody>
											<tr>
												<td
													>Building Web Apps With
													Wordpress</td
												>
												<td>Web, Wordpress, Design</td>
												<td>Lucia Victor</td>
											</tr>
											<tr>
												<th>Information Technology</th>
												<td
													>Management, Manager, Design</td
												>
												<td>Arora Sumita</td>
											</tr>
										</tbody>
									</table>
								</div>
							</TabPane>

							<TabPane
								class={customHoverTab == 3 ? "active" : ""}
								id="custom-hover-reviews">
								<h6>Customer Reviews</h6>
								<div class="table-responsive">
									<table class="table mb-0">
										<thead>
											<tr>
												<th scope="col">Name</th>
												<th scope="col">Location</th>
												<th scope="col">Amount</th>
												<th scope="col">Ratings</th>
											</tr>
										</thead>
										<tbody>
											<tr>
												<td>Luke Brown</td>
												<td>New York</td>
												<td>$745</td>
												<td
													>4.4 <i
														class="ri-star-s-fill ms-1 text-warning align-middle"
													/></td
												>
											</tr>
											<tr>
												<td>Matilda Walker</td>
												<td>USA</td>
												<td>$87.125</td>
												<td
													>2.7 <i
														class="ri-star-s-fill ms-1 text-warning align-middle"
													/></td
												>
											</tr>
										</tbody>
									</table>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Custom Vertical Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>custom-verti-nav-pills</code> class to create
							custom vertical tabs.
						</p>
						<Row>
							<Col lg={3}>
								<Nav
									pills
									class="nav nav-pills flex-column nav-pills-tab custom-verti-nav-pills text-center"
								>
									<NavItem>
										<NavLink
											style="cursor: pointer"
											on:click={() =>
												(customverticalTab = 1)}
											active={customverticalTab == 1}
											class=""
											id="custom-v-pills-home-tab"
										>
											<i
												class="ri-home-4-line d-block fs-20 mb-1"
											/>
											Home
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											style="cursor: pointer"
											on:click={() =>
												(customverticalTab = 2)}
											active={customverticalTab == 2}
											class=""
											id="custom-v-pills-profile-tab"
										>
											<i
												class="ri-user-2-line d-block fs-20 mb-1"
											/>
											Profile
										</NavLink>
									</NavItem>
									<NavItem>
										<NavLink
											style="cursor: pointer"
											on:click={() =>
												(customverticalTab = 3)}
											active={customverticalTab == 3}
											class=""
											id="custom-v-pills-messages-tab"
										>
											<i
												class="ri-mail-line d-block fs-20 mb-1"
											/>
											Messages
										</NavLink>
									</NavItem>
								</Nav>
							</Col>
							<Col lg={9}>
								<TabContent class="text-muted mt-3 mt-lg-0">
									<TabPane
										class={customverticalTab == 1
											? "active"
											: ""}
										id="custom-v-pills-home"
									>
										<div class="d-flex mb-4">
											<div class="flex-shrink-0">
												<img
													src={img4}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<p class="mb-0">
													Experiment and play around
													with the fonts that you
													already have in the software
													you’re working with
													reputable font websites.
													commodo enim craft beer
													mlkshk aliquip jean shorts
													ullamco ad vinyl cillum PBR.
													Homo nostrud organic,
													assumenda labore aesthetic
													magna delectus.
												</p>
											</div>
										</div>
										<div class="d-flex">
											<div class="flex-grow-1 me-3">
												<p class="mb-0">
													Always want to make sure
													that your fonts work well
													together and try to limit
													the number of fonts you use
													to three or less. Experiment
													and play around with the
													fonts that you already have
													in the software you’re
													working with reputable font
													websites.
												</p>
											</div>
											<div class="flex-shrink-0">
												<img
													src={img5}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
										</div>
									</TabPane>
									<TabPane
										class={customverticalTab == 2
											? "active"
											: ""}
										id="custom-v-pills-profile"
									>
										<div class="d-flex mb-4">
											<div class="flex-shrink-0">
												<img
													src={img3}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<p class="mb-0">
													In some designs, you might
													adjust your tracking to
													create a certain artistic
													effect. It can also help you
													fix fonts that are poorly
													spaced to begin with. A
													wonderful serenity has taken
													possession of my entire
													soul, like these sweet
													mornings of spring which I
													enjoy with my whole heart.
												</p>
											</div>
										</div>
										<div class="d-flex">
											<div class="flex-grow-1 me-3">
												<p class="mb-0">
													Each design is a new, unique
													piece of art birthed into
													this world, and while you
													have the opportunity to be
													creative and make your own
													style choices. For that very
													reason, I went on a quest
													and spoke to many different
													professional graphic
													designers.
												</p>
											</div>
											<div class="flex-shrink-0">
												<img
													src={img6}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
										</div>
									</TabPane>
									<TabPane
										class={customverticalTab == 3
											? "active"
											: ""}
										id="custom-v-pills-messages"
									>
										<div class="d-flex mb-4">
											<div class="flex-shrink-0">
												<img
													src={img7}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
											<div class="flex-grow-1 ms-3">
												<p class="mb-0">
													Trust fund seitan
													letterpress, keytar raw
													denim keffiyeh etsy art
													party before they sold out
													master cleanse gluten-free
													squid scenester freegan
													cosby sweater. Fanny pack
													portland seitan DIY, art
													party locavore wolf cliche
													high life echo park Austin.
													Cred vinyl keffiyeh DIY
													salvia PBR.
												</p>
											</div>
										</div>
										<div class="d-flex">
											<div class="flex-grow-1 me-3">
												<p class="mb-0">
													They all have something to
													say beyond the words on the
													page. They can come across
													as casual or neutral, exotic
													or graphic. That's why it's
													important to think about
													your message, then choose a
													font that fits. Cosby
													sweater eu banh mi, qui
													irure terry richardson ex
													squid.
												</p>
											</div>
											<div class="flex-shrink-0">
												<img
													src={img8}
													alt=""
													width="150"
													class="rounded"
												/>
											</div>
										</div>
									</TabPane>
								</TabContent>
							</Col>
						</Row>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Animation Nav</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>animation-nav</code> class to create animated
							tabs.
						</p>

						<Nav
							pills
							class="nav nav-pills animation-nav nav-justified gap-2 mb-3"
						>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (animationNavTab = 1)}
									active={animationNavTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (animationNavTab = 2)}
									active={animationNavTab == 2}
								>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (animationNavTab = 3)}
									active={animationNavTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (animationNavTab = 4)}
									active={animationNavTab == 4}
								>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={animationNavTab == 1 ? "active" : ""}
								id="animation-home">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Raw denim you probably haven't heard of
										them jean shorts Austin. Nesciunt tofu
										stumptown aliqua, retro synth master
										cleanse.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Too much or too little spacing, as in
										the example below, can make things
										unpleasant for the reader. The goal is
										to make your text as comfortable to read
										as possible.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={animationNavTab == 2 ? "active" : ""}
								id="animation-profile">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										In some designs, you might adjust your
										tracking to create a certain artistic
										effect. It can also help you fix fonts
										that are poorly spaced to begin with.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										A wonderful serenity has taken
										possession of my entire soul, like these
										sweet mornings of spring which I enjoy
										with my whole heart.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={animationNavTab == 3 ? "active" : ""}
								id="animation-messages">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Each design is a new, unique piece of
										art birthed into this world, and while
										you have the opportunity to be creative
										and make your own style choices.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={animationNavTab == 4 ? "active" : ""}
								id="animation-settings">
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										After gathering lots of different
										opinions and graphic design basics, I
										came up with a list of 30 graphic design
										tips that you can start implementing.
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Nav with Badge</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Example of nav tabs with badge wrapped in nav item.
						</p>

						<Nav tabs class="nav-tabs nav-justified mb-3">
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (navBadgeTab = 1)}
									active={navBadgeTab == 1}
								>
									Explore
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (navBadgeTab = 2)}
									active={navBadgeTab == 2}
								>
									Profile <span class="badge bg-success"
										>Done</span
									>
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (navBadgeTab = 3)}
									active={navBadgeTab == 3}
								>
									Messages <span
										class="badge bg-danger rounded-circle"
										>5</span
									>
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (navBadgeTab = 4)}
									active={navBadgeTab == 4}
								>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={navBadgeTab == 1 ? "active" : ""}
								id="nav-badge-home">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Raw denim you probably haven't heard of
										them jean shorts Austin. Nesciunt tofu
										stumptown aliqua, retro synth master
										cleanse.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Too much or too little spacing, as in
										the example below, can make things
										unpleasant for the reader. The goal is
										to make your text as comfortable to read
										as possible.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={navBadgeTab == 2 ? "active" : ""}
								id="nav-badge-profile">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										In some designs, you might adjust your
										tracking to create a certain artistic
										effect. It can also help you fix fonts
										that are poorly spaced to begin with.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										A wonderful serenity has taken
										possession of my entire soul, like these
										sweet mornings of spring which I enjoy
										with my whole heart.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={navBadgeTab == 3 ? "active" : ""}
								id="nav-badge-messages">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Each design is a new, unique piece of
										art birthed into this world, and while
										you have the opportunity to be creative
										and make your own style choices.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live.
									</div>
								</div>
							</TabPane>

							<TabPane
								class={navBadgeTab == 4 ? "active" : ""}
								id="nav-badge-settings">
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-fill text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										After gathering lots of different
										opinions and graphic design basics, I
										came up with a list of 30 graphic design
										tips that you can start implementing.
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Border Top Nav</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>nav-border-top</code> class to create nav tabs
							with border at top.
						</p>

						<Nav
							tabs
							class="nav nav-tabs nav-border-top nav-border-top-primary mb-3"
						>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (topBorderjustifyTab = 1)}
									active={topBorderjustifyTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (topBorderjustifyTab = 2)}
									active={topBorderjustifyTab == 2}
								>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (topBorderjustifyTab = 3)}
									active={topBorderjustifyTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (topBorderjustifyTab = 4)}
									active={topBorderjustifyTab == 4}
								>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={topBorderjustifyTab == 1 ? "active" : ""}
								id="nav-border-top-home">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-line text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Trust fund seitan letterpress, keytar
										raw denim keffiyeh etsy art party before
										they sold out master cleanse gluten-free
										squid scenester freegan cosby sweater.
										Fanny pack portland seitan DIY, art
										party locavore wolf cliche high life
										echo park Austin. Cred vinyl keffiyeh
										DIY salvia PBR.
										<div class="mt-2">
											<Link href={null} class="btn btn-link"
												>Read More <i
													class="ri-arrow-right-line ms-1 align-middle"
												/></Link
											>
										</div>
									</div>
								</div>
							</TabPane>

							<TabPane
								class={topBorderjustifyTab == 2 ? "active" : ""}
								id="nav-border-top-profile">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-line text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										When, while the lovely valley teems with
										vapour around me, and the meridian sun
										strikes the upper surface of the
										impenetrable foliage of my trees, and
										but a few stray gleams steal into the
										inner sanctuary, I throw myself down
										among the tall grass by the trickling
										stream; and, as I lie close to the
										earth, a thousand unknown.
										<div class="mt-2">
											<Link href={null} class="btn btn-link"
												>Read More <i
													class="ri-arrow-right-line ms-1 align-middle"
												/></Link
											>
										</div>
									</div>
								</div>
							</TabPane>

							<TabPane
								class={topBorderjustifyTab == 3 ? "active" : ""}
								id="nav-border-top-messages">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-line text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										Etsy mixtape wayfarers, ethical wes
										anderson tofu before they sold out
										mcsweeney's organic lomo retro fanny
										pack lo-fi farm-to-table readymade.
										Messenger bag gentrify pitchfork
										tattooed craft beer, iphone skateboard
										locavore carles etsy salvia banksy
										hoodie helvetica. DIY synth PBR banksy
										irony.
										<div class="mt-2">
											<Link href={null} class="btn btn-link"
												>Read More <i
													class="ri-arrow-right-line ms-1 align-middle"
												/></Link
											>
										</div>
									</div>
								</div>
							</TabPane>

							<TabPane
								class={topBorderjustifyTab == 4 ? "active" : ""}
								id="nav-border-top-settings">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i
											class="ri-checkbox-circle-line text-success"
										/>
									</div>
									<div class="flex-grow-1 ms-2">
										when darkness overspreads my eyes, and
										heaven and earth seem to dwell in my
										soul and absorb its power, like the form
										of a beloved mistress, then I often
										think with longing, Oh, would I could
										describe these conceptions, could
										impress upon paper all that is living so
										full and warm within me, that it might
										be the.
										<div class="mt-2">
											<Link href={null} class="btn btn-link"
												>Read More <i
													class="ri-arrow-right-line ms-1 align-middle"
												/></Link
											>
										</div>
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Border Top Nav Justified Tabs</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>nav-border-top nav-justified</code> class to
							create nav tabs with border at top with justified tabs
							position.
						</p>

						<Nav
							tabs
							class="nav nav-tabs nav-justified nav-border-top nav-border-top-success mb-3"
						>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (topBorderTab = 1)}
									active={topBorderTab == 1}
								>
									<i
										class="ri-home-5-line align-middle me-1"
									/> Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (topBorderTab = 2)}
									active={topBorderTab == 2}
								>
									<i class="ri-user-line me-1 align-middle" />
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (topBorderTab = 3)}
									active={topBorderTab == 3}
								>
									<i
										class="ri-question-answer-line align-middle me-1"
									/>Messages
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={topBorderTab == 1 ? "active" : ""}
								id="nav-border-justified-home">
								<h6>Give your text a good structure</h6>
								<p class="mb-0">
									Contrary to popular belief, you don’t have
									to work endless nights and hours to create a <Link
										href={null}
										class="text-decoration-underline"
										><b>Fantastic Design</b></Link
									> by using complicated 3D elements. Flat design
									is your friend. Remember that. And the great
									thing about flat design is that it has become
									more and more popular over the years, which is
									excellent news to the beginner and advanced designer.
								</p>
							</TabPane>

							<TabPane
								class={topBorderTab == 2 ? "active" : ""}
								id="nav-border-justified-profile">
								<h6>Use a color palette</h6>
								<p class="mb-0">
									Opposites attract, and that’s a fact. It’s
									in our nature to be interested in the
									unusual, and that’s why using contrasting
									colors in <Link
										href={null}
										class="text-decoration-underline"
										><b>Graphic Design</b></Link
									> is a must. It’s eye-catching, it makes a statement,
									it’s impressive graphic design. Increase or decrease
									the letter spacing depending on the situation
									and try, try again until it looks right, and
									each letter has the perfect spot of its own.
								</p>
							</TabPane>

							<TabPane
								class={topBorderTab == 3 ? "active" : ""}
								id="nav-border-justified-messages">
								<h6>Message</h6>
								<p class="mb-0">
									Consistency is the one thing that can take
									all of the different elements in your
									design, and tie them all together and make
									them work. In an awareness campaign, it is
									vital for people to begin put 2 and 2
									together and begin to recognize your cause.
									Consistency piques people’s interest is that
									it has become more and more popular over the
									years, which is excellent news to the
									beginner and advanced <Link
										href={null}
										class="text-decoration-underline"
										><b>Contact Designer</b></Link
									>.
								</p>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Outline Border Nav</h5>
				<Card>
					<CardBody>
						<p class="text-muted">*Use <code>nav-custom-</code> class with modifier class to color tabs.</p>

						<Nav pills class="nav-custom-outline nav-primary mb-3">
							<NavItem>
								<NavLink style="cursor: pointer" on:click={() =>(outlineborderTab = 1)} active={outlineborderTab ==1}>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink style="cursor: pointer" on:click={() =>(outlineborderTab = 2)} active={outlineborderTab ==2}>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink style="cursor: pointer" on:click={() =>(outlineborderTab = 3)} active={outlineborderTab ==3}>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink style="cursor: pointer" on:click={() =>(outlineborderTab = 4)} active={outlineborderTab ==4}>
									Settings
								</NavLink>
							</NavItem>
						</Nav>
						<TabContent class="text-muted">
							<TabPane tabId="1" id="border-nav-home" class={outlineborderTab == 1 ? "active" : ""}>
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										Raw denim you probably haven't heard of them jean shorts Austin.
										Nesciunt tofu stumptown aliqua, retro synth master cleanse.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										Too much or too little spacing, as in the example below, can make things unpleasant for the reader. The
										goal is to make your text as comfortable to read as possible.
									</div>
								</div>
							</TabPane>

							<TabPane tabId="2" id="border-nav-profile" class={outlineborderTab == 2 ? "active" : ""}>
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										In some designs, you might adjust your tracking to create a certain artistic effect. It can also help
										you fix fonts that are poorly spaced to begin with.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I
										enjoy with my whole heart.
									</div>
								</div>
							</TabPane>

							<TabPane tabId="3" id="border-nav-messages" class={outlineborderTab == 3 ? "active" : ""}>
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										Each design is a new, unique piece of art birthed into this world, and while you have the opportunity to
										be creative and make your own style choices.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest and spoke to many different professional graphic designers and
										asked them what graphic design tips they live.
									</div>
								</div>
							</TabPane>

							<TabPane tabId="4" id="border-nav-settings" class={outlineborderTab == 4 ? "active" : ""}>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest and spoke to many different professional graphic designers and
										asked them what graphic design tips they live.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										After gathering lots of different opinions and graphic design basics, I came up with a list of 30
										graphic design tips that you can start implementing.
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Custom Nav</h5>
				<Card>
					<CardBody>
						<p class="text-muted">*Use <code>nav-custom-</code> class with modifier class to color tabs.</p>

						<Nav pills class="nav-customs nav-danger mb-3">
							<NavItem>
								<NavLink style="cursor: pointer" on:click={() =>(customNav = 1)} active={customNav == 1}>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink style="cursor: pointer" on:click={() =>(customNav = 2)} active={customNav == 2}>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink style="cursor: pointer" on:click={() =>(customNav = 3)} active={customNav == 3}>
									Messages
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink style="cursor: pointer" on:click={() =>(customNav = 4)} active={customNav == 4}>
									Settings
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane tabId="1" id="border-navs-home" class={customNav == 1 ? "active" : ""}>
								<div class="tab-pane active" id="border-navs-home" role="tabpanel">
									<div class="d-flex">
										<div class="flex-shrink-0">
											<i class="ri-checkbox-circle-fill text-success"></i>
										</div>
										<div class="flex-grow-1 ms-2">
											Raw denim you probably haven't heard of them jean shorts Austin.
											Nesciunt tofu stumptown aliqua, retro synth master cleanse.
										</div>
									</div>
									<div class="d-flex mt-2">
										<div class="flex-shrink-0">
											<i class="ri-checkbox-circle-fill text-success"></i>
										</div>
										<div class="flex-grow-1 ms-2">
											Too much or too little spacing, as in the example below, can make things unpleasant for the reader. The
											goal is to make your text as comfortable to read as possible.
										</div>
									</div>
								</div>
							</TabPane>

							<TabPane tabId="2" id="border-navs-profile" class={customNav == 2 ? "active" : ""}>
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										In some designs, you might adjust your tracking to create a certain artistic effect. It can also help
										you fix fonts that are poorly spaced to begin with.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I
										enjoy with my whole heart.
									</div>
								</div>
							</TabPane>

							<TabPane tabId="3" id="border-navs-messages" class={customNav == 3 ? "active" : ""}>
								<div class="d-flex">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										Each design is a new, unique piece of art birthed into this world, and while you have the opportunity to
										be creative and make your own style choices.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest and spoke to many different professional graphic designers and
										asked them what graphic design tips they live.
									</div>
								</div>
							</TabPane>

							<TabPane tabId="4" id="border-navs-settings" class={customNav == 4 ? "active" : ""}>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										For that very reason, I went on a quest and spoke to many different professional graphic designers and
										asked them what graphic design tips they live.
									</div>
								</div>
								<div class="d-flex mt-2">
									<div class="flex-shrink-0">
										<i class="ri-checkbox-circle-fill text-success"></i>
									</div>
									<div class="flex-grow-1 ms-2">
										After gathering lots of different opinions and graphic design basics, I came up with a list of 30
										graphic design tips that you can start implementing.
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>
		<Row>
			<Col xxl={6}>
				<h5 class="mb-3">Colored Nav</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>nav-custom-</code> class with modifier class
							to color tabs.
						</p>

						<Nav
							pills
							class="nav nav-pills nav-custom nav-custom-success mb-3"
						>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (colorNavTab = 1)}
									active={colorNavTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (colorNavTab = 2)}
									active={colorNavTab == 2}
								>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (colorNavTab = 3)}
									active={colorNavTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={colorNavTab == 1 ? "active" : ""}
								id="nav-colored-home">
								<div class="d-flex mb-3">
									<div class="flex-shrink-0">
										<img
											src={avatar2}
											alt=""
											class="avatar-md rounded"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										Food truck fixie locavore, accusamus
										mcsweeney's marfa nulla single-origin
										coffee squid. Exercitation +1 labore
										velit, blog sartorial PBR leggings next
										level wes anderson artisan four loko
										farm-to-table craft beer twee. commodo
										enim craft beer mlkshk aliquip jean
										shorts ullamco.
									</div>
								</div>
								<div class="d-flex">
									<div class="flex-grow-1 me-3">
										For that very reason, I went on a quest
										and spoke to many different professional
										graphic designers and asked them what
										graphic design tips they live. vinyl
										cillum PBR. Homo nostrud organic,
										assumenda labore aesthetic magna
										delectus.
									</div>
									<div class="flex-shrink-0">
										<img
											src={avatar3}
											alt=""
											class="avatar-md rounded"
										/>
									</div>
								</div>
							</TabPane>

							<TabPane
								class={colorNavTab == 2 ? "active" : ""}
								id="nav-colored-profile">
								<div class="d-flex mb-3">
									<div class="flex-shrink-0">
										<img
											src={avatar4}
											alt=""
											class="avatar-md rounded"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										Increase or decrease the letter spacing
										depending on the situation and try, try
										again until it looks right, and each.
										next level wes anderson artisan four
										loko farm-to-table craft beer twee.
										commodo enim craft beer mlkshk aliquip
										jean shorts ullamco.
									</div>
								</div>
								<div class="d-flex">
									<div class="flex-grow-1 me-3">
										Experiment and play around with the
										fonts that you already have in the
										software you’re working with reputable
										font websites. commodo enim craft beer
										mlkshk aliquip jean shorts ullamco ad
										vinyl cillum PBR. Homo nostrud organic.
									</div>
									<div class="flex-shrink-0">
										<img
											src={avatar1}
											alt=""
											class="avatar-md rounded"
										/>
									</div>
								</div>
							</TabPane>

							<TabPane
								class={colorNavTab == 3 ? "active" : ""}
								id="nav-colored-messages">
								<div class="d-flex mb-3">
									<div class="flex-shrink-0">
										<img
											src={avatar4}
											alt=""
											class="avatar-md rounded"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										Trust fund seitan letterpress, keytar
										raw denim keffiyeh etsy art party before
										they sold out master cleanse gluten-free
										squid scenester freegan cosby sweater.
										Fanny pack portland seitan DIY, art
										party locavore wolf cliche high life
										echo park Austin.
									</div>
								</div>
								<div class="d-flex">
									<div class="flex-grow-1 me-3">
										Increase or decrease the letter spacing
										depending on the situation and try, try
										again until it looks right, and each
										assumenda labore aes Homo nostrud
										organic, assumenda labore aesthetic
										magna elements, buttons, everything..
									</div>
									<div class="flex-shrink-0">
										<img
											src={avatar1}
											alt=""
											class="avatar-md rounded"
										/>
									</div>
								</div>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={6}>
				<h5 class="mb-3">Light Nav</h5>
				<Card>
					<CardBody>
						<p class="text-muted">
							Use <code>nav-custom-light</code> class to lighten the
							nav tabs area.
						</p>

						<Nav
							pills
							class="nav nav-pills nav-custom nav-custom-light mb-3"
						>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (lightNavTab = 1)}
									active={lightNavTab == 1}
								>
									Home
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (lightNavTab = 2)}
									active={lightNavTab == 2}
								>
									Profile
								</NavLink>
							</NavItem>
							<NavItem>
								<NavLink
									style="cursor: pointer"
									on:click={() => (lightNavTab = 3)}
									active={lightNavTab == 3}
								>
									Messages
								</NavLink>
							</NavItem>
						</Nav>

						<TabContent class="text-muted">
							<TabPane
								class={lightNavTab == 1 ? "active" : ""}
								id="nav-light-home">
								<div class="d-flex mb-1">
									<div class="flex-grow-1 me-3">
										Experiment and play around with the
										fonts that you already have in the
										software you’re working with reputable
										font websites. commodo enim craft beer
										mlkshk aliquip jean shorts ullamco ad
										vinyl cillum PBR. Homo nostrud organic,
										assumenda labore aesthetic magna
										delectus. pposites attract, and that’s a
										fact. It’s in our nature to be
										interested in the unusual, and that’s
										why using contrasting.
									</div>
									<div class="flex-shrink-0">
										<img
											src={img4}
											alt=""
											width="150"
											class="rounded"
										/>
									</div>
								</div>
								<p class="mb-0">
									Food truck fixie locavore, accusamus
									mcsweeney's marfa nulla single-origin coffee
									squid. Exercitation +1 labore velit, blog
									sartorial PBR leggings next level wes
									anderson artisan four loko farm-to-table
									craft beer twee. commodo enim craft beer
									mlkshk aliquip jean shorts ullamco.
								</p>
							</TabPane>

							<TabPane
								class={lightNavTab == 2 ? "active" : ""}
								id="nav-light-profile">
								<div class="d-flex mb-1">
									<div class="flex-grow-1 me-3">
										Just like in the image where we talked
										about using multiple fonts, you can see
										that the background in this graphic
										design is blurred. Whenever you put text
										on top of an image, it’s important that
										your viewers can understand the text,
										and sometimes that means applying a
										gaussian readable Any bypasser will stop
										to see what you have to see, even if
										your design has nothing to do with them.
									</div>
									<div class="flex-shrink-0">
										<img
											src={img5}
											alt=""
											width="150"
											class="rounded"
										/>
									</div>
								</div>
								<p class="mb-0">
									It makes a statement, it’s impressive
									graphic design. Increase or decrease the
									letter spacing depending on the situation
									and try, try again until it looks right, and
									each letter has the perfect spot of its own.
									commodo enim craft beer mlkshk aliquip jean
									shorts ullamco.
								</p>
							</TabPane>

							<TabPane
								class={lightNavTab == 3 ? "active" : ""}
								id="nav-colored-messages">
								<div class="d-flex mb-1">
									<div class="flex-grow-1 me-3">
										Trust fund seitan letterpress, keytar
										raw denim keffiyeh etsy art party before
										they sold out master cleanse gluten-free
										squid scenester freegan cosby sweater.
										Fanny pack portland seitan DIY, art
										party locavore wolf cliche high life
										echo park Austin On the note of
										consistency, color consistency is a
										MUST. If you’re not trying to create
										crazy contrast in your design.
									</div>
									<div class="flex-shrink-0">
										<img
											src={img5}
											alt=""
											width="150"
											class="rounded"
										/>
									</div>
								</div>
								<p class="mb-0">
									Big July earthquakes confound zany
									experimental vow. My girl wove six dozen
									plaid jackets before she quit. Six big
									devils from Japan quickly forgot how to
									waltz. try again until it looks right, and
									each assumenda labore aes Homo nostrud
									organic, assumenda labore aesthetic magna
									elements, buttons, everything.
								</p>
							</TabPane>
						</TabContent>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
