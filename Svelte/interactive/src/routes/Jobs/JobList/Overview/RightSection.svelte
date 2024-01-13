<script>
  import Link from "svelte-link";
  import { Card, CardBody, CardHeader, Table, Label } from "sveltestrap";
  import img3 from "../../../../assets/images/companies/img-3.png";
  var isBookmarkClick = false;
</script>

<Card class="card">
  <CardHeader class="card-header">
    <h5 class="mb-0">Job Overview</h5>
  </CardHeader>
  <CardBody class="card-body">
    <div class="table-responsive table-card">
      <Table class="table mb-0">
        <tbody>
          <tr>
            <td class="fw-medium">Title</td>
            <td>Product Designer</td>
          </tr>
          <tr>
            <td class="fw-medium">Company Name</td>
            <td>Themesbrand</td>
          </tr>
          <tr>
            <td class="fw-medium">Location</td>
            <td>Zuweihir, UAE</td>
          </tr>
          <tr>
            <td class="fw-medium">Time</td>
            <td>
              <span class="badge bg-success-subtle text-success">Full Time</span
              >
            </td>
          </tr>
          <tr>
            <td class="fw-medium">Job Application</td>
            <td>54 Application</td>
          </tr>
          <tr>
            <td class="fw-medium">Post Date</td>
            <td>15 Sep, 2021</td>
          </tr>
          <tr>
            <td class="fw-medium">Salary</td>
            <td>$35k - $45k</td>
          </tr>
          <tr>
            <td class="fw-medium">Experience</td>
            <td>5+ Years</td>
          </tr>
          <tr>
            <td class="fw-medium">Qualification</td>
            <td>Master Degree</td>
          </tr>
        </tbody>
      </Table>
    </div>
    <div class="mt-4 pt-2 hstack gap-2">
      <Link href={null} class="btn btn-primary w-100">Apply Now</Link>
      <Link
        href={null}
        on:click={() => (isBookmarkClick = !isBookmarkClick)}
        class={isBookmarkClick
          ? "btn btn-soft-danger btn-icon custom-toggle flex-shrink-0 active"
          : "btn btn-soft-danger btn-icon custom-toggle flex-shrink-0"}
      >
        {#if !isBookmarkClick}
          <span class="icon-on">
            <i class="ri-bookmark-line align-bottom" />
          </span>
        {:else}
          <span class="icon-off">
            <i class="ri-bookmark-3-fill align-bottom" />
          </span>
        {/if}
      </Link>
    </div>
  </CardBody>
</Card>

<Card class="card">
  <CardBody class="card-body">
    <div class="avatar-sm mx-auto">
      <div class="avatar-title bg-warning-subtle rounded">
        <img src={img3} alt="" class="avatar-xxs" />
      </div>
    </div>
    <div class="text-center">
      <Link href={null}>
        <h5 class="mt-3">Themesbrand</h5>
      </Link>
      <p class="text-muted">IT Department</p>
    </div>

    <div class="table-responsive">
      <Table class="table mb-0">
        <tbody>
          <tr>
            <td class="fw-medium">Company Size</td>
            <td>5</td>
          </tr>
          <tr>
            <td class="fw-medium">Industry Type</td>
            <td>Software</td>
          </tr>
          <tr>
            <td class="fw-medium">Founded in</td>
            <td>2016</td>
          </tr>
          <tr>
            <td class="fw-medium">Phone</td>
            <td>+(234) 12345 67890</td>
          </tr>
          <tr>
            <td class="fw-medium">Email</td>
            <td>themesbrand@gmail.com</td>
          </tr>
          <tr>
            <td class="fw-medium">Social media</td>
            <td>
              <ul class="list-inline mb-0">
                <li class="list-inline-item">
                  <Link href={null}>
                    <i class="ri-whatsapp-line" />
                  </Link>
                </li>
                <li class="list-inline-item">
                  <Link href={null}>
                    <i class="ri-facebook-line" />
                  </Link>
                </li>
                <li class="list-inline-item">
                  <Link href={null}>
                    <i class="ri-twitter-line" />
                  </Link>
                </li>
                <li class="list-inline-item">
                  <Link href={null}>
                    <i class="ri-youtube-line" />
                  </Link>
                </li>
              </ul>
            </td>
          </tr>
        </tbody>
      </Table>
    </div>
  </CardBody>
</Card>

<Card>
  <CardHeader class="card-header">
    <h5 class="mb-0">Job Location</h5>
  </CardHeader>
  <CardBody class="card-body">
    <div class="ratio ratio-4x3">
      <iframe
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1861227.8137337372!2d51.654904288504646!3d24.33915646928631!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5e48dfb1ab12bd%3A0x33d32f56c0080aa7!2sUnited%20Arab%20Emirates!5e0!3m2!1sen!2sin!4v1664257145153!5m2!1sen!2sin"
        height="450"
        style="border: 0"
        title="abc"
        allowFullScreen=""
        loading="lazy"
        referrerPolicy="no-referrer-when-downgrade"
      />
    </div>
  </CardBody>
</Card>

<Card>
  <CardHeader class="card-header">
    <h5 class="mb-0">Contact Us</h5>
  </CardHeader>
  <CardBody class="card-body">
    <form>
      <div class="mb-3">
        <Label htmlfor="nameInput" class="form-label">Name</Label>
        <input
          type="text"
          class="form-control"
          id="nameInput"
          placeholder="Enter your name"
        />
      </div>
      <div class="mb-3">
        <Label htmlfor="emailInput" class="form-label">Email</Label>
        <input
          type="text"
          class="form-control"
          id="emailInput"
          placeholder="Enter your email"
        />
      </div>
      <div class="mb-3">
        <Label htmlfor="messageInput" class="form-label">Message</Label>
        <textarea
          class="form-control"
          id="messageInput"
          rows="3"
          placeholder="Message"
        />
      </div>
      <div class="text-end">
        <button type="submit" class="btn btn-primary"> Send Message </button>
      </div>
    </form>
  </CardBody>
</Card>
