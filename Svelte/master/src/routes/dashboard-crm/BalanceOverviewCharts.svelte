<script>
	import { onMount } from "svelte";
	import { themeChangeEvent } from "$lib/eventBus";
	import { browser } from "$app/environment";
	export let dataColors;
	let chart;

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
	const revenueExpensesChartsColors = getChartColorsArray(dataColors);

	const THEME_CHART_COLORS = {
		default: ["--vz-success", "--vz-danger"],
		minimal: ["--vz-primary", "--vz-info"],
		interactive: ["--vz-info", "--vz-primary"],
		galaxy: ["--vz-primary", "--vz-secondary"],
		classic: ["--vz-primary", "--vz-secondary"],
		creative: ["--vz-success", "--vz-danger"],
		corporate: ["--vz-success", "--vz-danger"],
		modern: ["--vz-success", "--vz-danger"],
		vintage: ["--vz-success", "--vz-danger"],
		saas: ["--vz-success", "--vz-danger"],
		material: ["--vz-success", "--vz-danger"],
	};

	// Function to find the index of a key
	function findIndexByKey(key) {
		const keys = Object.keys(THEME_CHART_COLORS);
		return keys.indexOf(key);
	}

	// Subscribe to the theme change event
	const unsubscribeEvent = themeChangeEvent.subscribe((newTheme) => {
		// Handle the theme change event
		if (newTheme == null || newTheme == undefined) {
			return;
		}
		let key = findIndexByKey(newTheme);
		let newColors;
		if (key >= 0) {
			newColors = THEME_CHART_COLORS[newTheme];
		}
		if (browser) {
			newColors = key >= 0 ? getChartColorsArray(newColors) : dataColors;
			setTimeout(() => {
				chart.updateOptions({
					colors: newColors,
					fill: {
						colors: newColors,
					},
				});
			}, 500);
		}
	});

	var options = {
		chart: {
			height: 290,
			type: "area",
			toolbar: "false",
		},
		series: [
			{
				name: "Revenue",
				data: [20, 25, 30, 35, 40, 55, 70, 110, 150, 180, 210, 250],
			},
			{
				name: "Expenses",
				data: [12, 17, 45, 42, 24, 35, 42, 75, 102, 108, 156, 199],
			},
		],
		dataLabels: {
			enabled: false,
		},
		stroke: {
			curve: "smooth",
			width: 2,
		},
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
		},
		yaxis: {
			labels: {
				formatter: function (value) {
					return "$" + value + "k";
				},
			},
			tickAmount: 5,
			min: 0,
			max: 260,
		},
		colors: revenueExpensesChartsColors,
		fill: {
			opacity: 0.06,
			colors: revenueExpensesChartsColors,
			type: "solid",
		},
	};
	onMount(() => {
		chart = new ApexCharts(
			document.querySelector("#balanceoverviewchart"),
			options,
		);
		chart.render();
	});
</script>

<div id="balanceoverviewchart" class="apex-charts" dir="ltr"></div>
