<template>
  <div>
    <HeaderLO></HeaderLO>
    <MainPage></MainPage>
    <FooterLO></FooterLO>
  </div>
</template>

<script>
import HeaderLO from "./layout/HeaderLO.vue";
import MainPage from "./layout/MainPage.vue";
import FooterLO from "./layout/FooterLO.vue";

export default {
  name: "App",
  components: {
    HeaderLO,
    MainPage,
    FooterLO,
  },
};
</script>

<style scoped>

</style>

