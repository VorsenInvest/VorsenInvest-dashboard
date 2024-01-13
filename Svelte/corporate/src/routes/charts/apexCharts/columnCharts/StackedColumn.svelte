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

	var chartColumnStackedColors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			stacked: !0,
			toolbar: {
				show: !1,
			},
			type: "bar",
			height: 350,
			zoom: {
				enabled: !0,
			},
		},
		series: [
			{
				name: "PRODUCT A",
				data: [44, 55, 41, 67, 22, 43],
			},
			{
				name: "PRODUCT B",
				data: [13, 23, 20, 8, 13, 27],
			},
			{
				name: "PRODUCT C",
				data: [11, 17, 15, 15, 21, 14],
			},
			{
				name: "PRODUCT D",
				data: [21, 7, 25, 13, 22, 8],
			},
		],
		responsive: [
			{
				breakpoint: 480,
				options: {
					legend: {
						position: "bottom",
						offsetX: -10,
						offsetY: 0,
					},
				},
			},
		],
		plotOptions: {
			bar: {
				horizontal: !1,
				borderRadius: 10,
			},
		},
		xaxis: {
			type: "datetime",
			categories: [
				"01/01/2011 GMT",
				"01/02/2011 GMT",
				"01/03/2011 GMT",
				"01/04/2011 GMT",
				"01/05/2011 GMT",
				"01/06/2011 GMT",
			],
		},
		legend: {
			position: "right",
			offsetY: 40,
		},
		fill: {
			opacity: 1,
		},
		colors: chartColumnStackedColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#stackedcolumn"), options)
  		chart.render()
	})
</script>

<div id="stackedcolumn" class="apex-charts" dir="ltr"></div>
