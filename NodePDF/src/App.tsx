
///*@ts-ignore*/
import { Home, Contact } from "./../src/components/index"
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { ConfigurationGlobal } from "./components/5-Pages/Config/ConfigurationGlobal";


function App() {

  return (
    <>
      <BrowserRouter> 
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/login" element={<Contact />} />
          <Route path="/Register" element={<Contact />} />
          <Route path="/error" element={<Contact />} />
          <Route path="/Configuration-global" element={<ConfigurationGlobal />} />
          <Route path="/Sobre-nosotros" element={<Contact />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;

