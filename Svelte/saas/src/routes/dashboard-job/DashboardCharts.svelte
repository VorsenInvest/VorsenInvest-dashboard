<script>
    import {onMount} from 'svelte';
	  export let seriesData,colors,id;

    const options = {
    chart: {
      type: "radialBar",
      width: 105,
      sparkline: {
        enabled: true,
      },
    },
    series : [seriesData],
    dataLabels: {
      enabled: false,
    },
    plotOptions: {
      radialBar: {
        hollow: {
          margin: 0,
          size: "70%",
        },
        track: {
          margin: 1,
        },
        dataLabels: {
          show: true,
          name: {
            show: false,
          },
          value: {
            show: true,
            fontSize: "16px",
            fontWeight: 600,
            offsetY: 8,
          },
        },
      },
    },
    colors: [colors],
  };
  onMount(() => {
		const chart = new ApexCharts(document.querySelector("#total_jobs"+ id), options)
  		chart.render()
	})
</script>

<div id={"total_jobs" + id} class="apex-charts" dir="ltr"></div>