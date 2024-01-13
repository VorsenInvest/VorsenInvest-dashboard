<script>
	import { Card, CardHeader, Col, CardBody, Progress } from 'sveltestrap';
    import Map from '../../Components/Common/Map.svelte'

</script>

<Col xl={4}>
	<Card class="card-height-100">
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Sales by Locations</h4>
			<div class="flex-shrink-0">
				<button type="button" class="btn btn-soft-primary btn-sm"> Export Report </button>
			</div>
		</CardHeader>

		<CardBody>
			<div style="height: 269px">
				<Map latitude={-34.397} longitude={150.644} dataColor={["--vz-light", "--vz-secondary", "--vz-primary"]} MapType={'world'}></Map>
			</div>

			<div class="px-2 py-2 mt-1">
				<p class="mb-1">Canada <span class="float-end">75%</span></p>

				<Progress striped color="primary" value={75} class="mt-2" style="height : 6px" />

				<p class="mt-3 mb-1">Greenland <span class="float-end">47%</span></p>

				<Progress striped value={47} class="mt-2" style="height : 6px" />

				<p class="mt-3 mb-1">Russia <span class="float-end">82%</span></p>

				<Progress striped value={82} class="mt-2" style="height : 6px" />
			</div>
		</CardBody>
	</Card>
</Col>
