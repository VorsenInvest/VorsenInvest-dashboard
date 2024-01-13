<script>
	import {onMount} from 'svelte'; 

    export let seriesData,chartsColor,id;
    
    const areachartlitecoinColors = [chartsColor];
    var options = {
        chart: {
            width: 130,
            height: 46,
            type: "area",
            sparkline: {
                enabled: true,
            },
            toolbar: {
                show: false,
            },
        },
        series : seriesData,
        dataLabels: {
            enabled: false,
        },
        stroke: {
            curve: "smooth",
            width: 1.5,
        },
        fill: {
            type: "gradient",
            gradient: {
                shadeIntensity: 1,
                inverseColors: false,
                opacityFrom: 0.45,
                opacityTo: 0.05,
                stops: [50, 100, 100, 100],
            },
        },
        colors: areachartlitecoinColors
    };
    onMount(() => {
		const chart = new ApexCharts(document.querySelector("#dashboardcryptochart"+id), options)
  		chart.render()
	})
</script>
<div id={"dashboardcryptochart" + id} class="apex-charts" dir="ltr"></div>

