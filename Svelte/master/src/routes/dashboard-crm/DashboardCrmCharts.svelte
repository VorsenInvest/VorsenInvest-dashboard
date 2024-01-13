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

	const areachartSalesColors = getChartColorsArray(dataColors);

	const THEME_CHART_COLORS = {
		default: ["--vz-primary", "--vz-success", "--vz-warning"],
		minimal: ["--vz-primary-rgb, 0.75", "--vz-primary", "--vz-primary-rgb, 0.55"],
		creative: ["--vz-primary", "--vz-secondary", "--vz-info"],
		corporate: ["--vz-primary", "--vz-success", "--vz-secondary"],
		galaxy: ["--vz-primary", "--vz-secondary", "--vz-info"], 
		classic: ["--vz-primary", "--vz-warning", "--vz-secondary"],
		modern: ["--vz-primary", "--vz-success", "--vz-warning"],
		interactive: ["--vz-primary", "--vz-success", "--vz-warning"],
		vintage: ["--vz-primary", "--vz-success", "--vz-warning"],
		saas: ["--vz-primary", "--vz-success", "--vz-warning"],
		material: ["--vz-primary", "--vz-success", "--vz-warning"],
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

	var options = {
		chart: {
			type: "bar",
			height: 341,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Goal",
				data: [37],
			},
			{
				name: "Pending Forcast",
				data: [12],
			},
			{
				name: "Revenue",
				data: [18],
			},
		],
		plotOptions: {
			bar: {
				horizontal: false,
				columnWidth: "65%",
			},
		},
		stroke: {
			show: true,
			width: 5,
			colors: ["transparent"],
		},
		xaxis: {
			categories: [""],
			axisTicks: {
				show: false,
				borderType: "solid",
				color: "#78909C",
				height: 6,
				offsetX: 0,
				offsetY: 0,
			},
			title: {
				text: "Total Forecasted Value",
				offsetX: 0,
				offsetY: -30,
				style: {
					color: "#78909C",
					fontSize: "12px",
					fontWeight: 400,
				},
			},
		},
		yaxis: {
			labels: {
				formatter: function (value) {
					return "$" + value + "k";
				},
			},
			tickAmount: 4,
			min: 0,
		},
		fill: {
			opacity: 1,
		},
		legend: {
			show: true,
			position: "bottom",
			horizontalAlign: "center",
			fontWeight: 500,
			offsetX: 0,
			offsetY: -14,
			itemMargin: {
				horizontal: 8,
				vertical: 0,
			},
			markers: {
				width: 10,
				height: 10,
			},
		},
		colors: areachartSalesColors,
	};
	onMount(() => {
			chart = new ApexCharts(
			document.querySelector("#dashboardcrmchart"),
			options
		);
		chart.render();
	});
</script>

<div id="dashboardcrmchart" class="apex-charts" dir="ltr" />
