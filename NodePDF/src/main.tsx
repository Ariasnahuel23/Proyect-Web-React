import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

import "./style/reset.css"
import "./style/style.css";


ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
