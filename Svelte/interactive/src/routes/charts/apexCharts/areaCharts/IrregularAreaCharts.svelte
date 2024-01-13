<script>
	import {onMount} from 'svelte';
	import allseries from "../series";
	import dayjs from "dayjs";
	import { browser } from "$app/environment"
	export let dataColors;

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

	var BasicAreaChartsColors = getChartColorsArray(dataColors);

	var ts1 = 1388534400000;
	var ts2 = 1388620800000;
	var ts3 = 1389052800000;

	var dataSet = [[], [], []];
	var i = 0;
	var j = 0;
	var k = 0;
	var innerArr = [];
	var innerArr1 = [];
	var innerArr3 = [];

	for (i = 0; i < 12; i++) {
		ts1 = ts1 + 86400000;
		innerArr = [ts1, allseries.dataSeries[2][i].value];
		dataSet[0].push(innerArr);
	}
	for (j = 0; j < 18; j++) {
		ts2 = ts2 + 86400000;
		innerArr1 = [ts2, allseries.dataSeries[1][j].value];
		dataSet[1].push(innerArr1);
	}
	for (k = 0; k < 12; k++) {
		ts3 = ts3 + 86400000;
		innerArr3 = [ts3, allseries.dataSeries[0][k].value];
		dataSet[2].push(innerArr3);
	}

	function convertTime(todaydate) {
		const datwe = dayjs(todaydate).format("DD MMM YYYY");
		return datwe;
	}

	var options = {
		chart: {
			type: "area",
			stacked: false,
			height: 350,
			zoom: {
				enabled: false,
			},
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "PRODUCT A",
				data: dataSet[0],
			},
			{
				name: "PRODUCT B",
				data: dataSet[1],
			},
			{
				name: "PRODUCT C",
				data: dataSet[2],
			},
		],
		dataLabels: {
			enabled: false,
		},
		markers: {
			size: 0,
		},
		fill: {
			type: "gradient",
			gradient: {
				shadeIntensity: 1,
				inverseColors: false,
				opacityFrom: 0.45,
				opacityTo: 0.05,
				stops: [20, 100, 100, 100],
			},
		},
		yaxis: {
			labels: {
				style: {
					colors: "#8e8da4",
				},
				offsetX: 0,
				formatter: function (val) {
					return (val / 1000000).toFixed(2);
				},
			},
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false,
			},
		},
		xaxis: {
			type: "datetime",
			tickAmount: 8,
			min: new Date("01/01/2014").getTime(),
			max: new Date("01/20/2014").getTime(),
			labels: {
				rotate: -15,
				rotateAlways: true,
				formatter: function (val, timestamp) {
					return convertTime(timestamp);
				},
			},
		},
		title: {
			text: "Irregular Data in Time Series",
			align: "left",
			offsetX: 14,
			style: {
				fontWeight: 500,
			},
		},
		tooltip: {
			shared: true,
		},
		legend: {
			position: "top",
			horizontalAlign: "right",
			offsetX: -10,
		},
		colors: BasicAreaChartsColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#irregularareacharts"), options)
  		chart.render()
	})
</script>

<div id="irregularareacharts" class="apex-charts" dir="ltr"></div>
