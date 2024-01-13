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

	var chartColumnStacked100Colors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			type: "bar",
			height: 350,
			stacked: !0,
			stackType: "100%",
			toolbar: {
				show: !1,
			},
		},
		series: [
			{
				name: "PRODUCT A",
				data: [44, 55, 41, 67, 22, 43, 21, 49],
			},
			{
				name: "PRODUCT B",
				data: [13, 23, 20, 8, 13, 27, 33, 12],
			},
			{
				name: "PRODUCT C",
				data: [11, 17, 15, 15, 21, 14, 15, 13],
			},
		],
		responsive: [
			{
				breakpoint: 480,
				options: {
					legend: {
						position: "bottom",
						offsetX: -10,
						offsetY: 0,
					},
				},
			},
		],
		xaxis: {
			categories: [
				"2011 Q1",
				"2011 Q2",
				"2011 Q3",
				"2011 Q4",
				"2012 Q1",
				"2012 Q2",
				"2012 Q3",
				"2012 Q4",
			],
		},
		fill: {
			opacity: 1,
		},
		legend: {
			position: "right",
			offsetX: 0,
			offsetY: 50,
		},
		colors: chartColumnStacked100Colors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#stackedcolumn2"), options)
  		chart.render()
	})
</script>

<div id="stackedcolumn2" class="apex-charts" dir="ltr"></div>
