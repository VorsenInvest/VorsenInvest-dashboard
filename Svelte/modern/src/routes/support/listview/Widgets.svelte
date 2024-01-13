<script>
    import { Card, CardBody, Col } from "sveltestrap";
    export let ticketsWidgets;
</script>

{#each ticketsWidgets as item}
    <Col xxl={3} sm={6}>
        <Card class="card-animate">
            <CardBody>
                <div class="d-flex justify-content-between">
                    <div>
                        <p class="fw-medium text-muted mb-0">{item.title}</p>
                        <h2 class="mt-4 ff-secondary fw-semibold">
                            <span
                                class="counter-value"
                                data-target={item.counter}>0</span
                            >{item.suffix}
                        </h2>
                        <p class="mb-0 text-muted">
                            <span
                                class="badge bg-light text-{item.percentageClass} mb-0"
                            >
                                <i class="ri-arrow-up-line align-middle" />
                                {item.percentage}
                            </span> vs. previous month
                        </p>
                    </div>
                    <div>
                        <div class="avatar-sm flex-shrink-0">
                            <span
                                class="avatar-title bg-{item.iconColor}-subtle text-{item.iconColor} rounded-circle fs-4"
                            >
                                <i class={item.icon} />
                            </span>
                        </div>
                    </div>
                </div>
            </CardBody>
            <!-- end card body -->
        </Card>
        <!-- end card-->
    </Col>
{/each}
