<script>
	import {onMount} from 'svelte';
	import { browser } from "$app/environment"

	export let dataColors;

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

	var chartBarReversedColors = getChartColorsArray(dataColors);

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
				data: [400, 430, 448, 470, 540, 580, 690],
			},
		],
		annotations: {
			xaxis: [
				{
					x: 500,
					borderColor: "#038edc",
					label: {
						borderColor: "#038edc",
						style: {
							color: "#fff",
							background: "#038edc",
						},
						text: "X annotation",
					},
				},
			],
			yaxis: [
				{
					y: "July",
					y2: "September",
					label: {
						text: "Y annotation",
					},
				},
			],
		},
		colors: chartBarReversedColors,
		plotOptions: {
			bar: {
				horizontal: true,
			},
		},
		dataLabels: {
			enabled: true,
		},
		xaxis: {
			categories: [
				"June",
				"July",
				"August",
				"September",
				"October",
				"November",
				"December",
			],
		},
		grid: {
			xaxis: {
				lines: {
					show: true,
				},
			},
		},
		yaxis: {
			reversed: true,
			axisTicks: {
				show: true,
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#reversedchart"), options)
  		chart.render()
	})
</script>

<div id="reversedchart" class="apex-charts" dir="ltr"></div>
