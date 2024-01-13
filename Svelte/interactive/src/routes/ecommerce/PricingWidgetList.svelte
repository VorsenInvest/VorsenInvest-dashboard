<script>
	import { Col } from 'sveltestrap';
	export let pricingDetails;

</script>

<Col lg={3} sm={6}>
	<div class="p-2 border border-dashed rounded">
		<div class="d-flex align-items-center">
			<div class="avatar-sm me-2">
				<div class="avatar-title rounded bg-transparent text-info fs-24">
					<i class={pricingDetails.icon} />
				</div>
			</div>
			<div class="flex-grow-1">
				<p class="text-muted mb-1">{pricingDetails.label} :</p>
				<h5 class="mb-0">{pricingDetails.labelDetail}</h5>
			</div>
		</div>
	</div>
</Col>