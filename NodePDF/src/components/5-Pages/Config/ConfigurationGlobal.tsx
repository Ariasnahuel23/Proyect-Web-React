
import { ArrowSVG,PageBreakSVG } from "../../../ComponentsSVG/index";
import "./ConfigurationGlobal.css";

export const ConfigurationGlobal = () => {
  return (
    <>
      <nav className="Nav">
        <ul className="ulNav">
          <li><a href="/">Home</a></li>
        </ul>
        <ArrowSVG />
      </nav>
      <section className="conteinerPage">
        <article className="conteinerA">
          <h1>A0</h1>
          <PageBreakSVG />
          <h1>Dimenciones</h1>
          <h6>Alto:</h6> 
          <input type="number" className="inputPage" min="0" max="10" step="1" />
          <h6>Ancho:</h6>
          <input type="number" className="inputPage" min="0" max="10" step="1" />

        </article>
       
      </section>
    </>
  )
}