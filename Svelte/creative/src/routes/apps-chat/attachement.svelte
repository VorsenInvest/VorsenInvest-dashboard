<script>
	import Link from "svelte-link";
	import {
		Dropdown,
		DropdownToggle,
		DropdownMenu,
		DropdownItem,
	} from "sveltestrap";
	export let attachement;
</script>

<div class="border rounded border-dashed p-2">
	<div class="d-flex align-items-center">
		<div class="flex-shrink-0 me-3">
			<div class="avatar-xs">
				<div class="avatar-title bg-light text-secondary rounded fs-20">
					<i class={attachement.foldericon} />
				</div>
			</div>
		</div>
		<div class="flex-grow-1 overflow-hidden">
			<h5 class="fs-15 mb-1">
				<Link href={null} class="text-body text-truncate d-block">
					{attachement.foldername}
				</Link>
			</h5>
			<div class="text-muted">{attachement.foldersize}</div>
		</div>
		<div class="flex-shrink-0 ms-2">
			<div class="d-flex gap-1">
				<button
					type="button"
					class="btn btn-icon text-muted btn-sm fs-18"
				>
					<i class="ri-download-2-line" />
				</button>
				<Dropdown>
					<DropdownToggle
						tag="button"
						class="btn btn-icon text-muted btn-sm fs-18 dropdown p-0"
						color="">
						<i class="ri-more-fill" />
					</DropdownToggle>
					<DropdownMenu>
						<DropdownItem>
							<i
								class="ri-share-line align-bottom me-2 text-muted"
							/>{" "}
							Share
						</DropdownItem>
						<DropdownItem>
							<i
								class="ri-bookmark-line align-bottom me-2 text-muted"
							/>{" "}
							Bookmark
						</DropdownItem>
						<DropdownItem>
							<i
								class="ri-delete-bin-line align-bottom me-2 text-muted"
							/>{" "}
							Delete
						</DropdownItem>
					</DropdownMenu>
				</Dropdown>
			</div>
		</div>
	</div>
</div>
