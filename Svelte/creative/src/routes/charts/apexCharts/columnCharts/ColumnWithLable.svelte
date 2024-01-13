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

	var chartColumnDatatalabelColors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			type: "bar",
			height: 350,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Inflation",
				data: [
					2.5, 3.2, 5.0, 10.1, 4.2, 3.8, 3, 2.4, 4.0, 1.2, 3.5, 0.8,
				],
			},
		],
		plotOptions: {
			bar: {
				dataLabels: {
					position: "top", // top, center, bottom
				},
			},
		},
		dataLabels: {
			enabled: true,
			formatter: function (val) {
				return val + "%";
			},
			offsetY: -20,
			style: {
				fontSize: "12px",
				colors: ["#adb5bd"],
			},
		},
		colors: chartColumnDatatalabelColors,
		grid: {
			borderColor: "#f1f1f1",
		},
		xaxis: {
			categories: [
				"Jan",
				"Feb",
				"Mar",
				"Apr",
				"May",
				"Jun",
				"Jul",
				"Aug",
				"Sep",
				"Oct",
				"Nov",
				"Dec",
			],
			position: "top",
			labels: {
				offsetY: -18,
			},
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false,
			},
			crosshairs: {
				fill: {
					type: "gradient",
					gradient: {
						colorFrom: "#D8E3F0",
						colorTo: "#BED1E6",
						stops: [0, 100],
						opacityFrom: 0.4,
						opacityTo: 0.5,
					},
				},
			},
			tooltip: {
				enabled: true,
				offsetY: -35,
			},
		},
		fill: {
			gradient: {
				shade: "light",
				type: "horizontal",
				shadeIntensity: 0.25,
				gradientToColors: undefined,
				inverseColors: true,
				opacityFrom: 1,
				opacityTo: 1,
				stops: [50, 0, 100, 100],
			},
		},
		yaxis: {
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false,
			},
			labels: {
				show: false,
				formatter: function (val) {
					return val + "%";
				},
			},
		},
		title: {
			text: "Monthly Inflation in Argentina, 2002",
			floating: true,
			offsetY: 320,
			align: "center",
			style: {
				color: "#444",
				fontWeight: 500,
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#columnwithlabel"), options)
  		chart.render()
	})
</script>

<div id="columnwithlabel" class="apex-charts" dir="ltr"></div>
