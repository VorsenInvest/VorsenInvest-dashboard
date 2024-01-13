<script>
	import {
		Card,
		CardBody,
		Col,
		Container,
		ListGroup,
		ListGroupItem,
		Row,
	} from "sveltestrap";
	import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
	import PreviewCardHeader from "../../../Components/Common/PreviewCardHeader.svelte";
	import UiContent from "../../../Components/Common/UiContent.svelte";
	import PrismCode from "../../../Components/Common/Prism.svelte";
	import Link from "svelte-link";

	import avatar1 from "../../../assets/images/users/avatar-1.jpg";
	import avatar2 from "../../../assets/images/users/avatar-2.jpg";
	import avatar3 from "../../../assets/images/users/avatar-3.jpg";
	import avatar4 from "../../../assets/images/users/avatar-4.jpg";

	// Default List

	const defaultListCode = `
<!-- Default List -->
<ListGroup>
    <ListGroupItem><i class="ri-bill-line align-middle me-2"></i> Send the billing agreement</ListGroupItem>
    <ListGroupItem><i class="ri-file-copy-2-line align-middle me-2"></i>Send over all the documentation.</ListGroupItem>
    <ListGroupItem><i class="ri-question-answer-line align-middle me-2"></i>Meeting with daron to review the intake form</ListGroupItem>
    <ListGroupItem><i class="ri-secure-payment-line align-middle me-2"></i>Check uikings theme and give customer support</ListGroupItem>
</ListGroup>
`;

	// Active Item
	const activeItemCode = `
<!-- Active Item -->
<ListGroup>
    <ListGroupItem active>Send the billing agreement</ListGroupItem>
    <ListGroupItem>Send over all the documentation.</ListGroupItem>
    <ListGroupItem>Meeting with daron to review the intake form</ListGroupItem>
    <ListGroupItem>Check uikings theme and give customer support</ListGroupItem>
    <ListGroupItem>Start making a presentation</ListGroupItem>
</ListGroup>
`;

	// Disabled Items
	const disabledItemCode = `
<!-- Disabled Items -->
<ListGroup>
    <ListGroupItem disabled>
        <div class="d-flex align-items-center">
            <div class="flex-shrink-0">
                <img src={avatar1} alt="" class="avatar-xs rounded-circle" />
            </div>
            <div class="flex-grow-1 ms-2">
                James Ballard
            </div>
        </div>
    </ListGroupItem>
    <ListGroupItem>
        <div class="d-flex align-items-center">
            <div class="flex-shrink-0">
                <img src={avatar2} alt="" class="avatar-xs rounded-circle" />
            </div>
            <div class="flex-grow-1 ms-2">
                Nancy Martino
            </div>
        </div>
    </ListGroupItem>
    <ListGroupItem>
        <div class="d-flex align-items-center">
            <div class="flex-shrink-0">
                <img src={avatar3} alt="" class="avatar-xs rounded-circle" />
            </div>
            <div class="flex-grow-1 ms-2">
                Henry Baird
            </div>
        </div>
    </ListGroupItem>
    <ListGroupItem>
        <div class="d-flex align-items-center">
            <div class="flex-shrink-0">
                <img src={avatar3} alt="" class="avatar-xs rounded-circle" />
            </div>
            <div class="flex-grow-1 ms-2">
                Erica Kernan
            </div>
        </div>
    </ListGroupItem>
</ListGroup>
`;

	// List with Link
	const listlinkCode = `
<!-- List with Link -->
<ListGroup class="list-group-fill-success">
    <ListGroupItem tag="a" href={null} class="list-group-item-action active"><i class="ri-download-2-fill align-middle me-2"></i>Category Download</ListGroupItem>
    <ListGroupItem tag="a" href={null} class="list-group-item-action"><i class="ri-shield-check-line align-middle me-2"></i>Security Access</ListGroupItem>
    <ListGroupItem tag="a" href={null} class="list-group-item-action"><i class="ri-database-2-line align-middle me-2"></i>Storage folder</ListGroupItem>
    <ListGroupItem tag="a" href={null} class="list-group-item-action"><i class="ri-notification-3-line align-middle me-2"></i>Push Notification</ListGroupItem>
    <ListGroupItem tag="a" href={null} class="list-group-item-action disabled" tabIndex="-1"><i class="ri-moon-fill align-middle me-2"></i>Dark Mode</ListGroupItem>
</ListGroup>
`;

	// List with Button
	const listButtonCode = `
<!-- List with Button -->
<ListGroup>
    <ListGroupItem tag="button" class="list-group-item-action active"><i class="ri-reply-fill align-middle me-2"></i>Reply</ListGroupItem>
    <ListGroupItem tag="button" class="list-group-item-action"><i class="ri-share-forward-fill align-middle me-2"></i>Forward Message</ListGroupItem>
    <ListGroupItem tag="button" class="list-group-item-action"><i class="ri-equalizer-line align-middle me-2"></i>Filter Message</ListGroupItem>
    <ListGroupItem tag="button" class="list-group-item-action"><i class="ri-delete-bin-5-line align-middle me-2"></i>Delete Message</ListGroupItem>
    <ListGroupItem tag="button" class="list-group-item-action" disabled><i class="ri-forbid-line align-middle me-2"></i>Block "Mark Spencer</ListGroupItem>
</ListGroup>
`;

	// Flush List
	const flushListCode = `
<!-- Flush List -->
<ListGroup flush>
    <ListGroupItem>Send the billing agreement</ListGroupItem>
    <ListGroupItem>Send over all the documentation.</ListGroupItem>
    <ListGroupItem>Meeting with daron to review the intake form</ListGroupItem>
    <ListGroupItem>Check uikings theme and give customer support</ListGroupItem>
    <ListGroupItem>Start making a presentation</ListGroupItem>
</ListGroup>
`;

	// Horizontal List
	const horizontalListCode = `
<!-- Start Alignment -->
<ListGroup class="mb-3" horizontal>
    <ListGroupItem>Inbox</ListGroupItem>
    <ListGroupItem>Work</ListGroupItem>
    <ListGroupItem>Shopping</ListGroupItem>
</ListGroup>
<ListGroup class="justify-content-center mb-3" horizontal>
    <ListGroupItem>Inbox</ListGroupItem>
    <ListGroupItem>Work</ListGroupItem>
    <ListGroupItem>Shopping</ListGroupItem>
</ListGroup>
<ListGroup class="justify-content-end" horizontal>
    <ListGroupItem>Inbox</ListGroupItem>
    <ListGroupItem>Work</ListGroupItem>
    <ListGroupItem>Shopping</ListGroupItem>
</ListGroup>
`;

	// Contextual Classes
	const contextualClassCode = `
<!-- Contextual Classes -->
<ListGroup>
    <ListGroupItem >Dapibus ac facilisis in</ListGroupItem>
    <ListGroupItem color="primary">A simple primary list group item</ListGroupItem>
    <ListGroupItem color="secondary">A simple secondary list group item</ListGroupItem>
    <ListGroupItem color="success">A simple success list group item</ListGroupItem>
    <ListGroupItem color="danger">A simple danger list group item</ListGroupItem>
    <ListGroupItem color="warning">A simple warning list group item</ListGroupItem>
    <ListGroupItem color="info">A simple info list group item</ListGroupItem>
    <ListGroupItem color="light">A simple light list group item</ListGroupItem>
    <ListGroupItem color="dark">A simple dark list group item</ListGroupItem>
</ListGroup>
`;

	// Contextual Classes with Link
	const contextualLinkCode = `
<!-- Contextual Classes with Link -->
<ListGroup>
    <ListGroupItem color="" tag="a" href={null} class="list-group-item-action">A simple default list group item</ListGroupItem>
    <ListGroupItem color="primary" tag="a" href={null} class="list-group-item-action">A simple primary list group item</ListGroupItem>
    <ListGroupItem color="secondary" tag="a" href={null} class="list-group-item-action">A simple secondary list group item</ListGroupItem>
    <ListGroupItem color="success" tag="a" href={null} class="list-group-item-action">A simple success list group item</ListGroupItem>
    <ListGroupItem color="danger" tag="a" href={null} class="list-group-item-action">A simple danger list group item</ListGroupItem>
    <ListGroupItem color="warning" tag="a" href={null} class="list-group-item-action">A simple warning list group item</ListGroupItem>
    <ListGroupItem color="info" tag="a" href={null} class="list-group-item-action">A simple info list group item</ListGroupItem>
    <ListGroupItem color="light" tag="a" href={null} class="list-group-item-action">A simple light list group item</ListGroupItem>
    <ListGroupItem color="dark" tag="a" href={null} class="list-group-item-action">A simple dark list group item</ListGroupItem>
</ListGroup>
`;

	// Colored Lists
	const coloredListCode = `
<!-- Colored Lists -->
<ListGroup>
    <ListGroupItem >Dapibus ac facilisis in</ListGroupItem>
    <ListGroupItem class="list-group-fill-primary">A simple primary list group item</ListGroupItem>
    <ListGroupItem class="list-group-fill-secondary">A simple secondary list group item</ListGroupItem>
    <ListGroupItem class="list-group-fill-success">A simple success list group item</ListGroupItem>
    <ListGroupItem class="list-group-fill-danger">A simple danger list group item</ListGroupItem>
    <ListGroupItem class="list-group-fill-warning">A simple warning list group item</ListGroupItem>
    <ListGroupItem class="list-group-fill-info">A simple info list group item</ListGroupItem>
    <ListGroupItem class="list-group-fill-light">A simple light list group item</ListGroupItem>
    <ListGroupItem class="list-group-fill-dark">A simple dark list group item</ListGroupItem>
</ListGroup>
`;

	// Custom Content
	const customContentCode = `
<!-- Custom Content -->
<ListGroup>
    <ListGroupItem tag="a" href={null} class="list-group-item-action active">
        <div class="float-end">
            Pending
        </div>
        <div class="d-flex mb-2 align-items-center">
            <div class="flex-shrink-0">
                <img src={avatar1} alt="" class="avatar-sm rounded-circle" />
            </div>
            <div class="flex-grow-1 ms-3">
                <h5 class="list-title fs-16 mb-1">Charlie Pritchard</h5>
                <p class="list-text mb-0 fs-13">12 min Ago</p>
            </div>
        </div>
        <p class="list-text mb-0">They all have something to say beyond the words on the page. They can come across as casual or neutral, exotic or graphic. That's why it's important to think about your message, then choose a font that fits. Cosby sweater eu banh mi, qui irure terry richardson ex squid.</p>
    </ListGroupItem>
    <ListGroupItem tag="a" href={null} class="list-group-item-action">
        <div class="float-end">
            Pending
        </div>
        <div class="d-flex mb-2 align-items-center">
            <div class="flex-shrink-0">
                <img src={avatar2} alt="" class="avatar-sm rounded-circle" />
            </div>
            <div class="flex-grow-1 ms-3">
                <h5 class="list-title fs-16 mb-1">Dominic Charlton</h5>
                <p class="list-text mb-0 fs-13">12 min Ago</p>
            </div>
        </div>
        <p class="list-text mb-0">Trust fund seitan letterpress, keytar raw denim keffiyeh etsy art party before they sold out master cleanse gluten-free squid scenester freegan cosby sweater. Fanny pack portland seitan DIY, art party locavore wolf cliche high life echo park Austin.</p>
    </ListGroupItem>
    <ListGroupItem tag="a" href={null} class="list-group-item-action">
        <div class="float-end">
            Rejected
        </div>
        <div class="d-flex mb-2 align-items-center">
            <div class="flex-shrink-0">
                <img src={avatar3} alt="" class="avatar-sm rounded-circle" />
            </div>
            <div class="flex-grow-1 ms-3">
                <h5 class="list-title fs-16 mb-1">Declan Long</h5>
                <p class="list-text mb-0 fs-13">12 min Ago</p>
            </div>
        </div>
        <p class="list-text mb-0">Big July earthquakes confound zany experimental vow. My girl wove six dozen plaid jackets before she quit. Six big devils from Japan quickly forgot how to waltz. try again until it looks right, and each assumenda labore aes Homo nostrud organic, assumenda labore aesthetic magna elements, buttons, everything.</p>
    </ListGroupItem>
    <ListGroupItem tag="a" href={null} class="list-group-item-action">
        <div class="float-end">
            Successful
        </div>
        <div class="d-flex mb-2 align-items-center">
            <div class="flex-shrink-0">
                <img src={avatar4} alt="" class="avatar-sm rounded-circle" />
            </div>
            <div class="flex-grow-1 ms-3">
                <h5 class="list-title fs-16 mb-1">Angela Bernier</h5>
                <p class="list-text mb-0 fs-13">5 days Ago</p>
            </div>
        </div>
        <p class="list-text mb-0">Just like in the image where we talked about using multiple fonts, you can see that the background in this graphic design is blurred. Whenever you put text on top of an image, it’s important that your viewers can understand the text, and sometimes that means applying a gaussian readable.</p>
    </ListGroupItem>
</ListGroup>
`;

	// List with Badges
	const listBadgeCode = `
<!-- List with Badges -->
<ListGroup>
    <ListGroupItem class="d-flex justify-content-between align-items-center">
        Send the billing agreement <span class="badge bg-success">High</span>
    </ListGroupItem>
    <ListGroupItem class="d-flex justify-content-between align-items-center">
        Send over all the documentation
    </ListGroupItem>
    <ListGroupItem class="d-flex justify-content-between align-items-center">
        Meeting with daron to review the intake form <span class="badge bg-danger">Low</span>
    </ListGroupItem>
    <ListGroupItem class="d-flex justify-content-between align-items-center">
        Check uikings theme and give customer support <span class="badge bg-secondary">Medium</span>
    </ListGroupItem>
    <ListGroupItem class="d-flex justify-content-between align-items-center">
        Start making a presentation <span class="badge bg-success">High</span>
    </ListGroupItem>
</ListGroup>
`;

	// List with Checkboxs
	const listCheckboxCode = `
<!-- List with Checkboxs -->
<ListGroup>
    <ListGroupItem tag="label">
        <Input class="form-check-input me-1" type="checkbox" value="" />
        Declined Payment
    </ListGroupItem>
    <ListGroupItem tag="label">
        <Input class="form-check-input me-1" type="checkbox" value="" checked />
        Delivery Error
    </ListGroupItem>
    <ListGroupItem tag="label">
        <Input class="form-check-input me-1" type="checkbox" value="" checked />
        Wrong Amount
    </ListGroupItem>
    <ListGroupItem tag="label">
        <Input class="form-check-input me-1" type="checkbox" value="" />
        Wrong Address
    </ListGroupItem>
    <ListGroupItem tag="label">
        <Input class="form-check-input me-1" type="checkbox" value="" />
        Wrong UX/UI Solution
    </ListGroupItem>
</ListGroup>
`;

	// List with Radios
	const listRadioCode = `
<!-- List with Radios -->
<ListGroup>
    <ListGroupItem tag="label">
        <Input class="form-check-input fs-14 mt-0 align-middle me-1" name="exampleRadios" type="radio" value="" />
        Declined Payment
    </ListGroupItem>
    <ListGroupItem tag="label">
        <Input class="form-check-input fs-14 mt-0 align-middle me-1" name="exampleRadios" type="radio" value="" checked />
        Delivery Error
    </ListGroupItem>
    <ListGroupItem tag="label">
        <Input class="form-check-input fs-14 mt-0 align-middle me-1" name="exampleRadios" type="radio" value="" />
        Wrong Amount
    </ListGroupItem>
    <ListGroupItem tag="label">
        <Input class="form-check-input fs-14 mt-0 align-middle me-1" name="exampleRadios" type="radio" value="" />
        Wrong Address
    </ListGroupItem>
    <ListGroupItem tag="label">
        <Input class="form-check-input fs-14 mt-0 align-middle me-1" name="exampleRadios" type="radio" value="" />
        Wrong UX/UI Solution
    </ListGroupItem>
</ListGroup>
`;

	// List with Icon
	const listIconCode = `
<!-- List with Icon -->
<ListGroup>
    <ListGroupItem><i class="mdi mdi-check-bold align-middle lh-1 me-2"></i> Send the billing agreement</ListGroupItem>
    <ListGroupItem><i class="mdi mdi-check-bold align-middle lh-1 me-2"></i> Send over all the documentation.</ListGroupItem>
    <ListGroupItem><i class="mdi mdi-check-bold align-middle lh-1 me-2"></i> Meeting with daron to review the intake form</ListGroupItem>
    <ListGroupItem><i class="mdi mdi-check-bold align-middle lh-1 me-2"></i> Check uikings theme and give customer support</ListGroupItem>
    <ListGroupItem><i class="mdi mdi-check-bold align-middle lh-1 me-2"></i> Start making a presentation</ListGroupItem>
</ListGroup>
`;

	// List with Numbered
	const listNumberedCode = `
<!-- List with Numbered -->
<ListGroup class="list-group-numbered">
    <ListGroupItem>Send the billing agreement</ListGroupItem>
    <ListGroupItem>Send over all the documentation.</ListGroupItem>
    <ListGroupItem>Meeting with daron to review the intake form</ListGroupItem>
    <ListGroupItem>Check uikings theme and give customer support</ListGroupItem>
    <ListGroupItem>Start making a presentation</ListGroupItem>
</ListGroup>
`;

	// Custom Content Lists
	const customListCode = `
<!-- Custom Content Lists -->
<SimpleBar style="max-height: 215px">
    <ListGroup class="mb-1">
        <ListGroupItem>
            <div class="d-flex align-items-center">
                <div class="flex-grow-1">
                    <div class="d-flex">
                        <div class="flex-shrink-0 avatar-xs">
                            <div class="avatar-title bg-danger-subtle text-danger rounded">
                                <i class="ri-netflix-fill"></i>
                            </div>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                            <h6 class="fs-14 mb-0">Netfilx</h6>
                            <small class="text-muted">2 min Ago</small>
                        </div>
                    </div>
                </div>
                <div class="flex-shrink-0">
                    <span class="text-danger">-$25.50</span>
                </div>
            </div>
        </ListGroupItem>
        <ListGroupItem>
            <div class="d-flex align-items-center">
                <div class="flex-grow-1">
                    <div class="d-flex">
                        <div class="flex-shrink-0 avatar-xs">
                            <div class="avatar-title bg-success-subtle text-success rounded">
                                <i class="ri-spotify-fill"></i>
                            </div>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                            <h6 class="fs-14 mb-0">Spotify</h6>
                            <small class="text-muted">5 days Ago</small>
                        </div>
                    </div>
                </div>
                <div class="flex-shrink-0">
                    <span class="text-success">$48.25</span>
                </div>
            </div>
        </ListGroupItem>
        <ListGroupItem>
            <div class="d-flex align-items-center">
                <div class="flex-grow-1">
                    <div class="d-flex">
                        <div class="flex-shrink-0">
                            <img src={avatar2} alt="" class="avatar-xs rounded" />
                        </div>
                        <div class="flex-shrink-0 ms-2">
                            <h6 class="fs-14 mb-0">Emily Slater</h6>
                            <small class="text-muted">8 days Ago</small>
                        </div>
                    </div>
                </div>
                <div class="flex-shrink-0">
                    <span class="text-success">$354.90</span>
                </div>
            </div>
        </ListGroupItem>
        <ListGroupItem>
            <div class="d-flex align-items-center">
                <div class="flex-grow-1">
                    <div class="d-flex">
                        <div class="flex-shrink-0 avatar-xs">
                            <div class="avatar-title bg-secondary-subtle text-secondary rounded">
                                <i class="ri-paypal-fill"></i>
                            </div>
                        </div>
                        <div class="flex-shrink-0 ms-2">
                            <h6 class="fs-14 mb-0">Paypal</h6>
                            <small class="text-muted">1 month Ago</small>
                        </div>
                    </div>
                </div>
                <div class="flex-shrink-0">
                    <span class="text-danger">-$12.22</span>
                </div>
            </div>
        </ListGroupItem>
        <ListGroupItem>
            <div class="d-flex align-items-center">
                <div class="flex-grow-1">
                    <div class="d-flex">
                        <div class="flex-shrink-0">
                            <img src={avatar3} alt="" class="avatar-xs rounded" />
                        </div>
                        <div class="flex-shrink-0 ms-2">
                            <h6 class="fs-14 mb-0">Harvey Wells</h6>
                            <small class="text-muted">4 month Ago</small>
                        </div>
                    </div>
                </div>
                <div class="flex-shrink-0">
                    <span class="text-success">-$459.78</span>
                </div>
            </div>
        </ListGroupItem>
    </ListGroup>
</SimpleBar>
`;
</script>

<svelte:head>
	<title>Lists | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<UiContent />
<div class="page-content">
	<Container fluid>
		<BreadCrumb title="List" pageTitle="Base UI" />
		<Row>
			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="Default List" />

					<CardBody>
						<p class="text-muted">
							Use <code>ListGroup</code> attribute in an unordered
							list and
							<code>ListGroupItem</code> attribute to create a default
							list group.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem
									><i
										class="ri-bill-line align-middle me-2"
									/> Send the billing agreement</ListGroupItem
								>
								<ListGroupItem
									><i
										class="ri-file-copy-2-line align-middle me-2"
									/>Send over all the documentation.</ListGroupItem
								>
								<ListGroupItem
									><i
										class="ri-question-answer-line align-middle me-2"
									/>Meeting with daron to review the intake
									form</ListGroupItem
								>
								<ListGroupItem
									><i
										class="ri-secure-payment-line align-middle me-2"
									/>Check uikings theme and give customer
									support</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={defaultListCode}
								id="defaultListCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="Active Item" />

					<CardBody>
						<p class="text-muted">
							Use <code>active</code> attribute to
							<code>ListGroupItem</code> to indicate the current active
							selection.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem active
									>Send the billing agreement</ListGroupItem
								>
								<ListGroupItem
									>Send over all the documentation.</ListGroupItem
								>
								<ListGroupItem
									>Meeting with daron to review the intake
									form</ListGroupItem
								>
								<ListGroupItem
									>Check uikings theme and give customer
									support</ListGroupItem
								>
								<ListGroupItem
									>Start making a presentation</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={activeItemCode}
								id="activeItemCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="Disabled Items" />

					<CardBody>
						<p class="text-muted">
							Use <code>disabled</code> attribute to
							<code>ListGroupItem</code>
							to make it
							<em>appear</em> disabled.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem disabled>
									<div class="d-flex align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar1}
												alt=""
												class="avatar-xs rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-2">
											James Ballard
										</div>
									</div>
								</ListGroupItem>
								<ListGroupItem>
									<div class="d-flex align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar2}
												alt=""
												class="avatar-xs rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-2">
											Nancy Martino
										</div>
									</div>
								</ListGroupItem>
								<ListGroupItem>
									<div class="d-flex align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar3}
												alt=""
												class="avatar-xs rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-2">
											Henry Baird
										</div>
									</div>
								</ListGroupItem>
								<ListGroupItem>
									<div class="d-flex align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar3}
												alt=""
												class="avatar-xs rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-2">
											Erica Kernan
										</div>
									</div>
								</ListGroupItem>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={disabledItemCode}
								id="disabledItemCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="List with Link" />

					<CardBody>
						<p class="text-muted">
							Use <code>tag="a"</code> to create actionable list group
							items with hover, disabled, and active states by adding
							list-group-item-action.
						</p>
						<div class="live-preview">
							<ListGroup class="list-group-fill-success">
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action active"
									><i
										class="ri-download-2-fill align-middle me-2"
									/>Category Download</ListGroupItem
								>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action"
									><i
										class="ri-shield-check-line align-middle me-2"
									/>Security Access</ListGroupItem
								>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action"
									><i
										class="ri-database-2-line align-middle me-2"
									/>Storage folder</ListGroupItem
								>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action"
									><i
										class="ri-notification-3-line align-middle me-2"
									/>Push Notification</ListGroupItem
								>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action disabled"
									tabIndex="-1"
									><i
										class="ri-moon-fill align-middle me-2"
									/>Dark Mode</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode code={listlinkCode} id="listlinkCode" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="List with Button" />

					<CardBody>
						<p class="text-muted">
							Use <code>tag="button"</code> to create actionable list
							group items with hover, disabled, and active states by
							adding list-group-item-action.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem
									tag="button"
									class="list-group-item-action active"
									><i
										class="ri-reply-fill align-middle me-2"
									/>Reply</ListGroupItem
								>
								<ListGroupItem
									tag="button"
									class="list-group-item-action"
									><i
										class="ri-share-forward-fill align-middle me-2"
									/>Forward Message</ListGroupItem
								>
								<ListGroupItem
									tag="button"
									class="list-group-item-action"
									><i
										class="ri-equalizer-line align-middle me-2"
									/>Filter Message</ListGroupItem
								>
								<ListGroupItem
									tag="button"
									class="list-group-item-action"
									><i
										class="ri-delete-bin-5-line align-middle me-2"
									/>Delete Message</ListGroupItem
								>
								<ListGroupItem
									tag="button"
									class="list-group-item-action"
									disabled
									><i
										class="ri-forbid-line align-middle me-2"
									/>Block "Mark Spencer</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={listButtonCode}
								id="listButtonCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="Flush List" />

					<CardBody>
						<p class="text-muted">
							Use <code>flush</code> attribute to ListGroup to remove
							some borders and rounded corners to render list group
							items.
						</p>
						<div class="live-preview">
							<ListGroup flush>
								<ListGroupItem
									>Send the billing agreement</ListGroupItem
								>
								<ListGroupItem
									>Send over all the documentation.</ListGroupItem
								>
								<ListGroupItem
									>Meeting with daron to review the intake
									form</ListGroupItem
								>
								<ListGroupItem
									>Check uikings theme and give customer
									support</ListGroupItem
								>
								<ListGroupItem
									>Start making a presentation</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={flushListCode}
								id="flushListCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xl={12}>
				<Card>
					<PreviewCardHeader title="Horizontal List" />

					<CardBody>
						<p class="text-muted">
							Use <code>horizontal</code> attribute to ListGroup to
							change the layout of list group items from vertical to
							horizontal across all breakpoints.
						</p>
						<div class="live-preview">
							<ListGroup class="mb-3 list-group-horizontal">
								<ListGroupItem>Inbox</ListGroupItem>
								<ListGroupItem>Work</ListGroupItem>
								<ListGroupItem>Shopping</ListGroupItem>
							</ListGroup>
							<ListGroup
								class="justify-content-center mb-3 list-group-horizontal"
							>
								<ListGroupItem>Inbox</ListGroupItem>
								<ListGroupItem>Work</ListGroupItem>
								<ListGroupItem>Shopping</ListGroupItem>
							</ListGroup>
							<ListGroup
								class="justify-content-end list-group-horizontal"
							>
								<ListGroupItem>Inbox</ListGroupItem>
								<ListGroupItem>Work</ListGroupItem>
								<ListGroupItem>Shopping</ListGroupItem>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={horizontalListCode}
								id="horizontalListCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="Contextual Classes" />

					<CardBody>
						<p class="text-muted">
							Use <code>color="Required color"</code> to style list
							items with a stateful background and color.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem
									>Dapibus ac facilisis in</ListGroupItem
								>
								<ListGroupItem color="primary"
									>A simple primary list group item</ListGroupItem
								>
								<ListGroupItem color="secondary"
									>A simple secondary list group item</ListGroupItem
								>
								<ListGroupItem color="success"
									>A simple success list group item</ListGroupItem
								>
								<ListGroupItem color="danger"
									>A simple danger list group item</ListGroupItem
								>
								<ListGroupItem color="warning"
									>A simple warning list group item</ListGroupItem
								>
								<ListGroupItem color="info"
									>A simple info list group item</ListGroupItem
								>
								<ListGroupItem color="light"
									>A simple light list group item</ListGroupItem
								>
								<ListGroupItem color="dark"
									>A simple dark list group item</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={contextualClassCode}
								id="contextualClassCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="Contextual Classes with Link" />

					<CardBody>
						<p class="text-muted">
							Use <code>tag="a" href={null}</code> to add link. Note
							the addition of the hover styles here not present in
							the previous example.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple default list group item</ListGroupItem
								>
								<ListGroupItem
									color="primary"
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple primary list group item</ListGroupItem
								>
								<ListGroupItem
									color="secondary"
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple secondary list group item</ListGroupItem
								>
								<ListGroupItem
									color="success"
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple success list group item</ListGroupItem
								>
								<ListGroupItem
									color="danger"
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple danger list group item</ListGroupItem
								>
								<ListGroupItem
									color="warning"
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple warning list group item</ListGroupItem
								>
								<ListGroupItem
									color="info"
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple info list group item</ListGroupItem
								>
								<ListGroupItem
									color="light"
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple light list group item</ListGroupItem
								>
								<ListGroupItem
									color="dark"
									tag="a"
									href={null}
									class="list-group-item-action"
									>A simple dark list group item</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={contextualLinkCode}
								id="contextualLinkCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="Colored Lists" />

					<CardBody>
						<p class="text-muted">
							Use <code>list-group-fill-</code> with modifier class
							to style list items with a stateful background and color.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem
									>Dapibus ac facilisis in</ListGroupItem
								>
								<ListGroupItem class="list-group-fill-primary"
									>A simple primary list group item</ListGroupItem
								>
								<ListGroupItem class="list-group-fill-secondary"
									>A simple secondary list group item</ListGroupItem
								>
								<ListGroupItem class="list-group-fill-success"
									>A simple success list group item</ListGroupItem
								>
								<ListGroupItem class="list-group-fill-danger"
									>A simple danger list group item</ListGroupItem
								>
								<ListGroupItem class="list-group-fill-warning"
									>A simple warning list group item</ListGroupItem
								>
								<ListGroupItem class="list-group-fill-info"
									>A simple info list group item</ListGroupItem
								>
								<ListGroupItem class="list-group-fill-light"
									>A simple light list group item</ListGroupItem
								>
								<ListGroupItem class="list-group-fill-dark"
									>A simple dark list group item</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={coloredListCode}
								id="coloredListCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xl={12}>
				<Card>
					<PreviewCardHeader title="Custom Content" />

					<CardBody>
						<p class="text-muted">
							Add nearly any HTML within, even for linked list
							groups like the one below, with the help of <Link
								href="/getbootstrap.com/docs/5.1/utilities/flex/"
								>flexbox utilities</Link
							>.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action active"
								>
									<div class="float-end">Pending</div>
									<div class="d-flex mb-2 align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar1}
												alt=""
												class="avatar-sm rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-3">
											<h5 class="list-title fs-16 mb-1">
												Charlie Pritchard
											</h5>
											<p class="list-text mb-0 fs-13">
												12 min Ago
											</p>
										</div>
									</div>
									<p class="list-text mb-0">
										They all have something to say beyond
										the words on the page. They can come
										across as casual or neutral, exotic or
										graphic. That's why it's important to
										think about your message, then choose a
										font that fits. Cosby sweater eu banh
										mi, qui irure terry richardson ex squid.
									</p>
								</ListGroupItem>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action"
								>
									<div class="float-end">Pending</div>
									<div class="d-flex mb-2 align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar2}
												alt=""
												class="avatar-sm rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-3">
											<h5 class="list-title fs-16 mb-1">
												Dominic Charlton
											</h5>
											<p class="list-text mb-0 fs-13">
												12 min Ago
											</p>
										</div>
									</div>
									<p class="list-text mb-0">
										Trust fund seitan letterpress, keytar
										raw denim keffiyeh etsy art party before
										they sold out master cleanse gluten-free
										squid scenester freegan cosby sweater.
										Fanny pack portland seitan DIY, art
										party locavore wolf cliche high life
										echo park Austin.
									</p>
								</ListGroupItem>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action"
								>
									<div class="float-end">Rejected</div>
									<div class="d-flex mb-2 align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar3}
												alt=""
												class="avatar-sm rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-3">
											<h5 class="list-title fs-16 mb-1">
												Declan Long
											</h5>
											<p class="list-text mb-0 fs-13">
												12 min Ago
											</p>
										</div>
									</div>
									<p class="list-text mb-0">
										Big July earthquakes confound zany
										experimental vow. My girl wove six dozen
										plaid jackets before she quit. Six big
										devils from Japan quickly forgot how to
										waltz. try again until it looks right,
										and each assumenda labore aes Homo
										nostrud organic, assumenda labore
										aesthetic magna elements, buttons,
										everything.
									</p>
								</ListGroupItem>
								<ListGroupItem
									tag="a"
									href={null}
									class="list-group-item-action"
								>
									<div class="float-end">Successful</div>
									<div class="d-flex mb-2 align-items-center">
										<div class="flex-shrink-0">
											<img
												src={avatar4}
												alt=""
												class="avatar-sm rounded-circle"
											/>
										</div>
										<div class="flex-grow-1 ms-3">
											<h5 class="list-title fs-16 mb-1">
												Angela Bernier
											</h5>
											<p class="list-text mb-0 fs-13">
												5 days Ago
											</p>
										</div>
									</div>
									<p class="list-text mb-0">
										Just like in the image where we talked
										about using multiple fonts, you can see
										that the background in this graphic
										design is blurred. Whenever you put text
										on top of an image, it’s important that
										your viewers can understand the text,
										and sometimes that means applying a
										gaussian readable.
									</p>
								</ListGroupItem>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={customContentCode}
								id="customContentCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>

		<Row>
			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="List with Badges" />
					<CardBody>
						<p class="text-muted">
							Use badges to any list group item to show unread
							counts, activity, and more with the help of some <Link
								href="/getbootstrap.com/docs/5.1/utilities/"
								>utilities</Link
							>.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem
									class="d-flex justify-content-between align-items-center"
								>
									Send the billing agreement <span
										class="badge bg-success">High</span
									>
								</ListGroupItem>
								<ListGroupItem
									class="d-flex justify-content-between align-items-center"
								>
									Send over all the documentation
								</ListGroupItem>
								<ListGroupItem
									class="d-flex justify-content-between align-items-center"
								>
									Meeting with daron to review the intake form <span
										class="badge bg-danger">Low</span
									>
								</ListGroupItem>
								<ListGroupItem
									class="d-flex justify-content-between align-items-center"
								>
									Check uikings theme and give customer
									support <span class="badge bg-secondary"
										>Medium</span
									>
								</ListGroupItem>
								<ListGroupItem
									class="d-flex justify-content-between align-items-center"
								>
									Start making a presentation <span
										class="badge bg-success">High</span
									>
								</ListGroupItem>
							</ListGroup>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={listBadgeCode}
								id="listBadgeCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="List with Checkboxs" />

					<CardBody>
						<p class="text-muted">
							Use Bootstrap’s checkboxes within list group items
							and customize as needed.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem tag="label">
									<input
										class="form-check-input me-1"
										type="checkbox"
										value=""
									/>
									Declined Payment
								</ListGroupItem>
								<ListGroupItem tag="label">
									<input
										class="form-check-input me-1"
										type="checkbox"
										value=""
										checked
									/>
									Delivery Error
								</ListGroupItem>
								<ListGroupItem tag="label">
									<input
										class="form-check-input me-1"
										type="checkbox"
										value=""
										checked
									/>
									Wrong Amount
								</ListGroupItem>
								<ListGroupItem tag="label">
									<input
										class="form-check-input me-1"
										type="checkbox"
										value=""
									/>
									Wrong Address
								</ListGroupItem>
								<ListGroupItem tag="label">
									<input
										class="form-check-input me-1"
										type="checkbox"
										value=""
									/>
									Wrong UX/UI Solution
								</ListGroupItem>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={listCheckboxCode}
								id="listCheckboxCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="List with Radios" />
					<CardBody>
						<p class="text-muted">
							Use Bootstrap’s radios within list group items and
							customize as needed.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem tag="label">
									<input
										class="form-check-input fs-14 mt-0 align-middle me-1"
										name="exampleRadios"
										type="radio"
										value=""
									/>
									Declined Payment
								</ListGroupItem>
								<ListGroupItem tag="label">
									<input
										class="form-check-input fs-14 mt-0 align-middle me-1"
										name="exampleRadios"
										type="radio"
										value=""
										checked
									/>
									Delivery Error
								</ListGroupItem>
								<ListGroupItem tag="label">
									<input
										class="form-check-input fs-14 mt-0 align-middle me-1"
										name="exampleRadios"
										type="radio"
										value=""
									/>
									Wrong Amount
								</ListGroupItem>
								<ListGroupItem tag="label">
									<input
										class="form-check-input fs-14 mt-0 align-middle me-1"
										name="exampleRadios"
										type="radio"
										value=""
									/>
									Wrong Address
								</ListGroupItem>
								<ListGroupItem tag="label">
									<input
										class="form-check-input fs-14 mt-0 align-middle me-1"
										name="exampleRadios"
										type="radio"
										value=""
									/>
									Wrong UX/UI Solution
								</ListGroupItem>
							</ListGroup>
						</div>
						<div class="d-none code-view">
							<PrismCode
								code={listRadioCode}
								id="listRadioCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="List with Icon" />
					<CardBody>
						<p class="text-muted">
							Use icons to any list group item to show icons to
							list group items.
						</p>
						<div class="live-preview">
							<ListGroup>
								<ListGroupItem
									><i
										class="mdi mdi-check-bold align-middle lh-1 me-2"
									/> Send the billing agreement</ListGroupItem
								>
								<ListGroupItem
									><i
										class="mdi mdi-check-bold align-middle lh-1 me-2"
									/> Send over all the documentation.</ListGroupItem
								>
								<ListGroupItem
									><i
										class="mdi mdi-check-bold align-middle lh-1 me-2"
									/> Meeting with daron to review the intake form</ListGroupItem
								>
								<ListGroupItem
									><i
										class="mdi mdi-check-bold align-middle lh-1 me-2"
									/> Check uikings theme and give customer support</ListGroupItem
								>
								<ListGroupItem
									><i
										class="mdi mdi-check-bold align-middle lh-1 me-2"
									/> Start making a presentation</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode code={listIconCode} id="listIconCode" />
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="List with Numbered" />

					<CardBody>
						<p class="text-muted">
							Use <code>list-group-numbered</code> class
							(optionally use an <code>&lt;ol&gt;</code> element) to
							show numbered list group items.
						</p>
						<div class="live-preview">
							<ListGroup class="list-group-numbered">
								<ListGroupItem
									>Send the billing agreement</ListGroupItem
								>
								<ListGroupItem
									>Send over all the documentation.</ListGroupItem
								>
								<ListGroupItem
									>Meeting with daron to review the intake
									form</ListGroupItem
								>
								<ListGroupItem
									>Check uikings theme and give customer
									support</ListGroupItem
								>
								<ListGroupItem
									>Start making a presentation</ListGroupItem
								>
							</ListGroup>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={listNumberedCode}
								id="listNumberedCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>

			<Col xxl={4} xl={6}>
				<Card>
					<PreviewCardHeader title="Custom Content Lists" />
					<CardBody>
						<p>
							Add nearly any HTML within, even for linked list
							groups like the one below, with the help of <Link
								href="/getbootstrap.com/docs/5.1/utilities/flex/"
								>flexbox utilities</Link
							>.
						</p>
						<div class="live-preview">
							<div data-simplebar style="max-height: 215px">
								<ListGroup class="mb-1">
									<ListGroupItem>
										<div class="d-flex align-items-center">
											<div class="flex-grow-1">
												<div class="d-flex">
													<div
														class="flex-shrink-0 avatar-xs"
													>
														<div
															class="avatar-title bg-danger-subtle text-danger rounded"
														>
															<i
																class="ri-netflix-fill"
															/>
														</div>
													</div>
													<div
														class="flex-shrink-0 ms-2"
													>
														<h6 class="fs-14 mb-0">
															Netfilx
														</h6>
														<small
															class="text-muted"
															>2 min Ago</small
														>
													</div>
												</div>
											</div>
											<div class="flex-shrink-0">
												<span class="text-danger"
													>-$25.50</span
												>
											</div>
										</div>
									</ListGroupItem>
									<ListGroupItem>
										<div class="d-flex align-items-center">
											<div class="flex-grow-1">
												<div class="d-flex">
													<div
														class="flex-shrink-0 avatar-xs"
													>
														<div
															class="avatar-title bg-success-subtle text-success rounded"
														>
															<i
																class="ri-spotify-fill"
															/>
														</div>
													</div>
													<div
														class="flex-shrink-0 ms-2"
													>
														<h6 class="fs-14 mb-0">
															Spotify
														</h6>
														<small
															class="text-muted"
															>5 days Ago</small
														>
													</div>
												</div>
											</div>
											<div class="flex-shrink-0">
												<span class="text-success"
													>$48.25</span
												>
											</div>
										</div>
									</ListGroupItem>
									<ListGroupItem>
										<div class="d-flex align-items-center">
											<div class="flex-grow-1">
												<div class="d-flex">
													<div class="flex-shrink-0">
														<img
															src={avatar2}
															alt=""
															class="avatar-xs rounded"
														/>
													</div>
													<div
														class="flex-shrink-0 ms-2"
													>
														<h6 class="fs-14 mb-0">
															Emily Slater
														</h6>
														<small
															class="text-muted"
															>8 days Ago</small
														>
													</div>
												</div>
											</div>
											<div class="flex-shrink-0">
												<span class="text-success"
													>$354.90</span
												>
											</div>
										</div>
									</ListGroupItem>
									<ListGroupItem>
										<div class="d-flex align-items-center">
											<div class="flex-grow-1">
												<div class="d-flex">
													<div
														class="flex-shrink-0 avatar-xs"
													>
														<div
															class="avatar-title bg-secondary-subtle text-secondary rounded"
														>
															<i
																class="ri-paypal-fill"
															/>
														</div>
													</div>
													<div
														class="flex-shrink-0 ms-2"
													>
														<h6 class="fs-14 mb-0">
															Paypal
														</h6>
														<small
															class="text-muted"
															>1 month Ago</small
														>
													</div>
												</div>
											</div>
											<div class="flex-shrink-0">
												<span class="text-danger"
													>-$12.22</span
												>
											</div>
										</div>
									</ListGroupItem>
									<ListGroupItem>
										<div class="d-flex align-items-center">
											<div class="flex-grow-1">
												<div class="d-flex">
													<div class="flex-shrink-0">
														<img
															src={avatar3}
															alt=""
															class="avatar-xs rounded"
														/>
													</div>
													<div
														class="flex-shrink-0 ms-2"
													>
														<h6 class="fs-14 mb-0">
															Harvey Wells
														</h6>
														<small
															class="text-muted"
															>4 month Ago</small
														>
													</div>
												</div>
											</div>
											<div class="flex-shrink-0">
												<span class="text-success"
													>-$459.78</span
												>
											</div>
										</div>
									</ListGroupItem>
								</ListGroup>
							</div>
						</div>

						<div class="d-none code-view">
							<PrismCode
								code={customListCode}
								id="customListCode"
							/>
						</div>
					</CardBody>
				</Card>
			</Col>
		</Row>
	</Container>
</div>
