<script>
    import { Card, CardBody, CardHeader, Col, Table } from "sveltestrap";
    import featuredCompany from "../../common/data/dashboardJobs";
    import Link from 'svelte-link';
</script>
<Col xl={6}>
    <Card class="card-height-100">
      <CardHeader class="align-items-center d-flex">
        <h4 class="card-title mb-0 flex-grow-1">Featured Companies</h4>
        <div class="flex-shrink-0">
          <Link href={null} class="btn btn-soft-primary btn-sm">
            View All Companies{" "}
            <i class="ri-arrow-right-line align-bottom"></i>
          </Link>
        </div>
      </CardHeader>

      <CardBody>
        <div class="table-responsive table-card">
          <Table class="table table-centered table-hover align-middle table-nowrap mb-0">
            <tbody>
                {#each featuredCompany.featuredCompany as company}
                    <tr>
                    <td>
                        <div class="d-flex align-items-center">
                        <div class="avatar-xs me-2 flex-shrink-0">
                            <div class={"avatar-title bg-" + company.bgColor + "-subtle rounded"}>
                            <img src={company.img} alt="" height="16" />
                            </div>
                        </div>
                        <h6 class="mb-0">{company.lable}</h6>
                        </div>
                    </td>
                    <td>
                        <i class="ri-map-pin-2-line text-primary me-1 align-bottom"></i>{" "}
                        {company.city}
                    </td>
                    <td>
                        <ul class="list-inline mb-0">
                        <li class="list-inline-item">
                            <Link href={null} class="link-secondary">
                            <i class="ri-facebook-fill"></i>
                            </Link>
                        </li>
                        <li class="list-inline-item">
                            <Link href={null} class="link-danger">
                            <i class="ri-mail-line"></i>
                            </Link>
                        </li>
                        <li class="list-inline-item">
                            <Link href={null} class="link-primary">
                            <i class="ri-global-line"></i>
                            </Link>
                        </li>
                        <li class="list-inline-item">
                            <Link href={null} class="link-info">
                            <i class="ri-twitter-line"></i>
                            </Link>
                        </li>
                        </ul>
                    </td>
                    <td>
                        <Link href={null} class="btn btn-link btn-sm">
                        View More{" "}
                        <i class="ri-arrow-right-line align-bottom"></i>
                        </Link>
                    </td>
                    </tr>
                {/each}
            </tbody>
          </Table>
        </div>
        <div class="align-items-center mt-4 pt-2 justify-content-between d-flex">
          <div class="flex-shrink-0">
            <div class="text-muted">
              Showing <span class="fw-semibold">5</span> of{" "}
              <span class="fw-semibold">25</span> Results
            </div>
          </div>
          <ul class="pagination pagination-separated pagination-sm mb-0">
            <li class="page-item disabled">
              <Link href={null} class="page-link">
                ←
              </Link>
            </li>
            <li class="page-item">
              <Link href={null} class="page-link">
                1
              </Link>
            </li>
            <li class="page-item active">
              <Link href={null} class="page-link">
                2
              </Link>
            </li>
            <li class="page-item">
              <Link href={null} class="page-link">
                3
              </Link>
            </li>
            <li class="page-item">
              <Link href={null} class="page-link">
                →
              </Link>
            </li>
          </ul>
        </div>
      </CardBody>
    </Card>
</Col>