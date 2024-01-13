<script>
	
	import Link from 'svelte-link';
	import CreateTaskModal from './createTaskModal.svelte';
	export let row;

	$: item = row.cell(3).data;
	let isOpen = false;
	let createModal = false;
	const toggle = () => (isOpen = !isOpen);
	const setCloseModal = (status) => {
		createModal = status;
	};
</script>

<div class="d-flex">
	<div class="flex-grow-1 tasks_name">{item}</div>
	<div class="flex-shrink-0 ms-4">
		<ul class="list-inline tasks-list-menu mb-0">
			<li class="list-inline-item">
				<Link href="/tasks/apps-tasks-details">
					<i class="ri-eye-fill align-bottom me-2 text-muted" />
				</Link>
			</li>
			<li class="list-inline-item">
				<Link href={''} on:click={() => setCloseModal(true)}>
					<i class="ri-pencil-fill align-bottom me-2 text-muted" />
				</Link>
			</li>
			<li class="list-inline-item">
				<Link href="{null}" class="remove-item-btn">
					<i class="ri-delete-bin-fill align-bottom me-2 text-muted" />
				</Link>
			</li>
		</ul>
	</div>
</div>

<CreateTaskModal
	show={createModal}
	onDeleteClick={toggle}
	onCloseClick={() => setCloseModal(false)}
/>