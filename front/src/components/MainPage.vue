<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-6 card">
        <h2>1. 부동산 시세 비교</h2>
        <rec-table :slice="6"></rec-table>
      </div>
      <div class="col-6 card">
        <h2>2. 보안 뉴스 기사 추천</h2>
      </div>
    </div>
    <div class="m-5"></div>
    <div class="row">
      <div class="col-6 card">
        <h2>3. 금융 워드 클라우드</h2>
      </div>
      <div class="col-6 card">
        <h2>4. 차량 시세 비교</h2>
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

<style scoped>
h2 {
  text-align: center;
  text-decoration: orange underline;
}
</style>
