<script>
	import data from '../../common/data/dashboardcrm';
</script>

<div class="col-xl-12">
	<div class="card crm-widget">
		<div class="card-body p-0">
			<div class="row row-cols-xxl-5 row-cols-md-3 row-cols-1 g-0">
				{#each data.crmWidgets as widget}
					<div class="col">
						<div class="py-4 px-3">
							<h5 class="text-muted text-uppercase fs-13">
								{widget.label}<i class={widget.badge + ' fs-18 float-end align-middle'} />
							</h5>
							<div class="d-flex align-items-center">
								<div class="flex-shrink-0">
									<i class={widget.icon + ' display-6 text-muted cfs-22'} />
								</div>
								<div class="flex-grow-1 ms-3">
									<h2 class="mb-0 cfs-22">
										{widget.prefix}<span class="counter-value" data-target={widget.counter}>0</span>{widget.suffix}
									</h2>
								</div>
							</div>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
</div>