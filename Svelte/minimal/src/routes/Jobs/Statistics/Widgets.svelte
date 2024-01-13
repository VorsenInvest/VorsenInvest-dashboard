<script>
    import { Card, Col } from "sveltestrap";
    import jobWidgets from "../../../common/data/appsJobs";
    import Charts from "./Charts.svelte";

</script>
{#each jobWidgets.jobWidgets as item}
    <Col class="col-xl-3 col-md-6">
        <Card class="card card-height-100">
        <div class="d-flex">
            <div class="flex-grow-1 p-3">
            <h5 class="mb-3">{item.lable}</h5>
            <p class="mb-0 text-muted">
                <span
                class={"badge bg-light text-" + item.badgeColor + " mb-0"}
                >
                {" "}
                <i class={item.icon + "align-middle"}></i> {item.number}
                </span>{" "}
                vs. previous month
            </p>
            </div>
            <div>
                <Charts seriesData={item.series} dataColors={item.chartColor} id={item.id} />
            </div>
        </div>
        </Card>
    </Col>
{/each}