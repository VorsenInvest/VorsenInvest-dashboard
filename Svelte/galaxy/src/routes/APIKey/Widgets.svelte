<script>
    import { Card, CardBody, Col, Progress } from "sveltestrap";
    import Counter from "../../Components/Common/CounterPage.svelte";
    import { CheckCircleIcon, AlertOctagonIcon } from "svelte-feather-icons";
    export let onhandleShow;
</script>

<Counter />
<Col class="col-lg-4">
    <Card class="card card-height-100">
        <CardBody class="card-body">
            <h5 class="card-title mb-3">Developer Plan</h5>
            <div class="progress animated-progress custom-progress mb-1">
                <Progress
                    value={38}
                    color="info"
                    class="progress-bar bg-secondary"
                    role="progressbar"
                    style="width: 38%"
                    aria-valuenow="38"
                    aria-valuemin="0"
                    aria-valuemax="100"
                />
            </div>
            <p class="text-muted mb-2">You used 215 of 2000 of your API</p>
            <div class="text-end">
                <button
                    type="button"
                    class="btn btn-primary btn-sm create-btn" on:click={onhandleShow}>
                    Create API Key
                </button>
            </div>
        </CardBody>
    </Card>
</Col>
<Col class="col-lg-4">
    <Card class="card card-animate card-height-100">
        <CardBody class="card-body">
            <div class="d-flex justify-content-between">
                <div>
                    <p class="fw-medium text-muted mb-0">
                        Successful conversions
                    </p>
                    <h2 class="mt-4 ff-secondary fw-bold">
                        <span class="counter-value" data-target="50" />
                    </h2>
                    <p class="mb-0 text-muted">
                        <span class="badge bg-light text-success mb-0">
                            <i class="ri-arrow-up-line align-middle" /> 8.24 %{" "}
                        </span>{" "}
                        7 last week
                    </p>
                </div>
                <div>
                    <div class="avatar-sm flex-shrink-0">
                        <span
                            class="avatar-title bg-success-subtle rounded-circle fs-2"
                        >
                            <CheckCircleIcon class="text-success" />
                        </span>
                    </div>
                </div>
            </div>
        </CardBody>
    </Card>
</Col>
<Col class="col-lg-4">
    <Card class="card card-animate card-height-100">
        <CardBody class="card-body">
            <div class="d-flex justify-content-between">
                <div>
                    <p class="fw-semibold text-muted mb-0">
                        Failed conversions
                    </p>
                    <h1 class="mt-4 ff-secondary fw-bold">
                        <span class="counter-value" data-target="8" />
                    </h1>
                    <p class="mb-0 text-muted">
                        <span class="badge bg-light text-danger mb-0">
                            <i class="ri-arrow-down-line align-middle" /> 25.87
                            %{" "}
                        </span>{" "}
                        7 last week
                    </p>
                </div>
                <div>
                    <div class="avatar-sm flex-shrink-0">
                        <span
                            class="avatar-title bg-danger-subtle rounded-circle fs-2"
                        >
                            <AlertOctagonIcon class="text-danger" />
                        </span>
                    </div>
                </div>
            </div>
        </CardBody>
    </Card>
</Col>
