import React, {useState} from "react";

const searchBar = () => {
  const [searchInput, setSearchInput] = useState('');
  const [cities, setCities] = useState([
    { name: "Ulyanovsk"},
    { name: "St.Petersburg" },
    { name: "Vladivostok" },
  ]);
  const initialCities = [
    { name: "Ulyanovsk"},
    { name: "St.Petersburg" },
    { name: "Vladivostok" },
  ];

  const handleChanges = (e) => {
    e.preventDefault();
    setSearchInput(e.target.value);
    if (searchInput.length > 0) {
      setCities(cities.filter((city) => {
        return city.name.match(searchInput);
      }))
    } else {
      setCities(initialCities);
    }
  };

  return <div className='search'>
    <input type="search" placeholder="Type here" onChange={handleChanges} value={searchInput} />

    <table>
        <tr>
            <th>City</th>
        </tr>

        {cities.map((city, index) => (
            <tr key={index}>
                <td>{city.name}</td>
            </tr>
        ))}
    </table>
  </div>
};

export default searchBar;