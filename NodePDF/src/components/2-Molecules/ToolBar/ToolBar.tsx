import { Inicio, Edit } from "../../../ComponentsSVG/index";

import "./ToolBar.css";

interface PropsToolBar {
  className?: string
}

export const ToolBar = ({ }: PropsToolBar) => {
  return (
    <section className="ConteinerTools">
      <Inicio  />
      <Edit />
    </section>
  )
};
