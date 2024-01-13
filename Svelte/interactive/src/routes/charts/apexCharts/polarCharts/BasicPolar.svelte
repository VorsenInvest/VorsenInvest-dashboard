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
	var chartPolarareaBasicColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: "polarArea",
			width: 400,
		},
		series: [14, 23, 21, 17, 15, 10, 12, 17, 21],
		labels: [
			"Series A",
			"Series B",
			"Series C",
			"Series D",
			"Series E",
			"Series F",
			"Series G",
			"Series H",
			"Series I",
		],
		stroke: {
			colors: ["#fff"],
		},
		fill: {
			opacity: 0.8,
		},

		legend: {
			position: "bottom",
		},
		colors: chartPolarareaBasicColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#basicploarchart"), options)
  		chart.render()
	})
</script>

<div id="basicploarchart" class="apex-charts" dir="ltr"></div>
