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

	onMount(() => {
		var chartTreemapRangeColors = getChartColorsArray(dataColors);
		var options = {
			legend: {
				show: false,
			},
			series: [
				{
					data: [
						{
							x: "INTC",
							y: 1.2,
						},
						{
							x: "GS",
							y: 0.4,
						},
						{
							x: "CVX",
							y: -1.4,
						},
						{
							x: "GE",
							y: 2.7,
						},
						{
							x: "CAT",
							y: -0.3,
						},
						{
							x: "RTX",
							y: 5.1,
						},
						{
							x: "CSCO",
							y: -2.3,
						},
						{
							x: "JNJ",
							y: 2.1,
						},
						{
							x: "PG",
							y: 0.3,
						},
						{
							x: "TRV",
							y: 0.12,
						},
						{
							x: "MMM",
							y: -2.31,
						},
						{
							x: "NKE",
							y: 3.98,
						},
						{
							x: "IYT",
							y: 1.67,
						},
					],
				},
			],
			chart: {
				height: 350,
				type: "treemap",
				toolbar: {
					show: false,
				},
			},
			title: {
				text: "Treemap with Color scale",
				style: {
					fontWeight: 500,
				},
			},
			dataLabels: {
				enabled: true,
				style: {
					fontSize: "12px",
				},
				formatter: function (text, op) {
					return [text, op.value];
				},
				offsetY: -4,
			},
			plotOptions: {
				treemap: {
					enableShades: true,
					shadeIntensity: 0.5,
					reverseNegativeShade: true,
					colorScale: {
						ranges: [
							{
								from: -6,
								to: 0,
								color: chartTreemapRangeColors[0],
							},
							{
								from: 0.001,
								to: 6,
								color: chartTreemapRangeColors[1],
							},
						],
					},
				},
			},
		};
		const chart = new ApexCharts(
			document.querySelector("#colorrangetreemapchart"),
			options
		);
		chart.render();
	});
</script>

<div id="colorrangetreemapchart" class="apex-charts" dir="ltr" />
