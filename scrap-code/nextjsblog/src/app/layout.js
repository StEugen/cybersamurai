import './globals.css'
import { Inter } from 'next/font/google'
import Header from "./components/Header.js"


const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'My Nextjs Blog',
  description: 'Made by StEugen',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en"> 
      <body className={inter.className}>
        <Header />
        {children}
      </body>
    </html>
  )
}
