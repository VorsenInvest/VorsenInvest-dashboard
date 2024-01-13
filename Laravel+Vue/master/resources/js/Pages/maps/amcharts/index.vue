<script>
import { Link, Head } from '@inertiajs/vue3';
import Layout from "@/Layouts/main.vue";
import PageHeader from "@/Components/page-header.vue";

import basic from './basic.vue';
import lineMap from './line.vue';
import imgMap from './image.vue';
import usaMapChart from './usamap.vue';
import pacificMap from './pacific.vue';
import animationMap from "./animation.vue";

export default {
    components: { Layout, PageHeader, Link, Head, basic, lineMap, imgMap, usaMapChart, pacificMap, animationMap },

};
</script>

<template>
    <Layout>

        <Head title="Amchart Maps" />
        <PageHeader title="Amchart Maps" pageTitle="Maps" />
        <BRow>
            <BCol lg="6">
                <BCard no-body>
                    <BCardBody>
                        <BCardTitle class="fw-semibold">Pacific Map with Multicolor And Tooltip</BCardTitle>
                        <pacificMap />
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol lg="6">
                <BCard no-body>
                    <BCardBody>
                        <BCardTitle class="fw-semibold">Line with Point</BCardTitle>
                        <lineMap />
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol lg="6">
                <BCard no-body>
                    <BCardBody>
                        <BCardTitle class="fw-semibold">Animation Along Lines</BCardTitle>
                        <animationMap />
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol lg="6">
                <BCard no-body>
                    <BCardBody>
                        <BCardTitle class="fw-semibold">Point With Zoom Conrtol</BCardTitle>
                        <basic />
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol lg="6">
                <BCard no-body>
                    <BCardBody>
                        <BCardTitle class="fw-semibold">Vector Map With Image Point</BCardTitle>
                        <imgMap />
                    </BCardBody>
                </BCard>
            </BCol>
            <BCol lg="6">
                <BCard no-body>
                    <BCardBody>
                        <BCardTitle class="fw-semibold">USA Vector Map</BCardTitle>
                        <usaMapChart />
                    </BCardBody>
                </BCard>
            </BCol>
        </BRow>
    </Layout>
</template>
