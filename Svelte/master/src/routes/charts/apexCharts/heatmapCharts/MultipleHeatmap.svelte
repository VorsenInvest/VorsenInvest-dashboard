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

	var chartHeatMapMultipleColors = getChartColorsArray(dataColors);
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
				name: "W1",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W2",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W3",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W4",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W5",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W6",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W7",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W8",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W9",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W10",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W11",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W12",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W13",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W14",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
			{
				name: "W15",
				data: generateData(8, {
					min: 0,
					max: 90,
				}),
			},
		],
		dataLabels: {
			enabled: false,
		},
		colors: chartHeatMapMultipleColors,
		xaxis: {
			type: "category",
			categories: [
				"10:00",
				"10:30",
				"11:00",
				"11:30",
				"12:00",
				"12:30",
				"01:00",
				"01:30",
			],
		},
		title: {
			text: "HeatMap Chart (Different color shades for each series)",
			style: {
				fontWeight: 500,
			},
		},
		grid: {
			padding: {
				right: 20,
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#multipleheatmapchart"), options)
  		chart.render()
	})
</script>

<div id="multipleheatmapchart" class="apex-charts" dir="ltr"></div>
