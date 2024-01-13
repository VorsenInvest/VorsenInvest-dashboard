<script>
	import {onMount} from 'svelte';
	export let dataColors;
	import avatar1 from "../../../../assets/images/users/avatar-1.jpg";
	import avatar2 from "../../../../assets/images/users/avatar-2.jpg";
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

	var chartScatterImagesColors = getChartColorsArray(dataColors);

	const options = {
		chart: {
			height: 350,
			type: "scatter",
			animations: {
				enabled: !1,
			},
			zoom: {
				enabled: !1,
			},
			toolbar: {
				show: !1,
			},
		},
		series: [
			{
				name: "User A",
				data: [
					[16.4, 5.4],
					[21.7, 4],
					[25.4, 3],
					[19, 2],
					[10.9, 1],
					[13.6, 3.2],
					[10.9, 7],
					[10.9, 8.2],
					[16.4, 4],
					[13.6, 4.3],
					[13.6, 12],
					[29.9, 3],
					[10.9, 5.2],
					[16.4, 6.5],
					[10.9, 8],
					[24.5, 7.1],
					[10.9, 7],
					[8.1, 4.7],
				],
			},
			{
				name: "User B",
				data: [
					[6.4, 5.4],
					[11.7, 4],
					[15.4, 3],
					[9, 2],
					[10.9, 11],
					[20.9, 7],
					[12.9, 8.2],
					[6.4, 14],
					[11.6, 12],
				],
			},
		],
		colors: chartScatterImagesColors,
		xaxis: {
			tickAmount: 10,
			min: 0,
			max: 40,
		},
		yaxis: {
			tickAmount: 7,
		},
		markers: {
			size: 20,
		},
		fill: {
			type: "image",
			opacity: 1,
			image: {
				src: [avatar1, avatar2],
				width: 40,
				height: 40,
			},
		},
		legend: {
			labels: {
				useSeriesColors: !0,
			},
			markers: {
				customHTML: [
					function () {
						return "";
					},
					function () {
						return "";
					},
				],
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#imagesscatterchart"), options)
  		chart.render()
	})
</script>

<div id="imagesscatterchart" class="apex-charts" dir="ltr"></div>
