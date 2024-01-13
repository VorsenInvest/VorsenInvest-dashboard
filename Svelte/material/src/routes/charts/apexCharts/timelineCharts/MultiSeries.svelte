<script>
	import {onMount} from 'svelte';
	import dayjs from "dayjs";

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
						var rgbaColor = getComputedStyle(document.documentElement).getPropertyValue(val[0]);
						rgbaColor = "rgba(" + rgbaColor + "," + val[1] + ")";
						return rgbaColor;
					} else {
						return newValue;
					}
				}
			});
		}
	}

	function convertTime(todaydate) {
		const datwe = dayjs(todaydate);
		return datwe;
	}

	var chartTimelineMultiSeriesColors = getChartColorsArray(dataColors);
	var options = {
		chart: {
			toolbar: {
				show: false,
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
							new Date("2019-03-08").getTime(),
							new Date("2019-03-11").getTime(),
						],
					},
					{
						x: "Test",
						y: [
							new Date("2019-03-11").getTime(),
							new Date("2019-03-16").getTime(),
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
						x: "Code",
						y: [
							new Date("2019-03-06").getTime(),
							new Date("2019-03-09").getTime(),
						],
					},
					{
						x: "Test",
						y: [
							new Date("2019-03-10").getTime(),
							new Date("2019-03-19").getTime(),
						],
					},
				],
			},
		],
		plotOptions: {
			bar: {
				horizontal: true,
			},
		},
		dataLabels: {
			enabled: true,
			formatter: function (val) {
				var a = convertTime(val[0]);
				var b = convertTime(val[1]);
				var diff = b.diff(a, "days");
				return diff + (diff > 1 ? " days" : " day");
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "light",
				type: "vertical",
				shadeIntensity: 0.25,
				gradientToColors: undefined,
				inverseColors: true,
				opacityFrom: 1,
				opacityTo: 1,
				stops: [50, 0, 100, 100],
			},
		},
		xaxis: {
			type: "datetime",
		},
		legend: {
			position: "top",
		},
		colors: chartTimelineMultiSeriesColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#multiserieschart"), options)
  		chart.render()
	})
</script>

<div id="multiserieschart" class="apex-charts" dir="ltr"></div>
