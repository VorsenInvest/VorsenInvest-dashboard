<script>
	import { Card, CardBody } from "sveltestrap";
	export let event;
	const getTime = (params) => {
		params = new Date(params);
		if (params.getHours() != null) {
			const hour = params.getHours();
			const minute = params.getMinutes() ? params.getMinutes() : "00";
			return hour + ":" + minute;
		}
	};
	const tConvert = (time) => {
		const t = time.split(":");
		var hours = t[0];
		var minutes = t[1];
		var newformat = hours >= 12 ? "PM" : "AM";
		hours = hours % 12;
		hours = hours ? hours : 12;
		minutes = minutes < 10 ? "0" + minutes : minutes;
		return hours + ":" + minutes + " " + newformat;
	};

	const str_dt = function formatDate(date) {
		const monthNames = [
			"January",
			"February",
			"March",
			"April",
			"May",
			"June",
			"July",
			"August",
			"September",
			"October",
			"November",
			"December",
		];
		var d = new Date(date),
			month = "" + monthNames[d.getMonth()],
			day = "" + d.getDate(),
			year = d.getFullYear();
		if (month.length < 2) month = "0" + month;
		if (day.length < 2) day = "0" + day;
		return [day + " " + month, year].join(",");
	};

	const category = event.className.split("-");

	var e_dt = event.end ? event.end : null;
	if (e_dt === "Invalid Date" || e_dt === undefined) {
		e_dt = null;
	} else {
		const newDate = new Date(e_dt).toLocaleDateString("en", {
			year: "numeric",
			month: "numeric",
			day: "numeric",
		});
		e_dt = new Date(newDate)
			.toLocaleDateString("en-GB", {
				day: "numeric",
				month: "short",
				year: "numeric",
			})
			.split(" ")
			.join(" ");
	}

	const st_date = event.start ? str_dt(event.start) : null;
	const ed_date = event.end ? str_dt(event.end) : null;
	if (st_date === ed_date) {
		e_dt = null;
	}
	var startDate = event.start;
	if (startDate === "Invalid Date" || startDate === undefined) {
		startDate = null;
	} else {
		const newDate = new Date(startDate).toLocaleDateString("en", {
			year: "numeric",
			month: "numeric",
			day: "numeric",
		});
		startDate = new Date(newDate)
			.toLocaleDateString("en-GB", {
				day: "numeric",
				month: "short",
				year: "numeric",
			})
			.split(" ")
			.join(" ");
	}

	var end_dt = e_dt ? " to " + e_dt : "";
	var e_time_s = tConvert(getTime(event.start));
	var e_time_e = tConvert(getTime(event.end));

	if (e_time_s === e_time_e) {
		e_time_s = "Full day event";
		e_time_e = null;
	}
	e_time_e = e_time_e ? " to " + e_time_e : "";
</script>

<Card class="mb-3 h-auto">
	<CardBody>
		<div class="d-flex mb-3">
			<div class="flex-grow-1">
				<i
					class={"mdi mdi-checkbox-blank-circle me-2 text-" +
						category[1]}
				/>
				<span class="fw-medium">
					{startDate}
					{end_dt}
				</span>
			</div>
			<div class="flex-shrink-0">
				<small class="badge bg-primary-subtle text-primary ms-auto">
					{e_time_s}
					{e_time_e}
				</small>
			</div>
		</div>
		<h6 class="card-title fs-16">{event.title}</h6>
		<p class="text-muted text-truncate-two-lines mb-0">
			{event.description}
		</p>
	</CardBody>
</Card>
