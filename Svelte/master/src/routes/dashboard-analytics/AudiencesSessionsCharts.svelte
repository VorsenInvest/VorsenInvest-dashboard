<script>
	import {onDestroy, onMount} from 'svelte'; 
    import { browser } from "$app/environment";
	import { themeChangeEvent } from "$lib/eventBus";
	export let dataColors;
	let chart;

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
			var x = (i + 1).toString() + 'h';
			var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

			series.push({
				x: x,
				y: y
			});
			i++;
		}
		return series;
	}

	const THEME_CHART_COLORS = {
		default: ["--vz-success", "--vz-info"],
		minimal: ["--vz-info", "--vz-primary"],
		modern: ["--vz-success", "--vz-secondary"],
		interactive: ["--vz-info", "--vz-primary"],
		creative: ["--vz-primary", "--vz-success"],
		corporate: ["--vz-secondary", "--vz-primary"],
		galaxy: ["--vz-primary", "--vz-secondary"], 
		classic: ["--vz-primary", "--vz-danger"],
		vintage: ["--vz-success", "--vz-secondary"],
		sass: ["--vz-success", "--vz-info"]
	};

	// Function to find the index of a key
	function findIndexByKey(key) {
		const keys = Object.keys(THEME_CHART_COLORS);
		return keys.indexOf(key);
	}

	// Subscribe to the theme change event
	const unsubscribeEvent = themeChangeEvent.subscribe((newTheme) => {
		// Handle the theme change event
		if(newTheme == null || newTheme == undefined){
			return;
		}
		let key = findIndexByKey(newTheme);
		let newColors;
		if (key >= 0) {
			newColors = THEME_CHART_COLORS[newTheme];
		}
		if (browser) {
			newColors = ( key >= 0) ? getChartColorsArray(newColors) : dataColors;
			setTimeout(() => {
				chart.updateOptions({
					series: [
				{
					name: 'Sat',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Fri',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Thu',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Wed',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Tue',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Mon',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Sun',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				}
					],
					colors: newColors,
				});
			}, 500);
		}
	});
	
	onMount(() => {
		const chartHeatMapBasicColors = getChartColorsArray(dataColors);
		var options = {
			chart: {
				height: 400,
				type: 'heatmap',
				offsetX: 0,
				offsetY: -8,
				toolbar: {
					show: false
				}
			},
			series: [
				{
					name: 'Sat',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Fri',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Thu',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Wed',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Tue',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Mon',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				},
				{
					name: 'Sun',
					data: generateData(18, {
						min: 0,
						max: 90
					})
				}
			],
			plotOptions: {
				heatmap: {
					colorScale: {
						ranges: [
							{
								from: 0,
								to: 50,
								color: chartHeatMapBasicColors[0]
							},
							{
								from: 51,
								to: 100,
								color: chartHeatMapBasicColors[1]
							}
						]
					}
				}
			},
			dataLabels: {
				enabled: false
			},
			legend: {
				show: true,
				horizontalAlign: 'center',
				offsetX: 0,
				offsetY: 20,
				markers: {
					width: 20,
					height: 6,
					radius: 2
				},
				itemMargin: {
					horizontal: 12,
					vertical: 0
				}
			},
			colors: chartHeatMapBasicColors,
			tooltip: {
				y: [
					{
						formatter: function (y) {
							if (typeof y !== 'undefined') {
								return y.toFixed(0) + 'k';
							}
							return y;
						}
					}
				]
			}
		};

		chart = new ApexCharts(document.querySelector("#audiencesessionchart"), options)
  		chart.render()
	})

	// Ensure to unsubscribe to avoid memory leaks
	onDestroy(() => {
		unsubscribeEvent();
	});
</script>

<div id="audiencesessionchart" class="apex-charts" dir="ltr"></div>
