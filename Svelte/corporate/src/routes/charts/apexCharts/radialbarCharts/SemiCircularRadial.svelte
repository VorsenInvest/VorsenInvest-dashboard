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

	var chartStorkeRadialbarColors = getChartColorsArray(dataColors);
	var options = {
		chart: {
			type: "radialBar",
			height: 350,
			offsetY: -20,
			sparkline: {
				enabled: true,
			},
		},
		series: [76],
		plotOptions: {
			radialBar: {
				startAngle: -90,
				endAngle: 90,
				track: {
					background: "#e7e7e7",
					strokeWidth: "97%",
					margin: 5, // margin is in pixels
					dropShadow: {
						enabled: true,
						top: 2,
						left: 0,
						color: "#999",
						opacity: 1,
						blur: 2,
					},
				},
				dataLabels: {
					name: {
						show: false,
					},
					value: {
						offsetY: -2,
						fontSize: "22px",
					},
				},
			},
		},
		grid: {
			padding: {
				top: -10,
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "light",
				shadeIntensity: 0.4,
				inverseColors: false,
				opacityFrom: 1,
				opacityTo: 1,
				stops: [0, 50, 53, 91],
			},
		},
		labels: ["Average Results"],
		colors: chartStorkeRadialbarColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#semicircleradialchart"), options)
  		chart.render()
	})
</script>

<div id="semicircleradialchart" class="apex-charts" dir="ltr"></div>
