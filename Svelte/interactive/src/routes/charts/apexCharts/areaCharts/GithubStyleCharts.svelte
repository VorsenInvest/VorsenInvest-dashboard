<script>
	import {onMount} from 'svelte';
	import allseries from "../series";
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

	var areachartMonthsColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			id: "chartyear",
			type: "area",
			height: 120,
			toolbar: {
				show: false,
				autoSelected: "pan",
			},
			events: {
				mounted: function (chart) {
					if (browser) {
						var commitsEl = document.querySelector(
							".cmeta span.commits"
						);
						var commits = chart.getSeriesTotalXRange(
							chart.w.globals.minX,
							chart.w.globals.maxX
						);

						commitsEl.innerHTML = commits;
					}
				},
				updated: function (chart) {
					if (browser) {
						var commitsEl = document.querySelector(
							".cmeta span.commits"
						);
						var commits = chart.getSeriesTotalXRange(
							chart.w.globals.minX,
							chart.w.globals.maxX
						);

						commitsEl.innerHTML = commits;
					}
				},
			},
		},
		series: [
			{
				name: "commits",
				data: allseries.githubdata.series,
			},
		],
		colors: areachartMonthsColors,
		stroke: {
			width: 0,
			curve: "smooth",
		},
		dataLabels: {
			enabled: false,
		},
		fill: {
			opacity: 1,
			type: "solid",
		},
		yaxis: {
			show: false,
			tickAmount: 3,
		},
		xaxis: {
			type: "datetime",
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#githubstylechart"), options)
  		chart.render()
	})
</script>

<div id="githubstylechart" class="apex-charts" dir="ltr"></div>
