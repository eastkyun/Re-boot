<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#"> <img src="https://getbootstrap.com/docs/5.1/assets/brand/bootstrap-logo.svg" alt="" width="30" height="24" />Re-Boot </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item" v-for="(item, idx) in nav_items" :key="idx">
            <a class="nav-link" :href="item[0]">{{ item[1] }}</a>
          </li>
        </ul>
        <ul class="navbar-nav mb-2 mb-lg-0">
          <li>
            <form class="d-flex">
              <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
              <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/login">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      // nav_items: [nav_href, nav_name]
      nav_items: [
        ["/", "메인화면"],
        ["rec", "부동산최저가"],
        ["bnr", "보안뉴스"],
        ["wcf", "금융클라우드"],
        ["car", "차량시세비교"],
      ],
    };
  },
};
</script>

<style></style>
