<script>
	import {
		Container,
		Button,
		Tooltip,
		Input,
		DropdownToggle,
		DropdownMenu,
		Dropdown,
		DropdownItem,
		Row,
		Col,
		Card,
		CardBody,
		Nav,
		NavItem,
		NavLink,
		TabContent,
		TabPane,
	} from "sveltestrap";

	import PersonalInfo from "./PersonalInfo.svelte";

	import Link from "svelte-link";

	import {
		SearchIcon,
		InfoIcon,
		MoreVerticalIcon,
	} from "svelte-feather-icons";

	import data from "../../common/data/chat";
	import ChatBoxImage from '../../assets/images/users/avatar-2.jpg'
	import userdummay from '../../assets/images/users/user-dummy-img.jpg'
	
	let currentRoomId = 1;
	let Chat_Box_Image = ChatBoxImage;
	let userDummayImage = userdummay;

	let search_Menu = false;
	let Chat_Box_Username = "Lisa Parker";
	let curMessage = "";
	let isInfoDetails = false;

	let activeTab = 1;

	const toggleInfo = () => (isInfoDetails = !isInfoDetails);

	function toggleSearch() {
		search_Menu = !search_Menu;
	}

	function userChatOpen(id, name, status, roomId, image) {
		Chat_Box_Username = name;
		currentRoomId = roomId;
		Chat_Box_Image = image;
	}
</script>

<svelte:head>
	<title>Chat | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<div class="chat-wrapper d-lg-flex gap-1 mx-n4 mt-n4 p-1">
			<div class="chat-leftsidebar minimal-border">
				<div class="px-4 pt-4 mb-3">
					<div class="d-flex align-items-start">
						<div class="flex-grow-1">
							<h5 class="mb-4">Chats</h5>
						</div>
						<div class="flex-shrink-0">
							<Tooltip placement="bottom" target="addcontact"
								>Add Contact</Tooltip>

							<Button
								color="soft-success"
								id="addcontact"
								size="sm"
								class="material-shadow-none">
								<i class="ri-add-line align-bottom" />
							</Button>
						</div>
					</div>
					<div class="search-box">
						<input
							type="text"
							class="form-control bg-light border-light"
							placeholder="Search here..."
						/>
						<i class="ri-search-2-line search-icon" />
					</div>
				</div>
				<Nav class="nav-tabs nav-tabs-custom nav-success nav-justified">
					<NavItem>
						<NavLink on:click={() => (activeTab = 1)} active={activeTab == 1}>Chats</NavLink>
					</NavItem>
					<NavItem>
						<NavLink on:click={() => (activeTab = 2)} active={activeTab == 2}>Contacts</NavLink>
					</NavItem>
				</Nav>

				<TabContent>
					<TabPane tabId={1} class={activeTab == 1 ? 'active' : ''}>
					<div class="chat-room-list pt-3" data-overlayscrollbars-initialize>
						<div class="d-flex align-items-center px-4 mb-2">
							<div class="flex-grow-1">
								<h4 class="mb-0 fs-11 text-muted text-uppercase">
									Direct Messages
								</h4>
							</div>
							<div class="flex-shrink-0">
								
								<Button
								type="button"
								id="addnewmsg"
								color="soft-success"
								size="sm"
								class="shadow-none material-shadow">
								<i class="ri-add-line align-bottom" />
							</Button>
							<Tooltip placement="bottom" target="addnewmsg"
								>New Message</Tooltip>
							</div>
						</div>

						<div class="chat-message-list">
							<ul
								class="list-unstyled chat-list chat-user-list"
								id="userList"
							>
								{#each data.direactContact as chat}
									<li
										class={currentRoomId === chat.roomId
											? "active"
											: ""}
									>
										<Link
											href="{null}"
											on:click={(e) => {
												e.preventDefault();
												userChatOpen(
													chat.id,
													chat.name,
													chat.status,
													chat.roomId,
													chat.image
												);
											}}
										>
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0 chat-user-img online align-self-center me-2 ms-0"
												>
													<div class="avatar-xxs">
														{#if chat.image}
															<img
																src={chat.image}
																class="rounded-circle img-fluid userprofile"
																alt=""
															/>
														{:else}
															<div class={"avatar-title rounded-circle bg-" +
																	chat.bgColor +
																	" userprofile"}
															>
																{chat.name.charAt(
																	0
																)}
															</div>
														{/if}
													</div>
													<span class="user-status" />
												</div>
												<div class="flex-grow-1 overflow-hidden"
												>
													<p class="text-truncate mb-0">
														{chat.name}
													</p>
												</div>
											</div>
										</Link>
									</li>
								{/each}
							</ul>
						</div>

						<div class="d-flex align-items-center px-4 mt-4 pt-2 mb-2">
							<div class="flex-grow-1">
								<h4 class="mb-0 fs-11 text-muted text-uppercase">
									Channels
								</h4>
							</div>
							<div class="flex-shrink-0">
								<Button
								color=""
								id="createnewmsg"
								class="btn btn-soft-success btn-sm">
								<i class="ri-add-line align-bottom" />
							</Button>
							<Tooltip placement="bottom" target="createnewmsg"
								>Create group</Tooltip>
							</div>
						</div>

						<div class="chat-message-list">
							<ul
								class="list-unstyled chat-list chat-user-list mb-0"
								id="channelList"
							>
								{#each data.channelsList as channel}
									<li>
										<a href="{null}" class="unread-msg-user">
											<div class="d-flex align-items-center">
												<div class="flex-shrink-0 chat-user-img online align-self-center me-2 ms-0"
												>
													<div class="avatar-xxs">
														<div class="avatar-title bg-light rounded-circle text-body">
															#
														</div>
													</div>
												</div>
												<div class="flex-grow-1 overflow-hidden"
												>
													<p class="text-truncate mb-0">
														{channel.name}
													</p>
												</div>
												{#if channel.unReadMessage}
													<div class="flex-shrink-0">
														<span
															class="badge badge-soft-dark rounded p-1"
														>
															{channel.unReadMessage}
														</span>
													</div>
												{/if}
											</div>
										</a>
									</li>
								{/each}
							</ul>
						</div>
					</div>
				</TabPane>
				<TabPane tabId={2} class={activeTab == 2 ? 'active' : ''}>
					<div class="chat-room-list pt-3" data-simplebar>
						<div class="sort-contact">
						{#each data.chatContactData as item}
							<div class="mt-3 h-auto">
								<div class="contact-list-title">{item.title}</div>
								<ul id={"contact-sort-" + item.title} class="list-unstyled contact-list">
									{#each item.contacts as item}
										<li>
											<div class="d-flex align-items-center">
											<div class="flex-shrink-0 me-2">
												<div class="avatar-xxs">
													{#if item.image}
														<img src={item.image} class="img-fluid rounded-circle" alt="" />
													{:else}
														<span class="avatar-title rounded-circle bg-primary fs-10">
															{item.name.charAt(0) + item.name.split(" ").slice(-1).toString().charAt(0)}
														</span>
													{/if}
												</div>
											</div>

											<!-- svelte-ignore a11y-click-events-have-key-events -->
											<div class="flex-grow-1" on:click={(e) => {
												e.preventDefault();
												userChatOpen(
												item.id,
												item.name,
												item.status,
												item.roomId,
												item.image
												);
											}}>
												<p class="text-truncate contactlist-name mb-0">{item.name}</p>
											</div>
											<div class="flex-shrink-0">
												<Dropdown>
												<DropdownToggle tag="a" class="text-muted" color="">
													<i class="ri-more-2-fill" />
												</DropdownToggle>
												<DropdownMenu class="dropdown-menu-end">
													<DropdownItem><i class="ri-pencil-line text-muted me-2 align-bottom" />Edit</DropdownItem>
													<DropdownItem><i class="ri-forbid-2-line text-muted me-2 align-bottom" />Block</DropdownItem>
													<DropdownItem><i class="ri-delete-bin-6-line text-muted me-2 align-bottom" /> Remove</DropdownItem>
												</DropdownMenu>
												</Dropdown>
											</div>
											</div>
										</li>
									{/each}
								</ul>
							</div>
						{/each}
						</div>
					</div>
				</TabPane>
				</TabContent>
			</div>

			<div class="user-chat w-100 overflow-hidden minimal-border">
				<div class="chat-content d-lg-flex">
					<div class="w-100 overflow-hidden position-relative">
						<div class="position-relative">
							<div class="p-3 user-chat-topbar">
								<Row class="align-items-center">
									<Col sm={4} xs={8}>
										<div class="d-flex align-items-center">
											<div class="flex-shrink-0 d-block d-lg-none me-3"
											>
												<a
													href="{null}"
													class="user-chat-remove fs-18 p-1"
												>
													<i
														class="ri-arrow-left-s-line align-bottom"
													/>
												</a>
											</div>
											<div class="flex-grow-1 overflow-hidden"
											>
												<div class="d-flex align-items-center"
												>
													<div class="flex-shrink-0 chat-user-img online user-own-img align-self-center me-3 ms-0"
													>
														{#if Chat_Box_Image === undefined}
															<img
																src={userDummayImage}
																class="rounded-circle avatar-xs"
																alt=""
															/>
														{:else}
															<img
																src={Chat_Box_Image}
																class="rounded-circle avatar-xs"
																alt=""
															/>
														{/if}
														<span
															class="user-status"
														/>
													</div>
													<div class="flex-grow-1 overflow-hidden"
													>
														<h5
															class="text-truncate mb-0 fs-16"
														>
															<a
																class="text-reset username"
																data-bs-toggle="offcanvas"
																href="#userProfileCanvasExample"
																aria-controls="userProfileCanvasExample"
																on:click={()=> toggleInfo()}
															>
																{Chat_Box_Username}
															</a>
														</h5>
														<p
															class="text-truncate text-muted fs-14 mb-0 userStatus"
														>
															<small>Online</small
															>
														</p>
													</div>
												</div>
											</div>
										</div>
									</Col>
									<Col sm={8} xs={4}>
										<ul
											class="list-inline user-chat-nav text-end mb-0"
										>
											<li class="list-inline-item m-0">
												<Dropdown
													isOpen={search_Menu}
													toggle={toggleSearch}
												>
													<DropdownToggle
														class="btn-icon p-0 material-shadow-none"
														tag="button"
														color="ghost-secondary"
													>
														<SearchIcon
															class="icon-sm"
														/>
													</DropdownToggle>
													<DropdownMenu
														class="p-0 dropdown-menu-end dropdown-menu-lg"
													>
														<div class="p-2">
															<div 						class="search-box"
															>
																<Input
																	type="text"
																	class="form-control bg-light border-light"
																	placeholder="Search here..."
																	id="searchMessage"
																/>
																<i
																	class="ri-search-2-line search-icon"
																/>
															</div>
														</div>
													</DropdownMenu>
												</Dropdown>
											</li>

											<li
												class="list-inline-item d-none d-lg-inline-block m-0"
											>
												<button
													type="button"
													class="btn btn-ghost-secondary btn-icon material-shadow-none"
													on:click={toggleInfo}
												>
													<InfoIcon class="icon-sm" />
												</button>
											</li>

											<li class="list-inline-item m-0">
												<Dropdown>
													<DropdownToggle
														class="btn-icon p-0 material-shadow-none"
														tag="button"
														color="ghost-secondary"
													>
														<MoreVerticalIcon
															class="icon-sm"
														/>
													</DropdownToggle>
													<DropdownMenu>
														<DropdownItem
															href="{null}"
															class="d-block d-lg-none user-profile-show"
														>
															<i
																class="ri-user-2-fill align-bottom text-muted me-2"
															/>{" "}
															View Profile
														</DropdownItem>
														<DropdownItem href="{null}">
															<i
																class="ri-inbox-archive-line align-bottom text-muted me-2"
															/>{" "}
															Archive
														</DropdownItem>
														<DropdownItem href="{null}">
															<i
																class="ri-mic-off-line align-bottom text-muted me-2"
															/>{" "}
															Muted
														</DropdownItem>
														<DropdownItem href="{null}">
															{" "}
															<i
																class="ri-delete-bin-5-line align-bottom text-muted me-2"
															/>{" "}
															Delete
														</DropdownItem>
													</DropdownMenu>
												</Dropdown>
											</li>
										</ul>
									</Col>
								</Row>
							</div>

							<div class="position-relative" id="users-chat">
								<div class="chat-conversation p-3 p-lg-4 "
									id="chat-conversation"
									data-simplebar
								>
									<ul
										class="list-unstyled chat-conversation-list"
										id="users-conversation"
									>
										{#each data.messages as message}
											<li
												class={message.sender ===
												Chat_Box_Username
													? " chat-list left"
													: "chat-list right"}
											>
												<div class="conversation-list">
													{#if message.sender === Chat_Box_Username}
														<div class="chat-avatar"
														>
															{#if Chat_Box_Image === undefined}
																<img
																	src={userDummayImage}
																	alt=""
																/>
															{:else}
																<img
																	src={Chat_Box_Image}
																	alt=""
																/>
															{/if}
														</div>
													{/if}

													<div class="user-chat-content"
													>
														<div class="ctext-wrap">
															<div 						class="ctext-wrap-content"
															>
																<p
																	class="mb-0 ctext-content"
																>
																	{message.message}
																</p>
															</div>
															<Dropdown
																class="align-self-start message-box-drop"
															>
																<DropdownToggle
																	href="{null}"
																	class="btn nav-btn p-0"
																	tag="i"
																	color=""
																>
																	<i
																		class="ri-more-2-fill"
																	/>
																</DropdownToggle>
																<DropdownMenu>
																	<DropdownItem
																		href="{null}"
																		class="reply-message"
																	>
																		<i
																			class="ri-reply-line me-2 text-muted align-bottom"
																		/>
																		Reply
																	</DropdownItem>
																	<DropdownItem
																		href="{null}"
																	>
																		<i
																			class="ri-share-line me-2 text-muted align-bottom"
																		/>
																		Forward
																	</DropdownItem>
																	<DropdownItem
																		href="{null}"
																	>
																		<i
																			class="ri-file-copy-line me-2 text-muted align-bottom"
																		/>
																		Copy
																	</DropdownItem>
																	<DropdownItem
																		href="{null}"
																	>
																		<i
																			class="ri-bookmark-line me-2 text-muted align-bottom"
																		/>
																		Bookmark
																	</DropdownItem>
																	<DropdownItem
																		href="{null}"
																	>
																		<i
																			class="ri-delete-bin-5-line me-2 text-muted align-bottom"
																		/>
																		Delete
																	</DropdownItem>
																</DropdownMenu>
															</Dropdown>
														</div>
														<div class="conversation-name"
														>
															<small
																class="text-muted time"
															>
																09:07 am
															</small>{" "}
															<span
																class="text-success check-message-icon"
															>
																<i
																	class="ri-check-double-line align-bottom"
																/>
															</span>
														</div>
													</div>
												</div>
											</li>
										{/each}
									</ul>
								</div>
							</div>

							<div class="chat-input-section p-3 p-lg-4">
								<form id="chatinput-form">
									<Row class="g-0 align-items-center">
										<div class="col-auto">
											<div class="chat-input-links me-2">
												<div class="links-list-item">
													<button
														type="button"
														class="btn btn-link text-decoration-none emoji-btn"
														id="emoji-btn"
													>
														<i
															class="bx bx-smile align-middle"
														/>
													</button>
												</div>
											</div>
										</div>

										<div class="col">
											<div class="chat-input-feedback">
												Please Enter a Message
											</div>
											<input
												type="text"
												value={curMessage}
												class="form-control chat-input bg-light border-light"
												id="chat-input"
												placeholder="Type your message..."
												autocomplete="off"
											/>
										</div>
										<div class="col-auto">
											<div class="chat-input-links ms-2">
												<div class="links-list-item">
													<Button
														type="button"
														color="success"
														class="chat-send waves-effect waves-light"
													>
														<i
															class="ri-send-plane-2-fill align-bottom"
														/>
													</Button>
												</div>
											</div>
										</div>
									</Row>
								</form>
							</div>

							<div class="replyCard">
								<Card class="mb-0">
									<CardBody class="py-3">
										<div class="replymessage-block mb-0 d-flex align-items-start"
										>
											<div class="flex-grow-1">
												<p class="mb-0" />
											</div>
											<div class="flex-shrink-0">
												<button
													type="button"
													id="close_toggle"
													class="btn btn-sm btn-link mt-n2 me-n3 fs-18"
												>
													<i
														class="bx bx-x align-middle"
													/>
												</button>
											</div>
										</div>
									</CardBody>
								</Card>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</Container>
</div>

<PersonalInfo
	show={isInfoDetails}
	onCloseClick={toggleInfo}
	currentuser={Chat_Box_Username}
	cuurentiseImg={Chat_Box_Image}
/>
