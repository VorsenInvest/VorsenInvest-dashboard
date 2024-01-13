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

	var chartRadialbarMultipleColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 350,
			type: "radialBar",
		},
		series: [44, 55, 67, 83],
		plotOptions: {
			radialBar: {
				dataLabels: {
					name: {
						fontSize: "22px",
					},
					value: {
						fontSize: "16px",
					},
					total: {
						show: true,
						label: "Total",
						formatter: function (w) {
							return 249;
						},
					},
				},
			},
		},
		labels: ["Apples", "Oranges", "Bananas", "Berries"],
		colors: chartRadialbarMultipleColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#multipleradialbarchart"), options)
  		chart.render()
	})
</script>

<div id="multipleradialbarchart" class="apex-charts" dir="ltr"></div>
