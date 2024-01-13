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

	var areachartNegativeColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: "area",
			height: 350,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "North",
				data: [
					{
						x: 1996,
						y: 322,
					},
					{
						x: 1997,
						y: 324,
					},
					{
						x: 1998,
						y: 329,
					},
					{
						x: 1999,
						y: 342,
					},
					{
						x: 2000,
						y: 348,
					},
					{
						x: 2001,
						y: 334,
					},
					{
						x: 2002,
						y: 325,
					},
					{
						x: 2003,
						y: 316,
					},
					{
						x: 2004,
						y: 318,
					},
					{
						x: 2005,
						y: 330,
					},
					{
						x: 2006,
						y: 355,
					},
					{
						x: 2007,
						y: 366,
					},
					{
						x: 2008,
						y: 337,
					},
					{
						x: 2009,
						y: 352,
					},
					{
						x: 2010,
						y: 377,
					},
					{
						x: 2011,
						y: 383,
					},
					{
						x: 2012,
						y: 344,
					},
					{
						x: 2013,
						y: 366,
					},
					{
						x: 2014,
						y: 389,
					},
					{
						x: 2015,
						y: 334,
					},
				],
			},
			{
				name: "South",
				data: [
					{
						x: 1996,
						y: 162,
					},
					{
						x: 1997,
						y: 90,
					},
					{
						x: 1998,
						y: 50,
					},
					{
						x: 1999,
						y: 77,
					},
					{
						x: 2000,
						y: 35,
					},
					{
						x: 2001,
						y: -45,
					},
					{
						x: 2002,
						y: -88,
					},
					{
						x: 2003,
						y: -120,
					},
					{
						x: 2004,
						y: -156,
					},
					{
						x: 2005,
						y: -123,
					},
					{
						x: 2006,
						y: -88,
					},
					{
						x: 2007,
						y: -66,
					},
					{
						x: 2008,
						y: -45,
					},
					{
						x: 2009,
						y: -29,
					},
					{
						x: 2010,
						y: -45,
					},
					{
						x: 2011,
						y: -88,
					},
					{
						x: 2012,
						y: -132,
					},
					{
						x: 2013,
						y: -146,
					},
					{
						x: 2014,
						y: -169,
					},
					{
						x: 2015,
						y: -184,
					},
				],
			},
		],
		dataLabels: {
			enabled: false,
		},
		stroke: {
			curve: "straight",
		},
		title: {
			text: "Area with Negative Values",
			align: "left",

			style: {
				fontSize: "14px",
				fontWeight: 500,
			},
		},
		xaxis: {
			type: "datetime",
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false,
			},
		},
		colors: areachartNegativeColors,
		yaxis: {
			tickAmount: 4,
			floating: false,

			labels: {
				style: {
					colors: "#038edc",
				},
				offsetY: -7,
				offsetX: 0,
			},
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false,
			},
		},
		fill: {
			opacity: 0.5,
		},
		tooltip: {
			x: {
				format: "yyyy",
			},
			fixed: {
				enabled: false,
				position: "topRight",
			},
		},
		grid: {
			yaxis: {
				lines: {
					offsetX: -30,
				},
			},
			padding: {
				left: 20,
			},
		},
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#negativeareachart"), options)
  		chart.render()
	})
</script>

<div id="negativeareachart" class="apex-charts" dir="ltr"></div>
