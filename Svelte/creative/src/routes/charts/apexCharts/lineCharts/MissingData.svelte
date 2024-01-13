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

	var MissingDataColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 480,
			type: "line",
			zoom: {
				enabled: false,
			},
			animations: {
				enabled: false,
			},
		},
		series: [
			{
				name: "Peter",
				data: [
					5,
					5,
					10,
					8,
					7,
					5,
					4,
					null,
					null,
					null,
					10,
					10,
					7,
					8,
					6,
					9,
				],
			},
			{
				name: "Johnny",
				data: [
					10,
					15,
					null,
					12,
					null,
					10,
					12,
					15,
					null,
					null,
					12,
					null,
					14,
					null,
					null,
					null,
				],
			},
			{
				name: "David",
				data: [
					null,
					null,
					null,
					null,
					3,
					4,
					1,
					3,
					4,
					6,
					7,
					9,
					5,
					null,
					null,
					null,
				],
			},
		],
		stroke: {
			width: [5, 5, 4],
			curve: "straight",
		},
		labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
		title: {
			text: "Missing data (null values)",
			style: {
				fontWeight: 500,
			},
		},
		xaxis: {},
		colors: MissingDataColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#MissingData"), options)
  		chart.render()
	})
</script>

<div id="MissingData" class="apex-charts" dir="ltr"></div>
