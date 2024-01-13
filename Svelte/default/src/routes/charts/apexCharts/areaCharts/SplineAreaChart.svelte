<script>
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

	var areachartSplineColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 350,
			type: "area",
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "series1",
				data: [31, 40, 28, 51, 42, 109, 100],
			},
			{
				name: "series2",
				data: [11, 32, 45, 32, 34, 52, 41],
			},
		],
		dataLabels: {
			enabled: false,
		},
		stroke: {
			curve: "smooth",
		},
		colors: areachartSplineColors,
		xaxis: {
			type: "datetime",
			categories: [
				"2018-09-19T00:00:00.000Z",
				"2018-09-19T01:30:00.000Z",
				"2018-09-19T02:30:00.000Z",
				"2018-09-19T03:30:00.000Z",
				"2018-09-19T04:30:00.000Z",
				"2018-09-19T05:30:00.000Z",
				"2018-09-19T06:30:00.000Z",
			],
		},
		tooltip: {
			x: {
				format: "dd/MM/yy HH:mm",
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#splineareachart"), options)
  		chart.render()
	})
</script>

<div id="splineareachart" class="apex-charts" dir="ltr"></div>
