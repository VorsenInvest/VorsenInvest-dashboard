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

	var chartScatterDateTimeColors = getChartColorsArray(dataColors);

	const generateDayWiseTimeSeries = (baseval, count, yrange) => {
		var i = 0;
		var series = [];
		while (i < count) {
			var y =
				Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
				yrange.min;

			series.push([baseval, y]);
			baseval += 86400000;
			i++;
		}
		return series;
	};

	const options = {
		chart: {
			height: 350,
			type: "scatter",
			zoom: {
				type: "xy",
			},
			toolbar: {
				show: !1,
			},
		},
		series: [
			{
				name: "TEAM 1",
				data: generateDayWiseTimeSeries(
					new Date("11 Feb 2017 GMT").getTime(),
					20,
					{
						min: 10,
						max: 60,
					}
				),
			},
			{
				name: "TEAM 2",
				data: generateDayWiseTimeSeries(
					new Date("11 Feb 2017 GMT").getTime(),
					20,
					{
						min: 10,
						max: 60,
					}
				),
			},
			{
				name: "TEAM 3",
				data: generateDayWiseTimeSeries(
					new Date("11 Feb 2017 GMT").getTime(),
					30,
					{
						min: 10,
						max: 60,
					}
				),
			},
			{
				name: "TEAM 4",
				data: generateDayWiseTimeSeries(
					new Date("11 Feb 2017 GMT").getTime(),
					10,
					{
						min: 10,
						max: 60,
					}
				),
			},
			{
				name: "TEAM 5",
				data: generateDayWiseTimeSeries(
					new Date("11 Feb 2017 GMT").getTime(),
					30,
					{
						min: 10,
						max: 60,
					}
				),
			},
		],
		dataLabels: {
			enabled: !1,
		},
		grid: {
			xaxis: {
				lines: {
					show: !0,
				},
			},
			yaxis: {
				lines: {
					show: !0,
				},
			},
		},
		xaxis: {
			type: "datetime",
		},
		yaxis: {
			max: 70,
		},
		colors: chartScatterDateTimeColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#datetimescatterchart"), options)
  		chart.render()
	})
</script>

<div id="datetimescatterchart" class="apex-charts" dir="ltr"></div>
