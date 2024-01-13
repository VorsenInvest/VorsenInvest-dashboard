<script>
    import { Tooltip } from "sveltestrap";
    export let row;
    import Link from 'svelte-link';

    $: items = row.cell(6).data

</script>
<div class="avatar-group">
    {#each items as item,index}
        <Link href={null} class="avatar-group-item" id="avatar{index}">
            <img src="{import.meta.env.VITE_PUBLIC_BASE_PATH}/images/users/{item.img}" alt="" class="rounded-circle avatar-xxs" />
        </Link>
        <Tooltip target="avatar{index}" placement="top">
            Alexis
          </Tooltip>
    {/each}
</div>