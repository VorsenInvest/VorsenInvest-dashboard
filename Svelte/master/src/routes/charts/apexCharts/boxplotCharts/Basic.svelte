<script>
	import {onMount} from 'svelte';
	import { browser } from "$app/environment"
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

	
	onMount(() => {
		var chartBoxBasicColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: "boxPlot",
			height: 350,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				type: "boxPlot",
				data: [
					{
						x: "Jan 2015",
						y: [54, 66, 69, 75, 88],
					},
					{
						x: "Jan 2016",
						y: [43, 65, 69, 76, 81],
					},
					{
						x: "Jan 2017",
						y: [31, 39, 45, 51, 59],
					},
					{
						x: "Jan 2018",
						y: [39, 46, 55, 65, 71],
					},
					{
						x: "Jan 2019",
						y: [29, 31, 35, 39, 44],
					},
					{
						x: "Jan 2020",
						y: [41, 49, 58, 61, 67],
					},
					{
						x: "Jan 2021",
						y: [54, 59, 66, 71, 88],
					},
				],
			},
		],
		title: {
			text: "Basic BoxPlot Chart",
			align: "left",
			style: {
				fontWeight: 500,
			},
		},
		plotOptions: {
			boxPlot: {
				colors: {
					upper: chartBoxBasicColors[0],
					lower: chartBoxBasicColors[1],
				},
			},
		},
	};
		const chart = new ApexCharts(document.querySelector("#barboxchart"), options)
  		chart.render()
	})
</script>

<div id="barboxchart" class="apex-charts" dir="ltr"></div>