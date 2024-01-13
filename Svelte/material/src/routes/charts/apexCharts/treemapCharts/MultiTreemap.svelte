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

	var chartTreemapMultiColors = getChartColorsArray(dataColors);

	var options = {
		legend: {
			show: false,
		},
		chart: {
			height: 350,
			type: "treemap",
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Desktops",
				data: [
					{
						x: "ABC",
						y: 10,
					},
					{
						x: "DEF",
						y: 60,
					},
					{
						x: "XYZ",
						y: 41,
					},
				],
			},
			{
				name: "Mobile",
				data: [
					{
						x: "ABCD",
						y: 10,
					},
					{
						x: "DEFG",
						y: 20,
					},
					{
						x: "WXYZ",
						y: 51,
					},
					{
						x: "PQR",
						y: 30,
					},
					{
						x: "MNO",
						y: 20,
					},
					{
						x: "CDE",
						y: 30,
					},
				],
			},
		],
		title: {
			text: "Multi-dimensional Treemap",
			align: "center",
			style: {
				fontWeight: 500,
			},
		},
		colors: chartTreemapMultiColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#multitreemap"), options)
  		chart.render()
	})
</script>

<div id="multitreemap" class="apex-charts" dir="ltr"></div>
