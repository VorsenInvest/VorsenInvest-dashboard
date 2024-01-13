<script>
    import {onMount} from 'svelte';
    import { browser } from "$app/environment"
    import { Card, CardBody, CardHeader, Col, DropdownItem, DropdownMenu, DropdownToggle, Dropdown } from "sveltestrap";
	  export let dataColors;

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

    var chartTreemapDiffColor = getChartColorsArray(dataColors);
    var series = [
      {
        data: [
          {
            x: "USA",
            y: 321,
          },
          {
            x: "Russia",
            y: 165,
          },
          {
            x: "India",
            y: 184,
          },
          {
            x: "China",
            y: 98,
          },
          {
            x: "Canada",
            y: 84,
          },
          {
            x: "Brazil",
            y: 31,
          },
          {
            x: "UK",
            y: 70,
          },
          {
            x: "Australia",
            y: 30,
          },
          {
            x: "Germany",
            y: 44,
          },
          {
            x: "Italy",
            y: 68,
          },
          {
            x: "Israel",
            y: 28,
          },
          {
            x: "Indonesia",
            y: 19,
          },
          {
            x: "Bangladesh",
            y: 29,
          },
        ],
      },
    ];

    var options = {
      legend: {
        show: false,
      },
      chart: {
        height: 350,
        type: "treemap",
        toolbar: {
          show: false,
        },
      },
      series: series,
      title: {
        text: "Visitors Location",
        align: "center",
        style: {
          fontWeight: 500,
        },
      },
      colors: chartTreemapDiffColor,
      plotOptions: {
        treemap: {
          distributed: true,
          enableShades: false,
        },
      },
    };

  onMount(() => {
      const chart = new ApexCharts(document.querySelector("#visitorgraphchart"), options)
      chart.render();
  });

</script>
<Col class="col-xl-8">
    <Card class="card">
        <CardHeader class="card-header">
        <div class="d-flex">
            <h5 class="card-title mb-0 flex-grow-1">Visitor Graph</h5>
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
                    Current Week
                    <i class="mdi mdi-chevron-down ms-1"></i>
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
        </div>
        </CardHeader>
        <CardBody>
            <div id="visitorgraphchart" class="apex-charts" dir="ltr"></div>
        </CardBody>
    </Card>
</Col>