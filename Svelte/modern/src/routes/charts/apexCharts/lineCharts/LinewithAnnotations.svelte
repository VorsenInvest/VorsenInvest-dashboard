<script>
	import {onMount} from 'svelte';
	import allseries from "../series";
	export let dataColors;
	import { browser } from "$app/environment"
	import logosm from '../../../../assets/images/logo-sm.png'

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

	var LinewithAnnotationsColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			height: 350,
			type: "line",
			id: "areachart-2",
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				data: allseries.seriesData.monthDataSeries1.prices,
			},
		],
		annotations: {
			yaxis: [
				{
					y: 8200,
					borderColor: "#038edc",
					label: {
						borderColor: "#038edc",
						style: {
							color: "#fff",
							background: "#038edc",
						},
						text: "Support",
					},
				},
				{
					y: 8600,
					y2: 9000,
					borderColor: "#f7cc53",
					fillColor: "#f7cc53",
					opacity: 0.2,
					label: {
						borderColor: "#f7cc53",
						style: {
							fontSize: "10px",
							color: "#000",
							background: "#f7cc53",
						},
						text: "Y-axis range",
					},
				},
			],
			xaxis: [
				{
					x: new Date("23 Nov 2017").getTime(),
					strokeDashArray: 0,
					borderColor: "#564ab1",
					label: {
						borderColor: "#564ab1",
						style: {
							color: "#fff",
							background: "#564ab1",
						},
						text: "Anno Test",
					},
				},
				{
					x: new Date("26 Nov 2017").getTime(),
					x2: new Date("28 Nov 2017").getTime(),
					fillColor: "#51d28c",
					opacity: 0.4,
					label: {
						borderColor: "#000",
						style: {
							fontSize: "10px",
							color: "#fff",
							background: "#000",
						},
						offsetY: -10,
						text: "X-axis range",
					},
				},
			],
			points: [
				{
					x: new Date("01 Dec 2017").getTime(),
					y: 8607.55,
					marker: {
						size: 8,
						fillColor: "#fff",
						strokeColor: "red",
						radius: 2,
						cssClass: "apexcharts-custom-class",
					},
					label: {
						borderColor: "#f34e4e",
						offsetY: 0,
						style: {
							color: "#fff",
							background: "#f34e4e",
						},

						text: "Point Annotation",
					},
				},
				{
					x: new Date("08 Dec 2017").getTime(),
					y: 9340.85,
					marker: {
						size: 0,
					},
					image: {
						path: logosm,
						width: 40,
						height: 40,
					},
				},
			],
		},
		dataLabels: {
			enabled: false,
		},
		stroke: {
			curve: "straight",
		},
		colors: LinewithAnnotationsColors,
		grid: {
			padding: {
				right: 30,
				left: 20,
			},
		},
		title: {
			text: "Line with Annotations",
			align: "left",
			style: {
				fontWeight: 500,
			},
		},
		labels: allseries.seriesData.monthDataSeries1.dates,
		xaxis: {
			type: "datetime",
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#linewithannotations"), options)
  		chart.render()
	})
</script>

<div id="linewithannotations" class="apex-charts" dir="ltr"></div>
