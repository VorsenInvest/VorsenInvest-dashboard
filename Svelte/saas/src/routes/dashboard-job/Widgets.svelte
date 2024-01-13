<script>
    import { Card, CardBody, Col, Row } from "sveltestrap";
    import jobWidgets from "../../common/data/dashboardJobs";
    import DashboardCharts from './DashboardCharts.svelte'
</script>
<Col xl={6}>
    <div class="d-flex flex-column h-100">
      <Row>
        {#each jobWidgets.jobWidgets as widget}
        <Col xl={6} md={6}>
            <Card class="card-animate overflow-hidden">
              <div
                class="position-absolute start-0"
                style="z-Index: 0"
              >
                <svg
                  version="1.2"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 200 120"
                  width="200"
                  height="120"
                >
                  <path
                    id="Shape 8"
                    style="opacity: .05;fill: #865ce2;"
                    d="m189.5-25.8c0 0 20.1 46.2-26.7 71.4 0 0-60 15.4-62.3 65.3-2.2 49.8-50.6 59.3-57.8 61.5-7.2 2.3-60.8 0-60.8 0l-11.9-199.4z"
                  />
                </svg>
              </div>
              <CardBody style="z-Index: 1">
                <div class="d-flex align-items-center">
                  <div class="flex-grow-1 overflow-hidden">
                    <p class="text-uppercase fw-medium text-muted text-truncate mb-3">
                      {" "}
                      {widget.lable}
                    </p>
                    <h4 class="fs-22 fw-bold ff-secondary mb-0">
                      <span class="counter-value" data-target={widget.jobs} />
                    </h4>
                  </div>
                  <div class="flex-shrink-0">
                    <DashboardCharts
                      seriesData={widget.series}
                      colors={widget.color}
                      id={"widget"+ widget.id}
                    />
                  </div>
                </div>
              </CardBody>
            </Card>
          </Col>
        {/each}
      </Row>
    </div>
  </Col>