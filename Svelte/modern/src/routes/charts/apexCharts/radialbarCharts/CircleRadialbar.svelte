<script>
	import {onMount} from 'svelte';
	import allseries from "../series";
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

	var chartRadialbarCircleColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 350,
			type: "radialBar",
		},
		series: [76, 67, 61, 55],
		plotOptions: {
			radialBar: {
				offsetY: 0,
				startAngle: 0,
				endAngle: 270,
				hollow: {
					margin: 5,
					size: "30%",
					background: "transparent",
					image: undefined,
				},
				dataLabels: {
					name: {
						show: false,
					},
					value: {
						show: false,
					},
				},
			},
		},
		colors: chartRadialbarCircleColors,
		labels: ["Vimeo", "Messenger", "Facebook", "LinkedIn"],
		legend: {
			show: true,
			floating: true,
			fontSize: "16px",
			position: "left",
			offsetX: 160,
			offsetY: 15,
			labels: {
				useSeriesColors: true,
			},
			markers: {
				size: 0,
			},
			formatter: function (seriesName, opts) {
				return (
					seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
				);
			},
			itemMargin: {
				vertical: 3,
			},
		},
		responsive: [
			{
				breakpoint: 480,
				options: {
					legend: {
						show: false,
					},
				},
			},
		],
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#circleradialbarchart"), options)
  		chart.render()
	})
</script>

<div id="circleradialbarchart" class="apex-charts" dir="ltr"></div>
