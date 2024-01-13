<svelte:head>
  <title>Range Slider | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import { Row, Col, Container, Card, CardBody, CardTitle } from "sveltestrap";
    import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
    import RangeSlider from "svelte-range-slider-pips";
    let demo = ["😁"];
    const moods = ["😁", "😀", "😊", "😐", "😥", "😫"];
    let values = ["😐"];
  </script>

<div class="page-content" id="app">
    <Container fluid>
      <BreadCrumb title="Advanced Kit" breadcrumbItem="Range Slider" />
  
      <div class="row">
        <div class="col-12">
          <Card>
            <CardBody>
              <CardTitle class="h4">ION Range slider</CardTitle>
              <p class="card-title-desc">
                Cool, comfortable, responsive and easily customizable range slider
              </p>
              <Row>
                <Col xl="6">
                  <div class="p-3">
                    <h5 class="fs-15 mb-3 mt-0">Default</h5>
                    <RangeSlider pips first="label" last="label" values={[11]} />
                  </div>
                </Col>
                <Col xl="6">
                  <div class="p-3">
                    <h5 class="fs-15 mb-3 mt-0">Min-Max</h5>
                    <RangeSlider min={100} max={200} pips all="label" />
                  </div>
                </Col>
              </Row>
              <Row>
                <Col xl="6">
                  <div class="p-3">
                    <h5 class="fs-15 mb-3 mt-0">Prefix</h5>
                    <RangeSlider
                      pips
                      range
                      values={[30, 70]}
                      prefix="$"
                      all="label"
                    />
                  </div>
                </Col>
                <Col xl="6">
                  <div class="p-3">
                    <h5 class="fs-15 mb-3 mt-0">Range</h5>
                    <RangeSlider pips range values={[20, 60]} all="label" />
                  </div>
                </Col>
              </Row>
              <Row>
                <Col xl="6">
                  <div class="p-3">
                    <h5 class="fs-15 mb-3 mt-0">Step</h5>
                    <RangeSlider pips step={2.5} pipstep={10} all="label" />
                  </div>
                </Col>
                <Col xl="6">
                  <div class="p-3">
                    <h5 class="fs-15 mb-3 mt-0">Float</h5>
                    <RangeSlider
                      float
                      hover={true}
                      values={[40, 60]}
                      all="label"
                    />
                  </div>
                </Col>
              </Row>
              <Row>
                <Col xl="6">
                  <div class="p-3">
                    <h5 class="fs-15 mb-3 mt-0">Max value</h5>
                    <RangeSlider pips id="reverse-pips" max={20} all="label" />
                  </div>
                </Col>
                <Col xl="6">
                  <div class="p-3">
                    <h5 class="fs-15 mb-3 mt-0">Suffix</h5>
                    <RangeSlider
                      pips
                      range
                      values={[40, 60]}
                      suffix="%"
                      all="label"
                    />
                  </div>
                </Col>
              </Row>
            </CardBody>
          </Card>
        </div>
      </div>
    </Container>
  </div>