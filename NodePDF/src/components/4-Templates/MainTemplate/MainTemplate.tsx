import { ReactNode } from "react"
import { Header, Nav, Main, Footer } from "../../3-Organisms/index";
import { NavBarSVG } from "../../../ComponentsSVG";

import "./MainTemplate.css"

interface mainTemplateProps {
  children?: ReactNode
}

export const MainTemplate = ({ }: mainTemplateProps) => {
  return (
    <>
      <section className='Banner'>
        <NavBarSVG />
        <Header className='Header' />
        <Nav className='Nav' />
      </section>      
      <Main />
      <Footer className='Footer' />

    </>
  )
}
