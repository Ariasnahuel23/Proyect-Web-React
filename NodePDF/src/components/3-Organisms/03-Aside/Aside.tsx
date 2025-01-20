import { ReactNode } from "react";
import "./Aside.css"

interface PropsAside {
  children?: ReactNode 
  className: string
}

export const Aside = ({ children, className }: PropsAside) => {
  return (
    <>
      <div className={className}>
        {children}
      </div>
    </>
  )
}
