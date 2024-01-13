<script>
    import { Card, CardBody, CardHeader, Col, Row } from "sveltestrap";
    import { html } from "gridjs";
    import Grid from "gridjs-svelte";
    import cryptoData from "../../../common/data/cryptoPage";

    const data = cryptoData.market;

    const columns = [
        {
            id: "coinName",
            hidden: true,
        },
        {
            name: "Currency",
            id: "img",
            sort:true,
            formatter: (cell, row) =>
                html(`<div class="d-flex align-items-center fw-medium">
                <img src=${cell} alt="" class="avatar-xxs me-2" />
                <a href={null} class="currency_name">${row.cells[0].data}</a>
            </div>`),
        },
        {
            name: "Price",
            id: "price",
            sort:true,
        },
        {
            name: "Pairs",
            id: "pairs",
            sort:true,
        },
        {
            name: "24 High",
            id: "high",
            sort:true,
        },
        {
            name: "24 Low",
            id: "low",
            sort:true,
        },
        {
            name: "Market Volume",
            id: "marketVolume",
            sort:true,
        },
        {
            id: "percentage",
            hidden: true,
        },
        {
            id: "icon",
            hidden: true,
        },
        {
            name: "Volume %",
            id: "iconClass",
            sort:true,
            formatter: (cell, row) =>
                html(`<h6 class="text-${cell} mb-0">
                    <i class="${row.cells[8].data} align-middle me-1"></i>
                    ${row.cells[7].data}
                </h6>`),
        },
        {
            name: "Action",
            formatter: (cell) =>
                html(
                    `<button class="btn btn-sm btn-soft-info">Trade Now</button>`
                ),
        },
    ];
</script>

<Card>
    <CardHeader class="border-bottom-dashed">
        <Row class="align-items-center">
            <Col xs={3}>
                <h5 class="card-title mb-0">Markets</h5>
            </Col>
            <div class="col-auto ms-auto">
                <div class="d-flex gap-2">
                    <button class="btn btn-success"
                        ><i class="ri-equalizer-line align-bottom me-1" /> Filters</button
                    >
                </div>
            </div>
        </Row>
    </CardHeader>
    <CardBody class="p-0 border-bottom border-bottom-dashed">
        <div class="search-box">
            <input
                type="text"
                class="form-control search border-0 py-3"
                placeholder="Search to currency..."
            />
            <i class="ri-search-line search-icon" />
        </div>
    </CardBody>
    <CardBody>
        <div class="table-card gridjs-border-none">
            <Grid
                {data}
                {columns}
                className={{ th: "text-muted" }}
                pagination={{ enabled: true, limit: 8 }}
            />
        </div>
    </CardBody>
</Card>
