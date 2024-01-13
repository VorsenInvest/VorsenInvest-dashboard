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

	var chartBoxBasicColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			toolbar: {
				show: !1,
			},
			type: "boxPlot",
			height: 350,
		},
		series: [
			{
				name: "Box",
				type: "boxPlot",
				data: [
					{
						x: new Date("2017-01-01").getTime(),
						y: [54, 66, 69, 75, 88],
					},
					{
						x: new Date("2018-01-01").getTime(),
						y: [43, 65, 69, 76, 81],
					},
					{
						x: new Date("2019-01-01").getTime(),
						y: [31, 39, 45, 51, 59],
					},
					{
						x: new Date("2020-01-01").getTime(),
						y: [39, 46, 55, 65, 71],
					},
					{
						x: new Date("2021-01-01").getTime(),
						y: [29, 31, 35, 39, 44],
					},
				],
			},
			{
				name: "Outliers",
				type: "scatter",
				data: [
					{
						x: new Date("2017-01-01").getTime(),
						y: 32,
					},
					{
						x: new Date("2018-01-01").getTime(),
						y: 25,
					},
					{
						x: new Date("2019-01-01").getTime(),
						y: 64,
					},
					{
						x: new Date("2020-01-01").getTime(),
						y: 27,
					},
					{
						x: new Date("2020-01-01").getTime(),
						y: 78,
					},
					{
						x: new Date("2021-01-01").getTime(),
						y: 15,
					},
				],
			},
		],
		colors: chartBoxBasicColors,
		title: {
			text: "BoxPlot - Scatter Chart",
			align: "left",
			style: {
				fontWeight: 500,
			},
		},
		xaxis: {
			type: "datetime",
			tooltip: {
				formatter: function (val) {
					return new Date(val).getFullYear();
				},
			},
		},
		plotOptions: {
			boxPlot: {
				colors: {
					upper: "#f06548",
					lower: "#405189",
				},
			},
		},
		tooltip: {
			shared: !1,
			intersect: !0,
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#scatterchart"), options)
  		chart.render()
	})
</script>

<div id="scatterchart" class="apex-charts" dir="ltr"></div>
