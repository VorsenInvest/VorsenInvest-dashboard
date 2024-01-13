<script>
import { Link, Head } from '@inertiajs/vue3';
import Layout from "@/Layouts/main.vue";
import PageHeader from "@/Components/page-header.vue";
import { layoutComputed } from "@/state/helpers.js"
import getChartColorsArray from "@/common/getChartColorsArray";
import {
  basicColumnChart,
  columnDatalabelChart,
  stackedColumnsChart,
  columnStackedChart,
  columnMarkersChart,
  columnRotatedLabel,
  columnNegativeChart,
  rangeColumnChart,
  chartYearOption,
  quarterChartOption,
  distributedColumnchart,
  dynamicQuarterLoadedChart,
  groupedStackedChart,
  dumbbellChart
} from "./data";

/**
 * Column Charts component
 */
export default {
  data() {
    return {
      basicColumnChart: basicColumnChart,
      columnDatalabelChart: columnDatalabelChart,
      stackedColumnsChart: stackedColumnsChart,
      columnStackedChart: columnStackedChart,
      columnMarkersChart: columnMarkersChart,
      columnRotatedLabel: columnRotatedLabel,
      columnNegativeChart: columnNegativeChart,
      rangeColumnChart: rangeColumnChart,
      chartYearOption: chartYearOption,
      quarterChartOption: quarterChartOption,
      distributedColumnchart: distributedColumnchart,
      dynamicQuarterLoadedChart: dynamicQuarterLoadedChart,
      groupedStackedChart: groupedStackedChart,
      dumbbellChart: dumbbellChart,
    };
  },
  components: {
    Layout,
    PageHeader,
    Link, Head
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
        this.basicColumnChart = {
          ...this.basicColumnChart,
          chartOptions: {
            ...this.basicColumnChart.chartOptions,
            colors: getChartColorsArray('["--vz-danger", "--vz-primary", "--vz-success"]')
          }
        };
        this.columnDatalabelChart = {
          ...this.columnDatalabelChart,
          chartOptions: {
            ...this.columnDatalabelChart.chartOptions,
            colors: getChartColorsArray('["--vz-success"]')
          }
        };
        this.stackedColumnsChart = {
          ...this.stackedColumnsChart,
          chartOptions: {
            ...this.stackedColumnsChart.chartOptions,
            colors: getChartColorsArray('["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger"]')
          }
        };
        this.columnStackedChart = {
          ...this.columnStackedChart,
          chartOptions: {
            ...this.columnStackedChart.chartOptions,
            colors: getChartColorsArray('["--vz-primary", "--vz-success", "--vz-warning"]')
          }
        };
        this.groupedStackedChart = {
          ...this.groupedStackedChart,
          chartOptions: {
            ...this.groupedStackedChart.chartOptions,
            colors: getChartColorsArray('["--vz-success", "--vz-primary","--vz-secondary", "--vz-danger"]')
          }
        };
        this.columnMarkersChart = {
          ...this.columnMarkersChart,
          chartOptions: {
            ...this.columnMarkersChart.chartOptions,
            colors: getChartColorsArray('["--vz-success", "--vz-primary"]')
          }
        };
        this.columnRotatedLabel = {
          ...this.columnRotatedLabel,
          chartOptions: {
            ...this.columnRotatedLabel.chartOptions,
            colors: getChartColorsArray('["--vz-info"]')
          }
        };
        this.columnNegativeChart = {
          ...this.columnNegativeChart,
          chartOptions: {
            ...this.columnNegativeChart.chartOptions,
            colors: getChartColorsArray('["--vz-success", "--vz-primary", "--vz-warning"]')
          }
        };
        this.rangeColumnChart = {
          ...this.rangeColumnChart,
          chartOptions: {
            ...this.rangeColumnChart.chartOptions,
            colors: getChartColorsArray('["--vz-primary", "--vz-success"]')
          }
        };
        this.chartYearOption = {
          ...this.chartYearOption,
          chartOptions: {
            ...this.chartYearOption.chartOptions,
            colors: getChartColorsArray('["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-body-color", "--vz-info"]')
          }
        };
        this.dynamicQuarterLoadedChart = {
          ...this.dynamicQuarterLoadedChart,
          chartOptions: {
            ...this.dynamicQuarterLoadedChart.chartOptions,
            colors: getChartColorsArray('["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-body-color", "--vz-info"]')
          }
        };
        this.distributedColumnchart = {
          ...this.distributedColumnchart,
          chartOptions: {
            ...this.distributedColumnchart.chartOptions,
            colors: getChartColorsArray('["--vz-primary", "--vz-success", "--vz-warning", "--vz-danger", "--vz-dark", "--vz-info"]')
          }
        };
      }, 200)
    },
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

    <Head title="Column Charts" />
    <PageHeader title="Column Charts" pageTitle="Apexcharts" />
    <BRow>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Basic Column Charts</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="basicColumnChart.series"
              :options="basicColumnChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Column with Data Labels</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="columnDatalabelChart.series"
              :options="columnDatalabelChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Stacked Column Charts</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="stackedColumnsChart.series"
              :options="stackedColumnsChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Stacked Column 100</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="columnStackedChart.series"
              :options="columnStackedChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>
    <BRow>
      <BCol xl="6">
        <BCard no-body>
          <BCardHeader>
            <BCardTitle class="mb-0">Grouped Stacked Columns</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="groupedStackedChart.series"
              :options="groupedStackedChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>

      <BCol xl="6">
        <BCard no-body>
          <BCardHeader>
            <BCardTitle class="mb-0">Dumbbell Chart</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="dumbbellChart.series"
              :options="dumbbellChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>

    </BRow>
    <BRow>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Column with Markers</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="columnMarkersChart.series"
              :options="columnMarkersChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Column with Rotated Labels</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="columnRotatedLabel.series"
              :options="columnRotatedLabel.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Column with Nagetive Values</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="columnNegativeChart.series"
              :options="columnNegativeChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Range Column Chart</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <apexchart class="apex-charts" height="350" dir="ltr" :series="rangeColumnChart.series"
              :options="rangeColumnChart.chartOptions"></apexchart>
          </BCardBody>
        </BCard>
      </BCol>
    </BRow>

    <BRow>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
            <BCardTitle>Dynamic Loaded Chart</BCardTitle>
          </BCardHeader>
          <BCardBody>
            <div id="dynamicloadedchart-wrap">
              <div id="chart-year">
                <apexchart type="bar" height="330" ref="chart" :options="chartYearOption.chartOptions"
                  :series="chartYearOption.series"></apexchart>
              </div>
              <div id="chart-quarter">
                <apexchart type="bar" height="330" ref="chartQuarter" :options="dynamicQuarterLoadedChart.chartOptions"
                  :series="dynamicQuarterLoadedChart.series"></apexchart>
              </div>
            </div>
          </BCardBody>
        </BCard>
      </BCol>
      <BCol lg="6">
        <BCard no-body>
          <BCardHeader class="justify-content-between d-flex align-items-center">
          <BCardTitle>Distributed Columns Charts</BCardTitle>
        </BCardHeader>
        <BCardBody>
          <apexchart class="apex-charts" height="350" dir="ltr" :series="distributedColumnchart.series"
            :options="distributedColumnchart.chartOptions"></apexchart>
        </BCardBody>
      </BCard>
    </BCol>
  </BRow>
</Layout></template>
