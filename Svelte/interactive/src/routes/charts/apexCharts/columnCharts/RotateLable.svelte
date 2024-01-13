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

	var chartColumnRotateLabelsColors = getChartColorsArray(dataColors);
	var options = {
		annotations: {
			points: [
				{
					x: "Bananas",
					seriesIndex: 0,
					label: {
						borderColor: "#775DD0",
						offsetY: 0,
						style: {
							color: "#fff",
							background: "#775DD0",
						},
						text: "Bananas are good",
					},
				},
			],
		},
		chart: {
			height: 350,
			type: "bar",
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Servings",
				data: [44, 55, 41, 67, 22, 43, 21, 33, 45, 31, 87, 65, 35],
			},
		],
		plotOptions: {
			bar: {
				borderRadius: 10,
				columnWidth: "50%",
			},
		},
		dataLabels: {
			enabled: false,
		},
		stroke: {
			width: 2,
		},
		colors: chartColumnRotateLabelsColors,
		xaxis: {
			labels: {
				rotate: -45,
			},
			categories: [
				"Apples",
				"Oranges",
				"Strawberries",
				"Pineapples",
				"Mangoes",
				"Bananas",
				"Blackberries",
				"Pears",
				"Watermelons",
				"Cherries",
				"Pomegranates",
				"Tangerines",
				"Papayas",
			],
			tickPlacement: "on",
		},
		yaxis: {
			title: {
				text: "Servings",
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "light",
				type: "horizontal",
				shadeIntensity: 0.25,
				gradientToColors: undefined,
				inverseColors: true,
				opacityFrom: 0.85,
				opacityTo: 0.85,
				stops: [50, 0, 100],
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#rotatelable"), options)
  		chart.render()
	})
</script>

<div id="rotatelable" class="apex-charts" dir="ltr"></div>
