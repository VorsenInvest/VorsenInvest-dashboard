<svelte:head>
  <title>Ranking | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
import { Container } from "sveltestrap";
import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
import Grid from 'gridjs-svelte';
import { html } from 'gridjs';
import Select from "svelte-select";
import nftranking from '../../../common/data/NFTMarketplace'

const data = nftranking.NFTRanking;
let status="All Time";
const SingleOptions = [
		{ value: "All Time", label: "All Time" },
		{ value: "1 Day", label: "1 Day" },
		{ value: "7 Days", label: "7 Days" },
		{ value: "15 Days", label: "15 Days" },
		{ value: "1 Month", label: "1 Month" },
		{ value: "6 Month", label: "6 Month" },
	];
const columns = [
        {
			name: 'Ranking',
            id: 'ranking',
            width: '98px',
            sort: true,
			formatter: (cell) => {
                if (cell < 4) {
                    return html(`<div class="ranking text-success fw-semibold">#${cell}</div>`);
                } else {
                    return html(`<div class="ranking">#${cell}</div>`);
                }
            }
		},
        {
			id: 'img',
			hidden: true
		},
        {
            name: "Collection",
            id: "collection",
            filterable: false,
            sort: true,
            formatter: (cell, row) => {
                return html(`<div class="collection">
                    <div class="d-flex align-items-center">
                        <img src=${row.cells[1].data} alt="" class="avatar-xs rounded-circle object-cover me-2" /> <a href="/NFTmarketplace/Itemdetails/apps-nft-item-details" class="link-dark">${cell}</a>
                    </div>
                </div>`)
            }
        },
        {
                name: "Volume",
                id: "volume_price",
                filterable: false,
                sort: true,
            },
            {
                name: "24h%",
                id: "hours",
                filterable: false,
                sort: true,
                formatter: (cell) => {
                    if (cell > 0) {
                        return html(`<h6 class="text-success mb-1 24h" > ${cell} ETH</h6 >`);
                    } else {
                        return html(`<h6 class="text-danger mb-1 24h">${cell} ETH</h6>`);
                    }
                }
            },
            {
                name: "7d%",
                id: "day",
                filterable: false,
                sort: true,
                formatter: (cell) => {
                    if (cell > 0) {
                        return html(`<h6 class="text-success mb-1 7d" > ${cell} ETH</h6 >`);
                    } else {
                        return html(`<h6 class="text-danger mb-1 7d">${cell} ETH</h6>`);
                    }
                }
            },
            {
                name: "Item",
                id: "item",
                filterable: false,
                sort: true,
            },
            {
                name: "Floor Price",
                id: "floor_price",
                filterable: false,
                sort: true,
            },
	];
</script>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Ranking" pageTitle="NFT Marketplace" />
        <div class="row">
            <div class="col-lg-12">
                <div class="card" id="contactList">
                    <div class="card-header border-0">
                        <div class="d-flex align-items center">
                            <h5 class="card-title mb-0 flex-grow-1">The top NFTs ranking on Velzon</h5>
                            <p class="text-muted mb-0">Updated: 28 April, 2022 08:05:00</p>
                        </div>
                    </div>
                    <div class="card-body">
                        <div class="row justify-content-between g-3">
                            <div class="col-xxl-3 col-sm-6">
                                <div class="search-box">
                                    <input type="text" class="form-control search" placeholder="Search for ...">
                                    <i class="ri-search-line search-icon"></i>
                                </div>
                            </div>
                            <!--end col-->
                            <div class="col-xxl-2 col-sm-4">
                                <Select bind:value={status}
								class="form-control"
								placeholder="Choose ..."
								title="idStatus"
								items={SingleOptions}
							/>
                            </div>
                            <!--end col-->
                        </div>
                    </div>
                    <div class="card-body gridjs-border-none">
                        {#if (data.length || []) > 0}
                            <Grid {data} {columns} className={{ th: "text-muted" }} pagination={{ enabled: true, limit: 10 }} />
                        {:else}
                            <div class="noresult">
                                <div class="text-center">
                                    <lord-icon src="https://cdn.lordicon.com/msoeawqm.json" trigger="loop" colors="primary:#8c68cd,secondary:#4788ff" style="width: 75px; height: 75px"></lord-icon>
                                    <h5 class="mt-2">Sorry! No Result Found</h5>
                                    <p class="text-muted mb-0">We've searched more than 150+ transactions We did not find any transactions for you search.</p>
                                </div>
                            </div>
                        {/if}
                    </div>
                </div>
            </div>
        </div>
    </Container>
</div>