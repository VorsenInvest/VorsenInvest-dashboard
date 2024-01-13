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

	var BasicColors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			type: "bar",
			height: 350,
			toolbar: {
				show: !1,
			},
		},
		series: [
			{
				data: [380, 430, 450, 475, 550, 584, 780, 1100, 1220, 1365],
			},
		],

		plotOptions: {
			bar: {
				horizontal: !0,
			},
		},
		dataLabels: {
			enabled: !1,
		},
		colors: BasicColors,
		grid: {
			borderColor: "#f1f1f1",
		},
		xaxis: {
			categories: [
				"South Korea",
				"Canada",
				"United Kingdom",
				"Netherlands",
				"Italy",
				"France",
				"Japan",
				"United States",
				"China",
				"Germany",
			],
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#basicbarchart"), options)
  		chart.render()
	})
</script>

<div id="basicbarchart" class="apex-charts" dir="ltr"></div>
