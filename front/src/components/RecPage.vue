<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-12 card">
        <h2>1. 부동산 시세 비교 일걸요</h2>
        <rec-table :slice="0"></rec-table>
      </div>
    </div>
  </div>
</template>

<script>
import RecTable from "./RecTable.vue";
export default {
  name: "MainPage",
  components: {
    RecTable,
  },
};
</script>

<style></style>
