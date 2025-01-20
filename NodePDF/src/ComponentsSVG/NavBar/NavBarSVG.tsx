import { ConfigPageSVGProps } from "../../components/interface/IconSVGProps"


export const NavBarSVG = ({ fill = "var(--edit-tool-icons-color)", ...props }: ConfigPageSVGProps) => (
    <svg
      viewBox="0 0 1.12 1.12"
      xmlns="http://www.w3.org/2000/svg"
      className="IconConfigSvg NavBarSVG"
      {...props}
    >
      <path
        fill={fill}
        d="M.32.292A.03.03 0 0 1 .352.26h.656a.03.03 0 0 1 .032.032v.016a.03.03 0 0 1-.032.032H.352A.03.03 0 0 1 .32.308zm0 .56A.03.03 0 0 1 .352.82h.656a.03.03 0 0 1 .032.032v.016A.03.03 0 0 1 1.008.9H.352A.03.03 0 0 1 .32.868zm0-.28A.03.03 0 0 1 .352.54h.656a.03.03 0 0 1 .032.032v.016a.03.03 0 0 1-.032.032H.352A.03.03 0 0 1 .32.588zM.2.3a.06.06 0 1 1-.12 0A.06.06 0 0 1 .2.3m0 .56a.06.06 0 1 1-.12 0 .06.06 0 0 1 .12 0m0-.28a.06.06 0 1 1-.12 0 .06.06 0 0 1 .12 0"
      />
    </svg>
  )