<script>
	import {onMount} from 'svelte'; 
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


	const barchartCountriesColors = getChartColorsArray(dataColors);

	var options = {
		chart: {
			type: 'bar',
			height: 436,
			toolbar: {
				show: false
			}
		},
		series: [
			{
				data: [1010, 1640, 490, 1255, 1050, 689, 800, 420, 1085, 589],
				name: 'Sessions'
			}
		],
		plotOptions: {
			bar: {
				borderRadius: 4,
				horizontal: true,
				distributed: true,
				dataLabels: {
					position: 'top'
				}
			}
		},
		colors: barchartCountriesColors,
		dataLabels: {
			enabled: true,
			offsetX: 32,
			style: {
				fontSize: '12px',
				fontWeight: 400,
				colors: ['#adb5bd']
			}
		},

		legend: {
			show: false
		},
		grid: {
			show: false
		},
		xaxis: {
			categories: [
				'India',
				'United States',
				'China',
				'Indonesia',
				'Russia',
				'Bangladesh',
				'Canada',
				'Brazil',
				'Vietnam',
				'UK'
			]
		}
	};
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#countrieschart"), options)
  		chart.render()
	})
</script>

<div id="countrieschart" class="apex-charts" dir="ltr"></div>