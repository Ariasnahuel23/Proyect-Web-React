import { useState } from 'react';

import "./NavToolBar.css";
import "../../../ComponentsSVG/ToolBar/1-Inicio/Inicio.css";

export const NavToolBar = () => {
  const [clasesElemento, setClasesElemento] = useState("");
  // const $ = document;
  // const hola = $.querySelector("#toolActive");
  // const styleTools = $.body.style;

  const HandleTool = (e: any) => {

    // const [ToolActive, setToolActive] = useState(true);
    // document.body.style.backgroundColor = "var(--color-assent)";
    // const InicioToolActive = document.querySelector(".Inicio");

    // const ComentarioTool = document.querySelector(".comentario");
    // const ConvertirTool = document.querySelector(".convertir");
    // const VerTool = document.querySelector(".ver");
    // const PaginaTool = document.querySelector(".pagina");
    // const FormularioTool = document.querySelector(".formulario");
    // const ProtegerTool = document.querySelector(".proteger");
    // const ConteinerTools= document.querySelector(".ConteinerTools");
    // const activeTools = document.querySelector(".activeTools");

    const InicioTool = document.querySelector(".Inicio");
    const textToolBar = document.querySelectorAll(".textToolBar");
    const activeTool = document.querySelector(".activeTool");
    const editTool = document.querySelector(".Edit");
    const editarTool = document.querySelector(".editar");

    (InicioTool as HTMLElement).style.setProperty("z-index", "20");
    (InicioTool as HTMLElement).style.backgroundColor = 'var(--color-assent)';


    const clases = e.target.className;
    setClasesElemento(clases);

    


    // Agregamos un evento click a cada elemento
    textToolBar.forEach(tool => {
      tool.addEventListener("click", () => {
        // Removemos la clase "activeTool" de todos los elementos
        textToolBar.forEach(t => t.classList.remove("activeTool"));

        // Agregamos la clase "activeTool" al elemento clickeado
        tool.classList.add("activeTool");
        
      });
    });
    if (activeTool && textToolBar && (e.target.className = editarTool)) {
      (editTool as HTMLElement).style.setProperty("z-index", "20");
    } 

  }
  return (
    <div className="conteinerTextToolBar">
      <h4 onClick={HandleTool} className="textToolBar inicio">Inicio</h4>
      <h4 onClick={HandleTool} className="textToolBar editar">Editar</h4>
      <h4 onClick={HandleTool} className="textToolBar comentario">Comentario</h4>
      <h4 onClick={HandleTool} className="textToolBar convertir">Convertir</h4>
      <h4 onClick={HandleTool} className="textToolBar ver">Ver</h4>
      <h4 onClick={HandleTool} className="textToolBar pagina">Página</h4>
      <h4 onClick={HandleTool} className="textToolBar formulario">Formulario</h4>
      <h4 onClick={HandleTool} className="textToolBar proteger">Proteger</h4>
      <button onClick={HandleTool}>boton prueba</button>
      <h4 style={{ color: 'aqua', whiteSpace: 'nowrap' }}>{clasesElemento || "Haz clic en un elemento para ver sus clases."}</h4>
    </div>
  )
}


