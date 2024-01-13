<script>
    import {onMount} from 'svelte';
	import { browser } from "$app/environment"
	export let dataColors;

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

    var chartColumnDistributedColors = getChartColorsArray(dataColors);
    var options = {
        chart: {
            height: 350,
            type: 'bar',
            toolbar: {
                show: false,
            }
        },
        series : [{
            name: "sales",
            data: [{
                x: '2020/01/01',
                y: 400
            }, {
                x: '2020/04/01',
                y: 430
            }, {
                x: '2020/07/01',
                y: 448
            }, {
                x: '2020/10/01',
                y: 470
            }, {
                x: '2021/01/01',
                y: 540
            }, {
                x: '2021/04/01',
                y: 580
            }, {
                x: '2021/07/01',
                y: 690
            }, {
                x: '2021/10/01',
                y: 690
            }]
        }],
        colors: chartColumnDistributedColors,
        plotOptions: {
            bar: {
                horizontal: false,
                columnWidth: '45%',
            }
        },
        dataLabels: {
            enabled: true
        },
        legend: {
            show: false
        },
        xaxis: {
            type: 'category',
            group: {
                style: {
                    fontSize: '10px',
                    fontWeight: 700
                },
                groups: [
                    { title: '2020', cols: 4 },
                    { title: '2021', cols: 4 }
                ]
            }
        },
        title: {
            text: 'Grouped Labels on the X-axis',
            style: {
                fontWeight: 500,
            },
        },
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#columngrouplabelchart"), options)
  		chart.render()
	})
</script>

<div id="columngrouplabelchart" class="apex-charts" dir="ltr"></div>