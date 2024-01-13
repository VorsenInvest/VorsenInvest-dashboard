<script>
  import { Card, CardBody, Col, Container, Input, Row } from "sveltestrap";
  import jobCandidates from "../../../../common/data/appsJobs";
  import BreadCrumb from "../../../../Components/Common/BreadCrumb.svelte";
  import Link from "svelte-link";
  var isBookmarkClick = false;
</script>

<svelte:head>
  <title
    >Candidates List View | Velzon - Svelte Admin & Dashboard Template</title
  >
</svelte:head>
<div class="page-content">
  <Container fluid>
    <BreadCrumb title="List View" pageTitle="Candidates Lists" />

    <Row class="g-4 mb-4">
      <Col class="col-sm-auto">
        <div>
          <Link href={null} class="btn btn-secondary">
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
              class="form-control"
              autoComplete="off"
              placeholder="Search for candidate name or designation..."
            />
            <i class="ri-search-line search-icon" />
          </div>

          <select class="form-control w-md">
            <option value="All">All</option>
            <option value="Today">Today</option>
            <option value="Yesterday" defaultValue> Yesterday </option>
            <option value="Last 7 Days">Last 7 Days</option>
            <option value="Last 30 Days">Last 30 Days</option>
            <option value="This Month">This Month</option>
            <option value="Last Year">Last Year</option>
          </select>
        </div>
      </Col>
    </Row>

    <Row class="gy-2 mb-2" id="candidate-list">
      {#each jobCandidates.jobCandidates as item}
        <Col md={6} lg={12}>
          <Card class="mb-0">
            <CardBody>
              <div class="d-lg-flex align-items-center">
                <div class="flex-shrink-0">
                  {#if item.nickname}
                    <div class="avatar-sm rounded">
                      <div
                        class="avatar-title border bg-light text-primary rounded text-uppercase fs-16"
                      >
                        {item.nickname}
                      </div>
                    </div>
                  {:else}
                    <div class="avatar-sm rounded">
                      <img
                        src={item.userImg}
                        alt=""
                        class="member-img img-fluid d-block rounded"
                      />
                    </div>
                  {/if}
                </div>
                <div class="ms-lg-3 my-3 my-lg-0">
                  <Link href="/pages-profile">
                    <h5 class="fs-16 mb-2">{item.candidateName}</h5>
                  </Link>
                  <p class="text-muted mb-0">{item.designation}</p>
                </div>
                <div class="d-flex gap-4 mt-0 text-muted mx-auto">
                  <div>
                    <i
                      class="ri-map-pin-2-line text-primary me-1 align-bottom"
                    />{" "}
                    {item.location}
                  </div>
                  <div>
                    <i
                      class="ri-time-line text-primary me-1 align-bottom"
                    />{" "}
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
                <div
                  class="d-flex flex-wrap gap-2 align-items-center mx-auto my-3 my-lg-0"
                >
                  <div class="badge text-bg-success">
                    <i class="mdi mdi-star me-1" />
                    {item.rating[0]}
                  </div>
                  <div class="text-muted">{item.rating[1]}</div>
                </div>
                <div>
                  <Link href={null} class="btn btn-soft-success">
                    View Details
                  </Link>
                  <Link
                    href={null}
                    on:click={(e) => {
                      e.preventDefault();
                      isBookmarkClick = !isBookmarkClick;
                    }}
                    class="active btn btn-ghost-danger btn-icon custom-toggle ">
                    <span class="icon-on">
                      <i class="ri-bookmark-line align-bottom" />
                    </span>

                    <span class="icon-off">
                      <i class="ri-bookmark-3-fill align-bottom" />
                    </span>
                  </Link>
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
            <Link href="" class="page-link" id="page-prev">Previous</Link>
          </div>
          <span id="page-num" class="pagination" />
          <div class="page-item">
            <Link href="" class="page-link" id="page-next">Next</Link>
          </div>
        </div>
      </Col>
    </Row>
  </Container>
</div>
