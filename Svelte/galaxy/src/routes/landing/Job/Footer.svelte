<script>
    import { Col, Container, Row } from "sveltestrap";
    import LogoLight from "../../../assets/images/logo-light.png";
    import Link from 'svelte-link'
</script>
<footer class="custom-footer bg-dark py-5 position-relative">
    <Container>
      <Row>
        <Col class="col-lg-4 mt-4">
          <div>
            <div>
              <img src={LogoLight} alt="logo light" height="17" />
            </div>
            <div class="mt-4 fs-15">
              <p>Premium Multipurpose Admin & Dashboard Template</p>
              <p>
                You can build any type of web application like eCommerce,
                CRM, CMS, Project management apps, Admin Panels, etc using
                Velzon.
              </p>
              <ul class="list-inline mb-0 footer-social-link">
                <li class="list-inline-item">
                  <Link href={null} class="avatar-xs d-block">
                    <div class="avatar-title rounded-circle">
                      <i class="ri-facebook-fill"></i>
                    </div>
                  </Link>
                </li>
                <li class="list-inline-item">
                  <Link href={null} class="avatar-xs d-block">
                    <div class="avatar-title rounded-circle">
                      <i class="ri-github-fill"></i>
                    </div>
                  </Link>
                </li>
                <li class="list-inline-item">
                  <Link href={null} class="avatar-xs d-block">
                    <div class="avatar-title rounded-circle">
                      <i class="ri-linkedin-fill"></i>
                    </div>
                  </Link>
                </li>
                <li class="list-inline-item">
                  <Link href={null} class="avatar-xs d-block">
                    <div class="avatar-title rounded-circle">
                      <i class="ri-google-fill"></i>
                    </div>
                  </Link>
                </li>
                <li class="list-inline-item">
                  <Link href={null} class="avatar-xs d-block">
                    <div class="avatar-title rounded-circle">
                      <i class="ri-dribbble-line"></i>
                    </div>
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </Col>

        <Col class="col-lg-7 ms-lg-auto">
          <Row>
            <Col class="col-sm-4 mt-4">
              <h5 class="text-white mb-0">Company</h5>
              <div class="text-muted mt-3">
                <ul class="list-unstyled ff-secondary footer-list fs-16">
                  <li>
                    <Link href="/pages/profile/simple">About Us</Link>
                  </li>
                  <li>
                    <Link href="/pages/gallery/pages-gallery">Gallery</Link>
                  </li>
                  <li>
                    <Link href="/pages/team/team">Team</Link>
                  </li>
                  <li>
                    <Link href="/pages/pricing/pages-pricing">Pricing</Link>
                  </li>
                  <li>
                    <Link href="/pages/timeline/timeline">Timeline</Link>
                  </li>
                </ul>
              </div>
            </Col>
            <Col class="col-sm-4 mt-4">
              <h5 class="text-white mb-0">For Jobs</h5>
              <div class="text-muted mt-3">
                <ul class="list-unstyled ff-secondary footer-list fs-16">
                  <li>
                    <Link href="/Jobs/JobList/List">Job List</Link>
                  </li>
                  <li>
                    <Link href="/Jobs/Application">
                      application
                    </Link>
                  </li>
                  <li>
                    <Link href="/Jobs/NewJob">New Job</Link>
                  </li>
                  <li>
                    <Link href="/Jobs/CompaniesList">
                      Company List
                    </Link>
                  </li>
                </ul>
              </div>
            </Col>
            <Col class="col-sm-4 mt-4">
              <h5 class="text-white mb-0">Support</h5>
              <div class="text-muted mt-3">
                <ul class="list-unstyled ff-secondary footer-list fs-16">
                  <li>
                    <Link href="/pages/faqs">FAQ</Link>
                  </li>
                  <li>
                    <Link href="/pages/faqs">Contact</Link>
                  </li>
                </ul>
              </div>
            </Col>
          </Row>
        </Col>
      </Row>

      <Row class="text-center text-sm-start align-items-center mt-5">
        <Col class="col-sm-6">
          <div>
            <p class="copy-rights mb-0">
              {new Date().getFullYear()} ©
              Velzon - Themesbrand
            </p>
          </div>
        </Col>
        <Col class="col-sm-6">
          <div class="text-sm-end mt-3 mt-sm-0">
            <ul class="list-inline mb-0 footer-list gap-4 fs-15">
              <li class="list-inline-item">
                <Link href="/pages/privacypolicy">Privacy Policy</Link>
              </li>
              <li class="list-inline-item">
                <Link href="/pages-term-conditions">
                  Terms & Conditions
                </Link>
              </li>
              <li class="list-inline-item">
                <Link href="/pages-privacy-policy">Security</Link>
              </li>
            </ul>
          </div>
        </Col>
      </Row>
    </Container>
  </footer>