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

    var chartSyncingColors = getChartColorsArray(dataColors);

    function generateDayWiseTimeSeriesline(baseval, count, yrange) {
        var i = 0;
        var series = [];
        while (i < count) {
            var x = baseval;
            var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;

            series.push([x, y]);
            baseval += 86400000;
            i++;
        }
        return series;
    }

    var options = {
        chart: {
            id: 'fb',
            group: 'social',
            type: 'line',
            height: 160,
            toolbar: {
                show: false
            },
        },
        series : [{
        data: generateDayWiseTimeSeriesline(new Date('11 Feb 2017').getTime(), 20, {
            min: 10,
            max: 60
            })
        }],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'straight',
            width: 3,
        },
        colors: chartSyncingColors,
        markers: {
            size: 4,
            hover: {
                size: 6
            }
        },
        tooltip: {
            followCursor: false,
            x: {
                show: false
            },
            marker: {
                show: false
            },
            y: {
                title: {
                    formatter: function () {
                        return '';
                    }
                }
            }
        },
        grid: {
            clipMarkers: false
        },
        yaxis: {
            tickAmount: 2
        },
        xaxis: {
            type: 'datetime'
        }
    };

    onMount(() => {
		const chart = new ApexCharts(document.querySelector("#Syncingline"), options)
  		chart.render()
	})
</script>
<div id="Syncingline" class="apex-charts" dir="ltr"></div>
