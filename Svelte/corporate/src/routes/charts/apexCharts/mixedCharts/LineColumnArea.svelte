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

	var chartLineAreaMultiColors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			stacked: !1,
			toolbar: {
				show: !1,
			},
			type: "line",
			height: 350,
		},
		series: [
			{
				name: "TEAM A",
				type: "column",
				data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
			},
			{
				name: "TEAM B",
				type: "area",
				data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
			},
			{
				name: "TEAM C",
				type: "line",
				data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
			},
		],
		stroke: {
			width: [0, 2, 5],
			curve: "smooth",
		},
		plotOptions: {
			bar: {
				columnWidth: "50%",
			},
		},

		fill: {
			opacity: [0.85, 0.25, 1],
			gradient: {
				inverseColors: !1,
				shade: "light",
				type: "vertical",
				opacityFrom: 0.85,
				opacityTo: 0.55,
				stops: [0, 100, 100, 100],
			},
		},
		labels: [
			"01/01/2003",
			"02/01/2003",
			"03/01/2003",
			"04/01/2003",
			"05/01/2003",
			"06/01/2003",
			"07/01/2003",
			"08/01/2003",
			"09/01/2003",
			"10/01/2003",
			"11/01/2003",
		],
		markers: {
			size: 0,
		},
		xaxis: {
			type: "datetime",
		},
		yaxis: {
			title: {
				text: "Points",
			},
			min: 0,
		},
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
		colors: chartLineAreaMultiColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#linecolumnmixedchart"), options)
  		chart.render()
	})
</script>

<div id="linecolumnmixedchart" class="apex-charts" dir="ltr"></div>
