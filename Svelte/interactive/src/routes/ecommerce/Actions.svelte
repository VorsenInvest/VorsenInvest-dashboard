<script lang="ts">
	import { Dropdown, DropdownToggle, DropdownItem, DropdownMenu } from 'sveltestrap';
</script>

<Dropdown>
	<DropdownToggle href={null} class="btn-soft-secondary btn-sm" tag="button">
		<i class="ri-more-fill" />
	</DropdownToggle>
	<DropdownMenu class="dropdown-menu-end">
		<DropdownItem href="/ecommerce/apps-ecommerce-product-details">
			<i class="ri-eye-fill align-bottom me-2 text-muted" />
			View
		</DropdownItem>

		<DropdownItem href="/ecommerce/apps-ecommerce-add-product">
			<i class="ri-pencil-fill align-bottom me-2 text-muted" />
			Edit
		</DropdownItem>

		<DropdownItem href={null}>
			<i class="ri-delete-bin-fill align-bottom me-2 text-muted"></i>
			Delete
		</DropdownItem>
	</DropdownMenu>
</Dropdown>