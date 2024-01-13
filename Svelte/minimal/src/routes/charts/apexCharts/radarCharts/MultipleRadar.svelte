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

	var chartRadarMultiColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 350,
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
				name: "Series 1",
				data: [80, 50, 30, 40, 100, 20],
			},
			{
				name: "Series 2",
				data: [20, 30, 40, 80, 20, 80],
			},
			{
				name: "Series 3",
				data: [44, 76, 78, 13, 43, 10],
			},
		],
		stroke: {
			width: 2,
		},
		fill: {
			opacity: 0.2,
		},
		markers: {
			size: 0,
		},
		colors: chartRadarMultiColors,
		xaxis: {
			categories: ["2014", "2015", "2016", "2017", "2018", "2019"],
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#multiradar"), options)
  		chart.render()
	})
</script>

<div id="multiradar" class="apex-charts" dir="ltr"></div>
