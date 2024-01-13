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

	var chartPiePatternColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 300,
			type: "donut",
			dropShadow: {
				enabled: true,
				color: "#111",
				top: -1,
				left: 3,
				blur: 3,
				opacity: 0.2,
			},
		},
		series: [44, 55, 41, 17, 15],
		stroke: {
			width: 0,
		},
		plotOptions: {
			pie: {
				donut: {
					labels: {
						show: true,
						total: {
							showAlways: true,
							show: true,
						},
					},
				},
			},
		},
		labels: ["Comedy", "Action", "SciFi", "Drama", "Horror"],
		dataLabels: {
			dropShadow: {
				blur: 3,
				opacity: 0.8,
			},
		},
		fill: {
			type: "pattern",
			opacity: 1,
			pattern: {
				enabled: true,
				style: [
					"verticalLines",
					"squares",
					"horizontalLines",
					"circles",
					"slantedLines",
				],
			},
		},
		states: {
			hover: {
				filter: "none",
			},
		},
		theme: {
			palette: "palette2",
		},
		title: {
			text: "Favourite Movie Type",
			style: {
				fontWeight: 500,
			},
		},
		legend: {
			position: "bottom",
		},
		colors: chartPiePatternColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#patterneddountchart"), options)
  		chart.render()
	})
</script>

<div id="patterneddountchart" class="apex-charts" dir="ltr"></div>
