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

	var dumbbellChartColors = getChartColorsArray(dataColors);

	const options = {
        series: [
            {
                data: [
                    {
                        x: 'Operations',
                        y: [2800, 4500]
                    },
                    {
                        x: 'Customer Success',
                        y: [3200, 4100]
                    },
                    {
                        x: 'Engineering',
                        y: [2950, 7800]
                    },
                    {
                        x: 'Marketing',
                        y: [3000, 4600]
                    },
                    {
                        x: 'Product',
                        y: [3500, 4100]
                    },
                    {
                        x: 'Data Science',
                        y: [4500, 6500]
                    },
                    {
                        x: 'Sales',
                        y: [4100, 5600]
                    }
                ]
            }
        ],
        chart: {
            height: 350,
            type: 'rangeBar',
            zoom: {
                enabled: false
            }
        },
        colors: ['#EC7D31', '#36BDCB'],
        plotOptions: {
            bar: {
                horizontal: true,
                isDumbbell: true,
                dumbbellColors: dumbbellChartColors
            }
        },
        title: {
            text: 'Paygap Disparity'
        },
        legend: {
            show: true,
            showForSingleSeries: true,
            position: 'top',
            horizontalAlign: 'left',
            customLegendItems: ['Female', 'Male']
        },
        fill: {
            type: 'gradient',
            gradient: {
                gradientToColors: ['#36BDCB'],
                inverseColors: false,
                stops: [0, 100]
            }
        },
        grid: {
            xaxis: {
                lines: {
                    show: true
                }
            },
            yaxis: {
                lines: {
                    show: false
                }
            }
        }
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#dumbbellChart"), options)
  		chart.render()
	})
</script>

<div id="dumbbellChart" class="apex-charts" dir="ltr"></div>
