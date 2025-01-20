
import { TextStrikethroughSVG } from "../1-Inicio/08-TextStrikethrough/TextStrikethrough"
import { Line, Arc } from "../../index"
import "./Edit.css"

export const Edit = () => {
    return (
        <>
            <figure className="ToolBar Edit">{/*cambiar a ToolIcons */}
                <section className="ConteinerIcons">
                    <Line />
                </section>
                <section className="ContainerArc">
                    <Arc />
                </section>
                <section className="ConteinerIcons">
                    <TextStrikethroughSVG />
                </section>

            </figure>
        </>
    )
}