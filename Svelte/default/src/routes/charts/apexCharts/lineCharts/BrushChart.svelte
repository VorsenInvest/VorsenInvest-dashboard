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

	var BrushChartColors = getChartColorsArray(dataColors);

	const generateDayWiseTimeSeries = (baseval, count, yrange) => {
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

	var data = generateDayWiseTimeSeries(
		new Date("11 Feb 2017").getTime(),
		185,
		{
			min: 30,
			max: 90,
		}
	);
	var options = {
		chart: {
			id: "chart2",
			type: "line",
			height: 220,
			toolbar: {
				autoSelected: "pan",
				show: false,
			},
		},
		series: [
			{
				data: data,
			},
		],
		colors: BrushChartColors,
		stroke: {
			width: 3,
		},
		dataLabels: {
			enabled: false,
		},
		fill: {
			opacity: 1,
		},
		markers: {
			size: 0,
		},
		xaxis: {
			type: "datetime",
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#brushchart"), options)
  		chart.render()
	})
</script>

<div id="brushchart" class="apex-charts" dir="ltr"></div>
