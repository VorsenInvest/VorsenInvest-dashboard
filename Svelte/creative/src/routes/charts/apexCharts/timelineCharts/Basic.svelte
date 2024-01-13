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

	onMount(() => {
		var chartTimelineBasicColors = getChartColorsArray(dataColors);

		const options = {
			chart: {
				toolbar: {
					show: !1,
				},
				type: "rangeBar",
				height: 350,
			},
			series: [
				{
					data: [
						{
							x: "Code",
							y: [
								new Date("2019-03-02").getTime(),
								new Date("2019-03-04").getTime(),
							],
						},
						{
							x: "Test",
							y: [
								new Date("2019-03-04").getTime(),
								new Date("2019-03-08").getTime(),
							],
						},
						{
							x: "Validation",
							y: [
								new Date("2019-03-08").getTime(),
								new Date("2019-03-12").getTime(),
							],
						},
						{
							x: "Deployment",
							y: [
								new Date("2019-03-12").getTime(),
								new Date("2019-03-18").getTime(),
							],
						},
					],
				},
			],
			plotOptions: {
				bar: {
					horizontal: !0,
				},
			},
			xaxis: {
				type: "datetime",
			},
			colors: chartTimelineBasicColors,
		};
		const chart = new ApexCharts(
			document.querySelector("#basictimelinechart"),
			options
		);
		chart.render();
	});
</script>

<div id="basictimelinechart" class="apex-charts" dir="ltr" />
