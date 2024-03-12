using System;
using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Wordprocessing;
using DocumentFormat.OpenXml;

class Program
{
    static void Main(string[] args)
    {
        string inputFilePath = "input.docx";
        string outputDirectory = "output/";

        using (WordprocessingDocument doc = WordprocessingDocument.Open(inputFilePath, false))
        {
            int pageNumber = 1;

            var extendedFilePropertiesPart = doc.ExtendedFilePropertiesPart;
            if (extendedFilePropertiesPart != null)
            {
                Pages pages = extendedFilePropertiesPart.Properties.Pages;
                int totalPages = pages ?? 0; // Make sure pages is not null
                foreach (var element in doc.MainDocumentPart.Document.Body.Elements())
                {
                    if (element is Paragraph && pageNumber <= totalPages)
                    {
                        string outputFilePath = $"{outputDirectory}Page_{pageNumber}.docx";

                        using (WordprocessingDocument outputDoc = WordprocessingDocument.Create(outputFilePath, WordprocessingDocumentType.Document))
                        {
                            MainDocumentPart mainPart = outputDoc.AddMainDocumentPart();
                            mainPart.Document = new Document(new Body());
                            mainPart.Document.Body.AppendChild((OpenXmlElement)element.Clone());
                        }

                        pageNumber++;
                    }
                }
            }
        }

        Console.WriteLine("Splitting completed successfully.");
    }
}

