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

	var chartColumnMarkersColors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			type: "bar",
			height: 350,
			toolbar: {
				show: !1,
			},
		},
		series: [
			{
				name: "Actual",
				data: [
					{
						x: "2011",
						y: 1292,
						goals: [
							{
								name: "Expected",
								value: 1400,
								strokeWidth: 5,
								strokeColor: "#775DD0",
							},
						],
					},
					{
						x: "2012",
						y: 4432,
						goals: [
							{
								name: "Expected",
								value: 5400,
								strokeWidth: 5,
								strokeColor: "#775DD0",
							},
						],
					},
					{
						x: "2013",
						y: 5423,
						goals: [
							{
								name: "Expected",
								value: 5200,
								strokeWidth: 5,
								strokeColor: "#775DD0",
							},
						],
					},
					{
						x: "2014",
						y: 6653,
						goals: [
							{
								name: "Expected",
								value: 6500,
								strokeWidth: 5,
								strokeColor: "#775DD0",
							},
						],
					},
					{
						x: "2015",
						y: 8133,
						goals: [
							{
								name: "Expected",
								value: 6600,
								strokeWidth: 5,
								strokeColor: "#775DD0",
							},
						],
					},
					{
						x: "2016",
						y: 7132,
						goals: [
							{
								name: "Expected",
								value: 7500,
								strokeWidth: 5,
								strokeColor: "#775DD0",
							},
						],
					},
					{
						x: "2017",
						y: 7332,
						goals: [
							{
								name: "Expected",
								value: 8700,
								strokeWidth: 5,
								strokeColor: "#775DD0",
							},
						],
					},
					{
						x: "2018",
						y: 6553,
						goals: [
							{
								name: "Expected",
								value: 7300,
								strokeWidth: 5,
								strokeColor: "#775DD0",
							},
						],
					},
				],
			},
		],
		plotOptions: {
			bar: {
				columnWidth: "30%",
			},
		},
		colors: chartColumnMarkersColors,
		dataLabels: {
			enabled: !1,
		},
		legend: {
			show: !0,
			showForSingleSeries: !0,
			customLegendItems: ["Actual", "Expected"],
			markers: {
				fillColors: ["#51d28c", "#564ab1"],
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#columnmarker"), options)
  		chart.render()
	})
</script>

<div id="columnmarker" class="apex-charts" dir="ltr"></div>
