import "./Contact.css";
import "../../3-Organisms/02-Nav/Nav.css";
import { ArrowSVG } from "../../../ComponentsSVG/Arrows/ArrowSVG";
// import { HomeSVG, ContactSVG } from "../../../ComponentsSVG/index";
export const Contact = () => {
    return (
        <>
            <nav className="Nav">
                <ul className="ulNav">
                    <li><a href="/">Home</a></li>
                </ul>
                <ul className="ulNav">
                    <li><a href="/">About</a></li>
                </ul>
                <ul className="ulNav">
                    <li><a href="/contact">Contact</a></li>
                </ul>
                <ArrowSVG />
            </nav>
            <div className="NavBarContainer">
                <nav className="NavBar">
                    <h3 className="h3NavBar">NavBar</h3>
                    <section className="SectionNavBar">
                        <ul className="ulNavBar">
                            <li className="liNavBar ">
                                {/* <HomeSVG /> */}
                                <a className="IconText" href="#">Home</a>
                            </li>
                        </ul>
                        <ul className="ulNavBar">
                            <li className="liNavBar ">
                                {/* <ContactSVG /> */}
                                <a className="IconText" href="#">Producto</a>
                            </li>
                        </ul>
                        <ul className="ulNavBar">
                            <li className="liNavBar ">
                                {/* <ContactSVG /> */}
                                <a className=" IconText" href="#">Sobre nosotros</a>
                            </li>
                        </ul>
                        <ul className="ulNavBar">
                            <li className="liNavBar ">
                                {/* <ContactSVG /> */}
                                <a className="IconText" href="#">Contacto</a>
                            </li>
                        </ul>
                    </section>
                    
                </nav>
            </div>
        </>
    )
}
//codigo limpio