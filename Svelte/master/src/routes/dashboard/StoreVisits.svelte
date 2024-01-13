<script>
	import {
		Card,
		CardHeader,
		Col,
		DropdownItem,
		DropdownMenu,
		DropdownToggle,
		Dropdown,
	} from "sveltestrap";

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

	const chartDonutBasicColors = getChartColorsArray(dataColors);

	const THEME_CHART_COLORS = {
		default: ["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-info"],
		minimal: ["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.70", "--vz-primary-rgb, 0.60", "--vz-primary-rgb, 0.45"],
		interactive: ["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.70", "--vz-primary-rgb, 0.60", "--vz-primary-rgb, 0.45"],
		galaxy: ["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.70", "--vz-primary-rgb, 0.60", "--vz-primary-rgb, 0.45"], 
		creative: ["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-info"],
		corporate: ["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-info"],
		classic: ["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-info"],
		modern: ["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-info"],
		vintage: ["--vz-primary", "--vz-success", "--vz-warning"],
		saas: ["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-info"],
		material: ["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-info"],
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
		labels: ["Direct", "Social", "Email", "Other", "Referrals"],
		chart: {
			height: 333,
			type: "donut",
		},
		series: [44, 55, 41, 17, 15],
		legend: {
			position: "bottom",
		},
		stroke: {
			show: false,
		},
		dataLabels: {
			dropShadow: {
				enabled: false,
			},
		},
		colors: chartDonutBasicColors,
	};

	onMount(() => {
		chart = new ApexCharts(
			document.querySelector("#storevisitor"),
			options
		);
		chart.render();
	});
</script>

<svelte:head>
	<script src="//unpkg.com/simplebar@latest/dist/simplebar.min.js"></script>

	<script
		src="//cdn.jsdelivr.net/npm/simplebar@latest/dist/simplebar.min.js"
	></script>
</svelte:head>

<Col xl={4}>
	<Card class="card-height-100">
		<CardHeader class="align-items-center d-flex">
			<h4 class="card-title mb-0 flex-grow-1">Store Visits by Source</h4>
			<div class="flex-shrink-0">
				<Dropdown class="card-header-dropdown">
					<DropdownToggle
						tag="a"
						color=""
						class="text-reset dropdown-btn p-0"
						role="button"
					>
						<span class="text-muted"
							>Report<i class="mdi mdi-chevron-down ms-1" /></span
						>
					</DropdownToggle>
					<DropdownMenu class="dropdown-menu-end" end>
						<DropdownItem>Download Report</DropdownItem>
						<DropdownItem>Export</DropdownItem>
						<DropdownItem>Import</DropdownItem>
					</DropdownMenu>
				</Dropdown>
			</div>
		</CardHeader>

		<div class="card-body">
			<div dir="ltr">
				<div id="storevisitor" class="apex-charts" dir="ltr" />
			</div>
		</div>
	</Card>
</Col>
