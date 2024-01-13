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

    var chartMultiSeriesColors = getChartColorsArray(dataColors);
    const options = {
        chart: {
            height: 350,
            type: "rangeBar",
            toolbar: {
                show: false,
            },
        },
        series: [
            // George Washington
            {
                name: "George Washington",
                data: [
                    {
                        x: "President",
                        y: [
                            new Date(1789, 3, 30).getTime(),
                            new Date(1797, 2, 4).getTime(),
                        ],
                    },
                ],
            },
            // John Adams
            {
                name: "John Adams",
                data: [
                    {
                        x: "President",
                        y: [
                            new Date(1797, 2, 4).getTime(),
                            new Date(1801, 2, 4).getTime(),
                        ],
                    },
                    {
                        x: "Vice President",
                        y: [
                            new Date(1789, 3, 21).getTime(),
                            new Date(1797, 2, 4).getTime(),
                        ],
                    },
                ],
            },
            // Thomas Jefferson
            {
                name: "Thomas Jefferson",
                data: [
                    {
                        x: "President",
                        y: [
                            new Date(1801, 2, 4).getTime(),
                            new Date(1809, 2, 4).getTime(),
                        ],
                    },
                    {
                        x: "Vice President",
                        y: [
                            new Date(1797, 2, 4).getTime(),
                            new Date(1801, 2, 4).getTime(),
                        ],
                    },
                    {
                        x: "Secretary of State",
                        y: [
                            new Date(1790, 2, 22).getTime(),
                            new Date(1793, 11, 31).getTime(),
                        ],
                    },
                ],
            },
            // Aaron Burr
            {
                name: "Aaron Burr",
                data: [
                    {
                        x: "Vice President",
                        y: [
                            new Date(1801, 2, 4).getTime(),
                            new Date(1805, 2, 4).getTime(),
                        ],
                    },
                ],
            },
            // George Clinton
            {
                name: "George Clinton",
                data: [
                    {
                        x: "Vice President",
                        y: [
                            new Date(1805, 2, 4).getTime(),
                            new Date(1812, 3, 20).getTime(),
                        ],
                    },
                ],
            },
            // John Jay
            {
                name: "John Jay",
                data: [
                    {
                        x: "Secretary of State",
                        y: [
                            new Date(1789, 8, 25).getTime(),
                            new Date(1790, 2, 22).getTime(),
                        ],
                    },
                ],
            },
            // Edmund Randolph
            {
                name: "Edmund Randolph",
                data: [
                    {
                        x: "Secretary of State",
                        y: [
                            new Date(1794, 0, 2).getTime(),
                            new Date(1795, 7, 20).getTime(),
                        ],
                    },
                ],
            },
            // Timothy Pickering
            {
                name: "Timothy Pickering",
                data: [
                    {
                        x: "Secretary of State",
                        y: [
                            new Date(1795, 7, 20).getTime(),
                            new Date(1800, 4, 12).getTime(),
                        ],
                    },
                ],
            },
            // Charles Lee
            {
                name: "Charles Lee",
                data: [
                    {
                        x: "Secretary of State",
                        y: [
                            new Date(1800, 4, 13).getTime(),
                            new Date(1800, 5, 5).getTime(),
                        ],
                    },
                ],
            },
            // John Marshall
            {
                name: "John Marshall",
                data: [
                    {
                        x: "Secretary of State",
                        y: [
                            new Date(1800, 5, 13).getTime(),
                            new Date(1801, 2, 4).getTime(),
                        ],
                    },
                ],
            },
        ],
        plotOptions: {
            bar: {
                horizontal: true,
                barHeight: "35%",
                rangeBarGroupRows: true,
            },
        },
        fill: {
            type: "solid",
        },
        legend: {
            position: "right",
        },
        xaxis: {
            type: "datetime",
        },
        tooltip: {
            custom: function (opts) {
                const fromYear = new Date(opts.y1).getFullYear();
                const toYear = new Date(opts.y2).getFullYear();
                const values = opts.ctx.rangeBar.getTooltipValues(opts);

                return (
                    '<div class="apexcharts-tooltip-rangebar">' +
                    '<div> <span class="series-name" style="color: ' +
                    values.color +
                    '">' +
                    (values.seriesName ? values.seriesName : "") +
                    "</span></div>" +
                    '<div> <span class="category">' +
                    values.ylabel +
                    ' </span> <span class="value start-value">' +
                    fromYear +
                    '</span> <span class="separator">-</span> <span class="value end-value">' +
                    toYear +
                    "</span></div>" +
                    "</div>"
                );
            },
        },
        colors: chartMultiSeriesColors,
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#multipleserieschart"), options)
  		chart.render()
	})
</script>

<div id="multipleserieschart" class="apex-charts" dir="ltr"></div>
