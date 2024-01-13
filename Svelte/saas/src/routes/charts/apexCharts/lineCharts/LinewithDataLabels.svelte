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
	var LinewithDataLabelsColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 380,
			type: "line",
			zoom: {
				enabled: false,
			},
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "High - 2018",
				data: [26, 24, 32, 36, 33, 31, 33],
			},
			{
				name: "Low - 2018",
				data: [14, 11, 16, 12, 17, 13, 12],
			},
		],
		colors: LinewithDataLabelsColors,
		dataLabels: {
			enabled: false,
		},
		stroke: {
			width: [3, 3],
			curve: "straight",
		},
		title: {
			text: "Average High & Low Temperature",
			align: "left",
			style: {
				fontWeight: 500,
			},
		},
		grid: {
			row: {
				colors: ["transparent", "transparent"], // takes an array which will be repeated on columns
				opacity: 0.2,
			},
			borderColor: "#f1f1f1",
		},
		markers: {
			style: "inverted",
			size: 6,
		},
		xaxis: {
			categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"],
			title: {
				text: "Month",
			},
		},
		yaxis: {
			title: {
				text: "Temperature",
			},
			min: 5,
			max: 40,
		},
		legend: {
			position: "top",
			horizontalAlign: "right",
			floating: true,
			offsetY: -25,
			offsetX: -5,
		},
		responsive: [
			{
				breakpoint: 600,
				options: {
					chart: {
						toolbar: {
							show: false,
						},
					},
					legend: {
						show: false,
					},
				},
			},
		],
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#LinewithDataLabels"), options)
  		chart.render()
	})
</script>

<div id="LinewithDataLabels" class="apex-charts" dir="ltr"></div>