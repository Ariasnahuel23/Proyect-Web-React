import { ReactNode } from "react";
import { MainIcon } from "../../../ComponentsSVG";
import { MainTitle } from "../../index";
import "./Header.css"

interface PropsHeader {
    children?: ReactNode
    className?: string

}

export const Header = ({ className }: PropsHeader) => {
    return (
        <>

            <header className={className}>
                <MainTitle />
                <MainIcon />
            </header>
        </>

    )
}
