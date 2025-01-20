import "./Main.css";
import { ToolBar, NavToolBar, Layout, NavBar } from "../../index";

export const Main = () => {
  return (
    <main>
      <NavToolBar />
      <ToolBar />
      <Layout />
      <NavBar ></NavBar>
    </main>
  )
}
