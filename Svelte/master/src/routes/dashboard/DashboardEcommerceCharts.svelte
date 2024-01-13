<script>
    import {onMount} from 'svelte';
    export let dataColors;
    import { browser } from "$app/environment";
    import { themeChangeEvent } from "$lib/eventBus";
    let chart;
    // ["--vz-primary", "--vz-success" , "--vz-danger" ]
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

    const linechartcustomerColors = getChartColorsArray(dataColors);

    const THEME_CHART_COLORS = {
		default: ["--vz-primary", "--vz-success" , "--vz-danger" ],
		minimal: ["--vz-light", "--vz-primary", "--vz-info"],
		saas: ["--vz-success", "--vz-info", "--vz-danger"],
		modern: ["--vz-warning", "--vz-primary", "--vz-success"],
		interactive: ["--vz-info", "--vz-primary", "--vz-danger"],
		creative: ["--vz-warning", "--vz-primary", "--vz-danger"],
		corporate: ["--vz-light", "--vz-primary", "--vz-secondary"],
		galaxy: ["--vz-secondary", "--vz-primary", "--vz-primary-rgb, 0.50"], 
		classic: ["--vz-light", "--vz-primary", "--vz-secondary"],
		vintage: ["--vz-success", "--vz-primary", "--vz-secondary"],
		material: ["--vz-primary", "--vz-success" , "--vz-danger" ],
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
			console.log("-->",newTheme,newColors,THEME_CHART_COLORS,key)
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
        series: [
            {
                name: "Orders",
                type: "area",
                data: [34, 65, 46, 68, 49, 61, 42, 44, 78, 52, 63, 67],
            },
            {
                name: "Earnings",
                type: "bar",
                data: [
                    89.25, 98.58, 68.74, 108.87, 77.54, 84.03, 51.24, 28.57,
                    92.57, 42.36, 88.51, 36.57,
                ],
            },
            {
                name: "Refunds",
                type: "line",
                data: [8, 12, 7, 17, 21, 11, 5, 9, 7, 29, 12, 35],
            },
        ],
        chart: {
            height: 370,
            type: "line",
            toolbar: {
                show: false,
            },
        },
        stroke: {
            curve: "straight",
            dashArray: [0, 0, 8],
            width: [2, 0, 2.2],
        },
        fill: {
            opacity: [0.1, 0.9, 1],
        },
        markers: {
            size: [0, 0, 0],
            strokeWidth: 2,
            hover: {
                size: 4,
            },
        },
        xaxis: {
            categories: [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ],
            axisTicks: {
                show: false,
            },
            axisBorder: {
                show: false,
            },
        },
        grid: {
            show: true,
            xaxis: {
                lines: {
                    show: true,
                },
            },
            yaxis: {
                lines: {
                    show: false,
                },
            },
            padding: {
                top: 0,
                right: -2,
                bottom: 15,
                left: 10,
            },
        },
        legend: {
            show: true,
            horizontalAlign: "center",
            offsetX: 0,
            offsetY: -5,
            markers: {
                width: 9,
                height: 9,
                radius: 6,
            },
            itemMargin: {
                horizontal: 10,
                vertical: 0,
            },
        },
        plotOptions: {
            bar: {
                columnWidth: "30%",
                barHeight: "70%",
            },
        },
        colors: linechartcustomerColors,
        tooltip: {
            shared: true,
            y: [
                {
                    formatter: function (y) {
                        if (typeof y !== "undefined") {
                            return y.toFixed(0);
                        }
                        return y;
                    },
                },
                {
                    formatter: function (y) {
                        if (typeof y !== "undefined") {
                            return "$" + y.toFixed(2) + "k";
                        }
                        return y;
                    },
                },
                {
                    formatter: function (y) {
                        if (typeof y !== "undefined") {
                            return y.toFixed(0) + " Sales";
                        }
                        return y;
                    },
                },
            ],
        },
    };
	onMount(() => {
		chart = new ApexCharts(document.querySelector("#dashboardecommercechart"), options)
  		chart.render()
	})
</script>

<div id="dashboardecommercechart" class="apex-charts" dir="ltr"></div>
