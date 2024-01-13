<script>
  import { Card, CardBody, Col, Row } from "sveltestrap";

  import Slack from "../../../../assets/images/brands/slack.png";
</script>

<Col lg={12}>
  <Card class="mt-n4 mx-n4">
    <div class="bg-primary-subtle">
      <CardBody class="px-4 pb-4">
        <Row class="mb-3">
          <div class="col-md">
            <Row class="align-items-center g-3">
              <div class="col-md-auto">
                <div class="avatar-md">
                  <div class="avatar-title bg-white rounded-circle">
                    <img src={Slack} alt="" class="avatar-xs" />
                  </div>
                </div>
              </div>
              <div class="col-md">
                <div>
                  <h4 class="fw-bold">Product Designer</h4>
                  <div class="hstack gap-3 flex-wrap">
                    <div>
                      <i class="ri-building-line align-bottom me-1" />{" "}
                      Themesbrand
                    </div>
                    <div class="vr" />
                    <div>
                      <i class="ri-map-pin-2-line align-bottom me-1" />{" "}
                      Zuweihir, UAE
                    </div>
                    <div class="vr" />
                    <div>
                      Post Date :{" "}
                      <span class="fw-medium">15 Sep, 2021</span>
                    </div>
                    <div class="vr" />
                    <div class="badge rounded-pill bg-success fs-12">
                      Full Time
                    </div>
                  </div>
                </div>
              </div>
            </Row>
          </div>

          <div class="col-md-auto">
            <div class="hstack gap-1 flex-wrap mt-4 mt-md-0">
              <button
                type="button"
                class="btn btn-icon btn-sm btn-ghost-warning fs-16 shadow-none"
              >
                <i class="ri-star-fill" />
              </button>
              <button
                type="button"
                class="btn btn-icon btn-sm btn-ghost-primary fs-16 shadow-none"
              >
                <i class="ri-share-line" />
              </button>
              <button
                type="button"
                class="btn btn-icon btn-sm btn-ghost-primary fs-16 shadow-none"
              >
                <i class="ri-flag-line" />
              </button>
            </div>
          </div>
        </Row>
      </CardBody>
    </div>
  </Card>
</Col>
