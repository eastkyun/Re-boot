<template>
  <div class="container mt-5">
    <div class="row">
      <div class="col-6 card">
        <h2>1. 부동산 시세 비교 일걸요</h2>
        <table id="rec">
          <tr>
            <th>아파트명</th>
            <th>가격(최저가)</th>
            <th>평단가</th>
          </tr>
          <tr>
            <td>중흥S클래스 1차</td>
            <td>3억 3천만원</td>
            <td>1200만원/평</td>
          </tr>
        </table>
      </div>
      <div class="col-6 card">
        <h2>2. 보안 뉴스 기사 추천 일거에요</h2>
      </div>
    </div>
    <div class="m-5"></div>
    <div class="row">
      <div class="col-6 card">
        <h2>3. 금융 워드 클라우드 할까요</h2>
      </div>
      <div class="col-6 card">
        <h2>4. 차량 시세 비교 할수도</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
#rec {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#rec td,
#rec th {
  border: 1px solid #ddd;
  padding: 8px;
}

#rec tr:nth-child(even) {
  background-color: #f2f2f2;
}

#rec tr:hover {
  background-color: #ddd;
}

#rec th {
  text-align: left;
  background-color: #04aa6d;
  color: white;
}
</style>
