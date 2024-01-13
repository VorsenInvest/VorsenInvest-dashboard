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

	function generateData(count, yrange) {
		var i = 0;
		var series = [];
		while (i < count) {
			var x = (i + 1).toString();
			var y =
				Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
				yrange.min;

			series.push({
				x: x,
				y: y,
			});
			i++;
		}
		return series;
	}

	var chartHeatMapBasicColors = getChartColorsArray(dataColors);
	generateData();
	var options = {
		chart: {
			height: 450,
			type: "heatmap",
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Metric1",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "Metric2",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "Metric3",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "Metric4",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "Metric5",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "Metric6",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "Metric7",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "Metric8",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "Metric9",
				data: generateData(18, {
					min: 0,
					max: 90,
				}),
			},
		],
		dataLabels: {
			enabled: false,
		},
		colors: chartHeatMapBasicColors,
		title: {
			text: "HeatMap Chart (Single color)",
			style: {
				fontWeight: 500,
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#basicheatmapchart"), options)
  		chart.render()
	})
</script>

<div id="basicheatmapchart" class="apex-charts" dir="ltr"></div>
