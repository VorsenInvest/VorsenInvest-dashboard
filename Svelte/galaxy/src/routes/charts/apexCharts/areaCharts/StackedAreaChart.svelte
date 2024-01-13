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

	var BasicAreaChartsColors = getChartColorsArray(dataColors);

	var generateDayWiseTimeSeries = function (baseval, count, yrange) {
		var i = 0;
		var series = [];
		while (i < count) {
			var x = baseval;
			var y =
				Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
				yrange.min;

			series.push([x, y]);
			baseval += 86400000;
			i++;
		}
		return series;
	};

	var options = {
		chart: {
			type: "area",
			height: 350,
			stacked: true,
			toolbar: {
				show: false,
			},
			events: {
				selection: function (chart, e) {
				},
			},
		},
		series: [
			{
				name: "South",
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
				name: "North",
				data: generateDayWiseTimeSeries(
					new Date("11 Feb 2017 GMT").getTime(),
					20,
					{
						min: 10,
						max: 20,
					}
				),
			},
			{
				name: "Central",
				data: generateDayWiseTimeSeries(
					new Date("11 Feb 2017 GMT").getTime(),
					20,
					{
						min: 10,
						max: 15,
					}
				),
			},
		],
		colors: BasicAreaChartsColors,
		dataLabels: {
			enabled: false,
		},
		stroke: {
			curve: "smooth",
		},
		fill: {
			type: "gradient",
			gradient: {
				opacityFrom: 0.6,
				opacityTo: 0.8,
			},
		},
		legend: {
			position: "top",
			horizontalAlign: "left",
		},
		xaxis: {
			type: "datetime",
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#stackedareachart"), options)
  		chart.render()
	})
</script>

<div id="stackedareachart" class="apex-charts" dir="ltr"></div>
