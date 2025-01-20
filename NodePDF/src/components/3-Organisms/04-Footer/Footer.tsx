import { ReactNode } from "react";

interface PropsFooter {
    children?: ReactNode
    className?: string
}

export const Footer = ({ children, className }: PropsFooter) => {
    return (
        <>
            <div className={className}>
                {children}
            </div>
        </>
    )
};