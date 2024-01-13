<script>
	import {
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Label,
		NavItem,
		NavLink,
		Offcanvas,
		OffcanvasBody,
		Row,
		Dropdown,
		Tooltip,
		Collapse,
		ButtonGroup,
		Button,
		ButtonDropdown,
	} from "sveltestrap";
	import Link from "svelte-link";
	import data from "../../common/data/mailbox";
	let isRight = false;
	const toggleRightCanvas = () => {
		isRight = !isRight;
	};
	import avatar3 from '../../assets/images/users/avatar-3.jpg'
	import avatar1 from '../../assets/images/users/avatar-1.jpg'
	import img2 from '../../assets/images/small/img-2.jpg'
	import img6 from '../../assets/images/small/img-6.jpg'
</script>

<div class="email-content">
	<div class="p-4 pb-0">
		<div class="border-bottom border-bottom-dashed">
			<Row class="mt-n2 mb-3 mb-sm-0">
				<Col class="col-sm-auto order-1 d-block d-lg-none">
					<button
						type="button"
						class="btn btn-soft-success btn-icon btn-sm fs-16 email-menu-btn">
						<i class="ri-menu-2-fill align-bottom" />
					</button>
				</Col>
				<div class="col-sm order-3 order-sm-2">
					<div class="hstack gap-sm-1 align-items-center flex-wrap email-topbar-link">
						<div class="form-check checkbox-wrapper-mail fs-14 m-0">
							<input
								class="form-check-input"
								type="checkbox"
								value=""
								id="flexCheck18"
							/>
							<Label class="form-check-label" for="flexCheck18" />
						</div>
						<Button
							id="archive"
							color=""
							class="btn-ghost-secondary btn-icon btn-sm fs-16"
						>
							<i class="ri-inbox-archive-fill align-bottom" />
						</Button>
						<Tooltip target="archive" placement="top">Archive</Tooltip
						>

						<Button
							id="reportspam"
							color=""
							class="btn btn-ghost-secondary btn-icon btn-sm fs-16"
						>
							<i class="ri-error-warning-fill align-bottom" />
						</Button>
						<Tooltip target="reportspam" placement="top">Report Spam</Tooltip
						>
						<Button
							color=""
							class="btn btn-ghost-secondary btn-icon btn-sm fs-16 remove-mail"
							id="trash"
						>
							<i class="ri-delete-bin-5-fill align-bottom" />
						</Button>
						<Tooltip target="trash" placement="top">Trash</Tooltip>

						<div class="vr align-self-center mx-2" />
						<Button
							class="btn btn-ghost-secondary btn-icon btn-sm fs-16"
							color=""
							id="labels"
						>
							<i class="ri-mail-open-fill align-bottom" />
						</Button>
						<Tooltip target="labels" placement="top">Labels</Tooltip
						>
						<Button
							color=""
							class="btn btn-ghost-secondary btn-icon btn-sm fs-16"
							id="labels1"
						>
							<i class="ri-price-tag-3-fill align-bottom" />
						</Button>
						<Tooltip target="labels1" placement="top">Labels</Tooltip
						>
					</div>
				</div>
				<div class="col-auto order-2 order-sm-3">
					<div class="d-flex gap-sm-1 email-topbar-link">
						<button
							type="button"
							class="btn btn-ghost-secondary btn-icon btn-sm fs-16"
						>
							<i class="ri-refresh-line align-bottom" />
						</button>
						<Dropdown>
							<DropdownToggle
								tag="button"
								class="btn btn-ghost-secondary btn-icon btn-sm fs-16 p-0"
								color="">
								<i class="ri-more-2-fill align-bottom" />
							</DropdownToggle>
							<DropdownMenu class="dropdown-menu-end">
								<DropdownItem>Mark as Unread</DropdownItem>
								<DropdownItem>Mark as Important</DropdownItem>
								<DropdownItem>Add to Tasks</DropdownItem>
								<DropdownItem>Add Star</DropdownItem>
								<DropdownItem>Mute</DropdownItem>
							</DropdownMenu>
						</Dropdown>
					</div>
				</div>
			</Row>

			<Row class="align-items-center mt-3">
				<Col>
					<ul
						class="nav nav-tabs nav-tabs-custom nav-success gap-1 text-center border-bottom-0"
						role="tablist">
						<NavItem>
							<NavLink class="fw-semibold active" href={null}>
								<i
									class="ri-inbox-fill align-bottom d-inline-block"
								/>
								<span class="ms-1 d-none d-sm-inline-block"
									>Primary</span
								>
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink class="fw-semibold" href={null}>
								<i
									class="ri-group-fill align-bottom d-inline-block"
								/>
								<span class="ms-1 d-none d-sm-inline-block"
									>Social</span
								>
							</NavLink>
						</NavItem>
						<NavItem>
							<NavLink class="fw-semibold" href={null}>
								<i
									class="ri-price-tag-3-fill align-bottom d-inline-block"
								/>
								<span class="ms-1 d-none d-sm-inline-block"
									>Promotions</span
								>
							</NavLink>
						</NavItem>
					</ul>
				</Col>
				<div class="col-auto">
					<div class="text-muted">1-50 of 154</div>
				</div>
			</Row>
		</div>

		<div
			class="message-list-content mx-n4 px-4 message-list-scroll"
			data-simplebar
		>
			<ul class="message-list">
				{#each data.mailbox as item}
					<li class={item.unread ? "unread" : null}>
						<div class="col-mail col-mail-1">
							<div class="form-check checkbox-wrapper-mail fs-14">
								<input
									class="form-check-input"
									type="checkbox"
									value=""
									id={item.forId}
								/>
								<Label
									class="form-check-label"
									for={item.forId}
								/>
							</div>
							<button
								type="button"
								class="btn avatar-xs p-0 favourite-btn fs-15 active">
								<i class="ri-star-fill" />
							</button>
							<Link href="{null}" class="title">{item.name}</Link>
						</div>
						<div class="col-mail col-mail-2">
							<!-- svelte-ignore a11y-click-events-have-key-events -->
							<div class="subject pointer"
								on:click={toggleRightCanvas}
								style="cursor: pointer;">
								{#if item.badge}
									<span
										class={"badge me-2 bg-" +
											item.badgeClass}>{item.badge}</span
									>
								{/if}
								{item.subject} -
								<span class="teaser">{item.teaser}</span>
							</div>
							<div class="date">{item.date}</div>
						</div>
					</li>
				{/each}
			</ul>
		</div>
	</div>
</div>

<div class="email-detail-content">
	<Offcanvas
		class="offcanvas-p-0"
		isOpen={isRight}
		placement="end"
		id="offcanvasRight"
	>
		<OffcanvasBody class="overflow-hidden">
			<div class="pb-4 border-bottom border-bottom-dashed">
				<Row>
					<Col>
						<div class="">
							<button
								type="button"
								class="btn btn-soft-danger btn-icon btn-sm fs-16 close-btn-email"
								on:click={toggleRightCanvas}>
								<i class="ri-close-fill align-bottom" />
							</button>
						</div>
					</Col>
					<Col class="col-auto">
						<div class="hstack gap-sm-1 align-items-center flex-wrap email-topbar-link"
						>
							<button
								type="button"
								class="btn btn-ghost-secondary btn-icon btn-sm fs-16 favourite-btn active">
								<i class="ri-star-fill align-bottom" />
							</button>
							<button
								class="btn btn-ghost-secondary btn-icon btn-sm fs-16">
								<i class="ri-printer-fill align-bottom" />
							</button>
							<button
								class="btn btn-ghost-secondary btn-icon btn-sm fs-16">
								<i class="ri-delete-bin-5-fill align-bottom" />
							</button>
							<Dropdown>
								<DropdownToggle
									tag="button"
									class="btn btn-ghost-secondary btn-icon btn-sm fs-16 p-0"
									color=""
								>
									<i class="ri-more-2-fill align-bottom" />
								</DropdownToggle>
								<DropdownMenu class="dropdown-menu-end">
									<DropdownItem>Mark as Unread</DropdownItem>
									<DropdownItem
										>Mark as Important</DropdownItem
									>
									<DropdownItem>Add to Tasks</DropdownItem>
									<DropdownItem>Add Star</DropdownItem>
									<DropdownItem>Mute</DropdownItem>
								</DropdownMenu>
							</Dropdown>
						</div>
					</Col>
				</Row>
			</div>
			<div class="mx-n4 px-4 email-detail-content-scroll" data-simplebar>
				<div class="mt-4 mb-3">
					<h5 class="fw-bold">New updates for Skote Theme</h5>
				</div>
				<div class="accordion accordion-flush">
					<div class="accordion-item border-dashed left">
						<div class="accordion-header">
							<Link
								role="button"
								href={null}
								class="btn w-100 text-start px-0 bg-transparent shadow-none collapsed"
								id="email-collapseOne">
								<div class="d-flex align-items-center text-muted"
								>
									<div class="flex-shrink-0 avatar-xs me-3">
										<img
											src={avatar3}
											alt=""
											class="img-fluid rounded-circle"
										/>
									</div>
									<div class="flex-grow-1 overflow-hidden">
										<h5 class="fs-14 text-truncate mb-0">
											Jack Davis
										</h5>
										<div class="text-truncate fs-12">
											to: me
										</div>
									</div>
									<div class="flex-shrink-0 align-self-start">
										<div class="text-muted fs-12">
											09 Jan 2022, 11:12 AM
										</div>
									</div>
								</div>
							</Link>
						</div>

						<Collapse
							toggler="#email-collapseOne"
							class="accordion-collapse collapse"
						>
							<div class="accordion-body text-body px-0">
								<div>
									<p>Hi,</p>
									<p>
										Praesent dui ex, dapibus eget mauris ut,
										finibus vestibulum enim. Quisque arcu
										leo, facilisis in fringilla id, luctus
										in tortor.
									</p>
									<p>
										Sed elementum turpis eu lorem interdum,
										sed porttitor eros commodo. Nam eu
										venenatis tortor, id lacinia diam. Sed
										aliquam in dui et porta. Sed bibendum
										orci non tincidunt ultrices.
									</p>
									<p>Sincerly,</p>

									<div class="d-flex gap-3">
										<div class="border rounded avatar-xl h-auto"
										>
											<img
												src={img2}
												alt=""
												class="img-fluid rouned-top"
											/>
											<div class="py-2 text-center">
												<Link
													href="{null}"
													class="d-block fw-semibold"
													>Download</Link
												>
											</div>
										</div>
										<div class="border rounded avatar-xl h-auto"
										>
											<img
												src={img6}
												alt=""
												class="img-fluid rouned-top"
											/>
											<div class="py-2 text-center">
												<Link
													href="{null}"
													class="d-block fw-semibold"
													>Download</Link
												>
											</div>
										</div>
									</div>
								</div>
							</div>
						</Collapse>
					</div>

					<div class="accordion-item border-dashed">
						<div class="accordion-header">
							<Link
								href={null}
								role="button"
								class="btn w-100 text-start px-0 bg-transparent shadow-none collapsed"
								data-bs-toggle="collapse"
								id="email-collapseTwo"
								aria-expanded="true"
								aria-controls="email-collapseTwo">
								<div class="d-flex align-items-center text-muted"
								>
									<div class="flex-shrink-0 avatar-xs me-3">
										<img
											src={avatar1}
											alt=""
											class="img-fluid rounded-circle"
										/>
									</div>
									<div class="flex-grow-1 overflow-hidden">
										<h5 class="fs-14 text-truncate mb-0">
											Anna Adame
										</h5>
										<div class="text-truncate fs-12">
											to: jackdavis@email.com
										</div>
									</div>
									<div class="flex-shrink-0 align-self-start">
										<div class="text-muted fs-12">
											09 Jan 2022, 02:15 PM
										</div>
									</div>
								</div>
							</Link>
						</div>

						<Collapse
							toggler="#email-collapseTwo"
							class="accordion-collapse collapse"
						>
							<div class="accordion-body text-body px-0">
								<div>
									<p>Hi,</p>
									<p>
										If several languages coalesce, the
										grammar of the resulting language is
										more simple and regular than that of the
										individual.
									</p>
									<p>Thank you</p>
								</div>
							</div>
						</Collapse>
					</div>

					<div class="accordion-item border-dashed">
						<div class="accordion-header">
							<Link
								href={null}
								role="button"
								class="btn w-100 text-start px-0 bg-transparent shadow-none"
								data-bs-toggle="collapse"
								id="email-collapseThree"
								aria-expanded="true"
								aria-controls="email-collapseThree">
								<div class="d-flex align-items-center text-muted"
								>
									<div class="flex-shrink-0 avatar-xs me-3">
										<img
											src={avatar3}
											alt=""
											class="img-fluid rounded-circle"
										/>
									</div>
									<div class="flex-grow-1 overflow-hidden">
										<h5 class="fs-14 text-truncate mb-0">
											Jack Davis
										</h5>
										<div class="text-truncate fs-12">
											to: me
										</div>
									</div>
									<div class="flex-shrink-0 align-self-start">
										<div class="text-muted fs-12">
											10 Jan 2022, 10:08 AM
										</div>
									</div>
								</div>
							</Link>
						</div>

						<Collapse
							toggler="#email-collapseThree"
							class="accordion-collapse collapse"
							defaultOpen
						>
							<div class="accordion-body text-body px-0">
								<div>
									<p>Hi,</p>
									<p>
										Everyone realizes why a new common
										language would be desirable: one could
										refuse to pay expensive translators. To
										achieve this, it would be necessary to
										have uniform grammar pronunciation.
									</p>
									<p>Thank you</p>
								</div>
							</div>
						</Collapse>
					</div>
				</div>
			</div>
		</OffcanvasBody>
		<div class="mt-auto p-4">
			<form class="mt-2">
				<div>
					<Label for="exampleFormControlTextarea1" class="form-label"
						>Reply :</Label>
					<textarea
						class="form-control border-bottom-0 rounded-top rounded-0 border"
						id="exampleFormControlTextarea1"
						rows="3"
						placeholder="Enter message"
					/>
					<div class="bg-light px-2 py-1 rouned-bottom border">
						<Row>
							<Col>
								<ButtonGroup>
									<Button size="sm" color="light" id="Bold1"
										><i
											class="ri-bold align-bottom"
										/></Button
									>
									<Button size="sm" color="light" id="Italic1"
										><i
											class="ri-italic align-bottom"
										/></Button
									>
									<Button size="sm" color="light" id="Link1"
										><i
											class="ri-link align-bottom"
										/></Button
									>
									<Button size="sm" color="light" id="Image1"
										><i
											class="ri-image-2-line align-bottom"
										/></Button
									>
								</ButtonGroup>
								<Tooltip placement="top" target="Bold1"
									>Bold</Tooltip
								>
								<Tooltip placement="top" target="Italic1"
									>Italic</Tooltip
								>
								<Tooltip placement="top" target="Link1"
									>Link</Tooltip
								>
								<Tooltip placement="top" target="Image1"
									>Image</Tooltip
								>
							</Col>
							<Col class="col-auto">
								<ButtonDropdown>
									<Button color="success" class="btn-sm"
										><i
											class="ri-send-plane-2-fill align-bottom"
										/></Button
									>
									<DropdownToggle
										tag="button"
										class="btn btn-success btn-sm"
										split
									/>
									<DropdownMenu>
										<DropdownItem
											><i
												class="ri-timer-line text-muted me-1 align-bottom"
											/> Schedule Send</DropdownItem
										>
									</DropdownMenu>
								</ButtonDropdown>
							</Col>
						</Row>
					</div>
				</div>
			</form>
		</div>
	</Offcanvas>
</div>
