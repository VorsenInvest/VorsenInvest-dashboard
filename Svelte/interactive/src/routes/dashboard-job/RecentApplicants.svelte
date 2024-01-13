<script>
  import { Card, CardBody, CardHeader, Col, Table } from "sveltestrap";
  import Link from 'svelte-link';
  import recentApplicants from "../../common/data/dashboardJobs";
</script>
<Col xxl={8}>
<Card>
  <CardHeader class="align-items-center d-flex">
    <h4 class="card-title mb-0 flex-grow-1">Recent Applicants</h4>
    <div class="flex-shrink-0">
      <button type="button" class="btn btn-soft-secondary btn-sm">
        <i class="ri-file-list-3-line align-bottom"></i> Generate
        Report
      </button>
    </div>
  </CardHeader>

  <CardBody>
    <div class="table-responsive table-card">
      <Table class="table table-borderless table-centered align-middle table-nowrap mb-0">
        <thead class="text-muted table-light">
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Candidate Name</th>
            <th scope="col">Designation</th>
            <th scope="col">Rate/hr</th>
            <th scope="col">Location</th>
            <th scope="col">Type</th>
            <th scope="col">Rating</th>
          </tr>
        </thead>
        <tbody>
          {#each recentApplicants.recentApplicants as item}
          <tr>
            <td>
              <Link href={null} class="fw-medium text-body">
              {item.no}
              </Link>
            </td>
            <td>
              <div class="d-flex align-items-center">
                <div class="flex-shrink-0 me-2">
                  <img src={item.img} alt="" class="avatar-xs rounded-circle" />
                </div>
                <div class="flex-grow-1">{item.name}</div>
              </div>
            </td>
            <td>{item.designation}</td>
            <td>
              <span class="text-success">{item.rate}</span>
            </td>
            <td>{item.city}</td>
            <td>
              <span class={"badge bg-" + item.typeColor + "-subtle text-" + item.typeColor}>
                {item.type}
              </span>
            </td>
            <td>
              <h5 class="fs-14 fw-medium mb-0">
                {item.rating}
                <span class="text-muted fs-12 ms-1">
                  {item.ratingDetails}
                </span>
              </h5>
            </td>
          </tr>
          {/each}
        </tbody>
      </Table>
    </div>
  </CardBody>
</Card>
</Col>