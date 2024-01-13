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

	var chartGroupbarColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: "bar",
			height: 410,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				data: [44, 55, 41, 64, 22, 43, 21],
			},
			{
				data: [53, 32, 33, 52, 13, 44, 32],
			},
		],
		plotOptions: {
			bar: {
				horizontal: true,
				dataLabels: {
					position: "top",
				},
			},
		},
		dataLabels: {
			enabled: true,
			offsetX: -6,
			style: {
				fontSize: "12px",
				colors: ["#fff"],
			},
		},
		stroke: {
			show: true,
			width: 1,
			colors: ["#fff"],
		},
		tooltip: {
			shared: true,
			intersect: false,
		},
		xaxis: {
			categories: [2001, 2002, 2003, 2004, 2005, 2006, 2007],
		},
		colors: chartGroupbarColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#groupesbarchart"), options)
  		chart.render()
	})
</script>

<div id="groupesbarchart" class="apex-charts" dir="ltr"></div>
