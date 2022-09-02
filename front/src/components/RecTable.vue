<template>
  <div class="container">
    <h3 class="p-3 text-center">부동산 최저 가격표</h3>
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>날짜</th>
          <th>아파트명</th>
          <th>가격(최저가)</th>
          <th>평단가</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(rec, index) in rec_list" :key="index">
          <td>{{ rec.Date }}</td>
          <td>{{ rec.Name }}</td>
          <td>{{ rec.Price }}</td>
          <td>{{ rec.PerPrice }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "RecTable",
  props: {
    slice: Number,
  },
  data() {
    return {
      rec_list: { Date: "2022-08-09", Name: "빛가람혁신도시중흥S-클래스센트럴1차", Price: "3억 5,000", PerPrice: 1220 },
    };
  },
  methods: {
    fetchData: function () {
      this.axios
        .get("rec/shorts/" + this.slice + "/")
        .then((response) => {
          this.rec_list = response.data;
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  async mounted() {
    await this.fetchData();
  },
};
</script>

<style></style>
