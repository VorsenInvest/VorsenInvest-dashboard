<script>
    import {onMount} from 'svelte';

    var options = {
        chart: {
            height: 300,
            type: "pie",
        },
        series: [25, 15, 44, 55, 41, 17],
        labels: [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ],
        theme: {
            monochrome: {
                enabled: true,
                color: "#405189",
                shadeTo: "light",
                shadeIntensity: 0.6,
            },
        },

        plotOptions: {
            pie: {
                dataLabels: {
                    offset: -5,
                },
            },
        },
        title: {
            text: "Monochrome Pie",
            style: {
                fontWeight: 500,
            },
        },
        dataLabels: {
            formatter: function (val, opts) {
                var name = opts.w.globals.labels[opts.seriesIndex];
                return [name, val.toFixed(1) + "%"];
            },
            dropShadow: {
                enabled: false,
            },
        },
        legend: {
            show: false,
        },
    };
	onMount(() => {
		const chart = new ApexCharts(document.querySelector("#monochromepiechart"), options)
  		chart.render()
	})
</script>

<div id="monochromepiechart" class="apex-charts" dir="ltr"></div>
