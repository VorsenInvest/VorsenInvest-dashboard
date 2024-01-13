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
			height: 326,
			type: "radialBar",
			offsetY: -10,
		},
		series: [67],
		plotOptions: {
			radialBar: {
				startAngle: -135,
				endAngle: 135,
				dataLabels: {
					name: {
						fontSize: "16px",
						color: undefined,
						offsetY: 120,
					},
					value: {
						offsetY: 76,
						fontSize: "22px",
						color: undefined,
						formatter: function (val) {
							return val + "%";
						},
					},
				},
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "dark",
				shadeIntensity: 0.15,
				inverseColors: false,
				opacityFrom: 1,
				opacityTo: 1,
				stops: [0, 50, 65, 91],
			},
		},
		stroke: {
			dashArray: 4,
		},
		labels: ["Median Ratio"],
		colors: chartStorkeRadialbarColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#stokedcircleradialchart"), options)
  		chart.render()
	})
</script>

<div id="stokedcircleradialchart" class="apex-charts" dir="ltr"></div>
