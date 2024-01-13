<svelte:head>
  <title>Pickers | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import { Card, CardBody, CardHeader, Container, Form, Row, Col, Label } from 'sveltestrap';
	import BreadCrumb from '../../../Components/Common/BreadCrumb.svelte';
	import Flatpickr from 'svelte-flatpickr';
  import ColorPicker, { ChromeVariant } from 'svelte-awesome-color-picker';
</script>
<div class="page-content">
        
    <Container fluid>
      <BreadCrumb title="Pickers" pageTitle="Forms" />

      <Row>
        <Col lg={12}>
          <Card >
            <CardHeader >
              <h4 class="card-title mb-0">Flatpickr - Datepicker</h4>
            </CardHeader>
            <CardBody>
              <Form >
                <Row class="gy-3">
                  <Col lg={6}>
                    <div>
                      <Label class="form-label">Basic</Label>
                    <Flatpickr
                      class="form-control"
                      options={{
                        dateFormat: "d M, Y"
                      }}
                    />
                    </div>
                  </Col>
                  <Col lg={6}>
                    <div>
                      <Label class="form-label">DateTime</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          enableTime: true,
                          dateFormat: "Y-m-d H:i",
                        }}
                      />
                    </div>
                  </Col>
                </Row>
                <Row >
                  <Col lg={6}>
                    <div class="mt-3">
                      <Label class="form-label">Human-Friendly Dates</Label>
                      <Flatpickr
                        class="form-control flatpickr-input"
                        options={{
                          altInput: true,
                          altFormat: "F j, Y",
                          dateFormat: "Y-m-d",
                        }}
                      />
                    </div>
                  </Col>
                  <Col lg={6}>
                    <div class="mt-3">
                      <Label class="form-label">MinDate and MaxDate</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          minDate: "today",
                          maxDate: new Date().fp_incr(14)
                        }}
                      />
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col lg={6} >
                    <div class="mt-3">
                      <Label class="form-label">Default Date</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          dateFormat: "Y-m-d",
                          defaultDate: ["2022-01-20"]
                        }}
                      />
                    </div>
                  </Col>
                  <Col lg={6} >
                    <div class="mt-3">
                      <Label class="form-label">Disabling Dates</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          disable: ["2022-01-30", "2022-02-21", "2022-03-08", new Date(2025, 4, 9)],
                          dateFormat: "Y-m-d",
                        }}
                      />
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col lg={6}>
                    <div class="mt-3">
                      <Label class="form-label">Selecting Multiple Dates</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          mode: "multiple",
                          dateFormat: "Y-m-d"
                        }}
                      />
                    </div>
                  </Col>
                  <Col lg={6}>
                    <div class="mt-3">
                      <Label class="form-label">Range</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          mode: "range",
                          dateFormat: "Y-m-d"
                        }}
                      />
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col lg={6} >
                    <div class="mt-3">
                      <Label class="form-label">Inline</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          inline: true,
                          dateFormat: "Y-m-d"
                        }}
                      />
                    </div>
                  </Col>
                  <Col lg={6} >
                    <div class="mt-3">
                      <Label class="form-label">Week Numbers</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          dateFormat: "d M, Y",
                          weekNumbers: true,
                        }}
                      />
                    </div>
                  </Col>
                </Row>
              </Form>
            </CardBody>
          </Card>
        </Col>
      </Row>
      <Row>
        <Col lg={12}>
          <Card>
            <CardHeader>
              <h4 class="card-title mb-0">Flatpickr - Timepicker</h4>
            </CardHeader>
            <CardBody>
              <Form >
                <Row class="gy-3">
                  <Col lg={6}>
                    <div>
                      <Label class="form-label">Timepicker</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          enableTime: true,
                          noCalendar: true,
                          dateFormat: "H:i",
                        }}
                      />
                    </div>
                  </Col>
                  <Col lg={6}>
                    <div>
                      <Label class="form-label">24-hour Time Picker</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          enableTime: true,
                          noCalendar: true,
                          dateFormat: "H:i",
                          time_24hr: true
                        }}
                      />
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col lg={6}>
                    <div class="mt-3">
                      <Label class="form-label">Time Picker w/ Limits</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          enableTime: true,
                          noCalendar: true,
                          dateFormat: "H:i",
                          minTime: "16:00",
                          maxTime: "22:30",
                        }}
                      />
                    </div>
                  </Col>
                  <Col lg={6}>
                    <div class="mt-3">
                      <Label class="form-label">Preloading Time</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          enableTime: true,
                          noCalendar: true,
                          dateFormat: "H:i",
                          defaultDate: "13:45"
                        }}
                      />
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col lg={6}>
                    <div class="mt-3">
                      <Label class="form-label">Inline</Label>
                      <Flatpickr
                        class="form-control"
                        options={{
                          enableTime: true,
                          noCalendar: true,
                          inline: true,
                        }}
                      />
                    </div>
                  </Col>
                </Row>
              </Form>
            </CardBody>
          </Card>
        </Col>
      </Row>
      <Row>
        <Col lg={12}>
          <Card>
            <CardHeader>
              <h4 class="card-title mb-0">Colorpicker</h4>
            </CardHeader>
            <CardBody>
              <Form >
                <h5 class="fs-14 mb-3">Themes</h5>
                <Row class="gy-3">
                  <Col lg={4}>
                    <div>
                      <Label class="form-label">Classic Demo</Label>
                      
                      <ColorPicker hex={'#405189'} label="" />
                    </div>
                  </Col>
                  <Col lg={4}>
                    <div>
                      <Label class="form-label">Chrome Variant</Label>
                      
                      <ColorPicker hex={'#405189'} components={ChromeVariant} label="" />
                    </div>
                  </Col>
                </Row>
              </Form>
            </CardBody>
          </Card>
        </Col>
      </Row>

    </Container>
  </div>