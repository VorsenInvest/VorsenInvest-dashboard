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

	var chartBubbleColors = getChartColorsArray(dataColors);
	const generateData = (baseval, count, yrange) => {
		var i = 0;
		var series = [];
		while (i < count) {
			var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;
			var y =
				Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
				yrange.min;
			var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

			series.push([x, y, z]);
			baseval += 86400000;
			i++;
		}
		return series;
	};

	const options = {
		chart: {
			toolbar: {
				show: false,
			},
			type: "bubble",
			height: 350,
		},
		series: [
			{
				name: "Product1",
				data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
					min: 10,
					max: 60,
				}),
			},
			{
				name: "Product2",
				data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
					min: 10,
					max: 60,
				}),
			},
			{
				name: "Product3",
				data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
					min: 10,
					max: 60,
				}),
			},
			{
				name: "Product4",
				data: generateData(new Date("11 Feb 2017 GMT").getTime(), 20, {
					min: 10,
					max: 60,
				}),
			},
		],
		dataLabels: {
			enabled: false,
		},
		fill: {
			type: "gradient",
		},
		title: {
			text: "3D Bubble Chart",
			style: {
				fontWeight: 500,
			},
		},
		xaxis: {
			tickAmount: 12,
			type: "datetime",
			labels: {
				rotate: 0,
			},
		},
		yaxis: {
			max: 70,
		},
		theme: {
			palette: "palette2",
		},
		colors: chartBubbleColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#threedbubblechart"), options)
  		chart.render()
	})
</script>

<div id="threedbubblechart" class="apex-charts" dir="ltr"></div>
