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

	var GradientChartsColors = getChartColorsArray(dataColors);
	var options = {
		chart: {
			height: 350,
			type: "line",
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Likes",
				data: [
					4, 3, 10, 9, 29, 19, 22, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7,
					5,
				],
			},
		],
		stroke: {
			width: 7,
			curve: "smooth",
		},
		xaxis: {
			type: "datetime",
			categories: [
				"1/11/2001",
				"2/11/2001",
				"3/11/2001",
				"4/11/2001",
				"5/11/2001",
				"6/11/2001",
				"7/11/2001",
				"8/11/2001",
				"9/11/2001",
				"10/11/2001",
				"11/11/2001",
				"12/11/2001",
				"1/11/2002",
				"2/11/2002",
				"3/11/2002",
				"4/11/2002",
				"5/11/2002",
				"6/11/2002",
			],
			tickAmount: 10,
		},
		title: {
			text: "Social Media",
			align: "left",
			style: {
				fontWeight: 500,
			},
		},
		fill: {
			type: "gradient",
			gradient: {
				shade: "dark",
				gradientToColors: ["#0ab39c"],
				shadeIntensity: 1,
				type: "horizontal",
				opacityFrom: 1,
				opacityTo: 1,
				stops: [0, 100, 100, 100],
			},
		},
		markers: {
			size: 4,
			colors: GradientChartsColors,
			strokeColors: "#fff",
			strokeWidth: 2,
			hover: {
				size: 7,
			},
		},
		yaxis: {
			min: -10,
			max: 40,
			title: {
				text: "Engagement",
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#gradientcharts"), options)
  		chart.render()
	})
</script>

<div id="gradientcharts" class="apex-charts" dir="ltr"></div>
