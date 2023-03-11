import logo from './logo.svg';
import './App.css';
import SearchBar from './searchBar';
import EmailSubmit from './emailSubmit';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Hello world, fuckers</h1>
        <SearchBar />
        <EmailSubmit />
      </header>
    </div>
  );
}

export default App;
