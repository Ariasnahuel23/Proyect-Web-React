import { jsPDF } from "jspdf";
import React, { useState, useEffect } from "react";
import "./Layout.css";
export const PdfEditor = () => {
  const [content, setContent] = useState<string>("Escriba aquí el texto que deseas mostrar en el PDF");
  const [pdfUrl, setPdfUrl] = useState<string>("");



  // Función para generar el PDF                  
  const generatePDF = () => {
    const pdf = new jsPDF({
      orientation: "landscape", // Orientación del PDF ("landscape" o "portrait" )
      unit: "mm",
      format: "a1", // Tamaño del PDF
      // Opciones de la página

    });
    const pageWidth = pdf.internal.pageSize.getWidth();
    const pageHeight = pdf.internal.pageSize.getHeight();

    // Obtener ancho del texto
    const textWidth = pdf.getTextWidth(content);

    // Calcular posiciones para centrar
    const x = (pageWidth - textWidth) / 2; // Centro horizontal
    const y = pageHeight / 2; // Centro vertical

    // Añadir texto centrado
    pdf.text(content, x, y);

    // Crear Blob y URL para la vista previa
    const pdfBlob = pdf.output("blob");
    const pdfURL = URL.createObjectURL(pdfBlob);
    setPdfUrl(pdfURL);
  };

  // Efecto para generar el PDF cada vez que el contenido cambie
  useEffect(() => {
    generatePDF();
  }, [content]);

  // Manejar cambios en el textarea
  const handleContentChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setContent(event.target.value);
  };

  return (
    <>
      <div className="layout">
        {/* Área de texto para editar el PDF */}
        <textarea className="textEdit"
          value={content}
          onChange={handleContentChange}
        ></textarea>

        {/* Visor del PDF */}
        {pdfUrl && (
          <iframe
            className="pdfPreview"
            src={pdfUrl}
            title="PDF Preview"
          ></iframe>
        )}
      </div>
      {/* Botón para actualizar el PDF manualmente */}
      <div className="pdfOptions">
        <button className="pdfButton" onClick={generatePDF}>
          Actualizar PDF
        </button>

      </div>
    </>
  );
};