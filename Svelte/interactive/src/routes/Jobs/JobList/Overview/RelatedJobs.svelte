<script>
  import Link from "svelte-link";
  import { Card, CardBody, Col, Row } from "sveltestrap";
  import overviewJobs from "../../../../common/data/appsJobs";
</script>

<Row>
  <Col lg={12}>
    <div class="d-flex align-items-center mb-4">
      <div class="flex-grow-1">
        <h5 class="mb-0">Related Jobs</h5>
      </div>
      <div class="flex-shrink-0">
        <Link href={null} class="btn btn-ghost-success">
          View All{" "}
          <i class="ri-arrow-right-line ms-1 align-bottom" />
        </Link>
      </div>
    </div>
  </Col>
  {#each overviewJobs.overviewJobs as item}
    <Col xl={4}>
      <Card>
        <CardBody>
          <button
            type="button"
            class="btn btn-icon btn-soft-danger float-end"
            data-bs-toggle="button"
            aria-pressed="true"
          >
            <i class="mdi mdi-cards-heart fs-16" />
          </button>
          <div class="avatar-sm mb-4">
            <div class="avatar-title bg-{item.imgbgColor}-subtle rounded">
              <img src={item.companyLogo} alt="" class="avatar-xxs" />
            </div>
          </div>
          <Link href={null}>
            <h5>{item.jobTitle}</h5>
          </Link>
          <p class="text-muted">{item.companyName}</p>

          <div class="d-flex gap-4 mb-3">
            <div>
              <i
                class="ri-map-pin-2-line text-primary me-1 align-bottom"
              />{" "}
              {item.location}
            </div>

            <div>
              <i class="ri-time-line text-primary me-1 align-bottom" />{" "}
              {item.time}
            </div>
          </div>

          <p class="text-muted">{item.description}</p>

          <div class="hstack gap-2">
            <span class="badge bg-success-subtle text-success">{item.s1}</span>
            <span class="badge bg-primary-subtle text-primary">{item.s2}</span>
            <span class="badge bg-danger-subtle text-danger">{item.s3}</span>
          </div>

          <div class="mt-4 hstack gap-2">
            <Link href={null} class="btn btn-soft-primary w-100">Apply Job</Link>
            <Link href={null} class="btn btn-soft-success w-100">Overview</Link>
          </div>
        </CardBody>
      </Card>
    </Col>
  {/each}
</Row>
