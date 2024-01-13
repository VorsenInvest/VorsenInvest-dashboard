<script>
import router from "@/router";
import simplebar from "simplebar-vue";
import { layoutComputed } from "@/state/helpers";

import NavBar from "@/components/nav-bar";
import Menu from "@/components/menu.vue";
import RightBar from "@/components/right-bar";
import Footer from "@/components/footer";
localStorage.setItem('hoverd', false);

/**
 * Vertical layout
 */
export default {
  components: { NavBar, RightBar, Footer, Menu, simplebar },
  data() {
    return {
      isMenuCondensed: false,
    };
  },
  computed: {
    ...layoutComputed,
  },
  created: () => {
    document.body.removeAttribute("data-layout", "horizontal");
    document.body.removeAttribute("data-topbar", "dark");
    document.body.removeAttribute("data-layout-size", "boxed");
    // this.updateSidebarSize();
  },
  methods: {
    updateSidebarSize() {
      let sidebarSize = ''
      // Check window.screen.width and update the data-sidebar-size attribute
      if (window.innerWidth < 1025) {
        this.sidebarSize = "sm";
        sidebarSize = 'sm'
      } else {
        this.sidebarSize = "lg"; // Reset sidebarSize if screen width is >= 1025
        sidebarSize = 'lg'
      }
      // Update the data-sidebar-size attribute of document.documentElement
      document.documentElement.setAttribute("data-sidebar-size", sidebarSize);
    },

    initActiveMenu() {
      if (document.documentElement.getAttribute('data-sidebar-size') === 'sm-hover') {
        localStorage.setItem('hoverd', true);
        document.documentElement.setAttribute('data-sidebar-size', 'sm-hover-active');
      } else if (document.documentElement.getAttribute('data-sidebar-size') === 'sm-hover-active') {
        localStorage.setItem('hoverd', false);
        document.documentElement.setAttribute('data-sidebar-size', 'sm-hover');
      } else {
        document.documentElement.setAttribute('data-sidebar-size', 'sm-hover');
      }
    },
    toggleMenu() {

      document.body.classList.toggle("sidebar-enable");
      if (window.screen.width >= 992) {
        // eslint-disable-next-line no-unused-vars
        router.afterEach((routeTo, routeFrom) => {
          document.body.classList.remove("sidebar-enable");
          document.body.classList.remove("vertical-collpsed");
        });
        document.body.classList.toggle("vertical-collpsed");
      } else {
        // eslint-disable-next-line no-unused-vars
        router.afterEach((routeTo, routeFrom) => {
          document.body.classList.remove("sidebar-enable");
        });
        document.body.classList.remove("vertical-collpsed");
      }
      this.isMenuCondensed = !this.isMenuCondensed;
    },
    toggleRightSidebar() {
      document.body.classList.toggle("right-bar-enabled");
    },
    hideRightSidebar() {
      document.body.classList.remove("right-bar-enabled");
    },

  },
  mounted() {
    if (localStorage.getItem('hoverd') == 'true') {
      document.documentElement.setAttribute('data-sidebar-size', 'sm-hover-active');
    }

    document.getElementById('overlay').addEventListener('click', () => {
      document.body.classList.remove('vertical-sidebar-enable');
    });
    if (window.screen.width < 1025) {
      document.documentElement.setAttribute("data-sidebar-size", "sm");
    }

    window.addEventListener("resize", () => {
      document.body.classList.remove('vertical-sidebar-enable');
      document.querySelector(".hamburger-icon").classList.add("open")
      this.updateSidebarSize()
    });

  },
  unmounted() {
    window.removeEventListener("resize", this.updateSidebarSize)
  }
};
</script>
  
<template>
  <div id="layout-wrapper">
    <NavBar />
    <div>
      <!-- ========== Left Sidebar Start ========== -->
      <!-- ========== App Menu ========== -->
      <div class="app-menu navbar-menu">
        <!-- LOGO -->
        <div class="navbar-brand-box">
          <!-- Dark Logo-->
          <router-link to="/" class="logo logo-dark">
            <span class="logo-sm">
              <img src="@/assets/images/logo-sm.png" alt="" height="22" />
            </span>
            <span class="logo-lg">
              <img src="@/assets/images/logo-dark.png" alt="" height="17" />
            </span>
          </router-link>
          <!-- Light Logo-->
          <router-link to="/" class="logo logo-light">
            <span class="logo-sm">
              <img src="@/assets/images/logo-sm.png" alt="" height="22" />
            </span>
            <span class="logo-lg">
              <img src="@/assets/images/logo-light.png" alt="" height="17" />
            </span>
          </router-link>
          <BButton size="sm" class="btn btn-sm p-0 fs-20 header-item float-end btn-vertical-sm-hover"
            id="vertical-hover" @click="initActiveMenu">
            <i class="ri-record-circle-line"></i>
          </BButton>
        </div>

        <BDropdown variant="link" class="sidebar-user m-1 rounded" toggle-class="rounded-circle" no-caret
          id="page-header-user-dropdown" menu-class="dropdown-menu-end"
          :offset="{ alignmentAxis: -14, crossAxis: 0, mainAxis: 0 }">
          <template #button-content>
            <span class="d-flex align-items-center gap-2">
              <img class="rounded header-profile-user" src="@/assets/images/users/avatar-1.jpg" alt="Header Avatar">
              <span class="text-start">
                <span class="d-block fw-medium sidebar-user-name-text">Anna Adame</span>
                <span class="d-block fs-14 sidebar-user-name-sub-text"><i
                    class="ri ri-circle-fill fs-10 text-success align-baseline"></i> <span
                    class="align-middle">Online</span></span>
              </span>
            </span>
          </template>
          <h6 class="dropdown-header">Welcome Anna!</h6>
          <router-link class="dropdown-item" to="/pages/profile"><i
              class="mdi mdi-account-circle text-muted fs-16 align-middle me-1"></i>
            <span class="align-middle"> Profile</span>
          </router-link>
          <router-link class="dropdown-item" to="/chat">
            <i class=" mdi mdi-message-text-outline text-muted fs-16 align-middle me-1"></i>
            <span class="align-middle"> Messages</span>
          </router-link>
          <router-link class="dropdown-item" to="/apps/tasks-kanban">
            <i class="mdi mdi-calendar-check-outline text-muted fs-16 align-middle me-1"></i>
            <span class="align-middle"> Taskboard</span>
          </router-link>
          <router-link class="dropdown-item" to="/pages/faqs"><i
              class="mdi mdi-lifebuoy text-muted fs-16 align-middle me-1"></i>
            <span class="align-middle"> Help</span>
          </router-link>
          <div class="dropdown-divider"></div>
          <router-link class="dropdown-item" to="/pages/profile"><i
              class="mdi mdi-wallet text-muted fs-16 align-middle me-1"></i>
            <span class="align-middle"> Balance : <b>$5971.67</b></span>
          </router-link>
          <router-link class="dropdown-item" to="/pages/profile-setting">
            <BBadge variant="success-subtle" class="bg-success-subtle text-success mt-1 float-end">New</BBadge><i
              class="mdi mdi-cog-outline text-muted fs-16 align-middle me-1"></i>
            <span class="align-middle"> Settings</span>
          </router-link>
          <router-link class="dropdown-item" to="/auth/lockscreen-basic"><i
              class="mdi mdi-lock text-muted fs-16 align-middle me-1"></i>
            <span class="align-middle"> Lock screen</span>
          </router-link>
          <router-link class="dropdown-item" to="/logout"><i
              class="mdi mdi-logout text-muted fs-16 align-middle me-1"></i>
            <span class="align-middle" data-key="t-logout"> Logout</span>
          </router-link>
        </BDropdown>

        <simplebar id="scrollbar" class="h-100" ref="scrollbar">
          <Menu></Menu>
        </simplebar>
        <div class="sidebar-background"></div>
      </div>
      <!-- Left Sidebar End -->
      <!-- Vertical Overlay-->
      <div class="vertical-overlay" id="overlay"></div>
    </div>
    <!-- ============================================================== -->
    <!-- Start Page Content here -->
    <!-- ============================================================== -->

    <div class="main-content">
      <div class="page-content">
        <!-- Start Content-->
        <BContainer fluid>
          <slot />
        </BContainer>
      </div>
      <Footer />
    </div>
    <RightBar />
  </div>
</template>