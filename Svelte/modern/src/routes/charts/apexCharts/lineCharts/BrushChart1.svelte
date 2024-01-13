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

	var BrushChart1Colors = getChartColorsArray(dataColors);

	const generateDayWiseTimeSeries = (baseval, count, yrange) => {
		var i = 0;
		var series = [];
		while (i < count) {
			var x = baseval;
			var y =
				Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
				yrange.min;

			series.push([x, y]);
			baseval += 86400000;
			i++;
		}
		return series;
	};

	var data = generateDayWiseTimeSeries(
		new Date("11 Feb 2017").getTime(),
		185,
		{
			min: 30,
			max: 90,
		}
	);

	var options = {
		chart: {
			height: 130,
			type: "area",
			brush: {
				target: "chart2",
				enabled: true,
			},
			selection: {
				enabled: true,
				xaxis: {
					min: new Date("19 Jun 2017").getTime(),
					max: new Date("14 Aug 2017").getTime(),
				},
			},
		},
		series: [
			{
				data: data,
			},
		],
		colors: BrushChart1Colors,
		fill: {
			type: "gradient",
			gradient: {
				opacityFrom: 0.91,
				opacityTo: 0.1,
			},
		},
		xaxis: {
			type: "datetime",
			tooltip: {
				enabled: !1,
			},
		},
		yaxis: {
			tickAmount: 2,
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#brushchart1"), options)
  		chart.render()
	})
</script>

<div id="brushchart1" class="apex-charts" dir="ltr"></div>
