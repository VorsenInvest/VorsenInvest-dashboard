<script>
	import { onMount } from "svelte";
	import dayjs from "dayjs";
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

	function convertTime(todaydate) {
		const datwe = dayjs(todaydate);
		return datwe;
	}

	onMount(() => {
		var chartTimelineColors = getChartColorsArray(dataColors);

		const options = {
			chart: {
				height: 350,
				type: "rangeBar",
				toolbar: {
					show: false,
				},
			},
			series: [
				{
					data: [
						{
							x: "Analysis",
							y: [
								new Date("2019-02-27").getTime(),
								new Date("2019-03-04").getTime(),
							],
							fillColor: chartTimelineColors[0],
						},
						{
							x: "Design",
							y: [
								new Date("2019-03-04").getTime(),
								new Date("2019-03-08").getTime(),
							],
							fillColor: chartTimelineColors[1],
						},
						{
							x: "Coding",
							y: [
								new Date("2019-03-07").getTime(),
								new Date("2019-03-10").getTime(),
							],
							fillColor: chartTimelineColors[2],
						},
						{
							x: "Testing",
							y: [
								new Date("2019-03-08").getTime(),
								new Date("2019-03-12").getTime(),
							],
							fillColor: chartTimelineColors[3],
						},
						{
							x: "Deployment",
							y: [
								new Date("2019-03-12").getTime(),
								new Date("2019-03-17").getTime(),
							],
							fillColor: chartTimelineColors[4],
						},
					],
				},
			],
			plotOptions: {
				bar: {
					horizontal: true,
					distributed: true,
					dataLabels: {
						hideOverflowingLabels: false,
					},
				},
			},
			dataLabels: {
				enabled: true,
				formatter: function (val, opts) {
					var label = opts.w.globals.labels[opts.dataPointIndex];
					var a = convertTime(val[0]);
					var b = convertTime(val[1]);
					var diff = b.diff(a, "days");
					return label + ": " + diff + (diff > 1 ? " days" : " day");
				},
			},
			xaxis: {
				type: "datetime",
			},
			yaxis: {
				show: true,
			},
		};
		const chart = new ApexCharts(
			document.querySelector("#differentcolorchart"),
			options
		);
		chart.render();
	});
</script>

<div id="differentcolorchart" class="apex-charts" dir="ltr" />
