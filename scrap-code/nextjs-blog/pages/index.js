import Head from 'next/head';
import styles from '../styles/Home.module.css';
import Link from 'next/link'
import Header from '../components/Header.js'

export default function Home() {
  return (
    <div>
    <Header />
    <div className={styles.container}>
      <h1 className="title">
        <Link href='/posts/first-post'>first post</Link>
      </h1>
    </div>
    </div>
  )
}
