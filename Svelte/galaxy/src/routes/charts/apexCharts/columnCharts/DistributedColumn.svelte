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

	var chartColumnDistributedColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 350,
			type: "bar",
			events: {
				click: function (chart, w, e) {},
			},
		},
		series: [
			{
				data: [21, 22, 10, 28, 16, 21, 13, 30],
			},
		],
		colors: chartColumnDistributedColors,
		plotOptions: {
			bar: {
				columnWidth: "45%",
				distributed: true,
			},
		},
		dataLabels: {
			enabled: false,
		},
		legend: {
			show: false,
		},
		xaxis: {
			categories: [
				["John", "Doe"],
				["Joe", "Smith"],
				["Jake", "Williams"],
				"Amber",
				["Peter", "Brown"],
				["Mary", "Evans"],
				["David", "Wilson"],
				["Lily", "Roberts"],
			],
			labels: {
				style: {
					colors: [
						"#038edc",
						"#51d28c",
						"#f7cc53",
						"#f34e4e",
						"#564ab1",
						"#5fd0f3",
					],
					fontSize: "12px",
				},
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#disributedcolumn"), options)
  		chart.render()
	})
</script>

<div id="disributedcolumn" class="apex-charts" dir="ltr"></div>
