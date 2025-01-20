import { StretchTextSVG, JustifyTextRigthSVG, JustifyTextCenterSVG, JustifyTextLeftSVG, TextBolderSVG, TextItalicSVG, TextUnderlineSVG, TextStrikethroughSVG, } from "../../../ComponentsSVG/index";
import "./Inicio.css";
export const Inicio = () => {
    
    return (
        <figure className="ToolBar Inicio">{/*cambiar a ToolIcons */}
            <section className="ConteinerIcons">
                <StretchTextSVG />
            </section>
            <section className="ConteinerIcons">
                <JustifyTextLeftSVG />
            </section>
            <section className="ConteinerIcons">
                <JustifyTextCenterSVG />
            </section>
            <section className="ConteinerIcons">
                <JustifyTextRigthSVG />
            </section>
            <section className="ConteinerIcons">
                <TextBolderSVG />
            </section>
            <section className="ConteinerIcons">
                <TextItalicSVG />
            </section>
            <section className="ConteinerIcons">
                <TextUnderlineSVG />
            </section>
            <section className="ConteinerIcons">
                <TextStrikethroughSVG />
            </section>
            <section className="ConteinerIcons">
                <TextStrikethroughSVG />
            </section>
            <section className="ConteinerIcons">
                <TextStrikethroughSVG />
            </section>
            <section className="ConteinerIcons">
                <TextStrikethroughSVG />
            </section>
            <section className="ConteinerIcons">
                <TextStrikethroughSVG />
            </section>
            <section className="ConteinerIcons">
                <TextStrikethroughSVG />
            </section>

        </figure>

    )
}