<script>
import Layout from "@/layouts/main.vue";
import PageHeader from "@/components/page-header";
import { layoutComputed } from "@/state/helpers.js"
import getChartColorsArray from "@/common/getChartColorsArray";
import { basicRangeAreaChart, comboChart } from "./data";

/**
 * Mixed chart component
 */
export default {
  components: {
    Layout,
    PageHeader
  },
  data() {
    return {
      basicRangeAreaChart: basicRangeAreaChart,
      comboChart: comboChart,
    };
  },
  computed: {
    ...layoutComputed,
    layoutTheme() {
      return this.$store ? this.$store.state.layout.layoutTheme : {} || {};
    }
  },
  methods: {
    handleUpdate() {
      setTimeout(() => {
        this.basicRangeAreaChart = {
          ...this.basicRangeAreaChart,
          chartOptions: {
            ...this.basicRangeAreaChart.chartOptions,
            colors: getChartColorsArray('["--vz-primary"]')
          }
        };
      }, 200)
    }
  },
  mounted() {
    this.handleUpdate();
  },
  watch: {
    layoutTheme() {
      this.handleUpdate();
    },
  },
};
</script>

<template>
  <Layout>
    <PageHeader title="Range Area Charts" pageTitle="Apexcharts" />
    <BRow>
      <BCol xl="6">
        <BCard no-body>
          <BCardHeader>
            <BCardTitle class="mb-0">Basic Range Area Chart</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="basicRangeAreaChart.series"
              :options="basicRangeAreaChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>


      <BCol xl="6">
        <BCard no-body>
          <BCardHeader>
            <BCardTitle class="mb-0">Combo</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <div>
              <apexchart class="apex-charts" height="350" dir="ltr" :series="comboChart.series"
                :options="comboChart.chartOptions"></apexchart>
            </div>
          </BCardBody>
        </BCard>
      </BCol>

    </BRow>
  </Layout>
</template>