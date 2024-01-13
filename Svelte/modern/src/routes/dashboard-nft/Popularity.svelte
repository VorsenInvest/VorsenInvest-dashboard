<script>
    import { Card, CardBody, CardHeader, Col } from 'sveltestrap';
    import data from "../../common/data/dashboardNFT";
    import Link from 'svelte-link'
    import PopularityChart from "./PopularityChart.svelte";

</script>
<Col xxl={3}>
    <Card>
        <CardHeader class="border-0 pb-0">
            <h6 class="card-title mb-0">Popularity</h6>
        </CardHeader>
        <div>
            <PopularityChart dataColors={["--vz-success", "--vz-warning"]} />
        </div>
    </Card>

    <Card>
        <CardHeader class="d-flex align-items-center">
            <h6 class="card-title mb-0 flex-grow-1">History of Bids</h6>
            <Link class="text-muted" href="/NFTmarketplace/Itemdetails/apps-nft-item-details">
                See All <i class="ri-arrow-right-line align-bottom"></i>
            </Link>
        </CardHeader>
        <CardBody>
            <div class="table-responsive table-card">
                <div id="scrollbar" data-simplebar style="max-height: 382px">
                    <ul class="list-group list-group-flush">
                        {#each data.popularityData as item}
                            <li class="list-group-item list-group-item-action">
                                <div class="d-flex align-items-center">
                                    <img src={item.img} alt="" class="avatar-xs object-cover rounded-circle" />
                                    <div class="ms-3 flex-grow-1">
                                        <Link href={null} class="stretched-link">
                                            <h6 class="fs-14 mb-1">{item.author}</h6>
                                        </Link>
                                        <p class="mb-0 text-muted">{item.username}</p>
                                    </div>
                                    <div>
                                        <h6>{item.price}</h6>
                                    </div>
                                </div>
                            </li>
                        {/each}
                    </ul>
                </div>
            </div>
        </CardBody>
    </Card>
</Col>