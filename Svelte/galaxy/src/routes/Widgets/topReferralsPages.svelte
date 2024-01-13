<script>
	import { onMount } from 'svelte';
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
	function generateData(count, yrange) {
		var i = 0;
		var series = [];
		while (i < count) {
			var x = 'w' + (i + 1).toString();
			var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

			series.push({
				x: x,
				y: y
			});
			i++;
		}
		return series;
	}
	
	onMount(() => {
		const chartHeatMapColors = getChartColorsArray(dataColors);

		const options = {
			chart: {
				height: 350,
				type: 'heatmap',
				toolbar: {
					show: false
				}
			},
			series: [
				{
					name: 'Jan',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				},
				{
					name: 'Feb',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				},
				{
					name: 'Mar',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				},
				{
					name: 'Apr',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				},
				{
					name: 'May',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				},
				{
					name: 'Jun',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				},
				{
					name: 'Jul',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				},
				{
					name: 'Aug',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				},
				{
					name: 'Sep',
					data: generateData(20, {
						min: -30,
						max: 55
					})
				}
			],
			dataLabels: {
				enabled: false
			},
			legend: {
				show: false
			},
			stroke: {
				width: 1
			},
			plotOptions: {
				heatmap: {
					shadeIntensity: 0.5,
					radius: 0,
					useFillColorAsStroke: true,
					dataLabels: {
						enabled: false
					},
					colorScale: {
						ranges: [
							{
								from: -30,
								to: 5,
								name: 'Low',
								color: chartHeatMapColors[0]
							},
							{
								from: 6,
								to: 20,
								name: 'Medium',
								color: chartHeatMapColors[1]
							},
							{
								from: 21,
								to: 45,
								name: 'High',
								color: chartHeatMapColors[2]
							},
							{
								from: 46,
								to: 55,
								name: 'Extreme',
								color: chartHeatMapColors[3]
							}
						]
					}
				}
			}
		};
		const chart = new ApexCharts(document.querySelector("#topreferralspageschart"), options)
  		chart.render()
	})
</script>

<div id="topreferralspageschart" class="apex-charts" dir="ltr"></div>
