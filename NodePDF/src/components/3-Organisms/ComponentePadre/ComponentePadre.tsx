import { ReactNode } from "react";

interface PropsComponentePadre {
  children: ReactNode;
}

export const ComponentePadre = ({ children }: PropsComponentePadre) => {
  return (
    <div style={{backgroundColor:'red', height:'300px', zIndex:'0', position:'relative'}}>
      {children}
    </div>
  );
};
