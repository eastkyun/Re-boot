import { createApp } from "vue";
import App from "./App.vue";
import "bootstrap";
import router from "./routes/index.js";
import "bootstrap/dist/css/bootstrap.min.css";

createApp(App).use(router).mount("#app");
