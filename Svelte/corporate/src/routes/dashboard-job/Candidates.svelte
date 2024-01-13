<script>
    import { Col, Card, CardBody, CardHeader, Row } from "sveltestrap";
    import Link from "svelte-link";
    import avtar10 from "../../assets/images/users/avatar-10.jpg";
    import avtar1 from "../../assets/images/users/avatar-1.jpg";
    import avtar9 from "../../assets/images/users/avatar-9.jpg";
    import avtar2 from "../../assets/images/users/avatar-2.jpg";
    import avtar5 from "../../assets/images/users/avatar-5.jpg";
    import avtar8 from "../../assets/images/users/avatar-8.jpg";

    const candidateList = [
        {
            id: 1,
            img: avtar10,
            name: "Tonya Noble",
            username: "@tonya",
            designation: "Web Developer",
        },
        {
            id: 2,
            img: avtar1,
            name: "Nicholas Ball",
            username: "@nicholas",
            designation: "Assistant / Store Keeper",
        },
        {
            id: 3,
            img: avtar9,
            name: "Zynthia Marrow",
            username: "@zynthia",
            designation: "Full Stack Engineer",
        },
        {
            id: 4,
            img: avtar2,
            name: "Cheryl Moore",
            username: "@cheryl",
            designation: "Product Designer",
        },
        {
            id: 5,
            img: avtar5,
            name: "Jennifer Bailey",
            username: "@jennifer",
            designation: "Marketing Director",
        },
        {
            id: 6,
            img: avtar8,
            name: "Hadley Leonard",
            username: "@hadley",
            designation: "Executive, HR Operations",
        },
    ];

    var isUpdateFollow = "";
    const handleChangeFollow = () => {
        isUpdateFollow = (current) => !current;
    };
</script>

<Col xxl={4}>
<Card>
    <CardHeader>
        <div class="d-flex align-items-center">
            <h6 class="card-title mb-0 flex-grow-1">Popular Candidates</h6>
            <div class="flex-shrink-0">
                <Link href="/Jobs/CandidateList/ListView" class="link-primary">
                View All <i class="ri-arrow-right-line" />
                </Link>
            </div>
        </div>
    </CardHeader>
    <Row class="g-0">
        <Col lg={6}>
        <CardBody class="border-end">
            <div class="search-box">
                <input type="text" class="form-control bg-light border-light" autoComplete="off" id="searchList"
                    placeholder="Search candidate..." />
                <i class="ri-search-line search-icon" />
            </div>
            <div data-simplebar style="max-height: 190px" class="px-3 mx-n3">
                <ul class="list-unstyled mb-0 pt-2" id="candidate-list">
                    {#each candidateList as item}
                    <li>
                        <Link href={null} class="d-flex align-items-center py-2">
                        <div class="flex-shrink-0 me-2">
                            <div class="avatar-xs">
                                <img src={item.img} alt="" class="img-fluid rounded-circle candidate-img" />
                            </div>
                        </div>
                        <div class="flex-grow-1">
                            <h5 class="fs-13 mb-1 text-truncate">
                                <span class="candidate-name">{item.name}</span>{" "}
                                <span class="text-muted fw-normal">{item.username}</span>
                            </h5>
                            <div class="d-none candidate-position">
                                {item.designation}
                            </div>
                        </div>
                        </Link>
                    </li>
                    {/each}
                </ul>
            </div>
        </CardBody>
        </Col>
        <Col lg={6}>
        <CardBody class="text-center">
            <div class="avatar-md mb-3 mx-auto">
                <img src={avtar10} alt="" id="candidate-img" class="img-thumbnail rounded-circle shadow-none" />
            </div>

            <h5 id="candidate-name" class="mb-0">Tonya Noble</h5>
            <p id="candidate-position" class="text-muted">
                Web Developer
            </p>

            <div class="d-flex gap-2 justify-content-center mb-3">
                <button type="button" class="btn avatar-xs p-0" data-bs-toggle="tooltip" data-bs-placement="top"
                    title="Google">
                    <span class="avatar-title rounded-circle bg-light text-body">
                        <i class="ri-google-line" />
                    </span>
                </button>

                <button type="button" class="btn avatar-xs p-0" data-bs-toggle="tooltip" data-bs-placement="top"
                    title="Linkedin">
                    <span class="avatar-title rounded-circle bg-light text-body">
                        <i class="ri-linkedin-line" />
                    </span>
                </button>
                <button type="button" class="btn avatar-xs p-0" data-bs-toggle="tooltip" data-bs-placement="top"
                    title="Dribbble">
                    <span class="avatar-title rounded-circle bg-light text-body">
                        <i class="ri-dribbble-fill" />
                    </span>
                </button>
            </div>

            <div>
                <button type="button" class={isUpdateFollow ? "btn btn-primary custom-toggle w-100 active"
                    : "btn btn-primary custom-toggle w-100" } on:click={handleChangeFollow}>
                    <span class="icon-on">
                        <i class="ri-add-line align-bottom me-1" /> Follow
                    </span>
                    <span class="icon-off">
                        <i class="ri-user-unfollow-line align-bottom me-1" />{" "}
                        Unfollow
                    </span>
                </button>
            </div>
        </CardBody>
        </Col>
    </Row>
</Card>
<Card class="overflow-hidden shadow-none">
    <CardBody class="bg-danger-subtle">
        <div class="d-flex align-items-center">
            <div class="flex-shrink-0">
                <div class="avatar-sm">
                    <div class="avatar-title bg-danger bg-opacity-10 text-danger rounded-circle fs-17">
                        <i class="ri-gift-line" />
                    </div>
                </div>
            </div>
            <div class="flex-grow-1 ms-3">
                <h6 class="fs-16">Invite your friends to Velzon</h6>
                <p class="text-muted mb-0">
                    Nor again is there anyone who loves or pursues or
                    desires to obtain pain of itself, because it is pain,
                    but because occasionally.
                </p>
            </div>
        </div>
        <div class="mt-3 text-end">
            <Link href={null} class="btn btn-danger">Invite Friends</Link>
        </div>
    </CardBody>
</Card>
</Col>