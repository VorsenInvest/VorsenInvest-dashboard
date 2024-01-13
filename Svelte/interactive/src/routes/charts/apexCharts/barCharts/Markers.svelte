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

	var chartBarMarkersColors = getChartColorsArray(dataColors);

	var options = {
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
						y: 12,
						goals: [
							{
								name: "Expected",
								value: 14,
								strokeWidth: 5,
								strokeColor: "#564ab1",
							},
						],
					},
					{
						x: "2012",
						y: 44,
						goals: [
							{
								name: "Expected",
								value: 54,
								strokeWidth: 5,
								strokeColor: "#564ab1",
							},
						],
					},
					{
						x: "2013",
						y: 54,
						goals: [
							{
								name: "Expected",
								value: 52,
								strokeWidth: 5,
								strokeColor: "#564ab1",
							},
						],
					},
					{
						x: "2014",
						y: 66,
						goals: [
							{
								name: "Expected",
								value: 65,
								strokeWidth: 5,
								strokeColor: "#564ab1",
							},
						],
					},
					{
						x: "2015",
						y: 81,
						goals: [
							{
								name: "Expected",
								value: 66,
								strokeWidth: 5,
								strokeColor: "#564ab1",
							},
						],
					},
					{
						x: "2016",
						y: 67,
						goals: [
							{
								name: "Expected",
								value: 70,
								strokeWidth: 5,
								strokeColor: "#564ab1",
							},
						],
					},
				],
			},
		],
		plotOptions: {
			bar: {
				horizontal: !0,
			},
		},
		colors: chartBarMarkersColors,
		dataLabels: {
			formatter: function (val, opt) {
				var goals =
					opt.w.config.series[opt.seriesIndex].data[
						opt.dataPointIndex
					].goals;

				if (goals && goals.length) {
					return `${val} / ${goals[0].value}`;
				}
				return val;
			},
		},
		legend: {
			show: !0,
			showForSingleSeries: !0,
			customLegendItems: ["Actual", "Expected"],
			Markers: {
				fillColors: ["#00E396", "#775DD0"],
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#markerbarchart"), options)
  		chart.render()
	})
</script>

<div id="markerbarchart" class="apex-charts" dir="ltr"></div>
