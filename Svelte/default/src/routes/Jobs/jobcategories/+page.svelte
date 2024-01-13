<svelte:head>
  <title>Job Categories | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<script>
    import {
  Card,
  CardBody,
  CardHeader,
  Col,
  Container,
  DropdownItem,
  DropdownMenu,
  DropdownToggle,
  Input,
  Row,
  Dropdown,
} from "sveltestrap";
import jobCategories from "../../../common/data/appsJobs";
import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
import Link from 'svelte-link'
</script>
<div class="page-content">
    <Container fluid class="container-fluid">
      <BreadCrumb title="Job Categories" pageTitle="Jobs" />
      <Row>
        <Col lg={12}>
          <Card>
            <CardHeader>
              <Row class="justify-content-between gy-3">
                <Col lg={3}>
                  <div class="search-box">
                    <Input
                      type="text"
                      class="form-control search"
                      placeholder="Search for job categories..."
                    />
                    <i class="ri-search-line search-icon"></i>
                  </div>
                </Col>
                <Col class="col-lg-auto">
                  <div class="d-md-flex text-nowrap gap-2">
                    <button
                      class="btn btn-info add-btn"
                      data-bs-toggle="modal"
                      data-bs-target="#showModal"
                    >
                      <i class="ri-add-fill me-1 align-bottom"></i> Add
                      Categories
                    </button>
                    <button class="btn btn-danger">
                      <i class="ri-filter-2-line me-1 align-bottom"></i>{" "}
                      Filters
                    </button>
                    <Dropdown>
                      <DropdownToggle
                        type="button"
                        role="button"
                        tag="button"
                        id="dropdownMenuLink1"
                        data-bs-toggle="dropdown"
                        aria-expanded="false"
                        class="btn btn-soft-info"
                      >
                        <i class="ri-more-2-fill"></i>
                      </DropdownToggle>
                      <DropdownMenu
                        class="dropdown-menu"
                        aria-labelledby="dropdownMenuLink1"
                      >
                        <li>
                          <DropdownItem class="dropdown-item" href={null}>
                            All
                          </DropdownItem>
                        </li>
                        <li>
                          <DropdownItem class="dropdown-item" href={null}>
                            Last Week
                          </DropdownItem>
                        </li>
                        <li>
                          <DropdownItem class="dropdown-item" href={null}>
                            Last Month
                          </DropdownItem>
                        </li>
                        <li>
                          <DropdownItem class="dropdown-item" href={null}>
                            Last Year
                          </DropdownItem>
                        </li>
                      </DropdownMenu>
                    </Dropdown>
                  </div>
                </Col>
              </Row>
            </CardHeader>
          </Card>
        </Col>
      </Row>

      <Row class="row-cols-xxl-5 row-cols-lg-3 row-cols-md-2 row-cols-1">
        {#each jobCategories.jobCategories as item}
            <Col>
                <Card>
                    <CardBody class="text-center py-4">
                        <lord-icon
                            src={item.icon}
                            trigger="hover"
                            colors="primary:#405189"
                            target="div"
                            style="width: 50px; height: 50px"></lord-icon>
                        <Link href={null} class="stretched-link">
                            <h5 class="mt-4">{item.lable}</h5>
                        </Link>
                        <p class="text-muted mb-0">{item.position}</p>
                    </CardBody>
                </Card>
            </Col>
        {/each}
      </Row>

      <Row>
        <Col lg={12}>
          <div class="text-center mb-3">
            <button
              class="btn btn-link text-info mt-2"
              id="loadmore"
            >
              <i class="mdi mdi-loading mdi-spin fs-20 align-middle me-2"></i>{" "}
              Load More{" "}
            </button>
          </div>
        </Col>
      </Row>
    </Container>
  </div>