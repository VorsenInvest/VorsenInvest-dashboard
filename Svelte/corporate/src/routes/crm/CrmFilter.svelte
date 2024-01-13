<script>
	import { Offcanvas, Form, Label, Input, Button } from "sveltestrap";
	import Flatpickr from "svelte-flatpickr";
	import Select from "svelte-select";
	export let show, onCloseClick;

	const country = [
		{ label: "Select country", value: "Select country" },
		{ label: "Argentina", value: "Argentina" },
		{ label: "Belgium", value: "Belgium" },
		{ label: "Brazil", value: "Brazil" },
		{ label: "Colombia", value: "Colombia" },
		{ label: "Denmark", value: "Denmark" },
		{ label: "France", value: "France" },
		{ label: "Germany", value: "Germany" },
		{ label: "Mexico", value: "Mexico" },
		{ label: "Russia", value: "Russia" },
		{ label: "Spain", value: "Spain" },
		{ label: "Syria", value: "Syria" },
		{ label: "United Kingdom", value: "United Kingdom" },
		{
			label: "United States of America",
			value: "United States of America",
		},
	];
	const selectCountry = "Select country";
</script>

<Offcanvas placement="end" isOpen={show} {onCloseClick}>
	<div class="offcanvas-header bg-light">
		<h5 class="offcanvas-title" id="offcanvasExampleLabel">Leads Filters</h5>
		<button type="button" class="btn-close text-reset" on:click={onCloseClick}></button>
	</div>
	<!--end offcanvas-header-->
	<Form action="" class="d-flex flex-column justify-content-end h-100">
		<div class="offcanvas-body">
			<div class="mb-4">
				<Label
					for="datepicker-range"
					class="form-label text-muted text-uppercase fw-semibold mb-3">Date</Label
				>
				<Flatpickr
					class="form-control"
					id="datepicker-publish-input"
					placeholder="Select a date"
					items={{
						altInput: true,
						altFormat: "F j, Y",
						mode: "multiple",
						dateFormat: "d.m.y",
					}}
				/>
			</div>
			<div class="mb-4">
				<Label
					for="country-select"
					class="form-label text-muted text-uppercase fw-semibold mb-3">Country</Label
				>
				<Select
					className="mb-0"
					value={selectCountry}
					items={country}
					id="country-select"
				/>
			</div>
			<div class="mb-4">
				<Label
					for="status-select"
					class="form-label text-muted text-uppercase fw-semibold mb-3">Status</Label
				>
				<div class="row g-2">
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="inlineCheckbox1"
								value="option1"
							/>
							<Label
								class="form-check-label"
								for="inlineCheckbox1">New Leads</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="inlineCheckbox2"
								value="option2"
							/>
							<Label
								class="form-check-label"
								for="inlineCheckbox2">Old Leads</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="inlineCheckbox3"
								value="option3"
							/>
							<Label
								class="form-check-label"
								for="inlineCheckbox3">Loss Leads</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="inlineCheckbox4"
								value="option4"
							/>
							<Label
								class="form-check-label"
								for="inlineCheckbox4">Follow Up</Label>
						</div>
					</div>
				</div>
			</div>
			<div class="mb-4">
				<Label
					for="leadscore"
					class="form-label text-muted text-uppercase fw-semibold mb-3">Lead Score</Label
				>
				<div class="row g-2 align-items-center">
					<div class="col-lg">
						<Input
							type="number"
							class="form-control"
							id="leadscore"
							placeholder="0"
						/>
					</div>
					<div class="col-lg-auto">To</div>
					<div class="col-lg">
						<Input
							type="number"
							class="form-control"
							id="leadscore"
							placeholder="0"
						/>
					</div>
				</div>
			</div>
			<div>
				<Label
					for="leads-tags"
					class="form-label text-muted text-uppercase fw-semibold mb-3">Tags</Label
				>
				<div class="row g-3">
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="marketing"
								value="marketing"
							/>
							<Label class="form-check-label" for="marketing"
								>Marketing</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="management"
								value="management"
							/>
							<Label class="form-check-label" for="management"
								>Management</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="business"
								value="business"
							/>
							<Label class="form-check-label" for="business"
								>Business</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="investing"
								value="investing"
							/>
							<Label class="form-check-label" for="investing"
								>Investing</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="partner"
								value="partner"
							/>
							<Label class="form-check-label" for="partner"
								>Partner</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="lead"
								value="lead"
							/>
							<Label class="form-check-label" for="lead"
								>Leads</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="sale"
								value="sale"
							/>
							<Label class="form-check-label" for="sale"
								>Sale</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="owner"
								value="owner"
							/>
							<Label class="form-check-label" for="owner"
								>Owner</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="banking"
								value="banking"
							/>
							<Label class="form-check-label" for="banking"
								>Banking</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="banking"
								value="banking"
							/>
							<Label class="form-check-label" for="banking"
								>Exiting</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="banking"
								value="banking"
							/>
							<Label class="form-check-label" for="banking"
								>Finance</Label>
						</div>
					</div>
					<div class="col-lg-6">
						<div class="form-check">
							<input
								class="form-check-input"
								type="checkbox"
								id="banking"
								value="banking"
							/>
							<Label class="form-check-label" for="banking"
								>Fashion</Label>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!--end offcanvas-body-->
		<div class="offcanvas-footer border-top p-3 text-center hstack gap-2">
			<Button color="light" class="w-100">Clear Filter</Button>
			<Button color="primary" class="w-100">Filters</Button>
		</div>
		<!--end offcanvas-footer-->
	</Form>
</Offcanvas>
