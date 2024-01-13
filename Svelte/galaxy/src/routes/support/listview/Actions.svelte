<script>
	import { DropdownItem, DropdownMenu, DropdownToggle, Dropdown } from 'sveltestrap';
</script>

<Dropdown>
	<DropdownToggle tag="a" class="btn btn-soft-secondary btn-sm">
		<i class="ri-more-fill align-middle" />
	</DropdownToggle>
	<DropdownMenu class="dropdown-menu-end">
		<li>
			<DropdownItem href="/support/ticketsdetails/apps-tickets-details"
				><i class="ri-eye-fill align-bottom me-2 text-muted" /> View</DropdownItem
			>
		</li>
		<li>
			<DropdownItem class="edit-item-btn" href="#showModal" data-bs-toggle="modal"
				><i class="ri-pencil-fill align-bottom me-2 text-muted" /> Edit</DropdownItem
			>
		</li>
		<li>
			<DropdownItem class="remove-item-btn" data-bs-toggle="modal" href="#deleteOrder">
				<i class="ri-delete-bin-fill align-bottom me-2 text-muted" /> Delete
			</DropdownItem>
		</li>
	</DropdownMenu>
</Dropdown>