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

	var chartDatalabelsBarColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: "bar",
			height: 350,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380],
			},
		],
		plotOptions: {
			bar: {
				barHeight: "100%",
				distributed: true,
				horizontal: true,
				dataLabels: {
					position: "bottom",
				},
			},
		},
		colors: chartDatalabelsBarColors,
		dataLabels: {
			enabled: true,
			textAnchor: "start",
			style: {
				colors: ["#fff"],
			},
			formatter: function (val, opt) {
				return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val;
			},
			offsetX: 0,
			dropShadow: {
				enabled: false,
			},
		},
		stroke: {
			width: 1,
			colors: ["#fff"],
		},
		xaxis: {
			categories: [
				"South Korea",
				"Canada",
				"United Kingdom",
				"Netherlands",
				"Italy",
				"France",
				"Japan",
				"United States",
				"China",
				"India",
			],
		},
		yaxis: {
			labels: {
				show: false,
			},
		},
		title: {
			text: "Custom DataLabels",
			align: "center",
			floating: true,
			style: {
				fontWeight: 500,
			},
		},
		subtitle: {
			text: "Category Names as DataLabels inside bars",
			align: "center",
		},
		tooltip: {
			theme: "dark",
			x: {
				show: false,
			},
			y: {
				title: {
					formatter: function () {
						return "";
					},
				},
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#customdatalabel"), options)
  		chart.render()
	})
</script>

<div id="customdatalabel" class="apex-charts" dir="ltr"></div>