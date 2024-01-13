<script>
    import {onMount} from 'svelte';

    var options = {
        chart: {
            width: 400,
            type: "polarArea",
        },
        series: [42, 47, 52, 58, 65],
        labels: ["Rose A", "Rose B", "Rose C", "Rose D", "Rose E"],
        fill: {
            opacity: 1,
        },
        stroke: {
            width: 1,
            colors: undefined,
        },
        yaxis: {
            show: false,
        },
        legend: {
            position: "bottom",
        },
        plotOptions: {
            polarArea: {
                rings: {
                    strokeWidth: 0,
                },
                spokes: {
                    strokeWidth: 0,
                },
            },
        },
        theme: {
            mode: "light",
            palette: "palette1",
            monochrome: {
                enabled: true,
                shadeTo: "light",
                color: "#405189",
                shadeIntensity: 0.6,
            },
        },
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#polarmonochromechart"), options)
  		chart.render()
	})
</script>

<div id="polarmonochromechart" class="apex-charts" dir="ltr"></div>
