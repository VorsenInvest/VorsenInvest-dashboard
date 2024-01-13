<script>
  import { onMount } from 'svelte';
  import { browser } from "$app/environment";
  import { Col, Card, CardBody, CardHeader, Row } from "sveltestrap";
  export let dataColors;
  import Counter from "../../Components/Common/CounterPage.svelte";
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

  var applicationsStatisticColors = getChartColorsArray(dataColors);

  const options = {
    chart: {
      height: 345,
      type: "line",
      zoom: {
        enabled: false,
      },
      toolbar: {
        show: false,
      },
    },
    series: [
      {
        name: "New Application",
        data: [89, 56, 74, 98, 72, 38, 64, 46, 84, 58, 46, 49],
      },
      {
        name: "Interview",
        data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10],
      },
      {
        name: " Hired",
        data: [36, 42, 60, 42, 13, 18, 29, 37, 36, 51, 32, 35],
      },
    ],
    colors: applicationsStatisticColors,

    dataLabels: {
      enabled: false,
    },
    stroke: {
      width: [3, 4, 3],
      curve: "straight",
      dashArray: [0, 8, 5],
    },
    series: [
      {
        name: "New Application",
        data: [89, 56, 74, 98, 72, 38, 64, 46, 84, 58, 46, 49],
      },
      {
        name: "Interview",
        data: [45, 52, 38, 24, 33, 26, 21, 20, 6, 8, 15, 10],
      },
      {
        name: " Hired",
        data: [36, 42, 60, 42, 13, 18, 29, 37, 36, 51, 32, 35],
      },
    ],
    markers: {
      size: 0,

      hover: {
        sizeOffset: 6,
      },
    },
    xaxis: {
      categories: [
        "01 Jan",
        "02 Jan",
        "03 Jan",
        "04 Jan",
        "05 Jan",
        "06 Jan",
        "07 Jan",
        "08 Jan",
        "09 Jan",
        "10 Jan",
        "11 Jan",
        "12 Jan",
      ],
    },
    grid: {
      borderColor: "#f1f1f1",
    },
  };

  onMount(() => {
    const chart = new ApexCharts(document.querySelector("#applicationStatistic"), options)
    chart.render()
  })

</script>
<Counter />
<Col xxl={8}>
<Card class="card-height-100">
  <CardHeader class="border-0 align-items-center d-flex">
    <h4 class="card-title mb-0 flex-grow-1">
      Applications Statistic
    </h4>
    <div>
      <button type="button" class="btn btn-soft-secondary btn-sm">
        ALL
      </button>
      <button type="button" class="btn btn-soft-secondary btn-sm">
        1M
      </button>
      <button type="button" class="btn btn-soft-secondary btn-sm">
        6M
      </button>
      <button type="button" class="btn btn-soft-primary btn-sm">
        1Y
      </button>
    </div>
  </CardHeader>

  <CardHeader class="p-0 border-0 bg-light-subtle">
    <Row class="g-0 text-center">
      <Col xs={6} sm={3}>
      <div class="p-3 border border-dashed border-start-0">
        <h5 class="mb-1">
          <span class="counter-value" data-target="3364">0</span>
        </h5>
        <p class="text-muted mb-0">New Applications</p>
      </div>
      </Col>
      <Col xs={6} sm={3}>
      <div class="p-3 border border-dashed border-start-0">
        <h5 class="mb-1">
          <span class="counter-value" data-target="2804">
          </span>
        </h5>
        <p class="text-muted mb-0">Interview</p>
      </div>
      </Col>
      <Col xs={6} sm={3}>
      <div class="p-3 border border-dashed border-start-0">
        <h5 class="mb-1">
          <span class="counter-value" data-target="2402">
          </span>
        </h5>
        <p class="text-muted mb-0">Hired</p>
      </div>
      </Col>
      <Col xs={6} sm={3}>
      <div class="p-3 border border-dashed border-start-0 border-end-0">
        <h5 class="mb-1 text-success">
          <span class="counter-value" data-target="8">
          </span>k
        </h5>
        <p class="text-muted mb-0">Total Applications</p>
      </div>
      </Col>
    </Row>
  </CardHeader>

  <CardBody class="p-0 pb-2">
    <div class="w-100">
      <div id={"applicationStatistic"} class="apex-charts" dir="ltr"></div>
    </div>
  </CardBody>
</Card>
</Col>