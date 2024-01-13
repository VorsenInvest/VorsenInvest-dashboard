<script>
  import { Card, CardBody, Col, Container, Input, Row } from "sveltestrap";
  import jobCandidates from "../../../../common/data/appsJobs";
  import BreadCrumb from "../../../../Components/Common/BreadCrumb.svelte";
  import Link from "svelte-link";
</script>

<svelte:head>
  <title
    >Candidates Grid View | Velzon - Svelte Admin & Dashboard Template</title
  >
</svelte:head>
<div class="page-content">
  <Container fluid class="container-fluid">
    <BreadCrumb title="Grid View" pageTitle="Candidates Grid" />

    <Row class="g-4 mb-4">
      <Col class="col-sm-auto">
        <div>
          <Link href={null} class="btn btn-success">
            <i class="ri-add-line align-bottom me-1" /> Add Candidate
          </Link>
        </div>
      </Col>
      <Col class="col-sm">
        <div class="d-md-flex justify-content-sm-end gap-2">
          <div class="search-box ms-md-2 flex-shrink-0 mb-3 mb-md-0">
            <Input
              type="text"
              id="searchJob"
              placeholder="Search for candidate name or designation..."
              autoComplete="off"
            />
            <i class="ri-search-line search-icon" />
          </div>

          <select
            class="form-control w-md"
            data-choices
            data-choices-search-false
          >
            <option value="All">All</option>
            <option value="Today">Today</option>
            <option value="Yesterday" defaultValue>Yesterday</option>
            <option value="Last 7 Days">Last 7 Days</option>
            <option value="Last 30 Days">Last 30 Days</option>
            <option value="This Month">This Month</option>
            <option value="Last Year">Last Year</option>
          </select>
        </div>
      </Col>
    </Row>

    <Row class="job-list-row" id="candidate-list">
      {#each jobCandidates.jobCandidates as item}
        <Col xxl={3} md={6}>
          <Card>
            <CardBody>
              <div class="d-flex align-items-center">
                <div class="flex-shrink-0">
                  {#if item.nickname}
                    <div class="avatar-lg rounded">
                      <div
                        class="avatar-title border bg-light text-primary rounded text-uppercase fs-24"
                      >
                        {item.nickname}
                      </div>
                    </div>
                  {:else}
                    <div class="avatar-lg rounded">
                      <img
                        src={item.userImg}
                        alt=""
                        class="member-img img-fluid d-block rounded"
                      />
                    </div>
                  {/if}
                </div>
                <div class="flex-grow-1 ms-3">
                  <a href="/pages/profile/simple">
                    <h5 class="fs-16 mb-1">{item.candidateName}</h5>
                  </a>
                  <p class="text-muted mb-2">{item.designation}</p>
                  <div class="d-flex flex-wrap gap-2 align-items-center">
                    <div class="badge text-bg-success">
                      <i class="mdi mdi-star me-1" />
                      {item.rating[0]}
                    </div>
                    <div class="text-muted">{item.rating[1]}</div>
                  </div>
                  <div class="d-flex gap-4 mt-2 text-muted">
                    <div>
                      <i
                        class="ri-map-pin-2-line text-primary me-1 align-bottom"
                      />{" "}
                      {item.location}
                    </div>
                    <div>
                      <i class="ri-time-line text-primary me-1 align-bottom" />
                      {#if item.type === "Part Time"}
                        <span class="badge bg-danger-subtle text-danger"
                          >{item.type}</span
                        >
                      {:else if item.type === "Full Time"}
                        <span class="badge bg-success-subtle text-success"
                          >{item.type}</span
                        >
                      {:else}
                        <span class="badge bg-info-subtle text-info"
                          >{item.type}</span
                        >
                      {/if}
                    </div>
                  </div>
                </div>
              </div>
            </CardBody>
          </Card>
        </Col>
      {/each}
    </Row>

    <Row class="g-0 justify-content-end mb-4" id="pagination-element">
      <Col sm={6}>
        <div
          class="pagination-block pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0"
        >
          <div class="page-item">
            <Link href="!#" class="page-link" id="page-prev">Previous</Link>
          </div>
          <span id="page-num" class="pagination" />
          <div class="page-item">
            <Link href="!#" class="page-link" id="page-next">Next</Link>
          </div>
        </div>
      </Col>
    </Row>
  </Container>
</div>
