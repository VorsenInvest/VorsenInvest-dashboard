<script>
	import {
		CardBody,
		Row,
		Col,
		Card,
		Container,
		CardHeader,
		Form,
		Input,
		Button,
		Dropdown,
		DropdownToggle,
		DropdownMenu,
		DropdownItem
	} from 'sveltestrap';
</script>

<Dropdown>
	<DropdownToggle href={null} class="btn-soft-secondary btn-sm dropdown" tag="button">
		<i class="ri-more-fill align-middle" />
	</DropdownToggle>
	<DropdownMenu class="dropdown-menu-end">
		<DropdownItem href="/ecommerce/apps-ecommerce-product-details">
			<i class="ri-eye-fill align-bottom me-2 text-muted" />
			View
		</DropdownItem>

		<DropdownItem href="/invoices/apps-invoices-create">
			<i class="ri-pencil-fill align-bottom me-2 text-muted" />
			Edit
		</DropdownItem>

		<DropdownItem href="/ecommerce/apps-ecommerce-add-product">
			<i class="ri-download-2-line align-bottom me-2 text-muted" />
			Download
		</DropdownItem>

		<DropdownItem divider />

		<DropdownItem href={null}>
			<i class="ri-delete-bin-fill align-bottom me-2 text-muted" />
			Delete
		</DropdownItem>
	</DropdownMenu>
</Dropdown>