
const stretchTextSVG = document.querySelector(".StretchTextSVG");
let ToolBarChanges = document.querySelectorAll(".ToolBarChange");
// let nuevaClase = document.querySelectorAll(".ToolBarChange");



// const JustifyTextLeftSVG = document.querySelector(".JustifyTextLeftSVG");
// const JustifyTextCenterSVG = document.querySelector(".JustifyTextCenterSVG");
// const JustifyTextRigthSVG = document.querySelector(".JustifyTextRigthSVG");
// const TextBolderSVG = document.querySelector(".TextBolderSVG");
// const TextItalicSVG = document.querySelector(".TextItalicSVG");
// const TextUnderlineSVG = document.querySelector(".TextUnderlineSVG");
// const TextStrikethroughSVG = document.querySelector(".TextStrikethroughSVG");
// export const HandleNavBar = ({ target }: any) => {
//   setActive(target.className);

// }

export const HandleNavBar2 = () => {
  if (stretchTextSVG) {
    stretchTextSVG.classList.add('nueva-clase')
  } 
}

export const HandleNavBar3 = () => {
  if ( ToolBarChanges && stretchTextSVG) {
    stretchTextSVG.classList.add('nuevaClase')
  }
}

ToolBarChanges.forEach((item) => {
  item.addEventListener('click', () =>
    item.classList.toggle('ToolBarChange')
    
  ) 
})