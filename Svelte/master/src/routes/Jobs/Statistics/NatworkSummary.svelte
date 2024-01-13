<script>
  import { onMount } from "svelte";
  import { browser } from "$app/environment";
  import {
    Card,
    CardHeader,
    Col,
    DropdownMenu,
    DropdownToggle,
    Dropdown,
    DropdownItem,
    CardBody,
  } from "sveltestrap";
  import { themeChangeEvent } from "$lib/eventBus";
  let chart;
  export let dataColors;

  function getChartColorsArray(colors) {
    if (browser) {
      return colors.map(function (value) {
        var newValue = value.replace(" ", "");
        if (newValue.indexOf(",") === -1) {
          var color = getComputedStyle(
            document.documentElement,
          ).getPropertyValue(newValue);
          if (color.indexOf("#") !== -1) color = color.replace(" ", "");
          if (color) return color;
          else return newValue;
        } else {
          var val = value.split(",");
          if (val.length === 2) {
            var rgbaColor = getComputedStyle(
              document.documentElement,
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

  var dealTypeChartsColors = getChartColorsArray(dataColors);

  const THEME_CHART_COLORS = {
		default: ["--vz-info", "--vz-secondary"],
		modern: ["--vz-info", "--vz-secondary"],
		minimal: ["--vz-info", "--vz-secondary"],
		creative: ["--vz-info", "--vz-secondary"],
		corporate: ["--vz-info", "--vz-secondary"],
		galaxy: ["--vz-info", "--vz-secondary"],
		classic: ["--vz-info", "--vz-secondary"],
		interactive: ["--vz-info", "--vz-secondary"],
		vintage: ["--vz-info", "--vz-secondary"],
		saas: ["--vz-info", "--vz-secondary"],
		material: ["--vz-info", "--vz-secondary"],
	};

	// Function to find the index of a key
	function findIndexByKey(key) {
		const keys = Object.keys(THEME_CHART_COLORS);
		return keys.indexOf(key);
	}

	// Subscribe to the theme change event
	const unsubscribeEvent = themeChangeEvent.subscribe((newTheme) => {
		// Handle the theme change event
		if(newTheme == null || newTheme == undefined){
			return;
		}
		let key = findIndexByKey(newTheme);
		let newColors;
		if (key >= 0) {
			newColors = THEME_CHART_COLORS[newTheme];
		}
		if (browser) {
			newColors = ( key >= 0) ? getChartColorsArray(newColors) : dataColors;
			setTimeout(() => {
				chart.updateOptions({
					colors: newColors,
				});
			}, 500);
		}
	});

  var options = {
    chart: {
      height: 341,
      type: "radar",
      dropShadow: {
        enabled: true,
        blur: 1,
        left: 1,
        top: 1,
      },
      toolbar: {
        show: false,
      },
    },
    series: [
      {
        name: "Following",
        data: [80, 50, 30, 40, 100, 20],
      },
      {
        name: "Followers",
        data: [20, 30, 40, 80, 20, 80],
      },
    ],
    stroke: {
      width: 2,
    },
    fill: {
      opacity: 0.2,
    },
    legend: {
      show: true,
      fontWeight: 500,
      offsetX: 0,
      offsetY: -8,
      markers: {
        width: 8,
        height: 8,
        radius: 6,
      },
      itemMargin: {
        horizontal: 10,
        vertical: 0,
      },
    },
    markers: {
      size: 0,
    },
    colors: dealTypeChartsColors,
    xaxis: {
      categories: ["2016", "2017", "2018", "2019", "2020", "2021"],
    },
  };

  onMount(() => {
    chart = new ApexCharts(
      document.querySelector("#networksummary"),
      options,
    );
    chart.render();
  });
</script>

<Col class="col-xxl-4 col-md-6">
  <Card class="card card-height-100">
    <CardHeader class="card-header align-items-center d-flex">
      <h4 class="card-title mb-0 flex-grow-1">Your Network Summary</h4>
      <div class="flex-shrink-0">
        <Dropdown class="card-header-dropdown">
          <DropdownToggle
            class="text-reset dropdown-btn p-0"
            tag="a"
            type="a"
            href={null}
            color=""
          >
            <span class="fw-bold text-uppercase fs-12">
              Sort by:{" "}
            </span>
            <span class="text-muted">
              Monthly<i class="mdi mdi-chevron-down ms-1"></i>
            </span>
          </DropdownToggle>
          <DropdownMenu class="dropdown-menu-end">
            <DropdownItem href={null}>Today</DropdownItem>
            <DropdownItem href={null}>Weekly</DropdownItem>
            <DropdownItem href={null}>Monthly</DropdownItem>
            <DropdownItem href={null}>Yearly</DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </div>
    </CardHeader>
    <CardBody class="pb-0">
      <div id="networksummary" class="apex-charts" dir="ltr"></div>
    </CardBody>
  </Card>
</Col>
