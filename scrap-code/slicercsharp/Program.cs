using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Spire.Doc;

namespace SplitDocument
{
    class Program
    {
        static void Main(string[] args)
        {
            Document document = new Document(); // Use '=' instead of '-' to assign a value
            document.LoadFromFile(@"./input.docx");
            Document newWord;
            for (int i = 0; i < document.Sections.Count; i++) // Use '=' instead of '-' in the for loop
            {
                newWord = new Document();
                newWord.Sections.Add(document.Sections[i].Clone());
                newWord.SaveToFile(String.Format(@"./out_{0}.docx", i)); // Use 'i' instead of '1' to have incremental file names
            }
        }
    }
}





