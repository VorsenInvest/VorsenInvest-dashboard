<script>
	import cryptoData from "../../../common/data/cryptoPage";
	import { Card, CardBody, Col } from "sveltestrap";
	import Counter from "../../../Components/Common/CounterPage.svelte";
</script>

<Counter />

{#each cryptoData.buysellWidgets as item}
	<Col xl={3} sm={6}>
		<Card class="card-animate">
			<CardBody>
				<div class="d-flex">
					<div class="flex-grow-1">
						<h6 class="text-muted mb-3">{item.title}</h6>
						<h4 class="mb-0">
							$<span
								class="counter-value"
								data-target="243"
							/><small class="text-muted fs-13">.10k</small>
						</h4>
					</div>
					<div class="flex-shrink-0 avatar-sm">
						<div
							class={"avatar-title fs-22 rounded bg-" +
								item.iconClass +
								"-subtle text-" +
								item.iconClass}
						>
							<i class={item.icon} />
						</div>
					</div>
				</div>
			</CardBody>
		</Card>
	</Col>
{/each}
