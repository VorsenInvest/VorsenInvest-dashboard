<script>
    import Kanban from "svelte-kanban";
    import BreadCrumb from "../../../Components/Common/BreadCrumb.svelte";
    import { Container, Row } from "sveltestrap";
</script>

<svelte:head>
    <title>kanban Board | Velzon - Svelte Admin & Dashboard Template</title>
</svelte:head>

<div class="page-content">
    <Container fluid>
        <BreadCrumb title="Kanban Board" pageTitle="Tasks" />
        <Row>
            <div class="kanbanboard" style="width:100%; height: 100%;">
                <Kanban
                    on:columnRemove
                    on:columnAdd
                    on:cardDragStart
                    on:cardDragMove
                    on:cardDragEnd
                    on:cardDragSuccess
                    on:cardDragFailed
                    on:cardAdd
                    on:cardPropSaved
                    on:cardPropModify
                    on:moveCardUp
                    on:moveCardDown
                    colsList={[
                        {
                            name: "New",
                            cards: [
                                {
                                    empty: false,
                                    title: "Me",
                                    description: "Me",
                                    date: "01/25/2021",
                                    category: {
                                        label: "New",
                                        bgColor: "gray",
                                        color: "white",
                                    },
                                },
                            ],
                        },
                        { name: "Done", cards: [] },
                    ]}
                    primary="#ff0000"
                    catsList={[
                        {
                            label: "important",
                            color: "#FFFFFF",
                            bgColor: "#EA0B38",
                        },
                        { label: "task", color: "black", bgColor: "#00F5DC" },
                    ]}
                />
            </div>
        </Row>
    </Container>
</div>
