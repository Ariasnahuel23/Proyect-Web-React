import { ReactNode } from "react";

interface PropsComponeteBase {
    children?: ReactNode 
    className: string
}

export const ComponeteBase = ({ children, className }: PropsComponeteBase) => {
    return (
        <>
            <div className={className}>
                {children}
            </div>
        </>
    )
};