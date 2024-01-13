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

	var chartRadialbarGradientColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 350,
			type: "radialBar",
			toolbar: {
				show: false,
			},
		},
		series: [75],
		plotOptions: {
			radialBar: {
				startAngle: -135,
				endAngle: 225,
				hollow: {
					margin: 0,
					size: "70%",
					image: undefined,
					imageOffsetX: 0,
					imageOffsetY: 0,
					position: "front",
				},
				track: {
					strokeWidth: "67%",
					margin: 0, // margin is in pixels
				},

				dataLabels: {
					show: true,
					name: {
						offsetY: -10,
						show: true,
						color: "#888",
						fontSize: "17px",
					},
					value: {
						formatter: function (val) {
							return parseInt(val);
						},
						color: "#111",
						fontSize: "36px",
						show: true,
					},
				},
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "dark",
				type: "horizontal",
				shadeIntensity: 0.5,
				gradientToColors: chartRadialbarGradientColors,
				inverseColors: true,
				opacityFrom: 1,
				opacityTo: 1,
				stops: [0, 100],
			},
		},
		stroke: {
			lineCap: "round",
		},
		labels: ["Percent"],
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#gradientcircleradialbarchart"), options)
  		chart.render()
	})
</script>

<div id="gradientcircleradialbarchart" class="apex-charts" dir="ltr"></div>
