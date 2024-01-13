<script>
	import { onMount } from "svelte";
	export let dataColors;
	import { browser } from "$app/environment";
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

	const areachartSalesColors = getChartColorsArray(dataColors);
	var options = {
		chart: {
			type: "bar",
			height: 341,
			toolbar: {
				show: false,
			},
		},
		series: [
			{
				name: "Goal",
				data: [37],
			},
			{
				name: "Pending Forcast",
				data: [12],
			},
			{
				name: "Revenue",
				data: [18],
			},
		],
		plotOptions: {
			bar: {
				horizontal: false,
				columnWidth: "65%",
			},
		},
		stroke: {
			show: true,
			width: 5,
			colors: ["transparent"],
		},
		xaxis: {
			categories: [""],
			axisTicks: {
				show: false,
				borderType: "solid",
				color: "#78909C",
				height: 6,
				offsetX: 0,
				offsetY: 0,
			},
			title: {
				text: "Total Forecasted Value",
				offsetX: 0,
				offsetY: -30,
				style: {
					color: "#78909C",
					fontSize: "12px",
					fontWeight: 400,
				},
			},
		},
		yaxis: {
			labels: {
				formatter: function (value) {
					return "$" + value + "k";
				},
			},
			tickAmount: 4,
			min: 0,
		},
		fill: {
			opacity: 1,
		},
		legend: {
			show: true,
			position: "bottom",
			horizontalAlign: "center",
			fontWeight: 500,
			offsetX: 0,
			offsetY: -14,
			itemMargin: {
				horizontal: 8,
				vertical: 0,
			},
			markers: {
				width: 10,
				height: 10,
			},
		},
		colors: areachartSalesColors,
	};
	onMount(() => {
		const chart = new ApexCharts(
			document.querySelector("#dashboardcrmchart"),
			options
		);
		chart.render();
	});
</script>

<div id="dashboardcrmchart" class="apex-charts" dir="ltr" />
