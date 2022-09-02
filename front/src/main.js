import { createApp } from "vue";
import App from "./App.vue";
import "bootstrap";
import router from "./routes/index.js";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";

const app = createApp(App);
axios.defaults.baseURL = "http://localhost:8000";
app.config.globalProperties.axios = axios;
app.use(router).mount("#app");
