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

	var chartTreemapBasicColors = getChartColorsArray(dataColors);

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
				data: [
					{
						x: "New Delhi",
						y: 218,
					},
					{
						x: "Kolkata",
						y: 149,
					},
					{
						x: "Mumbai",
						y: 184,
					},
					{
						x: "Ahmedabad",
						y: 55,
					},
					{
						x: "Bangaluru",
						y: 84,
					},
					{
						x: "Pune",
						y: 31,
					},
					{
						x: "Chennai",
						y: 70,
					},
					{
						x: "Jaipur",
						y: 30,
					},
					{
						x: "Surat",
						y: 44,
					},
					{
						x: "Hyderabad",
						y: 68,
					},
					{
						x: "Lucknow",
						y: 28,
					},
					{
						x: "Indore",
						y: 19,
					},
					{
						x: "Kanpur",
						y: 29,
					},
				],
			},
		],
		colors: chartTreemapBasicColors,
		title: {
			text: "Basic Treemap",
			style: {
				fontWeight: 500,
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#basictreemap"), options)
  		chart.render()
	})
</script>

<div id="basictreemap" class="apex-charts" dir="ltr"></div>
