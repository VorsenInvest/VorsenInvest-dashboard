<script>
  import BreadCrumb from "../../../../Components/Common/BreadCrumb.svelte";
  import { Card, CardBody, CardHeader, Col, Row } from "sveltestrap";
  import img10 from "../../../../assets/images/small/img-10.jpg";
  import img7 from "../../../../assets/images/companies/img-7.png";
  import img9 from "../../../../assets/images/small/img-9.jpg";
  import multiuser from "../../../../assets/images/users/multi-user.jpg";
  import AppSummaryChart from "./AppSummary.svelte";
  import Link from "svelte-link";
  const candidatelist = [
    {
      id: "1",
      name: "Tonya Noble",
      designation: "Web Designer",
      location: "Cullera, Spain",
      type: "Part Time",
      rating: "4.2",
      ratingCount: "2.2k",
      bookmark: "true",
    },
    {
      id: "2",
      name: "Nicholas Ball",
      designation: "Assistant / Store Keeper",
      location: "San Lorenzo",
      type: "Full Time",
      rating: "4.1",
      ratingCount: "1.72k",
      bookmark: "true",
    },
    {
      id: "3",
      name: "Zynthia Marrow",
      designation: "Assistant / Store Keeper",
      location: "Cullera, Spain",
      type: "Freelancer",
      rating: "4.0",
      ratingCount: "42.5k",
      bookmark: "false",
    },
    {
      id: "4",
      name: "Philippa Santiago",
      designation: "Project Manager ",
      location: "Ugashik, US",
      type: "Part Time",
      rating: "4.3",
      ratingCount: "15k",
      bookmark: "true",
    },
    {
      id: "5",
      name: "Elizabeth Allen",
      designation: "Education Training ",
      location: "Zuweihir, UAE",
      type: "Freelancer",
      rating: "3.5",
      ratingCount: "7.3k",
      bookmark: "false",
    },
    {
      id: "6",
      name: "Cassian Jenning",
      designation: "Graphic Designer ",
      location: "Limestone, US",
      type: "Part Time",
      rating: "4.3",
      ratingCount: "13.2k",
      bookmark: "false",
    },
    {
      id: "7",
      name: "Scott Holt",
      designation: "UI/UX Designer ",
      location: "Germany",
      type: "Part Time",
      rating: "3.5",
      ratingCount: "7.3k",
      bookmark: "false",
    },
    {
      id: "8",
      name: "Philbert Schwartz",
      designation: "React Developer ",
      location: "Zuweihir, UAE",
      type: "Full Time",
      rating: "4.1",
      ratingCount: "1.74k",
      bookmark: "true",
    },
    {
      id: "9",
      name: "Larry Villa",
      designation: "Assistant / Store Keeper",
      location: "San Lorenzo",
      type: "Full Time",
      rating: "4.0",
      ratingCount: "1.72k",
      bookmark: "false",
    },
    {
      id: "10",
      name: "Harley Watkins",
      designation: "Project Manager ",
      location: "Texanna, US",
      type: "Full Time",
      rating: "4.2",
      ratingCount: "3.21k",
      bookmark: "false",
    },
    {
      id: "11",
      name: "Marie Stewart",
      designation: "Web Designer",
      location: "Cullera, Spain",
      type: "Part Time",
      rating: "4.2",
      ratingCount: "2.2k",
      bookmark: "true",
    },
    {
      id: "12",
      name: "Hadley Leonard",
      designation: "Executive, HR Operations ",
      location: "Zuweihir, UAE",
      type: "Full Time",
      rating: "4.0",
      ratingCount: "3.2k",
      bookmark: "false",
    },
    {
      id: "13",
      name: "Zoderick Rodriquez",
      designation: "Full Stack Developer",
      location: "Muhtarqah, UAE",
      type: "Freelancer",
      rating: "3.9",
      ratingCount: "98.65k",
      bookmark: "false",
    },
    {
      id: "14",
      name: "Nadia Harding",
      designation: "Web Designer",
      location: "Pahoa, US",
      type: "Freelancer",
      rating: "4.3",
      ratingCount: "2.93k",
      bookmark: "true",
    },
    {
      id: "15",
      name: "Addison Black",
      designation: "UI/UX Designer",
      location: "Phoenix, Arizona",
      type: "Part Time",
      rating: "3.8",
      ratingCount: "10.32k",
      bookmark: "false",
    },
    {
      id: "16",
      name: "Priscilla Wise",
      designation: "Executive, HR Operations",
      location: "Ghurayfah, UAE",
      type: "Full Time",
      rating: "4.0",
      ratingCount: "7.36k",
      bookmark: "false",
    },
    {
      id: "17",
      name: "Lizzie Chandler",
      designation: "React Developer",
      location: "Maidaq, UAE",
      type: "Part Time",
      rating: "3.9",
      ratingCount: "1.35k",
      bookmark: "false",
    },
    {
      id: "18",
      name: "Jenson Carlson",
      designation: "Graphic Designer",
      location: "Quesada, US",
      type: "Freelancer",
      rating: "4.2",
      ratingCount: "3.16k",
      bookmark: "false",
    },
    {
      id: "19",
      name: "Jaylee Ward",
      designation: "Education Training",
      location: "Cullera, Spain",
      type: "Full Time",
      rating: "4.0",
      ratingCount: "3.21k",
      bookmark: "true",
    },
    {
      id: "20",
      name: "Trista Guerrero",
      designation: "Product Director",
      location: "Jereirah, UAE",
      type: "Full Time",
      rating: "4.1",
      ratingCount: "4.31k",
      bookmark: "false",
    },
    {
      id: "21",
      name: "James Stone",
      designation: "Graphic Designer",
      location: "Quesada, US",
      type: "Freelancer",
      rating: "4.2",
      ratingCount: "3.16k",
      bookmark: "false",
    },
    {
      id: "22",
      name: "Mike Watson",
      designation: "Product Director",
      location: "Jereirah, UAE",
      type: "Full Time",
      rating: "4.1",
      ratingCount: "4.13k",
      bookmark: "false",
    },
    {
      id: "23",
      name: "Mary Sak",
      designation: "Education Training",
      location: "Cullera, Spain",
      type: "Full Time",
      rating: "4.0",
      ratingCount: "3.21k",
      bookmark: "true",
    },
    {
      id: "24",
      name: "Roderick Jones",
      designation: "React Developer",
      location: "Maidaq, UAE",
      type: "Part Time",
      rating: "3.9",
      ratingCount: "1.35k",
      bookmark: "false",
    },
  ];
  import jobList from "../../../../common/data/appsJobs";
	import Modal from "../../../../Components/Common/Modal.svelte";

  let open = false;
	const toggle = () => (open = !open);
  var pages = [];
  var page = 1;
  var perPage = 8;

  var setPages = () => {
    let numberOfPages = Math.ceil(candidatelist.length / perPage);
    pages = [];
    for (let index = 1; index <= numberOfPages; index++) {
      pages.push(index);
    }
  };

  var paginate = (candidatelist) => {
    var page = page;
    var perPage = perPage;
    let from = page * perPage - perPage;
    let to = page * perPage;
    return candidatelist.slice(from, to);
  };

  setPages();
  paginate(candidatelist);
</script>

<svelte:head>
  <title>Job Lists | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
  <div class="container-fluid">
    <BreadCrumb title="Job Lists" pageTitle="Jobs" />

    <Row>
      <Col lg={12}>
        <Card>
          <CardBody class="bg-light-subtle">
            <div class="d-flex align-items-center">
              <h6 class="card-title mb-0 flex-grow-1 fw-bold">Search Jobs</h6>
              <div class="flex-shrink-0">
                <button
                  class="btn btn-secondary"
                  on:click={toggle}
                >
                  <i class="ri-add-line align-bottom me-1" />
                  Create New Job
                </button>
              </div>
            </div>

            <Row class="mt-3 gy-3">
              <Col xxl={10} md={6}>
                <div class="search-box">
                  <input
                    type="text"
                    class="form-control search bg-light border-light"
                    id="searchJob"
                    autoComplete="off"
                    placeholder="Search for jobs or companies..."
                  />
                  <i class="ri-search-line search-icon" />
                </div>
              </Col>
              <Col xxl={2} ms={6}>
                <div class="input-light">
                  <select
                    class="form-control"
                    data-choices
                    data-choices-search-false
                    name="choices-single-default"
                    id="idStatus"
                  >
                    <option value="All">All Selected</option>
                    <option value="Newest" defaultValue> Newest </option>
                    <option value="Popluar">Popluar</option>
                    <option value="Oldest">Oldest</option>
                  </select>
                </div>
              </Col>
              <Col class="col-xl-12 d-none" id="found-job-alert">
                <div class="alert alert-success mb-0 text-center" role="alert">
                  <strong id="total-result">253</strong> jobs found
                </div>
              </Col>
            </Row>
          </CardBody>
        </Card>
      </Col>
    </Row>

    <Row>
      <Col xxl={9}>
        <div id="job-list">
          {#each jobList.jobList as item}
            <Card class="joblist-card">
              <CardBody>
                <div class="d-flex mb-4">
                  <div class="avatar-sm">
                    <div class="avatar-title bg-light rounded">
                      <img
                        src={item.companyLogo}
                        alt=""
                        class="avatar-xxs companyLogo-img"
                      />
                    </div>
                  </div>
                  <div class="ms-3 flex-grow-1">
                    <img src={item.coverImg} alt="" class="d-none cover-img" />
                    <Link href={null}>
                      <h5 class="job-title">{item.jobTitle}</h5>
                    </Link>
                    <p class="company-name text-muted mb-0">
                      {item.companyName}
                    </p>
                  </div>
                  <div>
                    <button
                      type="button"
                      class="btn btn-ghost-primary btn-icon custom-toggle"
                      data-bs-toggle="button"
                    >
                      <span class="icon-on">
                        <i class="ri-bookmark-line" />
                      </span>
                      <span class="icon-off">
                        <i class="ri-bookmark-fill" />
                      </span>
                    </button>
                  </div>
                </div>
                <p class="text-muted job-description">
                  {item.description}
                </p>
                <div>
                  {#each item.tags as subItem}
                    <span class="badge bg-primary-subtle text-primary me-1"
                      >{subItem}</span
                    >
                  {/each}
                </div>
              </CardBody>
              <CardHeader class="card-footer border-top-dashed">
                <div
                  class="d-flex justify-content-between align-items-center flex-wrap gap-3"
                >
                  <div>
                    <i class="ri-briefcase-2-line align-bottom me-1" />{" "}
                    <span class="job-type">{item.type}</span>
                  </div>
                  <div class="d-none">
                    <span class="job-experience">
                      {item.experience}
                    </span>
                  </div>
                  <div>
                    <i class="ri-map-pin-2-line align-bottom me-1" />{" "}
                    <span class="job-location">{item.location}</span>
                  </div>
                  <div>
                    <i class="ri-user-3-line align-bottom me-1" />
                    {item.applied}
                  </div>
                  <div>
                    <i class="ri-time-line align-bottom me-1" />{" "}
                    <span class="job-postdate">{item.postDate}</span>
                  </div>
                  <div>
                    <Link href={null} class="btn btn-primary viewjob-list">
                      View More{" "}
                      <i class="ri-arrow-right-line align-bottom ms-1" />
                    </Link>
                  </div>
                </div>
              </CardHeader>
            </Card>
          {/each}
        </div>

        <Row class="g-0 justify-content-end mb-4" id="pagination-element">
          <Col sm={6}>
            {#if pages.length < 1}
              <div
                class="pagination-block pagination pagination-separated justify-content-center justify-content-sm-end mb-sm-0"
              >
                <div class="page-item">
                  <Link href="" class="page-link" id="page-prev">Previous</Link>
                </div>
                <span id="page-num" class="pagination">
                  {#each pages as pagenumber}
                    <div class="page-item active">
                      <a
                        class="page-link clickPageNumber"
                        href="!#"
                        target="_self"
                        onClick={(page = pagenumber)}>{pagenumber}</a
                      >
                    </div>
                  {/each}
                </span>
                <div class="page-item">
                  <Link
                    href=""
                    class="page-link"
                    id="page-next"
                    onClick={() => page++}
                  >
                    Next
                  </Link>
                </div>
              </div>
            {/if}

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
      </Col>
      <Col xxl={3}>
        <Card class="job-list-view-card overflow-hidden" id="job-overview">
          <img
            src={img10}
            alt=""
            id="cover-img"
            class="img-fluid background object-fit-cover"
          />
          <CardBody class="card-body">
            <div class="avatar-md mt-n5">
              <div class="avatar-title bg-light rounded-circle">
                <img src={img7} alt="" class="avatar-xs view-companylogo" />
              </div>
            </div>
            <div class="mt-3">
              <h5 class="view-title fs-18">Product Designer</h5>
              <div class="hstack gap-3 mb-3">
                <span class="text-muted">
                  <i class="ri-building-line me-1 align-bottom" />{" "}
                  <span class="view-companyname">Themesbrand</span>
                </span>
                <span class="text-muted">
                  <i class="ri-map-pin-2-line me-1 align-bottom" />{" "}
                  <span class="view-location">United Kingdom</span>
                </span>
              </div>
              <p class="text-muted view-desc">
                A UI/UX designer's job is to create user-friendly interfaces
                that enable users to understand how to use complex technical
                products. If you're passionate about the latest technology
                trends and devices, you'll find great fulfillment in being
                involved in the design process for the next hot gadget.
              </p>
              <div
                class="py-3 border border-dashed border-start-0 border-end-0 mt-4"
              >
                <Row>
                  <Col lg={4} sm={6}>
                    <div>
                      <p class="mb-2 text-uppercase fw-medium fs-12 text-muted">
                        Job Type
                      </p>
                      <h5 class="fs-14 mb-0 view-type">Full Time</h5>
                    </div>
                  </Col>
                  <Col lg={4} sm={6}>
                    <div>
                      <p class="mb-2 text-uppercase fw-medium fs-12 text-muted">
                        Post Date
                      </p>
                      <h5 class="fs-14 mb-0 view-postdate">15 Sep, 2022</h5>
                    </div>
                  </Col>
                  <Col lg={4} sm={6}>
                    <div>
                      <p class="mb-2 text-uppercase fw-medium fs-12 text-muted">
                        Experience
                      </p>
                      <h5 class="fs-14 mb-0 view-experience">0 - 5 Year</h5>
                    </div>
                  </Col>
                </Row>
              </div>
            </div>

            <div class="mt-4">
              <h5 class="mb-3">Application Summary</h5>
              <div>
                <AppSummaryChart
                  dataColors={[
                    "--vz-secondary",
                    "--vz-success",
                    "--vz-danger",
                  ]}
                />
              </div>
            </div>
            <div class="mt-4">
              <button type="button" class="btn btn-soft-primary w-100">
                Apply Now
              </button>
            </div>
          </CardBody>
        </Card>
      </Col>
    </Row>
  </div>
</div>

<Modal isOpen={open} className="modal-dialog-centered modal-lg">
 
  <form id="createjob-form" autocomplete="off" class="needs-validation" novalidate>
    <div class="modal-body">
        <input type="hidden" id="id-field" />
        <Row class="g-3">
            <Col lg={12}>
                <div class="px-1 pt-1">
                    <div class="modal-team-cover position-relative mb-0 mt-n4 mx-n4 rounded-top overflow-hidden">
                        <img src={img9} alt="" id="modal-cover-img" class="img-fluid">

                        <div class="d-flex position-absolute start-0 end-0 top-0 p-3">
                            <div class="flex-grow-1">
                                <h5 class="modal-title text-white" id="exampleModalLabel">Create New Job</h5>
                            </div>
                            <div class="flex-shrink-0">
                                <div class="d-flex gap-3 align-items-center">
                                    <div>
                                        <label for="cover-image-input" class="mb-0" data-bs-toggle="tooltip" data-bs-placement="top" title="Select Cover Image">
                                            <div class="avatar-xs">
                                                <div class="avatar-title bg-light border rounded-circle text-muted cursor-pointer">
                                                    <i class="ri-image-fill"></i>
                                                </div>
                                            </div>
                                        </label>
                                        <input class="form-control d-none" value="" id="cover-image-input" type="file" accept="image/png, image/gif, image/jpeg">
                                    </div>
                                    <button type="button" class="btn-close btn-close-white"  id="close-jobListModal" on:click={toggle}></button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="text-center mb-4 mt-n5 pt-2">
                    <div class="position-relative d-inline-block">
                        <div class="position-absolute bottom-0 end-0">
                            <label for="companylogo-image-input" class="mb-0" data-bs-toggle="tooltip" data-bs-placement="right" title="Select Image">
                                <div class="avatar-xs cursor-pointer">
                                    <div class="avatar-title bg-light border rounded-circle text-muted">
                                        <i class="ri-image-fill"></i>
                                    </div>
                                </div>
                            </label>
                            <input class="form-control d-none" value="" id="companylogo-image-input" type="file" accept="image/png, image/gif, image/jpeg">
                        </div>
                        <div class="avatar-lg p-1">
                            <div class="avatar-title bg-light rounded-circle">
                                <img src={multiuser} alt="" id="companylogo-img" class="avatar-md rounded-circle object-fit-cover" />
                            </div>
                        </div>
                    </div>
                    <h5 class="fs-13 mt-3">Company Logo</h5>
                </div>
                <div>
                    <label for="jobtitle-field" class="form-label">Job Title</label>
                    <input type="text" id="jobtitle-field" class="form-control" placeholder="Enter job title" required />
                    <div class="invalid-feedback">Please enter a job title.</div>
                </div>
              </Col>
            <Col lg={6}>
                <div>
                    <label for="companyname-field" class="form-label">Company Name</label>
                    <input type="text" id="companyname-field" class="form-control" placeholder="Enter company name" required />
                    <div class="invalid-feedback">Please enter a company name.</div>
                </div>
              </Col>
            <Col lg={6}>
                <div>
                    <label for="job_type-field" class="form-label">Job Type</label>
                    <select class="form-select" id="job_type-field" required>
                        <option value="Full Time">Full Time</option>
                        <option value="Part Time">Part Time</option>
                        <option value="Freelance">Freelance</option>
                        <option value="Internship">Internship</option>
                    </select>
                    <div class="invalid-feedback">Please select a job type.</div>
                </div>
              </Col>
            <Col lg={4}>
                <div>
                    <label for="experience-field" class="form-label">Experience</label>
                    <input type="text" id="experience-field" class="form-control" placeholder="Enter experience" required />
                    <div class="invalid-feedback">Please enter a job experience.</div>
                </div>
              </Col>
            <Col lg={4}>
                <div>
                    <label for="location-field" class="form-label">Location</label>
                    <input type="text" id="location-field" class="form-control" placeholder="Enter location" required />
                    <div class="invalid-feedback">Please enter a location.</div>
                </div>
              </Col>
            <Col lg={4}>
                <div>
                    <label for="Salary-field" class="form-label">Salary</label>
                    <input type="number" id="Salary-field" class="form-control" placeholder="Enter salary" />
                </div>
              </Col>
            <Col lg={12}>
                <div>
                    <label for="website-field" class="form-label">Tags</label>
                    <input class="form-control" id="taginput-choices" data-choices data-choices-text-unique-true type="text" value="Design, Remote" />
                </div>
              </Col>
            <Col lg={12}>
                <div>
                    <label for="description-field" class="form-label">Description</label>
                    <textarea class="form-control" id="description-field" rows="3" placeholder="Enter description" required></textarea>
                    <div class="invalid-feedback">Please enter a description.</div>
                </div>
              </Col>
            </Row>
    </div>
    <div class="modal-footer">
        <div class="hstack gap-2 justify-content-end">
            <button type="button" class="btn btn-light" on:click={toggle}>Close</button>
            <button type="submit" class="btn btn-success" id="add-btn">Add Job</button>
        </div>
    </div>
</form>

</Modal>