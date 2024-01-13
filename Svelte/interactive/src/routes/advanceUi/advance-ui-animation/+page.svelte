<script>
  import { Card, CardBody, CardHeader, Col, Container, Row } from "sveltestrap";
  import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
  import PrismCode from "../../../Components/Common/Prism.svelte";
  import { onMount } from 'svelte';

  import macimg from '../../../assets/images/mac-img.png'
  // Fade Up

  const fadeUpCode = `<div data-aos="fade-up"></div>`;

  // Fade Down
  const fadeDownCode = `<div data-aos="fade-down"></div>`;

  // Fade Right
  const fadeRightCode = `<div data-aos="fade-right"></div>`;

  // Fade Left
  const fadeLeftCode = `<div data-aos="fade-left"></div>`;

  // Fade Up Right
  const fadeUpRightCode = `<div data-aos="fade-up-right"></div>`;

  // Fade Up Left
  const fadeUpLeftCode = `<div data-aos="fade-up-left"></div>`;

  // Fade Down Right
  const fadeDownRightCode = `<div data-aos="fade-down-right"></div>`;

  // Fade Down Left
  const fadeDownLeftCode = `<div data-aos="fade-down-left"></div>`;

  // Flip Left
  const flipLeftCode = `<div data-aos="flip-left"></div>`;

  // Flip Right
  const flipRightCode = `<div data-aos="flip-right"></div>`;

  // Flip Up
  const filpUpCode = `<div data-aos="flip-up"></div>`;

  // Flip Down
  const filpDownCode = `<div data-aos="flip-down"></div>`;

  // Zoom In
  const zoomInCode = `<div data-aos="zoom-in"></div>`;

  // Zoom Out
  const zoomOutCode = `<div data-aos="zoom-out"></div>`;

  // Zoom In Up
  const zoomInUpCode = `<div data-aos="zoom-in-up"></div>`;

  // Zoom Out Up
  const zoomOutUpCode = `<div data-aos="zoom-out-up"></div>`;

  // Zoom In Down
  const zoomInDownCode = `<div data-aos="zoom-in-down"></div>`;

  // Zoom Out Down
  const zoomOutDownCode = `<div data-aos="zoom-out-down"></div>`;

  // Zoom In Right
  const zoomInRightCode = `<div data-aos="zoom-in-right"></div>`;

  // Zoom Out Right
  const zoomOutRightCode = `<div data-aos="zoom-out-right"></div>`;

  // Zoom In Left
  const zoomInLeftCode = `<div data-aos="zoom-in-left"></div>`;

  // Zoom Out Left
  const zoomOutLeftCode = `<div data-aos="zoom-out-left"></div>`;

  // Duration
  const durationCode = `<div data-aos="fade-up" data-aos-duration="3000"></div>`;

  // Easing="linear"
  const easingLinearCode = `<div data-aos="fade-down" data-aos-easing="linear" data-aos-duration="1500"></div>`;

  // Offset
  const offset1Code = `<div data-aos="fade-right" data-aos-offset="300" data-aos-easing="ease-in-sine"></div>`;

  // Offset
  const offset2Code = `<div data-aos="fade-left" data-aos-offset="500" data-aos-duration="500"></div>`;

  // Easing="ease-in-back"
  const easeInBackCode = `<div data-aos="fade-zoom-in" data-aos-easing="ease-in-back" data-aos-delay="300" data-aos-offset="0"></div>`;

  // Easing="ease-out-cubic"
  const easeOutCubicCode = `<div data-aos="flip-left" data-aos-easing="ease-out-cubic" data-aos-duration="2000"></div>`;

  import AOS from "aos";
  import "aos/dist/aos.css";
  
  onMount(() => {
    AOS.init();
  });
</script>

<svelte:head>
  <title>Animation | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
  <Container fluid>
    <BreadCrumb title="Animation" pageTitle="Advance UI" />
    <Row>
      <Col lg={12}>
        <Card>
          <CardHeader>
            <div class="text-center">
              <h4 class="card-title mb-0">Fade Animation</h4>
            </div>
          </CardHeader>

          <CardBody>
            <div class="live-preview">
              <div>
                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Fade Up</h4>
                      <PrismCode
                        code={fadeUpCode}
                        id="advanceuifadeup"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} lg={8}>
                          <div data-aos="fade-up">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Fade Down</h4>

                      <PrismCode
                        code={fadeDownCode}
                        id="advanceuifadedown"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} lg={8}>
                          <div data-aos="fade-down">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>

                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Fade Right</h4>

                      <PrismCode
                        code={fadeRightCode}
                        id="advanceuifaderight"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="fade-right">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Fade Left</h4>

                      <PrismCode
                        code={fadeLeftCode}
                        id="advanceuifadeleft"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="fade-left">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>

                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Fade Up Right</h4>

                      <PrismCode
                        code={fadeUpRightCode}
                        id="advanceuifadeupright"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="fade-up-right">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Fade Up Left</h4>

                      <PrismCode
                        code={fadeUpLeftCode}
                        id="advanceuifadeupleft"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="fade-up-left">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Fade Down Right</h4>

                      <PrismCode
                        code={fadeDownRightCode}
                        id="advanceuifadedownright"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="fade-down-right">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Fade Down Left</h4>

                      <PrismCode
                        code={fadeDownLeftCode}
                        id="advanceuifadedownleft"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="fade-down-left">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>
              </div>
            </div>
          </CardBody>
        </Card>
      </Col>
    </Row>

    <Row>
      <Col lg={12}>
        <Card>
          <CardHeader>
            <div class="text-center">
              <h4 class="card-title mb-0">Flip Animation</h4>
            </div>
          </CardHeader>

          <CardBody>
            <div class="live-preview">
              <div>
                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Flip Left</h4>

                      <PrismCode
                        code={flipLeftCode}
                        id="flipLeftCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="flip-left">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Flip Right</h4>

                      <PrismCode
                        code={flipRightCode}
                        id="flipRightCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="flip-right">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>

                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Flip Up</h4>

                      <PrismCode
                        code={filpUpCode}
                        id="filpUpCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="flip-up">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Flip Down</h4>

                      <PrismCode
                        code={filpDownCode}
                        id="filpDownCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="flip-down">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>
              </div>
            </div>
          </CardBody>
        </Card>
      </Col>
    </Row>

    <Row>
      <Col lg={12}>
        <Card>
          <CardHeader>
            <div class="text-center">
              <h4 class="card-title mb-0">Zoom Animation</h4>
            </div>
          </CardHeader>

          <CardBody>
            <div class="live-preview">
              <div>
                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom In</h4>

                      <PrismCode
                        code={zoomInCode}
                        id="zoomInCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-in">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>

                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom In Up</h4>

                      <PrismCode
                        code={zoomInUpCode}
                        id="zoomInUpCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-in-up">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>

                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom In Down</h4>

                      <PrismCode
                        code={zoomInDownCode}
                        id="zoomInDownCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-in-down">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>

                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom In Right</h4>

                      <PrismCode
                        code={zoomInRightCode}
                        id="zoomInRightCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-in-right">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>

                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom In Left</h4>

                      <PrismCode
                        code={zoomInLeftCode}
                        id="zoomInLeftCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-in-left">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom Out</h4>

                      <PrismCode
                        code={zoomOutCode}
                        id="zoomOutCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-out">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>

                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom Out Up</h4>

                      <PrismCode
                        code={zoomOutUpCode}
                        id="zoomOutUpCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-out-up">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>

                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom Out Down</h4>

                      <PrismCode
                        code={zoomOutDownCode}
                        id="zoomOutDownCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-out-down">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>

                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom Out Right</h4>

                      <PrismCode
                        code={zoomOutRightCode}
                        id="zoomOutRightCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-out-right">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>

                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Zoom Out Left</h4>

                      <PrismCode
                        code={zoomOutLeftCode}
                        id="zoomOutLeftCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="zoom-out-left">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>
              </div>
            </div>
          </CardBody>
        </Card>
      </Col>
    </Row>

    <Row>
      <Col lg={12}>
        <Card>
          <CardHeader>
            <div class="text-center">
              <h4 class="card-title mb-0">Animation Examples</h4>
            </div>
          </CardHeader>
          <CardBody>
            <div class="live-preview">
              <div>
                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Duration</h4>

                      <PrismCode
                        code={durationCode}
                        id="durationCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div data-aos="fade-up" data-aos-duration="3000">
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Easing="linear"</h4>

                      <PrismCode
                        code={easingLinearCode}
                        id="easingLinearCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div
                            data-aos="fade-down"
                            data-aos-easing="linear"
                            data-aos-duration="1500"
                          >
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>

                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Offset</h4>

                      <PrismCode
                        code={offset1Code}
                        id="offset1Code"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div
                            data-aos="fade-right"
                            data-aos-offset="300"
                            data-aos-easing="ease-in-sine"
                          >
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Offset</h4>

                      <PrismCode
                        code={offset2Code}
                        id="offset2Code"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div
                            data-aos="fade-left"
                            data-aos-offset="500"
                            data-aos-duration="500"
                          >
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>

                <Row>
                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Easing="ease-in-back"</h4>

                      <PrismCode
                        code={easeInBackCode}
                        id="easeInBackCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div
                            data-aos="fade-zoom-in"
                            data-aos-easing="ease-in-back"
                            data-aos-delay="300"
                            data-aos-offset="0"
                          >
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>

                  <Col lg={6}>
                    <div class="p-4 pb-0 border mt-4">
                      <h4 class="mb-4 text-center">Easing="ease-out-cubic"</h4>

                      <PrismCode
                        code={easeOutCubicCode}
                        id="easeOutCubicCode"
                      />

                      <Row class="justify-content-center">
                        <Col sm={10} md={8}>
                          <div
                            data-aos="flip-left"
                            data-aos-easing="ease-out-cubic"
                            data-aos-duration="2000"
                          >
                            <img
                              src={macimg}
                              alt="Mac "
                              class="img-fluid"
                            />
                          </div>
                        </Col>
                      </Row>
                    </div>
                  </Col>
                </Row>
              </div>
            </div>
          </CardBody>
        </Card>
      </Col>
    </Row>
  </Container>
</div>
