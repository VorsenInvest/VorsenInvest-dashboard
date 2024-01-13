<script>
	import { onDestroy, onMount } from "svelte";
	import { themeChangeEvent } from "$lib/eventBus";
	import { browser } from "$app/environment";

	const THEME_CHART_COLORS = {
		default: ["--vz-success", "--vz-light"],
		minimal: ["--vz-primary", "--vz-light"],
		modern: ["--vz-primary", "--vz-light"],
		interactive: ["--vz-primary", "--vz-light"],
		creative: ["--vz-secondary", "--vz-light"],
		corporate: ["--vz-primary", "--vz-light"],
		galaxy: ["--vz-primary", "--vz-light"],
		classic: ["--vz-primary", "--vz-secondary"],
		vintage: ["--vz-primary", "--vz-success-rgb, 0.5"],
	};

	// Function to find the index of a key
	function findIndexByKey(key) {
		const keys = Object.keys(THEME_CHART_COLORS);
		return keys.indexOf(key);
	}

	// default theme color
	export let dataColors;
	let chart;

	// Subscribe to the theme change event
	const unsubscribeEvent = themeChangeEvent.subscribe((newTheme) => {
		// Handle the theme change event
		if(newTheme == null || newTheme == undefined){
			return;
		}
		let key = findIndexByKey(newTheme);
		if (key >= 0) {
			dataColors = THEME_CHART_COLORS[newTheme];
		}
		console.log(newTheme,dataColors,THEME_CHART_COLORS)
		
		if (browser) {
			dataColors = getChartColorsArray(dataColors)
			setTimeout(() => {
				chart.updateOptions({
					colors: dataColors,
				});
			}, 100);
		}
	});

	function getChartColorsArray(colors) {
		if (browser) {
			return colors.map(function (value) {
				var newValue = value.replace(" ", "");
				if (newValue.indexOf(",") === -1) {
					var color = getComputedStyle(
						document.documentElement,
					).getPropertyValue(newValue);
					if (color.indexOf("#") !== -1)
						color = color.replace(" ", "");
					if (color) return color;
					else return newValue;
				} else {
					var val = value.split(",");
					if (val.length === 2) {
						var rgbaColor = getComputedStyle(
							document.documentElement,
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
	const chartAudienceColumnChartsColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: "bar",
			height: 306,
			stacked: true,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Last Year",
				data: [
					25.3, 12.5, 20.2, 18.5, 40.4, 25.4, 15.8, 22.3, 19.2, 25.3,
					12.5, 20.2,
				],
			},
			{
				name: "Current Year",
				data: [
					36.2, 22.4, 38.2, 30.5, 26.4, 30.4, 20.2, 29.6, 10.9, 36.2,
					22.4, 38.2,
				],
			},
		],
		plotOptions: {
			bar: {
				horizontal: false,
				columnWidth: "20%",
				borderRadius: 6,
			},
		},
		dataLabels: {
			enabled: false,
		},
		legend: {
			show: true,
			position: "bottom",
			horizontalAlign: "center",
			fontWeight: 400,
			fontSize: "8px",
			offsetX: 0,
			offsetY: 0,
			markers: {
				width: 9,
				height: 9,
				radius: 4,
			},
		},
		stroke: {
			show: true,
			width: 2,
			colors: ["transparent"],
		},
		grid: {
			show: false,
		},
		colors: chartAudienceColumnChartsColors,
		xaxis: {
			categories: [
				"Jan",
				"Feb",
				"Mar",
				"Apr",
				"May",
				"Jun",
				"Jul",
				"Aug",
				"Sep",
				"Oct",
				"Nov",
				"Dec",
			],
			axisTicks: {
				show: false,
			},
			axisBorder: {
				show: true,
				strokeDashArray: 1,
				height: 1,
				width: "100%",
				offsetX: 0,
				offsetY: 0,
			},
		},
		yaxis: {
			show: false,
		},
		fill: {
			opacity: 1,
		},
	};

	onMount(() => {
		chart = new ApexCharts(
			document.querySelector("#audiencescharts"),
			options,
		);
		chart.render();
	});

	// Ensure to unsubscribe to avoid memory leaks
	onDestroy(() => {
		unsubscribeEvent();
	});
</script>

<div id="audiencescharts" class="apex-charts" dir="ltr"></div>
