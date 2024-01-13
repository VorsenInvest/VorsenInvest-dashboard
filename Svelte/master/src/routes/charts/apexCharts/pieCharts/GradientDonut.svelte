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

    var chartPieGradientColors = getChartColorsArray(dataColors);

    var options = {
        chart: {
            height: 300,
            type: "donut",
        },
        series: [44, 55, 41, 17, 15],
        plotOptions: {
            pie: {
                startAngle: -90,
                endAngle: 270,
            },
        },
        dataLabels: {
            enabled: false,
        },
        fill: {
            type: "gradient",
        },
        legend: {
            position: "bottom",
            formatter: function (val, opts) {
                return val + " - " + opts.w.globals.series[opts.seriesIndex];
            },
        },
        title: {
            text: "Gradient Donut with custom Start-angle",
            style: {
                fontWeight: 500,
            },
        },
        colors: chartPieGradientColors,
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#gradientdountpiechart"), options)
  		chart.render()
	})
</script>

<div id="gradientdountpiechart" class="apex-charts" dir="ltr"></div>
