<script>
    export let chartsColor,id;
	import {afterUpdate, onMount} from 'svelte';

    const topartworkColors = [chartsColor];
        var options = {
            chart: {
                width: 80,
                height: 30,
                type: "line",
                sparkline: {
                    enabled: true,
                },
                toolbar: {
                    show: false,
                },
            },
            stroke: {
                curve: "smooth",
                width: 2.3,
            },
            series : [{ data: [25, 66, 41, 89, 63, 25, 44, 12] }],
            tooltip: {
                fixed: {
                    enabled: false
                },
                x: {
                    show: false
                },
                y: {
                    title: {
                        formatter: function (seriesName) {
                            return '';
                        }
                    }
                },
                marker: {
                    show: false
                }
            },
            colors: topartworkColors
        };
    onMount(() => {
		const chart = new ApexCharts(document.querySelector("#markercharts-" + id), options)
  		chart.render()
	})

    afterUpdate(() =>{
            console.log("called after update in TOPARTWORK chart");
    })
</script>

<div id={"markercharts-" + id} class="apex-charts" dir="ltr" />
