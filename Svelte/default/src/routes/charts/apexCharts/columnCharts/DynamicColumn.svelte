<script>
	import { onMount } from "svelte";
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

	const shuffleArray = (array1) => {
		for (var i = array1.length - 1; i > 0; i--) {
			var j = Math.floor(Math.random() * (i + 1));
			var temp = array1[i];
			array1[i] = array1[j];
			array1[j] = temp;
		}
		return array1;
	};

	onMount(() => {
		var chartColumnColors = getChartColorsArray(dataColors);
		const colors = chartColumnColors;

		const arrayData = [
			{
				y: 400,
				quarters: [
					{
						x: "Q1",
						y: 120,
					},
					{
						x: "Q2",
						y: 90,
					},
					{
						x: "Q3",
						y: 100,
					},
					{
						x: "Q4",
						y: 90,
					},
				],
			},
			{
				y: 430,
				quarters: [
					{
						x: "Q1",
						y: 120,
					},
					{
						x: "Q2",
						y: 110,
					},
					{
						x: "Q3",
						y: 90,
					},
					{
						x: "Q4",
						y: 110,
					},
				],
			},
			{
				y: 448,
				quarters: [
					{
						x: "Q1",
						y: 70,
					},
					{
						x: "Q2",
						y: 100,
					},
					{
						x: "Q3",
						y: 140,
					},
					{
						x: "Q4",
						y: 138,
					},
				],
			},
			{
				y: 470,
				quarters: [
					{
						x: "Q1",
						y: 150,
					},
					{
						x: "Q2",
						y: 60,
					},
					{
						x: "Q3",
						y: 190,
					},
					{
						x: "Q4",
						y: 70,
					},
				],
			},
			{
				y: 540,
				quarters: [
					{
						x: "Q1",
						y: 120,
					},
					{
						x: "Q2",
						y: 120,
					},
					{
						x: "Q3",
						y: 130,
					},
					{
						x: "Q4",
						y: 170,
					},
				],
			},
			{
				y: 580,
				quarters: [
					{
						x: "Q1",
						y: 170,
					},
					{
						x: "Q2",
						y: 130,
					},
					{
						x: "Q3",
						y: 120,
					},
					{
						x: "Q4",
						y: 160,
					},
				],
			},
		];

		const makeData = () => {
			var dataSet = shuffleArray(arrayData);

			var dataYearSeries = [
				{
					x: "2011",
					y: dataSet[0].y,
					color: colors[0],
					quarters: dataSet[0].quarters,
				},
				{
					x: "2012",
					y: dataSet[1].y,
					color: colors[1],
					quarters: dataSet[1].quarters,
				},
				{
					x: "2013",
					y: dataSet[2].y,
					color: colors[2],
					quarters: dataSet[2].quarters,
				},
				{
					x: "2014",
					y: dataSet[3].y,
					color: colors[3],
					quarters: dataSet[3].quarters,
				},
				{
					x: "2015",
					y: dataSet[4].y,
					color: colors[4],
					quarters: dataSet[4].quarters,
				},
				{
					x: "2016",
					y: dataSet[5].y,
					color: colors[5],
					quarters: dataSet[5].quarters,
				},
			];

			return dataYearSeries;
		};

		const options = {
			chart: {
				id: "barYear",
				type: "bar",
				height: 330,
				width: "100%",
			},
			series: [
				{
					data: makeData(),
				},
			],
			plotOptions: {
				bar: {
					distributed: true,
					horizontal: true,
					barHeight: "75%",
					dataLabels: {
						position: "bottom",
					},
				},
			},
			dataLabels: {
				enabled: true,
				textAnchor: "start",
				style: {
					colors: ["#fff"],
				},
				formatter: function (val, opt) {
					return opt.w.globals.labels[opt.dataPointIndex];
				},
				offsetX: 0,
				dropShadow: {
					enabled: false,
				},
			},

			colors: colors,

			states: {
				normal: {
					filter: {
						type: "desaturate",
					},
				},
				active: {
					allowMultipleDataPointsSelection: true,
					filter: {
						type: "darken",
						value: 1,
					},
				},
			},
			tooltip: {
				x: {
					show: false,
				},
				y: {
					title: {
						formatter: function (val, opts) {
							return opts.w.globals.labels[opts.dataPointIndex];
						},
					},
				},
			},
			title: {
				text: "Yearly Results",
				offsetX: 15,
				style: {
					fontWeight: 600,
				},
			},
			subtitle: {
				text: "(Click on bar to see details)",
				offsetX: 15,
			},
			yaxis: {
				labels: {
					show: false,
				},
			},
		};

		const chart = new ApexCharts(
			document.querySelector("#dynamiccolumn"),
			options
		);
		chart.render();
	});
</script>

<div id="dynamiccolumn" class="apex-charts" dir="ltr" />