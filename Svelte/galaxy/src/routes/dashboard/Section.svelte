<script>
	import { Col, Row, Button } from "sveltestrap";
	import Flatpickr from "svelte-flatpickr";
	import { browser } from "$app/environment";

	function sidebar() {
		if (browser) {
			const element = document.getElementById("layout-rightside-coll");
			element.classList.toggle("d-none");
		}
	}
</script>

<Row class="mb-3 pb-1">
	<Col xs={12}>
		<div class="d-flex align-items-lg-center flex-lg-row flex-column">
			<div class="flex-grow-1">
				<h4 class="fs-16 mb-1">Good Morning, Anna!</h4>
				<p class="text-muted mb-0">
					Here's what's happening with your store today.
				</p>
			</div>
			<div class="mt-3 mt-lg-0">
				<form action="#">
					<Row class="g-3 mb-0 align-items-center">
						<div class="col-sm-auto">
							<div class="input-group">
								<Flatpickr
									class="form-control dash-filter-picker"
									options={{
										mode: "range",
										dateFormat: "d M, Y",
										defaultDate: [
											"01 Jan 2022",
											"31 Jan 2022",
										],
									}}
								/>
								<div class="input-group-text bg-primary border-primary text-white"
								>
									<i class="ri-calendar-2-line" />
								</div>
							</div>
						</div>
						<div class="col-auto">
							<Button
								type="button"
								color=""
								class="btn btn-soft-primary"
								><i
									class="ri-add-circle-line align-middle me-1"
								/> Add Product</Button>
						</div>
						<div class="col-auto">
							<Button
								type="button"
								color=""
								class="btn btn-soft-primary btn-icon waves-effect waves-light layout-rightside-btn"
								on:click={sidebar}
								><i class="ri-pulse-line" /></Button>
						</div>
					</Row>
				</form>
			</div>
		</div>
	</Col>
</Row>
