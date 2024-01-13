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

	var chartNegativeBarColors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			type: "bar",
			height: 360,
			stacked: !0,
			toolbar: {
				show: !1,
			},
		},
		series: [
			{
				name: "Males",
				data: [
					0.4, 0.65, 0.76, 0.88, 1.5, 2.1, 2.9, 3.8, 3.9, 4.2, 4, 4.3,
					4.1, 4.2, 4.5, 3.9, 3.5, 3,
				],
			},
			{
				name: "Females",
				data: [
					-0.8, -1.05, -1.06, -1.18, -1.4, -2.2, -2.85, -3.7, -3.96,
					-4.22, -4.3, -4.4, -4.1, -4, -4.1, -3.4, -3.1, -2.8,
				],
			},
		],
		colors: chartNegativeBarColors,
		plotOptions: {
			bar: {
				horizontal: !0,
				barHeight: "80%",
			},
		},
		dataLabels: {
			enabled: !1,
		},
		stroke: {
			width: 1,
			colors: ["#fff"],
		},

		grid: {
			xaxis: {
				lines: {
					show: !1,
				},
			},
		},
		yaxis: {
			min: -5,
			max: 5,
			title: {
				text: "Age",
				style: {
					fontWeight: 600,
				},
			},
		},
		tooltip: {
			shared: !1,
			x: {
				formatter: function (val) {
					return val;
				},
			},
			y: {
				formatter: function (val) {
					return Math.abs(val) + "%";
				},
			},
		},
		title: {
			text: "Mauritius population pyramid 2011",
			style: {
				fontWeight: 600,
			},
		},
		xaxis: {
			categories: [
				"85+",
				"80-84",
				"75-79",
				"70-74",
				"65-69",
				"60-64",
				"55-59",
				"50-54",
				"45-49",
				"40-44",
				"35-39",
				"30-34",
				"25-29",
				"20-24",
				"15-19",
				"10-14",
				"5-9",
				"0-4",
			],
			title: {
				text: "Percent",
			},
			labels: {
				formatter: function (val) {
					return Math.abs(Math.round(val)) + "%";
				},
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#negativebarchart"), options)
  		chart.render()
	})
</script>

<div id="negativebarchart" class="apex-charts" dir="ltr"></div>
