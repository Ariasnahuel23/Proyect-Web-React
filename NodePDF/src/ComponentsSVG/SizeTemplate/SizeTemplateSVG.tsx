import { ConfigPageSVGProps } from "../../components/interface/IconSVGProps"

export const SizeTemplateSVG = ({ fill = "var(--edit-tool-icons-color)", ...props }: ConfigPageSVGProps) => (
  <svg
    // width={32}
    // height={32}
    viewBox="0 0 1.92 1.92"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    className="IconConfigSvg"
    {...props}
  >
    <path fill={fill} fillOpacity={0} d="M0 0h1.92v1.92H0z" />
    <path
      stroke={fill}
      strokeWidth={0.16}
      strokeLinejoin="round"
      d="M.28.16h1.36a.12.12 0 0 1 .12.12v1.36a.12.12 0 0 1-.12.12H.28a.12.12 0 0 1-.12-.12V.28A.12.12 0 0 1 .28.16z"
    />
    <path
      d="M.16.693h1.6M.693 1.76V.693"
      stroke={fill}
      strokeWidth={0.16}
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
)