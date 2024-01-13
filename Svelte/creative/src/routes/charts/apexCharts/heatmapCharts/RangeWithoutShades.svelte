<script>
	import { onMount } from "svelte";
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

	function generateData(count, yrange) {
		var i = 0;
		var series = [];
		while (i < count) {
			var x = (i + 1).toString();
			var y =
				Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
				yrange.min;

			series.push({
				x: x,
				y: y,
			});
			i++;
		}
		return series;
	}

	onMount(() => {
		var chartHeatMapShadesColors = getChartColorsArray(dataColors);

		var options = {
			chart: {
				height: 350,
				type: "heatmap",
				toolbar: {
					show: false,
				},
			},
			series: [
				{
					name: "Metric1",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
				{
					name: "Metric2",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
				{
					name: "Metric3",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
				{
					name: "Metric4",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
				{
					name: "Metric5",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
				{
					name: "Metric6",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
				{
					name: "Metric7",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
				{
					name: "Metric8",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
				{
					name: "Metric8",
					data: generateData(20, {
						min: 0,
						max: 90,
					}),
				},
			],
			stroke: {
				width: 0,
			},
			plotOptions: {
				heatmap: {
					radius: 30,
					enableShades: false,
					colorScale: {
						ranges: [
							{
								from: 0,
								to: 50,
								color: chartHeatMapShadesColors[0],
							},
							{
								from: 51,
								to: 100,
								color: chartHeatMapShadesColors[1],
							},
						],
					},
				},
			},
			dataLabels: {
				enabled: true,
				style: {
					colors: ["#fff"],
				},
			},
			xaxis: {
				type: "category",
			},
			title: {
				text: "Rounded (Range without Shades)",
				style: {
					fontWeight: 500,
				},
			},
		};
		const chart = new ApexCharts(document.querySelector("#rangewithoutshades"),options);
		chart.render();
	});
</script>

<div id="rangewithoutshades" class="apex-charts" dir="ltr" />
