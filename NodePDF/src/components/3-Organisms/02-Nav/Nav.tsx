import { ReactNode } from "react"

import "./Nav.css"
import { ArrowSVG } from "../../../ComponentsSVG/Arrows/ArrowSVG"
interface NavProps {
    children?: ReactNode
    className: string
}

export const Nav = ({ className }: NavProps) => {

    return (
        <>
            <nav className={className}>

                <ul className="ulNav">
                    <li className="liNav"><a href="/">Home</a></li>
                </ul>
                <ul className="ulNav">
                    <li className="liNav"><a href="/contact">Contact</a></li>
                </ul>
                <ul className="ulNav">
                    <li className="liNav"><a href="/login">Login</a></li>
                </ul>
                <ul className="ulNav">
                    <li className="liNav"><a href="/Register">Register</a></li>
                </ul>
                <ul className="ulNav">
                    <li className="liNav"><a href="/error">Errores</a></li>
                </ul>
                <ul className="ulNav">
                    <li className="liNav"><a href="/Configuration-global">Configuración</a></li>
                </ul>
                <ul className="ulNav">
                    <li className="liNav"><a href="/Sobre-nosotros">Nosotros</a></li>
                </ul>
                <ul className="ulNav">
                    <li className="liNav"><a href="/About">Tamaño de hoja</a></li>
                </ul>
                <ArrowSVG />
            </nav>



        </>

    )
}