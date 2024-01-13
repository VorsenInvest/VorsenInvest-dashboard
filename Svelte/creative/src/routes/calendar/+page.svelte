<script>
	import { onMount } from "svelte";
	import * as FullCalendar from "fullcalendar"; // Import FullCalendar
	import { CalendarIcon } from "svelte-feather-icons";
	import Flatpickr from "svelte-flatpickr";
	import {
		Card,
		Button,
		CardBody,
		Container,
		ModalBody,
		ModalHeader,
		Row,
		Col,
		Label,
		Alert,
	} from "sveltestrap";

	import UpcommingEvents from "./UpcommingEvents.svelte";

	import BreadCrumb from "../../Components/Common/BreadCrumb.svelte";
	import CalendarEventsList from "../../common/data/calender";
	import Modal from "../../Components/Common/Modal.svelte";
	import "overlayscrollbars/overlayscrollbars.css";

	let isOpen = false;
	let calendar;
	let calendarComponentRef;
	let modalcategory = false;
	let setEvent = {};
	let isedit = false;
	let setSelectedDay = new Date();
	let eventsList = CalendarEventsList;

	let deleteModal = false;

	const toggle = () => {
		isOpen = !isOpen;
		if (!isOpen) {
			setTimeout(() => {
				setEvent = {};

				isedit = false;
			}, 500);
		}
	};

	const eventData1 = {
		id: Math.floor(Math.random() * 100),
		title: "New Event Planning",
		start: new Date(),
		allDay: false,
		className: "bg-success-subtle",
	};

	const eventData2 = {
		id: Math.floor(Math.random() * 100),
		title: "Meeting",
		start: new Date(),
		allDay: false,
		className: "bg-info-subtle",
	};

	const eventData3 = {
		id: Math.floor(Math.random() * 100),
		title: "Generating Reports",
		start: new Date(),
		allDay: false,
		className: "bg-warning-subtle",
	};

	const eventData4 = {
		id: Math.floor(Math.random() * 100),
		title: "Create New theme",
		start: new Date(),
		allDay: false,
		className: "bg-danger-subtle",
	};

	function handleDateClick(arg) {
		setSelectedDay = new Date(arg);;
		toggle();
	}

	let options;
	let calendarEl;
	let externalEventContainerEl;

	function getInitialView() {
		if (window.innerWidth >= 768 && window.innerWidth < 1200) {
			return "timeGridWeek";
		} else if (window.innerWidth <= 768) {
			return "listMonth";
		} else {
			return "dayGridMonth";
		}
	}

	onMount(() => {
		var Draggable = FullCalendar.Draggable;
		externalEventContainerEl = document.getElementById("external-events");
		// init draggable
		new Draggable(externalEventContainerEl, {
			itemSelector: ".external-event",
			eventData: function (eventEl) {
				return {
					id: Math.floor(Math.random() * 11000),
					title: eventEl.innerText,
					allDay: true,
					start: new Date(),
					className: eventEl.getAttribute("data-class"),
				};
			},
		});

		calendarEl = document.getElementById("calendar");
		options = {
			timeZone: "local",
			editable: true,
			droppable: true,
			selectable: true,
			navLinks: true,
			initialView: getInitialView(),
			themeSystem: "bootstrap",
			headerToolbar: {
				left: "prev,next today",
				center: "title",
				right: "dayGridMonth,timeGridWeek,timeGridDay,listMonth",
			},
			events: eventsList.events,
			windowResize: function (view) {
				var newView = getInitialView();
				calendar.changeView(newView);
			},
			eventClick: (event) => handleEventClick(event),
			dateClick: (event) => handleDateClick(event.dateStr),
			eventReceive: function (info) {
				var newid = parseInt(info.event.id);
				var newEvent = {
					id: newid,
					title: info.event.title,
					start: info.event.start,
					allDay: info.event.allDay,
					className: info.event.classNames[0],
				};
				eventsList.events = [...eventsList.events, newEvent];
				updateCalendarEvents();
			},
		};
		// Initialize FullCalendar
		calendar = new FullCalendar.Calendar(calendarEl, options);

		calendar.render(); // Render the calendar
	});

	function updateCalendarEvents() {
		// Reassign the events property with the updated events data
		options.events = eventsList.events;
		calendar.destroy(); // Destroy the existing instance
		calendar = new FullCalendar.Calendar(calendarEl, options); // Reinitialize with updated options
		calendar.render();
		calendar.refetchEvents(); // Refresh the calendar with the updated events
	}

	const handleEventClick = (arg) => {
		const event = arg.event;
		setEvent = {
			id: parseInt(event.id),
			title: event.title,
			title_category: event.title_category,
			start: event.start,
			className: event.classNames,
			category: event.classNames[0],
			event_category: event.classNames[0],
		};
        setSelectedDay = setEvent.start;
		isedit = true;
		toggle();
	};

	const toggleCategory = () => {
		modalcategory = !modalcategory;
	};

	const handleValidEventSubmit = async ({
		target: {
			elements: { category, title },
		},
	}) => {
		if (isedit) {
			if (
				title.value == null ||
				title.value == undefined ||
				title.value == ""
			) {
				document.getElementById("divAlert").style.display = "block";
				return false;
			}
			const updateEvent = {
				id: setEvent.id,
				title: title.value,
				className: category.value,
				start: setSelectedDay,
				allDay: false,
			};

			const i = eventsList.events.findIndex(
				(t) => t.id === updateEvent.id
			);
			// update event
			eventsList.events[i] = updateEvent;
			eventsList.events = [...eventsList.events];

			updateCalendarEvents();
		} else {
			if (
				title.value == null ||
				title.value == undefined ||
				title.value == ""
			) {
				document.getElementById("divAlert").style.display = "block";
				return false;
			}
			let newEvent = {
				id: Math.floor(Math.random() * 100),
				title: title.value,
				start: setSelectedDay ? setSelectedDay : new Date(),
				allDay: false,
				className: category.value,
			};
			eventsList.events = [...eventsList.events, newEvent];
			updateCalendarEvents();
		}

		setSelectedDay = "";
		toggle();
	};

	const handleDeleteEvent = () => {
		var calendarEvents = CalendarEventsList.events.filter((e, i) => {
			return e.id !== setEvent.id;
		});

		// calendarEvents = [...calendarEvents];
		eventsList.events = calendarEvents;

		setDeleteModal(false);
		updateCalendarEvents();
		toggle();
	};

	const setDeleteModal = (status) => {
		deleteModal = status;
		isOpen = false;

		var calendarEvents = CalendarEventsList.events.filter((e, i) => {
			return e.id !== setEvent.id;
		});

		eventsList.events = calendarEvents;
		updateCalendarEvents();
		setTimeout(() => {
			setEvent = {};
			isedit = false;
		}, 500);
	};
</script>

<svelte:head>
	<title>Calendar | Velzon - Svelte Admin & Dashboard Template</title>
	<style>
		#divAlert {
			display: none;
		}
	</style>
</svelte:head>

<div class="page-content">
	<Container fluid>
		<BreadCrumb title="Calendar" pageTitle="Apps" />
		<Row>
			<Col xs={12}>
				<Row>
					<Col xl={3}>
						<Card class="card-h-100">
							<CardBody>
								<button
									class="btn btn-primary w-100"
									id="btn-new-event"
									on:click={toggle}
								>
									<i class="mdi mdi-plus" /> Create New Event
								</button>
								<div id="external-events">
									<br />
									<p class="text-muted">
										Drag and drop your event or click in the
										calendar
									</p>
									<div
										class="external-event fc-event bg-success-subtle text-success"
										data-class="bg-success-subtle"
									>
										<i
											class="mdi mdi-checkbox-blank-circle me-2"
										/>New Event Planning
									</div>
									<div class="external-event fc-event bg-info-subtle text-info" data-class="bg-info-subtle">
										<i class="mdi mdi-checkbox-blank-circle me-2"></i>Meeting
									</div>
									<div class="external-event fc-event bg-warning-subtle text-warning" data-class="bg-warning-subtle">
										<i class="mdi mdi-checkbox-blank-circle me-2"></i>Generating Reports
									</div>
									<div class="external-event fc-event bg-danger-subtle text-danger" data-class="bg-danger-subtle">
										<i class="mdi mdi-checkbox-blank-circle me-2"></i>Create New theme
									</div>
								</div>
							</CardBody>
						</Card>
						<div>
							<h5 class="mb-1">Upcoming Events</h5>
							<p class="text-muted">
								Don't miss scheduled events
							</p>
							<div
								class="pe-2 me-n1 mb-3"
								data-overlayscrollbars-initialize
								style="height: 400px"
							>
								<div id="upcoming-event-list">
									{#if CalendarEventsList.defaultevent}
										{#each CalendarEventsList.defaultevent as event}
											<UpcommingEvents {event} />
										{/each}
									{/if}
								</div>
							</div>
						</div>
						<Card>
							<CardBody class="bg-info-subtle">
								<div class="d-flex">
									<div class="flex-shrink-0">
										<CalendarIcon
											class="text-info icon-dual-info"
											size="24"
										/>
									</div>
									<div class="flex-grow-1 ms-3">
										<h6 class="fs-15">
											Welcome to your Calendar!
										</h6>
										<p class="text-muted mb-0">
											Event that applications book will
											appear here. Click on an event to
											see the details and manage
											applicants event.
										</p>
									</div>
								</div>
							</CardBody>
						</Card>
					</Col>
					<Col xl={9}>
						<Card className="card-h-100">
							<CardBody>
								<div id="calendar" />
							</CardBody>
						</Card>
					</Col>
				</Row>
			</Col>
		</Row>
	</Container>
</div>

<Modal {isOpen}>
	<ModalHeader {toggle} tag="h4">
		{!!isedit ? "Edit Event" : "Add Event"}
	</ModalHeader>
	<ModalBody>
		<form on:submit|preventDefault={handleValidEventSubmit}>
			<Row>
				<Col class="col-12">
					<div class="mb-3">
						<div id="divAlert">
							<Alert color="danger">Please provide a valid event name</Alert>
						</div>
						<Label class="form-label" for="title">Event Name</Label>
						<input
							type="text"
							class="form-control"
							name="title"
							placeholder="Event Name"
							value={setEvent && setEvent.title
								? setEvent.title
								: ""}
						/>
					</div>
				</Col>
				<Col class="col-12">
					<div class="mb-3">
						<Label class="form-label" for="category">Category</Label
						>
						<select
							name="category"
							class="form-control form-select"
							placeholder="Select Category"
							value={setEvent ? setEvent.category : "bg-primary"}
						>
							<option value="bg-danger-subtle">Danger</option>
							<option value="bg-success-subtle">Success</option>
							<option value="bg-primary-subtle">Primary</option>
							<option value="bg-info-subtle">Info</option>
							<option value="bg-dark-subtle">Dark</option>
							<option value="bg-warning-subtle">Warning</option>
						</select>
					</div>
				</Col>
				<Col class="col-12">
					<div class="mb-3">
						<Label class="form-label" for="date">Date</Label>
						<Flatpickr
                            class="form-control"
                            id="date"
                            placeholder="Select a date"
                            bind:value={setSelectedDay}
                            options={{
                                altInput: true,
                                altFormat: "F j, Y",
                                dateFormat: "d-m-Y",
                            }}
                        />
					</div>
				</Col>
			</Row>
			<Row class="mt-2">
				<Col xs="12" class="text-end">
					{#if !!isedit}
						<button
							type="button"
							class="btn btn-danger"
							on:click={() => setDeleteModal(true)}>Delete</button
						>
					{/if}
					<button
						type="button"
						class="btn btn-light me-2"
						on:click={toggle}
					>
						Close
					</button>
					<button type="submit" class="btn btn-success save-event">
						Save
					</button>
				</Col>
			</Row>
		</form>
	</ModalBody>
</Modal>