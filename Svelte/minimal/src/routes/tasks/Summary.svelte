<script>
	import { Card, CardBody, Label } from "sveltestrap";
</script>

<Card>
	<CardBody>
		<div class="text-muted">
			<h6 class="mb-3 fw-semibold text-uppercase">Summary</h6>
			<p>
				It will be as simple as occidental in fact, it will be
				Occidental. To an English person, it will seem like simplified
				English, as a skeptical Cambridge friend of mine told me what
				Occidental is. The European languages are members of the same
				family. Their separate existence is a myth. For science, music,
				sport, etc, Europe uses the same vocabulary. The languages only
				differ in their grammar, their pronunciation and their most
				common words.
			</p>

			<h6 class="mb-3 fw-semibold text-uppercase">Sub-tasks</h6>
			<ul class=" ps-3 list-unstyled vstack gap-2">
				<li>
					<div class="form-check">
						<input
							class="form-check-input"
							type="checkbox"
							value=""
							id="productTask"
						/>
						<Label class="form-check-label" for="productTask">
							Product Design, Figma (Software), Prototype
						</Label>
					</div>
				</li>
				<li>
					<div class="form-check">
						<input
							class="form-check-input"
							type="checkbox"
							value=""
							id="dashboardTask"
							checked
						/>
						<Label class="form-check-label" for="dashboardTask">
							Dashboards : Ecommerce, Analytics, Project,etc.
						</Label>
					</div>
				</li>
				<li>
					<div class="form-check">
						<input
							class="form-check-input"
							type="checkbox"
							value=""
							id="calenderTask"
						/>
						<Label class="form-check-label" for="calenderTask">
							Create calendar, chat and email app pages
						</Label>
					</div>
				</li>
				<li>
					<div class="form-check">
						<input
							class="form-check-input"
							type="checkbox"
							value=""
							id="authenticationTask"
						/>
						<Label
							class="form-check-label"
							for="authenticationTask"
						>
							Add authentication pages
						</Label>
					</div>
				</li>
			</ul>

			<div class="pt-3 border-top border-top-dashed mt-4">
				<h6 class="mb-3 fw-semibold text-uppercase">Tasks Tags</h6>
				<div class="hstack flex-wrap gap-2 fs-15">
					<div class="badge fw-medium bg-secondary-subtle text-secondary">
						UI/UX
					</div>
					<div class="badge fw-medium bg-secondary-subtle text-secondary">
						Dashboard
					</div>
					<div class="badge fw-medium bg-secondary-subtle text-secondary">
						Design
					</div>
				</div>
			</div>
		</div>
	</CardBody>
</Card>
