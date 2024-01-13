<script lang="ts">
	import { Dropdown, DropdownToggle, DropdownItem, DropdownMenu } from 'sveltestrap';
</script>

<Dropdown>
	<DropdownToggle href={null} class="btn-soft-secondary btn-sm" tag="button">
		<i class="ri-more-fill align-middle" />
	</DropdownToggle>
	<DropdownMenu class="dropdown-menu-end">
		<DropdownItem class="edit-item-btn">
			Rename
		</DropdownItem>

		<DropdownItem class="regenerate-api-btn">
			Regenerate Key
		</DropdownItem>

		<DropdownItem class="disable-btn" href={null}>
			Disable
		</DropdownItem>
        <DropdownItem class="remove-item-btn" href={null}>
			Delete
		</DropdownItem>
	</DropdownMenu>
</Dropdown>