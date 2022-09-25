<template>
  <div id="body">
    <HeaderLO></HeaderLO>
    <router-view></router-view>
    <FooterLO></FooterLO>
  </div>
</template>

<script>
import HeaderLO from "./layout/HeaderLO.vue";
import FooterLO from "./layout/FooterLO.vue";

export default {
  name: "App",
  components: {
    HeaderLO,
    FooterLO,
  },
};
</script>

<style scoped></style>
