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
const donutchartportfolioColors = getChartColorsArray(dataColors);
    
    var options = {
        labels: ["Bitcoin", "Ethereum", "Litecoin", "Dash"],
        chart: {
            type: "donut",
            height: 224,
        },
        series : [19405, 40552, 15824, 30635],
        plotOptions: {
            pie: {
                size: 100,
                offsetX: 0,
                offsetY: 0,
                donut: {
                    size: "70%",
                    labels: {
                        show: true,
                        name: {
                            show: true,
                            fontSize: '18px',
                            offsetY: -5,
                        },
                        value: {
                            show: true,
                            fontSize: '20px',
                            color: '#343a40',
                            fontWeight: 500,
                            offsetY: 5,
                            formatter: function (val) {
                                return "$" + val;
                            }
                        },
                        total: {
                            show: true,
                            fontSize: '13px',
                            label: 'Total value',
                            color: '#9599ad',
                            fontWeight: 500,
                            formatter: function (w) {
                                return "$" + w.globals.seriesTotals.reduce(function (a, b) {
                                    return a + b;
                                }, 0);
                            }
                        }
                    }
                },
            },
        },
        dataLabels: {
            enabled: false,
        },
        legend: {
            show: false,
        },
        yaxis: {
            labels: {
                formatter: function (value) {
                    return "$" + value;
                }
            }
        },
        stroke: {
            lineCap: "round",
            width: 2
        },
        colors: donutchartportfolioColors,
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#myportfoliochart"), options)
  		chart.render()
	})
</script>

<div id="myportfoliochart" class="apex-charts" dir="ltr"></div>