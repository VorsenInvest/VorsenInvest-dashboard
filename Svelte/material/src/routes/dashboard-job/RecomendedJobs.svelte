<script>
  import { onMount } from "svelte";
  import { Col, Card, CardBody, CardHeader, Row } from "sveltestrap";
  import Grid from "gridjs-svelte";
  let data = [
    ["Marketing Director", "Meta4Systems", "Vinninga, Sweden", "$250 - $800", "0-5 year", "Full Time"],
    ["UI/UX designer", "Zoetic Fashion", "Cullera, Spain", "$400+", "0-2 year", "Part Time"],
    ["Web Designer", "Force Medicines", "Ugashik, US", "$412 - $241 ", "3+ year", "Freelancer"],
    ["Full Stack Engineer", "Syntyce Solutions", "Zuweihir, UAE", "$650 - $900", "0-1+ year", "Full Time"],
    ["Assistant / Store Keeper", "Moetic Fashion", "Limestone, US", "$340 - $800", "0-3 year", "Intership"],
    ["Project Manager", "Themesbrand", "California, US", "$400 - $600", "3+ year", "Part Time"],
    ["Education Training", "Micro Design", "Germany", "$750 - $940", "1.5+ year", "Freelancer"],
    ["Graphic Designer", "Digitech Galaxy", "Mughairah, UAE", "$160 - $230", "2-3+ year", "Full Time"],
    ["React Developer", "iTest Factory", "Khabākhib, UAE", "$90 - $160", "5+ year", "Intership"],
    ["Executive, HR Operations", "Micro Design", "Texanna, US", "$50 - $120", "1-5 year", "Part Time"],
    ["Project Manager", "Meta4Systems", "Limestone, US", "$210 - $300", "0-2+ year", "Freelancer"],
    ["Full Stack Engineer", "Force Medicines", "Ugashik, US", "$120 - $180", "2-5 year", "Part Time"],
    ["Full Stack Engineer", "Digitech Galaxy", "Maidaq, UAE", "$900 - $1020", "3-5 year", "Full Time"],
    ["Marketing Director", "Zoetic Fashion", "Quesada, US", "$600 - $870", "0-5 year", "Freelancer"],
  ];
  const columns = ['Position', 'Company Name', 'Location', 'Salary', 'Experience', 'Job Type'];
  const sort = {
    multiColumn: true
  }
  const pagination = {
    limit: 6
  }

</script>
<style global>
  @import "https://cdn.jsdelivr.net/npm/gridjs/dist/theme/mermaid.min.css";
</style>

<Col lg={12}>
<Card>
  <CardHeader>
    <Row class="g-4 align-items-center">
      <Col class="col-sm-auto">
      <div>
        <h4 class="card-title mb-0 flex-grow-1">
          Recommended Jobs
        </h4>
      </div>
      </Col>
      <Col class="col-sm">
      <div class="d-flex justify-content-sm-end">
        <div class="search-box ms-2">
          <input type="text" class="form-control" id="searchResultList" placeholder="Search for jobs..." />
          <i class="ri-search-line search-icon">

          </i>
        </div>
      </div>
      </Col>
    </Row>
  </CardHeader>
  <CardBody>
    <Grid {data} {columns} {sort} {pagination}/>
  </CardBody>
</Card>
</Col>