<script>
	import {onMount} from 'svelte';
	import allseries from "../series";
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

	var chartLineAreaColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			toolbar: {
				show: !1,
			},
			type: "line",
			height: 350,
		},
		series: [
			{
				name: "TEAM A",
				type: "area",
				data: [44, 55, 31, 47, 31, 43, 26, 41, 31, 47, 33],
			},
			{
				name: "TEAM B",
				type: "line",
				data: [55, 69, 45, 61, 43, 54, 37, 52, 44, 61, 43],
			},
		],
		stroke: {
			curve: "smooth",
		},
		fill: {
			type: "solid",
			opacity: [0.35, 1],
		},
		labels: [
			"Dec 01",
			"Dec 02",
			"Dec 03",
			"Dec 04",
			"Dec 05",
			"Dec 06",
			"Dec 07",
			"Dec 08",
			"Dec 09 ",
			"Dec 10",
			"Dec 11",
		],
		markers: {
			size: 0,
		},
		yaxis: [
			{
				title: {
					text: "Series A",
				},
			},
			{
				opposite: !0,
				title: {
					text: "Series B",
				},
			},
		],
		tooltip: {
			shared: !0,
			intersect: !1,
			y: {
				formatter: function (y) {
					if (typeof y !== "undefined") {
						return y.toFixed(0) + " points";
					}
					return y;
				},
			},
		},
		colors: chartLineAreaColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#areamixedchart"), options)
  		chart.render()
	})
</script>

<div id="areamixedchart" class="apex-charts" dir="ltr"></div>
