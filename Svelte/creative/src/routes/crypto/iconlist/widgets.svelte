<script>
	import { Card, CardBody} from "sveltestrap";
	import CryptoData from "../../../common/data/cryptoPage";
</script>

{#each CryptoData.CryptoicoWidgets as item}
	<div class="col">
		<Card>
			<CardBody class="d-flex">
				<div class="flex-grow-1">
					<h4>{item.counter}</h4>
					<h6 class="text-muted mb-0">{item.label}</h6>
				</div>
				<div class="flex-shrink-0 avatar-sm">
					<div class="avatar-title bg-{item.iconClass}-subtle text-{item.iconClass} fs-22 rounded">
						<i class={item.icon} />
					</div>
				</div>
			</CardBody>
		</Card>
	</div>
{/each}