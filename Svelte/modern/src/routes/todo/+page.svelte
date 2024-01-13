<script>
    import {
        Col,
        Container,
        DropdownItem,
        DropdownMenu,
        Input,
        Row,
        Dropdown,
        Collapse,
        Label,
    } from "sveltestrap";
    import Flatpickr from "svelte-flatpickr";
    import { createForm } from "svelte-forms-lib";
    import * as yup from "yup";
    import Link from "svelte-link";
    import { onMount } from "svelte";
    import dayjs from "dayjs";
    import { getTodos, addTodos } from "../../helpers/fakebackend_helper";
    import Modal from "../../Components/Common/Modal.svelte";

    import taskImg from "../../assets/images/task.png";
    // Import Images
    import avatar1 from "../../assets/images/users/avatar-1.jpg";
    import avatar2 from "../../assets/images/users/avatar-2.jpg";
    import avatar3 from "../../assets/images/users/avatar-3.jpg";
    import avatar4 from "../../assets/images/users/avatar-4.jpg";
    import avatar5 from "../../assets/images/users/avatar-5.jpg";
    import avatar6 from "../../assets/images/users/avatar-6.jpg";
    import avatar7 from "../../assets/images/users/avatar-7.jpg";
    import avatar8 from "../../assets/images/users/avatar-8.jpg";
    import avatar9 from "../../assets/images/users/avatar-9.jpg";
    import avatar10 from "../../assets/images/users/avatar-10.jpg";

    let droplist = false;
    let modalTodo = false;
    const toggle = () => (modalTodo = !modalTodo);
    let todo = [];
    let data = [];
    let tododata = [];

    const assigned = [
        { id: 1, img: avatar2, name: "James Forbes" },
        { id: 2, img: avatar3, name: "John Robles" },
    ];

    const assignee = [
        { id: 1, img: avatar2, name: "James Forbes" },
        { id: 2, img: avatar3, name: "John Robles" },
        { id: 3, img: avatar4, name: "Mary Gant" },
        { id: 4, img: avatar1, name: "Curtis Saenz" },
        { id: 5, img: avatar5, name: "Virgie Price" },
        { id: 6, img: avatar10, name: "Anthony Mills" },
        { id: 7, img: avatar6, name: "Marian Angel" },
        { id: 8, img: avatar7, name: "Johnnie Walton" },
        { id: 9, img: avatar8, name: "Donna Weston" },
        { id: 10, img: avatar9, name: "Diego Norris" },
    ];

    onMount(async () => {
        const res = await getTodos();
        tododata = res;
        data = tododata;
    });

    function handleValidDate(todaydate) {
        const datwe = dayjs(todaydate).format("DD MMM YYYY");
        return datwe;
    }

    const flipDurationMs = 300;
    function handleDndConsider(e) {
        items = e.detail.items;
    }
    function handleDndFinalize(e) {
        items = e.detail.items;
    }

    const { form, handleChange, handleSubmit, handleReset } = createForm({
        initialValues: {
            task: "",
            dueDate: "",
            status: "",
            priority: "",
        },
        validationSchema: yup.object().shape({
            task: yup.string().required("Please Enter Task"),
            priority: yup.string().required("Please Enter priority"),
            status: yup.string().required("Please Enter status"),
        }),
        onSubmit: (values) => {
            var newTodo = {
                id: (Math.floor(Math.random() * (30 - 20)) + 20).toString(),
                task: values.task,
                dueDate: date,
                status: values.status,
                priority: values.priority,
                subItem: assigned,
            };

            data = [...data, newTodo];
            handleReset();
            open = false;
        },
    });

    const taskStatus = (e) => {
        if (e) {
            data = data.filter((item) => item.status === e);
        } else {
            data = data.filter((item) => item.status !== e);
        }
    };

    const sortbystatus = [
        { label: "Completed", value: "Completed" },
        { label: "Inprogress", value: "Inprogress" },
        { label: "New", value: "New" },
        { label: "Pending", value: "Pending" },
    ];

    const sortbypriority = [
        { label: "High", value: "High" },
        { label: "Medium", value: "Medium" },
        { label: "Low", value: "Low" },
    ];
</script>

<svelte:head>
    <title>ToDo | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>
<div class="page-content">
    <Container fluid>
        <div class="chat-wrapper d-lg-flex gap-1 mx-n4 mt-n4 p-1">
            <div class="file-manager-sidebar">
                <div class="p-4 d-flex flex-column h-100">
                    <div class="mb-3">
                        <button class="btn btn-success w-100"
                            ><i class="ri-add-line align-bottom" /> Add Project</button
                        >
                    </div>

                    <div
                        class="px-4 mx-n4"
                        data-simplebar
                        style="height: calc(100vh - 468px);"
                    >
                        <ul
                            class="to-do-menu list-unstyled"
                            id="projectlist-data"
                        >
                            <li>
                                <Link
                                    href={null}
                                    class="nav-link fs-14 active"
                                    id="velzonAdmin"
                                    >Velzon Admin & Dashboard
                                </Link>

                                <Collapse toggler="#velzonAdmin" isOpen>
                                    <ul
                                        class="mb-0 sub-menu list-unstyled ps-3 vstack gap-2 mb-2"
                                    >
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-danger"
                                                /> v1.4.0
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-secondary"
                                                /> v1.5.0
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-info"
                                                />
                                                v1.6.0</Link
                                            >
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-primary"
                                                /> v1.7.0
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-warning"
                                                /> v1.8.0
                                            </Link>
                                        </li>
                                    </ul>
                                </Collapse>
                            </li>
                            <li>
                                <Link
                                    href={null}
                                    class="nav-link fs-14"
                                    id="projectManagement"
                                    >Project Management</Link
                                >
                                <Collapse toggler="#projectManagement">
                                    <ul
                                        class="mb-0 sub-menu list-unstyled ps-3 vstack gap-2 mb-2"
                                    >
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-danger"
                                                /> v2.1.0
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-secondary"
                                                /> v2.2.0
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-info"
                                                />
                                                v2.3.0</Link
                                            >
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-primary"
                                                /> v2.4.0
                                            </Link>
                                        </li>
                                    </ul>
                                </Collapse>
                            </li>
                            <li>
                                <Link
                                    href={null}
                                    class="nav-link fs-14"
                                    id="skoteAdmin"
                                    >Skote Admin & Dashboard</Link
                                >
                                <Collapse toggler="#skoteAdmin">
                                    <ul
                                        class="mb-0 sub-menu list-unstyled ps-3 vstack gap-2 mb-2"
                                    >
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-danger"
                                                /> v4.1.0
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-secondary"
                                                /> v4.2.0
                                            </Link>
                                        </li>
                                    </ul>
                                </Collapse>
                            </li>
                            <li>
                                <Link
                                    href={null}
                                    class="nav-link fs-14"
                                    id="ecommerceProject"
                                    >Doot - Chat App Template
                                </Link>
                                <Collapse toggler="#ecommerceProject">
                                    <ul
                                        class="mb-0 sub-menu list-unstyled ps-3 vstack gap-2 mb-2"
                                    >
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-danger"
                                                /> v1.0.0
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-secondary"
                                                /> v1.1.0
                                            </Link>
                                        </li>
                                        <li>
                                            <Link href={null}
                                                ><i
                                                    class="ri-stop-mini-fill align-middle fs-15 text-info"
                                                />
                                                v1.2.0</Link
                                            >
                                        </li>
                                    </ul>
                                </Collapse>
                            </li>
                        </ul>
                    </div>

                    <div class="mt-auto text-center">
                        <img src={taskImg} alt="Task" class="img-fluid" />
                    </div>
                </div>
            </div>
            <div class="file-manager-content w-100 p-4 pb-0">
                <div class="row mb-4">
                    <div class="col-auto order-1 d-block d-lg-none">
                        <button
                            type="button"
                            class="btn btn-soft-success btn-icon btn-sm fs-16 file-menu-btn"
                        >
                            <i class="ri-menu-2-fill align-bottom" />
                        </button>
                    </div>
                    <div class="col-sm order-3 order-sm-2 mt-3 mt-sm-0">
                        <h5 class="fw-semibold mb-0">
                            Velzon Admin & Dashboard <span
                                class="badge bg-primary align-bottom ms-2"
                                >v2.0.0</span
                            >
                        </h5>
                    </div>

                    <div class="col-auto order-2 order-sm-3 ms-auto">
                        <div class="hstack gap-2">
                            <div
                                class="btn-group"
                                role="group"
                                aria-label="Basic example"
                            >
                                <button
                                    class="btn btn-icon fw-semibold btn-soft-danger"
                                    ><i class="ri-arrow-go-back-line" /></button
                                >
                                <button
                                    class="btn btn-icon fw-semibold btn-soft-success"
                                    ><i
                                        class="ri-arrow-go-forward-line"
                                    /></button
                                >
                            </div>
                        </div>
                    </div>
                </div>
                <div class="p-3 bg-light rounded mb-4">
                    <Row class="g-2">
                        <Col class="col-lg-auto">
                            <select
                                class="form-control"
                                name="choices-select-sortlist"
                                id="choices-select-sortlist"
                            >
                                <option value="">Sort</option>
                                <option value="By ID">By ID</option>
                                <option value="By Name">By Name</option>
                            </select>
                        </Col>
                        <Col class="col-lg-auto">
                            <select
                                class="form-control"
                                name="choices-select-status"
                                id="choices-select-status"
                            >
                                <option value="">All Tasks</option>
                                <option value="Completed">Completed</option>
                                <option value="Inprogress">Inprogress</option>
                                <option value="Pending">Pending</option>
                                <option value="New">New</option>
                            </select>
                        </Col>
                        <Col class="col-lg">
                            <div class="search-box">
                                <input
                                    type="text"
                                    id="searchTaskList"
                                    class="form-control search"
                                    placeholder="Search task name"
                                />
                                <i class="ri-search-line search-icon" />
                            </div>
                        </Col>
                        <Col class="col-lg-auto">
                            <button
                                class="btn btn-primary createTask"
                                type="button"
                                on:click={toggle}
                            >
                                <i class="ri-add-fill align-bottom" /> Add Tasks
                            </button>
                        </Col>
                    </Row>
                </div>

                <div
                    class="todo-content position-relative px-4 mx-n4"
                    id="todo-content"
                >
                    {#if (data.length || []) > 0}
                        <div class="todo-task" id="todo-task">
                            <div class="table-responsive">
                                <table
                                    class="table align-middle position-relative table-nowrap table-nowrap"
                                >
                                    <thead class="table-active">
                                        <tr>
                                            <th scope="col">Task Name</th>
                                            <th scope="col">Assigned</th>
                                            <th scope="col">Due Date</th>
                                            <th scope="col">Status</th>
                                            <th scope="col">Priority</th>
                                            <th scope="col">Action</th>
                                        </tr>
                                    </thead>

                                    <tbody id="task-list">
                                        {#each data as item}
                                            <tr>
                                                <td>
                                                    <div
                                                        class="d-flex align-items-start"
                                                    >
                                                        <div
                                                            class="flex-shrink-0 me-3"
                                                        >
                                                            <div
                                                                class="task-handle px-1 bg-light rounded"
                                                            >
                                                                : :
                                                            </div>
                                                        </div>
                                                        <div
                                                            class="flex-grow-1"
                                                        >
                                                            <div
                                                                class="form-check"
                                                            >
                                                                <input
                                                                    class="form-check-input me-1"
                                                                    type="checkbox"
                                                                    value="13"
                                                                    id={"todo" +
                                                                        item.id}
                                                                    checked={item.status ===
                                                                    "Completed"
                                                                        ? "checked"
                                                                        : ""}
                                                                />
                                                                <Label
                                                                    class="form-check-label"
                                                                    for={"todo" +
                                                                        item.id}
                                                                    >{item.title}
                                                                </Label>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </td>
                                                <td>
                                                    <div class="avatar-group">
                                                        {#each item.assigned_to as assigned}
                                                            <Link
                                                                href={null}
                                                                class="avatar-group-item"
                                                            >
                                                                <img
                                                                    src={"https://api-node.themesbrand.website/images/users/" +
                                                                        assigned.profile}
                                                                    alt=""
                                                                    class="rounded-circle avatar-xxs"
                                                                />
                                                            </Link>
                                                        {/each}
                                                    </div>
                                                </td>
                                                <td
                                                    >{handleValidDate(
                                                        item.due_date
                                                    )}</td
                                                >
                                                <td>
                                                    {#if item.status == "New"}
                                                        <span
                                                            class="badge bg-info-subtle text-info text-uppercase"
                                                            >New</span
                                                        >
                                                    {:else if item.status == "Pending"}
                                                        <span
                                                            class="badge bg-warning-subtle text-warning text-uppercase"
                                                            >Pending</span
                                                        >
                                                    {:else if item.status == "Inprogress"}
                                                        <span
                                                            class="badge bg-secondary-subtle text-secondary text-uppercase"
                                                            >Inprogress</span
                                                        >
                                                    {:else if item.status == "Completed"}
                                                        <span
                                                            class="badge bg-success-subtle text-success text-uppercase"
                                                            >Completed</span
                                                        >
                                                    {:else}
                                                        <span
                                                            class="badge bg-success-subtle text-success text-uppercase"
                                                            >Completed</span
                                                        >
                                                    {/if}
                                                </td>
                                                <td>
                                                    {#if item.priority == "High"}
                                                        <span
                                                            class="badge bg-danger text-uppercase"
                                                            >High</span
                                                        >
                                                    {:else if item.priority == "Medium"}
                                                        <span
                                                            class="badge bg-warning text-uppercase"
                                                            >Medium</span
                                                        >
                                                    {:else if item.priority == "Low"}
                                                        <span
                                                            class="badge bg-success text-uppercase"
                                                            >Low</span
                                                        >
                                                    {:else}
                                                        <span
                                                            class="badge bg-success text-uppercase"
                                                            >Low</span
                                                        >
                                                    {/if}
                                                </td>
                                                <td>
                                                    <div class="hstack gap-2">
                                                        <button
                                                            class="btn btn-sm btn-soft-danger remove-list"
                                                        >
                                                            <i
                                                                class="ri-delete-bin-5-fill align-bottom"
                                                            />
                                                        </button>
                                                        <button
                                                            class="btn btn-sm btn-soft-info edit-list"
                                                        >
                                                            <i
                                                                class="ri-pencil-fill align-bottom"
                                                            />
                                                        </button>
                                                    </div>
                                                </td>
                                            </tr>
                                        {/each}
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    {:else}
                        <div
                            class="py-4 mt-4 text-center"
                            id="noresult"
                            style="display: none"
                        >
                            <lord-icon
                                src="https://cdn.lordicon.com/msoeawqm.json"
                                trigger="loop"
                                colors="primary:#405189,secondary:#0ab39c"
                                style="width: 72px; height: 72px"
                            />
                            <h5 class="mt-4">Sorry! No Result Found</h5>
                        </div>
                    {/if}
                </div>
            </div>
        </div>
    </Container>
</div>

<Modal isOpen={modalTodo} className="modal-dialog-centered">
    <div class="modal-header p-3 bg-success-subtle">
        <h5 class="modal-title" id="createFileModalLabel">Create Task</h5>
        <button type="button" class="btn-close" on:click={toggle} />
    </div>
    <div class="modal-body">
        <form id="creattask-form" on:submit|preventDefault={handleSubmit}>
            <div class="mb-3">
                <Label for="task-title-input" class="form-label"
                    >Task Title</Label
                >
                <input
                    type="text"
                    id="task-title-input"
                    class="form-control"
                    placeholder="Enter task title"
                    name="task"
                    on:change={handleChange}
                    on:blur={handleChange}
                    bind:value={$form.task}
                />
            </div>
            <div class="mb-3 position-relative">
                <Label for="task-assign-input" class="form-label"
                    >Assigned To</Label
                >

                <div
                    class="avatar-group justify-content-center"
                    id="assignee-member"
                />
                <div class="select-element">
                    <button
                        class="btn btn-light w-100 d-flex justify-content-between"
                        type="button"
                        on:click={() => (droplist = !droplist)}
                    >
                        <span
                            >Assigned To<b id="total-assignee" class="mx-1">0</b
                            >Members</span
                        > <i class="mdi mdi-chevron-down" />
                    </button>
                    <Dropdown>
                        <DropdownMenu class={droplist ? "w-100 show" : "w-100"}>
                            <div data-simplebar style="max-height: 141px">
                                <ul class="list-unstyled mb-0">
                                    {#each assignee as item}
                                        <li>
                                            <DropdownItem
                                                class="d-flex align-items-center"
                                                href={null}
                                            >
                                                <div
                                                    class="avatar-xxs flex-shrink-0 me-2"
                                                >
                                                    <img
                                                        src={item.img}
                                                        alt=""
                                                        class="img-fluid rounded-circle"
                                                    />
                                                </div>
                                                <div class="flex-grow-1">
                                                    {item.name}
                                                </div>
                                            </DropdownItem>
                                        </li>
                                    {/each}
                                </ul>
                            </div>
                        </DropdownMenu>
                    </Dropdown>
                </div>
            </div>
            <Row class="g-4 mb-3">
                <Col lg={6}>
                    <Label for="task-status" class="form-label">Status</Label>
                    <Input type="select" id="task-status" name="status" class="form-select"
                    on:blur={handleChange} bind:value={$form.status} 
                >
                {#each sortbystatus as item}
                <option value={item.value}>{item.label}</option>
                {/each}
                </Input>
                </Col>
                <Col lg={6}>
                    <Label
                        name="priority"
                        for="priority-field"
                        class="form-label">Priority</Label
                    >
                    <Input name="priority" id="priority-status" type="select" class="form-select"
                    on:blur={handleChange} bind:value={$form.priority} 
                >
                {#each sortbypriority as item}
                <option value={item.value}>{item.label}</option>
                {/each}
                </Input>
                </Col>
            </Row>

            <div class="mb-4">
                <Label for="task-duedate-input" class="form-label"
                    >Due Date:</Label
                >
                <Flatpickr
                    name="dueDate"
                    id="date-field"
                    class="form-control"
                    placeholder="Due date"
                    options={{
                        altInput: true,
                        altFormat: "d M, Y",
                        dateFormat: "d M, Y",
                    }}
                />
            </div>

            <div class="hstack gap-2 justify-content-end">
                <button
                    type="button"
                    class="btn btn-ghost-success"
                    on:click={toggle}
                    ><i class="ri-close-fill align-bottom" /> Close</button
                >
                <button type="submit" class="btn btn-primary" id="addNewTodo"
                    >Add Task</button
                >
            </div>
        </form>
    </div>
</Modal>
