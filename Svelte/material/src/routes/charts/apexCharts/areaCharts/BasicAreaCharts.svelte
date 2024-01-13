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

	var BasicAreaChartsColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: "area",
			height: 350,
			zoom: {
				enabled: false,
			},
		},
		series: [
			{
				name: "STOCK ABC",
				data: allseries.seriesData.monthDataSeries1.prices,
			},
		],
		dataLabels: {
			enabled: false,
		},
		stroke: {
			curve: "straight",
		},

		title: {
			text: "Fundamental Analysis of Stocks",
			align: "left",
			style: {
				fontWeight: 500,
			},
		},
		subtitle: {
			text: "Price Movements",
			align: "left",
		},
		labels: allseries.seriesData.monthDataSeries1.dates,
		xaxis: {
			type: "datetime",
		},
		yaxis: {
			opposite: true,
		},
		legend: {
			horizontalAlign: "left",
		},
		colors: BasicAreaChartsColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#basicareachart"), options)
  		chart.render()
	})
</script>

<div id="basicareachart" class="apex-charts" dir="ltr"></div>
