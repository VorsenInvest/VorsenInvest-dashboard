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

	var chartBasicRangeAreaColors = getChartColorsArray(dataColors);
	const options = {
		series: [
            {
                name: 'New York Temperature',
                data: [
                    {
                        x: 'Jan',
                        y: [-2, 4]
                    },
                    {
                        x: 'Feb',
                        y: [-1, 6]
                    },
                    {
                        x: 'Mar',
                        y: [3, 10]
                    },
                    {
                        x: 'Apr',
                        y: [8, 16]
                    },
                    {
                        x: 'May',
                        y: [13, 22]
                    },
                    {
                        x: 'Jun',
                        y: [18, 26]
                    },
                    {
                        x: 'Jul',
                        y: [21, 29]
                    },
                    {
                        x: 'Aug',
                        y: [21, 28]
                    },
                    {
                        x: 'Sep',
                        y: [17, 24]
                    },
                    {
                        x: 'Oct',
                        y: [11, 18]
                    },
                    {
                        x: 'Nov',
                        y: [6, 12]
                    },
                    {
                        x: 'Dec',
                        y: [1, 7]
                    }
                ]
            }
        ],
        chart: {
            height: 350,
            type: 'rangeArea'
        },
        stroke: {
            curve: 'straight'
        },
        title: {
            text: 'New York Temperature (all year round)'
        },
        markers: {
            hover: {
                sizeOffset: 5
            }
        },
        dataLabels: {
            enabled: false
        },
        yaxis: {
            labels: {
                formatter: (val) => {
                    return val + '°C'
                }
            }
        },
		colors: chartBasicRangeAreaColors,
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#basicrangeareachart"), options)
  		chart.render()
	})
</script>

<div id="basicrangeareachart" class="apex-charts" dir="ltr"></div>
