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

	var chartRangeColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: "rangeBar",
			height: 335,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				data: [
					{
						x: "Team A",
						y: [1, 5],
					},
					{
						x: "Team B",
						y: [4, 6],
					},
					{
						x: "Team C",
						y: [5, 8],
					},
					{
						x: "Team D",
						y: [3, 11],
					},
				],
			},
			{
				data: [
					{
						x: "Team A",
						y: [2, 6],
					},
					{
						x: "Team B",
						y: [1, 3],
					},
					{
						x: "Team C",
						y: [7, 8],
					},
					{
						x: "Team D",
						y: [5, 9],
					},
				],
			},
		],
		plotOptions: {
			bar: {
				horizontal: !1,
			},
		},
		dataLabels: {
			enabled: !0,
		},
		legend: {
			show: !1,
		},
		colors: chartRangeColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#rabgecolumnchart"), options)
  		chart.render()
	})
</script>

<div id="rabgecolumnchart" class="apex-charts" dir="ltr"></div>
