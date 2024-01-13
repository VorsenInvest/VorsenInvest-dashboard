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

	var chartColumnColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 350,
			type: "bar",
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Net Profit",
				data: [46, 57, 59, 54, 62, 58, 64, 60, 66],
			},
			{
				name: "Revenue",
				data: [74, 83, 102, 97, 86, 106, 93, 114, 94],
			},
			{
				name: "Free Cash Flow",
				data: [37, 42, 38, 26, 47, 50, 54, 55, 43],
			},
		],
		plotOptions: {
			bar: {
				horizontal: false,
				columnWidth: "45%",
				endingShape: "rounded",
			},
		},
		dataLabels: {
			enabled: false,
		},
		stroke: {
			show: true,
			width: 2,
			colors: ["transparent"],
		},
		colors: chartColumnColors,
		xaxis: {
			categories: [
				"Feb",
				"Mar",
				"Apr",
				"May",
				"Jun",
				"Jul",
				"Aug",
				"Sep",
				"Oct",
			],
		},
		yaxis: {
			title: {
				text: "$ (thousands)",
			},
		},
		grid: {
			borderColor: "#f1f1f1",
		},
		fill: {
			opacity: 1,
		},
		tooltip: {
			y: {
				formatter: function (val) {
					return "$ " + val + " thousands";
				},
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#basiccolumn"), options)
  		chart.render()
	})
</script>

<div id="basiccolumn" class="apex-charts" dir="ltr"></div>
