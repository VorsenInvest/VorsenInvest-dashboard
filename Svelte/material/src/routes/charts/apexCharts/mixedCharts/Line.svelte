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

	var chartLineColumnColors = getChartColorsArray(dataColors);
	const options = {
		chart: {
			toolbar: {
				show: !1,
			},
			type: "line",
			height: 350,
		},
		series: [
			{
				name: "Website Blog",
				type: "column",
				data: [
					440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160,
				],
			},
			{
				name: "Social Media",
				type: "line",
				data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16],
			},
		],
		stroke: {
			width: [0, 4],
		},
		title: {
			text: "Traffic Sources",
			style: {
				fontWeight: 600,
			},
		},
		dataLabels: {
			enabled: true,
			enabledOnSeries: [1],
		},
		labels: [
			"01 Jan 2001",
			"02 Jan 2001",
			"03 Jan 2001",
			"04 Jan 2001",
			"05 Jan 2001",
			"06 Jan 2001",
			"07 Jan 2001",
			"08 Jan 2001",
			"09 Jan 2001",
			"10 Jan 2001",
			"11 Jan 2001",
			"12 Jan 2001",
		],
		xaxis: {
			type: "datetime",
		},
		yaxis: [
			{
				title: {
					text: "Website Blog",
					style: {
						fontWeight: 600,
					},
				},
			},
			{
				opposite: true,
				title: {
					text: "Social Media",
					style: {
						fontWeight: 600,
					},
				},
			},
		],
		colors: chartLineColumnColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#linemixedchart"), options)
  		chart.render()
	})
</script>

<div id="linemixedchart" class="apex-charts" dir="ltr"></div>
