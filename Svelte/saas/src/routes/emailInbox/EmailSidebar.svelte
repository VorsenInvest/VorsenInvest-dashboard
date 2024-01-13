<script lang="ts">
	import {
		// Modal,
		ModalBody,
		ModalHeader,
		Input,
		Progress,
		Dropdown,
		DropdownToggle,
		DropdownMenu,
		DropdownItem,
		Label,
		Card,
		CardHeader,
		CardBody,
		Row,
		Col,
	} from "sveltestrap";
	import Link from "svelte-link";
	import { PlusCircleIcon } from "svelte-feather-icons";
    import Modal from "../../Components/Common/Modal.svelte";
	let showFileModal = false;
    const fileToggle = () => (showFileModal = !showFileModal);

	let open = false;
	const toggle = () => (open = !open);

	import avatar2 from "../../assets/images/users/avatar-2.jpg";
	import avatar3 from "../../assets/images/users/avatar-3.jpg";
	import avatar4 from "../../assets/images/users/avatar-4.jpg";
	import avatar5 from "../../assets/images/users/avatar-5.jpg";

	const chatBox = (value) => {
		const element = document.getElementById("emailchat-detailElem");
		element.style.display = value;
	};
	const chatData = [
		{
			id: 1,
			img: avatar2,
			name: "Scott Median",
			caption: "Hello ! are you there?",
		},
		{
			id: 2,
			img: avatar4,
			name: "Julian Rosa",
			caption: "What about our next..",
		},
		{
			id: 3,
			img: avatar3,
			name: "David Medina",
			caption: "Yeah everything is fine",
		},
		{ id: 4, img: avatar5, name: "Jay Baker", caption: "Wow that's great" },
	];

	let setInfo = [];
</script>

<div class="email-menu-sidebar">
	<div class="p-4 d-flex flex-column h-100">
		<div class="pb-4 border-bottom border-bottom-dashed">
			<button
				type="button"
				class="btn btn-danger w-100"
				on:click={fileToggle}
			>
				<PlusCircleIcon class="icon-xs me-1 icon-dual-light" />
				Compose
			</button>
		</div>

		<div class="mx-n4 px-4 email-menu-sidebar-scroll" data-simplebar>
			<div class="mail-list mt-3 h-auto">
				<Link href={null} >
					<i class="ri-mail-fill me-3 align-middle fw-medium" />
					<span class="mail-list-link">All</span>
				</Link>
				<Link href={null}>
					<i
						class="ri-inbox-archive-fill me-3 align-middle fw-medium"
					/>
					Inbox
					<span class="badge bg-success-subtle text-success ms-auto"
						>5</span
					>
				</Link>
				<Link href={null}>
					<i
						class="ri-send-plane-2-fill me-3 align-middle fw-medium"
					/>{" "}
					Sent
				</Link>
				<Link href={null}>
					<i class="ri-edit-2-fill me-3 align-middle fw-medium" />
					Draft
				</Link>
				<Link href={null}>
					<i
						class="ri-error-warning-fill me-3 align-middle fw-medium"
					/>
					Spam
				</Link>
				<Link href={null}>
					<i
						class="ri-delete-bin-5-fill me-3 align-middle fw-medium"
					/>
					Trash
				</Link>
				<Link href={null}>
					<i class="ri-star-fill me-3 align-middle fw-medium" />
					Starred
				</Link>
				<Link href={null}>
					<i
						class="ri-price-tag-3-fill me-3 align-middle fw-medium"
					/>
					Important
				</Link>
			</div>

			<div>
				<h5 class="fs-12 text-uppercase text-muted mt-4">Labels</h5>

				<div class="mail-list mt-1">
					<Link href={null}>
						<span
							class="ri-checkbox-blank-circle-line me-2 text-info"
						/>{" "}
						Theme Support{" "}
						<span
							class="badge bg-success-subtle text-success ms-auto"
							>3</span
						>
					</Link>
					<Link href={null}>
						<span
							class="ri-checkbox-blank-circle-line me-2 text-warning"
						/>{" "}
						Freelance
					</Link>
					<Link href={null}>
						<span
							class="ri-checkbox-blank-circle-line me-2 text-primary"
						/>{" "}
						Social
					</Link>
					<Link href={null}>
						<span
							class="ri-checkbox-blank-circle-line me-2 text-danger"
						/>{" "}
						Friends
						<span
							class="badge bg-success-subtle text-success ms-auto"
							>2</span
						>
					</Link>
					<Link href={null}>
						<span
							class="ri-checkbox-blank-circle-line me-2 text-success"
						/>{" "}
						Family
					</Link>
				</div>
			</div>

			<div class="border-top border-top-dashed pt-3 mt-3">
				<Link
					href={null}
					class="btn btn-icon btn-sm btn-soft-info rounded-pill float-end"
				>
					<i class="bx bx-plus fs-16" />
				</Link>
				<h5 class="fs-12 text-uppercase text-muted mb-3">Chat</h5>

				<div class="mt-2 vstack gap-3 email-chat-list mx-n4">
					{#each chatData as item}
						<Link href={null} class="d-flex align-items-center">
							<div class="flex-shrink-0 me-2 avatar-xxs">
								<img
									class="img-fluid rounded-circle"
									src={item.img}
									alt=""
								/>
							</div>

							<!-- svelte-ignore a11y-click-events-have-key-events -->
							<div
								class="flex-grow-1 chat-user-box overflow-hidden"
								on:click={() => {
									chatBox("block");
									setInfo = item;
								}}
							>
								<h5 class="fs-13 text-truncate mb-0">
									{item.name}
								</h5>
								<small class="text-muted text-truncate mb-0">
									{item.caption}
								</small>
							</div>
						</Link>
					{/each}
				</div>
			</div>
		</div>

		<div class="mt-auto">
			<h5 class="fs-13">1.75 GB of 10 GB used</h5>
			<Progress color="success" class="progress-sm" value={25} />
		</div>
	</div>
</div>

<div class="email-chat-detail" id="emailchat-detailElem">
	<Card class="mb-0">
		<CardHeader class="align-items-center d-flex bg-primary text-white-50">
			<div class="flex-grow-1">
				<h5 class="fs-13 text-white mb-1 profile-username">
					{setInfo.name}
				</h5>
				<p class="mb-0 fs-12 lh-1">Active</p>
			</div>
			<div class="flex-shrink-0">
				<div class="mt-n3 me-n3">
					<button
						type="button"
						class="btn btn-link text-white fs-16 text-decoration-none"
						id="emailchat-btn-close"
						on:click={() => chatBox("none")}
						><i class="ri-close-fill" /></button
					>
				</div>
			</div>
		</CardHeader>

		<CardBody class="p-0">
			<div id="users-chat">
				<div
					data-simplebar
					class="chat-conversation p-3"
					id="chat-conversation"
					style="height: 250px"
				>
					<ul
						class="list-unstyled chat-conversation-list chat-sm"
						id="users-conversation"
					>
						<li class="chat-list left">
							<div class="conversation-list">
								<div class="chat-avatar">
									<img src={setInfo.img} alt="" />
								</div>
								<div class="user-chat-content">
									<div class="ctext-wrap">
										<div class="ctext-wrap-content">
											<p class="mb-0 ctext-content">
												Good morning 😊
											</p>
										</div>

										<Dropdown
											class="align-self-start message-box-drop"
										>
											<DropdownToggle
												tag="a"
												role="button"
												color=""
												class="p-0"
											>
												<i class="ri-more-2-fill" />
											</DropdownToggle>
											<DropdownMenu>
												<DropdownItem
													><i
														class="ri-reply-line me-2 text-muted align-bottom"
													/>Reply</DropdownItem
												>
												<DropdownItem
													><i
														class="ri-file-copy-line me-2 text-muted align-bottom"
													/>Copy</DropdownItem
												>
												<DropdownItem
													><i
														class="ri-delete-bin-5-line me-2 text-muted align-bottom"
													/>Delete</DropdownItem
												>
											</DropdownMenu>
										</Dropdown>
									</div>
									<div class="conversation-name">
										<small class="text-muted time"
											>09:07 am</small
										>
										<span
											class="text-success check-message-icon"
											><i
												class="ri-check-double-line align-bottom"
											/></span
										>
									</div>
								</div>
							</div>
						</li>

						<li class="chat-list right">
							<div class="conversation-list">
								<div class="user-chat-content">
									<div class="ctext-wrap">
										<div class="ctext-wrap-content">
											<p class="mb-0 ctext-content">
												Good morning, How are you? What
												about our next meeting?
											</p>
										</div>
										<Dropdown
											class="align-self-start message-box-drop"
										>
											<DropdownToggle
												tag="a"
												role="button"
												color=""
												class="p-0"
											>
												<i class="ri-more-2-fill" />
											</DropdownToggle>
											<DropdownMenu>
												<DropdownItem
													><i
														class="ri-reply-line me-2 text-muted align-bottom"
													/>Reply</DropdownItem
												>
												<DropdownItem
													><i
														class="ri-file-copy-line me-2 text-muted align-bottom"
													/>Copy</DropdownItem
												>
												<DropdownItem
													><i
														class="ri-delete-bin-5-line me-2 text-muted align-bottom"
													/>Delete</DropdownItem
												>
											</DropdownMenu>
										</Dropdown>
									</div>
									<div class="conversation-name">
										<small class="text-muted time"
											>09:08 am</small
										>
										<span
											class="text-success check-message-icon"
											><i
												class="ri-check-double-line align-bottom"
											/></span
										>
									</div>
								</div>
							</div>
						</li>

						<li class="chat-list left">
							<div class="conversation-list">
								<div class="chat-avatar">
									<img src={setInfo.img} alt="" />
								</div>
								<div class="user-chat-content">
									<div class="ctext-wrap">
										<div class="ctext-wrap-content">
											<p class="mb-0 ctext-content">
												Yeah everything is fine. Our
												next meeting tomorrow at 10.00
												AM
											</p>
										</div>
										<Dropdown
											class="align-self-start message-box-drop"
										>
											<DropdownToggle
												tag="a"
												role="button"
												color=""
												class="p-0"
											>
												<i class="ri-more-2-fill" />
											</DropdownToggle>
											<DropdownMenu>
												<DropdownItem
													><i
														class="ri-reply-line me-2 text-muted align-bottom"
													/>Reply</DropdownItem
												>
												<DropdownItem
													><i
														class="ri-file-copy-line me-2 text-muted align-bottom"
													/>Copy</DropdownItem
												>
												<DropdownItem
													><i
														class="ri-delete-bin-5-line me-2 text-muted align-bottom"
													/>Delete</DropdownItem
												>
											</DropdownMenu>
										</Dropdown>
									</div>
									<div class="conversation-name">
										<small class="text-muted time"
											>09:10 am</small
										>
										<span
											class="text-success check-message-icon"
											><i
												class="ri-check-double-line align-bottom"
											/></span
										>
									</div>
								</div>
							</div>
						</li>

						<li class="chat-list right">
							<div class="conversation-list">
								<div class="user-chat-content">
									<div class="ctext-wrap">
										<div class="ctext-wrap-content">
											<p class="mb-0 ctext-content">
												Wow that's great
											</p>
										</div>
										<Dropdown
											class="align-self-start message-box-drop"
										>
											<DropdownToggle
												tag="a"
												role="button"
												color=""
												class="p-0"
											>
												<i class="ri-more-2-fill" />
											</DropdownToggle>
											<DropdownMenu>
												<DropdownItem
													><i
														class="ri-reply-line me-2 text-muted align-bottom"
													/>Reply</DropdownItem
												>
												<DropdownItem
													><i
														class="ri-file-copy-line me-2 text-muted align-bottom"
													/>Copy</DropdownItem
												>
												<DropdownItem
													><i
														class="ri-delete-bin-5-line me-2 text-muted align-bottom"
													/>Delete</DropdownItem
												>
											</DropdownMenu>
										</Dropdown>
									</div>
									<div class="conversation-name">
										<small class="text-muted time"
											>09:12 am</small
										>
										<span
											class="text-success check-message-icon"
											><i
												class="ri-check-double-line align-bottom"
											/></span
										>
									</div>
								</div>
							</div>
						</li>
					</ul>
				</div>
			</div>

			<div class="border-top border-top-dashed">
				<Row class="g-2 mx-3 mt-2 mb-3">
					<Col class="col">
						<div class="position-relative">
							<input
								type="text"
								class="form-control border-light bg-light"
								placeholder="Enter Message..."
							/>
						</div>
					</Col>
					<Col class="col-auto">
						<button type="submit" class="btn btn-info"
							><i class="mdi mdi-send" /></button
						>
					</Col>
				</Row>
			</div>
		</CardBody>
	</Card>
</div>

<!-- <Modal id="composemodal" class="" isOpen={open} {toggle} centered>
	<ModalHeader class="p-3 bg-light" {toggle}>New Message</ModalHeader>
	<ModalBody>
		<div>
			<div class="mb-3 position-relative">
				<Input
					type="text"
					class="form-control email-compose-input"
					defaultValue="support@themesbrand.com"
				/>
				<div class="position-absolute top-0 end-0">
					<div class="d-flex">
						<button
							class="btn btn-link text-reset fw-semibold px-2"
							type="button"
						>
							Cc
						</button>
						<button
							class="btn btn-link text-reset fw-semibold px-2"
							type="button"
						>
							Bcc
						</button>
					</div>
				</div>
			</div>
			<div class="collapse" id="CcRecipientsCollapse">
				<div class="mb-3">
					<Label>Cc:</Label>
					<Input
						type="text"
						class="form-control"
						placeholder="Cc recipients"
					/>
				</div>
			</div>
			<div class="collapse" id="BccRecipientsCollapse">
				<div class="mb-3">
					<Label>Bcc:</Label>
					<Input
						type="text"
						class="form-control"
						placeholder="Bcc recipients"
					/>
				</div>
			</div>

			<div class="mb-3">
				<Input type="text" class="form-control" placeholder="Subject" />
			</div>
		</div>
	</ModalBody>
	 <div class="modal-footer">
		<button type="button" class="btn btn-ghost-danger" on:click={toggle}>
			Discard
		</button>

		<Dropdown class="btn-group">
			<button type="button" class="btn btn-success" on:click={toggle}>
				Send
			</button>
			<DropdownToggle
				tag="button"
				type="button"
				class="btn btn-success"
				split
			>
				<span class="visually-hidden">Toggle Dropdown</span>
			</DropdownToggle>
			<DropdownMenu class="dropdown-menu-end">
				<li>
					<DropdownItem href={null}>
						<i
							class="ri-timer-line text-muted me-1 align-bottom"
						/>{" "}
						Schedule Send
					</DropdownItem>
				</li>
			</DropdownMenu>
		</Dropdown>
	</div> 
</Modal> -->

<Modal isOpen={showFileModal} className={'modal-dialog-centered modal-lg'}>	
    <div class="modal-header p-3 bg-light">
        <h5 class="modal-title" id="composemodalTitle">New Message</h5>
        <button type="button" class="btn-close" on:click={fileToggle} ></button>
    </div>
    <div class="modal-body">
        <div>
			<div class="mb-3 position-relative">
				<Input
					type="text"
					class="form-control email-compose-input"
					value="support@themesbrand.com"
				/>
				<div class="position-absolute top-0 end-0">
					<div class="d-flex">
						<button
							class="btn btn-link text-reset fw-semibold px-2"
							type="button"
						>
							Cc
						</button>
						<button
							class="btn btn-link text-reset fw-semibold px-2"
							type="button"
						>
							Bcc
						</button>
					</div>
				</div>
			</div>
			<div class="collapse" id="CcRecipientsCollapse">
				<div class="mb-3">
					<Label>Cc:</Label>
					<Input
						type="text"
						class="form-control"
						placeholder="Cc recipients"
					/>
				</div>
			</div>
			<div class="collapse" id="BccRecipientsCollapse">
				<div class="mb-3">
					<Label>Bcc:</Label>
					<Input
						type="text"
						class="form-control"
						placeholder="Bcc recipients"
					/>
				</div>
			</div>

			<div class="mb-3">
				<Input type="text" class="form-control" placeholder="Subject" />
			</div>
			<div class="ck-editor-reverse">
				
				<Input type="textarea" name="text" class="form-control" rows="5" id="exampleText" />
			</div>
		</div>
    </div>
	<div class="modal-footer">
		<button type="button" class="btn btn-ghost-danger" on:click={fileToggle}>Discard</button>

		<div class="btn-group">
			<Dropdown class="btn-group">
				<button type="button" class="btn btn-success" on:click={toggle}>
					Send
				</button>
				<DropdownToggle
					tag="button"
					type="button"
					class="btn btn-success"
					split
				>
					<span class="visually-hidden">Toggle Dropdown</span>
				</DropdownToggle>
				<DropdownMenu class="dropdown-menu-end">
					<li>
						<DropdownItem href={null}>
							<i
								class="ri-timer-line text-muted me-1 align-bottom"
							/>{" "}
							Schedule Send
						</DropdownItem>
					</li>
				</DropdownMenu>
			</Dropdown>
		</div>
	</div>
</Modal>