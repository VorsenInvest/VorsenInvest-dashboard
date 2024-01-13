<script>
	import { onMount } from "svelte";
	export let dataColors;
	import { browser } from "$app/environment";
	import { themeChangeEvent } from "$lib/eventBus";
let chart;

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

	const THEME_CHART_COLORS = {
		default: ["--vz-primary", "--vz-warning", "--vz-success"],
		minimal: ["--vz-primary", "--vz-primary-rgb, 0.1", "--vz-primary-rgb, 0.50"],
		interactive: ["--vz-primary", "--vz-info", "--vz-warning"],
		creative: ["--vz-secondary", "--vz-warning", "--vz-success"],
		corporate: ["--vz-primary", "--vz-secondary", "--vz-danger"],
		galaxy: ["--vz-primary", "--vz-primary-rgb, 0.1", "--vz-primary-rgb, 0.50"], 
		classic: ["--vz-primary", "--vz-secondary", "--vz-warning"],
		modern: ["--vz-primary", "--vz-warning", "--vz-success"],
		vintage: ["--vz-primary", "--vz-warning", "--vz-success"],
		saas: ["--vz-primary", "--vz-warning", "--vz-success"],
		material: ["--vz-primary", "--vz-warning", "--vz-success"],
	};

	// Function to find the index of a key
	function findIndexByKey(key) {
		const keys = Object.keys(THEME_CHART_COLORS);
		return keys.indexOf(key);
	}

	// Subscribe to the theme change event
	const unsubscribeEvent = themeChangeEvent.subscribe((newTheme) => {
		// Handle the theme change event
		if(newTheme == null || newTheme == undefined){
			return;
		}
		let key = findIndexByKey(newTheme);
		let newColors;
		if (key >= 0) {
			newColors = THEME_CHART_COLORS[newTheme];
		}
		if (browser) {
			newColors = ( key >= 0) ? getChartColorsArray(newColors) : dataColors;
			setTimeout(() => {
				chart.updateOptions({
					colors: newColors,
				});
			}, 500);
		}
	});

	onMount(() => {
		const linechartcustomerColors = getChartColorsArray(dataColors);

		var options = {
			chart: {
				height: 374,
				type: "line",
				toolbar: {
					show: false,
				},
			},
			series: [
				{
					name: "Number of Projects",
					type: "bar",
					data: [34, 65, 46, 68, 49, 61, 42, 44, 78, 52, 63, 67],
				},
				{
					name: "Revenue",
					type: "area",
					data: [
						89.25, 98.58, 68.74, 108.87, 77.54, 84.03, 51.24, 28.57,
						92.57, 42.36, 88.51, 36.57,
					],
				},
				{
					name: "Active Projects",
					type: "bar",
					data: [8, 12, 7, 17, 21, 11, 5, 9, 7, 29, 12, 35],
				},
			],
			stroke: {
				curve: "smooth",
				dashArray: [0, 3, 0],
				width: [0, 1, 0],
			},
			fill: {
				opacity: [1, 0.1, 1],
			},
			markers: {
				size: [0, 4, 0],
				strokeWidth: 2,
				hover: {
					size: 4,
				},
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
				axisTicks: {
					show: false,
				},
				axisBorder: {
					show: false,
				},
			},
			grid: {
				show: true,
				xaxis: {
					lines: {
						show: true,
					},
				},
				yaxis: {
					lines: {
						show: false,
					},
				},
				padding: {
					top: 0,
					right: -2,
					bottom: 15,
					left: 10,
				},
			},
			legend: {
				show: true,
				horizontalAlign: "center",
				offsetX: 0,
				offsetY: -5,
				markers: {
					width: 9,
					height: 9,
					radius: 6,
				},
				itemMargin: {
					horizontal: 10,
					vertical: 0,
				},
			},
			plotOptions: {
				bar: {
					columnWidth: "30%",
					barHeight: "70%",
				},
			},
			colors: linechartcustomerColors,
			tooltip: {
				shared: true,
				y: [
					{
						formatter: function (y) {
							if (typeof y !== "undefined") {
								return y.toFixed(0);
							}
							return y;
						},
					},
					{
						formatter: function (y) {
							if (typeof y !== "undefined") {
								return "$" + y.toFixed(2) + "k";
							}
							return y;
						},
					},
					{
						formatter: function (y) {
							if (typeof y !== "undefined") {
								return y.toFixed(0);
							}
							return y;
						},
					},
				],
			},
		};
			chart = new ApexCharts(
			document.querySelector("#projectoverviewchart"),
			options
		);
		chart.render();
	});
</script>

<div id="projectoverviewchart" class="apex-charts" dir="ltr" />
