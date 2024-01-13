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

	var chartTimelineAdvancedColors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			toolbar: {
				show: !1,
			},
			type: "rangeBar",
			height: 350,
		},
		series: [
			{
				name: "Bob",
				data: [
					{
						x: "Design",
						y: [
							new Date("2019-03-05").getTime(),
							new Date("2019-03-08").getTime(),
						],
					},
					{
						x: "Code",
						y: [
							new Date("2019-03-02").getTime(),
							new Date("2019-03-05").getTime(),
						],
					},
					{
						x: "Code",
						y: [
							new Date("2019-03-05").getTime(),
							new Date("2019-03-07").getTime(),
						],
					},
					{
						x: "Test",
						y: [
							new Date("2019-03-03").getTime(),
							new Date("2019-03-09").getTime(),
						],
					},
					{
						x: "Test",
						y: [
							new Date("2019-03-08").getTime(),
							new Date("2019-03-11").getTime(),
						],
					},
					{
						x: "Validation",
						y: [
							new Date("2019-03-11").getTime(),
							new Date("2019-03-16").getTime(),
						],
					},
					{
						x: "Design",
						y: [
							new Date("2019-03-01").getTime(),
							new Date("2019-03-03").getTime(),
						],
					},
				],
			},
			{
				name: "Joe",
				data: [
					{
						x: "Design",
						y: [
							new Date("2019-03-02").getTime(),
							new Date("2019-03-05").getTime(),
						],
					},
					{
						x: "Test",
						y: [
							new Date("2019-03-06").getTime(),
							new Date("2019-03-16").getTime(),
						],
					},
					{
						x: "Code",
						y: [
							new Date("2019-03-03").getTime(),
							new Date("2019-03-07").getTime(),
						],
					},
					{
						x: "Deployment",
						y: [
							new Date("2019-03-20").getTime(),
							new Date("2019-03-22").getTime(),
						],
					},
					{
						x: "Design",
						y: [
							new Date("2019-03-10").getTime(),
							new Date("2019-03-16").getTime(),
						],
					},
				],
			},
			{
				name: "Dan",
				data: [
					{
						x: "Code",
						y: [
							new Date("2019-03-10").getTime(),
							new Date("2019-03-17").getTime(),
						],
					},
					{
						x: "Validation",
						y: [
							new Date("2019-03-05").getTime(),
							new Date("2019-03-09").getTime(),
						],
					},
				],
			},
		],
		plotOptions: {
			bar: {
				horizontal: !0,
				barHeight: "80%",
			},
		},
		xaxis: {
			type: "datetime",
		},
		stroke: {
			width: 1,
		},
		fill: {
			type: "solid",
			opacity: 0.6,
		},
		legend: {
			position: "top",
			horizontalAlign: "left",
		},
		colors: chartTimelineAdvancedColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#advancedtimelinechart"), options)
  		chart.render()
	})
</script>

<div id="advancedtimelinechart" class="apex-charts" dir="ltr"></div>
