<script>
    import { onDestroy, onMount } from "svelte";
    export let dataColors;
    import { browser } from "$app/environment";
    import { themeChangeEvent } from "$lib/eventBus";
    let chart;

    function getChartColorsArray(colors) {
        if (browser) {
            return colors.map(function (value) {
                var newValue = value.replace(" ", "");
                if (newValue.indexOf(",") === -1) {
                    var color = getComputedStyle(
                        document.documentElement,
                    ).getPropertyValue(newValue);
                    if (color.indexOf("#") !== -1)
                        color = color.replace(" ", "");
                    if (color) return color;
                    else return newValue;
                } else {
                    var val = value.split(",");
                    if (val.length === 2) {
                        var rgbaColor = getComputedStyle(
                            document.documentElement,
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

    const THEME_CHART_COLORS = {
		default: ["--vz-primary", "--vz-info", "--vz-warning", "--vz-success"],
		minimal: ["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.65", "--vz-primary-rgb, 0.50"],
		interactive: ["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.65", "--vz-primary-rgb, 0.50"],
		corporate: ["--vz-primary", "--vz-secondary", "--vz-info", "--vz-success"],
		galaxy: ["--vz-primary", "--vz-primary-rgb, 0.85", "--vz-primary-rgb, 0.65", "--vz-primary-rgb, 0.50"], 
		creative: ["--vz-primary", "--vz-secondary", "--vz-info"],
		classic: ["--vz-primary", "--vz-info", "--vz-warning", "--vz-success"],
		modern: ["--vz-primary", "--vz-info", "--vz-warning", "--vz-success"],
		vintage: ["--vz-primary", "--vz-info", "--vz-warning", "--vz-success"],
		saas: ["--vz-primary", "--vz-info", "--vz-warning", "--vz-success"],
		material: ["--vz-primary", "--vz-info", "--vz-warning", "--vz-success"],
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
					colors: newColors,
				});
			}, 500);
		}
	});

    var options = {
        labels: ["Bitcoin", "Ethereum", "Litecoin", "Dash"],
        chart: {
            type: "donut",
            height: 224,
        },
        series: [19405, 40552, 15824, 30635],
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
                            fontSize: "18px",
                            offsetY: -5,
                        },
                        value: {
                            show: true,
                            fontSize: "20px",
                            color: "#343a40",
                            fontWeight: 500,
                            offsetY: 5,
                            formatter: function (val) {
                                return "$" + val;
                            },
                        },
                        total: {
                            show: true,
                            fontSize: "13px",
                            label: "Total value",
                            color: "#9599ad",
                            fontWeight: 500,
                            formatter: function (w) {
                                return (
                                    "$" +
                                    w.globals.seriesTotals.reduce(function (
                                        a,
                                        b,
                                    ) {
                                        return a + b;
                                    }, 0)
                                );
                            },
                        },
                    },
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
                },
            },
        },
        stroke: {
            lineCap: "round",
            width: 2,
        },
        colors: donutchartportfolioColors,
    };
    onMount(() => {
         chart = new ApexCharts(
            document.querySelector("#portfoliochart"),
            options,
        );
        chart.render();
    });

    onDestroy(() =>{
        unsubscribeEvent();
    })
</script>

<div id="portfoliochart" class="apex-charts" dir="ltr"></div>
