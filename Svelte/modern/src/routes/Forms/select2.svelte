<svelte:head>
  <title>Select2 | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
import { Card, CardBody, CardHeader, Col, Container, Row } from 'sveltestrap';
import BreadCrumb from '../../Components/Common/BreadCrumb.svelte';
import Select from "svelte-select";
const sortbyname = [
        { label: "Alabama", value: "AL" },
        { label: "Madrid", value: "MA" },
        { label: "Toronto", value: "TO" },
        { label: "Londan", value: "LO" },
        { label: "Wyoming", value: "WY" }
    ];

    const sortbyMulti = [
        { label: "London", value: "London", group : "UK" },
        { label: "Manchester", value: "Manchester", group : "UK" },
        { label: "Liverpool", value: "Liverpool", group : "UK" },
        { label: "Paris", value: "Paris", group : "FR" },
        { label: "Lyon", value: "Lyon", group : "FR" },
        { label: "Marseille", value: "Marseille", group : "FR" },
        { label: "Madrid", value: "Madrid", group : "SP" },
        { label: "Barcelona", value: "Barcelona", group : "SP" },
        { label: "Malaga", value: "Malaga", group : "SP" },
        { label: "Montreal", value: "Montreal", group : "CA" },
        { label: "Toronto", value: "Toronto", group : "CA" },
        { label: "Vancouver", value: "Vancouver", group : "CA" }
    ];

    const ajaxSelectOption = [
        { label: "enhancement", value: "enhancement" },
        { label: "bug", value: "bug" },
        { label: "duplicate", value: "duplicate" },
        { label: "invalid", value: "invalid" },
        { label: "wontfix", value: "wontfix" }
    ];

    const tempOption = [
        { label: "Alaska", value: "AK", group : "Alaskan/Hawaiian Time Zone" },
        { label: "Hawaii", value: "HI", group : "Alaskan/Hawaiian Time Zone" },
        { label: "California", value: "CA" ,group : "Pacific Time Zone" },
        { label: "Nevada", value: "NV" ,group : "Pacific Time Zone" },
        { label: "Oregon", value: "OR" ,group : "Pacific Time Zone" },
        { label: "Washington", value: "WA" ,group : "Pacific Time Zone" }
    ];

    const selTempOption = [
        { label: "Alaska", value: "AK", group : "Alaskan/Hawaiian Time Zone" },
        { label: "Hawaii", value: "HI", group : "Alaskan/Hawaiian Time Zone" },
        { label: "California", value: "CA" ,group : "Pacific Time Zone" },
        { label: "Nevada", value: "NV" ,group : "Pacific Time Zone" },
        { label: "Oregon", value: "OR" ,group : "Pacific Time Zone" },
        { label: "Washington", value: "WA" ,group : "Pacific Time Zone" }
    ];

    const dissortbyname = [
        { label: "Alabama", value: "AL" },
        { label: "Madrid", value: "MA" },
        { label: "Toronto", value: "TO" },
        { label: "Londan", value: "LO" },
        { label: "Wyoming", value: "WY" }
    ];

    const dissortbyMulti = [
        { label: "London", value: "London", group : "UK" },
        { label: "Manchester", value: "Manchester", group : "UK" },
        { label: "Liverpool", value: "Liverpool", group : "UK" },
        { label: "Paris", value: "Paris", group : "FR" },
        { label: "Lyon", value: "Lyon", group : "FR" },
        { label: "Marseille", value: "Marseille", group : "FR" },
        { label: "Madrid", value: "Madrid", group : "SP" },
        { label: "Barcelona", value: "Barcelona", group : "SP" },
        { label: "Malaga", value: "Malaga", group : "SP" },
        { label: "Montreal", value: "Montreal", group : "CA" },
        { label: "Toronto", value: "Toronto", group : "CA" },
        { label: "Vancouver", value: "Vancouver", group : "CA" }
    ];
    let disable = false;
    const setdisable = (sdisable) =>{
        disable = sdisable;
    }
</script>
<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Select2" pageTitle="Forms" />
        <Row>
            <Col lg={12}>
                <Card>
                    <CardHeader>
                        <h5 class="card-title mb-0">Basic Select2</h5>
                    </CardHeader>
                    <CardBody>
                        <p class="text-muted">Use <code>js-example-basic-single</code>, <code>js-example-basic-multiple</code>, <code>js-example-data-array</code>, <code>js-example-templating</code>, <code>select-flag-templating</code>,  class to show select2 example.</p>
                        <Row class="g-4">
                            <Col lg={4}>
                                <h6 class="fw-semibold">Basic Select</h6>
                                <Select
                                    items={sortbyname}
                                    id="choices-single-default"
                                    class="js-example-basic-single mb-0"
                                    name="state"
                                />
                            </Col>
                            <Col lg={4}>
                                <h6 class="fw-semibold">Multi Select</h6>

                                <Select
                                    isMulti={true}
                                    items={sortbyMulti}
                                />
                            </Col>
                            <Col lg={4}>
                                <h6 class="fw-semibold">Ajax Select</h6>

                                <Select
                                    items={ajaxSelectOption}
                                    isLoading={true}
                                />
                            </Col>

                            <Col lg={4}>
                                <h6 class="fw-semibold">Templating</h6>

                                <Select
                                    items={tempOption}
                                    id="choices-single-default"
                                    class="js-example-templating mb-0"
                                />
                            </Col>
                            <Col lg={4}>
                                <h6 class="fw-semibold">Selections Templating</h6>

                                <Select
                                    items={selTempOption}
                                    id="choices-single-default"
                                    class="select-flag-templating mb-0"
                                />
                            </Col>
                        </Row>
                    </CardBody>
                </Card>
            </Col>
        </Row>

        <Row>
            <Col lg={12}>
                <Card>
                    <CardHeader>
                        <h5 class="card-title mb-0">Disabling a Select2 Control</h5>
                    </CardHeader>
                    <CardBody>
                        <p class="text-muted">Select2 will respond to the disabled attribute on <code>&lt;select&gt;</code> elements. You can also initialize Select2 with disabled: true to get the same effect.</p>
                        <div class="vstack gap-3">

                            <Select
                                items={dissortbyname}
                                class="js-example-disabled mb-0"
                                isDisabled={disable}
                            />

                            <Select
                                isMulti={true}
                                items={dissortbyMulti}
                                isDisabled={disable}
                            />
                        </div>
                        <div class="hstack gap-2 mt-3">
                            <button type="button" class="js-programmatic-enable btn btn-primary" on:click={() => setdisable(false)}>
                                Enable
                            </button>
                            <button type="button" class="js-programmatic-disable btn btn-success" on:click={() => setdisable(true)}>
                                Disable
                            </button>
                        </div>
                    </CardBody>
                </Card>
            </Col>
        </Row>
    </Container>
</div>