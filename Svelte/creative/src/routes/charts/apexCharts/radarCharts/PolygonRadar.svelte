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

	var chartRadarPolyradarColors = getChartColorsArray(dataColors);
	var options = {
		chart: {
			height: 350,
			type: "radar",
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Series 1",
				data: [20, 100, 40, 30, 50, 80, 33],
			},
		],
		dataLabels: {
			enabled: true,
		},
		plotOptions: {
			radar: {
				size: 140,
			},
		},
		title: {
			text: "Radar with Polygon Fill",
			style: {
				fontWeight: 500,
			},
		},
		colors: chartRadarPolyradarColors,
		markers: {
			size: 4,
			colors: ["#fff"],
			strokeColor: "#f34e4e",
			strokeWidth: 2,
		},
		tooltip: {
			y: {
				formatter: function (val) {
					return val;
				},
			},
		},
		xaxis: {
			categories: [
				"Sunday",
				"Monday",
				"Tuesday",
				"Wednesday",
				"Thursday",
				"Friday",
				"Saturday",
			],
		},
		yaxis: {
			tickAmount: 7,
			labels: {
				formatter: function (val, i) {
					if (i % 2 === 0) {
						return val;
					} else {
						return "";
					}
				},
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#polygonradarchart"), options)
  		chart.render()
	})
</script>

<div id="polygonradarchart" class="apex-charts" dir="ltr"></div>
