<script>
    import {Card,CardBody,CardHeader,Col,DropdownItem,DropdownMenu,DropdownToggle,Dropdown,} from "sveltestrap";

	import {onMount} from 'svelte';
	export let dataColors;
	import { browser } from "$app/environment"

    function getChartColorsArray(colors) {
        if (browser) {
            return colors.map(function (value) {
                var newValue = value.replace(" ", "");
                if (newValue.indexOf(",") === -1) {
                    var color = getComputedStyle(
                        document.documentElement
                    ).getPropertyValue(newValue);
                    if (color.indexOf("#") !== -1)
                        color = color.replace(" ", "");
                    if (color) return color;
                    else return newValue;
                } else {
                    var val = value.split(",");
                    if (val.length === 2) {
                        var rgbaColor = getComputedStyle(
                            document.documentElement
                        ).getPropertyValue(val[0]);
                        rgbaColor = "rgba(" + rgbaColor + "," + val[1] + ")";
                        return rgbaColor;
                    } else {
                        return newValue;
                    }
                }
            });
        }
    }

    var revenueExpensesChartsColors = getChartColorsArray(dataColors);

    var series = [
        {
            name: "Application Sent  ",
            data: [33, 28, 30, 35, 40, 55, 70, 110, 150, 180, 210, 250],
        },
        {
            name: " Interviews",
            data: [20, 26, 45, 32, 42, 53, 59, 70, 78, 97, 110, 125],
        },
        {
            name: " Hired",
            data: [12, 17, 45, 42, 24, 35, 42, 75, 102, 108, 156, 199],
        },
        {
            name: " Rejected",
            data: [8, 13, 22, 27, 32, 34, 46, 59, 65, 97, 100, 110],
        },
    ];

    var options = {
        chart: {
            height: 320,
            type: "area",
            toolbar: "false",
        },
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 2,
        },
        xaxis: {
            categories: [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
        },
        series: series,
        colors: revenueExpensesChartsColors,
        fill: {
            opacity: 0.06,
            type: "solid",
        },
    };

    onMount(() => {
		const chart = new ApexCharts(document.querySelector("#jobsummary"), options)
  		chart.render()
	})

</script>

<Col xxl={8} md={6}>
    <Card class="card-height-100">
        <CardHeader class="align-items-center d-flex">
            <h4 class="card-title mb-0 flex-grow-1">Jobs Summary</h4>
            <div class="flex-shrink-0">
                <Dropdown class="card-header-dropdown">
                    <DropdownToggle
                        class="text-reset dropdown-btn p-0"
                        tag="a"
                        type="a"
                        href={null}
                        color=""
                    >
                        <span class="fw-semibold text-uppercase fs-12">
                            Sort by:{" "}
                        </span>
                        <span class="text-muted">
                            Current Year
                            <i class="mdi mdi-chevron-down ms-1" />
                        </span>
                    </DropdownToggle>
                    <DropdownMenu class="dropdown-menu-end">
                        <DropdownItem href={null}>Today</DropdownItem>
                        <DropdownItem href={null}>Last Week</DropdownItem>
                        <DropdownItem href={null}>Last Month</DropdownItem>
                        <DropdownItem href={null}>Current Year</DropdownItem>
                    </DropdownMenu>
                </Dropdown>
            </div>
        </CardHeader>
        <CardBody class="card-body px-0">
            <div id="jobsummary" class="apex-charts" dir="ltr"></div>
        </CardBody>
    </Card>
</Col>
