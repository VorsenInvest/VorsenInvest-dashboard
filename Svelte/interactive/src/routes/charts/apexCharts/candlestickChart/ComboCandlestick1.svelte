<script>
    import { onMount } from "svelte";
	export let dataColors;
	import { browser } from "$app/environment"
    import data from './series'

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
        const chartCandlestickBasicColors = getChartColorsArray(dataColors);

        const options = {
        chart: {
            height: 150,
            type: 'bar',
            brush: {
                enabled: true,
                target: 'candles'
            },
            selection: {
                enabled: true,
                xaxis: {
                    min: new Date('20 Jan 2017').getTime(),
                    max: new Date('10 Dec 2017').getTime()
                },
                fill: {
                    color: '#ccc',
                    opacity: 0.4
                },
                stroke: {
                    color: '#0d47a1',
                }
            },
        },
        series : [
            {
                name: "volume",
                data: data.seriesDataLinear,
            },
        ],
        dataLabels: {
            enabled: false
        },
        plotOptions: {
            bar: {
                columnWidth: '80%',
                colors: {
                    ranges: [{
                        from: -1000,
                        to: 0,
                        color: chartCandlestickBasicColors[1]
                    }, {
                        from: 1,
                        to: 10000,
                        color: chartCandlestickBasicColors[0]
                    }],

                },
            }
        },
        stroke: {
            width: 0
        },
        xaxis: {
            type: 'datetime',
            axisBorder: {
                offsetX: 13
            }
        },
        yaxis: {
            labels: {
                show: false
            },
        },
    };
    const chart = new ApexCharts(document.querySelector("#combocandlestickchart1"), options)
    chart.render()
	})
</script>

<div id="combocandlestickchart1" class="apex-charts" dir="ltr"></div>